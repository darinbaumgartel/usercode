
# Directory where you want the castor directory mirrored.
ndir = '/store/group/phys_smp/WPlusJets/BHSNtuples'

if ndir[-1] != '/':
	ndir += '/'

import os
import sys
import random
from time import sleep
import subprocess, datetime, os, time, signal


alldirs = [((x.replace('\n','')).replace('\t','')).replace(' ','') for x in open(sys.argv[1],'r')]


cdirs = []
for a in alldirs:
	if '#' not in a and len(a) > 3:
		cdirs.append(a)
print ' ----------------------------------------------------------------------- '


marker = ndir.split('/')[-2]
edirs = []
for c in cdirs:
	print c
	e = ndir + c.split(marker)[-1]
	e = e.replace('//','/')
	print e
	edirs.append(e)
	print ' '
print ' ----------------------------------------------------------------------- '

alldirs = []
for e in edirs:
	print e
	_e = e.replace(ndir,'')
	_r = _e.split('/')

	tdir = ndir
	for x in _r:
		tdir += '/'+x
		tdir = tdir.replace('//','/')

		alldirs.append(tdir)

print ' ----------------------------------------------------------------------- '

eosinfo = os.popen('cmsLs -R '+ndir+ ' | grep store ').readlines()
stre = str(eosinfo)

for a in alldirs:
	if a not in stre:
		print 'cmsMkdir '+a
		os.system( 'cmsMkdir '+a )
		os.system('sleep 1')

print ' ----------------------------------------------------------------------- '



castorfiles = []
castorinfo = []
for c in cdirs:
	print 'Analyzing',c
	castorfiles += [c+'/'+x.replace('\n','') for x in os.popen('nsls '+c+'| grep root').readlines()]

	__castorinfo = [x.replace('\n','') for x in os.popen('nsls -l '+c+'| grep root').readlines()]

	__castorinfo2 = []

	for x in __castorinfo:
		x = x.split()
		x[-1] = c+'/'+x[-1]
		y = ''
		for aa in x:
			y += aa + '  '
		__castorinfo2.append(y)

	castorinfo += __castorinfo2


eosfiles = []
cpcommands = []



for c in castorfiles:
	# print c
	e = ndir + c.split(marker)[-1]
	e = e.replace('//','/')
	# print e
	eosfiles.append(e)
	cp = 'xrdcp "root://castorcms/'+c+'" root://eoscms//eos/cms'+e + ' '
	cpcommands.append(cp)

	# print ' '


print ' ----------------------------------------------------------------------- '


necessarycps = []
necessarycastorfiles = []

for n in range(len(castorfiles)):
	c = castorfiles[n]
	e = eosfiles[n]
	csize = '-1'
	esize = '-1'
	einf = ''
	cinf = ''
	for x in castorinfo:
		if c in x:
			csize = x.split()[4]
			cinf = x
	for x in eosinfo:
		if e in x:
			esize = x.split()[1]
			einf = x
	print ' ---------------------------- '
	print 'c:',c
	print 'c inf:',cinf
	print 'e:',e
	print 'e inf:',einf
	print n, csize,esize,csize == esize
	if csize != esize:
		necessarycps.append(cpcommands[n])
		necessarycastorfiles.append(c)


print ' ----------------------------------------------------------------------- '

for c in necessarycastorfiles:
	if '--stage' not in sys.argv:
		continue
	os.system('stager_get -M '+c)
	os.system('sleep 0.1')

print ' ----------------------------------------------------------------------- '

for nc in necessarycps:
	print nc

os.system('rm -r BatchJobs')
os.system('mkdir  BatchJobs')

def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

cpgroups = chunks(necessarycps,10)

subs = []

for xx in range(len(cpgroups)):
	f = open('BatchJobs/CP_'+str(xx)+'.tcsh','w')
	subs.append(['BatchJobs/CP_'+str(xx)+'.tcsh','eos_copy_job_'+str(xx)])
	f.write('#!/bin/tcsh\n\n')
	for cp in cpgroups[xx]:
		f.write(cp+'\n\n')
	f.close()

for s in subs:
	os.system('chmod 755 '+s[0])
	print 'bsub -q 1nh -J '+s[1] +' < '+s[0]


print 'Total Files: ',len(castorfiles)
print 'Files requiring copy:',len(necessarycastorfiles)
print ' '
if len(necessarycastorfiles) == 0:
	print "There are no files which require copying. Transfer is complete!"








sys.exit()
cfiles = []

eosinfo = str(os.popen('cmsLs '+ndir+ ' | grep store ').readlines())

eosverboseinfo = []

castorverboseinfo = []

for c in cdirs:
	n = ndir + '/'+c.split('/')[-1]
	if n not in eosinfo:
		print n
		print 'xrd eoscms mkdir  '+n
		#sys.exit()
		# os.system ( 'xrd eoscms mkdir  '+n)
		sleep(1)
	print 'scanning... cmsLs '+n
	sleep(.1)
	
	thisverbose = os.popen('cmsLs '+n).readlines()
	eosverboseinfo.append(thisverbose)
	castorverboseinfo.append(os.popen('nsls -l '+c).readlines())

sys.exit()

for c in cdirs:
	files = os.popen('nsls '+c).readlines()
	for f in files:
		cfiles.append(c + '/'+f.replace('\n',''))

castorfiles=[]
eosfiles = []
for x in eosverboseinfo:
	for y in x:
		if '.root' in y:
			info = [y.split()[1],y.split()[4]]
			eosfiles.append(info)

for x in castorverboseinfo:
	for y in x:
		if '.root' in y:
			info = [y.split()[1],y.split()[4]]
			castorfiles.append(info)

NCopy = 0

BatchCopy = ((((sys.argv[1]).split('/'))[-1]).split('.'))[0]

os.system('rm -r '+BatchCopy)

os.system('mkdir '+BatchCopy)

fstat = open(BatchCopy+'/CopyCommands.txt','w')
fstat.write("echo Starting\n")

NTotal = 0
NSub = 0
NStage = 0
NFinished = 0
for f in range(len(cfiles)):
	NTotal += 1
	print 'Checking file ', f+1,' of ',(len(cfiles)), 
	c = cfiles[f]
	lfile = c.split('/')
	n = ndir + '/'+lfile[-2]+'/'+lfile[-1]

	cp = 'xrdcp "root://castorcms/'+c+'" root://eoscms//eos/cms'+n + ' '

	is_present_on_eos = False
	has_correct_size_on_eos = False
	bytesize = -1

	for e in eosfiles:
		if n==e[-1]:
			is_present_on_eos = True
			bytesize = int(e[0])


	if is_present_on_eos:
		castorbytesize=int( (((os.popen('nsls -l '+c).readlines())[0]).split())[4])
		if castorbytesize == bytesize:
			print '...  Correct file with byte size: ', castorbytesize, '==' ,bytesize, '. '
			has_correct_size_on_eos = True
		else:
			print '... Incorrect file size. Removing. ', castorbytesize, '!=' ,bytesize, '. '
			print('xrd eoscms rm  /eos/cms'+n)
			os.system('xrd eoscms rm  /eos/cms'+n)


	has_good_copy = has_correct_size_on_eos*is_present_on_eos

	if has_good_copy:
		NFinished += 1
		continue

	sleep(.17)
	stageinfo = str(os.popen('stager_qry -M '+c).readlines())
	if 'STAGED' not in stageinfo:
		print 'Staging file and skipping for now... '
		if 'STAGEIN' not in stageinfo:
		#if True:
			sleep (.17)
			os.system('stager_get -M '+c)
		NStage += 1
		continue

	print '... writing copy statement to file.'
	fstat.write(cp+'\n')
	NSub += 1
	
fstat.close()

if (NTotal != NFinished and '--norun' not in sys.argv):
	fsub= open (BatchCopy+'/MasterSubber.tcsh','w')
	fsub.write('#!/bin/tcsh\n\n')
	n=0
	m=0
	for line in open(BatchCopy+'/CopyCommands.txt','r'):
		if n==0:
			m+=1
			print 'Making subber number ' , m
			f1 = open(''+BatchCopy+'/Subber_'+str(m)+'.tcsh','w')
			f1.write('#!/bin/tcsh\n\ncd /afs/cern.ch/user/d/darinb/scratch0/Analyzer_PostLP/CMSSW_4_2_8/src\neval `scramv1 runtime -csh`\ncd -\n\n')
			fsub.write('bsub -q 8nh -o /dev/null -e /dev/null -J JobNTupleMigration_'+str(m)+' < Subber_'+str(m)+'.tcsh\nsleep .5\n\n')
		f1.write(line)
		n+=1 
		if n==3:
			f1.close()
			n=0
	f1.close()
	fsub.close()
	os.system('chmod 777 '+BatchCopy+'/*')
	
	frun = open('run.tcsh','w')
	frun.write('#!/bin/tcsh\n\ncd '+BatchCopy+'\n./MasterSubber.tcsh\ncd - \n')
	frun.close()
	os.system('chmod 777 run.tcsh')
	os.system('./run.tcsh')



print '\n\n   FileCheck Summary: \n\n'
print 'File Count: ',NTotal 
print 'Files submitted for Copying: ',NSub 
print 'Files on hold for staging: ',NStage 
print 'Files already finished: ',NFinished 
print '\n\n'

if (NTotal == NFinished) and 'DONE' not in sys.argv[1]:
	print "Data migration is complete. Moving the input file to Done Status. \n\n         "+sys.argv[1] + '\n     --> '+ (sys.argv[1]).replace('.txt','_DONE.txt')+'\n\n'
	os.system('mv '+sys.argv[1]+' '+ (sys.argv[1]).replace('.txt','_DONE.txt') + ' ')
	
