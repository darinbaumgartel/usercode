import os 
import sys
for x in range(len(sys.argv)):
	if sys.argv[x] == '-c':
		castordirectory = sys.argv[x+1]

cast = castordirectory.split('/')[-1]
options = str(sys.argv)
domumu = 0
domunu = 0
donorun = 0
mumu = ['--MuMu','--mumu','--MUMU']
munu = ['--MuNu','--munu','--MUNU']
norun = ['--NoRun','--norun','--NORUN']
for x in mumu:
	if x in options:
		domumu = 1
for x in munu:
	if x in options:
		domunu = 1
for x in norun:
	if x in options:
		donorun = 1

f = open('LoadCastorFiles.C','r')
f2 = open('LoadCastorFiles_'+cast+'.C','w')
for line in f:
	line = line.replace('/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_VBTFTight_2011_06_10_12_28_30',castordirectory)
	f2.write(line)
f.close()
f2.close()

if (domumu):
	f = open('MakePlotsMuMuSub.C','r')
	f2 = open('MakePlotsMuMuSub_'+cast+'.C','w')
	for line in f:
		if 'float' in line and 'ZNormalization' in line:
			line =  'float ZNormalization = 1.0;'
		if 'PlotsMuMuSub' in line:
			line = line.replace('PlotsMuMuSub','PlotsMuMuSub_'+cast)
		if 'LoadCastorFiles' in line:
			line = line.replace('LoadCastorFiles','LoadCastorFiles_'+cast)
		f2.write(line)
	f.close()
	f2.close()

if (domunu):
	f = open('MakePlotsMuNuSub.C','r')
	f2 = open('MakePlotsMuNuSub_'+cast+'.C','w')
	for line in f:
		if 'float' in line and 'WNormalization' in line:
			line =  'float WNormalization = 1.0;'
		if 'PlotsMuNuSub' in line:
			line = line.replace('PlotsMuNuSub','PlotsMuNuSub_'+cast)
		if 'LoadCastorFiles' in line:
			line = line.replace('LoadCastorFiles','LoadCastorFiles_'+cast)
		f2.write(line)
	f.close()
	f2.close()

#from subprocess import call
#call('source /afs/cern.ch/sw/lcg/external/gcc/4.3.2/x86_64-slc5/setup.sh',shell=True)
#call('source /afs/cern.ch/sw/lcg/app/releases/ROOT/5.26.00c_python2.6/x86_64-slc5-gcc43-opt/root/bin/thisroot.sh',shell=True)
from subprocess import call
if (domumu) :
	call ('rm -r PlotsMuMuSub_'+cast,shell=True)
	call ('mkdir PlotsMuMuSub_'+cast,shell=True)
	print 'Getting Scale factors for ZJets for MuMu Plots ...'
	ZOutput = os.popen('root -b MakePlotsMuMuSub_'+cast+'.C').readlines()
	for x in ZOutput:
		if 'Scale Factor' in x:
			Zfac = (x.split(':')[-1])
			ZfacCode = Zfac.split('+-')[0]
if (domunu):
	call ('rm -r PlotsMuNuSub_'+cast,shell=True)
	call ('mkdir PlotsMuNuSub_'+cast,shell=True)
	print 'Getting Scale factors for WJets for MuNu Plots ...'
	WOutput = os.popen('root -b MakePlotsMuNuSub_'+cast+'.C').readlines()
	for x in WOutput:
		if 'Scale Factor' in x:
			Wfac = (x.split(':')[-1])
			WfacCode = Wfac.split('+-')[0]



if (domumu) :
	print 'Plots completed using Z scale factor: '+Zfac

if (domunu):
	print 'Plots completed using W scale factor: '+Wfac

if (domumu) :
	f = open('MakePlotsMuMuSub.C','r')
	f2 = open('MakePlotsMuMuSub_'+cast+'.C','w')
	for line in f:
		if 'float' in line and 'ZNormalization' in line:
			line =  'float ZNormalization = ' + ZfacCode +';'
		if 'PlotsMuMuSub' in line:
			line = line.replace('PlotsMuMuSub','PlotsMuMuSub_'+cast)
		if 'LoadCastorFiles' in line:
			line = line.replace('LoadCastorFiles','LoadCastorFiles_'+cast)
		f2.write(line)
	f.close()
	f2.close()

if (domunu):
	f = open('MakePlotsMuNuSub.C','r')
	f2 = open('MakePlotsMuNuSub_'+cast+'.C','w')
	for line in f:
		if 'float' in line and 'WNormalization' in line:
			line =  'float WNormalization = ' + WfacCode +';'
		if 'PlotsMuNuSub' in line:
			line = line.replace('PlotsMuNuSub','PlotsMuNuSub_'+cast)
		if 'LoadCastorFiles' in line:
			line = line.replace('LoadCastorFiles','LoadCastorFiles_'+cast)
		f2.write(line)
	f.close()
	f2.close()


if (domumu) :

	thisdir = os.popen('pwd').readlines()[0].replace('\n','')
	sub_mumu = open("subMuMu_"+cast+".sh",'w')
	sub_mumu.write('#!/bin/sh\ncd '+thisdir+'\nsource /afs/cern.ch/sw/lcg/external/gcc/4.3.2/x86_64-slc5/setup.sh\nsource /afs/cern.ch/sw/lcg/app/releases/ROOT/5.26.00c_python2.6/x86_64-slc5-gcc43-opt/root/bin/thisroot.sh\nroot -b MakePlotsMuMuSub_'+cast+'.C\n\n')
	sub_mumu.close()
	os.system('chmod 777 sub*sh')
	if (donorun==0):
		os.system('bsub -R "pool>20000" -o /dev/null -e /dev/null -q 1nd -J jobMuMu_'+cast+' < subMuMu_'+cast+'.sh')

if (domunu):
	thisdir = os.popen('pwd').readlines()[0].replace('\n','')
	sub_munu = open("subMuNu_"+cast+".sh",'w')
	sub_munu.write('#!/bin/sh\ncd '+thisdir+'\nsource /afs/cern.ch/sw/lcg/external/gcc/4.3.2/x86_64-slc5/setup.sh\nsource /afs/cern.ch/sw/lcg/app/releases/ROOT/5.26.00c_python2.6/x86_64-slc5-gcc43-opt/root/bin/thisroot.sh\nroot -b MakePlotsMuNuSub_'+cast+'.C\n\n')
	sub_munu.close()
	os.system('chmod 777 sub*sh')
	if (donorun==0):
		os.system('bsub -R "pool>20000" -o /dev/null -e /dev/null -q 1nd -J jobMuNu_'+cast+'< subMuNu_'+cast+'.sh')

#os.system('root -b MakePlotsMuMuSub_'+cast+'.C')
#os.system('root -b MakePlotsMuNuSub_'+cast+'.C')
if (domumu and donorun==0) :
	print 'Plots in batch using Z scale factor: '+Zfac
if (domunu and donorun==0):
	print 'Plots in batch using W scale factor: '+Wfac

