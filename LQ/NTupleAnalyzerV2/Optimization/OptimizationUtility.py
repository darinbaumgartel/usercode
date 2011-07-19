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
FileLocation="/tmp/darinb/NTupleAnalyzer_V00_02_04_Default__2011_07_12_16_27_56/SummaryFiles/"

#print(AnalysisType)
if AnalysisType == "":
	print("\n\nYou need to specify an analysis type\n\n Example: \n >> python OptimizationUtility.py MuNu\n\nProcess Exiting")
	sys.exit(0)
from time import strftime

ttbarscale = 165./121.
wscale = 1.25
zscale = 1.42
CutVariablesMuMu=['ST_pf_mumu','M_muon1muon2'] # Which variables do you want to cut on

VariableStartingPointMuMu = [250,100] # Where to start cutting on the variable 
VariableIntervalMuMu = [5,5] # Intervals in which you will test cuts
VariablePointsToTestMuMu = [2000,30] # Number of cutting points to test at the given interval

CutVariables=['ST_pf_munu','MT_muon1pfMET'] # Which variables do you want to cut on

VariableInterval = [10,10] # Intervals in which you will test cuts
VariableStartingPoint = [170,120] # Where to start cutting on the variable 
VariablePointsToTest = [75,20] # Number of cutting points to test at the given interval

person = (os.popen("whoami").readlines())[0].replace('\n','')

# Other variable to precut on as they appear in the root file (these are not variable cuts, they are single static cuts):
lumi= 964.0

preselectionmumu = str(lumi)+'*weight*((Pt_muon1>40)*(Pt_muon2>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_mumu>250)*(M_muon1muon2>100)*((abs(Eta_muon1)<2.1)||(abs(Eta_muon2)<2.1)))'
preselectionmunu = str(lumi)+'*weight*((Pt_muon1>40)*(Pt_muon2<15.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))'


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


if AnalysisType=="MuMu" or AnalysisType =="MuMu" or AnalysisType=="mumu":
	CutVariables = CutVariablesMuMu
	VariableStartingPoint = VariableStartingPointMuMu 
	VariableInterval = VariableIntervalMuMu 
	VariablePointsToTest= VariablePointsToTestMuMu
	preselection = preselectionmumu
if AnalysisType=="MuNu" or AnalysisType =="Munu" or AnalysisType=="munu":
	CutVariables = CutVariablesMuNu
	VariableStartingPoint = VariableStartingPointMuNu 
	VariableInterval = VariableIntervalMuNu 
	VariablePointsToTest= VariablePointsToTestMuNu	
	preselection = preselectionmunu
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
		if "LQ" in SignalType[x] and "MuNuJJFilter" in SignalType[x]: 
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
cuts = []
for i in multi_for(map(xrange, VariablePointsToTest)):
	cut = "1.0"
	for c in range(len(i)):
		cut += "*("+CutVariables[c] +' > ' +str((VariableStartingPoint[c])+VariableInterval[c]*i[c] )+")"
	cuts.append(cut)
	BackgroundValues.append(0.0)
	SignalValues.append(0.0)
	SignifValues.append(0.0)

	print cut

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
	T = t.CopyTree(preselection + '*'+str(scalefactor))
	h = TH1D('h','h',1,0,2)
	
	for y in range(len(cuts)):
		T.Project('h','1.0',preselection+"*"+cuts[y])
		BackgroundValues[y]+=(h.Integral())
	
	#print BackgroundValues
	

for x in range(len(SignalType)):
	if SigOrBG[x] ==0:
		continue
	print SignalType[x]
	BestSignif = -999.9
	BestCut = ''
	sfile = FileLocation+'/'+SignalType[x]+'.root'
	f = TFile.Open(sfile)
	t = f.Get("PhysicalVariables")
	fout = TFile("/tmp/"+person+"/"+SignalType[x]+"_tmp.root","RECREATE")
	scalefactor = 1.0
	T = t.CopyTree(preselection + '*'+str(scalefactor))
	h = TH1D('h','h',1,0,2)
	
	for y in range(len(cuts)):
		T.Project('h','1.0',preselection+"*"+cuts[y])
		SignalValues[y]=(h.Integral())
		SignifValues[y] = SignalValues[y] / math.sqrt(BackgroundValues[y] + SignalValues[y])
		if SignifValues[y]>BestSignif:
			BestSignif = SignifValues[y]
			BestCut = cuts[y]
	print BestCut
	print BestSignif
	





