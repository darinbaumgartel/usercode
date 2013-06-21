import os
import sys

os.system('rm WJetsTreeAnalyzerTCHPT.py')
os.system('rm WJetsTreeAnalyzerSSVHPT.py')
os.system('rm WJetsTreeAnalyzerJPT.py')


os.system('cat WJetsTreeAnalyzer.py | sed \'s/pyplots/pyplotsTCHPT/g\' > WJetsTreeAnalyzerTCHPT.py ')
os.system('cat WJetsTreeAnalyzerTCHPT.py | sed \'s/TCHPT/SSVHPT/g\' > WJetsTreeAnalyzerSSVHPT.py ')
os.system('cat WJetsTreeAnalyzerTCHPT.py | sed \'s/TCHPT/JPT/g\' > WJetsTreeAnalyzerJPT.py ')

os.system('rm -r pyplotsTCHPT')
os.system('rm -r pyplotsSSVHPT')
os.system('rm -r pyplotsJPT')
os.system('mkdir pyplotsTCHPT')
os.system('mkdir pyplotsSSVHPT')
os.system('mkdir pyplotsJPT')

record = False
lines = []
for line in open('WJetsTreeAnalyzerTCHPT.py','r'):
	if 'def' in line and "main()" in line:
		record=True
	if '###########' in line:
		record=False
	if record==True and 'FullAnalysisWithUncertainty' in line and '#Full' not in line and "(" in line:
		lines.append(line)

os.system('rm SubTempTCHPT_*py SubTempTCHPT_*csh')
n=0
for keeper in lines:
	f=open('SubTempTCHPT_'+str(n)+'.py','w')
	for line in open('WJetsTreeAnalyzerTCHPT.py','r'):
		line = line.replace('tmp.root','tmpTCHPT_'+str(n)+'.root')
		if line ==keeper or line not in lines:
			f.write(line)
	f.close() 
	n += 1

fsub = open('SubTempTCHPT_All.csh','w')
fsub.write('#!/bin/csh\n\n')

for x in range(n):
	fsub.write('bsub -q 2nd  -R "pool>30000" -J SubTempTCHPT_'+str(x)+'< SubTempTCHPT_'+str(x)+'.tcsh\n\n')
	os.system('sed \'s/WJetsTreeAnalyzer.py/SubTempTCHPT_'+str(x)+'.py/g\' RunWJetsBatch.tcsh > SubTempTCHPT_'+str(x)+'.tcsh ')

fsub.close()

os.system('chmod 777 *sh')
os.system('./SubTempTCHPT_All.csh')



record = False
lines = []
for line in open('WJetsTreeAnalyzerSSVHPT.py','r'):
	if 'def' in line and "main()" in line:
		record=True
	if '###########' in line:
		record=False
	if record==True and 'FullAnalysisWithUncertainty' in line and '#Full' not in line and "(" in line:
		lines.append(line)

os.system('rm SubTempSSVHPT_*py SubTempSSVHPT_*csh')
n=0
for keeper in lines:
	f=open('SubTempSSVHPT_'+str(n)+'.py','w')
	for line in open('WJetsTreeAnalyzerSSVHPT.py','r'):
		line = line.replace('tmp.root','tmpSSVHPT_'+str(n)+'.root')
		if line ==keeper or line not in lines:
			f.write(line)
	f.close() 
	n += 1

fsub = open('SubTempSSVHPT_All.csh','w')
fsub.write('#!/bin/csh\n\n')

for x in range(n):
	fsub.write('bsub -q 2nd -J SubTempSSVHPT_'+str(x)+'< SubTempSSVHPT_'+str(x)+'.tcsh\n\n')
	os.system('sed \'s/WJetsTreeAnalyzer.py/SubTempSSVHPT_'+str(x)+'.py/g\' RunWJetsBatch.tcsh > SubTempSSVHPT_'+str(x)+'.tcsh ')

fsub.close()

os.system('chmod 777 *sh')
os.system('./SubTempSSVHPT_All.csh')



record = False
lines = []
for line in open('WJetsTreeAnalyzerJPT.py','r'):
	if 'def' in line and "main()" in line:
		record=True
	if '###########' in line:
		record=False
	if record==True and 'FullAnalysisWithUncertainty' in line and '#Full' not in line and "(" in line:
		lines.append(line)

os.system('rm SubTempJPT_*py SubTempJPT_*csh')
n=0
for keeper in lines:
	f=open('SubTempJPT_'+str(n)+'.py','w')
	for line in open('WJetsTreeAnalyzerJPT.py','r'):
		line = line.replace('tmp.root','tmpJPT_'+str(n)+'.root')
		if line ==keeper or line not in lines:
			f.write(line)
	f.close() 
	n += 1

fsub = open('SubTempJPT_All.csh','w')
fsub.write('#!/bin/csh\n\n')

for x in range(n):
	fsub.write('bsub -q 2nd -J SubTempJPT_'+str(x)+'< SubTempJPT_'+str(x)+'.tcsh\n\n')
	os.system('sed \'s/WJetsTreeAnalyzer.py/SubTempJPT_'+str(x)+'.py/g\' RunWJetsBatch.tcsh > SubTempJPT_'+str(x)+'.tcsh ')

fsub.close()

os.system('chmod 777 *sh')
os.system('./SubTempJPT_All.csh')
