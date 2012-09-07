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
	print(b+' = array.array("d",[0])')
	print('tout.Branch("'+b+'",'+b+',"'+b+'/D")' )
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


def TightIDMuons(T):
	muons = []
	for n in range(len(T.MuonPt)):
		Pass = True
		Pass *= (T.MuonPt[n] > 40)
		Pass *= abs(T.MuonEta[n])<2.1
		Pass *= T.MuonIsGlobal[n]*T.MuonIsTracker[n]
		Pass *= (T.MuonTrackerIsoSumPT[n]/T.MuonPt[n])<0.1
		Pass *= T.MuonTrkHitsTrackerOnly[n]>=11
		Pass *= T.MuonStationMatches[n]>1
		Pass *= abs(T.MuonPrimaryVertexDXY[n])<0.2
		Pass *= T.MuonGlobalChi2[n]<10.0
		Pass *= T.MuonPixelHitCount[n]>=1
		Pass *= T.MuonGlobalTrkValidHits[n]>=1
		if (Pass):
			m = TLorentzVector()
			m.SetPtEtaPhiM(T.MuonPt[n],T.MuonEta[n],T.MuonPhi[n],0)
			muons.append(m)
	return muons


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

for n in range(N):
	t.GetEntry(n)
	if n%100==0:
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
	muons = TightIDMuons(t)

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



	tout.Fill()

fout.Write()
fout.Close()

