import os 
import sys
for x in range(len(sys.argv)):
	if sys.argv[x] == '-c':
		castordirectory = sys.argv[x+1]

cast = castordirectory.split('/')[-1]

f = open('LoadCastorFiles.C','r')
f2 = open('LoadCastorFilesTemp.C','w')
for line in f:
	line = line.replace('/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_VBTFTight_2011_06_10_12_28_30/',castordirectory)
	f2.write(line)
f.close()
f2.close()

f = open('MakePlotsMuMuSub.C','r')
f2 = open('MakePlotsMuMuSub_'+cast+'.C','w')
for line in f:
	if 'float' in line and 'ZNormalization' in line:
		line =  'float ZNormalization = 1.0;'
	if 'PlotsMuMuSub' in line:
		line = line.replace('PlotsMuMuSub','PlotsMuMuSub_'+cast)
	f2.write(line)
f.close()
f2.close()

f = open('MakePlotsMuNuSub.C','r')
f2 = open('MakePlotsMuNuSub_'+cast+'.C','w')
for line in f:
	if 'float' in line and 'WNormalization' in line:
		line =  'float WNormalization = 1.0;'
	if 'PlotsMuNuSub' in line:
		line = line.replace('PlotsMuNuSub','PlotsMuNuSub_'+cast)
	f2.write(line)
f.close()
f2.close()

#from subprocess import call
#call('source /afs/cern.ch/sw/lcg/external/gcc/4.3.2/x86_64-slc5/setup.sh',shell=True)
#call('source /afs/cern.ch/sw/lcg/app/releases/ROOT/5.26.00c_python2.6/x86_64-slc5-gcc43-opt/root/bin/thisroot.sh',shell=True)
from subprocess import call
call ('rm -r PlotsMuMuSub_'+cast,shell=True)
call ('rm -r PlotsMuNuSub_'+cast,shell=True)
call ('mkdir PlotsMuMuSub_'+cast,shell=True)
call ('mkdir PlotsMuNuSub_'+cast,shell=True)

ZOutput = os.popen('root -b MakePlotsMuMuSub_'+cast+'.C').readlines()

for x in ZOutput:
	if 'Scale Factor' in x:
		Zfac = (x.split(':')[-1])
		ZfacCode = Zfac.split('+-')[0]

WOutput = os.popen('root -b MakePlotsMuNuSub_'+cast+'.C').readlines()

for x in WOutput:
	if 'Scale Factor' in x:
		Wfac = (x.split(':')[-1])
		WfacCode = Wfac.split('+-')[0]



print 'Plots completed using Z scale factor: '+Zfac

print 'Plots completed using W scale factor: '+Wfac


f = open('MakePlotsMuMuSub.C','r')
f2 = open('MakePlotsMuMuSub_'+cast+'.C','w')
for line in f:
	if 'float' in line and 'ZNormalization' in line:
		line =  'float ZNormalization = ' + ZfacCode +';'
	if 'PlotsMuMuSub' in line:
		line = line.replace('PlotsMuMuSub','PlotsMuMuSub_'+cast)
	f2.write(line)
f.close()
f2.close()

f = open('MakePlotsMuNuSub.C','r')
f2 = open('MakePlotsMuNuSub_'+cast+'.C','w')
for line in f:
	if 'float' in line and 'WNormalization' in line:
		line =  'float WNormalization = ' + WfacCode +';'
	if 'PlotsMuNuSub' in line:
		line = line.replace('PlotsMuNuSub','PlotsMuNuSub_'+cast)
	f2.write(line)
f.close()
f2.close()




os.system('root -b MakePlotsMuMuSub_'+cast+'.C')

os.system('root -b MakePlotsMuNuSub_'+cast+'.C')

print 'Plots completed using Z scale factor: '+Zfac

print 'Plots completed using W scale factor: '+Wfac

