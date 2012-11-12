#!/usr/bin/python
from datetime import datetime
import sys
sys.argv.append( '-b True' )
from ROOT import *
import array
import math
from optparse import OptionParser
startTime = datetime.now()
tRand = TRandom3()


##########################################################################################
#################      SETUP OPTIONS - File, Normalization, etc    #######################
##########################################################################################

# Input Options - file, cross-section, number of vevents
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="input root file", metavar="FILE")
parser.add_option("-b", "--batch", dest="dobatch", help="run in batch mode", metavar="BATCH")
parser.add_option("-s", "--sigma", dest="crosssection", help="specify the process cross-section", metavar="SIGMA")
parser.add_option("-n", "--ntotal", dest="ntotal", help="total number of MC events for the sample", metavar="NTOTAL")
parser.add_option("-l", "--lumi", dest="lumi", help="integrated luminosity for data taking", metavar="LUMI")
parser.add_option("-p", "--pileup", dest="pileup", help="path to the pileup input histogram root file", metavar="PILEUP")
(options, args) = parser.parse_args()

# Here we get the file name, and adjust it accordingly for EOS, castor, or local directory
name = options.filename
if '/store' in name:
	name = 'root://eoscms//eos/cms'+name
if '/castor/cern.ch' in name:
	name = 'rfio://'+name

# Typical event weight, sigma*lumi/Ngenerated
startingweight = float(options.crosssection)*float(options.lumi)/float(options.ntotal)

# Get the file, tree, and number of entries
fin = TFile.Open(name,"READ")
t = fin.Get("rootTupleTree/tree")
N = t.GetEntries()

# Create the output file and tree "PhysicalVariables"
fout = TFile.Open(name.split('/')[-1].replace('.root','_tree.root'),"RECREATE")
tout=TTree("PhysicalVariables","PhysicalVariables")



##########################################################################################
#################      PREPARE THE VARIABLES FOR THE OUTPUT TREE   #######################
##########################################################################################

# Branches will be created as follows: One branch for each kinematic variable for each 
# systematic variation determined in _variations. One branch for each weight and flag.
# So branch names will include weight_central, run_number, Pt_muon1, Pt_muon1MESUP, etc.

_kinematicvariables = ['Pt_muon1','Pt_muon2','Pt_ele1','Pt_ele2','Pt_jet1','Pt_jet2','Pt_miss']
_kinematicvariables += ['Eta_muon1','Eta_muon2','Eta_ele1','Eta_ele2','Eta_jet1','Eta_jet2','Eta_miss']
_kinematicvariables += ['Phi_muon1','Phi_muon2','Phi_ele1','Phi_ele2','Phi_jet1','Phi_jet2','Phi_miss']
_kinematicvariables += ['St_uujj','St_uvjj']
_kinematicvariables += ['St_eejj','St_evjj']
_kinematicvariables += ['M_uujj1','M_uujj2','MT_uvjj1','MT_uvjj2','M_uvjj','MT_uvjj']
_kinematicvariables += ['M_eejj1','M_eejj2','MT_evjj1','MT_evjj2','M_evjj','MT_evjj']
_kinematicvariables += ['JetCount','MuonCount','ElectronCount']
_weights = ['weight_central', 'weight_pu_up', 'weight_pu_down']
_flags = ['run_number','event_number','lumi_number','pass_HLTMu40_eta2p1']
_variations = ['','JESup','JESdown','MESup','MESdown','EESup','EESdown','JER','MER','EER']


def GetPDFWeightVars(T):
	# Pupose: Determine all the branch names needed to store the PDFWeights 
	#         for CTEQ, MSTW, and NNPDF in flat (non vector) form. 
	if T.isData:
		return []
	else:
		T.GetEntry(1)
		pdfweights=[]
		for x in range(len(T.PDFCTEQWeights)):
			pdfweights.append('factor_cteq_'+str(x+1))
		for x in range(len(T.PDFMSTWWeights)):
			pdfweights.append('factor_mstw_'+str(x+1))		
		for x in range(len(T.PDFNNPDFWeights)):
			pdfweights.append('factor_nnpdf_'+str(x+1))			
		return pdfweights

# Use the above function to get the pdfweights
_pdfweights = GetPDFWeightVars(t)

# _pdfLHS will store the lefthand side of an equation to cast all pdfweights
#  into their appropriate branches
_pdfLHS = '['

# Below all the branches are created, everything is a double except for flags
for b in _kinematicvariables:
	for v in _variations:
		exec(b+v+' = array.array("d",[0])')
		exec('tout.Branch("'+b+v+'",'+b+v+',"'+b+v+'/D")' )
for b in _weights:
	exec(b+' = array.array("d",[0])')
	exec('tout.Branch("'+b+'",'+b+',"'+b+'/D")' )
for b in _pdfweights:
	exec(b+' = array.array("d",[0])')
	exec('tout.Branch("'+b+'",'+b+',"'+b+'/D")' )
	_pdfLHS += (b+'[0],')
for b in _flags:
	exec(b+' = array.array("d",[0])')
	exec('tout.Branch("'+b+'",'+b+',"'+b+'/I")' )

_pdfLHS +=']' 
_pdfLHS = _pdfLHS.replace(',]',']')


##########################################################################################
#################           SPECIAL FUNCTIONS FOR ANALYSIS         #######################
##########################################################################################

def PrintBranchesAndExit(T):
	# Pupose: Just list the branches on the input file and bail out. 
	#         For coding and debugging
	x = T.GetListOfBranches()
	for n in x:
		print n
	sys.exit()

# PrintBranchesAndExit(t)

def GeomFilterCollection(collection_to_clean,good_collection,dRcut):
	# Pupose: Take a collection of TLorentzVectors that you want to clean (arg 1)
	#         by removing all objects within dR of dRcut (arg 3) of any element in
	#         the collection of other particles (arg 2)
	#         e.g.  argumments (jets,muons,0.3) gets rid of jets within 0.3 of muons. 
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
	# Pupose: Simple calculation of transverse mass between two TLorentzVectors
	return math.sqrt( 2*p1.Pt()*p2.Pt()*(1-math.cos(p1.DeltaPhi(p2))) )

def InvMass(particles):
	# Pupose: Simple calculation of invariant mass between two TLorentzVectors	
	output=particles
	return (p1+p2).M()

def ST(particles):
	# Pupose: Calculation of the scalar sum of PT of a set of TLorentzVectors	
	st = 0.0
	for p in particles:
		st += p.Pt()
	return st

def PassTrigger(T,trigger_identifiers,prescale_threshold):
	# Pupose: Return a flag (1 or 0) to indicate whether the event passes any trigger
	#         which is syntatically matched to a set of strings trigger_identifiers,
	#         considering only triggers with a prescale <= the prescale threshold.	
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

def GetPUWeight(T,version):
	# Pupose: Get the pileup weight for an event. Version can indicate the central
	#         weight, or the Upper or Lower systematics. Needs to be updated for
	#         input PU histograms given only the generated disribution........	
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

def FillPDFWeights(T):
	# Pupose: Given the _pdfLHS stored at the begging when branches were created,
	#         this function will set all PDFweights in the event. 	
	_allweights = []
	_allweights += T.PDFCTEQWeights
	_allweights += T.PDFNNPDFWeights
	_allweights += T.PDFMSTWWeights
	return (_pdfLHS+' = '+str(_allweights))


def MuonsFromLQ(T):
	# Pupose: Testing. Get the muons from LQ decays and find the matching reco muons. 
	#         Return TLorentzVectors of the gen and reco muons, and the indices for
	#         the recomuons as well.
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


def PropagatePTChangeToMET(met,original_object,varied_object):
	# Pupose: This takes an input TLorentzVector met representing the missing ET
	#         (no eta component), and an original object (arg 2), which has been
	#         kinmatically modified for a systematic (arg 3), and modifies the 
	#         met to compensate for the change in the object.
	return  met + varied_object - original_object


def TightIDMuons(T,met,variation):
	# Pupose: Gets the collection of muons passing tight muon ID. 
	#         Returns muons as TLorentzVectors, and indices corrresponding
	#         to the surviving muons of the muon collection. 
	#         Also returns modified MET for systematic variations.
	muons = []
	muoninds = []
	if variation=='MESup':	
		_MuonPt = [pt*1.01 for pt in T.MuonPt]
	elif variation=='MESdown':	
		_MuonPt = [pt*0.99 for pt in T.MuonPt]
	elif variation=='MER':	
		_MuonPt = [pt+pt*tRand.Gaus(0.0,0.04) for pt in T.MuonPt]
	else:	
		_MuonPt = [pt for pt in T.MuonPt]	

	for n in range(len(_MuonPt)):
		Pass = True
		Pass *= (T.MuonPt[n] > 20)
		Pass *= abs(T.MuonEta[n])<2.1
		Pass *= T.MuonIsGlobal[n]
		Pass *= T.MuonIsPF[n]
		Pass *= T.MuonBestTrackVtxDistXY[n] < 0.2
		Pass *= T.MuonBestTrackVtxDistZ[n] < 0.5
		Pass *= (T.MuonTrackerIsoSumPT[n]/_MuonPt[n])<0.1
		# Pass *= T.MuonTrkHitsTrackerOnly[n]>=11 // old !!
		Pass *= T.MuonStationMatches[n]>1
		# Pass *= abs(T.MuonPrimaryVertexDXY[n])<0.2 //old !!
		Pass *= T.MuonGlobalChi2[n]<10.0
		Pass *= T.MuonPixelHits[n]>=1
		Pass *= T.MuonGlobalTrkValidHits[n]>=1
		Pass *= T.MuonTrackLayersWithMeasurement[n] > 5

		if (Pass):
			NewMu = TLorentzVector()
			OldMu = TLorentzVector()
			NewMu.SetPtEtaPhiM(_MuonPt[n],T.MuonEta[n],T.MuonPhi[n],0)
			OldMu.SetPtEtaPhiM(T.MuonPt[n],T.MuonEta[n],T.MuonPhi[n],0)
			met = PropagatePTChangeToMET(met,OldMu,NewMu)

		Pass *= (_MuonPt[n] > 45)
		if (Pass):
			muons.append(NewMu)
			muoninds.append(n)
	return [muons,muoninds,met]

def HEEPElectrons(T,met,variation):
	# Pupose: Gets the collection of electrons passing HEEP ID. 
	#         Returns electrons as TLorentzVectors, and indices corrresponding
	#         to the surviving electrons of the electron collection. 
	#         Also returns modified MET for systematic variations.	
	electrons = []
	electroninds = []
	if variation=='EESup':	
		_ElectronPt = [pt*1.01 for pt in T.ElectronPtHeep]
	elif variation=='EESdown':	
		_ElectronPt = [pt*0.99 for pt in T.ElectronPtHeep]
	elif variation=='EER':	
		_ElectronPt = [pt+pt*tRand.Gaus(0.0,0.04) for pt in T.ElectronPtHeep]
	else:	
		_ElectronPt = [pt for pt in T.ElectronPtHeep]	

	for n in range(len(_ElectronPt)):
		Pass = True
		Pass *= (T.ElectronPtHeep[n] > 20)
		Pass *= abs(T.ElectronEta[n])<2.1

		barrel = (abs(T.ElectronEta[n]))<1.442
		endcap = (abs(T.ElectronEta[n]))>1.56 
		Pass *= (barrel+endcap)

		if barrel:
			Pass *= T.ElectronHasEcalDrivenSeed[n]
			Pass *= T.ElectronDeltaEtaTrkSC[n] < 0.005
			Pass *= T.ElectronDeltaPhiTrkSC[n] < 0.06
			Pass *= T.ElectronHoE[n] < 0.05
			# Pass *= T.ElectronSigmaIEtaIEta[n] < 0.03
			Pass *= ((T.ElectronE2x5OverE5x5[n] > 0.94) or (T.ElectronE1x5OverE5x5[n] > 0.83) )
			# I HAVE NO IDEA IF THESE ARE THE RIGHT VARIABLES BELOW
			Pass *= T.ElectronHcalIsoD1DR03[n] <  (2.0 + 0.03*_ElectronPt[n] + 0.28*T.rhoForHEEP)
			Pass *= T.ElectronEcalIsoDR03 < 5.0
			Pass *= T.ElectronMissingHits[n] <=1
			Pass *= T.ElectronLeadVtxDistXY<0.02

		if endcap:
			Pass *= T.ElectronHasEcalDrivenSeed[n]
			Pass *= T.ElectronDeltaEtaTrkSC[n] < 0.007
			Pass *= T.ElectronDeltaPhiTrkSC[n] < 0.06
			Pass *= T.ElectronHoE[n] < 0.05
			Pass *= T.ElectronSigmaIEtaIEta[n] < 0.03
			# Pass *= (T.ElectronE2x5OverE5x5[n] > 0.94) or (T.ElectronE1x5OverE5x5[n] > 0.83) 
			# I HAVE NO IDEA IF THESE ARE THE RIGHT VARIABLES BELOW
			if _ElectronPt[n]<50:
				Pass *= (T.ElectronHcalIsoD1DR03[n] < (2.5 + 0.28*T.rhoForHEEP))
			else:
				Pass *= (T.ElectronHcalIsoD1DR03[n] < (2.5 + 0.03*(_ElectronPt[n]-50.0) + 0.28*T.rhoForHEEP))
			Pass *= T.ElectronEcalIsoDR03 < 5.0
			Pass *= T.ElectronMissingHits[n] <=1
			Pass *= T.ElectronLeadVtxDistXY<0.05

		if (Pass):
			NewEl = TLorentzVector()
			OldEl = TLorentzVector()
			NewEl.SetPtEtaPhiM(_ElectronPt[n],T.ElectronEta[n],T.ElectronPhi[n],0)
			OldEl.SetPtEtaPhiM(T.ElectronPtHeep[n],T.ElectronEta[n],T.ElectronPhi[n],0)
			met = PropagatePTChangeToMET(met,OldEl,NewEl)

		Pass *= (_ElectronPt[n] > 45)
		if (Pass):
			electrons.append(NewEl)
			electroninds.append(n)
	return [electrons,electroninds,met]

def JERModifiedPt(pt,eta,phi,T):
	# Pupose: Dummy function for the moment. Input is pt/eta/phi of a jet. 
	#         The jet will be matched to a gen jet, and the difference
	#         between reco and gen will be modified according to appropriate
	#         pt/eta dependent scale factors (STILL NEEDED). 
	#         The modified jet PT is returned.
	bestn = -1
	bestdpt = 0
	bestdR = 9999999.9
	jet = TLorentzVector()
	jet.SetPtEtaPhiM(pt,eta,phi,0.0)
	for n in range(len(T.GenJetPt)):
		gjet = TLorentzVector()
		gjet.SetPtEtaPhiM(T.GenJetPt[n],T.GenJetEta[n],T.GenJetPhi[n],0.0)
		dR = abs(jet.DeltaR(gjet))
		if dR<bestdR:
			bestdR = dR
			bestn = n
			bestdpt = pt-gjet.Pt()

	if bestdR>0.5:
		return pt

	adjustmentfactor = 0.1
	ptadjustment = adjustmentfactor*bestdpt
	pt += ptadjustment
	return pt

def LooseIDJets(T,met,variation):
	# Pupose: Gets the collection of jets passing loose PFJet ID. 
	#         Returns jets as TLorentzVectors, and indices corrresponding
	#         to the surviving jetss of the jet collection. 
	#         Also returns modified MET for systematic variations.	

	if variation=='JESup':	
		_PFJetPt = [ T.PFJetPt[n]*(1.0+T.PFJetJECUnc[n]) for n in range(len(T.PFJetPt))]
	elif variation=='JESdown':	
		_PFJetPt = [ T.PFJetPt[n]*(1.0-T.PFJetJECUnc[n]) for n in range(len(T.PFJetPt))]
	elif variation=='JER':	
		_PFJetPt = [JERModifiedPt(T.PFJetPt[n],T.PFJetEta[n],T.PFJetPhi[n],T) for n in range(len(T.PFJetPt))] 
	else:	
		_PFJetPt = [pt for pt in T.PFJetPt]	

	jets=[]
	jetinds = []
	for n in range(len(_PFJetPt)):
		if _PFJetPt[n]>40 and abs(T.PFJetEta[n])<2.4 and T.PFJetPassLooseID[n]==1:
			j = TLorentzVector()
			j.SetPtEtaPhiM(_PFJetPt[n],T.PFJetEta[n],T.PFJetPhi[n],0)
			jets.append(j)
			jetinds.append(n)
	return [jets,jetinds,met]

def MetVector(T):
	# Purpose: Creates a TLorentzVector represting the MET. No pseudorapidith, obviously.
	met = TLorentzVector()
	met.SetPtEtaPhiM(T.PFMET[0],0,T.PFMETPhi[0],0)
	return met

def GetLLJJMasses(l1,l2,j1,j2):
	# Pupose: For LLJJ channels, this function returns two L-J Masses, corresponding to the
	#         pair of L-Js which minimizes the difference between LQ masses in the event
	m11 = (l1+j1).M()
	m12 = (l1+j2).M()
	m21 = (l2+j1).M()
	m22 = (l2+j2).M()
	diff1 = abs(m21-m12)
	diff2 = abs(m11-m22)
	if diff1 < diff2:
		pair =  [m21,m12]
	else:
		pair = [m11,m22]
	pair.sort()
	pair.reverse()
	return pair

def GetLVJJMasses(l1,met,j1,j2):
	# Pupose: For LVJJ channels, this function returns two L-J Masses, and an LJ mass and mT, 
	#         Quantities corresponding to the pair of L-Js which minimizes the difference 
	#         between LQ masses in the event
	m11 = (l1+j1).M()
	m12 = (l1+j2).M()
	mt11 = TransMass(l1,j1)
	mt12 = TransMass(l1,j2)
	mte1 = TransMass(met,j1)
	mte2 = TransMass(met,j2)	
	diff1 = abs(mte1-mt12)
	diff2 = abs(mt11-mte2)
	if diff1 < diff2:
		pair =  [mte1,mt12]
		pairwithinv = [m12,mte1]
	else:
		pair = [mt11,mte2]
		invmass = m11
		pairwithinv = [m11,mte2]
	pair.sort()
	pair.reverse()
	
	return [pair,pairwithinv]


##########################################################################################
###########      FULL CALCULATION OF ALL VARIABLES, REPEATED FOR EACH SYS   ##############
##########################################################################################

def FullKinematicCalculation(T,variation):
	# Pupose: This is the magic function which calculates all kinmatic quantities using
	#         the previous functions. It returns them as a simple list of doubles. 
	#         It will be used in the loop over events. The 'variation' argument is passed
	#         along when getting the sets of leptons and jets, so the kinematics will vary.
	#         This function is repeated for all the sytematic variations inside the event
	#         loop. The return arguments ABSOLUELY MUST be in the same order they are 
	#         listed in the branch declarations. Modify with caution.  

	# MET as a vector
	met = MetVector(T)
	# ID Muons
	[muons,goodmuoninds,met] = TightIDMuons(T,met,variation)
	[electrons,electroninds,met] = HEEPElectrons(T,met,variation)
	# ID Jets and filter from muons
	[jets,jetinds,met] = LooseIDJets(T,met,variation)
	jets = GeomFilterCollection(jets,muons,0.3)
	jets = GeomFilterCollection(jets,electrons,0.3)
	# Empty lorenz vector for bookkeeping
	EmptyLorentz = TLorentzVector()
	EmptyLorentz.SetPtEtaPhiM(.01,0,0,0)

	# Muon and Jet Counts
	_mucount = len(muons)
	_elcount = len(electrons)
	_jetcount = len(jets)

	# Make sure there are two of every object, even if zero
	if len(muons) < 1 : muons.append(EmptyLorentz)
	if len(muons) < 2 : muons.append(EmptyLorentz)
	if len(electrons) < 1 : electrons.append(EmptyLorentz)
	if len(electrons) < 2 : electrons.append(EmptyLorentz)	
	if len(jets) < 1 : jets.append(EmptyLorentz)
	if len(jets) < 2 : jets.append(EmptyLorentz)

	# Get kinmetic quantities
	[_ptmu1,_etamu1,_phimu1] = [muons[0].Pt(),muons[0].Eta(),muons[0].Phi()]
	[_ptmu2,_etamu2,_phimu2] = [muons[1].Pt(),muons[1].Eta(),muons[1].Phi()]
	[_ptel1,_etael1,_phiel1] = [electrons[0].Pt(),electrons[0].Eta(),electrons[0].Phi()]
	[_ptel2,_etael2,_phiel2] = [electrons[1].Pt(),electrons[1].Eta(),electrons[1].Phi()]
	[_ptj1,_etaj1,_phij1]    = [jets[0].Pt(),jets[0].Eta(),jets[0].Phi()]
	[_ptj2,_etaj2,_phij2]    = [jets[1].Pt(),jets[1].Eta(),jets[1].Phi()]
	[_ptmet,_etamet,_phimet] = [met.Pt(),0,met.Phi()]

	_stuujj = ST([muons[0],muons[1],jets[0],jets[1]])
	_stuvjj = ST([muons[0],met,jets[0],jets[1]])

	_steejj = ST([electrons[0],electrons[1],jets[0],jets[1]])
	_stevjj = ST([electrons[0],met,jets[0],jets[1]])

	[_Muujj1, _Muujj2] = GetLLJJMasses(muons[0],muons[1],jets[0],jets[1])
	[[_MTuvjj1, _MTuvjj2], [_Muvjj, _MTuvjj]] = GetLVJJMasses(muons[0],met,jets[0],jets[1])

	[_Meejj1, _Meejj2] = GetLLJJMasses(electrons[0],electrons[1],jets[0],jets[1])
	[[_MTevjj1, _MTevjj2], [_Mevjj, _MTevjj]] = GetLVJJMasses(electrons[0],met,jets[0],jets[1])

	# This MUST have the same structure as _kinematic variables!
	toreturn = [_ptmu1,_ptmu2,_ptel1,_ptel2,_ptj1,_ptj2,_ptmet]
	toreturn += [_etamu1,_etamu2,_etael1,_etael2,_etaj1,_etaj2,_etamet]
	toreturn += [_phimu1,_phimu2,_phiel1,_phiel2,_phij1,_phij2,_phimet]
	toreturn += [_stuujj,_stuvjj]
	toreturn += [_steejj,_stevjj]
	toreturn += [_Muujj1, _Muujj2]
	toreturn += [_MTuvjj1, _MTuvjj2,_Muvjj, _MTuvjj]
	toreturn += [_Meejj1, _Meejj2]
	toreturn += [_MTevjj1, _MTevjj2,_Mevjj, _MTevjj]	
	toreturn += [_jetcount,_mucount,_elcount]
	return toreturn



##########################################################################################
#################    BELOW IS THE ACTUAL LOOP OVER ENTRIES         #######################
##########################################################################################

# Please don't edit here. It is static. The kinematic calulations are the only thing to edit!

for n in range(N):

	# This is the loop over events. Due to the heavy use of functions and automation of 
	# systematic variations, this loop is very small. It should not really be editted, 
	# except possibly to add a new flag or weight variable. 
	# All editable contents concerning kinematics are in the function defs.

	# Get the entry
	t.GetEntry(n)
	if n > 100:  # Testing....
		break
	if n%1000==0:
		print 'Procesing event',n, 'of', N # where we are in the loop...

	## ===========================  BASIC SETUP  ============================= ##

	# Assign Weights
	weight_central[0] = startingweight*GetPUWeight(t,'Central')
	weight_pu_down[0] = startingweight*GetPUWeight(t,'SysDown')
	weight_pu_up[0] = startingweight*GetPUWeight(t,'SysUp')
	exec(FillPDFWeights(t))
	
	# Event Flags
	run_number   = t.run
	event_number = t.event
	lumi_number  = t.ls
	pass_HLTMu40_eta2p1[0] = PassTrigger(t,["HLT_Mu40_eta2p1_v"],1)


	## ===========================  Calculate everything!  ============================= ##

	# Looping over systematic variations
	for v in _variations:
		# All calucations are done here
		calculations = FullKinematicCalculation(t,v)
		# Now cleverly cast the variables
		for b in range(len(_kinematicvariables)):
			exec(_kinematicvariables[b]+v+'[0] = calculations['+str(b)+']')


	## ===========================     Skim out events     ============================= ##

	# Feel like skimming? Do it here. The syntax is just {branchname}[0] > blah, or whatever condition
	# you want to impose. The [0] is because pyroot passes everything as an array of length 1.
	# BE MINDFUL: Just because the central (non-systematic) quantity meets the skim, does not mean 
	# that the systematic varied quantity will, and that will throw off systematics calculations later.
	# Make sure your skim is looser than any selection you will need afterward!
	if (St_uujj[0] < 200) and (St_uvjj[0] < 200): continue

	# Fill output tree with event
	tout.Fill()

# All done. Write and close file.
fout.Write()
fout.Close()

# Timing, for debugging and optimization
print(datetime.now()-startTime)