#################################################################################################
##########                    N Tuple Analyzer Script Producer                        ###########
##########      Store NTuple Info In NTupleInfo.csv File in current Directory         ###########
##########      Darin Baumgartel - May 31, 2011 - darin.carl.baumgartel@cern.ch      ###########
#################################################################################################

import os # For direcory scanning abilities, etc
from time import strftime
import sys

myfile = sys.argv[1]

### This portion reads the NTupleInfo.csv file and gets the information ###
import csv
csvfile = open(myfile,'r')
table=[]

for row in csv.reader(csvfile):
	if len(row) == 0:
		continue
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

f_sub = open("sub_AllAnalyzer.csh", 'w')
f_sub.write('#!/bin/csh')


thisdir = os.popen('pwd').readlines()[0].replace('\n','')
person = os.popen('whoami').readlines()[0].replace('\n','')
thiscastor = '/castor/cern.ch/user/'+person[0]+'/'+person+'/LQAnalyzerOutput/NTupleAnalyzer_'+now
os.system('rfmkdir '+ thiscastor.replace('NTupleAnalyzer_'+now,''))
os.system('rfmkdir '+ thiscastor)

bjobs = []

for x in range(len(SignalType)):
	
	print 'Preparing '+ SignalType[x]
	path = CastorDirectory[x]	
	FullList = os.popen('nsls '+path).readlines()

	dirList = []
	for y in FullList:
		thistype = y[0:len(SignalType[x])]
		if SignalType[x] ==thistype:
			dirList.append(y)

	newdirList = []
	sublist = []
	for y in dirList:
		sublist.append(y)
		if len(sublist)>14:
			newdirList.append(sublist)
			sublist =[]
		if y==dirList[-1]:
			newdirList.append(sublist)
			sublist =[]

	for y in range( len(newdirList)):

		part = 'part'+str(y+1)+'of'+str(len(newdirList))

		sub_thisroot = open("sub_"+SignalType[x]+part+".csh",'w')
		sub_thisroot.write('#!/bin/csh\ncd '+thisdir+'\neval `scramv1 runtime -csh`\ncd -\ncp '+thisdir+'/NTupleAnalyzer_'+SignalType[x].replace('-','_')+part+'.* .\ncp '+thisdir+'/RootProcesses_'+SignalType[x]+part+' .\nroot -b RootProcesses_'+SignalType[x]+part+'\nrfcp '+SignalType[x].replace('-','_')+part+'.root '+thiscastor+'\n')
		sub_thisroot.close()

		f_sub.write('\nsleep 5\nbsub -R "pool>50000" -o /dev/null -e /dev/null -q 1nd -J job'+SignalType[x]+part+' < sub_'+SignalType[x]+part+'.csh\n')

		f_thisroot =  open("RootProcesses_"+SignalType[x]+part,'w')


		f_thisroot.write('{\n')
		RootLinesToAdd = 'gROOT->ProcessLine(\"gErrorIgnoreLevel = 3001;\");\ngROOT->ProcessLine(\".L NTupleAnalyzer_'+ SignalType[x].replace('-','_') + part+'.C++\");\ngROOT->ProcessLine(\"NTupleAnalyzer_'+ SignalType[x].replace('-','_') + part+' t\");\ngROOT->ProcessLine(\"t.Loop()\");\ngROOT->ProcessLine(\"gROOT->Reset()\");\ngROOT->ProcessLine(".q");\n}\n'
		f_thisroot.write(RootLinesToAdd)
		f_thisroot.close()

		bjobs.append('NTupleAnalyzer_'+ SignalType[x].replace('-','_') + part )

		s1 = open("NTupleAnalyzer.C").read() # Open the NTupleAnalyzer.C template and replace with array values
		s1 = s1.replace('Numberofevents',str(float(N_orig[x])))
		s1 = s1.replace('placeholder', SignalType[x].replace('-','_')+part)
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
		f1 = open("NTupleAnalyzer_"+SignalType[x].replace('-','_')+part+".C", 'w') # write a new file based on the template
		f1.write(s1)
		f1.close()
		
	
		s2 = open("NTupleAnalyzer.h") # Same deal for the .h file now...
		f2 = open("NTupleAnalyzer_"+SignalType[x].replace('-','_')+part+".h", 'w')
		for line in s2.readlines():
			line = line.replace('placeholder', SignalType[x].replace('-','_')+part)
			f2.write(line)
			if 'filetracermark000' in line:	
				f2.write('\nTChain * chain = new TChain(\"rootTupleTree/tree\",\"\");\n')
				for z in range(len(newdirList[y])):
					thisline = '\nchain->Add(\"rfio://' + path + '/' + newdirList[y][z] + '");\n'
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
	
f_sub.close()
os.system('chmod 777 sub*.csh')

os.system('./sub_AllAnalyzer.csh')

done = 0
print '\n Waiting for job completion. Status as follows: \n\n'
while done!=1:
	os.system('sleep 30')
	jobinfo = os.popen('bjobs').readlines()
	jobinfo = len(jobinfo)
	jobsleft = jobinfo -1
	if jobsleft == -1:
		done = 1
	if jobsleft>=0:
		print '\n' + str(jobsleft) +' jobs remaining.'
	
print '\n Checking output root files in directory '+thiscastor+' \n\n'

castorinfo = os.popen('nsls '+thiscastor).readlines()
castorinfo = str(castorinfo)
ok = 1
for x in bjobs:
	if x.replace('NTupleAnalyzer_','') not in castorinfo:
		ok = 0
		print (x +' is missing from castor directory.')	

if ok == 1:
	print ('Castor directory check OK. All files present. Copying castor files to temp.\n\n')

castorinfo = os.popen('nsls '+thiscastor).readlines()

os.system
thistemp = '/tmp/'+person+'/NTupleAnalyzer_'+now
os.system('mkdir '+thistemp)
for x in castorinfo:
	os.system('rfcp '+thiscastor+'/'+x.replace('\n','')+' '+thistemp)
print ('\n\n Analysis and transfer complete.')



