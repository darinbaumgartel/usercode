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
tagname = ''
print '-------------------------------------------------------------------'
print '          Precauationary cleanup... please ignore\n'
os.system('rm RootProcess* *part*.C *part*.h *part*.d *part*.so sub*csh ')
neucopy = False 

newjetscale = '1.0'
newmuscale = '1.0'
newjetres = '0.0'
newmures = '0.0'

StagerCheck = 0
a = sys.argv
for x in range(len(a)):
	if a[x] == '-i':
		ifile = a[x+1]
	if a[x] == '-c':
		cfile = a[x+1]
	if a[x] == '-h':
		hfile = a[x+1]
	if a[x] == '--stager_check':
		StagerCheck=1
	if a[x] == '-t':
		tagname = a[x+1]
	if 'neucopy' in a[x] or 'NEUCOPY' in a[x] or 'NEUcopy' in a[x] or 'NEUCopy' in a[x]:
		neucopy = True
	if a[x] == '--jetscale':
		newjetscale = a[x+1]
	if a[x] == '--muscale':
		newmuscale = a[x+1]
	if a[x] == '--jetres':
		newjetres = a[x+1]
	if a[x] == '--mures':
		newmures = a[x+1]



if cfile == '' or hfile == '' or ifile == '':
	print 'Must specify input .C, .h, and .csv files, e.g.:\n\npython AnalyzerMakerFast.py -i NTupleInfoSpring2011.csv -c NTupleAnalyzer.C -h NTupleAnalyzer.h\n\n   Exiting   \n\n'
	sys.exit()
#if  ifile == '':
	#print 'Must specify input  .csv file, e.g.:\n\npython AnalyzerMakerFast.py -i NTupleInfoSpring2011.csv \n\n   Exiting   \n\n'
	#sys.exit()
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
for x in range(0,len(SigOrBG)):
	#HLTBit[x]=int(HLTBit[x])
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
thiscastor = '/castor/cern.ch/user/'+person[0]+'/'+person+'/LQAnalyzerOutput/'+c2file.replace('.C','')+'_'+tagname+'_'+now
os.system('rfmkdir '+ thiscastor.replace(c2file.replace('.C','')+'_'+now,''))
os.system('rfmkdir '+ thiscastor)
print (' ')
print '-------------------------------------------------------------------'
bjobs = []


for x in range(len(SignalType)):
	
	#cfile=Analyzer[x]+'.C'
	#hfile=Analyzer[x]+'.h'
	
	print 'Preparing '+ SignalType[x]
	path = CastorDirectory[x]	
	FullList = os.popen('nsls '+path).readlines()

	dirList = []
	for y in FullList:
		thistype = y[0:len(SignalType[x])]
		if SignalType[x] ==thistype:
			dirList.append(y)
		
	if StagerCheck:	
		for cf in dirList:
			cf = CastorDirectory[x]+'/' + cf
			fstatus = (((os.popen('stager_qry -M '+cf).readlines())[-1]).split(' '))[-1]
			os.system('sleep .25')
			if 'STAGED' not in fstatus:
				os.system('stager_get -M '+cf)
		
		
	newdirList = []
	sublist = []
	for y in dirList:
		sublist.append(y)
		if len(sublist)>6:
			newdirList.append(sublist)
			sublist =[]
		if y==dirList[-1]:
			newdirList.append(sublist)
			sublist =[]

	for y in range( len(newdirList)):

		part = 'part'+str(y+1)+'of'+str(len(newdirList))

		sub_thisroot = open("sub_"+SignalType[x]+part+".csh",'w')
		sub_thisroot.write('#!/bin/csh\ncd '+thisdir+'\neval `scramv1 runtime -csh`\ncd -\ncp '+thisdir+'/'+c2file.replace('.C','')+'_'+SignalType[x].replace('-','_')+part+'.* .\ncp '+thisdir+'/JSONFilterFunction.* .\ncp '+thisdir+'/ResidualModifier.* .\ncp '+thisdir+'/RootProcesses_'+SignalType[x]+part+' .\nroot -b RootProcesses_'+SignalType[x]+part+'\nrfcp '+c2file.replace('.C','')+'_'+SignalType[x].replace('-','_')+part+'.root '+thiscastor+'\n')
		sub_thisroot.close()

		f_sub.write('\nsleep 1\nbsub -R "pool>10000" -o /dev/null -e /dev/null -q 8nh -J job'+SignalType[x]+part+' < sub_'+SignalType[x]+part+'.csh\n')

		f_thisroot =  open("RootProcesses_"+SignalType[x]+part,'w')


		f_thisroot.write('{\n')
		RootLinesToAdd = 'gROOT->ProcessLine(\"gErrorIgnoreLevel = 3001;\");\ngROOT->ProcessLine(\".L '+c2file.replace('.C','')+'_'+ SignalType[x].replace('-','_') + part+'.C++\");\ngROOT->ProcessLine(\"'+c2file.replace('.C','')+'_'+ SignalType[x].replace('-','_') + part+' t\");\ngROOT->ProcessLine(\"t.Loop()\");\ngROOT->ProcessLine(\"gROOT->Reset()\");\ngROOT->ProcessLine(".q");\n}\n'
		f_thisroot.write(RootLinesToAdd)
		f_thisroot.close()

		bjobs.append(''+c2file.replace('.C','')+'_'+ SignalType[x].replace('-','_') + part )

		s1 = open(cfile).read() # Open the NTupleAnalyzer.C template and replace with array values
		s1 = s1.replace('Numberofevents',str(float(N_orig[x])))
		s1 = s1.replace('placeholder', c2file.replace('.C','')+'_'+SignalType[x].replace('-','_')+part)
		s1 = s1.replace('crosssection', str(float(Xsections[x])))
		s1 = s1.replace('desired_luminosity', str(float(1.0)))
		s1 = s1.replace('FILEINPUT', path + '/' + dirList[0] )
		s1 = s1.replace('MassOfLQ', str(float(MassOfLQ[x])))
		s1 = s1.replace('MyCustomHTCut', str(float(HTRemoveIfGreater[x])))

		
		s1 = s1.replace('Double_t JetRescaleFactor = 1.00;','Double_t JetRescaleFactor = '+newjetscale+';\n')
		s1 = s1.replace('Double_t MuonRescaleFactor = 1.00;','Double_t MuonRescaleFactor = '+newmuscale+';\n')
		s1 = s1.replace('Double_t JetSmearFactor = 0.0;','Double_t JetSmearFactor = '+newjetres+';\n')
		s1 = s1.replace('Double_t MuonSmearFactor = 0.0;','Double_t MuonSmearFactor = '+newmures+';\n')
		

	
		if SignalType[x][0] == 'W' and 'Jets' in SignalType[x][0]:
			s1 = s1.replace('IsItWMC', 'true')
		if SignalType[x][0] != 'W' or 'Jets' not in SignalType[x][0]:
			s1 = s1.replace('IsItWMC', 'false')
			
		if SignalType[x][0] == 'Z' and 'Spring11' in CastorDirectory[x] and 'ALPGEN' in CastorDirectory[x]:
			s1 = s1.replace('IsItSpring11ZAlpgen', 'true')
		if SignalType[x][0] != 'Z' or 'Spring11' in CastorDirectory[x] or 'ALPGEN' in CastorDirectory[x]:
			s1 = s1.replace('IsItSpring11ZAlpgen', 'false')
	
		
	
		#ScaleFacs =  (RescalingInfo[x]).replace('[','').replace(']','').replace(' ','')
		#ScaleFacs = ScaleFacs.split(';')

		#eFac = 1.0
		#muFac = 1.0
		#tauFac = 1.0
		#if len(ScaleFacs)>1:
			#eFac = ScaleFacs[0]
			#muFac = ScaleFacs[1]
			#tauFac = ScaleFacs[2]
		
		#s1 = s1.replace('electron_rescalevalue',str(eFac))
		#s1 = s1.replace('muon_rescalevalue',str(muFac))
		#s1 = s1.replace('tau_rescalevalue',str(tauFac))

		
	#	os.system('rm NTupleAnalyzer_'+SignalType[x]+'.*')
		f1 = open(c2file.replace('.C','')+'_'+SignalType[x].replace('-','_')+part+".C", 'w') # write a new file based on the template
		f1.write(s1)
		f1.close()
		
	
		s2 = open(hfile) # Same deal for the .h file now...
		f2 = open(c2file.replace('.C','')+'_'+SignalType[x].replace('-','_')+part+".h", 'w')
		for line in s2.readlines():
			line = line.replace('placeholder', c2file.replace('.C','')+'_'+SignalType[x].replace('-','_')+part)
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

subjobs = ''
if '--autorun' in sys.argv:
	subjobs='y'
while subjobs != 'y' and subjobs != 'n':
	subjobs = raw_input('\n\n  Would you like to automatically submit and check jobs now? (answer y/n):  ')
if subjobs == 'n':
	print '\n\n Jobs can be submitted now using the submission command:\n\n    ./sub_AllAnalyzer.csh\n'
	print '\n If you wish to test functionality, run a single root process like:\n'
	print '  root -l RootProcesses_TTJetspart1of4  (or whatever RootProcesses file you have available)\n\n'
	sys.exit()

os.system('./sub_AllAnalyzer.csh')   ##FIXME

	
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
		print  str(jobsleft) +' jobs remaining.'
	
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
thistemp = '/tmp/'+person+'/'+c2file.replace('.C','')+'_'+tagname+'_'+now
os.system('mkdir '+thistemp)


print ('Waiting for file transfers to complete\n\n')

for x in castorinfo:
	os.system('sleep .1')
	os.system('rfcp '+thiscastor+'/'+x.replace('\n','')+' '+thistemp+' &')
ok = 0
oldduinfo = ''
duinfo = '-'
timeoutcount = 0
while ok!=1:
	unfin = 0
	ok = 1
	tempinfo =  os.popen('ls -1 '+thistemp).readlines()
	tempinfo = str(tempinfo)
	os.system('sleep 30')
	os.system('sleep 30')

	os.system('sleep 300')

	waiting = 1
	while waiting != 0:
		os.system('sleep 30')
		print "Running recovery on "+str(len(os.popen('bjobs').readlines()))+" bjobs. "
		if len(os.popen('bjobs').readlines()) == 0:
			waiting = 0
		

	fsubs = open('resub_tmp.csh','w')
	frfcps = open('rfcp_tmp.csh','w')
	fsubs.write('#!/bin/csh\n\n')
	frfcps.write('#!/bin/csh\n\n')

	castorinfo = os.popen('nsls '+thiscastor).readlines()

	
	for x in bjobs:
		if x.replace(c2file.replace('.C','')+'_','') not in tempinfo:
			print 'Missing '+x.replace(c2file.replace('.C','')+'_','') 
			unfin += 1
			ok = 0
			filegrep = x.replace(c2file.replace('.C','')+'_','')
			filegrep = filegrep.replace('-','_')
			for rr in range(3):
				filegrep = filegrep.replace('__','_')
				
			filegrep = filegrep.replace('_',' | grep  ')
			filegrep = 'cat sub_AllAnalyzer.csh | grep '+filegrep
			
			#resubinfo = os.popen('cat sub_AllAnalyzer.csh | grep '+x.replace(c2file.replace('.C','')+'_','') ).readlines()
			resubinfo = os.popen( filegrep ).readlines()

			rfcpcoms = []
			
			
			if (x.replace(c2file.replace('.C','')+'_','')  in str(castorinfo)): 
				if (x.replace(c2file.replace('.C','')+'_','') not in str(tempinfo)) :
					for y in castorinfo:
						if x.replace(c2file.replace('.C','')+'_','') in y:
							rfcpcoms.append('rfcp '+thiscastor+'/'+y.replace('\n','')+' '+thistemp+' &')
			for com in resubinfo:
				fsubs.write(com+'\n')
			for rfcpcom in rfcpcoms:
				frfcps.write(rfcpcom+'\n')
				
	fsubs.close()
	frfcps.close()
	os.system("chmod 777 resub*csh rfcp*csh")
	os.system("./resub_tmp.csh")


	#sys.exit()   ##  FIXME

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
			print  str(jobsleft) +' jobs remaining.'
	os.system('sleep 60')
	os.system("./rfcp_tmp.csh")

			
	duinfo = (os.popen('du -s '+thistemp).readlines())[0]
	if duinfo != oldduinfo:
		ok = 0
	oldduinfo = duinfo
	#print 'Waiting on '+str(unfin)+' files to transfer.\n' 

print ('\n\n Analysis and transfer complete. Grouping files for easier use. Please wait !')
os.system('sleep 300')

os.system('mkdir '+thistemp+'/SummaryFiles')
os.system('rfmkdir '+thiscastor+'/SummaryFiles')
	
os.system('cmsenv')

groups = []
for x in range(len(SignalType)):
	if Group[x] not in groups:
		groups.append(Group[x])
Contents = []
for g in groups:
	Contents.append([])
for g in range(len(groups)):
	for x in range(len(SignalType)):
		if groups[g] == Group[x]:
			Contents[g].append(SignalType[x])
for g in range(len(groups)):
	haddstring = 'hadd '+thistemp+'/SummaryFiles/'+groups[g]+'.root'
	for c in Contents[g]:
		haddstring += ' '+thistemp+'/*'+c.replace('-','_')+'*root'+' '
	os.system(haddstring)
	os.system('rfcp '+thistemp+'/SummaryFiles/'+groups[g]+'.root '+thiscastor+'/SummaryFiles')

print '-------------------------------------------------------------------'
print '         Cleaning up temporary files\n'
from subprocess import call
print '         Removing Root Run Processes' 
call('rm RootProcess*',shell=True)
print '         Removing Temporary C/h modules'
call('rm *part*',shell=True)
print '         Removing batch submission scripts'
call('rm sub*csh',shell=True)
print (' ')
print '-------------------------------------------------------------------'

print ('\n\n'+140*'*'+ '\n\n      Analysis Complete. A full set of output files can be found in  \n\n       '+thiscastor+'/SummaryFiles\n')
os.system('nsls -l '+thiscastor+'/SummaryFiles')
print ('\n\n'+140*'*'+ '\n\n')

if neucopy == False:
	sys.exit()

print ('Please wait - transfering output additionally to neu machine. ')
neudir =  '/home/'+person+'/LQAnalyzerOutput/'
os.system('rm '+thistemp+'/*.*')
os.system('scp -r '+thistemp+' neu:'+neudir)

print ('Transfer Complete. ')

