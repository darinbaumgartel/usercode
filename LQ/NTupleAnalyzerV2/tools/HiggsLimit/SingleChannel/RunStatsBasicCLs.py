import os
import sys
import subprocess
import matplotlib.pyplot
 
ESTIMATIONMETHOD = ' -M Asymptotic '
METHOD = '-M HybridNew --rule CLs --frequentist CONFIGURATION --clsAcc=0 -s -1 -T 50 -i 40 --singlePoint SINGLEPOINT --saveToys --saveHybridResult'
person = (os.popen('whoami').readlines())[0].replace('\n','')

masses = []
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
iters = 1
if 'CLSLimits' not in os.listdir('.'):
	os.system('mkdir CLSLimits')
if 'ShellScriptsForBatch' not in os.listdir('.'):
	os.system('mkdir ShellScriptsForBatch')
os.system('rfmkdir /castor/cern.ch/user/'+person[0]+'/'+person+'/CLSLimits'+cdir)

dobatch = True
for x in range(len(sys.argv)):
	if sys.argv[x] == '-c':
		cdir = sys.argv[x+1]
		os.system('rfmkdir /castor/cern.ch/user/'+person[0]+'/'+person+'/CLSLimits/BetaOne'+cdir)
		os.system('rfmkdir /castor/cern.ch/user/'+person[0]+'/'+person+'/CLSLimits/BetaHalf'+cdir)
		os.system('mkdir CLSLimits/BetaOne'+cdir)
		os.system('mkdir CLSLimits/BetaHalf'+cdir)
	if sys.argv[x] == '-n':
		numdo = int(sys.argv[x+1])
	if sys.argv[x] == '-q':
		queue = str(sys.argv[x+1])
	if sys.argv[x] == '--iters':
		iters = int(sys.argv[x+1])		
	if '--Asymptotic_Only' in sys.argv[x]:
		dobatch = False 
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

digis = '0123456789'
name = []
for x in mycards:
	if '.txt' in x:
		name.append((x.replace('.txt','')).replace('\n','')) 
		mm = ''
		for a in x:
			if a in digis:
				mm += a
		if int(mm) not in masses:
			masses.append(int(mm))

BetaOneObs = []
BetaOne95down = []
BetaOne95up = []
BetaOne68down = []
BetaOne68up = []
BetaOneExp = []

BetaHalfObs = []
BetaHalf95down = []
BetaHalf95up = []
BetaHalf68down = []
BetaHalf68up = []
BetaHalfExp = []

ComboObs = []
Combo95down = []
Combo95up = []
Combo68down = []
Combo68up = []
ComboExp = []

if do_BetaOne == 1:
	for x in range(len(name)):
		if 'BetaHalf' in name[x]:
			continue
		print 'Calculating limit for: ' + name[x]
		f = open('CLSLimits/BetaOne'+cdir+'/confbetaone_'+cdir+'_'+name[x]+'.cfg','w')
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
	
		f.close()

		os.system('rfmkdir /castor/cern.ch/user/'+person[0]+'/'+person+'/CLSLimits/BetaOne'+cdir+'/'+name[x])
		os.system('rfcp CLSLimits/BetaOne'+cdir+'/confbetaone_'+cdir+'_'+name[x]+'.cfg /castor/cern.ch/user/'+person[0]+'/'+person+'/CLSLimits/BetaOne'+cdir+'/')
		os.system('mkdir CLSLimits/BetaOne'+cdir+'/'+name[x])

		mdir = (os.popen('pwd').readlines())[0]
		mdir = mdir.replace('\n','')
		fsub = open('ShellScriptsForBatch/subbetaone_'+cdir+name[x]+'.csh','w')
		fsub.write('#!/bin/csh'+ cr)
		fsub.write('cd ' + mdir+ cr)
		fsub.write('eval `scramv1 runtime -csh`'+ cr)
		fsub.write('cd -'+ cr)
		fsub.write('cp '+mdir+'/CLSLimits/BetaOne'+cdir+'/confbetaone_'+cdir+'_'+name[x]+ '.cfg . '+ cr)
		fsub.write('SUBCOMMAND'+'\n')
		if '--castor_only' not in sys.argv:
			fsub.write('cp *root '+mdir+'/CLSLimits/BetaOne'+cdir+'/'+name[x]+'/'+ cr +cr )					
		fsub.write('rfcp *root /castor/cern.ch/user/'+person[0]+'/'+person+'/CLSLimits/BetaOne'+cdir+'/'+name[x]+'/'+ cr +cr )			
		fsub.close()
		
		## Estimate the r values with Asymptotic CLs
		EstimationInformation = [' r < 0.0000']
		rmax = 1000.0
		breaker = False 
		while 'r < 0.0000' in str(EstimationInformation):
			EstimationInformation = os.popen('combine '+ESTIMATIONMETHOD+' CLSLimits/BetaOne'+cdir+'/confbetaone_'+cdir+'_'+name[x]+'.cfg --rMax '+str(rmax)).readlines()
			if breaker ==True:
				break
			if 'r < 0.0000' not in str(EstimationInformation):
				effrmax = -999999
				for e in EstimationInformation:
					if 'r <'  in e and 'Expected' in e:
						thisrval = e.split('<')[-1]
						thisrval = thisrval.replace('\n','')
						thisrval = float(thisrval)
						if thisrval>effrmax:
							effrmax = thisrval
				rmax = effrmax*15.0
				EstimationInformation = [' r < 0.0000']
				breaker = True
			rmax = rmax/5.0
		## Estimation Complete

		
		expectedlines = []
		for line in EstimationInformation:
			if 'Expected' in line and 'r <' in line:
				expectedlines.append(line.replace('\n',''))
		values = []
		for e in expectedlines:
			print e
			values.append(float(e.split()[-1]))
		
		## Fill the arrays of Asymptotic Values
		for line in EstimationInformation:
			if 'Observed' in line and '<' in line:
				BetaOneObs.append((line.split('<')[-1]).replace('\n',''))
			if 'Expected' in line and '<' in line:
				if '2.5%' in line:
					BetaOne95down.append((line.split('<')[-1]).replace('\n',''))
				if '16.0%' in line:
					BetaOne68down.append((line.split('<')[-1]).replace('\n',''))
				if '50.0%' in line:
					BetaOneExp.append((line.split('<')[-1]).replace('\n',''))
				if '84.0%' in line:
					BetaOne68up.append((line.split('<')[-1]).replace('\n',''))
				if '97.5%' in line:
					BetaOne95up.append((line.split('<')[-1]).replace('\n',''))

				
		
		vstart = round((min(values)/3),5)
		vstop = round((max(values)*3),5)
		rvalues = []
		interval = abs(vstop-vstart)/100.0
		
		nindex = 0
		thisr = 0
		while thisr<vstop:
			thisr = vstart*1.1**(float(nindex))
			rvalues.append(thisr)
			nindex +=1
		strRvalues = []
		for r in rvalues:
			strRvalues.append(str(round(r,5)))
		print strRvalues
		
		for r in strRvalues:
			command = 'combine '+METHOD.replace('SINGLEPOINT',r).replace('CONFIGURATION','confbetaone_'+cdir+'_'+name[x]+'.cfg')
			strR = r.replace('.','_')
			os.system('cat ShellScriptsForBatch/subbetaone_'+cdir+name[x]+'.csh | sed  \'s/SUBCOMMAND/'+command+'/g\'  > ShellScriptsForBatch/subbetaone_'+strR+'_'+cdir+name[x]+'.csh')
			os.system('chmod 777 ShellScriptsForBatch/subbetaone_'+strR+'_'+cdir+name[x]+'.csh')

			for nn in range(numdo):
				if (dobatch):
					os.system('bsub -o /dev/null -e /dev/null -q '+queue+' -J jobbetaone'+str(nn)+'_R_'+strR+'_'+name[x]+' < ShellScriptsForBatch/subbetaone_'+strR+'_'+cdir+name[x]+'.csh')

if do_BetaHalf == 1:
	
	for x in range(len(name)):
		if 'BetaHalf' not in name[x]:
			continue		
		print 'Calculating limit for: ' + name[x]			
		f = open('CLSLimits/BetaHalf'+cdir+'/confbetahalf_'+cdir+'_'+name[x]+'.cfg','w')
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
		f.close()

		os.system('rfmkdir /castor/cern.ch/user/'+person[0]+'/'+person+'/CLSLimits/BetaHalf'+cdir+'/'+name[x])
		os.system('rfcp CLSLimits/BetaHalf'+cdir+'/confbetahalf_'+cdir+'_'+name[x]+'.cfg /castor/cern.ch/user/'+person[0]+'/'+person+'/CLSLimits/BetaHalf'+cdir+'/')
	
		os.system('mkdir CLSLimits/BetaHalf'+cdir+'/'+name[x])

		mdir = (os.popen('pwd').readlines())[0]
		mdir = mdir.replace('\n','')
		fsub = open('ShellScriptsForBatch/subbetahalf_'+cdir+name[x]+'.csh','w')
		fsub.write('#!/bin/csh'+ cr)
		fsub.write('cd ' + mdir+ cr)
		fsub.write('eval `scramv1 runtime -csh`'+ cr)
		fsub.write('cd -'+ cr)
		fsub.write('cp '+mdir+'/CLSLimits/BetaHalf'+cdir+'/confbetahalf_'+cdir+'_'+name[x]+ '.cfg . '+ cr)
		fsub.write('SUBCOMMAND'+'\n')
		if '--castor_only' not in sys.argv:
			fsub.write('cp *root '+mdir+'/CLSLimits/BetaHalf'+cdir+'/'+name[x]+'/'+ cr +cr )					
		fsub.write('rfcp *root /castor/cern.ch/user/'+person[0]+'/'+person+'/CLSLimits/BetaHalf'+cdir+'/'+name[x]+'/'+ cr +cr )			
		fsub.close()
		
		## Estimate the r values with Asymptotic CLs
		EstimationInformation = [' r < 0.0000']
		rmax = 1000.0
		breaker = False 
		while 'r < 0.0000' in str(EstimationInformation):
			EstimationInformation = os.popen('combine '+ESTIMATIONMETHOD+' CLSLimits/BetaHalf'+cdir+'/confbetahalf_'+cdir+'_'+name[x]+'.cfg --rMax '+str(rmax)).readlines()
			if breaker ==True:
				break
			if 'r < 0.0000' not in str(EstimationInformation):
				effrmax = -999999
				for e in EstimationInformation:
					if 'r <'  in e and 'Expected' in e:
						thisrval = e.split('<')[-1]
						thisrval = thisrval.replace('\n','')
						thisrval = float(thisrval)
						if thisrval>effrmax:
							effrmax = thisrval
				rmax = effrmax*15.0
				EstimationInformation = [' r < 0.0000']
				breaker = True
			rmax = rmax/5.0
		## Estimation Complete
		
		expectedlines = []
		for line in EstimationInformation:
			if 'Expected' in line and 'r <' in line:
				expectedlines.append(line.replace('\n',''))
		values = []
		for e in expectedlines:
			print e
			values.append(float(e.split()[-1]))

		## Fill the arrays of Asymptotic Values
		for line in EstimationInformation:
			if 'Observed' in line and '<' in line:
				BetaHalfObs.append((line.split('<')[-1]).replace('\n',''))
			if 'Expected' in line and '<' in line:
				if '2.5%' in line:
					BetaHalf95down.append((line.split('<')[-1]).replace('\n',''))
				if '16.0%' in line:
					BetaHalf68down.append((line.split('<')[-1]).replace('\n',''))
				if '50.0%' in line:
					BetaHalfExp.append((line.split('<')[-1]).replace('\n',''))
				if '84.0%' in line:
					BetaHalf68up.append((line.split('<')[-1]).replace('\n',''))
				if '97.5%' in line:
					BetaHalf95up.append((line.split('<')[-1]).replace('\n',''))
		
		vstart = round((min(values)/3),5)
		vstop = round((max(values)*3),5)
		rvalues = []
		interval = abs(vstop-vstart)/100.0
		
		nindex = 0
		thisr = 0
		while thisr<vstop:
			thisr = vstart*1.1**(float(nindex))
			rvalues.append(thisr)
			nindex += 1
		strRvalues = []
		for r in rvalues:
			strRvalues.append(str(round(r,5)))
		print strRvalues
		
		for r in strRvalues:
			command = 'combine '+METHOD.replace('SINGLEPOINT',r).replace('CONFIGURATION','confbetahalf_'+cdir+'_'+name[x]+'.cfg')
			strR = r.replace('.','_')
			os.system('cat ShellScriptsForBatch/subbetahalf_'+cdir+name[x]+'.csh | sed  \'s/SUBCOMMAND/'+command+'/g\'  > ShellScriptsForBatch/subbetahalf_'+strR+'_'+cdir+name[x]+'.csh')
			os.system('chmod 777 ShellScriptsForBatch/subbetahalf_'+strR+'_'+cdir+name[x]+'.csh')

			for nn in range(numdo):
				if (dobatch):
					os.system('bsub -o /dev/null -e /dev/null -q '+queue+' -J jobbetahalf'+str(nn)+'_R_'+strR+'_'+name[x]+' < ShellScriptsForBatch/subbetahalf_'+strR+'_'+cdir+name[x]+'.csh')
os.system('rm higgsCombineTest*root')

print '\n\n\n'

#### ASYMPTOTIC CLS PRINTOUT ###


mTh = [ 150, 200, 250, 300, 350, 400,450,500,550,600,650,700,750,800,850]
xsTh = [  53.3, 11.9, 3.47, 1.21, 0.477, .205,.0949,.0463,.0236,.0124,.00676,.00377,.00215,.00124,.000732]


#### BETA ONE CHANNEL
if do_BetaOne == 1:

	print "*"*40 + '\n BETA ONE ASYMPTOTIC CLS RESULTS\n\n' +"*"*40
	
	band1sigma = 'Double_t y_1sigma[20]={'
	band2sigma = 'Double_t y_2sigma[20]={'
	excurve = 'Double_t xsUp_expected[10] = {' 
	obcurve = 'Double_t xsUp_observed[10] = {'  
	
	ob = BetaOneObs 
	down2 = BetaOne95down 
	up2 = BetaOne95up 
	down1 = BetaOne68down 
	up1 = BetaOne68up 
	med = BetaOneExp 
	
	fac = 1.0
	sigma = []
	for x in range(len(mTh)):
		if (mTh[x]) in masses: 
			sigma.append(xsTh[x]*fac)
	
	for x in range(len(masses)):
		excurve += str(float(med[x])*float(sigma[x])) + ' , ' 
		obcurve += str(float(ob[x])*float(sigma[x])) + ' , ' 
		band1sigma += str(float(down1[x])*float(sigma[x])) + ' , ' 
		band2sigma += str(float(down2[x])*float(sigma[x])) + ' , ' 
	
	for x in range(len(masses)):
		band1sigma += str(float(up1[-(x+1)])*float(sigma[-(x+1)])) + ' , ' 
		band2sigma += str(float(up2[-(x+1)])*float(sigma[-(x+1)])) + ' , ' 
	excurve += '}'
	obcurve += '}'
	band1sigma += '}'
	band2sigma += '}'
	excurve = excurve.replace(' , }',' }; ' )
	obcurve = obcurve.replace(' , }',' }; ' )
	band1sigma = band1sigma.replace(' , }',' }; ' )
	band2sigma = band2sigma.replace(' , }',' }; ' )
	
	print '\n'
	print excurve
	print '\n'
	print obcurve
	print '\n'
	print band1sigma
	print '\n'
	print band2sigma
	print '\n'
	print '\n'


#### BETA HALF CHANNEL
if do_BetaHalf == 1:

	print "*"*40 + '\n BETA HALF ASYMPTOTIC CLS RESULTS\n\n' +"*"*40
	
	band1sigma = 'Double_t y_1sigma[20]={'
	band2sigma = 'Double_t y_2sigma[20]={'
	excurve = 'Double_t xsUp_expected[10] = {' 
	obcurve = 'Double_t xsUp_observed[10] = {'  
	
	ob = BetaHalfObs 
	down2 = BetaHalf95down 
	up2 = BetaHalf95up 
	down1 = BetaHalf68down 
	up1 = BetaHalf68up 
	med = BetaHalfExp 
	
	fac = 0.5
	sigma = []
	for x in range(len(mTh)):
		if (mTh[x]) in masses: 
			sigma.append(xsTh[x]*fac)
	
	for x in range(len(masses)):
		excurve += str(float(med[x])*float(sigma[x])) + ' , ' 
		obcurve += str(float(ob[x])*float(sigma[x])) + ' , ' 
		band1sigma += str(float(down1[x])*float(sigma[x])) + ' , ' 
		band2sigma += str(float(down2[x])*float(sigma[x])) + ' , ' 
	
	for x in range(len(masses)):
		band1sigma += str(float(up1[-(x+1)])*float(sigma[-(x+1)])) + ' , ' 
		band2sigma += str(float(up2[-(x+1)])*float(sigma[-(x+1)])) + ' , ' 
	excurve += '}'
	obcurve += '}'
	band1sigma += '}'
	band2sigma += '}'
	excurve = excurve.replace(' , }',' }; ' )
	obcurve = obcurve.replace(' , }',' }; ' )
	band1sigma = band1sigma.replace(' , }',' }; ' )
	band2sigma = band2sigma.replace(' , }',' }; ' )
	
	print '\n'
	print excurve
	print '\n'
	print obcurve
	print '\n'
	print band1sigma
	print '\n'
	print band2sigma
	print '\n'
	print '\n'