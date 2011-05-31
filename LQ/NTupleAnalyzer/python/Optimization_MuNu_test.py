#############################################################################
## This file creates scripts for optimization with signicance and CLA       ##
## Leptoquark NTuples are interpreted from NTupleInfo.csv file              ##
## Background is utilized with the ALLBKG Sample - MUST BE PRESENT         ##
#############################################################################

import os # For direcory scanning abilities, etc
from time import strftime
from GetDirInfo import *
from CSVInterpreter import *
from OptimizationInfo_MuNu import *
from RunInformation import *

FileLocation=AnalysisDirectory+"Stage1_NTupleAnalysis/CurrentRootFiles"
WhatType=['Background','Signal','CollisionData'] # So that WhatType[SigOrBG[x]] returns string "Signal" or "Background"

LQList=['']
SBList=[5]

# Ideal condtions for CLA optimization
ErrorInSigEff=0.0 # Fraction, multiplies directly by signal efficiency
ErrInNBKG= 0.0  # Fraction, multiplies directly by NBKG


# Get list of Leptoqark types and ALLBKG
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
	basic_w = open(AnalysisDirectory+"Stage2_Optimization/MuNu/BasicAnalysis_"+SIG+".C", 'w')
	basic_w.write('{\n\n')

	basic_w.write(com + bar + cr +com +wsp+"Optimization from Tree Formated Files"+cr+com+wsp+"DBaumgartel - June 14, 2010 - Summer 2010 LQ Analysis"+cr+com+wsp+"To run, simply:   root -l {name of file}.C --- and wait"+cr+com+bar+cr*2)

	basic_w.write('\n TFile f__'+SIG+'(\"'+FileLocation+'/'+SIG+'.root\");\n\n')
	basic_w.write('\n TFile f__'+BAK+'(\"'+FileLocation+'/'+BAK+'.root\");\n\n')
	dummy0 = ['ii','jj','kk','ll','mm','nn']
	for x in range(len(dummy0)):
		basic_w.write(' float '+dummy0[x]+' = 0.0;\n')
	
	basic_w.write(' int SigOrBG = 0;\n')

	for x in range(len(CutVariables)):
		basic_w.write(' int int_'+CutVariables[x]+' = 0;\n')

	for z in range(len(CutVariables)):
		basic_w.write('\n float '+CutVariables[z]+'_startingpoint = '+ `VariableStartingPoint[z]` +';')
		basic_w.write('\n float '+CutVariables[z]+'_interval = '+ `VariableInterval[z]` +';')
		basic_w.write('\n int '+CutVariables[z]+'_points = '+ `VariablePointsToTest[z]` +';')
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
	basic_w.write('\nstd::cout<<\"@@@ Evaluating For '+SIG+' Type '+SIG +'\"<<std::endl;\n')
	basic_w.write('\nstring precut = \"1.0')
	for x in range(len(PrecutVariables)):
		basic_w.write('*('+PrecutVariables[x]+'>'+`PrecutMinValues[x]`+')')
	for x in range(len(CutVariables)):
		basic_w.write('*('+CutVariables[x]+'>'+`VariableStartingPoint[x]`+')')
	basic_w.write('\";')
	basic_w.write('\nTString precutstring = precut;\n') 
	
	basic_w.write('\nTFile f__temp__'+SIG+'("temp__'+SIG+'.root","recreate");')
	basic_w.write('\nTTree* Var__'+SIG+' = Var__orig__'+SIG+' ->CopyTree(precutstring);\n')

	basic_w.write('\nstd::cout<<\"Precuts Complete. \"<<Var__orig__'+SIG+'->GetEntries()<<\"  MC Events Reduced to \"<<Var__'+SIG+'->GetEntries()<<std::endl;\n')

	basic_w.write(2*cr + com +bar +cr+ com + wsp + "Loop over Cut vals, set Cut String, Evaluate " + cr + com + bar + 2*cr)

	basic_w.write('\nTH1D* h__Op__'+SIG+'= new TH1D(\"h__Op__'+SIG+'\",\"title\",5,0,10);\n\n')
			
	for w in range(len(CutVariables)):
		basic_w.write('\n'+'for (int_'+CutVariables[w]+'=0; int_'+CutVariables[w]+' < '+CutVariables[w]+'_points; int_'+CutVariables[w]+'++){')
			
	for x in range(len(CutVariables)):
		basic_w.write('\nstd::ostringstream strs;\n')
		basic_w.write('strs << '+CutVariables[x]+'_Cut[int_'+CutVariables[x]+'];\n')
		basic_w.write('std::string str'+`x`+' = strs.str();\n')


	basic_w.write('\nstring cut = \"weight*('+`IntLumi`+')')

	for x in range(len(CutVariables)):
		basic_w.write('*('+CutVariables[x]+'>\" + str'+`x`+' + \")')
	basic_w.write('\";')

	basic_w.write('\nTString cutstring = cut;\n') 	
	basic_w.write('\nVar__'+SIG+'->Project("h__Op__'+SIG+'","5",cutstring);\n')

	basic_w.write('S'+braces+'=h__Op__'+SIG+'->Integral();')


	basic_w.write('\n'+ (len(CutVariables))*'}')
	basic_w.write('\nstd::cout<<\"Optimization Cuts Complete\"<<std::endl;\n')

	# BAKGROUND
	basic_w.write(2*cr + com +BAR +cr+ com + wsp + " ** BACKGROUND CALCULATIONS HERE ** " + cr + com + BAR + 2*cr)
	basic_w.write('\nTTree* Var__orig__'+BAK+' = (TTree*)f__'+BAK+'->Get(\"PhysicalVariables\");')
	basic_w.write('\nTH1D* h__'+BAK+'= new TH1D(\"h__'+BAK+'\",\"title\",5,0,10);\n')
	basic_w.write('\nVar__orig__'+BAK+'->Project("h__'+BAK+'\",\"5",\"weight*('+`IntLumi`+')*Events_Orig/Events_AfterLJ");')
	basic_w.write('\nconst Double_t B_orig =h__'+BAK+'->Integral();')
	basic_w.write('\nstd::cout<<\"@@@ Evaluating For '+BAK+' Type '+BAK +'\"<<std::endl;\n')
	basic_w.write('\nstring precut = \"1.0')
	for x in range(len(PrecutVariables)):
		basic_w.write('*('+PrecutVariables[x]+'>'+`PrecutMinValues[x]`+')')
	for x in range(len(CutVariables)):
		basic_w.write('*('+CutVariables[x]+'>'+`VariableStartingPoint[x]`+')')
	basic_w.write('\";')
	basic_w.write('\nTString precutstring = precut;\n') 
	
	basic_w.write('\nTFile f__temp__'+BAK+'("temp__'+BAK+'.root","recreate");')
	basic_w.write('\nTTree* Var__'+BAK+' = Var__orig__'+BAK+' ->CopyTree(precutstring);\n')

	basic_w.write('\nstd::cout<<\"Precuts Complete. \"<<Var__orig__'+BAK+'->GetEntries()<<\"  MC Events Reduced to \"<<Var__'+BAK+'->GetEntries()<<std::endl;\n')

	basic_w.write(2*cr + com +bar +cr+ com + wsp + "Loop over Cut vals, set Cut String, Evaluate " + cr + com + bar + 2*cr)

	basic_w.write('\nTH1D* h__Op__'+BAK+'= new TH1D(\"h__Op__'+BAK+'\",\"title\",5,0,10);\n\n')
			
	for w in range(len(CutVariables)):
		basic_w.write('\n'+'for (int_'+CutVariables[w]+'=0; int_'+CutVariables[w]+' < '+CutVariables[w]+'_points; int_'+CutVariables[w]+'++){')
			
	for x in range(len(CutVariables)):
		basic_w.write('\nstd::ostringstream strs;\n')
		basic_w.write('strs << '+CutVariables[x]+'_Cut[int_'+CutVariables[x]+'];\n')
		basic_w.write('std::string str'+`x`+' = strs.str();\n')


	basic_w.write('\nstring cut = \"weight*('+`IntLumi`+')')

	for x in range(len(CutVariables)):
		basic_w.write('*('+CutVariables[x]+'>\" + str'+`x`+' + \")')
	basic_w.write('\";')

	basic_w.write('\nTString cutstring = cut;\n') 	
	basic_w.write('\nVar__'+BAK+'->Project("h__Op__'+BAK+'","5",cutstring);\n')

	basic_w.write('B'+braces+'=h__Op__'+BAK+'->Integral();')


	basic_w.write('\n'+ (len(CutVariables))*'}')
	basic_w.write('\nstd::cout<<\"Optimization Cuts Complete\"<<std::endl;\n\n\n')

### Below the part of the script is printed which finds the optimum cut based on significance...

	for x in range(len(CutVariables)):
		basic_w.write('\n int ideal_int_'+CutVariables[x]+'=0.0;')
		
	basic_w.write('\n float Signif_max =0.0;')

	basic_w.write('\n float Signif')
	for x in range(len(CutVariables)):
		basic_w.write('['+CutVariables[x]+'_points]')
	basic_w.write(';\n\n')	
	basic_w.write('std::cout<<"\\n\\nDetermining optimal cut values for the discriminating variables ...\\n\\n"<<std::endl;\n')
		
	for y in range(len(CutVariables)):
		basic_w.write('\n'+y*''+'for (int_'+CutVariables[y]+'=0; int_'+CutVariables[y]+' < '+CutVariables[y]+'_points; int_'+CutVariables[y]+'++){\n')

	brac1 = ''		
	for x in range(len(CutVariables)):
		brac1 = brac1 + '[int_'+CutVariables[x]+']'	
	SigNow='Signif'+brac1
	BNow ='B'+brac1
	SNow ='S'+brac1
	basic_w.write('\n'+SigNow+' = '+SNow+'*pow('+SNow+'+'+BNow+',-.5);\n')
	basic_w.write('if('+SigNow+'>Signif_max) {\nSignif_max='+SigNow+';\n')
	for x in range(len(CutVariables)):
		basic_w.write('\n ideal_int_'+CutVariables[x]+'=int_'+CutVariables[x]+';')
	basic_w.write(len(CutVariables)*'}'+'}')
	
		
### Below the part of the script is printed which displays the results of signifiance optimization to screen...
	basic_w.write('\n\nstd::cout<<"Significance maximization cuts results as follows:"<<std::endl;\n')
	basic_w.write('std::cout<<"    "<<std::endl;\n')
	
	for x in range(len(CutVariables)):
		basic_w.write('std::cout<<"@@@ Best ' +CutVariables[x]+ ' Cut:  ' +CutVariables[x]+ '   > "<<'+CutVariables[x]+'_Cut[ideal_int_'+CutVariables[x]+']<<std::endl;\n')		
		basic_w.write('std::cout<<"    "<<std::endl;\n')
	basic_w.write('std::cout<<"@@@ Significance at Optimizal Cut Levels:   S = "<<Signif_max<<std::endl;\n\n')					
	basic_w.write('std::cout<<"    "<<std::endl;\n'*2)


#		for z in range(len(SignalType)):
#			if (SigOrBG[z]==1):
	basic_w.write('\nstd::cout<<"Analysis Complete for '+SignalType[z]+'\"<<std::endl;\nstd::ofstream file(\"CLAEvaluation_'+SignalType[z]+'.C\");\nstd::cout.rdbuf(file.rdbuf());\n\n');		

	basic_w.write('\nstd::cout<<\"#include \\"CLA.C\\"\"<<std::endl;')
	basic_w.write('\nstd::cout<<\"void MakeData()\"<<std::endl;')
	basic_w.write('\nstd::cout<<\"{\"<<std::endl;')
#		
	coutbrackets=''
	for x in range(len(CutVariables)):
		coutbrackets=coutbrackets+'["<<'+CutVariables[x]+'_points<<"]'
		
	coutbrackets_int=''
	for x in range(len(CutVariables)):
		coutbrackets_int=coutbrackets_int+'[int_'+CutVariables[x]+']'

	for z in range(len(CutVariables)):
		basic_w.write('\nstd::cout<<\"float '+CutVariables[z]+'_CutValue'+coutbrackets+';\"<<std::endl;')

	basic_w.write('\nstd::cout<<\"float val_sys'+coutbrackets+';\"<<std::endl;')
			
	basic_w.write('\nstd::cout<<\"int index0=0;\"<<std::endl;')
			
	for x in range(len(CutVariables)):
		basic_w.write('\n'+x*''+'for (int_'+CutVariables[x]+'=0; int_'+CutVariables[x]+' < '+CutVariables[x]+'_points; int_'+CutVariables[x]+'++){\n')
#			

	basic_w.write('\nstd::cout<<\"index0=index0+1;\"<<std::endl;')
		
	for x in range(len(CutVariables)):
		basic_w.write('\nstd::cout<<\"' +CutVariables[x]+'_CutValue"<<')
		for t in range(len(CutVariables)):
			basic_w.write('\"[\"<<int_'+CutVariables[t]+'<<\"]\"<<')
		basic_w.write('\"=\"<<'+CutVariables[x]+'_Cut[int_'+CutVariables[x]+']<<\";\"<<std::endl;\n')
#		
#		
	basic_w.write('\nstd::cout<<\"val_sys\"<<')
	for t in range(len(CutVariables)):
		basic_w.write('\"[\"<<int_'+CutVariables[t]+'<<\"]\"<<')
	basic_w.write('\" = CLA('+`IntLumi`+','+`IntLumi*IntLumiFracError`+', \"<<(1.0*S'+coutbrackets_int+')/(1.0*S_orig)<<\",\"<< ('+`ErrorInSigEff`+'*S'+coutbrackets_int+')/(1.0*S_orig)<<\",\"<<B'+coutbrackets_int+'<<\",\"<<B'+coutbrackets_int+'*'+`ErrInNBKG`+'<<");"<<std::endl;')
		
	basic_w.write('\nstd::cout<<\"std::cout<<\\" ****************************************************************** \\"<<std::endl;\"<<std::endl;')
	basic_w.write('\nstd::cout<<\"std::cout<<\\"CLA Calculation    \\"<<index0<<\\"   of   \\"<<"<<')
	for x in range(len(CutVariables)):
		basic_w.write(CutVariables[x]+'_points*')
	basic_w.write('1.0<<"<<\\"   Completed\\"<<std::endl;\"<<std::endl;')
	basic_w.write('\nstd::cout<<\"std::cout<<\\" ****************************************************************** \\"<<std::endl;\"<<std::endl;')
	for x in range(len(CutVariables)):
		basic_w.write('\n'+ (len(CutVariables)-x)*''+'}')
	basic_w.write('\n')			

	basic_w.write('\nstd::cout<<\"float xsys =99999999;\"<<std::endl;')
#		
	for x in range(len(CutVariables)):
		basic_w.write('\nstd::cout<<\"float '+CutVariables[x]+'_syscut = 0.0;\"<<std::endl;')
		basic_w.write('\nstd::cout<<\"int jj_'+CutVariables[x]+'=0;\"<<std::endl;')

	for x in range(len(CutVariables)):
		basic_w.write('\nstd::cout<<\" for (jj_'+CutVariables[x]+'=0; jj_'+CutVariables[x]+'<"<<'+CutVariables[x]+'_points<<"; jj_'+CutVariables[x]+'++){\"<<std::endl;')
	basic_w.write('\nstd::cout<<\" if (val_sys')
	for x in range(len(CutVariables)):
		basic_w.write('[jj_'+CutVariables[x]+']')
	basic_w.write('<xsys){\"<<std::endl;')
#		
	basic_w.write('\nstd::cout<<\" xsys=val_sys')
	for x in range(len(CutVariables)):
		basic_w.write('[jj_'+CutVariables[x]+']')
	basic_w.write(';\"<<std::endl;')
	
	for z in range(len(CutVariables)):
		basic_w.write('\nstd::cout<<\" '+CutVariables[z]+'_syscut= '+CutVariables[z]+'_CutValue')
		for x in range(len(CutVariables)):
			basic_w.write('[jj_'+CutVariables[x]+']')
		basic_w.write(';\"<<std::endl;')
	

	basic_w.write('\nstd::cout<<\"}'+len(CutVariables)*'}'+'\"<<std::endl;')
	basic_w.write('\n')
	
	for z in range(len(CutVariables)):
			basic_w.write('\nstd::cout<<\"std::cout<<\\"'+CutVariables[z]+' @@@cut for cross section upper limit minimization (No Systematics) is determined to be:   \\"<<'+CutVariables[z]+'_syscut<<std::endl;\"<<std::endl;')
	basic_w.write('\nstd::cout<<\"}\"<<std::endl;')

	basic_w.write('}')
	basic_w.close()
	os.system("mv "+AnalysisDirectory+"Stage2_Optimization/MuNu/BasicAnalysis_"+SIG+".C "+AnalysisDirectory+"Stage2_Optimization/MuNu/temptest.C")
	os.system("bcpp "+AnalysisDirectory+"Stage2_Optimization/MuNu/temptest.C "+AnalysisDirectory+"Stage2_Optimization/MuNu/BasicAnalysis_"+SIG+".C")
	os.system("rm "+AnalysisDirectory+"Stage2_Optimization/MuNu/temptest.C ")


RunCommands_w = open(AnalysisDirectory+"Stage2_Optimization/MuNu/RunCommands.sh","w")
RunCommands_w.write('#!/bin/sh\n\n') 

for z in range(len(SignalType)):

	if (SigOrBG[z]==1):
		RootCommands_w = open(AnalysisDirectory+"Stage2_Optimization/MuNu/RootCommandsBasic"+SignalType[z],"w")
		RootCommands_w2 = open(AnalysisDirectory+"Stage2_Optimization/MuNu//RootCommandsCLA"+SignalType[z],"w")
		RootCommands_w.write('{\n\n') 
		RootCommands_w2.write('{\n\n') 
		RootLinesToAdd = '\ngROOT->ProcessLine(\".x ' +SignalType[z]+'_BasicAnalysis.C\");\ngROOT->ProcessLine(\"gROOT->Reset()\");\ngROOT->ProcessLine(\"gROOT->Clear()\");\ngROOT->ProcessLine(\".q");\n'
		RootCommands_w.write(RootLinesToAdd)

		RootLinesToAdd = '\ngROOT->ProcessLine(\".L CLAEvaluation_'+SignalType[z]+'.C++\");\ngROOT->ProcessLine(\"MakeData()");\ngROOT->ProcessLine(\"gROOT->Reset()\");\ngROOT->ProcessLine(\"gROOT->Clear()\");\ngROOT->ProcessLine(\".q");\n\n'
		RootCommands_w2.write(RootLinesToAdd)

		RunCommands_w.write('root -l RootCommandsBasic'+SignalType[z]+'\n')
		RunCommands_w.write('root -l RootCommandsCLA'+SignalType[z]+'\n\n')

		RootCommands_w.write('\n\n}')
		RootCommands_w2.write('\n\n}')


		RootCommands_w2.close()
RootCommands_w.close()

