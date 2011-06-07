#################################################################################################
##########                    N Tuple Analyzer Script Producer                        ###########
##########      Store NTuple Info In NTupleInfo.csv File in current Directory         ###########
##########      Darin Baumgartel - May 31, 2011 - darin.carl.baumgartel@cern.ch      ###########
#################################################################################################

import os # For direcory scanning abilities, etc
from time import strftime
import sys

cfile = ''
hfile = ''
ifile = ''

a = sys.argv
for x in range(len(a)):
	if a[x] == '-i':
		ifile = a[x+1]
	if a[x] == '-c':
		cfile = a[x+1]
	if a[x] == '-h':
		hfile = a[x+1]	

if cfile == '' or hfile == '' or ifile == '':
	print 'Must specify input .C, .h, and .csv files, e.g.:\n\npython AnalyzerMakerFast.py -i NTupleInfoSpring2011.csv -c NTupleAnalyzer.C -h NTupleAnalyzer.h\n\n   Exiting   \n\n'
	sys.exit()

### This portion reads the NTupleInfo.csv file and gets the information ###
import csv
csvfile = open(ifile,'r')
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
f1 = open(hfile,'r')
statuscommands = ''

variables = []
for line in f1:
	if 'SetBranchAddress' in line:
		var = (line.split('\"')[1])
		variables.append( ((var.replace('\n','')).replace('\r','')).replace(' ','')  )
for x in variables:
	use =0
	f2 = open(cfile,'r')
	for line in f2:
		if x in line:	
			use = 1
	if use ==1:
		statuscommands += '   fChain->SetBranchStatus("'+x+'",1);\n'
	else:
		statuscommands += '   fChain->SetBranchStatus("'+x+'",0);\n'
	f2.close()
f1.close()

c2file = cfile.split('/')[-1]

###----------------------------------------------------------------------###

now=str(strftime("%Y-%m-%d-%H:%M:%S"))
now = now.replace(" ","")
now = now.replace("\t","")
now = now.replace("-","_")
now = now.replace(":","_")

WhatType=['Background','Signal','CollisionData'] # So that WhatType[SigOrBG[x]] returns string "Signal" or "Background"

# initialize file that stores root processes to be run

f_sub = open("sub_AllAnalyzer.csh", 'w')
f_sub.write('#!/bin/csh')


thisdir = os.popen('pwd').readlines()[0].replace('\n','')
person = os.popen('whoami').readlines()[0].replace('\n','')
thiscastor = '/castor/cern.ch/user/'+person[0]+'/'+person+'/LQAnalyzerOutput/'+c2file.replace('.C','')+'_'+now
os.system('rfmkdir '+ thiscastor.replace(c2file.replace('.C','')+'_'+now,''))
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
		sub_thisroot.write('#!/bin/csh\ncd '+thisdir+'\neval `scramv1 runtime -csh`\ncd -\ncp '+thisdir+'/'+c2file.replace('.C','')+'_'+SignalType[x].replace('-','_')+part+'.* .\ncp '+thisdir+'/JSONFilterFunction.* .\ncp '+thisdir+'/RootProcesses_'+SignalType[x]+part+' .\nroot -b RootProcesses_'+SignalType[x]+part+'\nrfcp '+SignalType[x].replace('-','_')+part+'.root '+thiscastor+'\n')
		sub_thisroot.close()

		f_sub.write('\nsleep 1\nbsub -R "pool>10000" -o /dev/null -e /dev/null -q 1nd -J job'+SignalType[x]+part+' < sub_'+SignalType[x]+part+'.csh\n')

		f_thisroot =  open("RootProcesses_"+SignalType[x]+part,'w')


		f_thisroot.write('{\n')
		RootLinesToAdd = 'gROOT->ProcessLine(\"gErrorIgnoreLevel = 3001;\");\ngROOT->ProcessLine(\".L '+c2file.replace('.C','')+'_'+ SignalType[x].replace('-','_') + part+'.C++\");\ngROOT->ProcessLine(\"'+c2file.replace('.C','')+'_'+ SignalType[x].replace('-','_') + part+' t\");\ngROOT->ProcessLine(\"t.Loop()\");\ngROOT->ProcessLine(\"gROOT->Reset()\");\ngROOT->ProcessLine(".q");\n}\n'
		f_thisroot.write(RootLinesToAdd)
		f_thisroot.close()

		bjobs.append(''+c2file.replace('.C','')+'_'+ SignalType[x].replace('-','_') + part )

		s1 = open(cfile).read() # Open the NTupleAnalyzer.C template and replace with array values
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
		f1 = open(c2file.replace('.C','')+'_'+SignalType[x].replace('-','_')+part+".C", 'w') # write a new file based on the template
		f1.write(s1)
		f1.close()
		
	
		s2 = open(hfile) # Same deal for the .h file now...
		f2 = open(c2file.replace('.C','')+'_'+SignalType[x].replace('-','_')+part+".h", 'w')
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
	RootLinesToAdd = 'gROOT->ProcessLine(\"gErrorIgnoreLevel = 3001;\");\ngROOT->ProcessLine(\".L '+c2file.replace('.C','')+'_'+ SignalType[x] + '.C++\");\ngROOT->ProcessLine(\"'+c2file.replace('.C','')+'_'+ SignalType[x] + ' t\");\ngROOT->ProcessLine(\"t.Loop()\");\ngROOT->ProcessLine(\"gROOT->Reset()\");\n\n'
	
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
	if x.replace(c2file.replace('.C','')+'_','') not in castorinfo:
		ok = 0
		print (x +' is missing from castor directory.')	

if ok == 1:
	print ('Castor directory check OK. All files present. Copying castor files to temp.\n\n')

castorinfo = os.popen('nsls '+thiscastor).readlines()

os.system
thistemp = '/tmp/'+person+'/'+c2file.replace('.C','')+'_'+now
os.system('mkdir '+thistemp)

print ('Waiting for file transfers to complete\n\n')

for x in castorinfo:
	os.system('sleep .3')
	os.system('rfcp '+thiscastor+'/'+x.replace('\n','')+' '+thistemp+'&')

ok = 0
while ok!=1:
	unfin = 0
	ok = 1
	tempinfo =  os.popen('ls -1 '+thistemp).readlines()
	tempinfo = str(tempinfo)
	os.system('sleep 20')
	for x in bjobs:
		if x.replace(c2file.replace('.C','')+'_','') not in tempinfo:
			unfin += 1
			ok = 0
	print 'Waiting on '+str(unfin)+' files to transfer.\n' 

print ('\n\n Analysis and transfer complete.')


