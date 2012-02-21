import os
import sys
import subprocess
import matplotlib.pyplot
import math 

import random
 #betas = [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.11,0.12,0.13,0.14,0.15,0.16,0.17,0.18,0.19,0.2,0.21,0.22,0.23,0.24,0.25,0.26,0.27,0.28,0.29,0.3,0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.65,0.66,0.67,0.68,0.69,0.7,0.71,0.72,0.73,0.74,0.75,0.76,0.77,0.78,0.79,0.8,0.81,0.82,0.83,0.84,0.85,0.86,0.87,0.88,0.89,0.9,0.91,0.92,0.93,0.94,0.95,0.96,0.97,0.98,0.99,0.99999]
betas = [.3,0.5]
 
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
if 'do_Combo' in str(sys.argv):
	do_combo = 1
if 'just_observed' in str(sys.argv):
	do_observedonly = 1	
numdo = 1	
queue = '1nd'
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
		os.system('rfmkdir /castor/cern.ch/user/'+person[0]+'/'+person+'/CLSLimits/Combo'+cdir)

		os.system('mkdir CLSLimits/BetaOne'+cdir)
		os.system('mkdir CLSLimits/BetaHalf'+cdir)
		os.system('mkdir CLSLimits/Combo'+cdir)

	if sys.argv[x] == '-n':
		numdo = int(sys.argv[x+1])
	if sys.argv[x] == '-q':
		queue = str(sys.argv[x+1])

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
			thisr = vstart*1.05**(float(nindex))
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
			thisr = vstart*1.05**(float(nindex))
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
					

################################################################################################################
################################################################################################################

if do_combo == 1:
	digits = '0123456789'

	cards = []
	cardmasses = []
	cardcontent = []
	card = ''

	flog = open('FinalCards.txt','r')
	os.system('rm -r TMPComboCards/; mkdir TMPComboCards')	
	for line in flog:
		if '.txt' not in line:
			card += line
		if '.txt' in line:
			cardcontent.append(card)
	
			card  = ''
			
			line = line.replace('.txt\n','')
			cards.append(line)
			m = ''
			for x in line:
				if x in digits:
					m+=(x)
			cardmasses.append(m)
			
	cardcontent.append(card)
	
	cardcontent = cardcontent[1:]
	combocards = []
	for x in cardcontent:
		for y in cards:
			if y in x:
				fout = open('combocard_'+y+'.cfg','w')
				x = x.replace('stat_','stat_'+y)
				fout.write(x)
				fout.close()
				combocards.append('combocard_'+y+'.cfg')
	uniquecardmasses = []
	for x in cardmasses:
		if x not in uniquecardmasses:
			uniquecardmasses.append(x)
	for m in uniquecardmasses:
		pair = []
		for x in combocards:
			if m in x:
				pair.append(x)
		os.system('combineCards.py '+pair[0]+ ' '+pair[1]+ '  > TMPComboCards/combocard_COMBO_M_'+m+'.cfg ' )
		print pair
	for m in uniquecardmasses:
		combocards.append('TMPComboCards/combocard_COMBO_M_'+m+'.cfg')

	betaind = -1

	for beta in betas:
		betaind += 1
		ComboObs.append([])
		Combo95down.append([])
		Combo68down.append([])
		ComboExp.append([])
		Combo68up.append([])
		Combo95up.append([])
						
								
		betaval = str(beta).replace('.','_')
		os.system('mkdir CLSLimits/Combo'+cdir+'/Combo_beta_'+betaval)
		os.system('rfmkdir /castor/cern.ch/user/'+person[0]+'/'+person+'/CLSLimits/Combo'+cdir+'/Combo_beta_'+betaval)


		for x in range(len(uniquecardmasses)):	
			print 'Calculating limit for combination mass: ' + str(uniquecardmasses[x]) + ' , beta = '+str(beta)			
			newcard = ('CLSLimits/Combo'+cdir+'/combocard_COMBO_M_'+uniquecardmasses[x]+'.cfg').replace('COMBO','beta_'+betaval+'_COMBO')
			newcastorcard = ( '/castor/cern.ch/user/'+person[0]+'/'+person+'/CLSLimits/Combo'+cdir+'/combocard_COMBO_M_'+uniquecardmasses[x]+'.cfg').replace('COMBO','beta_'+betaval+'_COMBO')

			
			ftmp = open(newcard,'w')
			fnorm = open('TMPComboCards/combocard_COMBO_M_'+str(uniquecardmasses[x])+'.cfg','r')
			
			betahalfplace = 99
			betaoneplace = 99
			for line in fnorm:

				if ('LQ' in line and 'process' in line):
					linesplit = line.split()
					for place in range(len(linesplit)):
						if 'LQ' in linesplit[place] and 'BetaHalf' in linesplit[place]:
							betahalfplace = place
						if 'LQ' in linesplit[place] and 'BetaHalf' not in linesplit[place]:
							betaoneplace = place
							
				if ( 'rate' in line):

					linesplit = line.split()
					linesplit2 = []
					for place in range(len(linesplit)):
						arg = linesplit[place]
						if betahalfplace == place:
							arg = str(float(arg)*beta*(1.0-beta)*4.0)
						
						if betaoneplace == place:						
							arg = str(float(arg)*beta*beta)
						linesplit2.append(arg)
					line2 = ''
					for xpart in linesplit2:
						line2 += xpart + '    '
					line2 += '\n'
					line = line2
				if  'stat' in line and 'sig' in line and 'gmN' in line:
					linesplit = line.split()
					for nsp in range(len(linesplit)):
						if 'BetaHalf' not in line and nsp == betaoneplace+1:
							repsold =  str(linesplit[nsp+1])
							repsnew = str(float(repsold)*beta*beta)
							line = line.replace(repsold,repsnew)
						if 'BetaHalf' in line and nsp == betahalfplace+1:
							repsold =  str(linesplit[nsp+1])
							repsnew = str(float(repsold)*beta*(1.0-beta)*4.0)
							line = line.replace(repsold,repsnew)
				ftmp.write(line)
			ftmp.close()
	
			os.system('rfcp '+newcard+' '+newcastorcard)
		
			thisname ='beta_'+ betaval + '_M_'+str(uniquecardmasses[x])
			mdir = (os.popen('pwd').readlines())[0]
			mdir = mdir.replace('\n','')
			fsub = open('ShellScriptsForBatch/subcombo_'+cdir+thisname+'.csh','w')
			fsub.write('#!/bin/csh'+ cr)
			fsub.write('cd ' + mdir+ cr)
			fsub.write('eval `scramv1 runtime -csh`'+ cr)
			fsub.write('cd -'+ cr)
			fsub.write('cp '+mdir+'/'+newcard+' .'+ cr)
			fsub.write('SUBCOMMAND'+'\n')
			if '--castor_only' not in sys.argv:
				fsub.write('cp *root '+mdir+'/CLSLimits/Combo'+cdir+'/Combo_beta_'+betaval+'/ ' )					
			fsub.write('mv *root Combo_'+thisname+'_R_RVALUE_ind_`bash -c \'echo $RANDOM\'`.root \n')			
			fsub.write('rfcp *root /castor/cern.ch/user/'+person[0]+'/'+person+'/CLSLimits/Combo'+cdir+'/Combo_beta_'+betaval+'/' +cr +cr )			

			fsub.close()
			
			## Estimate the r values with Asymptotic CLs
			EstimationInformation = [' r < 0.0000']
			rmax = 1000.0
			breaker = False 
			while 'r < 0.0000' in str(EstimationInformation):
				#print 'combine '+ESTIMATIONMETHOD+' '+newcard +'--rMax '+str(rmax)
				EstimationInformation = os.popen('combine '+ESTIMATIONMETHOD+' '+newcard +' --rMax '+str(rmax)).readlines()
				
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
					ComboObs[betaind].append((line.split('<')[-1]).replace('\n',''))
				if 'Expected' in line and '<' in line:
					if '2.5%' in line:
						Combo95down[betaind].append((line.split('<')[-1]).replace('\n',''))
					if '16.0%' in line:
						Combo68down[betaind].append((line.split('<')[-1]).replace('\n',''))
					if '50.0%' in line:
						ComboExp[betaind].append((line.split('<')[-1]).replace('\n',''))
					if '84.0%' in line:
						Combo68up[betaind].append((line.split('<')[-1]).replace('\n',''))
					if '97.5%' in line:
						Combo95up[betaind].append((line.split('<')[-1]).replace('\n',''))
			
			vstart = round((min(values)/2),5)
			vstop = round((max(values)*2),5)
			rvalues = []
			interval = abs(vstop-vstart)/100.0
			
			nindex = 0
			thisr = 0
			
			expinc = 0.9999*(2.718281828**((0.0666666666667*(math.log(vstop/vstart)))))
			while thisr<vstop:
				thisr = vstart*expinc**(float(nindex))
				rvalues.append(thisr)
				nindex += 1
			strRvalues = []
			for r in rvalues:
				strRvalues.append(str(round(r,5)))
			print strRvalues
			
			for r in strRvalues:
				command = 'combine '+METHOD.replace('SINGLEPOINT',r).replace('CONFIGURATION',newcard.split('/')[-1])
				strR = r.replace('.','_')
				os.system('cat ShellScriptsForBatch/subcombo_'+cdir+thisname+'.csh | sed  \'s/SUBCOMMAND/'+command+'/g\' | sed  \'s/RVALUE/'+strR+'/g\' > ShellScriptsForBatch/subcombo_R_'+strR+'_'+cdir+thisname+'.csh')
				os.system('chmod 777 ShellScriptsForBatch/subcombo_R_'+strR+'_'+cdir+thisname+'.csh')
	
				for nn in range(numdo):
					if (dobatch):
						os.system('bsub -o /dev/null -e /dev/null -q '+queue+' -J jobcombo'+str(nn)+'_R_'+strR+'_'+thisname+' < ShellScriptsForBatch/subcombo_R_'+strR+'_'+cdir+thisname+'.csh')
	


################################################################################################################
################################################################################################################






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
	
	
	


ComboObs =[[' 0.2097', ' 0.1796', ' 0.2490', ' 0.4723', ' 0.6617', ' 0.9450', ' 1.3528', ' 2.0420', ' 4.9287', ' 12.1046'], [' 0.0739', ' 0.0623', ' 0.1058', ' 0.1897', ' 0.3089', ' 0.4262', ' 0.7052', ' 1.1312', ' 2.5923', ' 5.5280']]

Combo95down=[[' 0.1164', ' 0.1418', ' 0.1872', ' 0.2700', ' 0.3671', ' 0.5050', ' 0.6485', ' 0.9686', ' 2.1676', ' 5.4799'], [' 0.0423', ' 0.0643', ' 0.0884', ' 0.1348', ' 0.1887', ' 0.2722', ' 0.3917', ' 0.5879', ' 1.2841', ' 3.1920']]

Combo68down=[[' 0.1548', ' 0.1886', ' 0.2490', ' 0.3591', ' 0.4882', ' 0.6717', ' 0.8626', ' 1.2885', ' 2.8832', ' 7.2891'], [' 0.0562', ' 0.0855', ' 0.1176', ' 0.1792', ' 0.2510', ' 0.3621', ' 0.5210', ' 0.7819', ' 1.7080', ' 4.2458']]

ComboExp=[[' 0.2145', ' 0.2613', ' 0.3450', ' 0.4976', ' 0.6765', ' 0.9308', ' 1.1953', ' 1.7854', ' 3.9951', ' 10.1002'], [' 0.0779', ' 0.1184', ' 0.1629', ' 0.2484', ' 0.3478', ' 0.5017', ' 0.7220', ' 1.0835', ' 2.3668', ' 5.8833']]

Combo68up=[[' 0.2979', ' 0.3629', ' 0.4792', ' 0.6912', ' 0.9397', ' 1.2928', ' 1.6603', ' 2.4799', ' 5.5493', ' 14.0292'], [' 0.1082', ' 0.1645', ' 0.2263', ' 0.3450', ' 0.4831', ' 0.6969', ' 1.0029', ' 1.5050', ' 3.2874', ' 8.1718']]

Combo95up=[[' 0.3958', ' 0.4822', ' 0.6367', ' 0.9183', ' 1.2485', ' 1.7177', ' 2.2059', ' 3.2948', ' 7.3729', ' 18.6397'], [' 0.1438', ' 0.2186', ' 0.3007', ' 0.4584', ' 0.6418', ' 0.9259', ' 1.3324', ' 1.9996', ' 4.3678', ' 10.8574']]

#### COMBINATION CHANNEL
if do_combo == 0:

	print "*"*40 + '\n COMBINATIONASYMPTOTIC CLS RESULTS\n\n' +"*"*40

					
	mTh = [ 150, 200, 250, 300, 350, 400,450,500,550,600,650,700,750,800,850]
	xsTh = [  53.3, 11.9, 3.47, 1.21, 0.477, .205,.0949,.0463,.0236,.0124,.00676,.00377,.00215,.00124,.000732]
	sigma = []
	fac = 1.0
	for x in range(len(mTh)):
		if (mTh[x]) in masses: 
			sigma.append(xsTh[x]*fac)
	
	def re_eval(rlist):
		outlist = []
		for mset in rlist:
			newset = []
			for r_ind in range(len(mset)):
				newset.append(sigma[r_ind]*float(mset[r_ind]))		
			outlist.append(newset)
		return outlist
	
	s_ComboObs = re_eval(ComboObs)
	s_Combo95down = re_eval(Combo95down)
	s_Combo68down = re_eval(Combo68down)
	s_ComboExp = re_eval(ComboExp)
	s_Combo68up = re_eval(Combo68up)
	s_Combo95up = re_eval(Combo95up)
	

	from ROOT import *
	from array import array
		
	mTh = array("d",[ 150, 200, 250, 300, 350, 400,450,500,550,600,650,700,750,800,850])
	xsTh = array("d",[  53.3, 11.9, 3.47, 1.21, 0.477, .205,.0949,.0463,.0236,.0124,.00676,.00377,.00215,.00124,.000732])
	
	g = TGraph(len(mTh),mTh,xsTh);
	spline = TSpline3("xsection",g) 
	#xx = (spline.Eval(310));
	M_th=[ 150, 200, 250, 300, 350, 400,450,500,550,600,650,700,750,800,850]
	X_th=[  53.3, 11.9, 3.47, 1.21, 0.477, .205,.0949,.0463,.0236,.0124,.00676,.00377,.00215,.00124,.000732]
		
		
	def sigmaval(mval):
		return spline.Eval(mval)
		
	
	def mval(sigma):
		testm = 150
		oldtestm = 800
		inc = 50
		dif = 55
		olddif = 000
		while abs(oldtestm - testm)>0.01:
			testsigma = sigmaval(testm)
			olddif = dif
			dif = testsigma -sigma
			if testm>1000:
				break
			if dif*olddif <= 0.0:
				inc = -inc/2.3
			oldtestm = testm
			#print '**' + str(testm) + '  ' + str(testsigma) +'  ' +str(dif) + '   ' + str(dif*olddif)
	
			testm = testm + inc
		return testm
	import math
	inputarrayX = []
	inputarrayY = []
	def logspline(inputarrayX,inputarrayY):
		logarray = []
		for x in inputarrayY:
			logarray.append(math.log(x))
		x = array("d",inputarrayX)
		y = array("d",logarray)
		g = TGraph(len(x),x,y)
		outspline = TSpline3("",g)
		return outspline
	logtheory = logspline(M_th,X_th)
	
	from math import exp
	def get_intersection(spline1, spline2, xmin,xmax):
		num = xmax-xmin
		inc = (xmax - xmin)/num
		dif = []
		sdif = []
		x = xmin
		xvals = []
		xx = []
		yy = []
		xvals = []
		while x<xmax:
			thisdif = (exp(spline1.Eval(x)) - exp(spline2.Eval(x)))
			#print (str(x)) + '   ' + str(thisdif)
			xx.append(exp(spline1.Eval(x)))
			yy.append(exp(spline2.Eval(x)))
			sdif.append(thisdif)
			dif.append(abs(thisdif))
			xvals.append(x)
			#print  str(x) + '   ' +str(exp(spline1.Eval(x))) + '    '+str(exp(spline2.Eval(x))) + '    ' + str(thisdif)
			x = x+inc
		mindif = min(dif)
		bestmass = 0	
		
	
		for x in range(len(dif)-2):
			a = sdif[x]
			b = sdif[x+1]	
			#print str(xvals[x+1]) +'    '+str(a)  + '     ' +str(b) 
			if ((a/abs(a))*(b/abs(b))) < 0.0 and a >0.0 :
				#print 'Limit found at: '+ (str(xvals[x]))
				bestmass = xvals[x]
				break;
						
		return [bestmass,mindif]
		
	


	def fill_mlists(clist):
		mlist = []
		for limit_set in clist:
			fitted_limits = logspline(masses,limit_set)
			goodm = get_intersection(logtheory,fitted_limits,250,850)
			mlist.append(goodm[0])
		return mlist
		
	m_ComboObs = fill_mlists(s_ComboObs)
	m_Combo95down = fill_mlists(s_Combo95down)
	m_Combo68down = fill_mlists(s_Combo68down)
	m_ComboExp = fill_mlists(s_ComboExp)
	m_Combo68up = fill_mlists(s_Combo68up)
	m_Combo95up = fill_mlists(s_Combo95up)
	
	betav = []
	for x in betas:
		betav.append(str(round(x,4)))
	betastring = 'Double_t beta_vals['+str(len(betas))+'] = {' +str(betav).replace('[','').replace(']','').replace('\'','')+'};'

	band1sigma = 'Double_t m_1sigma['+str(2*len(betas))+']={'
	band2sigma = 'Double_t m_2sigma['+str(2*len(betas))+']={'
	excurve = 'Double_t m_expected['+str(len(betas))+'] = {' 
	obcurve = 'Double_t m_observed['+str(len(betas))+'] = {'  
	
	excurve += str(m_ComboExp).replace('[','').replace(']','')+'};'
	obcurve += str(m_ComboObs).replace('[','').replace(']','')+'};'
	m_Combo68up.reverse()
	m_Combo95up.reverse()
	band1sigma += str(m_Combo68down).replace('[','').replace(']','') + ', '+  str(m_Combo68up).replace('[','').replace(']','')+'};'
	band2sigma += str(m_Combo95down).replace('[','').replace(']','') + ', '+ str(m_Combo95up).replace('[','').replace(']','')+'};'
	print '\n'
	print betastring
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