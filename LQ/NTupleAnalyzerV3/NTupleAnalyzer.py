import sys
sys.argv.append( '-b True' )
from ROOT import *
import array

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="input root file", metavar="FILE")
parser.add_option("-b", "--batch", dest="dobatch", help="run in batch mode", metavar="BATCH")
parser.add_option("-s", "--sigma", dest="crosssection", help="specify the process cross-section", metavar="SIGMA")
parser.add_option("-n", "--ntotal", dest="ntotal", help="total number of MC events for the sample", metavar="NTOTAL")
(options, args) = parser.parse_args()

name = options.filename
if '/store' in name:
	name = 'root://eoscms//eos/cms'+name

fin = TFile.Open(name,"READ")
t = fin.Get("rootTupleTree/tree")

N = t.GetEntries()
fout = TFile.Open(name.split('/')[-1].replace('.root','_tree.root'),"RECREATE")
tout=TTree("PhysicalVariables","PhysicalVariables")

branches = ['Et_miss','Pt_muon1','Pt_muon2','Pt_jet1','Pt_jet2','Pt_ele1','Pt_ele2']

for b in branches:
	print(b+' = array.array("f",[0])')
	print('tout.Branch("'+b+'",'+b+',"'+b+'/F")' )
	exec(b+' = array.array("f",[0])')
	exec('tout.Branch("'+b+'",'+b+',"'+b+'/F")' )

def FilterJets(pt,eta,phi,looseid):
	jets=[]
	for n in range(len(pt)):
		if pt[n]>20 and abs(eta[n])<2.4 and looseid[n]==1:
			j = TLorentzVector()
			j.SetPtEtaPhiM(pt[n],eta[n],phi[n],0)
			jets.append(j)
	return jets

def FilterMuons(pt, eta, phi, isglobal, istracker, trkiso, stationmatches, vertexdxy, chi2, pixelhits, trackerhits, trkvalidhits):
	muons = []
	for n in range(len(pt)):
		Pass = True
		Pass *= (pt[n] > 40)
		Pass *= abs(eta[n])<2.1
		Pass *= isglobal[n]*istracker[n]
		Pass *= (trkiso[n]/pt[n])<0.1
		Pass *= trackerhits[n]>=11
		Pass *= stationmatches[n]>1
		Pass *= abs(vertexdxy[n])<0.2
		Pass *= chi2[n]<10.0
		Pass *= pixelhits[n]>=1
		Pass *= trkvalidhits[n]>=1
		if (Pass):
			m = TLorentzVector()
			m.SetPtEtaPhiM(pt[n],eta[n],phi[n],0)
			muons.append(m)
	return muons


for n in range(N):
	t.GetEntry(n)
	if n%100==0:
		print n, 'of', N


	met = TLorentzVector()
	met.SetPtEtaPhiM(t.PFMET[0],0,t.PFMETPhi[0],0)

	jets = FilterJets(t.PFJetPt,t.PFJetEta,t.PFJetPhi,t.PFJetPassLooseID)
	muons =FilterMuons(t.MuonPt, t.MuonEta, t.MuonPhi, t.MuonIsGlobal, t.MuonIsTracker, t.MuonTrackerIsoSumPT, t.MuonStationMatches, t.MuonPrimaryVertexDXY,t.MuonGlobalChi2, t.MuonPixelHitCount, t.MuonTrkHitsTrackerOnly, t.MuonGlobalTrkValidHits)




	Et_miss[0] = met.Pt()


	tout.Fill()

fout.Write()
fout.Close()

