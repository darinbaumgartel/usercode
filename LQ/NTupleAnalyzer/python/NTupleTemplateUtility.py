#################################################################################################
##########                    N Tuple Analyzer Script Producer                        ###########
##########      Store NTuple Info In NTupleInfo.csv File in current Directory         ###########
##########      Darin Baumgartel - July 26, 2010 - darin.carl.baumgartel@cern.ch      ###########
#################################################################################################

import os # For direcory scanning abilities, etc
from time import strftime
from GetDirInfo import *
from CSVInterpreter import *
IntLumi = 1.0


now=str(strftime("%Y-%m-%d %H:%M:%S"))
now = now.replace(" ","")
now = now.replace("\t","")
os.system("mkdir ../Stage1_NTupleAnalysis/ROOTBAK_"+now)
os.system("mv ../Stage1_NTupleAnalysis/CurrentRootFiles/*.root ../Stage1_NTupleAnalysis/ROOTBAK_"+now)
os.system("rm ../Stage1_NTupleAnalysis/*_*.* ../Stage1_NTupleAnalysis/RootProcesses")
# Analysis Details Below
WhatType=['Background','Signal','CollisionData'] # So that WhatType[SigOrBG[x]] returns string "Signal" or "Background"

# initialize file that stores root processes to be run
f_root = open(AnalysisDirectory+"Stage1_NTupleAnalysis/RootProcesses", 'w')
f_root.write('{\n')



for x in range(len(SignalType)):
	if SigOrBG[x]==0:
		path=BGDirectory + SignalType[x]
	if SigOrBG[x]==1: 
		path=SigDirectory + SignalType[x]	
	if SigOrBG[x]==2:
		path = DataDirectory + SignalType[x]	

	dirList=os.listdir(path) # list of files in directory

	s1 = open(AnalysisDirectory+"Stage1_NTupleAnalysis/NTupleAnalyzer.C").read() # Open the NTupleAnalyzer.C template and replace with array values
	s1 = s1.replace('Numberofevents',`N_orig[x]`)
	s1 = s1.replace('placeholder', SignalType[x])
	s1 = s1.replace('crosssection', `Xsections[x]`)
	s1 = s1.replace('desired_luminosity', `IntLumi`)
	s1 = s1.replace('efficiency', `FilterEffs[x]`)
#	s1 = s1.replace('HLTmarker',`HLTBit[x]`)
	s1 = s1.replace('FILEINPUT', path + '/' + dirList[0] )
	s1 = s1.replace('MassOfLQ', `MassOfLQ[x]`)

	if SignalType[x][0] == 'W':
		s1 = s1.replace('IsItWMC', 'true')
	if SignalType[x][0] != 'W':
		s1 = s1.replace('IsItWMC', 'false')

	f1 = open(AnalysisDirectory+"Stage1_NTupleAnalysis/NTupleAnalyzer_"+SignalType[x]+".C", 'w') # write a new file based on the template
	f1.write(s1)
	f1.close()
	

	s2 = open(AnalysisDirectory+"Stage1_NTupleAnalysis/NTupleAnalyzer.h") # Same deal for the .h file now...
	f2 = open(AnalysisDirectory+"Stage1_NTupleAnalysis/NTupleAnalyzer_"+SignalType[x]+".h", 'a')
	for line in s2.readlines():
		line = line.replace('placeholder', SignalType[x])
		f2.write(line)
		if 'filetracermark000' in line:	
			f2.write('\nTChain * chain = new TChain(\"rootTupleTree/tree\",\"\");\n')
			for y in range(len(dirList)):
				f2.write('\nchain->Add(\"' + path + '/' + dirList[y] + '");\n')
	s2.close()
	f2.close()
	
	# Now the .h and .C files to run have been written
	
	# The next task is to write the root commands to a file for running using the gROOT->ProcessLine commands
	# Note here that "gErrorIgnoreLevel = 3001" stops the issuance of warnings and errors, as a number of known-irrelevant  errors can appear. Use only if you are sure of your code :)
	RootLinesToAdd = 'gROOT->ProcessLine(\"gErrorIgnoreLevel = 3001;\");\ngROOT->ProcessLine(\".L NTupleAnalyzer_'+ SignalType[x] + '.C++\");\ngROOT->ProcessLine(\"NTupleAnalyzer_'+ SignalType[x] + ' t\");\ngROOT->ProcessLine(\"t.Loop()\");\ngROOT->ProcessLine(\"gROOT->Reset()\");\n\n'
	
	# Below I give an alternate version with errors not supressed (no GErrorIgnoreLevel). Choose wisely.
	# # # RootLinesToAdd = 'gROOT->ProcessLine(\".L NTupleAnalyzer_'+ SignalType[x] + '.C++\");\ngROOT->ProcessLine(\"NTupleAnalyzer_'+ SignalType[x] + ' t\");\ngROOT->ProcessLine(\"t.Loop()\");\ngROOT->ProcessLine(\"gROOT->Reset()\");\n\n'
	
	f_root.write(RootLinesToAdd)
f_root.write('\ngROOT->ProcessLine(\".q\");\n}')
f_root.close()
# The Root commands file "RootProcesses" has now been written and saved 

# The structure of these root files is also compatible with TMVA. Here we will write over a TMVA Analysis Template to produce a file you can run in TMVA. 
# If this does not interest you, just ignore it. Writing it takes no time and there is no need to run the TMVA file
tmva_r = open(AnalysisDirectory+"/TMVA/TMVAnalysis_template.C")
tmva_w = open(AnalysisDirectory+"/TMVA/TMVAnalysis.C", 'w')
tmva_w.write('\n')
tmva_w.close()
tmva_w2 = open(AnalysisDirectory+"/TMVA/TMVAnalysis.C", 'a')
for line in tmva_r.readlines():
	tmva_w2.write(line)
	if 'list_tracer_000' in line:
		for z in range(len(SignalType)):
			tmva_w2.write('\nint use_'+SignalType[z]+' =1;')
	if 'list_tracer_001' in line:
		for z in range(len(SignalType)):
			tmva_w2.write('\nTChain '+SignalType[z]+'tree(\"'+SignalType[z]+'\");')
			tmva_w2.write('\n'+SignalType[z]+'tree->Add(\"'+AnalysisDirectory+'NTupleAnalyzerLQ_Inputs.root\");')
			tmva_w2.write('\nTTree *'+SignalType[z]+'Signal = (TTree*)'+SignalType[z]+'tree;')
			tmva_w2.write('\nfloat '+SignalType[z]+'_weight;')
			tmva_w2.write('\n'+SignalType[z]+'Signal->SetBranchAddress(\"tmva_weight\",&'+SignalType[z]+'_weight);')
			tmva_w2.write('\n'+SignalType[z]+'Signal->GetEntry(1);')
	if 'list_tracer_002' in line:
		for z in range(len(SignalType)):
				tmva_w2.write('\nif (use_'+SignalType[z]+' ==1){')
				tmva_w2.write('\n\tfactory->Add'+WhatType[SigOrBG[z]]+'Tree ( ' +SignalType[z]+'Signal,'+ SignalType[z]+'_weight );\n\t}\n')


tmva_r.close()
tmva_w2.close()

