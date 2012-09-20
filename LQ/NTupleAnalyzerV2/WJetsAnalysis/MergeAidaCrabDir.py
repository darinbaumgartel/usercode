
import sys
import os

crabdir = sys.argv[1]

aidas = [(crabdir + '/res/'+x.replace('\n','')).replace('//','/') for x in os.popen('ls -1 '+crabdir+'/res | grep ".aida"').readlines()]

aidaout = crabdir.replace('/','')+'.aida'

if aidaout in str(os.listdir('.')):
	os.system('rm '+aidaout)
	print 'Removing old aida file'

aidamerge = './aidamerge -o '+aidaout

for x in aidas:
	aidamerge += ' '+x


f = open('tempmerge.sh','w')
f.write('#!/bin/sh\n\ncd /afs/cern.ch/cms/slc5_amd64_gcc434/cms/cmssw/CMSSW_4_2_5/src\neval `scramv1 runtime -sh`\ncd -\n\nsource setupRivetProf.sh\n\n'+aidamerge+'\n\nrivet-mkhtml '+aidaout+'\n\n')
f.close()
#sys.exit()
os.system('chmod 777 tempmerge.sh')
os.system('./tempmerge.sh')
os.system('rm tempmerge.sh')
