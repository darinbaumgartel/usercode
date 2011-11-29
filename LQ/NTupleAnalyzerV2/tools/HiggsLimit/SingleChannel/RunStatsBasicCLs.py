import os
import sys
import subprocess
import matplotlib.pyplot
# Check the root version
 
ESTIMATIONMETHOD = ' -M Asymptotic '
METHOD = '-M HybridNew --rule CLs --frequentist CONFIGURATION --clsAcc=0 -s -1 -T 100 -i 50 --singlePoint SINGLEPOINT --saveToys --saveHybridResult'
person = (os.popen('whoami').readlines())[0].replace('\n','')


rootinfo = os.popen('root -b -q').readlines()
hostinfo = os.popen('hostname').readline()
hostinfo = str(hostinfo)

rootinfo2 = str(rootinfo)

rootinfo = rootinfo[4].split()[2].split('/')[0]
rootinfo = float(rootinfo)

do_BetaOne = 0
do_BetaHalf = 0 
do_combo = 0
do_observedonly = 0
cdir = ''
if 'do_BetaOne' in str(sys.argv):
	do_BetaOne = 1
if 'do_BetaHalf' in str(sys.argv):
	do_BetaHalf = 1
if 'do_combo' in str(sys.argv):
	do_combo = 1
if 'just_observed' in str(sys.argv):
	do_observedonly = 1	
numdo = 1	
queue = '1nd'
launcher = 'launcherCLs.py'
iters = 1
for x in range(len(sys.argv)):
	if sys.argv[x] == '-c':
		cdir = sys.argv[x+1]
		os.system('rfmkdir /castor/cern.ch/user/d/darinb/CLSLimits/BetaOne'+cdir)
		os.system('rfmkdir /castor/cern.ch/user/d/darinb/CLSLimits/BetaHalf'+cdir)
		os.system('mkdir '+cdir)
	if sys.argv[x] == '-n':
		numdo = int(sys.argv[x+1])
	if sys.argv[x] == '-q':
		queue = str(sys.argv[x+1])
	if sys.argv[x] == '-l':
		launcher = str(sys.argv[x+1])	
	if sys.argv[x] == '--iters':
		iters = int(sys.argv[x+1])		
from ROOT import *
from array import array

beta_combo = []
m_combo = []
dif_combo = []
cr = '  \n'

fullcards = open('FinalCards.txt','r')
mycards = []
for line in fullcards:
	mycards.append(line.replace('\n',''))

name = []
for x in mycards:
	if '.txt' in x:
		name.append((x.replace('.txt','')).replace('\n','')) 


if do_BetaOne == 1:
	for x in range(len(name)):
		if 'BetaHalf' in name[x]:
			continue
		print 'Calculating limit for: ' + name[x]
		f = open('confbetaone_'+cdir+'_'+name[x]+'.cfg','w')
		count = 0
		print name[x]
		for l in mycards:
			if count ==1:
				f.write(l+'\n')
			if 'BetaHalf' not in l and '.txt' in l:
				newname = l
				if name[x] in newname:
					print newname
					count = 1
				else:
					count = 0
		os.system('rfmkdir /castor/cern.ch/user/d/darinb/CLSLimits/BetaOne'+cdir+'/'+name[x])
		f.close()

		mdir = (os.popen('pwd').readlines())[0]
		mdir = mdir.replace('\n','')
		fsub = open('subbetaone_'+cdir+name[x]+'.csh','w')
		fsub.write('#!/bin/csh'+ cr)
		fsub.write('cd ' + mdir+ cr)
		fsub.write('eval `scramv1 runtime -csh`'+ cr)
		fsub.write('cd -'+ cr)
		fsub.write('cp '+mdir+'/confbetaone_'+cdir+'_'+name[x]+ '.cfg . '+ cr)
		fsub.write('SUBCOMMAND'+'\n')
		fsub.write('cp log*.txt '+mdir+'/'+cdir+'/'+ cr +cr +cr)
		fsub.write('rfcp log*.txt /castor/cern.ch/user/d/darinb/CLSLimits/BetaOne'+cdir+'/'+ cr +cr +cr)
		fsub.write('rfcp *root /castor/cern.ch/user/d/darinb/CLSLimits/BetaOne'+cdir+'/'+name[x]+'/'+ cr +cr +cr)			
		fsub.close()
		
		
		EstimationInformation = os.popen('combine '+ESTIMATIONMETHOD+' confbetaone_'+cdir+'_'+name[x]+'.cfg ').readlines()
		
		expectedlines = []
		for line in EstimationInformation:
			if 'Expected' in line and 'r <' in line:
				expectedlines.append(line.replace('\n',''))
		values = []
		for e in expectedlines:
			print e
			values.append(float(e.split()[-1]))
		print values
		
		vstart = round((min(values)/3),5)
		vstop = round((max(values)*3),5)
		rvalues = []
		interval = abs(vstop-vstart)/100.0
		
		nindex = 0
		thisr = 0
		while thisr<vstop:
			thisr = vstart*1.03**(float(nindex))
			rvalues.append(thisr)
			nindex +=1
		#for n in range(100):
			#rvalues.append(vstart+n*interval)
		strRvalues = []
		for r in rvalues:
			strRvalues.append(str(round(r,5)))
		print strRvalues
		
		for r in strRvalues:
			command = 'combine '+METHOD.replace('SINGLEPOINT',r).replace('CONFIGURATION','confbetaone_'+cdir+'_'+name[x]+'.cfg')
			strR = r.replace('.','_')
			os.system('cat subbetaone_'+cdir+name[x]+'.csh | sed  \'s/SUBCOMMAND/'+command+'/g\'  > subbetaone_'+strR+'_'+cdir+name[x]+'.csh')
			os.system('chmod 777 *csh')

			for nn in range(numdo):
				os.system('bsub -o /dev/null -e /dev/null -q '+queue+' -J jobbetaone'+str(nn)+'_'+name[x]+' < subbetaone_'+strR+'_'+cdir+name[x]+'.csh')
				#print('bsub -o /dev/null -e /dev/null -q '+queue+' -J jobbetaone'+str(nn)+'_'+name[x]+' < subbetaone_'+strR+'_'+cdir+name[x]+'.csh')



if do_BetaHalf == 1:
	
	for x in range(len(name)):
		if 'BetaHalf' not in name[x]:
			continue		
		print 'Calculating limit for: ' + name[x]			
		f = open('confbetahalf_'+cdir+'_'+name[x]+'.cfg','w')
		count = 0
		print name[x]
		for l in mycards:
			if '.txt' in l and 'BetaHalf' not in l:
				break			
			if count ==1:
				f.write(l+'\n')
			if 'BetaHalf' in l and '.txt' in l:
				newname = l
				if name[x].replace('LQ','') in newname:
					print newname
					count = 1
				else:
					count = 0
		os.system('rfmkdir /castor/cern.ch/user/d/darinb/CLSLimits/BetaHalf'+cdir+'/'+name[x])

		f.close()
					

		mdir = (os.popen('pwd').readlines())[0]
		mdir = mdir.replace('\n','')
		fsub = open('subbetahalf_'+cdir+name[x]+'.csh','w')
		fsub.write('#!/bin/csh'+ cr)
		fsub.write('cd ' + mdir+ cr)
		fsub.write('eval `scramv1 runtime -csh`'+ cr)
		fsub.write('cd -'+ cr)
		fsub.write('cp '+mdir+'/confbetahalf_'+cdir+'_'+name[x]+ '.cfg . '+ cr)
		fsub.write('SUBCOMMAND'+'\n')
		fsub.write('cp log*.txt '+mdir+'/'+cdir+'/'+ cr +cr +cr)
		fsub.write('rfcp log*.txt /castor/cern.ch/user/d/darinb/CLSLimits/BetaHalf'+cdir+'/'+ cr +cr +cr)
		fsub.write('rfcp *root /castor/cern.ch/user/d/darinb/CLSLimits/BetaHalf'+cdir+'/'+name[x]+'/'+ cr +cr +cr)			
		fsub.close()
		
		
		EstimationInformation = os.popen('combine '+ESTIMATIONMETHOD+' confbetahalf_'+cdir+'_'+name[x]+'.cfg ').readlines()
		
		expectedlines = []
		for line in EstimationInformation:
			if 'Expected' in line and 'r <' in line:
				expectedlines.append(line.replace('\n',''))
		values = []
		for e in expectedlines:
			print e
			values.append(float(e.split()[-1]))
		print values
		
		
		vstart = round((min(values)/3),5)
		vstop = round((max(values)*3),5)
		rvalues = []
		interval = abs(vstop-vstart)/100.0
		
		nindex = 0
		thisr = 0
		while thisr<vstop:
			thisr = vstart*1.03**(float(nindex))
			rvalues.append(thisr)
			nindex += 1
		#for n in range(100):
			#rvalues.append(vstart+n*interval)		
		#vstart = round((min(values)/3.0),5)
		#vstop = round((max(values)*3.0),5)
		#rvalues = []
		#interval = abs(vstop-vstart)/70.0
		#for n in range(100):
			#rvalues.append(vstart+n*interval)
		strRvalues = []
		for r in rvalues:
			strRvalues.append(str(round(r,5)))
		print strRvalues
		
		for r in strRvalues:
			command = 'combine '+METHOD.replace('SINGLEPOINT',r).replace('CONFIGURATION','confbetahalf_'+cdir+'_'+name[x]+'.cfg')
			strR = r.replace('.','_')
			os.system('cat subbetahalf_'+cdir+name[x]+'.csh | sed  \'s/SUBCOMMAND/'+command+'/g\'  > subbetahalf_'+strR+'_'+cdir+name[x]+'.csh')
			os.system('chmod 777 *csh')

			for nn in range(numdo):
				os.system('bsub -o /dev/null -e /dev/null -q '+queue+' -J jobbetahalf'+str(nn)+'_'+name[x]+' < subbetahalf_'+strR+'_'+cdir+name[x]+'.csh')
				#print('bsub -o /dev/null -e /dev/null -q '+queue+' -J jobbetahalf'+str(nn)+'_'+name[x]+' < subbetahalf_'+strR+'_'+cdir+name[x]+'.csh')
