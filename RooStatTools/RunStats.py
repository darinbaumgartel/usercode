import os
import sys
import subprocess
# Check the root version
rootinfo = os.popen('root -b -q').readlines()
hostinfo = os.popen('hostname').readline()
hostinfo = str(hostinfo)

rootinfo2 = str(rootinfo)

rootinfo = rootinfo[4].split()[2].split('/')[0]
rootinfo = float(rootinfo)

if 'Version' not in rootinfo2:
	print 'No ROOT version available. Please install ROOT 5.28'
	if 'lxplus' in hostinfo:
		print ('\nLXPlus machine detected. ROOT 5.28 Can be set up with:\n')
		print ('source /afs/cern.ch/sw/lcg/external/gcc/4.3.2/x86_64-slc5/setup.csh\n')
		print ('source /afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00c/x86_64-slc5-gcc43-opt/root/bin/thisroot.csh\n\n')
	sys.exit(0)
		
if (rootinfo<5.28):
	print '\n\nROOT check: Root Version '+str(rootinfo) + ' not recent enough. Use 5.28 or greater.'

	if 'lxplus' in hostinfo:
		print ('\nLXPlus machine detected. ROOT 5.28 Can be set up with:\n')
		print ('source /afs/cern.ch/sw/lcg/external/gcc/4.3.2/x86_64-slc5/setup.csh\n')
		print ('source /afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00c/x86_64-slc5-gcc43-opt/root/bin/thisroot.csh\n\n')
	sys.exit(0)

	
if (rootinfo>=5.28):
	print '\n\nROOT check: Root Version '+str(rootinfo) + ' OK. Continuing with statistical process.\n\n'



# Get relevant information.
XLSFile = sys.argv[1]
filetype = XLSFile.split('.')[-1]

if filetype == 'csv' or filetype == 'CSV':
	os.system('cp '+XLSFile+' LQDataTemp.csv')

if filetype not in ['CSV','csv']:
	print ('File must be of type csv. Please save as .csv file. Exiting.')
	sys.exit(0)


f = os.popen('cat LQDataTemp.csv').readlines()
munu = 0
if "MuNu" in XLSFile:
	munu = 1
	print "Changes will be made to accomodate the MuNu channel cross sections"
	
info = []
start = 0
for x in f:
	if "Summary" in x:
		start = 1
	if "End Summary" in x:
		start = 0
	if start:	
		info.append(x)
	
for x in info:
	if "Signal" in x and "Error" in x and "Data" in x:
		x = x.replace('"','')
		x = x.split(',')
		index = 0
		for entry in x:
			if entry == "Signal":
				SignalPlace = index
				SignalErrorPlace = index + 1
			if entry == "Data":
				DataPlace = index
			if entry == "BG":
				BGPlace = index
				BGErrorPlace = index + 1
			index = index + 1
			
name = []
sig = []
sigerr = []
bg = []
bgerr = []
data = []

for x in info:
	if "Integrated Luminosity" in x:
		lumi = x.replace(',','')
	x = x.replace('"','')
	x = x.split(',')
	if "Sig:" in x[0]:
		name.append(x[0].replace('Sig:',''))
		sig.append(x[SignalPlace])		
		sigerr.append(x[SignalErrorPlace])		
		bg.append(x[BGPlace])		
		bgerr.append(x[BGErrorPlace])		
		data.append(x[DataPlace])	

lumi = lumi.replace('"','').replace(' ','')
lumierror = lumi.split('+-')[-1]
lumi = lumi.replace('IntegratedLuminosity:','').split('+-')[0]
		
codehere = (os.popen('ls roostats_cl95.C').readlines())
codehere = codehere[0].replace('\n','')
if codehere != 'roostats_cl95.C':
	print 'Error: Bayesian Calculator roostats_cl95.C not found in current directory'
	sys.exit(0)

f = open('ExpectedLimits.C','w')
f.write('\n#include "roostats_cl95.C" \n\nvoid MakeLimits()\n{\n\nLimitResult Value;\n\n')

beginline = 'Value = roostats_clm('+str(lumi)+','+str(lumierror)+','

numpseudo = 25
for x in range(len(sys.argv)):
	if sys.argv[x]=='-n':
		numpseudo = sys.argv[x+1]
numpseudo = str(numpseudo)
print "Using psuedoexperimemtns:  " +numpseudo 

for x in range(len(name)):
	thisinfo = []
	thisinfo.append(sig[x])
	thisinfo.append(sigerr[x])
	thisinfo.append(bg[x])
	thisinfo.append(bgerr[x])
	thisinfo.append(numpseudo)
	thisinfo.append('1')
	thisline = (beginline + str(thisinfo).replace('[','').replace(']','') + ');//'+name[x]).replace('\n','')
	thisline = thisline.replace('\'','') + '\n'
	f.write(thisline)

f.write('\n\n}\n\n')
f.close()

f = open('ObservedLimits.C','w')
f.write('\n#include "roostats_cl95.C" \n\nvoid MakeLimits()\n{\n\nfloat Value = 0.0;\n\n')

beginline = 'Value = roostats_cl95('+str(lumi)+','+str(lumierror)+','

for x in range(len(name)):
	thisinfo = []
	thisinfo.append(sig[x])
	thisinfo.append(sigerr[x])
	thisinfo.append(bg[x])
	thisinfo.append(bgerr[x])
	thisinfo.append(data[x])
	thisinfo.append('false')
	thisinfo.append('1')
	thisline = (beginline + str(thisinfo).replace('[','').replace(']','') + ');//'+name[x]).replace('\n','')
	thisline = thisline.replace('\'','') + '\n'
	f.write(thisline)

f.write('\n\n}\n\n')
f.close()

f = open('RunExpectation','w')
f.write('{\ngROOT->ProcessLine(".L ExpectedLimits.C+");\n gROOT->ProcessLine("MakeLimits()");\n gROOT->ProcessLine(".q");\n}')
f.close()
f = open('RunObservation','w')
f.write('{\ngROOT->ProcessLine(".L ObservedLimits.C+");\n gROOT->ProcessLine("MakeLimits()");\n gROOT->ProcessLine(".q");\n}')
f.close()

todo = ''
if len(sys.argv) > 2:
	todo = sys.argv[2]
if todo == 'nocalc':
	todo = 0
else:
	todo = 1

if todo:
	os.system('rm ExpectationLog.txt ObservationLog.txt')

if todo:
	print '\n\n Running Observed Limits. This may take some time and TCanvas Windows may flash on screen.\n\n'
	os.system('root -b RunObservation > ObservationLog.txt ')
	print '\n\n Running Expected Limits. This may take some time and TCanvas Windows may flash on screen.\n\n'
	os.system('root -b RunExpectation > ExpectationLog.txt ')

observedlimits = []
expectedlimits = []
expectedlimits_1sigma_upperbound = []
expectedlimits_1sigma_lowerbound = []
expectedlimits_2sigma_upperbound = []
expectedlimits_2sigma_lowerbound = []
f = os.popen('cat ObservationLog.txt').readlines()
for x in f:
	if '95% C.L. upper limit:' in x:
		thisval = x.replace('\n','').split(':')[-1]
		thisval = thisval.replace(' ','')
		observedlimits.append(thisval)
		
f = os.popen('cat ExpectationLog.txt').readlines()
for x in f:
#	if 'Average upper 95% C.L. limit' in x:
#		thisval = x.replace('\n','').split('=')[-1]
#		thisval = thisval.replace(' pb','')
#		thisval = thisval.replace(' ','')
#		expectedlimits.append(thisval)
	if "median limit:" in x:
		x = x.split()[-1]
		expectedlimits.append(x)
	if "1 sigma band:" in x:
		x =  x.replace('[','@@').replace(']','@@')
		x = x.split('@@')
		x =  x[3]
		x = x.split(',')
		expectedlimits_1sigma_upperbound.append(x[-1])
		expectedlimits_1sigma_lowerbound.append(x[0])
	if "2 sigma band:" in x:
		x =  x.replace('[','@@').replace(']','@@')
		x = x.split('@@')
		x= x[3]
		x = x.split(',')
		expectedlimits_2sigma_upperbound.append(x[-1])
		expectedlimits_2sigma_lowerbound.append(x[0])
		
masses = []
for x in name:
	masses.append(x.replace('LQ',''))
#print masses
#print observedlimits
#print expectedlimits

obstring = (str(observedlimits)).replace(']','').replace('[','').replace('\'','')
exstring = (str(expectedlimits)).replace(']','').replace('[','').replace('\'','')
mstring = (str(masses)).replace(']','').replace('[','').replace('\'','')

PlotTemp=open("BetaSquaredPlot_Template.C")
PlotWrite=open("BetaSquaredPlot.C","w")

shademasses = []
shade1sigma = []
shade2sigma = []

for x in range(len(masses)):
	shademasses.append(masses[x])
	shade1sigma.append(expectedlimits_1sigma_upperbound[x])
	shade2sigma.append(expectedlimits_2sigma_upperbound[x])
for x in range(len(masses)):
	shademasses.append(masses[-x-1])
	shade1sigma.append(expectedlimits_1sigma_lowerbound[-x-1])
	shade2sigma.append(expectedlimits_2sigma_lowerbound[-x-1])
	
#print shademasses
#print shade1sigma
#print shade2sigma

shademassesstring = (str(shademasses)).replace(']','').replace('[','').replace('\'','')
shade1sigmastring = (str(shade1sigma)).replace(']','').replace('[','').replace('\'','')
shade2sigmastring = (str(shade2sigma)).replace(']','').replace('[','').replace('\'','')

for line in PlotTemp.readlines():
	line = line.replace('IntLumiValue',str(lumi))
	if 'Double_t mData[4]' in line:
		line = 'Double_t mData['+`len(name)`+'] = {'+mstring+'};'
	if '@Double_t xsUp_observed' in line:
		line ='Double_t xsUp_observed['+`len(name)`+'] = {'+obstring+'};'
	if '@Double_t xsUp_expected' in line:
		line ='Double_t xsUp_expected['+`len(name)`+'] = {'+exstring+'};'
	if 'new TGraph(size' in line:
		line = line.replace('size',`len(name)`)
	if 'string fileName' in line:
		line = line.replace('.','_'+str(lumi).replace('.','_')+'.')
		
	if 'Double_t x_shademasses' in line:
		line ='Double_t x_shademasses['+ `len(shademasses)`+']={' + shademassesstring+'};\n'
	if 'Double_t y_1sigma' in line:
		line ='Double_t y_1sigma['+ `len(shademasses)`+']={' + shade1sigmastring+'};\n'
	if 'Double_t y_2sigma' in line:
		line ='Double_t y_2sigma['+ `len(shademasses)`+']={' + shade2sigmastring+'};\n'
	if 'numbershade' in line:
		line = line.replace('numbershade',`len(shademasses)`)
	if (munu==1) and ('Double_t xsTh' in line or 'Double_t y_pdf[' in line) :
		contents = line.split('{')[-1]
		contents = contents.split('}')[0]
		contents = contents.split(',')
		for x in contents:
			line = line.replace(x,x+'/2.0')
	if (munu==1):
		line = line.replace('beta^{2}#times','beta(1-#beta)#times')
		line = line.replace('beta=1','beta=1/2')
		line = line.replace('316,316','270,270')
	if 'TGraph *xsData_vs_m_' in line:
		line = line.replace('numberofpoints',str(len(name)))
	PlotWrite.write(line)
PlotWrite.close()
PlotTemp.close()


PlotTemp=open("BetaPlot_Template.C")
PlotWrite=open("BetaPlot.C","w")

for line in PlotTemp.readlines():
	line = line.replace('IntLumiValue',str(lumi))
	if 'Double_t mData[4]' in line:
		line = 'Double_t mData['+`len(name)`+'] = {'+mstring+'};'
	if '@Double_t xsUp_observed' in line:
		line ='Double_t xsUp_observed['+`len(name)`+'] = {'+obstring+'};'
	if '@Double_t xsUp_expected' in line:
		line ='Double_t xsUp_expected['+`len(name)`+'] = {'+exstring+'};'
	if 'string fileName' in line:
		line = line.replace('.','_'+str(lumi).replace('.','_')+'.')
#	if 'new TGraph(size' in line:
#		line = line.replace('size',`len(name)`)
	PlotWrite.write(line)
PlotWrite.close()
PlotTemp.close()


RootPlot=open("PlotRun_BetaSquared","w")
RootLinesToAdd = '\n{\ngROOT->ProcessLine(\".L BetaSquaredPlot.C++\");\ngROOT->ProcessLine(\"makePlots()\");\ngROOT->ProcessLine(\".q\");\n\n}\n'
RootPlot.write(RootLinesToAdd)
RootPlot.close()


RootPlot2=open("PlotRun_Beta","w")
RootLinesToAdd = '\n{\ngROOT->ProcessLine(\".L BetaPlot.C++\");\ngROOT->ProcessLine(\"makePlots()\");\ngROOT->ProcessLine(\".q\");\n\n}\n'
RootPlot2.write(RootLinesToAdd)
RootPlot2.close()


os.system('root -l PlotRun_Beta')
os.system('root -l PlotRun_BetaSquared')


#os.system('rm *.d *.so LQDataTemp.csv Beta*Plot.C PlotRun_* RunExpectation RunObservation *Limits.C')

f = open('LimitSummary.csv','w')
f.write('Sample, Observed, Expected, Expected 1 Sigma Upper, Expected 1 Sigma Lower, Expected 2 Sigma Upper, Expected 2 Sigma  Lower \n')
for x in range(len(masses)):
#	print masses[x]
	line = masses[x] + ','	+observedlimits[x]+','+expectedlimits[x]+','+expectedlimits_1sigma_upperbound[x]+','+expectedlimits_1sigma_lowerbound[x]+','+expectedlimits_2sigma_upperbound[x]+','+expectedlimits_2sigma_lowerbound[x]
	f.write(line)
	f.write('\n')
f.close()


