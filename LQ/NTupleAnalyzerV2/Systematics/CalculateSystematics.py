import os
import sys
from ROOT import *

castors = ['/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_Default_NoScaling_2011_06_29_23_09_36/SummaryFiles','/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_Default_JetScaleDown0p4_2011_06_29_23_10_16/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_Default_JetScaleUp0p4_2011_06_29_23_10_02/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_Default_MuonScaleDown0p1_2011_06_29_23_12_34/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_Default_MuonScaleUp0p1_2011_06_29_23_11_46/SummaryFiles'
]

if "--neuswitch" in sys.argv:
	castors2 = []
	for x in castors:
		castors2.append(x.replace(x.split('LQAnalyzerOutput')[0],'/home/darinb/'))

for c in castors:
	print '-'*100
	print 'Evaluating files in castor directory: \n\n  ' +c + '\n\n'
	files = os.popen('nsls '+c).readlines()
	cfiles = []
	for x in files:
		cfiles.append(c+'/'+x.replace('\n',''))
	for x in cfiles:
		os.system('stager_qry -M '+x)
		os.system('stager_get -M '+x)
		
		
lumi = 361.0
preselectionmumu = str(lumi)+'*weight*((Pt_muon1>40)*(Pt_muon2>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_mumu>250)*((abs(Eta_muon1)<2.1)||(abs(Eta_muon2)<2.1)))'
preselectionmunu = str(lumi)+'*weight*((Pt_muon1>40)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))'


cut_mc = ''
cut_mc += "*(";
cut_mc += "((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)*(0.234142999219))+";
cut_mc += "((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)*(0.391919924679))+";
cut_mc += "((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)*(0.891152608268))+";
cut_mc += "((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)*(1.47305139771))+";
cut_mc += "((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)*(1.93017858004))+";
cut_mc += "((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)*(2.11833150885))+";
cut_mc += "((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)*(2.01751788566))+";
cut_mc += "((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)*(1.70944803697))+";
cut_mc += "((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)*(1.31229365332))+";
cut_mc += "((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)*(0.925434484034))+";
cut_mc += "((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)*(0.605971483275))+";
cut_mc += "((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)*(0.394941952849))+";
cut_mc += "((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)*(0.276345990362))+";
cut_mc += "((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)*(0.20009735534))+";
cut_mc += "((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)*(0.141456188741))+";
cut_mc += "((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)*(0.108972760522))+";
cut_mc += "((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)*(0.0833670643396))+";
cut_mc += "((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)*(0.0634614340846))+";
cut_mc += "((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)*(0.0469071585524))+";
cut_mc += "((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)*(0.0416480206016))+";
cut_mc += "((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)*(0.0329466598014))+";
cut_mc += "((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)*(0.0330046295408))+";
cut_mc += "((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)*(0.033396930948))+";
cut_mc += "((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)*(0.0326118832875))+";
cut_mc += "((N_PileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)*(0.0748840402223))";
cut_mc += ")";
preselectionmumu = preselectionmumu + cut_mc
preselectionmunu = preselectionmunu + cut_mc

thefiles = []
theintegrals = []
thecastors = []
theselection = []

print '\n\n'+'='*100+'\n           EVALUATING FOR MUMU PRESELECTION           \n'+'='*100 +'\n\n'
for c in castors:
	print '-'*100
	print 'Evaluating files in castor directory: \n\n  ' +c + '\n\n'
	files = os.popen('nsls '+c).readlines()
	cfiles = []
	for x in files:
		cfiles.append('rfio://'+c+'/'+x.replace('\n',''))
	for x in cfiles:
		f = TFile.Open(x)
		t = f.Get("PhysicalVariables")
		h = TH1D('h','h',2,-1,3)
		t.Project('h','1.0',preselectionmumu)
		n = h.Integral()
		rootfile = (x.split('/')[-1]).replace('.root','')
		print rootfile +(50-len(rootfile))*' '+ str(n)
		thecastors.append(c)
		theintegrals.append(str(n))
		thefiles.append(rootfile)
		theselection.append('MuMu')
	
print '='*100+'\n           EVALUATING FOR MUMU PRESELECTION           \n'+'='*100 +'\n\n'

for c in castors:
	print '-'*100
	print 'Evaluating files in castor directory: \n\n  ' +c + '\n\n'
	files = os.popen('nsls '+c).readlines()
	cfiles = []
	for x in files:
		cfiles.append('rfio://'+c+'/'+x.replace('\n',''))
	for x in cfiles:
		f = TFile.Open(x)
		t = f.Get("PhysicalVariables")
		h = TH1D('h','h',2,-1,3)
		t.Project('h','1.0',preselectionmunu)
		n = h.Integral()
		rootfile = (x.split('/')[-1]).replace('.root','')
		print rootfile +(50-len(rootfile))*' '+ str(n)
		thecastors.append(c)
		theintegrals.append(str(n))
		thefiles.append(rootfile)
		theselection.append('MuNu')
		
print '\n\n'
fout = open('SystematicsLog.csv')
for x in range(len(thefiles)):
	c = ','
	fout.write(thecastors[x]+c+thefiles[x]+c+theselection[x]+c+theintegrals[x])
