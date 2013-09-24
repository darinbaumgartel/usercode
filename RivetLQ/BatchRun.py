import os
import sys

files = []

dirs = ['/store/group/phys_exotica/leptonsPlusJets/leptoquarks/Pythia','/store/group/phys_exotica/leptonsPlusJets/leptoquarks/CalcHep']

dirs = ['/store/group/phys_exotica/leptonsPlusJets/leptoquarks/Pythia']


for d in dirs:
	files += [x.replace('\n','') for x in os.popen('cmsLs '+d+'  | awk \'{print $5}\'')]

runfiles = []
for f in files:
	if 'root' in f or 'lhe' in f and 'rivet' not in f:
		runfiles.append(f)

os.system('rm -r batch')

os.system('mkdir batch')

os.system('rm -r results')

os.system('mkdir results')


srcdir = (os.popen('pwd').readlines()[0].replace('\n','')).split('src')[0]+'src'
pwd = (os.popen('pwd').readlines()[0].replace('\n',''))

for f in runfiles:
	infile = f
	outfile = f.split('.')[0]+'_rivet.root'
	pyfile = 'batch/'+f.split('/')[-1].split('.')[0]+'_sub.py'

	# rf = open(pyfile)
	print '* ',infile
	print '* ',outfile
	print '* ',pyfile
	print ' '

	sf = open(pyfile,'w')
	rf = open('Rivet_LQ_TEST_FromCentralGen.py','r')
	for line in rf:
		if 'PoolSource' in line:
			if 'lhe' in infile:
				line = line.replace('Pool','LHE')
		if 'fileNames' in line:
		 	line = line.replace('SourceFile',infile.split('/')[-1])
		sf.write(line)
	sf.close()
	rf.close()

	batchfile = 'batch/'+f.split('/')[-1].split('.')[0]+'_batch.tcsh'

	b = open(batchfile,'w')
	b.write('#!/bin/tcsh\n\ncd '+srcdir+'\ncmsenv\ncd -\n')
	b.write('cp '+pwd+'/'+pyfile+' . \ncmsStage '+infile+ ' '+infile.split('/')[-1]+' \n')
	if 'lhe' in infile:
		b.write('sed -i \'s/LQ_P&B_2nd_gen/LQ/g\' '+infile.split('/')[-1]+'\n\n')
	b.write('cmsRun '+pyfile.split('/')[-1]+'\nmv rivetTree.root '+outfile.split('/')[-1]+'\ncmsStageOut '+outfile.split('/')[-1]+' '+outfile+'\n\n')
	b.close()

	com = ('bsub -R "pool>40000" -q 2nd -e /dev/null -J Job'+outfile+' < '+batchfile)
	print com
	if '--do' in sys.argv:
		os.system(com)