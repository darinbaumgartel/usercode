import sys
sys.argv.append( '-b' )
from ROOT import *
from array import array

name = sys.argv[1]

fin = TFile.Open(name,"READ")
tin = fin.Get("rootTupleTree/tree")
hin = fin.Get("LJFilter/EventCount")

fout = TFile.Open((name.split('/')[-1]).replace('.root','skim.root'),"RECREATE")

savdir = gDirectory
h1dir = savdir.mkdir("LJFilter")
adir = savdir.mkdir("rootTupleTree")
h2dir = h1dir.mkdir("EventCount")
h2dir.cd()
h = fin.Get("LJFilter/EventCount/EventCounter")
h.Write()
savdir.cd()
adir.cd()

tout = tin.CopyTree("0")

N = tin.GetEntries()

for n in range(N):
	tin.GetEntry(n)
	
	if n%5000==0:
		print n, 'of', N
		
	ept1=0
	mpt1=0
	jpt1=0
	jpt2=0

	
	ept2=0
	mpt2=0
	
	met = 0
	
	jetpts = []
	
	if len(tin.ElectronPt)> 0:
		ept1 = tin.ElectronPt[0]	

	if len(tin.MuonPt)> 0:
		mpt1 = tin.MuonPt[0]	

	for x in range(len(tin.PFJetPt)):
		if (tin.PFJetPassLooseID[x] == 1) and ( abs(tin.PFJetEta[x]) < 2.5) :
			jetpts.append(tin.PFJetPt[x])
	
	jetpts.append(0)
	jetpts.append(0)
	
	jpt1 = jetpts[0]
	jpt2=jetpts[1]

	if len(tin.ElectronPt)> 1:
		ept2 = tin.ElectronPt[1]	

	if len(tin.MuonPt)> 1:
		mpt2 = tin.MuonPt[1]	

	met = tin.PFMET[0]

	leps = [met,ept1,ept2,mpt1,mpt2]
	
	leps.sort()
	
	l1 = leps[4]
	l2 = leps[3]	

	keep = 0

	if ( ept1 > 35 and ept2 > 35 and jpt1>25):
		keep = 1
	
	if ( ept1 > 35 and mpt1 > 35 and jpt1>25):
		keep = 1	

	if ( mpt1 > 35 and mpt2 > 35 and jpt1>25):
		keep = 1	

	if ( mpt1 > 35 and met > 45 and jpt1>25):
		keep = 1

	if ( ept1 > 35 and met > 45 and jpt1>25):
		keep = 1
		
	if (keep ==0):
		continue
		
	keep2 = 0
		
	if ( (ept1 + ept2 + jpt1 + jpt2) > 230 ):
		keep2 = 1
		
	if ( (ept1 + met + jpt1 + jpt2) > 230 ):
		keep2 = 1
		
	if ( (mpt1 + mpt2 + jpt1 + jpt2) > 230 ):
		keep2 = 1
		
	if ( (mpt1 + met + jpt1 + jpt2) > 230 ):
		keep2 = 1
		
	if ( (ept1 + mpt1 + jpt1 + jpt2) > 230 ):
		keep2 = 1

	if (keep2 == 0):
		continue
	
		
	tout.Fill()

fout.Write()
fout.Close()

