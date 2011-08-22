import os
import sys
import subprocess
import matplotlib.pyplot
# Check the root version
rootinfo = os.popen('root -b -q').readlines()
hostinfo = os.popen('hostname').readline()
hostinfo = str(hostinfo)

rootinfo2 = str(rootinfo)

rootinfo = rootinfo[4].split()[2].split('/')[0]
rootinfo = float(rootinfo)

do_mumu = 0
do_munu = 0 
do_combo = 0
do_observedonly = 0
cdir = ''
if 'do_mumu' in str(sys.argv):
	do_mumu = 1
if 'do_munu' in str(sys.argv):
	do_munu = 1
if 'do_combo' in str(sys.argv):
	do_combo = 1
if 'just_observed' in str(sys.argv):
	do_observedonly = 1	
numdo = 1	
queue = '1nd'
launcher = 'launcherMCMC.py'
iters = 1
for x in range(len(sys.argv)):
	if sys.argv[x] == '-c':
		cdir = sys.argv[x+1]
		os.system('rfmkdir /castor/cern.ch/user/d/darinb/MuMu'+cdir)
		os.system('rfmkdir /castor/cern.ch/user/d/darinb/MuNu'+cdir)
		os.system('mkdir '+cdir)
	if sys.argv[x] == '-n':
		numdo = int(sys.argv[x+1])
	if sys.argv[x] == '-q':
		queue = str(sys.argv[x+1])
	if sys.argv[x] == '-l':
		launcher = str(sys.argv[x+1])	
	if sys.argv[x] == '--iters':
		iters = int(sys.argv[x+1])		
from ROOT import *
from array import array
	
mTh = array("d",[ 150, 200, 250, 300, 350, 400,450,500,550,600,650,700,750,800,850])
xsTh = array("d",[  53.3, 11.9, 3.47, 1.21, 0.477, .205,.0949,.0463,.0236,.0124,.00676,.00377,.00215,.00124,.000732])

g = TGraph(len(mTh),mTh,xsTh);
spline = TSpline3("xsection",g) 
#xx = (spline.Eval(310));
M_th=[ 150, 200, 250, 300, 350, 400,450,500,550,600,650,700,750,800,850]
X_th=[  53.3, 11.9, 3.47, 1.21, 0.477, .205,.0949,.0463,.0236,.0124,.00676,.00377,.00215,.00124,.000732]
	


XLSFile = sys.argv[1]
filetype = XLSFile.split('.')[-1]

if filetype == 'csv' or filetype == 'CSV':
	os.system('cp '+XLSFile+' LQDataTemp.csv')

if filetype not in ['CSV','csv']:
	print ('File must be of type csv. Please save as .csv file. Exiting.')
	sys.exit(0)


f = os.popen('cat LQDataTemp.csv').readlines()

	
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
			if entry == "S_final":
				SignalPlace = index
			if entry == "Signal":
				SignalErrorPlace = index + 1
			if entry == "Data":
				DataPlace = index
			if entry == "BG":
				BGPlace = index
				BGErrorPlace = index + 1
			if entry == "Stat":
				StatErrorPlace = index
			if entry == "Norm":
				NormErrorPlace = index
			if entry == "JES":
				JESErrorPlace = index
			if entry == "LepID":
				LepIDErrorPlace = index
			if entry == "LepRes":
				LepResErrorPlace = index
			if entry == "Other": 
				OtherErrorPlace = index
			if entry == "Shape":
				ShapeErrorPlace = index
			index = index + 1
			
name = []
sig = []
sigerr = []
bg = []
bgerr = []
data = []
stat = []
norm = []
jes = []
lepid = []
lepres = []
other = []
shape = []

for x in info:
	if "Integrated Luminosity" in x:
		lumi = x.replace(',','')
	x = x.replace('"','')
	x = x.split(',')
	if "Sig:" in x[0]:
		name.append(x[0].replace('Sig:',''))
		sig.append(x[SignalPlace])		
		sigerr.append(str(float(x[SignalErrorPlace])*float(x[SignalPlace])))		
		bg.append(x[BGPlace])		
		bgerr.append(x[BGErrorPlace])		
		data.append(x[DataPlace])	
		stat.append(x[StatErrorPlace])
		norm.append(x[NormErrorPlace])
		jes.append(x[JESErrorPlace])
		lepid.append(x[LepIDErrorPlace])
		lepres.append(x[LepResErrorPlace])
		other.append(x[OtherErrorPlace])
		shape.append(x[ShapeErrorPlace])

lumi = lumi.replace('"','').replace(' ','')
lumierror = lumi.split('+-')[-1]
lumi = lumi.replace('IntegratedLuminosity:','').split('+-')[0]

print XLSFile+':  \n\nInformation will be parsed to cards: \n\n'

print data
print stat
print norm
print jes
print lepid
print lepres
print other
print shape


#  ------------------------------------------------------------------------------------------------------- #


XLSFile = sys.argv[2]
filetype = XLSFile.split('.')[-1]

if filetype == 'csv' or filetype == 'CSV':
	os.system('cp '+XLSFile+' LQDataTemp.csv')

if filetype not in ['CSV','csv']:
	print ('File must be of type csv. Please save as .csv file. Exiting.')
	sys.exit(0)


f = os.popen('cat LQDataTemp.csv').readlines()

	
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
			if entry == "S_final":
				SignalPlace = index
			if entry == "Signal":
				SignalErrorPlace = index + 1
			if entry == "Data":
				DataPlace = index
			if entry == "BG":
				BGPlace = index
				BGErrorPlace = index + 1
			if entry == "Stat":
				StatErrorPlace = index
			if entry == "Norm":
				NormErrorPlace = index
			if entry == "JES":
				JESErrorPlace = index
			if entry == "LepID":
				LepIDErrorPlace = index
			if entry == "LepRes":
				LepResErrorPlace = index
			if entry == "Other": 
				OtherErrorPlace = index
			if entry == "Shape":
				ShapeErrorPlace = index
			index = index + 1
name2 = []
sig2 = []
sigerr2 = []
bg2 = []
bgerr2 = []
data2 = []
stat2 = []
norm2 = []
jes2 = []
lepid2 = []
lepres2 = []
other2 = []
shape2 = []

for x in info:
	if "Integrated Luminosity" in x:
		lumi = x.replace(',','')
	x = x.replace('"','')
	x = x.split(',')
	if "Sig:" in x[0]:
		name2.append(x[0].replace('Sig:',''))
		sig2.append(x[SignalPlace])		
		sigerr2.append(str(float(x[SignalErrorPlace])*float(x[SignalPlace])))		
		bg2.append(x[BGPlace])		
		bgerr2.append(x[BGErrorPlace])		
		data2.append(x[DataPlace])	
		stat2.append(x[StatErrorPlace])
		norm2.append(x[NormErrorPlace])
		jes2.append(x[JESErrorPlace])
		lepid2.append(x[LepIDErrorPlace])
		lepres2.append(x[LepResErrorPlace])
		other2.append(x[OtherErrorPlace])
		shape2.append(x[ShapeErrorPlace])
cr = '\n'
print '\n\n'+XLSFile+':  \n\nInformation will be parsed to cards: \n\n'


print data2
print stat2
print norm2
print jes2
print lepid2
print lepres2
print other2
print shape2




masses_comb = 'Double_t masses_comb['
masses_mumu = 'Double_t masses_one['
masses_munu = 'Double_t masses_half['

b_comb = 'Double_t beta_comb['
b_mumu = 'Double_t beta_one['
b_munu= 'Double_t beta_half['


theoryratios = []
theoryratioerrors = []

beta_combo = []
m_combo = []
dif_combo = []

rat = -99.0
precision = .001


relstat = []
relnorm = []
reljes = []
rellepid = []
rellepres = []
relother = []
relshape = []

relstat2 = []
relnorm2 = []
reljes2 = []
rellepid2 = []
rellepres2 = []
relother2 = []
relshape2 = []


for i in range(len(data)):
	nbg = float(bg[i])
	nstat = float(stat[i])
	nnorm = float(norm[i])
	njes = float( jes[i])
	nlepid = float(lepid[i])
	nlepres = float(lepres[i])
	nother = float(other[i])
	nshape = float(shape[i])
		
	relstat.append(str((nbg+nstat)/nbg))
	relnorm.append(str((nbg+nnorm)/nbg))
	reljes.append(str((nbg+njes)/nbg))
	rellepid.append(str((nbg+nlepid)/nbg))
	rellepres.append(str((nbg+nlepres)/nbg))
	relother.append(str((nbg+nother)/nbg))
	relshape.append(str((nbg+nshape)/nbg))
		
print relstat
print relnorm
print reljes
print rellepid
print rellepres
print relother
print relshape


for i in range(len(data2)):
	nbg = float(bg2[i])
	nstat = float(stat2[i])
	nnorm = float(norm2[i])
	njes = float( jes2[i])
	nlepid = float(lepid2[i])
	nlepres = float(lepres2[i])
	nother = float(other2[i])
	nshape = float(shape2[i])
		
	relstat2.append(str((nbg+nstat)/nbg))
	relnorm2.append(str((nbg+nnorm)/nbg))
	reljes2.append(str((nbg+njes)/nbg))
	rellepid2.append(str((nbg+nlepid)/nbg))
	rellepres2.append(str((nbg+nlepres)/nbg))
	relother2.append(str((nbg+nother)/nbg))
	relshape2.append(str((nbg+nshape)/nbg))
		
print relstat2
print relnorm2
print reljes2
print rellepid2
print rellepres2
print relother2
print relshape2



beta_mumu = []
m_mumu = []
dif_mumu = []
rat = -99.0
precision = .001

if do_mumu == 1:
	for x in range(len(name)):
		f = open('confmumu'+cdir+'_'+name[x]+'.cfg','w')
		f.write( 'imax    1'+cr )
		f.write(  'jmax    1' +cr)
		f.write(  'kmax    8 '+cr)
		f.write(  'bin   1  '+cr)
		f.write(  'observation   '+str(data[x])+cr)
		f.write(  'bin 1 1 '+cr)
		f.write(  'process ' +name[x]+ ' bkg_all  ' +cr)
		f.write(  ' process 0 1 '+cr)
		f.write(  'rate  '+str(float(sig[x])) + '  '+str(bg[x])  +'  '+cr)
		f.write(  'lumi lnN  1.045 - '+cr)
		#f.write(  'allsys lnN ' + str( ( ( float(sig[x]))  + float(sigerr[x]) ) /float(sig[x]) ) +'  ' + str( ( ( float(bg[x]))  + float(bgerr[x]) ) /float(bg[x]) ) +'  '+cr )
		#f.write(  'allsys lnN ' + str( ( ( float(sig[x]))  + float(sigerr[x]) ) /float(sig[x]) ) +'  ' + str( ( ( float(bg[x]))  + float(bgerr[x]) ) /float(bg[x]) ) +cr )
		f.write( 'sigsys lnN ' + str( ( ( float(sig[x]))  + float(sigerr[x]) ) /float(sig[x]) ) +' - ' +cr )
		f.write( 'stat lnN   -  ' + relstat[x]  + '  ' + cr   )
		f.write( 'norm lnN   -  ' + relnorm[x]  + '    ' + cr   )
		f.write( 'jes lnN   -  ' + reljes[x]  + '    ' + cr   )
		f.write( 'lepid lnN   -  ' + rellepid[x]  + '     ' + cr   )
		f.write( 'lepres lnN   -  ' + rellepres[x]  + '    ' + cr   )
		#f.write( 'other lnN   -  ' + relother[x]  + '    ' + cr   )	
		f.write( 'shape lnN   -  ' + relshape[x]  + '     ' + cr   )
		os.system('rfmkdir /castor/cern.ch/user/d/darinb/MuMu'+cdir+'/'+name[x])
					
		f.close()
		if (do_observedonly == 0):
			

			mdir = (os.popen('pwd').readlines())[0]
			mdir = mdir.replace('\n','')
			fsub = open('submumu_'+cdir+name[x]+'.csh','w')
			fsub.write('#!/bin/csh'+ cr)
			fsub.write('cd ' + mdir+ cr)
			fsub.write('eval `scramv1 runtime -csh`'+ cr)
			fsub.write('cd -'+ cr)
			fsub.write('cp '+mdir+'/'+launcher+' . '+ cr)
			fsub.write('cp '+mdir+'/confmumu'+cdir+'_'+name[x]+ '.cfg . '+ cr)
			for ii in range(iters):
				fsub.write('python '+launcher+' '+name[x]+' mumu'+cdir+cr)
			fsub.write('cp log*.txt '+mdir+'/'+cdir+'/'+ cr +cr +cr)
			fsub.write('rfcp log*.txt /castor/cern.ch/user/d/darinb/MuMu'+cdir+'/'+ cr +cr +cr)
			fsub.write('rfcp *root /castor/cern.ch/user/d/darinb/MuMu'+cdir+'/'+name[x]+'/'+ cr +cr +cr)			
			fsub.close()
			os.system('chmod 777 *csh')
			for nn in range(numdo):
	
				os.system('bsub -o /dev/null -e /dev/null -q '+queue+' -J jobmumu'+str(nn)+'_'+name[x]+' < submumu_'+cdir+name[x]+'.csh')
	
		if (do_observedonly == 1):
			#os.system('combine -v 0 -d confmumu'+'_'+cdir+name[x]+'.cfg -M MarkovChainMC --tries 200 -i 20000 -H ProfileLikelihood --hintSafetyFactor 30') 
			os.system('combine -v -1 -d confmumu'+'_'+cdir+name[x]+'.cfg -M HybridNew --rule CLs -s -1 --testStat LHC -H ProfileLikelihood --fork 16') 
	


beta_munu = []
m_munu = []
dif_munu = []
rat = -99.0
precision = .001

if do_munu == 1:
	
	for x in range(len(name)):
		f = open('confmunu'+cdir+'_'+name[x]+'.cfg','w')
		f.write( 'imax    1'+cr )
		f.write(  'jmax    1' +cr)
		f.write(  'kmax    8'+cr)
		f.write(  'bin   1  '+cr)
		f.write(  'observation   '+str(data2[x])+cr)
		f.write(  'bin 1 1 '+cr)
		f.write(  'process ' +name[x]+ ' bkg_all  ' +cr)
		f.write(  ' process 0 1 '+cr)
		f.write(  'rate  '+str(float(sig2[x])) + '  '+str(bg2[x])  +'  '+cr)
		f.write(  'lumi lnN  1.045 - '+cr)
		#f.write(  'allsys lnN ' + str( ( ( float(sig2[x]))  + float(sigerr2[x]) ) /float(sig2[x]) ) +'  ' + str( ( ( float(bg2[x]))  + float(bgerr2[x]) ) /float(bg2[x]) ) +'  '+cr )
		#f.write(  'allsys lnN ' + str( ( ( float(sig2[x]))  + float(sigerr2[x]) ) /float(sig2[x]) ) +'  ' + str( ( ( float(bg2[x]))  + float(bgerr2[x]) ) /float(bg2[x]) ) +cr )
		f.write( 'sigsys lnN ' + str( ( ( float(sig2[x]))  + float(sigerr2[x]) ) /float(sig2[x]) ) +'  -  ' +cr )
		f.write( 'stat lnN   -  ' + relstat2[x]  + '  ' + cr   )
		f.write( 'norm lnN   -  ' + relnorm2[x]  + '    ' + cr   )
		f.write( 'jes lnN   -  ' + reljes2[x]  + '    ' + cr   )
		f.write( 'lepid lnN   -  ' + rellepid2[x]  + '     ' + cr   )
		f.write( 'lepres lnN   -  ' + rellepres2[x]  + '    ' + cr   )
		#f.write( 'other lnN   -  ' + relother[x]  + '    ' + cr   )	
		f.write( 'shape lnN   -  ' + relshape2[x]  + '     ' + cr   )
		os.system('rfmkdir /castor/cern.ch/user/d/darinb/MuNu'+cdir+'/'+name[x])

					
		f.close()
		if (do_observedonly == 0):
					
			mdir = (os.popen('pwd').readlines())[0]
			mdir = mdir.replace('\n','')
			fsub = open('submumu_'+cdir+name[x]+'.csh','w')
			fsub.write('#!/bin/csh'+ cr)
			fsub.write('cd ' + mdir+ cr)
			fsub.write('eval `scramv1 runtime -csh`'+ cr)
			fsub.write('cd -'+ cr)
			fsub.write('cp '+mdir+'/'+launcher+' . '+ cr)
			fsub.write('cp '+mdir+'/confmunu'+cdir+'_'+name[x]+ '.cfg . '+ cr)
			for ii in range(iters):
				fsub.write('python '+launcher+' '+name[x]+' munu'+cdir+cr)
			fsub.write('cp log.txt '+mdir+'/'+cdir+'/'+ cr +cr +cr)
			fsub.write('rfcp log*.txt /castor/cern.ch/user/d/darinb/MuNu'+cdir+'/'+ cr +cr +cr)
			fsub.write('rfcp *root /castor/cern.ch/user/d/darinb/MuNu'+cdir+'/'+name[x]+'/'+ cr +cr +cr)	
			fsub.close()
			os.system('chmod 777 *csh')
			for nn in range(numdo):
	
				os.system('bsub -o /dev/null -e /dev/null -q '+queue+' -J jobmunu'+str(nn)+'_'+name[x]+' < submumu_'+cdir+name[x]+'.csh')			
			
		if (do_observedonly == 1):
			#os.system('combine -v 0  -d confmunu'+'_'+name[x]+'.cfg -M MarkovChainMC --tries 200 -i 20000 -H ProfileLikelihood --hintSafetyFactor 30')
			os.system('combine -v -1 -d confmunu'+'_'+cdir+name[x]+'.cfg -M HybridNew --rule CLs -s -1 --testStat LEP -H ProfileLikelihood --fork 16') 
