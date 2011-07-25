import os
import sys
from ROOT import *

castors = ['/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_StandardSelections_2011_07_21_00_08_14/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_JetScaleUp0p4_2011_07_21_05_45_22/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_JetScaleDown0p4_2011_07_21_05_34_49/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_MuScaleUp0p1_2011_07_21_05_46_48/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_MuScaleDown0p1_2011_07_21_05_35_58/SummaryFiles'
]

normtag = 'StandardSelections'
scaletags = ['JetScaleUp','JetScaleDown','MuScaleUp','MuScaleDown']

prefix = 'rfio'
lsqry = 'nsls'
if "--neuswitch" in sys.argv:
	os.system('sshfs -o nonempty darinb@neu:/home/darinb/ ~/neuhome;')
	castors2 = []
	for x in castors:
		castors2.append(x.replace(x.split('LQAnalyzerOutput')[0],'~/neuhome/'))
	castors = castors2
	prefix = 'file'
	lsqry = 'ls'
	

for c in castors:
	print '-'*100
	print 'Evaluating files in directory: \n\n  ' +c + '\n\n'
	files = os.popen(lsqry+' '+c).readlines()
	cfiles = []
	for x in files:
		cfiles.append(c+'/'+x.replace('\n',''))
	if lsqry == 'nsls':
		for x in cfiles:
			os.system('stager_qry -M '+x)
			os.system('stager_get -M '+x)
		
		
lumi = 964.0
#preselectionmumu = str(lumi)+'*weight*((Pt_muon1>40)*(Pt_muon2>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_mumu>250)*((abs(Eta_muon1)<2.1)||(abs(Eta_muon2)<2.1)))'
#preselectionmunu = str(lumi)+'*weight*((Pt_muon1>40)*(Pt_muon2<15.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))'

preselectionmumu = str(lumi)+'*weight*((Pt_muon1>40)*(Pt_muon2>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_mumu>250)*(deltaR_muon1muon2>0.3)*(M_muon1muon2>100)*(LowestMass_BestLQCombo>180)*((abs(Eta_muon1)<2.1)||(abs(Eta_muon2)<2.1)))'
preselectionmunu = str(lumi)+'*weight*(((Pt_muon1>40)*(Pt_muon2<30.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5)*(FailIDPFThreshold<25.0)*(MT_muon1pfMET>110.0)*(M_bestmupfjet_munu>180))'

# Final Selection

preselectionmumu += "*(ST_pf_mumu > 490)*(M_muon1muon2 > 140)*(LowestMass_BestLQCombo > 180)"
preselectionmunu += "*(ST_pf_munu > 630)*(MT_muon1pfMET > 150)*(M_bestmupfjet_munu > 120)*(MET_pf>85)*(Pt_muon1>85)"

#cut_mc = ''
#cut_mc += "*(";
#cut_mc += "((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)*(0.234142999219))+";
#cut_mc += "((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)*(0.391919924679))+";
#cut_mc += "((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)*(0.891152608268))+";
#cut_mc += "((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)*(1.47305139771))+";
#cut_mc += "((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)*(1.93017858004))+";
#cut_mc += "((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)*(2.11833150885))+";
#cut_mc += "((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)*(2.01751788566))+";
#cut_mc += "((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)*(1.70944803697))+";
#cut_mc += "((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)*(1.31229365332))+";
#cut_mc += "((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)*(0.925434484034))+";
#cut_mc += "((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)*(0.605971483275))+";
#cut_mc += "((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)*(0.394941952849))+";
#cut_mc += "((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)*(0.276345990362))+";
#cut_mc += "((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)*(0.20009735534))+";
#cut_mc += "((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)*(0.141456188741))+";
#cut_mc += "((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)*(0.108972760522))+";
#cut_mc += "((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)*(0.0833670643396))+";
#cut_mc += "((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)*(0.0634614340846))+";
#cut_mc += "((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)*(0.0469071585524))+";
#cut_mc += "((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)*(0.0416480206016))+";
#cut_mc += "((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)*(0.0329466598014))+";
#cut_mc += "((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)*(0.0330046295408))+";
#cut_mc += "((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)*(0.033396930948))+";
#cut_mc += "((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)*(0.0326118832875))+";
#cut_mc += "((N_PileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)*(0.0748840402223))";
#cut_mc += ")";

cut_mc = "*(";
cut_mc += "((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)*(0.133))+";
cut_mc += "((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)*(0.5311))+";
cut_mc += "((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)*(1.0839))+";
cut_mc += "((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)*(1.7548))+";
cut_mc += "((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)*(2.2326))+";
cut_mc += "((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)*(2.293))+";
cut_mc += "((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)*(2.0818))+";
cut_mc += "((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)*(1.74354))+";
cut_mc += "((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)*(1.329634))+";
cut_mc += "((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)*(0.950884))+";
cut_mc += "((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)*(0.65398))+";
cut_mc += "((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)*(0.4212))+";
cut_mc += "((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)*(0.2595))+";
cut_mc += "((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)*(0.158601))+";
cut_mc += "((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)*(0.100442))+";
cut_mc += "((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)*(0.05945))+";
cut_mc += "((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)*(0.034516))+";
cut_mc += "((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)*(0.02072))+";
cut_mc += "((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)*(0.01170))+";
cut_mc += "((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)*(0.006946))+";
cut_mc += "((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)*(0.003486))";
#cut_mc += "((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)*(0.00191943200042))+";
#cut_mc += "((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)*(0.00120128248423))+";
#cut_mc += "((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)*(0.000647624891971))+";
#cut_mc += "((N_PileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)*(0.000455476442992))+";
#cut_mc += "((N_PileUpInteractions > 24.5)*(N_PileUpInteractions < 25.5)*(0.000196385472519))+";
#cut_mc += "((N_PileUpInteractions > 25.5)*(N_PileUpInteractions < 26.5)*(0.000101079948326))+";
#cut_mc += "((N_PileUpInteractions > 26.5)*(N_PileUpInteractions < 27.5)*(8.14199879897e-05))+";
#cut_mc += "((N_PileUpInteractions > 27.5)*(N_PileUpInteractions < 28.5)*(4.89354471066e-05))+";
#cut_mc += "((N_PileUpInteractions > 28.5)*(N_PileUpInteractions < 29.5)*(3.35058351289e-05))";
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
	files = os.popen(lsqry+' '+c).readlines()
	cfiles = []
	for x in files:
		cfiles.append(prefix+'://'+c+'/'+x.replace('\n',''))
	for x in cfiles:
		if "BetaHalf" in x:
			continue
		f = TFile.Open(x)
		t = f.Get("PhysicalVariables")
		h = TH1D('h','h',2,-1,3)
		t.Project('h','1.0',preselectionmumu)
		n = h.Integral()
		rootfile = (x.split('/')[-1]).replace('.root','')
		print rootfile +(50-len(rootfile))*' '+ str(n)
		#print preselectionmumu
		thecastors.append(c)
		theintegrals.append(str(n))
		thefiles.append(rootfile)
		theselection.append('MuMu')
		f.Close()
		del t
	
print '='*100+'\n           EVALUATING FOR MUMU PRESELECTION           \n'+'='*100 +'\n\n'

for c in castors:
	print '-'*100
	print 'Evaluating files in castor directory: \n\n  ' +c + '\n\n'
	files = os.popen(lsqry+' '+c).readlines()
	cfiles = []
	for x in files:
		cfiles.append(prefix+'://'+c+'/'+x.replace('\n',''))
	for x in cfiles:
		if "LQToCMu_" in x and "BetaHalf" not in x:
			continue
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
		f.Close()
		del t
		
print '\n\n'
fout = open('SystematicsLog.csv','w')
fout.write('Location,File,Selection,N_Events\n\n')

for x in range(len(thefiles)):
	c = ','
	fout.write(thecastors[x]+c+thefiles[x]+c+theselection[x]+c+theintegrals[x]+'\n')


fout.close()
fout = open('SystematicsSummaryTable.csv','w')

uniquefiles = []
for x in thefiles:
	if x not in uniquefiles:
		uniquefiles.append(x)
uniqueselections = []
for x in theselection:
	if x not in uniqueselections:
		uniqueselections.append(x)
fout.write('\n\n , , , Integrals , , , , , , Percent Variations , , \n')
fout.write('Selection,File, ,'+normtag)
for x in scaletags:
	fout.write(c+x)
fout.write(' , ')
for x in scaletags:
	fout.write(c+x)
fout.write(' \n\n')

for sel in uniqueselections:
	for f in uniquefiles:
		scalevalues = []
		for x in range(len(thefiles)):
			if normtag in thecastors[x] and sel in theselection[x] and f in thefiles[x]:
				normvalue = float(theintegrals[x])
			for s in scaletags:
				if s in thecastors[x] and sel in theselection[x] and f in thefiles[x]:
					scalevalues.append(float(theintegrals[x]))
		scalepercents = []
		fout.write(sel+c+f+c+' ')
		for s in scalevalues:
			if normvalue > .001:
				scalepercents.append(100.0*(s - normvalue)/normvalue)
			if normvalue<.001:
				scalepercents.append(0)
		fout.write(c+str(s))
		for x in scalevalues:
			fout.write(c+str(x))
		fout.write(' , ')
		for x in scalepercents:
			fout.write(c+str(x))
		fout.write('\n')
	fout.write('\n')
fout.close()
			
		

fout.close()
