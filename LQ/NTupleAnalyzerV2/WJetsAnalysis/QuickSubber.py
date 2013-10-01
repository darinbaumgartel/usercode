import os
import sys

_indicator = ''
if len(sys.argv)>=1:
	_indicator = '_'+sys.argv[1]


thisdir = (os.popen('pwd').readlines()[0]).replace('\n','')
if thisdir[-1] !='/':
	thisdir+= '/'


# TAGGERS = ['TCHEM','TCHEMBINBYBIN','TCHEMBGSF','TCHEMWSFOFF','TCHEMNORECOIL','TCHPT','SSVHPT','TCHEL','JPT']

# TAGGERS = ['TCHEM','TCHEMV2','TCHEMV3','TCHEMNOJESTAG','TCHEMVARQCD','TCHEMBINBYBIN','TCHEMBGSF','TCHEMWSFOFF','TCHEMNORECOIL','TCHPT','SSVHPT','TCHEL','JPT']
#TAGGERS = ['TCHPT','TCHEM','SSVHPT','JPT','TCHEL','TCHPTUnCorr']
# TAGGERS = ['TCHEM','TCHEMBINBYBIN']
# TAGGERS=['TCHPT']
# TAGGERS = ['TCHEM']

TAGGERS = ['TCHEM','TCHEMBTAGOFF','TCHEMNOJESTAG','TCHEMNOJESTAGBTAGOFF','TCHEMVARQCD','TCHEMBINBYBIN','TCHEMBGSF','TCHPT','SSVHPT','TCHEL','JPT']

if False:
	for n in range(len(TAGGERS)):
		TAGGERS[n]+= 'NOSYS'

from time import strftime
now=str(strftime("%Y-%m-%d-%H:%M:%S"))
now = now.replace(" ","")
now = now.replace("\t","")
now = now.replace("-","_")
now = now.replace(":","_")


ResDir = 'Results'+'_'+now+_indicator+'/'
print ResDir


# sys.exit()

os.system('mkdir '+ResDir)
bashResDir = ResDir.replace('/','\/')

for TAGGER in TAGGERS:
	dosf = False
	norecoil=False
	wsfoff = False
	dobinbybin = False
	dov2 = False
	dov3 = False
	dobtagoff = False
	dovarqcd = False
	donojestag = False
	donosys = False
	if 'BGSF' in TAGGER:
		TAGGER = TAGGER.replace('BGSF','')
		dosf = True
	if 'WSFOFF' in TAGGER:
		TAGGER = TAGGER.replace('WSFOFF','')
		wsfoff = True
	if 'NORECOIL' in TAGGER:
		TAGGER = TAGGER.replace('NORECOIL','')
		norecoil = True
	if 'BINBYBIN' in TAGGER:
		TAGGER = TAGGER.replace('BINBYBIN','')
		dobinbybin = True
	if 'V2' in TAGGER:
		TAGGER = TAGGER.replace('V2','')
		dov2 = True
	if 'V3' in TAGGER:
		TAGGER = TAGGER.replace('V3','')
		dov3 = True		
	if 'BTAGOFF' in TAGGER:
		TAGGER=TAGGER.replace('BTAGOFF','')
		dobtagoff = True
	if 'VARQCD' in TAGGER:
		TAGGER=TAGGER.replace('VARQCD','')
		dobtagoff = True
	if 'NOJESTAG' in TAGGER:
		TAGGER=TAGGER.replace('NOJESTAG','')
		donojestag = True
	if 'NOSYS' in TAGGER:
		TAGGER=TAGGER.replace('NOSYS','')
		donosys = True

	_TAGGER = str(TAGGER)
	sfadd = ""+dosf*("BGSFOn")+norecoil*("NoRecoil")+wsfoff*("NoWScale")+dobinbybin*('BinByBin')+dov2*("V2")+dov3*("V3")+dobtagoff*("BTagOff")+dovarqcd*("VariableQCD")+donojestag*("NoJESTag")+donosys*("NoSys")
	TAGGER+=sfadd
	os.system('rm WJetsTreeAnalyzer'+TAGGER+'.py')

	os.system('cat WJetsTreeAnalyzer.py  | sed \'s/TCHEM/'+_TAGGER+'/g\' '+(dobtagoff)*' | sed \'s/PFJet30TCHEMCountCentral/0.0/g\''+' | sed \'s/pyplots/'+bashResDir+'pyplots'+TAGGER+'/g\' | sed \'s/MT_muon1METR/MT_muon1MET'+('R')*(norecoil==False)+'/g\'  > WJetsTreeAnalyzer'+TAGGER+'.py ')
	print ' ---------->  WJetsTreeAnalyzer'+TAGGER+'.py '
	# sys.exit()
	os.system('rm -r '+ResDir+'pyplots'+TAGGER)
	os.system('mkdir '+ResDir+'pyplots'+TAGGER)

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
	fsub.write('#!/bin/csh\n\ncd '+ResDir+'\n\n')

	q = '1nw'
	if donosys ==True:
		q = '8nh'

	for x in range(n):
		fsub.write('bsub -q '+q+'  -R "pool>60000" -J SubTemp'+TAGGER+'_'+str(x)+'< ../SubTemp'+TAGGER+'_'+str(x)+'.tcsh\n\n')
		os.system('cat RunWJetsBatch.tcsh | sed \'s#WJetsTreeAnalyzer.py#SubTemp'+TAGGER+'_'+str(x)+'.py#g\' | sed \'s#ResDir#'+ResDir+'#g\' | sed \'s#OutDir#'+ResDir+'pyplots'+TAGGER+'#g\' | sed \'s#AFSDir#'+thisdir+ResDir+'pyplots'+TAGGER+'#g\'  > SubTemp'+TAGGER+'_'+str(x)+'.tcsh ')
		# print('cat RunWJetsBatch.tcsh | sed \'s#WJetsTreeAnalyzer.py#SubTemp'+TAGGER+'_'+str(x)+'.py#g\' | sed \'s#ResDir#'+ResDir+'#g\' | sed \'s#OutDir#'+ResDir+'pyplots'+TAGGER+'#g\' | sed \'s#AFSDir#'+thisdir+ResDir+'pyplots'+TAGGER+'#g\'  > SubTemp'+TAGGER+'_'+str(x)+'.tcsh ')

	fsub.close()

	os.system('chmod 777 *sh')
	os.system('./SubTemp'+TAGGER+'_All.csh')
	os.system('./SubTemp'+TAGGER+'_All.csh')









