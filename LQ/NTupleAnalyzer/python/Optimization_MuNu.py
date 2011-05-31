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

#=======================================================================================================
#   Here we will build a full optimization file from a fragment file
#=======================================================================================================

basic_r = open(AnalysisDirectory+"fragments/BasicAnalysis_Template.C")
basic_w = open(AnalysisDirectory+"Stage2_Optimization/MuNu/BasicAnalysis"".C", 'w')
basic_w.write('{\n\n')

# Store some shorthand
com = "//"   # C++ comment
bar = "-"*125 # horizontal bar
wsp = " "*20 # 20 spaces whitespace
cr = "\n" # new line /return

basic_w.write(com + bar + cr +com +wsp+"Optimization from Tree Formated Files"+cr+com+wsp+"DBaumgartel - June 14, 2010 - Summer 2010 LQ Analysis"+cr+com+wsp+"To run, simply:   root -l {name of file}.C --- and wait"+cr+com+bar+cr*2)
for z in range(len(SignalType)):
	basic_w.write('\n TFile f__'+SignalType[z]+'(\"'+FileLocation+'/'+SignalType[z]+'.root\");\n')

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
	basic_w.write('\n '+z*'\t'+'for (int_'+CutVariables[z]+'=0; int_'+CutVariables[z]+' < '+CutVariables[z]+'_points; int_'+CutVariables[z]+'++){')
for x in range(len(dummy2)):
	basic_w.write('\n ' + len(CutVariables)*'\t' +dummy2[x])
	for z in range(len(CutVariables)):
		basic_w.write('[int_'+CutVariables[z]+']')
	basic_w.write('=0;')
for z in range(len(CutVariables)):
	basic_w.write('\n '+(len(CutVariables)-z)*'\t'+'}')

for z in range(len(CutVariables)):
	basic_w.write('\n'+'for (int_'+CutVariables[z]+'=0; int_'+CutVariables[z]+' < '+CutVariables[z]+'_points; int_'+CutVariables[z]+'++){')
	basic_w.write('\n \t'+CutVariables[z]+'_Cut[int_'+CutVariables[z]+'] = '+CutVariables[z]+'_startingpoint + '+CutVariables[z]+'_interval*int_'+CutVariables[z]+';') 
	basic_w.write('\n \t}\n')

braces = ''
for z in range(len(CutVariables)):
	braces = braces+'[int_' + CutVariables[z] +']'   

	#!!!------------------------------
## Below the part of the script is printed which determines evaluates the cut values...
basic_w.close()
basic_w2 = open("BasicAnalysis.C", 'a')
for line in basic_r.readlines():
	basic_w2.write(line)
	if 'list_tracer_000' in line:

		for z in range(len(SignalType)):
			basic_w2.write('\nint use_'+SignalType[z]+' ='+`int(1-SigOrBG[z])`+';\n')

	if 'list_tracer_001' in line:
		for z in range(len(SignalType)):
			basic_w2.write('\n\n\t\t\t\t//#######################################################################################\n\t\t\t\t//                         '+SignalType[z]+'                         \n\t\t\t\t//#######################################################################################\n')
			basic_w2.write('\nif (use_'+SignalType[z]+' ==1){')
			basic_w2.write('\n SigOrBG = '+`SigOrBG[z]`+';')
			basic_w2.write('\n\n\t\t//---------------------------------------------------------------------------------------//\n\t\t//----------------   Declare background trees/Temp Histograms   -------------------------//\n\t\t//---------------------------------------------------------------------------------------//\n')

			basic_w2.write('\n\t\tTTree* Var__orig__'+SignalType[z]+' = (TTree*)f__'+SignalType[z]+'->Get(\"PhysicalVariables\");')
			basic_w2.write('\n\t\tTH1D* h__'+SignalType[z]+'= new TH1D(\"h__'+SignalType[z]+'\",\"title\",100,0.0,10000.0);\n\n')

			basic_w2.write('\n\t\tVar__orig__'+SignalType[z]+'->Project("h__'+SignalType[z]+'\",\"weight*('+`IntLumi`+')\",\"weight*('+`IntLumi`+')*Events_Orig/Events_AfterLJ");')

			basic_w2.write('\n\t\tif (SigOrBG==1) const Double_t S_orig =h__'+SignalType[z]+'->Integral();')
			basic_w2.write('\n\t\tif (SigOrBG==0) const Double_t B_orig =h__'+SignalType[z]+'->Integral();')

			basic_w2.write('\n\t\tstd::cout<<\"@@@ Evaluating For '+WhatType[SigOrBG[z]]+' Type '+SignalType[z] +'\"<<std::endl;\n')

			basic_w2.write('\n\t\tstring precut = \"1.0')

			for x in range(len(PrecutVariables)):
				basic_w2.write('*('+PrecutVariables[x]+'>'+`PrecutMinValues[x]`+')')

			for x in range(len(CutVariables)):
				basic_w2.write('*('+CutVariables[x]+'>'+`VariableStartingPoint[x]`+')')
			basic_w2.write('\";')

			basic_w2.write('\n\t\tTString precutstring = precut;\n') 
			
			basic_w2.write('\n\t\tTFile f__temp__'+SignalType[z]+'("temp__'+SignalType[z]+'.root","recreate");')

			basic_w2.write('\n\t\tTTree* Var__'+SignalType[z]+' = Var__orig__'+SignalType[z]+' ->CopyTree(precutstring);\n')
			basic_w2.write('\n\t\tstd::cout<<\"Precuts Complete. \"<<Var__orig__'+SignalType[z]+'->GetEntries()<<\"  MC Events Reduced to \"<<Var__'+SignalType[z]+'->GetEntries()<<std::endl;\n')

			basic_w2.write('\n\n\t\t//---------------------------------------------------------------------------------------//\n\t\t//-----------------   Loop over Cut vals, set Cut String, Evaluate   --------------------//\n\t\t//---------------------------------------------------------------------------------------//\n\n')

			basic_w2.write('\n\t\tTH1D* h__Op__'+SignalType[z]+'= new TH1D(\"h__Op__'+SignalType[z]+'\",\"title\",100,0.0,10000.0);\n\n')
			
			goodtab='\t'*len(CutVariables)
			for y in range(len(CutVariables)):
				basic_w2.write('\n\t'+y*'\t'+'for (int_'+CutVariables[y]+'=0; int_'+CutVariables[y]+' < '+CutVariables[y]+'_points; int_'+CutVariables[y]+'++){')
				
			for x in range(len(CutVariables)):

				basic_w2.write('\n\n'+goodtab+'std::ostringstream strs;\n')
				basic_w2.write(goodtab+'strs << '+CutVariables[x]+'_Cut[int_'+CutVariables[x]+'];\n')
				basic_w2.write(goodtab+'std::string str'+`x`+' = strs.str();\n')


			basic_w2.write('\n\n'+goodtab+'string cut = \"weight*('+`IntLumi`+')')

			for x in range(len(CutVariables)):
				basic_w2.write('*('+CutVariables[x]+'>\" + str'+`x`+' + \")')
			basic_w2.write('\";')

			basic_w2.write('\n\n'+goodtab+'TString cutstring = cut;\n') 
			
			basic_w2.write('\n'+goodtab+'Var__'+SignalType[z]+'->Project("h__Op__'+SignalType[z]+'","ST_calo",cutstring);\n')

			basic_w2.write('\n'+goodtab+'if (SigOrBG==1) S'+braces+'=h__Op__'+SignalType[z]+'->Integral();')
			basic_w2.write('\n'+goodtab+'if (SigOrBG==0) B'+braces+'=h__Op__'+SignalType[z]+'->Integral();')

			for x in range(len(CutVariables)):
				basic_w2.write('\n'+ (len(CutVariables)-x)*'\t'+'}')
			basic_w2.write('}')
			basic_w2.write('\n\t\tstd::cout<<\"Optimization Cuts Complete\"<<std::endl;\n')

## Below the part of the script is printed which finds the optimum cut based on significance...
	if 'list_tracer_002' in line:
		for x in range(len(CutVariables)):
			basic_w2.write('\n int ideal_int_'+CutVariables[x]+'=0.0;')
		
		basic_w2.write('\n float Signif_max =0.0;')

		basic_w2.write('\n float Signif')
		for x in range(len(CutVariables)):
			basic_w2.write('['+CutVariables[x]+'_points]')
		basic_w2.write(';\n\n')	


		basic_w2.write('std::cout<<"\\n\\nDetermining optimal cut values for the discriminating variables ...\\n\\n"<<std::endl;\n')
		
		for y in range(len(CutVariables)):
			basic_w2.write('\n\t'+y*'\t'+'for (int_'+CutVariables[y]+'=0; int_'+CutVariables[y]+' < '+CutVariables[y]+'_points; int_'+CutVariables[y]+'++){\n')
			
		basic_w2.write('\n\t\tSignif')
		for x in range(len(CutVariables)):
			basic_w2.write('[int_'+CutVariables[x]+']')
		basic_w2.write('=1.0*S')
		for x in range(len(CutVariables)):
			basic_w2.write('[int_'+CutVariables[x]+']')
		basic_w2.write('*pow(1.0*(S')
		for x in range(len(CutVariables)):
			basic_w2.write('[int_'+CutVariables[x]+']')
		basic_w2.write('+B')
		for x in range(len(CutVariables)):
			basic_w2.write('[int_'+CutVariables[x]+']')
		basic_w2.write('),-.5);\n')	


		basic_w2.write('\n\t\t\tif (Signif')
		for x in range(len(CutVariables)):
			basic_w2.write('[int_'+CutVariables[x]+']')
		basic_w2.write('>Signif_max) {\n\t\t\t\tSignif_max=Signif')
		for x in range(len(CutVariables)):
			basic_w2.write('[int_'+CutVariables[x]+']')
		basic_w2.write(';\n')
			
		for x in range(len(CutVariables)):
			basic_w2.write('\n\t\t\t\t ideal_int_'+CutVariables[x]+'=int_'+CutVariables[x]+';')

		for x in range(len(CutVariables)):
			basic_w2.write('\n\t\t\t'+ (len(CutVariables)-x)*'\t'+'}')
		basic_w2.write('\n\t}\n\n\n\n')		
		
## Below the part of the script is printed which displays the results of signifiance optimization to screen...
		basic_w2.write('std::cout<<"Significance maximization cuts results as follows:"<<std::endl;\n')
		basic_w2.write('std::cout<<"    "<<std::endl;\n')
		
		for x in range(len(CutVariables)):
			basic_w2.write('std::cout<<"@@@ Best ' +CutVariables[x]+ ' Cut:  ' +CutVariables[x]+ '   > "<<'+CutVariables[x]+'_Cut[ideal_int_'+CutVariables[x]+']<<std::endl;\n')		
			basic_w2.write('std::cout<<"    "<<std::endl;\n')

		basic_w2.write('std::cout<<"@@@ Significance at Optimizal Cut Levels:   S = "<<Signif_max<<std::endl;\n\n')			
		
		basic_w2.write('std::cout<<"    "<<std::endl;\n')
		basic_w2.write('std::cout<<"    "<<std::endl;\n')

		for z in range(len(SignalType)):
			if (SigOrBG[z]==1):
				basic_w2.write('if (use_'+SignalType[z]+'==1){\n\tstd::cout<<"Analysis Complete for '+SignalType[z]+'\"<<std::endl;\n\tstd::ofstream file(\"CLAEvaluation_'+SignalType[z]+'.C\");\n\tstd::cout.rdbuf(file.rdbuf());\n\t}\n\n');		

		basic_w2.write('\nstd::cout<<\"#include \\"CLA.C\\"\"<<std::endl;')
		basic_w2.write('\nstd::cout<<\"void MakeData()\"<<std::endl;')
		basic_w2.write('\nstd::cout<<\"{\"<<std::endl;')
		
		coutbrackets=''
		for x in range(len(CutVariables)):
			coutbrackets=coutbrackets+'["<<'+CutVariables[x]+'_points<<"]'
		
		coutbrackets_int=''
		for x in range(len(CutVariables)):
			coutbrackets_int=coutbrackets_int+'[int_'+CutVariables[x]+']'

		for z in range(len(CutVariables)):
			basic_w2.write('\nstd::cout<<\"float '+CutVariables[z]+'_CutValue'+coutbrackets+';\"<<std::endl;')

		basic_w2.write('\nstd::cout<<\"float val_sys'+coutbrackets+';\"<<std::endl;')

			
		basic_w2.write('\nstd::cout<<\"int index0=0;\"<<std::endl;')
		
		for y in range(len(CutVariables)):
			basic_w2.write('\n\t'+y*'\t'+'for (int_'+CutVariables[y]+'=0; int_'+CutVariables[y]+' < '+CutVariables[y]+'_points; int_'+CutVariables[y]+'++){\n')
			

		basic_w2.write('\n\t\t\tstd::cout<<\"index0=index0+1;\"<<std::endl;')
		
		for y in range(len(CutVariables)):
			basic_w2.write('\n\t\t\tstd::cout<<\"' +CutVariables[y]+'_CutValue"<<')
			for t in range(len(CutVariables)):
				basic_w2.write('\"[\"<<int_'+CutVariables[t]+'<<\"]\"<<')
			basic_w2.write('\"=\"<<'+CutVariables[y]+'_Cut[int_'+CutVariables[y]+']<<\";\"<<std::endl;')
		
		
		basic_w2.write('\n\t\t\tstd::cout<<\"val_sys\"<<')
		for t in range(len(CutVariables)):
			basic_w2.write('\"[\"<<int_'+CutVariables[t]+'<<\"]\"<<')
		basic_w2.write('\" = CLA('+`IntLumi`+','+`IntLumi*IntLumiFracError`+', \"<<(1.0*S'+coutbrackets_int+')/(1.0*S_orig)<<\",\"<< ('+`ErrorInSigEff`+'*S'+coutbrackets_int+')/(1.0*S_orig)<<\",\"<<B'+coutbrackets_int+'<<\",\"<<B'+coutbrackets_int+'*'+`ErrInNBKG`+'<<");"<<std::endl;')
		
		basic_w2.write('\n\t\t\tstd::cout<<\"std::cout<<\\" ****************************************************************** \\"<<std::endl;\"<<std::endl;')
		basic_w2.write('\n\t\t\tstd::cout<<\"std::cout<<\\"CLA Calculation    \\"<<index0<<\\"   of   \\"<<"<<')
		for x in range(len(CutVariables)):
			basic_w2.write(CutVariables[x]+'_points*')
		basic_w2.write('1.0<<"<<\\"   Completed\\"<<std::endl;\"<<std::endl;')
		basic_w2.write('\n\t\t\tstd::cout<<\"std::cout<<\\" ****************************************************************** \\"<<std::endl;\"<<std::endl;')
		for x in range(len(CutVariables)):
			basic_w2.write('\n\t\t\t'+ (len(CutVariables)-x)*'\t'+'}')
		basic_w2.write('\n')			

		basic_w2.write('\nstd::cout<<\"float xsys =99999999;\"<<std::endl;')
		
		for x in range(len(CutVariables)):
			basic_w2.write('\nstd::cout<<\"float '+CutVariables[x]+'_syscut = 0.0;\"<<std::endl;')
			basic_w2.write('\nstd::cout<<\"int jj_'+CutVariables[x]+'=0;\"<<std::endl;')

		for x in range(len(CutVariables)):
			basic_w2.write('\nstd::cout<<\"\t for (jj_'+CutVariables[x]+'=0; jj_'+CutVariables[x]+'<"<<'+CutVariables[x]+'_points<<"; jj_'+CutVariables[x]+'++){\"<<std::endl;')
		basic_w2.write('\nstd::cout<<\"\t\t\t if (val_sys')
		for x in range(len(CutVariables)):
			basic_w2.write('[jj_'+CutVariables[x]+']')
		basic_w2.write('<xsys){\"<<std::endl;')
		
		basic_w2.write('\nstd::cout<<\"\t\t\t\t xsys=val_sys')
		for x in range(len(CutVariables)):
			basic_w2.write('[jj_'+CutVariables[x]+']')
		basic_w2.write(';\"<<std::endl;')
		
		for z in range(len(CutVariables)):
			basic_w2.write('\nstd::cout<<\"\t\t\t\t '+CutVariables[z]+'_syscut= '+CutVariables[z]+'_CutValue')
			for x in range(len(CutVariables)):
				basic_w2.write('[jj_'+CutVariables[x]+']')
			basic_w2.write(';\"<<std::endl;')
		

		basic_w2.write('\nstd::cout<<\"}'+len(CutVariables)*'}'+'\"<<std::endl;')
		basic_w2.write('\n')
		
		for z in range(len(CutVariables)):
			basic_w2.write('\nstd::cout<<\"std::cout<<\\"'+CutVariables[z]+' @@@cut for cross section upper limit minimization (No Systematics) is determined to be:   \\"<<'+CutVariables[z]+'_syscut<<std::endl;\"<<std::endl;')
	
		basic_w2.write('\n')
		basic_w2.write('\nstd::cout<<\"}\"<<std::endl;')
		
		
basic_r.close()
basic_w2.write('\n}')
basic_w2.close()

RunCommands_w = open("RunCommands.sh","w")
RunCommands_w.write('#!/bin/sh\n\n') 

for z in range(len(SignalType)):

	if (SigOrBG[z]==1):
		BasicEdit_r = open("BasicAnalysis.C") 
		BasicEdit_w = open(SignalType[z]+'_BasicAnalysis.C',"w") 
		RootCommands_w = open('RootCommandsBasic'+SignalType[z],"w")
		RootCommands_w2 = open('RootCommandsCLA'+SignalType[z],"w")
		RootCommands_w.write('{\n\n') 
		RootCommands_w2.write('{\n\n') 
		for line in BasicEdit_r.readlines():
			line = line.replace('int use_'+SignalType[z]+' ='+`int(1-SigOrBG[z])`,'int use_'+SignalType[z]+' =1')
			BasicEdit_w.write(line) 

		RootLinesToAdd = '\ngROOT->ProcessLine(\".x ' +SignalType[z]+'_BasicAnalysis.C\");\ngROOT->ProcessLine(\"gROOT->Reset()\");\ngROOT->ProcessLine(\"gROOT->Clear()\");\ngROOT->ProcessLine(\".q");\n'
		RootCommands_w.write(RootLinesToAdd)

		RootLinesToAdd = '\ngROOT->ProcessLine(\".L CLAEvaluation_'+SignalType[z]+'.C++\");\ngROOT->ProcessLine(\"MakeData()");\ngROOT->ProcessLine(\"gROOT->Reset()\");\ngROOT->ProcessLine(\"gROOT->Clear()\");\ngROOT->ProcessLine(\".q");\n\n'
		RootCommands_w2.write(RootLinesToAdd)

		RunCommands_w.write('root -l RootCommandsBasic'+SignalType[z]+'\n')
		RunCommands_w.write('root -l RootCommandsCLA'+SignalType[z]+'\n\n')

		RootCommands_w.write('\n\n}')
		RootCommands_w2.write('\n\n}')
	BasicEdit_r.close()
	BasicEdit_w.close()


	RootCommands_w.close()
	RootCommands_w2.close()


