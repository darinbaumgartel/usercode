#############################################################################
## This file creates scripts for optimization with signicance and CLA       ##
## Leptoquark NTuples are interpreted from NTupleInfo.csv file              ##
## Background is utilized with the ALLBKG Sample - MUST BE PRESENT         ##
#############################################################################

import os # For direcory scanning abilities, etc
import sys
AnalysisType=sys.argv[1] 
if AnalysisType == "":
	print("\n\nYou need to specify an analysis type\n\n Example: \n >> python OptimizationUtility.py MuNu\n\nProcess Exiting")
	sys.exit(0)
from time import strftime
from GetDirInfo import *
from CSVInterpreter import *

if AnalysisType=="MuNu" or AnalysisType =="Munu" or AnalysisType=="munu":
	from OptimizationInfo_MuNu import *
if AnalysisType=="MuMu" or AnalysisType =="MuMu" or AnalysisType=="mumu":
	from OptimizationInfo_MuMu import *
if AnalysisType!="MuNu" and AnalysisType !="Munu" and AnalysisType!="munu" and AnalysisType!="MuMu" and AnalysisType !="MuMu" and AnalysisType!="mumu":
	print("\n\nAnalysis Type must be specified as MuMu or MuNu\n\n Example: \n >> python OptimizationUtility.py MuNu\n\nProcess Exiting")
	sys.exit(0)

from RunInformation import *

FileLocation=AnalysisDirectory+"Stage1_NTupleAnalysis/CurrentRootFiles"
WhatType=['Background','Signal','CollisionData'] # So that WhatType[SigOrBG[x]] returns string "Signal" or "Background"

LQList=['']
SBList=[5]

# Ideal condtions for CLA optimization
ErrorInSigEff=0.0 # Fraction, multiplies directly by signal efficiency
ErrInNBKG= 0.0  # Fraction, multiplies directly by NBKG


# Get list of Leptoqark types and ALLBKG
if AnalysisType=="MuNu" or AnalysisType =="Munu" or AnalysisType=="munu":
	for x in range(len(SignalType)):
		if SigOrBG[x]==1:
			if "LQ" in SignalType[x] and "MuNuJJFilter" in SignalType[x]: 
				LQList.append(SignalType[x])
				SBList.append(SigOrBG[x])
	LQList=LQList[1:]
	SBList=SBList[1:]
	LQList.append('ALLBKG')
	SBList.append(0)
	SigOrBG=SBList
	SignalType=LQList

if AnalysisType=="MuMu" or AnalysisType =="MuMu" or AnalysisType=="mumu":
	for x in range(len(SignalType)):
		if SigOrBG[x]==1:
			if "LQ" in SignalType[x] and "MuNuJJFilter" not in SignalType[x]: 
				LQList.append(SignalType[x])
				SBList.append(SigOrBG[x])
	LQList=LQList[1:]
	SBList=SBList[1:]
	LQList.append('ALLBKG')
	SBList.append(0)
	SigOrBG=SBList
	SignalType=LQList


# Store some shorthand

com = "//"   # C++ comment
bar = "-"*100 # horizontal bar
BAR = "="*100 # horizontal bar
wsp = " "*20 # 20 spaces whitespace
cr = "\n" # new line /return
pbar = "std::cout<<\""+bar+'\"<<std::endl;'
co = 'std::cout<<'
ce = '<<std::endl;\n'
cut=[]
texbrk='<<"\\t&\\t"<<'
texend='<<"\\\\\\\\\\\\hline"'
cbrk = "<<"

for x in NonOptCutLevels:
	cut.append(x)

for x in CutVariables:
	cut.append('('+x+' > CutValue_'+x+')')

#print(cut)

def makeentry(q,m,whichtype):
	q = str(q)
	m = str(m)
	stringret = ""
	stringret = cr+com+bar+cr+com+2*wsp+q+cr+com+bar+2*cr
	stringret = stringret + '\nTFile f__'+q+' (\"'+FileLocation+'/'+q+'.root\");'
	stringret = stringret + '\nTTree* Var__'+q+' = (TTree*) f__'+q+'->Get("PhysicalVariables");'
	stringret = stringret + '\nTH1D* h__'+q+' = new TH1D("h__'+q+'","",5,0,10);\n'
	for x in range(len(cut)):
		stringret = stringret + '\nVar__'+q+'->Project("h__'+q+'","5",cut_'+whichtype+str(x)+');'
		stringret = stringret + '\nDouble_t '+q+'_'+str(x) + ' = h__'+q+'->'+m+';'
		stringret = stringret + '\nDouble_t '+q+'_'+str(x) + '_MC = h__'+q+'->GetEntries();\n'
		stringret = stringret + 'if ('+q+'_'+str(x)+'_MC==0) Double_t '+q+'_'+str(x)+'_MC_fracerr = 0.0; else Double_t '+q+'_'+str(x)+'_MC_fracerr = 1/sqrt('+q+'_'+str(x)+'_MC);'
	return stringret

def errorentry(q,maxval,numcutsval):
	stringret = ""
	stringret = stringret + '\n\nif ('+q+'_0_MC>=1) Double_t '+q+'Err = '+q+'_'+numcutsval+'/sqrt('+q+'_0_MC);'
	stringret = stringret + '\nif ('+q+'_0_MC<1) Double_t '+q+'Err = 0;'
	return stringret

def maketotal(n):
	n = str(n)
	stringret = 2*cr
	stringret = stringret + 'Double_t Total_'+n+' = ('
	r=1
	l = len(BackgroundTypes)
	for a in BackgroundTypes:
		stringret = stringret + a +'_'+n+ int(bool(l-r))*' + '
		r=r+1
	stringret = stringret + ');\n'
	stringret = stringret + 'Double_t Total_'+n+'_err = sqrt('

	r=1
	l = len(BackgroundTypes)
	for a in BackgroundTypes:
		A = a+'_'+n
		Aerr = A+'_MC_fracerr'
		AAerr = A + '*' +Aerr
		stringret = stringret + AAerr+'*'+AAerr+ int(bool(l-r))*' + '
		r=r+1
	stringret = stringret+');'

	return stringret

def Qt(a):
	stringret = '\"'+a+'\"'
	return stringret

def texlineq(v):
	stringret = co
	for a in v:
		stringret = stringret + Qt(a) + texbrk
	stringret = stringret +'" "'+ texend + ce + cr
	return stringret

def texlinen(v,n):
	stringret = co + Qt(str(n))

	for a in v:
		an = a + '_'+str(n)
		anerr = an + '*'+an+'_MC_fracerr'
		if a != 'CurrentData' and a !='Total':
			stringret = stringret + texbrk + an + cbrk+ Qt('$\\\\pm$')+cbrk + anerr
		if a == 'CurrentData':
			stringret = stringret + texbrk + an
		if a == 'Total':
			stringret = stringret + texbrk + an + cbrk + Qt('$\\\\pm$') + cbrk + an + '_err'
	stringret = stringret + texend + ce + cr
	return stringret

#=======================================================================================================
#   Here we will build a full optimization file 
#=======================================================================================================

for y in range(len(SignalType)):
	#SIGNAL
	if SignalType[y]=='ALLBKG':
		continue
	SIG=SignalType[y]
	BAK='ALLBKG'
	basic_w = open(AnalysisDirectory+"Stage3_MCCutFlow/"+AnalysisType+"/CutFlow_"+SIG+".C", 'w')

#	testfile = open(AnalysisDirectory+"Stage2_Optimization/"+AnalysisType+"/Log_RootOptCommandsCLA_"+SignalType[y]+".txt", 'r')
	testfile = open(AnalysisDirectory+"Stage2_Optimization/"+AnalysisType+"/Log_RootOptCommandsCLA_LQToCMu_MuNuJJFilter_M_300.txt", 'r')
	for line in testfile:
		if "Best" in line:
			thisvar = (line.split()[-3])
			thisval = line.split()[-1]
			for x in cut:
				if thisvar in x:
					xx=x.replace("CutValue_"+thisvar,thisval)
					for place in range(len(cut)):
						cut[place]= cut[place].replace(x,xx)
	basic_w.write('{'+2*cr+pbar + 2*cr)

	currentcut=''
	ind=0
	for x in cut:
		if x == cut[0]:
			currentcut = currentcut+x
		else:
			currentcut = currentcut + "*" +x

		basic_w.write('\nTString cut_data'+str(ind)+' = "'+currentcut+'";\n' )
		ind=ind+1

	currentcut=''
	ind=0
	for x in cut:
		if x == cut[0]:
			currentcut = currentcut+x
		else:
			currentcut = currentcut + "*" +x

		basic_w.write('\nTString cut_mc'+str(ind)+' = "(weight*'+str(IntLumi)+')*'+currentcut+'";\n' )
		ind=ind+1

	basic_w.write(makeentry("CurrentData","GetEntries()",'data'))
	basic_w.write(makeentry(SignalType[y],"Integral()",'mc'))

	for a in BackgroundTypes:
		basic_w.write(makeentry(a,"Integral()",'mc'))

	basic_w.write(3*cr+com+BAR+cr+com+2*wsp+'STATISTICS ...'+cr+com+BAR+2*cr)
	
	mval = str(ind-1)
	

	basic_w.write('\nDouble_t Seff = ('+SignalType[y]+'_'+mval+'/'+SignalType[y]+'_0);')
	basic_w.write('\nDouble_t SMCOrig = '+SignalType[y]+'_0_MC/Seff;')
	basic_w.write('\nDouble_t SMCAfter = '+SignalType[y]+'_0_MC;')
	basic_w.write('\nDouble_t ErrSeff = Seff*sqrt( 1/SMCAfter + 1/SMCOrig) ;')

	for a in BackgroundTypes:
		basic_w.write(errorentry(a,mval,str(len(cut)-1)))
	
	for x in range(len(cut)):
		basic_w.write(maketotal(x))
	
	basic_w.write(3*cr+com+BAR+cr+com+2*wsp+'PRINT A TABLE ...'+cr+com+BAR+2*cr)
	basic_w.write( 2*cr + pbar+cr + co +'"'+wsp + SignalType[y] + '"'+ce+ pbar+cr+co + '"   "'+ce+2*cr)

	header = ['cut','Data']
	for a in BackgroundTypes:
		header.append(a)
	header.append('AllBG')

	basic_w.write(texlineq(header))

	
	for n in range(len(cut)):
		tline=['CurrentData',SignalType[y]]
		for a in BackgroundTypes:
			tline.append(a)
		tline.append('Total')
		basic_w.write(texlinen(tline,n))

	basic_w.write('\n\ngROOT->ProcessLine(".q");\n\n')
	basic_w.write(cr*2+'}')
