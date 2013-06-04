from ROOT import *
import os
import sys
import array
import math

ntuplefile=''
ntuplepatchfile=''

for n in range(len(sys.argv)):
	if sys.argv[n]=="--ntuple":
		ntuplefile=sys.argv[n+1]
	if sys.argv[n]=="--ntuplepatch":
		ntuplepatchfile=sys.argv[n+1]	

if ntuplefile=='' or ntuplepatchfile=='':
	print "ERROR: Must specify an input file and a patch file, e.g.\n   python GenLeptonPatcher.py --ntuple WJets_MG.root --ntuplepatch mergedoutput.root\n"
	sys.exit()

tn = TFile.Open(ntuplefile,"READ").Get("PhysicalVariables")
tp = TFile.Open(ntuplepatchfile,"READ").Get("rootTupleTree/tree")
outfile = ntuplefile.replace(".root","_out.root")
fo = TFile.Open(outfile,"RECREATE")
to = tn.CopyTree("0")

tn.BuildIndex("run_number","event_number")
tp.BuildIndex("run","event")

def DeltaPhi(phi1,phi2):
	dphi = abs(phi1-phi2)
	_pi = 3.14159265358;
	if (dphi>_pi):
		dphi = 2.0*_pi-dphi
	return dphi

def ST(vecs):
	ST = 0.0
	for v in vecs:
		ST += v.Pt()
	return ST

def TMass(Pt1, Pt2, DPhi12):
	return math.sqrt( 2*Pt2*Pt1*(1-math.cos(DPhi12)) );


def LV(pt,eta,phi,m):
	v = TLorentzVector()
	v.SetPtEtaPhiM(pt,eta,phi,m)
	return v

def GetMuonByRunEvent(r,e,recomuon):
	x = tp.GetEntryWithIndex(r,e)
	v = TLorentzVector()
	v.SetPtEtaPhiM(0,0,0,0)	
	if x == -1:
		return v
	npart = len(tp.GenParticlePdgId)
	if npart ==0:
		return v
	dif   = 999999999999
	drmax = 999999999999
	bestp = -1
	for p in range(npart):
		pt  = tp.GenParticlePt[p]
		eta = tp.GenParticleEta[p]
		phi = tp.GenParticlePhi[p]
		dpt = abs(pt - recomuon.Pt())
		v.SetPtEtaPhiM(pt,eta,phi,0)
		dr = abs(v.DeltaR(recmuon))
		if dpt<dif:
			dif = dpt
			if (dr < drmax) and (dr < .5):
				bestp = p
				drmax = dr
	if (bestp > -1):
		pt  = tp.GenParticlePt[bestp]
		eta = tp.GenParticleEta[bestp]
		phi = tp.GenParticlePhi[bestp]		
		v.SetPtEtaPhiM(pt,eta,phi,0)
	else:
		v.SetPtEtaPhiM(0,0,0,0)
	return v

N = tn.GetEntries()	

variables = ['Pt_genmuon1', 'Eta_genmuon1', 'Phi_genmuon1', ]
variables.append('DeltaPhi_genjet1genmuon1')
variables.append('DeltaPhi_genjet2genmuon1')
variables.append('DeltaPhi_genjet3genmuon1')
variables.append('DeltaPhi_genjet4genmuon1')
variables.append('DeltaPhi_genjet5genmuon1')
variables.append('ST_genmuongenMET')
variables.append('ST_genmuongenMETgenjet1')
variables.append('ST_genmuongenMETgenjet12')
variables.append('ST_genmuongenMETgenjet123')
variables.append('ST_genmuongenMETgenjet1234')
variables.append('ST_genmuongenMETgenjet12345')
variables.append('ST_genmuongenMETgenjet123456')
variables.append('MT_genmuon1genMET')
variables.append('MT_genmuon1genneutrino')


for v in variables:
	exec(v+'mod=array.array(\'d\',[0])')
	exec('to.SetBranchAddress("'+v+'",'+v+'mod)')

nbad = []
for n in range(N):
	tn.GetEntry(n)
	if n%1000==0:
		done_str = str( round(((1.0*n)/(1.0*N)*100),1) )+"% completed."
		sys.stdout.flush()
		sys.stdout.write('%s\r' % done_str)
		
	for v in variables:
		exec(v+'mod[0] = tn.'+v)

	if tn.Pt_genmuon1<=0:
		recmuon = TLorentzVector()
		recmuon.SetPtEtaPhiM(tn.Pt_muon1,tn.Eta_muon1, tn.Phi_muon1,0)
		genmuon = GetMuonByRunEvent(tn.run_number,tn.event_number,recmuon)
		
		gennu = LV(tn.Phi_genmuonneutrino1,tn.Eta_genmuonneutrino1,tn.Phi_genmuonneutrino1,0) 
		genmet = LV(tn.Pt_genMET, 0, tn.Phi_genMET,0)
		
		genjet1 = LV(tn.Pt_genjet1, tn.Eta_genjet1, tn.Phi_genjet1,0)	
		genjet2 = LV(tn.Pt_genjet2, tn.Eta_genjet2, tn.Phi_genjet2,0)	
		genjet3 = LV(tn.Pt_genjet3, tn.Eta_genjet3, tn.Phi_genjet3,0)	
		genjet4 = LV(tn.Pt_genjet4, tn.Eta_genjet4, tn.Phi_genjet4,0)	
		genjet5 = LV(tn.Pt_genjet5, tn.Eta_genjet5, tn.Phi_genjet5,0)	
				
		if genmuon.Pt() > 0.001:
			Pt_genmuon1mod[0] = genmuon.Pt()
			Eta_genmuon1mod[0] = genmuon.Eta()
			Phi_genmuon1mod[0] = genmuon.Phi()
			MT_genmuon1genMETmod[0] = TMass(genmuon.Pt(),genmet.Pt(),DeltaPhi(genmuon.Phi(),genmet.Phi()))
			MT_genmuon1genneutrinomod[0] = TMass(genmuon.Pt(),gennu.Pt(),DeltaPhi(genmuon.Phi(),gennu.Phi()))
			
			ST_genmuongenMETmod[0] = ST([genmuon,genmet])
			ST_genmuongenMETgenjet1mod[0] = ST([genmuon,genmet, genjet1])
			ST_genmuongenMETgenjet12mod[0] = ST([genmuon,genmet, genjet1, genjet1])
			ST_genmuongenMETgenjet123mod[0] = ST([genmuon,genmet, genjet1, genjet2, genjet3 ])
			ST_genmuongenMETgenjet1234mod[0] = ST([genmuon,genmet, genjet1, genjet2, genjet3, genjet4 ])
			ST_genmuongenMETgenjet12345mod[0] = ST([genmuon,genmet, genjet1, genjet2, genjet3, genjet4, genjet5 ])

			if (tn.PFJetCount>=1) : DeltaPhi_genjet1genmuon1mod[0] = DeltaPhi(genmuon.Phi(), genjet1.Phi())
			if (tn.PFJetCount>=2) : DeltaPhi_genjet2genmuon1mod[0] = DeltaPhi(genmuon.Phi(), genjet2.Phi())
			if (tn.PFJetCount>=3) : DeltaPhi_genjet3genmuon1mod[0] = DeltaPhi(genmuon.Phi(), genjet3.Phi())
			if (tn.PFJetCount>=4) : DeltaPhi_genjet4genmuon1mod[0] = DeltaPhi(genmuon.Phi(), genjet4.Phi())
			if (tn.PFJetCount>=5) : DeltaPhi_genjet5genmuon1mod[0] = DeltaPhi(genmuon.Phi(), genjet5.Phi())
			
	to.Fill()


sys.stdout.flush()
print " "
print tn.GetEntries(), tn.GetEntries("Pt_genmuon1<0.0001")
print to.GetEntries(), to.GetEntries("Pt_genmuon1<0.0001")

os.system('mv '+ntuplefile+' '+ntuplefile.replace(".root","_.roobak"))
os.system('mv '+ntuplefile.replace(".root","_out.root")+' '+ntuplefile)
to.Write()
fo.Close()

