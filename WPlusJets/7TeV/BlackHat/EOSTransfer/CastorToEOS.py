
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
	# print ' ---------------------------- '
	# print 'c:',c
	# print 'c inf:',cinf
	# print 'e:',e
	# print 'e inf:',einf
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
	if '--submit' in sys.argv:
		os.system('bsub -q 1nh  -e /dev/null -J '+s[1] +' < '+s[0])

	print 'bsub -q 1nh -e /dev/null -J '+s[1] +' < '+s[0]


print 'Total Files: ',len(castorfiles)
print 'Files requiring copy:',len(necessarycastorfiles)
print ' '
if len(necessarycastorfiles) == 0:
	print "There are no files which require copying. Transfer is complete!"




