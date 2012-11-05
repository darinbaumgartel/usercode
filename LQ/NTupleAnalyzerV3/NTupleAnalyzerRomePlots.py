#!/afs/cern.ch/cms/slc5_amd64_gcc434/cms/cmssw/CMSSW_4_2_8/external/slc5_amd64_gcc434/bin/python

import sys
sys.argv.append( '-b True' )
from ROOT import *
import array
import math
# Input Options - file, cross-section, number of vevents
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="input root file", metavar="FILE")
parser.add_option("-b", "--batch", dest="dobatch", help="run in batch mode", metavar="BATCH")
parser.add_option("-s", "--sigma", dest="crosssection", help="specify the process cross-section", metavar="SIGMA")
parser.add_option("-n", "--ntotal", dest="ntotal", help="total number of MC events for the sample", metavar="NTOTAL")
parser.add_option("-l", "--lumi", dest="lumi", help="integrated luminosity for data taking", metavar="lumi")

(options, args) = parser.parse_args()

name = options.filename
if '/store' in name:
	name = 'root://eoscms//eos/cms'+name

startingweight = float(options.crosssection)*float(options.lumi)/float(options.ntotal)

fin = TFile.Open(name,"READ")
t = fin.Get("rootTupleTree/tree")

N = t.GetEntries()
fout = TFile.Open(name.split('/')[-1].replace('.root','_tree.root'),"RECREATE")
tout=TTree("PhysicalVariables","PhysicalVariables")

branches = ['Et_miss','Pt_muon1','Pt_muon2','Pt_jet1','Pt_jet2','Pt_ele1','Pt_ele2', 'weight_central', 'weight_pu_up', 'weight_pu_down']

for b in branches:
	# print(b+' = array.array("d",[0])')
	# print('tout.Branch("'+b+'",'+b+',"'+b+'/D")' )
	exec(b+' = array.array("d",[0])')
	exec('tout.Branch("'+b+'",'+b+',"'+b+'/D")' )

def GeomFilterCollection(collection_to_clean,good_collection,dRcut):
	output_collection = []
	for c in collection_to_clean:
		isgood = True
		for g in good_collection:
			if (c.DeltaR(g))<dRcut:
				isgood = False
		if isgood==True:
			output_collection.append(c)
	return output_collection

def TransMass(p1,p2):
	return math.sqrt( 2*p1.Pt()*p2.Pt()*(1-math.cos(p1.DeltaPhi(p2))) )

def InvMass(particles):
	output=particles
	return (p1+p2).M()

def ST(particles):
	st = 0.0
	for p in particles:
		st += p.Pt()
	return st

def PassTrigger(T,trigger_identifiers,prescale_threshold):
	for n in range(len(T.HLTInsideDatasetTriggerNames)):
		name = T.HLTInsideDatasetTriggerNames[n]
		consider_trigger=True

		for ident in trigger_identifiers:
			if ident not in name:
				consider_trigger=False
		if (consider_trigger==False) : continue

		prescale = T.HLTInsideDatasetTriggerPrescales[n]
		if prescale > prescale_threshold:
			consider_trigger=False
		if (consider_trigger==False) : continue

		decision = T.HLTInsideDatasetTriggerDecisions[n]
		if decision==True:
			return 1
	return 0	

# def MatchingGenParticle(T,recoparticle,pdgIds,motherids,maxDR):
# 	genparts = []
# 	drs = []
# 	for n in range(len(T.GenParticlePdgId)):
# 		pdg = T.GenParticlePdgId[n]
# 		if pdgid not in pdgIds:
# 			continue
# 		motherIndex = T.GenParticleMotherIndex[n]
# 		motherid = 0
# 		if motherIndex>-1:
# 			motherid = T.GenParticlePdgId[motherIndex]
# 		if motherid not in motherids:
# 			continue
# 		vgen = TLorentzVector()
# 		vgen.SetPtEtaPhiM(T.GenParticlePt[n],T.GenParticleEta[n],T.GenParticlePhi[n],0.0)
# 		genparts.append(vgen)
# 		drs.append(abs(vgen.DeltaR(recoparticle)))
# 	mindr = 99999999
# 	matchedpart =TLorentzVector()
# 	matchedpart.SetPtEtaPhiM(0,0,0,0)
# 	bestpart_ind = -1
# 	for n in range(len(genparts)):
# 		if drs[n]<mindr:
# 			bestpart_ind=n
# 	if bestpart_ind>-1:
# 		matchedpart = genparts[bestpart_ind]
# 	return matchedpart

def MuonsFromLQ(T):
	muons = []
	genmuons=[]
	recomuoninds = []
	for n in range(len(T.MuonPt)):	
		m = TLorentzVector()
		m.SetPtEtaPhiM(T.MuonPt[n],T.MuonEta[n],T.MuonPhi[n],0)
		muons.append(m)
	for n in range(len(T.GenParticlePdgId)):
		pdg = T.GenParticlePdgId[n]
		if pdg not in [13,-13]:
			continue
		motherIndex = T.GenParticleMotherIndex[n]
		motherid = 0
		if motherIndex>-1:
			motherid = T.GenParticlePdgId[motherIndex]
		if motherid not in [42,-42]:
			continue	
		m = TLorentzVector()
		m.SetPtEtaPhiM(T.GenParticlePt[n],T.GenParticleEta[n],T.GenParticlePhi[n],0.0)
		genmuons.append(m)
	
	matchedrecomuons=[]
	emptyvector = TLorentzVector()
	emptyvector.SetPtEtaPhiM(0,0,0,0)
	for g in genmuons:
		bestrecomuonind=-1
		mindr = 99999
		ind=-1
		for m in muons:
			ind+=1
			dr = abs(m.DeltaR(g))
			if dr<mindr:
				mindr =dr
				bestrecomuonind=ind
		if mindr<0.4:
			matchedrecomuons.append(muons[bestrecomuonind])
			recomuoninds.append(bestrecomuonind)
		else:
			matchedrecomuons.append(emptyvector)
			recomuoninds.append(-99)
		# print mindr, muons[bestrecomuonind].Pt(), g.Pt()
	return([genmuons,matchedrecomuons,recomuoninds])

def PrintBranchesAndExit(T):
	x = T.GetListOfBranches()
	for n in x:
		print n
	sys.exit()

def TightIDMuons(T):
	muons = []
	muoninds = []
	for n in range(len(T.MuonPt)):
		Pass = True
		Pass *= (T.MuonPt[n] > 45)
		Pass *= abs(T.MuonEta[n])<2.1
		Pass *= T.MuonIsGlobal[n]
		Pass *= T.MuonIsPF[n]
		Pass *= T.MuonBestTrackVtxDistXY[n] < 0.2
		Pass *= T.MuonBestTrackVtxDistZ[n] < 0.5
		Pass *= (T.MuonTrackerIsoSumPT[n]/T.MuonPt[n])<0.1
		# Pass *= T.MuonTrkHitsTrackerOnly[n]>=11 // old !!
		Pass *= T.MuonStationMatches[n]>1
		# Pass *= abs(T.MuonPrimaryVertexDXY[n])<0.2 //old !!
		Pass *= T.MuonGlobalChi2[n]<10.0
		Pass *= T.MuonPixelHits[n]>=1
		Pass *= T.MuonGlobalTrkValidHits[n]>=1
		Pass *= T.MuonTrackLayersWithMeasurement[n] > 5
		if (Pass):
			m = TLorentzVector()
			m.SetPtEtaPhiM(T.MuonPt[n],T.MuonEta[n],T.MuonPhi[n],0)
			muons.append(m)
			muoninds.append(n)
	return [muons,muoninds]


def LooseIDJets(T):
	jets=[]
	for n in range(len(T.PFJetPt)):
		if T.PFJetPt[n]>40 and abs(T.PFJetEta[n])<2.4 and T.PFJetPassLooseID[n]==1:
			j = TLorentzVector()
			j.SetPtEtaPhiM(T.PFJetPt[n],T.PFJetEta[n],T.PFJetPhi[n],0)
			jets.append(j)
	return jets

def GetPUWeight(T,version):
	if T.isData:
		return 1.0
	N_pu = 0
	for n in range(len(T.PileUpInteractions)):
		if abs(T.PileUpOriginBX[n]==0):
			N_pu = int(1.0*(T.PileUpInteractions[n]))

	puweight = 0
	CentralWeights = [0.0136759963465, 0.145092627325, 0.337346053675, 0.603889700177, 0.875723164145, 1.09904167986, 1.25430629491, 
                     1.34642557836, 1.39979322363, 1.43532953354, 1.47049703593, 1.51604545424, 1.57633567564, 1.64932013381, 
                     1.74029438919, 1.83791180719, 1.94039579764, 2.04245281118, 2.13680461818, 2.22395017393, 2.29776136337, 
                     2.34107958833, 2.37047306281, 2.38365361416, 2.37251953266, 2.33390734715, 2.28287109918, 2.18527775378, 
                     2.09984989719, 2.02417217124, 1.89559469244, 1.73994553659, 1.60146781888, 1.5415176127, 1.38880554853]
	UpperWeights =   [0.00924647898767, 0.103765308587, 0.254901026276, 0.480371942144, 0.729944556297, 0.954968986548, 1.13004026908, 
                     1.25116215302, 1.3354960398, 1.40112202125, 1.46629994308, 1.54467848996, 1.64461047702, 1.7680582782, 
                     1.9248181748, 2.10637260323, 2.31374222506, 2.54319600245, 2.78724430301, 3.04707340275, 3.31429303739, 
                     3.56161966349, 3.80974218256, 4.05230970884, 4.27119855299, 4.45358283315, 4.6210083076, 4.69553893978, 
                     4.79226541944, 4.90898557824, 4.88722270965, 4.77074865948, 4.67125617297, 4.78457737387, 4.58784771674,]
	LowerWeights =   [0.0201084522235, 0.201872953791, 0.444291440305, 0.754784951423, 1.04300038865, 1.25373948702, 1.37815071794, 
                     1.43249643277, 1.44824842983, 1.44760397441, 1.44595859288, 1.45056585209, 1.46233900245, 1.47682664198, 
                     1.49703207679, 1.51206676472, 1.52066555932, 1.51950731213, 1.50475499659, 1.47887521537, 1.43996103898, 
                     1.38034035275, 1.31320230704, 1.2392809902, 1.15650697488, 1.06581520421, 0.975973223375, 0.874112959041, 
                     0.785480306938, 0.707777917329, 0.619354107892, 0.531056657066, 0.456479768112, 0.410264344317, 0.345060491391]

	puweights = CentralWeights
	if version=='SysUp':
		puweights=UpperWeights
	if version=='SysDown':
		puweights=LowerWeights

	NRange = range(len(puweights))
	if N_pu in NRange:
		puweight=puweights[N_pu]


	return puweight

totalmuons = 0
totalmuonspass = 0

totalevents=0
totaleventspass2l2j=0
eventspass2l2jpasstrigger = 0
allpasstrigger = 0
passidleadmu = 0
allleadmu = 0
passidsecondmu = 0
allsecondmu=0

for n in range(N):
	t.GetEntry(n)
	# if n > 100: 
	# 	break
	if n%1000==0:
		print n, 'of', N

	# Assign Weights
	weight_central[0] = startingweight*GetPUWeight(t,'Central')
	weight_pu_down[0] = startingweight*GetPUWeight(t,'SysDown')
	weight_pu_up[0] = startingweight*GetPUWeight(t,'SysUp')

	### Select Particles
	
	# MET as a vector
	met = TLorentzVector()
	met.SetPtEtaPhiM(t.PFMET[0],0,t.PFMETPhi[0],0)

	# ID Muons
	[muons,goodmuoninds] = TightIDMuons(t)

	# ID Jets and filter from muons
	jets = LooseIDJets(t)
	jets = GeomFilterCollection(jets,muons,0.3)



	### Fill Output Trees

	for x in [Pt_muon1,Pt_muon2,Pt_jet1,Pt_jet2]:
		x[0]=-1

	if len(muons)>=1:
		Pt_muon1[0]=muons[0].Pt()

	if len(muons)>=2:
		Pt_muon2[0]=muons[1].Pt()

	if len(jets)>=1:
		Pt_jet1[0]=jets[0].Pt()

	if len(jets)>=2:
		Pt_jet2[0]=jets[1].Pt()


	Et_miss[0] = met.Pt()

	trigger_pass = PassTrigger(t,["HLT_Mu40_eta2p1_v"],1)
	allpasstrigger += trigger_pass
	totalevents+=1
	if (len(muons)>=2 and len(jets)>=2):
		totaleventspass2l2j+=1
		eventspass2l2jpasstrigger += trigger_pass

	totalmuons += 2*(len(t.MuonPt)>1)
	for mu in muons:
		totalmuonspass += 1

	# PrintBranchesAndExit(t)

	[genmuvec,recomuvec,recoinds]=MuonsFromLQ(t)
	if (len(genmuvec)>0) : allleadmu +=1 
	if (len(genmuvec)>1) : allsecondmu +=1 

	if (len(recomuvec)>0):
		if recoinds[0] in goodmuoninds:
			passidleadmu += 1

	if (len(recomuvec)>1):
		if recoinds[1] in goodmuoninds:
			passidsecondmu += 1			

	# print len(genmuvec),len(recomuvec)
	tout.Fill()

fout.Write()
fout.Close()

print "STATS:",totalevents,totaleventspass2l2j,eventspass2l2jpasstrigger,allpasstrigger,allleadmu,passidleadmu,allsecondmu,passidsecondmu
print (1.0*totaleventspass2l2j)/(1.0*totalevents)