import os
import sys
sys.argv.append('-b')
from ROOT import *
from glob import glob    
from array import array

masses =  [300,450,600,750,900,1050,1200]

masses = [300]

files = glob('RootFiles/*')

FD = {}
tset = ['S (Pythia)','S (CalcHep)','YM (CalcHep)', 'MC (CalcHep)','MM (CalcHep)']

for m in masses:
	ms = str(m)
	[ps,cs,cym,cmc,cmm] = ['','','','','']
	for pt in [1,2]:
		for f in files:
			keepfile = False

			if pt ==1:
				if 'pythia' not in f and 'uujj' in f:
					keepfile = True
				if 'pythia' in f and 'MuNuJJFilter' not in f:
					keepfile = True
			else:
				if 'pythia' not in f and 'uvjj' in f:
					keepfile = True
				if 'pythia' in f and 'MuNuJJFilter' in f:
					keepfile = True
			if keepfile == False:
				continue

			if 'pythia' in f and 'M_'+ms in f:
				ps = f 
			if 'LQPair' in f:
				if 'scalar' in f:
					if 'MLQ'+ms in f:
						cs = f
				else:
					if 'MLQ'+ms in f:
						if 'KG0' in f and 'LG0' in f:
							cym = f 
						if 'KG1' in f and 'LG0' in f:
							cmc = f 
						if 'KG-1' in f and 'LG-1' in f:
							cmm = f 

		FD[m+pt] = [ps,cs,cym,cmc,cmm]
		print FD[m+pt]

# sys.exit()

def ConvertBinning(binning):
	binset=[]
	if len(binning)==3:
		for x in range(binning[0]+1):
			binset.append(((binning[2]-binning[1])/(1.0*binning[0]))*x*1.0+binning[1])
	else:
		binset=binning
	return binset

f2 = TFile.Open('tmp.root','RECREATE')


def Histo(afile,aname,var,cuts,binning):
	# print 'Histo ',aname,'from',afile
	f = TFile.Open(afile)
	t = f.Get("RivetTree")
	binset=ConvertBinning(binning) # Assure variable binning
	n = len(binset)-1 # carry the 1
	# print '   ... bins created.'
	hout= TH1D(aname,aname,n,array('d',binset)) # Declar empty TH1D
	hout.Sumw2() # Store sum of squares
	# print '   ... histo initialized.'
	t.Project(aname,var,cuts) # Project from branch to histo
	hout.Scale(1.0/(hout.Integral()))
	del t

	return hout


VD = {}
VD['ptjet1'] = 'p_{T} (jet 1) [GeV]'
VD['ptjet2'] = 'p_{T} (jet 2) [GeV]'
VD['ptmuon1'] = 'p_{T} (muon 1) [GeV]'
VD['ptmuon2'] = 'p_{T} (muon 2) [GeV]'
VD['ptmet'] = 'MET [GeV]'

SELS = {}
SELS['null'] = '(1)'
SELS['STuujj300'] = '((ptjet1+ptjet2+ptmuon1+ptmuon2) > 300)'
SELS['STuujj500'] = '((ptjet1+ptjet2+ptmuon1+ptmuon2) > 500)'
SELS['STuujj700'] = '((ptjet1+ptjet2+ptmuon1+ptmuon2) > 700)'

SELS['STuvjj300'] = '((ptjet1+ptjet2+ptmuon1+ptmet) > 300)'
SELS['STuvjj500'] = '((ptjet1+ptjet2+ptmuon1+ptmet) > 500)'
SELS['STuvjj700'] = '((ptjet1+ptjet2+ptmuon1+ptmet) > 700)'


def ShapePlot(afileset,aselection,aselectionname,avariable,xlabel,abinning,aplotname):
	c1 = TCanvas("c1","",1000,1000)
	c1.Divide(1,4)
	gStyle.SetOptStat(0)	
	histos = []
	
	hp = Histo(afileset[0],'hp',avariable,aselection,abinning)
	hcs = Histo(afileset[1],'hcs',avariable,aselection,abinning)
	hcym = Histo(afileset[2],'hcym',avariable,aselection,abinning)
	hcmc = Histo(afileset[3],'hcmc',avariable,aselection,abinning)
	hcmm = Histo(afileset[4],'hcmm',avariable,aselection,abinning)

	hcs.Divide(hp)
	hcym.Divide(hp)
	hcmc.Divide(hp)
	hcmm.Divide(hp)
	
	hcs.SetMaximum(3)
	hcym.SetMaximum(3)
	hcmc.SetMaximum(3)
	hcmm.SetMaximum(3)
	unity=TLine(binning[0], 1.0 , binning[-1],1.0)
	unity.SetLineStyle(2)
	
	c1.cd(1)
	hcs.Draw("EP")
	unity.Draw("SAME")

	c1.cd(2)
	hcym.Draw("EP")
	unity.Draw("SAME")

	c1.cd(3)
	hcmc.Draw("EP")
	unity.Draw("SAME")

	c1.cd(4)
	hcmm.Draw("EP")				
	unity.Draw("SAME")


	c1.Print(aplotname+'pdf')
	c1.Print(aplotname+'png')


binning = [50,0,2000]
for m in masses:
	for pt in [1,2]:
		if pt==1:
			chan = 'uujj'
		else:
			chan == 'uvjj'
		for s in SELS:
			for v in VD:
				mass = m
				var = v
				label = VD[v]
				selname = s
				selcut = SELS[s]
				print mass,var,label,selname,selcut
				files = FD[m+pt]
				print files
				print ' '
				plotname = 'Results/'+var+'_'+selname+'__'+chan+'.'
				ShapePlot(files,selcut,selname,var,label,binning,plotname)
			# sys.exit()