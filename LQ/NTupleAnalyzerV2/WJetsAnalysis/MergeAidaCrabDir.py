
import sys
import os

crabdir = sys.argv[1]

rename =''
if (len(sys.argv)>1):
	rename = sys.argv[2]



aidas = [(crabdir + '/res/'+x.replace('\n','')).replace('//','/') for x in os.popen('ls -1 '+crabdir+'/res | grep ".aida"').readlines()]

roots = [(crabdir + '/res/'+x.replace('\n','')).replace('//','/') for x in os.popen('ls -1 '+crabdir+'/res | grep ".root"').readlines()]


aidaout = crabdir.replace('/','')+'.aida'

rootout = crabdir.replace('/','')+'.root'

if (rename!=''):
	os.system('mv '+aidaout+ ' '+rename+'.aida')
	os.system('mv '+rootout+ ' '+rename+'.root')

	aidaout = rename+'.aida'
	rootout = rename+'_tree.root'


if aidaout in str(os.listdir('.')):
	os.system('rm '+aidaout)
	print 'Removing old aida file'

if rootout in str(os.listdir('.')):
	os.system('rm '+rootout)
	print 'Removing old root file'

aidamerge = './aidamerge -o '+aidaout

rootmerge = 'hadd '+rootout


for x in aidas:
	aidamerge += ' '+x


for x in roots:
	rootmerge += ' '+x


os.system(rootmerge)

f = open('tempmerge.sh','w')
f.write('#!/bin/sh\n\ncd /afs/cern.ch/cms/slc5_amd64_gcc434/cms/cmssw/CMSSW_4_2_5/src\neval `scramv1 runtime -sh`\ncd -\n\nsource setupRivetProf.sh\n\n'+aidamerge+'\n\nrivet-mkhtml '+aidaout+'\n\n')
f.close()
#sys.exit()
os.system('chmod 777 tempmerge.sh')
os.system('./tempmerge.sh')
os.system('rm tempmerge.sh')
os.system('aida2root '+aidaout)

for x in os.listdir('plots/CMS_WJets_TEST'):
	if '.pdf' not in x:
		continue
		
	os.system( 'rm plots/CMS_WJets_TEST/'+x.replace('.pdf','.png'))
	os.system('convert -trim plots/CMS_WJets_TEST/'+x+' plots/CMS_WJets_TEST/'+x.replace('.pdf','.png'))
