#############################################################################
## This file creates scripts for optimization with signicance and CLA       ##
## Leptoquark NTuples are interpreted from NTupleInfo.csv file              ##
## Background is utilized with the ALLBKG Sample - MUST BE PRESENT         ##
#############################################################################

import os # For direcory scanning abilities, etc
import sys
AnalysisType=sys.argv[1] 
print(AnalysisType)
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


#=======================================================================================================
#   Here we will build a full optimization file from a fragment file
#=======================================================================================================

for y in range(len(SignalType)):
	#SIGNAL
	if SignalType[y]=='ALLBKG':
		continue
	SIG=SignalType[y]
	BAK='ALLBKG'
	basic_w = open(AnalysisDirectory+"Stage2_Optimization/"+AnalysisType+"/OptimizationCLA_"+SIG+".C", 'w')

	basic_w.write(com + bar + cr +com +wsp+"Optimization from Tree Formatted Files"+cr+com+wsp+"DBaumgartel - Oct 07, 2010 - Fall 2010 LQ Analysis"+cr+com+bar+cr*2)

	basic_w.write('#include <iostream>\n#include <iomanip>\n#include \"TROOT.h\"\n#include \"TH2F.h\"\n#include \"TGraph.h\"\n#include \"TTree.h\"\n#include \"TFile.h\"\n#include <sstream>\n#include <fstream>\n#include "CL95cms.C"\n\n')

	basic_w.write('\n TFile* f__'+SIG+' = new TFile(\"'+FileLocation+'/'+SIG+'.root\",\"READ\");\n\n')
	basic_w.write('\n TFile* f__'+BAK+' = new TFile(\"'+FileLocation+'/'+BAK+'.root\",\"READ\");\n\n')


	basic_w.write('void Optimize()\n{\n\n')
	basic_w.write('std::ostringstream strs;\nTString cutstring;\nstring cut;\nstring precut;\nTString precutstring;\n\n')

	for x in range(len(CutVariables)):
		basic_w.write(' int int_'+CutVariables[x]+' = 0;\n')

	for z in range(len(CutVariables)):
		basic_w.write('\n float '+CutVariables[z]+'_startingpoint = '+ `VariableStartingPoint[z]` +';')
		basic_w.write('\n float '+CutVariables[z]+'_interval = '+ `VariableInterval[z]` +';')
		basic_w.write('\n const int '+CutVariables[z]+'_points = '+ `VariablePointsToTest[z]` +';')
		basic_w.write('\n float '+CutVariables[z]+'_Cut['+CutVariables[z]+'_points];\n\n') 

	basic_w.write('\n\n') 
	dummy2=['S','B','S_Pass_MC','B_Pass_MC']
	for x in range(len(dummy2)):
		basic_w.write('\n float '+dummy2[x])
		for z in range(len(CutVariables)):
			basic_w.write('['+CutVariables[z]+'_points]')
		basic_w.write(';')
	basic_w.write(2*cr) 
	for z in range(len(CutVariables)):
		basic_w.write('\n '+z*''+'for (int_'+CutVariables[z]+'=0; int_'+CutVariables[z]+' < '+CutVariables[z]+'_points; int_'+CutVariables[z]+'++){')
	for x in range(len(dummy2)):
		basic_w.write('\n ' + len(CutVariables)*'' +dummy2[x])
		for z in range(len(CutVariables)):
			basic_w.write('[int_'+CutVariables[z]+']')
		basic_w.write('=0;')
	for z in range(len(CutVariables)):
		basic_w.write('\n '+(len(CutVariables)-z)*''+'}')
	for z in range(len(CutVariables)):
		basic_w.write('\n'+'for (int_'+CutVariables[z]+'=0; int_'+CutVariables[z]+' < '+CutVariables[z]+'_points; int_'+CutVariables[z]+'++){')
		basic_w.write('\n '+CutVariables[z]+'_Cut[int_'+CutVariables[z]+'] = '+CutVariables[z]+'_startingpoint + '+CutVariables[z]+'_interval*int_'+CutVariables[z]+';') 
		basic_w.write('\n }\n')
	braces = ''
	for z in range(len(CutVariables)):
		braces = braces+'[int_' + CutVariables[z] +']'   
	basic_w.write(2*cr + com +BAR +cr+ com + wsp + " ** SIGNAL CALCULATIONS HERE ** " + cr + com + BAR + 2*cr)
	basic_w.write('\nTTree* Var__orig__'+SIG+' = (TTree*)f__'+SIG+'->Get(\"PhysicalVariables\");')
	basic_w.write('\nTH1D* h__'+SIG+'= new TH1D(\"h__'+SIG+'\",\"title\",5,0,10);\n')
	basic_w.write('\nVar__orig__'+SIG+'->Project("h__'+SIG+'\",\"5",\"weight*('+`IntLumi`+')*Events_Orig/Events_AfterLJ");')
	basic_w.write('\nconst Double_t S_orig =h__'+SIG+'->Integral();')
	basic_w.write('\nstd::cout<<\">> Evaluating For '+SIG+' Type '+SIG +'\"<<std::endl;\n')
	basic_w.write('\nprecut = \"1.0')
	for x in range(len(PrecutVariables)):
		basic_w.write('*('+PrecutVariables[x]+'>'+`PrecutMinValues[x]`+')')
	for x in range(len(CutVariables)):
		basic_w.write('*('+CutVariables[x]+'>'+`VariableStartingPoint[x]`+')')
	basic_w.write('\";')
	basic_w.write('\nprecutstring = precut;\n') 
	
	basic_w.write('\nTFile f__temp__'+SIG+'("temp__'+SIG+'.root","recreate");')
	basic_w.write('\nTTree* Var__'+SIG+' = Var__orig__'+SIG+' ->CopyTree(precutstring);\n')

	basic_w.write('\nstd::cout<<\"Precuts Complete. \"<<Var__orig__'+SIG+'->GetEntries()<<\"  MC Events Reduced to \"<<Var__'+SIG+'->GetEntries()<<std::endl;\n')

	basic_w.write(2*cr + com +bar +cr+ com + wsp + "Loop over Cut vals, set Cut String, Evaluate " + cr + com + bar + 2*cr)

	basic_w.write('\nTH1D* h__Op__'+SIG+'= new TH1D(\"h__Op__'+SIG+'\",\"title\",5,0,10);\n\n')
			
	for w in range(len(CutVariables)):
		basic_w.write('\n'+'for (int_'+CutVariables[w]+'=0; int_'+CutVariables[w]+' < '+CutVariables[w]+'_points; int_'+CutVariables[w]+'++){')

	for x in range(len(CutVariables)):
		basic_w.write('strs << '+CutVariables[x]+'_Cut[int_'+CutVariables[x]+'];  std::string str'+`x`+' = strs.str();  strs.str("");\n')

	basic_w.write('\ncut = \"weight*('+`IntLumi`+')')

	for x in range(len(CutVariables)):
		basic_w.write('*('+CutVariables[x]+'>\" + str'+`x`+' + \")')
	basic_w.write('\";')

	basic_w.write('\ncutstring = cut;\n') 	
	basic_w.write('\nVar__'+SIG+'->Project("h__Op__'+SIG+'","5",cutstring);\n')

	basic_w.write('S'+braces+'=h__Op__'+SIG+'->Integral();')
	basic_w.write('\n'+ (len(CutVariables))*'}')
	basic_w.write('\nstd::cout<<\"Optimization Cuts Complete\"<<std::endl;\n')

	# BAKGROUND
	basic_w.write(2*cr + com +BAR +cr+ com + wsp + " ** BACKGROUND CALCULATIONS HERE ** " + cr + com + BAR + 2*cr)
	basic_w.write('\nTTree* Var__orig__'+BAK+' = (TTree*)f__'+BAK+'->Get(\"PhysicalVariables\");')
	basic_w.write('\nTH1D* h__'+BAK+'= new TH1D(\"h__'+BAK+'\",\"title\",5,0,10);\n')

	basic_w.write('\nstd::cout<<\">> Evaluating For '+BAK+' Type '+BAK +'\"<<std::endl;\n')
	basic_w.write('\nprecut = \"1.0')
	for x in range(len(PrecutVariables)):
		basic_w.write('*('+PrecutVariables[x]+'>'+`PrecutMinValues[x]`+')')
	for x in range(len(CutVariables)):
		basic_w.write('*('+CutVariables[x]+'>'+`VariableStartingPoint[x]`+')')
	basic_w.write('\";')
	basic_w.write('\nprecutstring = precut;\n') 
	
	basic_w.write('\nTFile f__temp__'+BAK+'("temp__'+BAK+'.root","recreate");')
	basic_w.write('\nTTree* Var__'+BAK+' = Var__orig__'+BAK+' ->CopyTree(precutstring);\n')

	basic_w.write('\nstd::cout<<\"Precuts Complete. \"<<Var__orig__'+BAK+'->GetEntries()<<\"  MC Events Reduced to \"<<Var__'+BAK+'->GetEntries()<<std::endl;\n')

	basic_w.write(2*cr + com +bar +cr+ com + wsp + "Loop over Cut vals, set Cut String, Evaluate " + cr + com + bar + 2*cr)

	basic_w.write('\nTH1D* h__Op__'+BAK+'= new TH1D(\"h__Op__'+BAK+'\",\"title\",5,0,10);\n\n')
			
	for w in range(len(CutVariables)):
		basic_w.write('\n'+'for (int_'+CutVariables[w]+'=0; int_'+CutVariables[w]+' < '+CutVariables[w]+'_points; int_'+CutVariables[w]+'++){')
			
	for x in range(len(CutVariables)):
		basic_w.write('strs << '+CutVariables[x]+'_Cut[int_'+CutVariables[x]+'];  std::string str'+`x`+' = strs.str();  strs.str("");\n')


	basic_w.write('\ncut = \"weight*('+`IntLumi`+')')

	for x in range(len(CutVariables)):
		basic_w.write('*('+CutVariables[x]+'>\" + str'+`x`+' + \")')
	basic_w.write('\";')

	basic_w.write('\ncutstring = cut;\n') 	
	basic_w.write('\nVar__'+BAK+'->Project("h__Op__'+BAK+'","5",cutstring);\n')

	basic_w.write('B'+braces+'=h__Op__'+BAK+'->Integral();')


	basic_w.write('\n'+ (len(CutVariables))*'}')
	basic_w.write('\nstd::cout<<\"Optimization Cuts Complete\"<<std::endl;\n\n\n')

### Below the part of the script is printed which finds the optimum cut based on significance...


	for x in range(len(CutVariables)):
		basic_w.write('\n int ideal_int_'+CutVariables[x]+'=0.0;')
	basic_w.write('\n float Signif_max =0.0;')
	basic_w.write('\n float Signif=0.0;\n\n')

	for x in range(len(CutVariables)):
		basic_w.write('\n int idealCLA_int_'+CutVariables[x]+'=0.0;')
	basic_w.write('\n float clamax =9999999.0;')
	basic_w.write('\n float claval=0.0;\n\n')

	basic_w.write('std::cout<<"\\n\\nDetermining optimal cut values for the discriminating variables ...\\n\\n"<<std::endl;\n')
		
	for y in range(len(CutVariables)):
		basic_w.write('\n'+'for (int_'+CutVariables[y]+'=0; int_'+CutVariables[y]+' < '+CutVariables[y]+'_points; int_'+CutVariables[y]+'++){\n')

	brac1 = ''		
	for x in range(len(CutVariables)):
		brac1 = brac1 + '[int_'+CutVariables[x]+']'	
	SigNow='Signif'
	CLANow='claval'
	BNow ='B'+brac1
	SNow ='S'+brac1
	basic_w.write('\n if ('+SNow+' ==0) continue;\n')
	basic_w.write('\n'+SigNow+' = '+SNow+'*pow('+SNow+'+'+BNow+',-.5);\n')
	basic_w.write('if('+SigNow+'>Signif_max) {\nSignif_max='+SigNow+';\n')
	for x in range(len(CutVariables)):
		basic_w.write('\n ideal_int_'+CutVariables[x]+'=int_'+CutVariables[x]+';')
	basic_w.write('}')

	basic_w.write('\n\n\n'+CLANow+' = CLA('+str(IntLumi)+','+str(IntLumiFracError*IntLumi)+','+SNow+'/(1.0*S_orig),0,'+BNow+',0,1);\n\n')
	basic_w.write('if('+CLANow+'<clamax) {\nclamax='+CLANow+';\n')
	for x in range(len(CutVariables)):
		basic_w.write('\n idealCLA_int_'+CutVariables[x]+'=int_'+CutVariables[x]+';')
	basic_w.write(len(CutVariables)*'}'+'}')
		
### Below the part of the script is printed which displays the results of signifiance optimization to screen...
	basic_w.write('\n\nstd::cout<<\">>'+bar+'\"<<std::endl;\nstd::cout<<">>'+wsp+'Significance maximization cuts results as follows:"<<std::endl;\nstd::cout<<\">>'+bar+'\"<<std::endl;\n')
	basic_w.write('std::cout<<"    "<<std::endl;\n')
	for x in range(len(CutVariables)):
		basic_w.write('std::cout<<">> Best ' +CutVariables[x]+ ' Cut:  ' +CutVariables[x]+ '   > "<<'+CutVariables[x]+'_Cut[ideal_int_'+CutVariables[x]+']<<std::endl;\n')		
		basic_w.write('std::cout<<"    "<<std::endl;\n')
	basic_w.write('std::cout<<">> Significance at Optimized Cut Levels:   S = "<<Signif_max<<std::endl;\n\n')					
	basic_w.write('\n\nstd::cout<<\">>'+bar+'\"<<std::endl;\n\n')

	basic_w.write('\n\nstd::cout<<\">>'+bar+'\"<<std::endl;\nstd::cout<<">>'+wsp+'CLA maximization cuts results as follows:"<<std::endl;\nstd::cout<<\">>'+bar+'\"<<std::endl;\n')
	basic_w.write('std::cout<<"    "<<std::endl;\n')
	for x in range(len(CutVariables)):
		basic_w.write('std::cout<<">> Best ' +CutVariables[x]+ ' Cut:  ' +CutVariables[x]+ '   > "<<'+CutVariables[x]+'_Cut[idealCLA_int_'+CutVariables[x]+']<<std::endl;\n')		
		basic_w.write('std::cout<<"    "<<std::endl;\n')
	basic_w.write('std::cout<<">> CLA at Optimized Cut Levels:   CLA = "<<clamax<<std::endl;\n\n')					
	basic_w.write('\n\nstd::cout<<\">>'+BAR+'\"<<std::endl;\n\n')

	basic_w.write('\nstd::cout<<"Analysis Complete for '+SignalType[z]+'\"<<std::endl;\n\n}')
	basic_w.close()


# BCPP - clean up the C++ output. Comment this part if you don't have BCPP installed and don't want it. 

	os.system("mv "+AnalysisDirectory+"Stage2_Optimization/"+AnalysisType+"/OptimizationCLA_"+SIG+".C "+AnalysisDirectory+"Stage2_Optimization/"+AnalysisType+"/temptest.C")
	os.system("bcpp "+AnalysisDirectory+"Stage2_Optimization/"+AnalysisType+"/temptest.C "+AnalysisDirectory+"Stage2_Optimization/"+AnalysisType+"/OptimizationCLA_"+SIG+".C")
	os.system("rm "+AnalysisDirectory+"Stage2_Optimization/"+AnalysisType+"/temptest.C ")

# END BCPP


for z in range(len(SignalType)):
	if (SigOrBG[z]==1):
		RootCommands_w = open(AnalysisDirectory+"Stage2_Optimization/"+AnalysisType+"/RootOptCommandsCLA_"+SignalType[z],"w")
		RootCommands_w.write('{\n\n') 
		RootLinesToAdd = '\ngROOT->ProcessLine(\".L OptimizationCLA_'+SignalType[z]+'.C++\");\ngROOT->ProcessLine(\"Optimize()");\ngROOT->ProcessLine(\"gROOT->Reset()\");\ngROOT->ProcessLine(\"gROOT->Clear()\");\n'#'gROOT->ProcessLine(\".q");\n\n'
		RootCommands_w.write(RootLinesToAdd)
		RootCommands_w.write('gROOT->ProcessLine(\".q");\n\n')
		RootCommands_w.write('\n\n}')
		RootCommands_w.close()

dirList=os.listdir(AnalysisDirectory+"Stage2_Optimization/"+AnalysisType)
for item in dirList:
	if "CLA" in item and item!="CLA.C" and "Root" not in item and "Run" not in item:
		scpfile = item.replace("CLA","SCP")
		filecla = open(AnalysisDirectory+"Stage2_Optimization/"+AnalysisType+"/"+item)
		filescp = open(AnalysisDirectory+"Stage2_Optimization/"+AnalysisType+"/"+scpfile,"w")
		for line in filecla:
			line = line.replace("CLA","scp")
			line = line.replace("cla","scp")
			if "float scpmax" in line:
				line = "float scpmax = -1.0;\n"
			if "scpval =" in line:
				line2 = line.split("=")
				line = line.replace(line2[-1],'scp('+SNow+','+BNow+','+str(BGPseudoError)+'*'+BNow+',0);\n')
			if "scpval" in line and "scpmax" in line:
				line = line.replace('<','>')
			filescp.write(line)
		filescp.close()
		filecla.close()
	if "CLA" in item and "Root" in item:
		scpfile = item.replace("CLA","SCP")
		filecla = open(AnalysisDirectory+"Stage2_Optimization/"+AnalysisType+"/"+item)
		filescp = open(AnalysisDirectory+"Stage2_Optimization/"+AnalysisType+"/"+scpfile,"w")
		for line in filecla:
			line = line.replace("CLA","SCP")
			line = line.replace("++","")
			filescp.write(line)
		filescp.close()
		filecla.close()

runfile = open(AnalysisDirectory+"Stage2_Optimization/"+AnalysisType+"/RunOpt.sh","w")
runfile.write("#!/bin/sh\n\n")
dirList=os.listdir(AnalysisDirectory+"Stage2_Optimization/"+AnalysisType)
dirList.sort()
for item in dirList:
	if "OptCommands" in item:
		name = item.replace("optCommands","")
		name = "Log_"+name+".txt"
		runfile.write("\nroot -l "+item+" > " +name)
runfile.write('\n\ncat Log*CLA*txt > Log_Total_CLA.txt')
runfile.write('\n\ncat Log*SCP*txt > Log_Total_SCP.txt')
runfile.write('\n\ngrep ">>" Log_Total_CLA.txt > Log_Summary_CLA.txt')
runfile.write('\n\ngrep ">>" Log_Total_SCP.txt > Log_Summary_SCP.txt')
runfile.close()







