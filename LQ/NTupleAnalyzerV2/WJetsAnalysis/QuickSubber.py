import os
import sys

TAGGERS = ['TCHEM','TCHEMBGSF','TCHEMNORECOIL']

#TAGGERS = ['TCHPT','TCHEM','SSVHPT','JPT','TCHEL','TCHPTUnCorr']



for TAGGER in TAGGERS:
	dosf = False
	norecoil=False
	if 'BGSF' in TAGGER:
		TAGGER = TAGGER.replace('BGSF','')
		dosf = True
	if 'NORECOIL' in TAGGER:
		TAGGER = TAGGER.replace('NORECOIL','')
		norecoil = True
	_TAGGER = str(TAGGER)
	sfadd = ""+dosf*("BGSFOn")+norecoil*("NoRecoil")
	TAGGER+=sfadd
	os.system('rm WJetsTreeAnalyzer'+TAGGER+'.py')
	os.system('cat WJetsTreeAnalyzer.py  | sed \'s/TCHEM/'+_TAGGER+'/g\' | sed \'s/pyplots/pyplots'+TAGGER+'/g\' | sed \'s/MT_muon1METR/MT_muon1MET'+('R')*(norecoil==False)+'/g\'  > WJetsTreeAnalyzer'+TAGGER+'.py ')
	os.system('rm -r pyplots'+TAGGER)
	os.system('mkdir pyplots'+TAGGER)

	record = False
	lines = []
	for line in open('WJetsTreeAnalyzer'+TAGGER+'.py','r'):
		if 'def' in line and "main()" in line:
			record=True
		if '###########' in line:
			record=False
		if record==True and 'FullAnalysisWithUncertainty' in line and '#Full' not in line and "(" in line:
			lines.append(line)

	os.system('rm SubTemp'+TAGGER+'_*py SubTemp'+TAGGER+'_*csh')
	n=0
	for keeper in lines:
		f=open('SubTemp'+TAGGER+'_'+str(n)+'.py','w')
		for line in open('WJetsTreeAnalyzer'+TAGGER+'.py','r'):
			line = line.replace('tmp.root','tmp'+TAGGER+'_'+str(n)+'.root')
			if line ==keeper or line not in lines:
				f.write(line)
		f.close() 
		n += 1

	fsub = open('SubTemp'+TAGGER+'_All.csh','w')
	fsub.write('#!/bin/csh\n\n')

	for x in range(n):
		fsub.write('bsub -q 2nd  -R "pool>30000" -J SubTemp'+TAGGER+'_'+str(x)+'< SubTemp'+TAGGER+'_'+str(x)+'.tcsh\n\n')
		os.system('sed \'s/WJetsTreeAnalyzer.py/SubTemp'+TAGGER+'_'+str(x)+'.py/g\' RunWJetsBatch.tcsh > SubTemp'+TAGGER+'_'+str(x)+'.tcsh ')

	fsub.close()

	os.system('chmod 777 *sh')
	os.system('./SubTemp'+TAGGER+'_All.csh')










