#############################################################################
## This file creates scripts for optimization with signicance and CLA       ##
## Leptoquark NTuples are interpreted from NTupleInfo.csv file              ##
## Background is utilized with the ALLBKG Sample - MUST BE PRESENT         ##
#############################################################################
from ROOT import *
import os # For direcory scanning abilities, etc
import sys
import math
AnalysisType=sys.argv[1] 
#FileLocation="~/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_Default__2011_07_12_16_27_56/SummaryFiles/"
#FileLocation="/tmp/darinb/NTupleAnalyzer_V00_02_04_Default__2011_07_12_16_27_56/SummaryFiles/"
FileLocation="/afs/cern.ch/user/d/darinb/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_StandardSelections_2fb_2011_10_04_15_37_02/SummaryFiles/"

#print(AnalysisType)
if AnalysisType == "":
	print("\n\nYou need to specify an analysis type\n\n Example: \n >> python OptimizationUtility.py MuNu\n\nProcess Exiting")
	sys.exit(0)
from time import strftime

ttbarscale = 1.01
wscale = 1.24
zscale = 8.723

ErrorFactorMuMu = 0.25
ErrorFactorMuNu = 0.9

CutVariablesMuMu=['ST_pf_mumu','M_muon1muon2','LowestMass_BestLQCombo'] # Which variables do you want to cut on

VariableStartingPointMuMu = [250,100,100] # Where to start cutting on the variable 
VariableIntervalMuMu = [10,10,10] # Intervals in which you will test cuts
VariablePointsToTestMuMu = [85,12,90] # Number of cutting points to test at the given interval


#CutVariablesMuNu=['ST_pf_munu','MT_muon1pfMET','M_bestmupfjet_munu'] # Which variables do you want to cut on
CutVariablesMuNu=['ST_pf_munu','MET_pf','M_bestmupfjet_munu'] # Which variables do you want to cut on

#VariableStartingPointMuNu = [250,45,50] # Where to start cutting on the variable 
#VariableIntervalMuNu = [10,5,10] # Intervals in which you will test cuts
#VariablePointsToTestMuNu = [85,30,80] # Number of cutting points to test at the given interval

VariableStartingPointMuNu = [250,100,100] # Where to start cutting on the variable 
VariableIntervalMuNu = [10,10,10] # Intervals in which you will test cuts
VariablePointsToTestMuNu = [85,20,90] # Number of cutting points to test at the given interval
person = (os.popen("whoami").readlines())[0].replace('\n','')

# Other variable to precut on as they appear in the root file (these are not variable cuts, they are single static cuts):
lumi= 2000.0
preselectionmumu = '((Pt_muon1>40)*(Pt_muon2>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_mumu>250)*(deltaR_muon1muon2>0.3)*(M_muon1muon2>100)*(LowestMass_BestLQCombo>50)*((abs(Eta_muon1)<2.1)||(abs(Eta_muon2)<2.1)))'
preselectionmunu = '((Pt_muon1>40)*(Pt_muon2<15.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5)*(FailIDPFThreshold<25.0)*(MT_muon1pfMET>50.0)*(M_bestmupfjet_munu>50)'

for x in range(len(CutVariablesMuNu)):
	preselectionmunu += '*('+CutVariablesMuNu[x]+'> '+str(VariableStartingPointMuNu[x])+')'

cut_mc = str(lumi)+'*weight_pileup2fb'
# These are MC - driven Summer11 for the bug fix
#cut_mc += "*(";
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
	
KeepFiles = ['LQToCMu_BetaHalf_M_250.root',
'LQToCMu_BetaHalf_M_350.root',
'LQToCMu_BetaHalf_M_400.root',
'LQToCMu_BetaHalf_M_450.root',
'LQToCMu_BetaHalf_M_500.root',
'LQToCMu_BetaHalf_M_550.root',
'LQToCMu_BetaHalf_M_600.root',
'LQToCMu_BetaHalf_M_650.root',
'LQToCMu_BetaHalf_M_750.root',
'LQToCMu_BetaHalf_M_850.root',
'LQToCMu_M_250.root',
'LQToCMu_M_350.root',
'LQToCMu_M_400.root',
'LQToCMu_M_450.root',
'LQToCMu_M_500.root',
'LQToCMu_M_550.root',
'LQToCMu_M_600.root',
'LQToCMu_M_650.root',
'LQToCMu_M_750.root',
'LQToCMu_M_850.root',
'DiBoson.root',
'SingleTop.root',
'TTBar.root',
'WJets_Sherpa.root',
'ZJets_Sherpa.root']	
	
preselectionmumu = preselectionmumu
preselectionmunu = preselectionmunu

logout = open(AnalysisType+"_log.txt",'w')
logoutSB = open(AnalysisType+"_SB_log.txt",'w')
logoutSSB = open(AnalysisType+"_SSB_log.txt",'w')
logoutSSBdB2 = open(AnalysisType+"_SSBdB2_log.txt",'w')

BGErrorFactor = 0.0

if AnalysisType=="MuMu" or AnalysisType =="MuMu" or AnalysisType=="mumu":
	CutVariables = CutVariablesMuMu
	VariableStartingPoint = VariableStartingPointMuMu 
	VariableInterval = VariableIntervalMuMu 
	VariablePointsToTest= VariablePointsToTestMuMu
	preselection = preselectionmumu
	BGErrorFactor =  ErrorFactorMuMu	
if AnalysisType=="MuNu" or AnalysisType =="Munu" or AnalysisType=="munu":
	CutVariables = CutVariablesMuNu
	VariableStartingPoint = VariableStartingPointMuNu 
	VariableInterval = VariableIntervalMuNu 
	VariablePointsToTest= VariablePointsToTestMuNu	
	preselection = preselectionmunu
	BGErrorFactor =  ErrorFactorMuNu	

if AnalysisType!="MuNu" and AnalysisType !="Munu" and AnalysisType!="munu" and AnalysisType!="MuMu" and AnalysisType !="MuMu" and AnalysisType!="mumu":
	print("\n\nAnalysis Type must be specified as MuMu or MuNu\n\n Example: \n >> python OptimizationUtility.py MuNu\n\nProcess Exiting")
	sys.exit(0)


WhatType=['Background','Signal','CollisionData'] # So that WhatType[SigOrBG[x]] returns string "Signal" or "Background"

LQList=[]
SBList=[]

# Ideal condtions for CLA optimization
ErrorInSigEff=0.0 # Fraction, multiplies directly by signal efficiency
ErrInNBKG= 0.0  # Fraction, multiplies directly by NBKG

fileinfo = os.popen('ls '+FileLocation).readlines()
dirfiles = []
SignalType = []
SigOrBG = []
for x in fileinfo:
	dirfiles.append( x.replace('\n',''))
	tocontinue = 1
	for k in KeepFiles:
		if k in x:
			tocontinue = 0
	if (tocontinue):
		continue
	SignalType.append(x.replace('.root','').replace('\n',''))
	if 'LQ' in x:
		SigOrBG.append(1)
	else:
		SigOrBG.append(0)
	
# Get list of Leptoqark types and ALLBKG

if AnalysisType=="MuNu" or AnalysisType =="Munu" or AnalysisType=="munu":
	for x in range(len(SignalType)):
		if "Data" in SignalType[x] or "Summer" in SignalType[x]:
			continue
		if "LQ" in SignalType[x] and "BetaHalf" in SignalType[x]: 
			LQList.append(SignalType[x])
			SBList.append(SigOrBG[x])
		if "LQ" not in SignalType[x]: 
			LQList.append(SignalType[x])
			SBList.append(SigOrBG[x])

	SigOrBG=SBList
	SignalType=LQList

if AnalysisType=="MuMu" or AnalysisType =="MuMu" or AnalysisType=="mumu":
	for x in range(len(SignalType)):
		if "Data" in SignalType[x] or "Summer" in SignalType[x]:
			continue
		if "LQ" in SignalType[x] and "BetaHalf" not in SignalType[x]: 
			LQList.append(SignalType[x])
			SBList.append(SigOrBG[x])
		if "LQ" not in SignalType[x]: 
			LQList.append(SignalType[x])
			SBList.append(SigOrBG[x])

	SigOrBG=SBList
	SignalType=LQList

print LQList

def multi_for(iterables):
	if not iterables:
		yield ()
	else:
		for item in iterables[0]:
			for rest_tuple in multi_for(iterables[1:]):
				yield (item,) + rest_tuple

BackgroundValues = []
SignalValues = []
SignifValues = []

SignifValuesSSB = []
SignifValuesSB = []
SignifValuesSSBdB2 = []

cuts = []
n = 0
for i in multi_for(map(xrange, VariablePointsToTest)):
	cuts.append('')
for i in multi_for(map(xrange, VariablePointsToTest)):
	#print n
	cuts[n] += "1.0"
	for c in range(len(i)):
		cuts[n]+="*("+CutVariables[c] +' > ' +str((VariableStartingPoint[c])+VariableInterval[c]*i[c] )+")"
	#cuts.append(cut)
	BackgroundValues.append(0.0)
	SignalValues.append(0.0)
	SignifValues.append(0.0)
	#print n
	#print cuts[n]
	n = n + 1

numcut = len(cuts)

	#print cut

for x in range(len(SignalType)):
	if SigOrBG[x] ==1:
		continue
	print SignalType[x]
	sfile = FileLocation+'/'+SignalType[x]+'.root'
	f = TFile.Open(sfile)
	t = f.Get("PhysicalVariables")
	fout = TFile("/tmp/"+person+"/"+SignalType[x]+"_tmp.root","RECREATE")
	scalefactor = 1.0
	if 'TTBar' in SignalType[x]: 
		scalefactor = ttbarscale
	if 'ZJets' in SignalType[x]: 
		scalefactor = zscale
	if 'WJets' in SignalType[x]: 
		scalefactor = wscale
	print "Reducing tree with preselection ... " 
	T = t.CopyTree(preselection)
	h = TH1F('h','h',1,0,2)
	print "Evaluating Cuts... " 
	for y in range(len(cuts)):
		T.Project('h','1.0',cut_mc+'*'+str(scalefactor)+"*"+cuts[y])
		BackgroundValues[y]+=(h.Integral())
	del t
	del T
	del h
num = '0123456789'


for x in range(len(SignalType)):
	if SigOrBG[x] ==0:
		continue
	print SignalType[x]
	sig = SignalType[x]
	mass = ''
	for q in sig:
		if q in num:
			mass +=q
	mass = float(mass)
			
	BestSignif = -999.9
	BestSignifSB = -999.9
	BestSignifSSB = -999.9
	BestSignifSSBdB2 = -999.9

	BestCut = ''
	BestCutSB = ''
	BestCutSSB = ''
	BestCutSSBdB2 = ''

	sfile = FileLocation+'/'+SignalType[x]+'.root'
	f = TFile.Open(sfile)
	t = f.Get("PhysicalVariables")
	fout = TFile("/tmp/"+person+"/"+SignalType[x]+"_tmp.root","RECREATE")
	scalefactor = 1.0
	print "Reducing tree with preselection ... " 
	T = t.CopyTree(preselection)
	h = TH1F('h','h',1,0,2)
	print "Evaluating Cuts... " 

	for y in range(len(cuts)):
		T.Project('h','1.0',cut_mc+'*'+str(scalefactor)+"*"+cuts[y])
		SignalValues[y]=(h.Integral())
		SignifValues[y] = SignalValues[y] / math.sqrt(BackgroundValues[y] + SignalValues[y])
		
		SignifValuesSSB[y] = SignalValues[y] / math.sqrt(BackgroundValues[y] + SignalValues[y])
		SignifValuesSB[y] = SignalValues[y] / math.sqrt(BackgroundValues[y] )
		SignifValuesSSBdB2[y] = SignalValues[y] / math.sqrt( BackgroundValues[y] + BGErrorFactor*BackgroundValues[y]*BackgroundValues[y] +  SignalValues[y])
		
		if SignifValues[y]>BestSignif:
			BestSignif = SignifValues[y]
			BestCut = cuts[y]

		if SignifValuesSB[y]>BestSignifSB:
			BestSignifSB = SignifValuesSB[y]
			BestCutSB = cuts[y]
			
		if SignifValuesSSB[y]>BestSignifSSB:
			BestSignifSSB = SignifValuesSSB[y]
			BestCutSSB = cuts[y]
						
		if SignifValuesSSBdB2[y]>BestSignifSSBdB2:
			BestSignifSSBdB2 = SignifValuesSSBdB2[y]
			BestCutSSBdB2 = cuts[y]
			
	del T
	del t
	del h
	print BestCut
	print BestSignif
	
	logout.write(SignalType[x]+'\n')
	logout.write(BestCut+'\n\n')
	
	logoutSB.write(SignalType[x]+'\n')
	logoutSB.write(BestCutSB+'\n\n')

	logoutSSB.write(SignalType[x]+'\n')
	logoutSSB.write(BestCutSSB+'\n\n')	

	logoutSSBdB2.write(SignalType[x]+'\n')
	logoutSSBdB2.write(BestCutSSBdB2+'\n\n')	

logoutSB.close()
logoutSSB.close()
logoutSSBdB2.close()
logout.close()
