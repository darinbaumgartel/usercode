import os
import sys
from ROOT import *
import math

castors = ['/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_StandardSelections_PreApproval_2011_07_27_05_59_49/SummaryFiles/']

normtag = 'StandardSelections'
scaletags = ['JetScaleUp','JetScaleDown','MuScaleUp','MuScaleDown']

prefix = 'rfio'
lsqry = 'nsls'
if "--neuswitch" in sys.argv:
	#os.system('sshfs -o nonempty darinb@neu:/home/darinb/ ~/neuhome;')
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

presel = 0
if 'presel' in str(sys.argv):
	presel = 1
	
emu = 0
if 'ttbaremu' in  str(sys.argv):
	emu = 1
	print "\n\nUsing data driven ttbar...\n"
#preselectionmumu = str(lumi)+'*weight*((Pt_muon1>40)*(Pt_muon2>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_mumu>250)*((abs(Eta_muon1)<2.1)||(abs(Eta_muon2)<2.1)))'
#preselectionmunu = str(lumi)+'*weight*((Pt_muon1>40)*(Pt_muon2<15.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))'

preselectionmumu = str(lumi)+'*weight_964pileup_bugfix*((Pt_muon1>40)*(Pt_muon2>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_mumu>250)*(deltaR_muon1muon2>0.3)*(M_muon1muon2>50)*((abs(Eta_muon1)<2.1)||(abs(Eta_muon2)<2.1)))'
#preselectionemu = str(lumi)+'*weight*(LowestUnprescaledTriggerPass>0.5)*((Pt_muon1>40)*(Pt_HEEPele1>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_emu>250)*(deltaR_muon1HEEPele1>0.3)*(M_muon1HEEPele1>50)*((abs(Eta_muon1)<2.1)||(abs(Eta_muon2)<2.1)))'
preselectionmunu = str(lumi)+'*weight_964pileup_bugfix*(((Pt_muon1>40)*(Pt_muon2<30.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5)*(FailIDPFThreshold<25.0)*(MT_muon1pfMET>50.0))'
preselectionenu = '0.6284*(Pt_muon1>40)*(Pt_HEEPele1>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_emu>250)*(M_muon1HEEPele1>50)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.1)||(abs(Eta_HEEPele1)<2.1))';


#*(ST_pf_munu > 380)*(MT_muon1pfMET > 110)*(M_bestmupfjet_munu > 130)

# These are MC - driven Summer11 for the bug fix
#cut_mc = "*(";
#cut_mc += "((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)*(0.133068262644))+";
#cut_mc += "((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)*(0.531177727826))+";
#cut_mc += "((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)*(1.08393607934))+";
#cut_mc += "((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)*(1.75485574706))+";
#cut_mc += "((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)*(2.23265146857))+";
#cut_mc += "((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)*(2.29302545029))+";
#cut_mc += "((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)*(2.08187693395))+";
#cut_mc += "((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)*(1.74354004493))+";
#cut_mc += "((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)*(1.32963414181))+";
#cut_mc += "((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)*(0.950884829018))+";
#cut_mc += "((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)*(0.653989809522))+";
#cut_mc += "((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)*(0.421230072952))+";
#cut_mc += "((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)*(0.259599212011))+";
#cut_mc += "((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)*(0.158601185413))+";
#cut_mc += "((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)*(0.100442489896))+";
#cut_mc += "((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)*(0.0594521650904))+";
#cut_mc += "((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)*(0.0345162335823))+";
#cut_mc += "((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)*(0.0207204183018))+";
#cut_mc += "((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)*(0.0117033339315))+";
#cut_mc += "((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)*(0.00694640146464))+";
#cut_mc += "((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)*(0.00348689915421))+";
#cut_mc += "((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)*(0.00191943200042))+";
#cut_mc += "((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)*(0.00120128248423))+";
#cut_mc += "((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)*(0.000647624891971))+";
#cut_mc += "((N_PileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)*(0.000455476442992))+";
#cut_mc += "((N_PileUpInteractions > 24.5)*(N_PileUpInteractions < 25.5)*(0.000196385472519))+";
#cut_mc += "((N_PileUpInteractions > 25.5)*(N_PileUpInteractions < 26.5)*(0.000101079948326))+";
#cut_mc += "((N_PileUpInteractions > 26.5)*(N_PileUpInteractions < 27.5)*(8.14199879897e-05))+";
#cut_mc += "((N_PileUpInteractions > 27.5)*(N_PileUpInteractions < 28.5)*(4.89354471066e-05))+";
#cut_mc += "((N_PileUpInteractions > 28.5)*(N_PileUpInteractions < 29.5)*(3.35058351289e-05))";
#cut_mc += ")";

#preselectionmumu += cut_mc
#preselectionmunu += cut_mc

# Final Selection

#preselectionmumu += "*(ST_pf_mumu > 490)*(M_muon1muon2 > 140)*(LowestMass_BestLQCombo > 180)"
#preselectionmunu += "*(ST_pf_munu > 630)*(MT_muon1pfMET > 150)*(M_bestmupfjet_munu > 120)*(MET_pf>85)*(Pt_muon1>85)"

BetaHalfSignals = []
BetaOneSignals = []
Backgrounds = []
BetaHalfSignalNames = []
BetaOneSignalNames = []
BackgroundNames = []
Data = ''
DataNames =  ''


for x in cfiles:
	if 'LQToCMu' in x:
		if 'BetaHalf' in x:
			BetaHalfSignals.append(x)
			BetaHalfSignalNames.append(x.split('/')[-1].replace('.root',''))
		else:
			BetaOneSignals.append(x)
			BetaOneSignalNames.append(x.split('/')[-1].replace('.root',''))

	else:
		if 'SingleMuData' not in x:
			Backgrounds.append(x)	
			BackgroundNames.append(x.split('/')[-1].replace('.root',''))
for x in cfiles:
	if 'SingleMuData' in x:
		Backgrounds.append(x)	
		BackgroundNames.append(x.split('/')[-1].replace('.root',''))

logsignals = []
logcuts = []	
BetaOneCuts = []
BetaHalfCuts=[]
log = open('OptimizationResultsV2.txt','r')
for line in log:
	if 'LQToCMu' in line:
		logsignals.append(line.replace('\n',''))
	if '>' in line:
		logcuts.append(line.replace('\n',''))

#for x in range(len(logsignals)):
	#print logsignals[x]
	#print logcuts[x]

for x in (BetaOneSignalNames):
	for y in range(len(logsignals)):
		if x in logsignals[y]:
			BetaOneCuts.append(logcuts[y])
for x in (BetaHalfSignalNames):
	for y in range(len(logsignals)):
		if x in logsignals[y]:
			BetaHalfCuts.append(logcuts[y])
			
#for x in range(len(BetaOneSignalNames)):
	#print BetaOneSignalNames[x]
	#print BetaOneCuts[x]

#for x in range(len(BetaHalfSignalNames)):
	#print BetaHalfSignalNames[x]
	#print BetaHalfCuts[x]

if (presel ==1):
	print '\n\n PreSelection for MuMu \n\n'
else:
	print '\n\n Full Selection for MuMu \n\n'

for n in range(len(BetaOneSignals)):
	fullsel = '*1.0'
	thisfullsel = fullsel
	if presel != 1:
		fullsel = '*'+BetaOneCuts[n]
	totalbackground = 0.0
	totalbackgrounderror = 0.0
	berrors = []
	tableline = ''
	if n == 0:
		headerline = 'LQ Mass'
	f = TFile.Open(BetaOneSignals[n])
	t = f.Get("PhysicalVariables")
	h = TH1D('h','h',2,-1,3)
	t.Project('h','1.0',preselectionmumu+fullsel)
	I = h.Integral()
	E = I / math.sqrt(1.0*h.GetEntries())
	f.Close()
	del t
	tableline += BetaOneSignalNames[n]+' , '+str(I) +' , +- , '+ str(E)
	if n == 0:
		headerline += ', LQ Signal , ,  '

	for m in range(len(Backgrounds)):
		if emu==1 and 'DiBoson' in Backgrounds[m]:
			continue
		trigger = ""
		thisfullsel = fullsel
		thispreselection = preselectionmumu
		f = TFile.Open(Backgrounds[m])
		t = f.Get("PhysicalVariables")
		h = TH1D('h','h',2,-1,3)
		scalefactor = 1.0
		if 'WJets' in Backgrounds[m]:
			scalefactor = 0.94
		if 'ZJets' in Backgrounds[m]:
			scalefactor = 1.03
		if 'TTBar' in Backgrounds[m] and emu==0:
			scalefactor = (1.00)
		if 'TTBar' in Backgrounds[m] and emu==1:
			thisfullsel = thisfullsel.replace('ST_pf_mumu','ST_pf_emu')
			thisfullsel = thisfullsel.replace('muon1muon2','muon1HEEPele1')
			thisfullsel = thisfullsel.replace('LowestMass_BestLQCombo','LowestMass_BestLQCombo_emuselection')
			scalefactor = 1.0
			thispreselection = preselectionenu
			for x in Backgrounds:
				if "SingleMuData" in x:
					datfile = x
			f.Close() 
			del t
			f = TFile.Open(datfile)
			t = f.Get("PhysicalVariables")
			h = TH1D('h','h',2,-1,3)
			trigger = "*(LowestUnprescaledTriggerPass>0.5)"

		if 'SingleMuData' in Backgrounds[m]:
			trigger = "*(LowestUnprescaledTriggerPass>0.5)"
		t.Project('h','1.0',thispreselection+thisfullsel+trigger)
		if 'SingleMuData' in Backgrounds[m]:
			I = 1.0*(h.GetEntries())
		else:
			I = scalefactor*(h.Integral())
		if I>0.001:
			E = I / math.sqrt(1.0*h.GetEntries())
		else:
			E=0.0
		if 'SingleMuData' not in Backgrounds[m]:
			totalbackground += I
			berrors.append(E)
		f.Close()
		del t
		if 'SingleMuData' in Backgrounds[m]:
			tableline += ' , '+str(I) 
		else:
			tableline += ' , '+str(I) +' , +-  , '+ str(E)
		if n == 0:
			headerline += ', '+BackgroundNames[m] + ('SingleMuData' not in BackgroundNames[m])*' , ,  '
	for x in berrors:
		totalbackgrounderror+=(x*x)
	totalbackgrounderror = math.sqrt(totalbackgrounderror)
	tableline += ' , '+ str(totalbackground) + ' , +- , '+str(totalbackgrounderror)
	if n == 0:
		headerline += ' , Total BG , , '
		print headerline
	print tableline


if (presel ==1):
	print '\n\n PreSelection for MuNu \n\n'
else:
	print '\n\n Full Selection for MuNu \n\n'

for n in range(len(BetaHalfSignals)):
	fullsel = '*1.0'
	if presel != 1:
		fullsel = '*'+BetaHalfCuts[n]
	totalbackground = 0.0
	totalbackgrounderror = 0.0
	berrors = []
	tableline = ''
	if n == 0:
		headerline = 'LQ Mass'
	f = TFile.Open(BetaHalfSignals[n])
	t = f.Get("PhysicalVariables")
	h = TH1D('h','h',2,-1,3)
	t.Project('h','1.0',preselectionmunu+fullsel)
	I = h.Integral()
	E = I / math.sqrt(1.0*h.GetEntries())
	f.Close()
	del t
	tableline += BetaHalfSignalNames[n]+' , '+str(I) +' , +- , '+ str(E)
	if n == 0:
		headerline += ', LQ Signal , ,'

	for m in range(len(Backgrounds)):
		trigger = ""
		f = TFile.Open(Backgrounds[m])
		t = f.Get("PhysicalVariables")
		h = TH1D('h','h',2,-1,3)
		scalefactor = 1.0
		if 'WJets' in Backgrounds[m]:
			scalefactor = 0.94
		if 'ZJets' in Backgrounds[m]:
			scalefactor = 1.03
		if 'TTBar' in Backgrounds[m]:
			scalefactor = (1.01)
		if 'SingleMuData' in Backgrounds[m]:
			trigger = "*(LowestUnprescaledTriggerPass>0.5)"

		t.Project('h','1.0',preselectionmunu+fullsel+trigger)
		if 'SingleMuData' in Backgrounds[m]:
			I = 1.0*(h.GetEntries())
		else:
			I = scalefactor*(h.Integral())
		if I>0.001:
			E = I / math.sqrt(1.0*h.GetEntries())
		else:
			E=0.0
		if 'SingleMuData' not in Backgrounds[m]:
			totalbackground += I
			berrors.append(E)
		f.Close()
		del t
		if 'SingleMuData' in Backgrounds[m]:
			tableline += ' , '+str(I) 
		else:
			tableline += ' , '+str(I) +' , +-  , '+ str(E)
		if n == 0:
			headerline += ', '+BackgroundNames[m] + ('SingleMuData' not in BackgroundNames[m])*' , ,  '
	for x in berrors:
		totalbackgrounderror+=(x*x)
	totalbackgrounderror = math.sqrt(totalbackgrounderror)
	tableline += ' , '+ str(totalbackground) + ' , +- , '+str(totalbackgrounderror)
	if n == 0:
		headerline += ' , Total BG , , '
		print headerline
	print tableline

print '\n\n'

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

#cut_mc = "*(";
#cut_mc += "((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)*(0.133))+";
#cut_mc += "((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)*(0.5311))+";
#cut_mc += "((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)*(1.0839))+";
#cut_mc += "((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)*(1.7548))+";
#cut_mc += "((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)*(2.2326))+";
#cut_mc += "((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)*(2.293))+";
#cut_mc += "((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)*(2.0818))+";
#cut_mc += "((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)*(1.74354))+";
#cut_mc += "((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)*(1.329634))+";
#cut_mc += "((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)*(0.950884))+";
#cut_mc += "((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)*(0.65398))+";
#cut_mc += "((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)*(0.4212))+";
#cut_mc += "((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)*(0.2595))+";
#cut_mc += "((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)*(0.158601))+";
#cut_mc += "((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)*(0.100442))+";
#cut_mc += "((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)*(0.05945))+";
#cut_mc += "((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)*(0.034516))+";
#cut_mc += "((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)*(0.02072))+";
#cut_mc += "((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)*(0.01170))+";
#cut_mc += "((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)*(0.006946))+";
#cut_mc += "((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)*(0.003486))";
##cut_mc += "((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)*(0.00191943200042))+";
##cut_mc += "((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)*(0.00120128248423))+";
##cut_mc += "((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)*(0.000647624891971))+";
##cut_mc += "((N_PileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)*(0.000455476442992))+";
##cut_mc += "((N_PileUpInteractions > 24.5)*(N_PileUpInteractions < 25.5)*(0.000196385472519))+";
##cut_mc += "((N_PileUpInteractions > 25.5)*(N_PileUpInteractions < 26.5)*(0.000101079948326))+";
##cut_mc += "((N_PileUpInteractions > 26.5)*(N_PileUpInteractions < 27.5)*(8.14199879897e-05))+";
##cut_mc += "((N_PileUpInteractions > 27.5)*(N_PileUpInteractions < 28.5)*(4.89354471066e-05))+";
##cut_mc += "((N_PileUpInteractions > 28.5)*(N_PileUpInteractions < 29.5)*(3.35058351289e-05))";
#cut_mc += ")";


#preselectionmumu = preselectionmumu + cut_mc
#preselectionmunu = preselectionmunu + cut_mc

#thefiles = []
#theintegrals = []
#thecastors = []
#theselection = []


#print '\n\n'+'='*100+'\n           EVALUATING FOR MUMU PRESELECTION           \n'+'='*100 +'\n\n'
#for c in castors:
	#print '-'*100
	#print 'Evaluating files in castor directory: \n\n  ' +c + '\n\n'
	#files = os.popen(lsqry+' '+c).readlines()
	#cfiles = []
	#for x in files:
		#cfiles.append(prefix+'://'+c+'/'+x.replace('\n',''))
	#for x in cfiles:
		#if "BetaHalf" in x:
			#continue
		#f = TFile.Open(x)
		#t = f.Get("PhysicalVariables")
		#h = TH1D('h','h',2,-1,3)
		#t.Project('h','1.0',preselectionmumu)
		#n = h.Integral()
		#rootfile = (x.split('/')[-1]).replace('.root','')
		#print rootfile +(50-len(rootfile))*' '+ str(n)
		##print preselectionmumu
		#thecastors.append(c)
		#theintegrals.append(str(n))
		#thefiles.append(rootfile)
		#theselection.append('MuMu')
		#f.Close()
		#del t
		
		
	
#print '='*100+'\n           EVALUATING FOR MUMU PRESELECTION           \n'+'='*100 +'\n\n'

#for c in castors:
	#print '-'*100
	#print 'Evaluating files in castor directory: \n\n  ' +c + '\n\n'
	#files = os.popen(lsqry+' '+c).readlines()
	#cfiles = []
	#for x in files:
		#cfiles.append(prefix+'://'+c+'/'+x.replace('\n',''))
	#for x in cfiles:
		#if "LQToCMu_" in x and "BetaHalf" not in x:
			#continue
		#f = TFile.Open(x)
		#t = f.Get("PhysicalVariables")
		#h = TH1D('h','h',2,-1,3)
		#t.Project('h','1.0',preselectionmunu)
		#n = h.Integral()
		#rootfile = (x.split('/')[-1]).replace('.root','')
		#print rootfile +(50-len(rootfile))*' '+ str(n)
		#thecastors.append(c)
		#theintegrals.append(str(n))
		#thefiles.append(rootfile)
		#theselection.append('MuNu')
		#f.Close()
		#del t
		
#print '\n\n'
#fout = open('SelectionTableLog.csv','w')
#fout.write('Location,File,Selection,N_Events\n\n')

#for x in range(len(thefiles)):
	#c = ','
	#fout.write(thecastors[x]+c+thefiles[x]+c+theselection[x]+c+theintegrals[x]+'\n')


#fout.close()
#fout = open('SelectionSummaryTable.csv','w')

#uniquefiles = []
#for x in thefiles:
	#if x not in uniquefiles:
		#uniquefiles.append(x)
#uniqueselections = []
#for x in theselection:
	#if x not in uniqueselections:
		#uniqueselections.append(x)
#fout.write('\n\n , , , Integrals , , , , , , Percent Variations , , \n')
#fout.write('Selection,File, ,'+normtag)
#for x in scaletags:
	#fout.write(c+x)
#fout.write(' , ')
#for x in scaletags:
	#fout.write(c+x)
#fout.write(' \n\n')

#for sel in uniqueselections:
	#for f in uniquefiles:
		#scalevalues = []
		#for x in range(len(thefiles)):
			#if normtag in thecastors[x] and sel in theselection[x] and f in thefiles[x]:
				#normvalue = float(theintegrals[x])
			#for s in scaletags:
				#if s in thecastors[x] and sel in theselection[x] and f in thefiles[x]:
					#scalevalues.append(float(theintegrals[x]))
		#scalepercents = []
		#fout.write(sel+c+f+c+' ')
		#for s in scalevalues:
			#if normvalue > .001:
				#scalepercents.append(100.0*(s - normvalue)/normvalue)
			#if normvalue<.001:
				#scalepercents.append(0)
		#fout.write(c+str(s))
		#for x in scalevalues:
			#fout.write(c+str(x))
		#fout.write(' , ')
		#for x in scalepercents:
			#fout.write(c+str(x))
		#fout.write('\n')
	#fout.write('\n')
#fout.close()
			
		

#fout.close()
