#################################################################################################
##########                    N Tuple Analyzer Script Producer                        ###########
##########      Store NTuple Info In NTupleInfo.csv File in current Directory         ###########
##########      Darin Baumgartel - May 31, 2011 - darin.carl.baumgartel@cern.ch      ###########
#################################################################################################

import os # For direcory scanning abilities, etc
from time import strftime


### This portion reads the NTupleInfo.csv file and gets the information ###
import csv
csvfile = open('NTupleInfo.csv','r')
table=[]

for row in csv.reader(csvfile):
	if row[0][0]=='#':
		continue
	table.append(row)
for r in range(1,len(table)):
	for c in range(1,len(table[0])):
		table[r][c]=(table[r][c])
table2= map(list,zip(*table[1:]))
for x in range(0,len(table2)):
	exec (table[0][x]+'='+`table2[x]`)	
for x in range(0,len(HLTBit)):
	HLTBit[x]=int(HLTBit[x])
	SigOrBG[x]=int(SigOrBG[x])
###----------------------------------------------------------------------###

### This portion creates the branch status commands to speed up the code ###
f1 = open('NTupleAnalyzer.h','r')
statuscommands = ''

variables = []
for line in f1:
	if 'SetBranchAddress' in line:
		var = (line.split('\"')[1])
		variables.append( ((var.replace('\n','')).replace('\r','')).replace(' ','')  )
for x in variables:
	use =0
	f2 = open('NTupleAnalyzer.C','r')
	for line in f2:
		if x in line:	
			use = 1
	if use ==1:
		statuscommands += '   fChain->SetBranchStatus("'+x+'",1);\n'
	else:
		statuscommands += '   fChain->SetBranchStatus("'+x+'",0);\n'
	f2.close()
f1.close()
###----------------------------------------------------------------------###

now=str(strftime("%Y-%m-%d-%H:%M:%S"))
now = now.replace(" ","")
now = now.replace("\t","")
now = now.replace("-","_")
now = now.replace(":","_")
#os.system("mkdir ../Stage1_NTupleAnalysis/ROOTBAK_"+now)
#os.system("mv ../Stage1_NTupleAnalysis/CurrentRootFiles/*.root ../Stage1_NTupleAnalysis/ROOTBAK_"+now)
#os.system("rm ../Stage1_NTupleAnalysis/*_*.* ../Stage1_NTupleAnalysis/RootProcesses")
# Analysis Details Below
WhatType=['Background','Signal','CollisionData'] # So that WhatType[SigOrBG[x]] returns string "Signal" or "Background"

# initialize file that stores root processes to be run
f_root = open("RootProcesses", 'w')
f_root.write('{\n')

f_sub = open("sub_AllAnalyzer.csh", 'w')
f_sub.write('#!/bin/csh')


thisdir = os.popen('pwd').readlines()[0].replace('\n','')
person = os.popen('whoami').readlines()[0].replace('\n','')
thiscastor = '/castor/cern.ch/user/'+person[0]+'/'+person+'/LQAnalyzerOutput/NTupleAnalyzer_'+now
os.system('rfmkdir '+ thiscastor.replace('NTupleAnalyzer_'+now,''))
os.system('rfmkdir '+ thiscastor)

for x in range(len(SignalType)):
	sub_thisroot = open("sub_"+SignalType[x]+".csh",'w')
	sub_thisroot.write('#!/bin/csh\ncd '+thisdir+'\neval `scramv1 runtime -csh`\ncd -\ncp '+thisdir+'/NTupleAnalyzer_'+SignalType[x].replace('-','_')+'.* .\ncp '+thisdir+'/RootProcesses_'+SignalType[x]+' .\nroot -b RootProcesses_'+SignalType[x]+'\nrfcp '+SignalType[x].replace('-','_')+'.root '+thiscastor+'\n')
	sub_thisroot.close()

	f_sub.write('\nbsub -R "pool>50000" -q 1nd -J job'+SignalType[x]+' < sub_'+SignalType[x]+'.csh\n')

	f_thisroot =  open("RootProcesses_"+SignalType[x],'w')


	f_thisroot.write('{\n')
	RootLinesToAdd = 'gROOT->ProcessLine(\"gErrorIgnoreLevel = 3001;\");\ngROOT->ProcessLine(\".L NTupleAnalyzer_'+ SignalType[x].replace('-','_') + '.C++\");\ngROOT->ProcessLine(\"NTupleAnalyzer_'+ SignalType[x].replace('-','_') + ' t\");\ngROOT->ProcessLine(\"t.Loop()\");\ngROOT->ProcessLine(\"gROOT->Reset()\");\ngROOT->ProcessLine(".q");\n}\n'
	f_thisroot.write(RootLinesToAdd)
	f_thisroot.close()

	
	print 'Preparing '+ SignalType[x]
	path = CastorDirectory[x]	
	FullList = os.popen('nsls '+path).readlines()

	dirList = []
	for y in FullList:
		thistype = y[0:len(SignalType[x])]
		if SignalType[x] ==thistype:
			dirList.append(y)

	s1 = open("NTupleAnalyzer.C").read() # Open the NTupleAnalyzer.C template and replace with array values
	s1 = s1.replace('Numberofevents',str(float(N_orig[x])))
	s1 = s1.replace('placeholder', SignalType[x].replace('-','_'))
	s1 = s1.replace('crosssection', str(float(Xsections[x])))
	s1 = s1.replace('efficiency', str(float(FilterEffs[x])))
	s1 = s1.replace('desired_luminosity', str(float(1.0)))
	s1 = s1.replace('FILEINPUT', path + '/' + dirList[0] )
	s1 = s1.replace('MassOfLQ', str(float(MassOfLQ[x])))

	if SignalType[x][0] == 'W':
		s1 = s1.replace('IsItWMC', 'true')
	if SignalType[x][0] != 'W':
		s1 = s1.replace('IsItWMC', 'false')

#	os.system('rm NTupleAnalyzer_'+SignalType[x]+'.*')
	f1 = open("NTupleAnalyzer_"+SignalType[x].replace('-','_')+".C", 'w') # write a new file based on the template
	f1.write(s1)
	f1.close()
	

	s2 = open("NTupleAnalyzer.h") # Same deal for the .h file now...
	f2 = open("NTupleAnalyzer_"+SignalType[x].replace('-','_')+".h", 'w')
	for line in s2.readlines():
		line = line.replace('placeholder', SignalType[x].replace('-','_'))
		f2.write(line)
		if 'filetracermark000' in line:	
			f2.write('\nTChain * chain = new TChain(\"rootTupleTree/tree\",\"\");\n')
			for y in range(len(dirList)):
				thisline = '\nchain->Add(\"rfio://' + path + '/' + dirList[y] + '");\n'
				thisline = thisline.replace('\n','') + '\n'
#				print thisline
				f2.write(thisline)
		if 'filetracermarkstatus' in line:
			f2.write(statuscommands)
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
f_sub.close()
os.system('chmod 777 sub*.csh')
