import os
import sys

srcdir = '2013-09-19_19-48-39'
if len(sys.argv)>1:
	srcdir = sys.argv[1]

sys.argv.append('-b')
from ROOT import *
gROOT.ProcessLine("gErrorIgnoreLevel = 3001;")
from glob import glob
import array 
import math

	

if False:
	os.system('rm -r ntuples')
	os.system('mkdir ntuples')
	print srcdir

	for x in glob(srcdir+'/'+'*nt'):
		infile = x.replace('\n','')
		outfile = 'ntuples/'+x.split('/')[-1].replace('.nt','.root')
		print infile
		print outfile
		os.system('h2root '+infile + ' '+outfile)
	sys.exit()

def emptylorentz():
	v = TLorentzVector()
	v.SetPtEtaPhiM(0.00001,0.,0.,0.0)
	return v
def SetToLorentz(id,px,py,pz,pe):
	if (len(id) != len(px)) or (len(id) != len(px)) or (len(id) != len(py)) or (len(id) != len(pz)):
		print 'Major error'
		print len(id),len(px),len(py),len(pz)
		sys.exit()
	
	met = emptylorentz()
	mus = []
	nus = []
	jets = []
	for a in range(len(id)):
		i = abs(id[a])
		x = px[a]
		y = py[a]
		z = pz[a]
		e = pe[a]
		v = TLorentzVector()
		v.SetPxPyPzE(x,y,z,e)
		ptype = 'null'
		if v.Pt() ==0.0:
			continue

		if (i >=1) and (i <=6):
			ptype = 'j'
			jets.append(v)
		if i == 13:
			ptype = 'mu'
			mus.append(v)
		if i == 14:
			ptype = 'nu'
			nus.append(v)
		if ptype!='nu':
			met = met - v
		

	jets.sort(key=lambda x: float(x.Pt()))	
	mus.sort(key=lambda x: float(x.Pt()))	
	nus.sort(key=lambda x: float(x.Pt()))	

	return [met,mus,nus,jets]

def cleancollection(coll,pt,eta):
	outcoll = []
	for x in coll:
		if x.Pt()>pt:
			if abs(x.Eta()<eta):
				outcoll.append(x)
	return outcoll

def convertntuple(infile):
	print infile
	f = TFile.Open(infile,'READ')
	t = f.Get("h10")
	N = t.GetEntries()

	_treeFileName = infile.replace('.root',"_rivetTree.root")
	_treeFile = TFile.Open(_treeFileName, "recreate")
	_rivetTree = TTree("RivetTree", "RivetTree")	


	_nevt = array.array("i",[0])
	_njet_WMuNu = array.array("i",[0])
	_evweight = array.array("d",[0])
	_mt_munu = array.array("d",[0])
	_mt_mumet = array.array("d",[0])
	_htjets = array.array("d",[0])
	_ptmuon1 = array.array("d",[0])
	_etamuon1 = array.array("d",[0])
	_phimuon1 = array.array("d",[0])
	_ptmuon2 = array.array("d",[0])
	_etamuon2 = array.array("d",[0])
	_phimuon2 = array.array("d",[0])
	_ptneutrino = array.array("d",[0])
	_etaneutrino = array.array("d",[0])
	_phineutrino = array.array("d",[0])
	_ptmet = array.array("d",[0])
	_phimet = array.array("d",[0])
	_ptjet1 = array.array("d",[0])
	_etajet1 = array.array("d",[0])
	_phijet1 = array.array("d",[0])
	_dphijet1muon = array.array("d",[0])
	_ptjet2 = array.array("d",[0])
	_etajet2 = array.array("d",[0])
	_phijet2 = array.array("d",[0])
	_dphijet2muon = array.array("d",[0])
	_ptjet3 = array.array("d",[0])
	_etajet3 = array.array("d",[0])
	_phijet3 = array.array("d",[0])
	_dphijet3muon = array.array("d",[0])
	_ptjet4 = array.array("d",[0])
	_etajet4 = array.array("d",[0])
	_phijet4 = array.array("d",[0])
	_dphijet4muon = array.array("d",[0])
	_ptjet5 = array.array("d",[0])
	_etajet5 = array.array("d",[0])
	_phijet5 = array.array("d",[0])
	_dphijet5muon = array.array("d",[0])

	_rivetTree.Branch("nevt", _nevt, "nevt/I")	
	_rivetTree.Branch("njet_WMuNu", _njet_WMuNu, "njet_WMuNu/I")

	_rivetTree.Branch("evweight", _evweight, "evweight/D")			

	_rivetTree.Branch("mt_munu", _mt_munu, "mt_munu/D")			
	_rivetTree.Branch("mt_mumet", _mt_mumet, "mt_mumet/D")			

	_rivetTree.Branch("htjets", _htjets, "htjets/D")			

	_rivetTree.Branch("ptmuon1", _ptmuon1, "ptmuon1/D")			
	_rivetTree.Branch("etamuon1", _etamuon1, "etamuon1/D")			
	_rivetTree.Branch("phimuon1", _phimuon1, "phimuon1/D")			

	_rivetTree.Branch("ptmuon2", _ptmuon2, "ptmuon2/D")			
	_rivetTree.Branch("etamuon2", _etamuon2, "etamuon2/D")			
	_rivetTree.Branch("phimuon2", _phimuon2, "phimuon2/D")			

	_rivetTree.Branch("ptneutrino", _ptneutrino, "ptneutrino/D")			
	_rivetTree.Branch("etaneutrino", _etaneutrino, "etaneutrino/D")			
	_rivetTree.Branch("phineutrino", _phineutrino, "phineutrino/D")			

	_rivetTree.Branch("ptmet", _ptmet, "ptmet/D")			
	_rivetTree.Branch("phimet", _phimet, "phimet/D")	

	_rivetTree.Branch("ptjet1", _ptjet1, "ptjet1/D")			
	_rivetTree.Branch("etajet1", _etajet1, "etajet1/D")			
	_rivetTree.Branch("phijet1", _phijet1, "phijet1/D")
	_rivetTree.Branch("dphijet1muon", _dphijet1muon, "dphijet1muon/D")			

	_rivetTree.Branch("ptjet2", _ptjet2, "ptjet2/D")			
	_rivetTree.Branch("etajet2", _etajet2, "etajet2/D")			
	_rivetTree.Branch("phijet2", _phijet2, "phijet2/D")
	_rivetTree.Branch("dphijet2muon", _dphijet2muon, "dphijet2muon/D")			

	_rivetTree.Branch("ptjet3", _ptjet3, "ptjet3/D")			
	_rivetTree.Branch("etajet3", _etajet3, "etajet3/D")			
	_rivetTree.Branch("phijet3", _phijet3, "phijet3/D")
	_rivetTree.Branch("dphijet3muon", _dphijet3muon, "dphijet3muon/D")			

	_rivetTree.Branch("ptjet4", _ptjet4, "ptjet4/D")			
	_rivetTree.Branch("etajet4", _etajet4, "etajet4/D")			
	_rivetTree.Branch("phijet4", _phijet4, "phijet4/D")
	_rivetTree.Branch("dphijet4muon", _dphijet4muon, "dphijet4muon/D")			

	_rivetTree.Branch("ptjet5", _ptjet5, "ptjet5/D")			
	_rivetTree.Branch("etajet5", _etajet5, "etajet5/D")			
	_rivetTree.Branch("phijet5", _phijet5, "phijet5/D")
	_rivetTree.Branch("dphijet5muon", _dphijet5muon, "dphijet5muon/D")			

	_N = round((1.0*N)/10.0)

	print 'Completed ...',

	for n in range(N):
		t.GetEntry(n)
		if n%_N == 0:
			print round(100*((1.0*n)/(1.0*N)),1) ,'%... ',
		# _id = t.Nprt
		_id = [x for x in t.Ikf]
		_px = [x for x in t.Xpup]
		_py = [x for x in t.Ypup]
		_pz = [x for x in t.Zpup]
		_e  = [x for x in t.Epup]

		[met,mus,nus,jets] = SetToLorentz(_id,_px,_py,_pz,_e)

		for x in range(5):
			mus.append(emptylorentz())
			nus.append(emptylorentz())
			jets.append(emptylorentz())

		_nevt[0] = n
		_njet_WMuNu[0] = 0
		_htjets[0] = 0.0
		for j in cleancollection(jets,30,2.4):
			_njet_WMuNu[0] += 1
			_htjets[0] += j.Pt() 
		_evweight[0] = 1.0



		_mt_munu[0] = math.sqrt(2*(mus[0].Pt())*(nus[0].Pt())*(1-cos(nus[0].DeltaPhi(mus[0]))))
		_mt_mumet[0] = math.sqrt(2*(mus[0].Pt())*(met.Pt())*(1-cos(met.DeltaPhi(mus[0]))))

		_ptmuon1[0] = mus[0].Pt()
		_etamuon1[0] = mus[0].Eta()
		_phimuon1[0] = mus[0].Phi()

		_ptmuon2[0] = mus[1].Pt()
		_etamuon2[0] = mus[1].Eta()
		_phimuon2[0] = mus[1].Phi()

		_ptneutrino[0] = nus[0].Pt()
		_etaneutrino[0] = nus[0].Eta()
		_phineutrino[0] = nus[0].Phi()

		_ptmet[0] = met.Pt()
		_phimet[0] = met.Phi()

		_ptjet1[0] = jets[0].Pt()
		_etajet1[0] = jets[0].Eta()
		_phijet1[0] = jets[0].Phi()
		_dphijet1muon[0] = jets[0].DeltaPhi(mus[0])

		_ptjet2[0] = jets[1].Pt()
		_etajet2[0] = jets[1].Eta()
		_phijet2[0] = jets[1].Phi()
		_dphijet2muon[0] = jets[1].DeltaPhi(mus[0])

		_ptjet3[0] = jets[2].Pt()
		_etajet3[0] = jets[2].Eta()
		_phijet3[0] = jets[2].Phi()
		_dphijet3muon[0] = jets[2].DeltaPhi(mus[0])

		_ptjet4[0] = jets[3].Pt()
		_etajet4[0] = jets[3].Eta()
		_phijet4[0] = jets[3].Phi()
		_dphijet4muon[0] = jets[3].DeltaPhi(mus[0])

		_ptjet5[0] = jets[4].Pt()
		_etajet5[0] = jets[4].Eta()
		_phijet5[0] = jets[4].Phi()
		_dphijet5muon[0] = jets[4].DeltaPhi(mus[0])


		_rivetTree.Fill()
	
	_rivetTree.Write()
	_treeFile.Close()
	f.Close()
	print ' *** Done.\n'

for x in glob('ntuples/*root'):
	convertntuple(x)
	# print ' '
	# sys.exit()