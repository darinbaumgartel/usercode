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
if 'do_mumu' in str(sys.argv):
	do_mumu = 1
if 'do_munu' in str(sys.argv):
	do_munu = 1
if 'do_combo' in str(sys.argv):
	do_combo = 1
	
from ROOT import *
from array import array
	
mTh = array("d",[ 150, 200, 250, 300, 350, 400,450,500,550,600,650,700,750,800,850])
xsTh = array("d",[  53.3, 11.9, 3.47, 1.21, 0.477, .205,.0949,.0463,.0236,.0124,.00676,.00377,.00215,.00124,.000732])

g = TGraph(len(mTh),mTh,xsTh);
spline = TSpline3("xsection",g) 
#xx = (spline.Eval(310));
M_th=[ 150, 200, 250, 300, 350, 400,450,500,550,600,650,700,750,800,850]
X_th=[  53.3, 11.9, 3.47, 1.21, 0.477, .205,.0949,.0463,.0236,.0124,.00676,.00377,.00215,.00124,.000732]
	
def sigmaval(mval):
	return spline.Eval(mval)
	

def mval(sigma):
	testm = 150
	oldtestm = 800
	inc = 50
	dif = 55
	olddif = 000
	while abs(oldtestm - testm)>0.01:
		testsigma = sigmaval(testm)
		olddif = dif
		dif = testsigma -sigma
		if testm>1000:
			break
		if dif*olddif <= 0.0:
			inc = -inc/2.3
		oldtestm = testm
		#print '**' + str(testm) + '  ' + str(testsigma) +'  ' +str(dif) + '   ' + str(dif*olddif)

		testm = testm + inc
	return testm
import math
inputarrayX = []
inputarrayY = []
def logspline(inputarrayX,inputarrayY):
	logarray = []
	for x in inputarrayY:
		logarray.append(math.log(x))
	x = array("d",inputarrayX)
	y = array("d",logarray)
	g = TGraph(len(x),x,y)
	outspline = TSpline3("",g)
	return outspline
logtheory = logspline(M_th,X_th)

#revth = X_th
#revth.reverse()
from math import exp
#antilogtheory = logspline(M_th,revth)
#print "starting"
def get_intersection(spline1, spline2, xmin,xmax):
	num = xmax-xmin
	inc = (xmax - xmin)/num
	dif = []
	sdif = []
	x = xmin
	xvals = []
	xx = []
	yy = []
	xvals = []
	while x<xmax:
		thisdif = (exp(spline1.Eval(x)) - exp(spline2.Eval(x)))
		xx.append(exp(spline1.Eval(x)))
		yy.append(exp(spline2.Eval(x)))
		sdif.append(thisdif)
		dif.append(abs(thisdif))
		xvals.append(x)
		#print  str(x) + '   ' +str(exp(spline1.Eval(x))) + '    '+str(exp(spline2.Eval(x))) + '    ' + str(thisdif)
		x = x+inc
	mindif = min(dif)
	bestmass = 0		
	for x in range(len(dif)-2):
		a = sdif[x]
		b = sdif[x+1]
		#print str(xvals[x+1]) +'    '+str(a)  + '     ' +str(b) 
		if ((a/abs(a))*(b/abs(b))) < 0.0:
			bestmass = xvals[x]
			break;
					
	return [bestmass,mindif]

	
#goodm = get_intersection(logtheory,antilogtheory,150,850)
	

#betas = [0.01,0.03,.05,0.07,.09,.10,0.15,0.25,0.35,0.4,0.45,0.5,0.55,0.6,0.7,.8,.9,.95,.999]
#betas = [0.1,0.3,0.5,0.6,0.7,0.9,0.9999]
#betas = [0.01,0.03,0.05,0.07,0.09,0.11,0.13,0.15,0.17,0.19,0.21,0.23,0.25,0.27,0.29,0.31,0.33,0.35,0.37,0.39,0.41,0.43,0.45,0.47,0.49,0.5,0.52,0.54,0.56,0.58,0.6,0.62,0.64,0.66,0.68,0.7,0.72,0.74,0.76,0.78,0.8,0.82,0.84,0.86,0.88,0.9,0.92,0.94,0.96,0.98,0.9999]
#betas = [0.99999999]
#betas = [0.9999]
#betas = [.01,.04,.07,.11,.15]

#betas = [0.15,0.17,0.19,0.21,0.23,0.25,0.27,0.29,0.31,0.33,0.35,0.37,0.39,0.41,0.43,0.45,0.47,0.49,0.5,0.52,0.54,0.56,0.58,0.6,0.62,0.64,0.66,0.68,0.7,0.72,0.74,0.76,0.78,0.8,0.82,0.84,0.86,0.88,0.9,0.92,0.94,0.96,0.98,0.9999]
betas = [.01,.03,.05,.07,.09,.11,.13,.15,.17,.19,.23,.27,.31,.35,.39,.43,.45,.47,.49,.51,.53,.56,.59,.63,.67,.71,.74,.76,.78,.80,.82,.84,.86,.88,.90,.92,.94,.96,.98,.99999]
betas = [0.9999999]


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




if do_combo == 1:
	kill = 0 
	for beta in betas:
		beta_combo.append(beta)
		these_masses = []
		these_ratios = []
		these_limits = []
		
		for x in range(len(name)):
			these_masses.append(float(name[x].replace('LQ','')))

			f = open('conf_'+name[x]+'.cfg','w')
			f.write( 'imax    2'+cr )
			f.write(  'jmax    1' +cr)
			f.write(  'kmax    12'+cr)
			f.write(  'bin   1  2'+cr)
			f.write(  'observation   '+str(data[x])+ '  '+str(data2[x])+cr)
			f.write(  'bin 1 1 2 2 '+cr)
			f.write(  'process ' +name[x]+ ' bkg_all  ' +name[x]+ ' bkg_all  '+cr)
			f.write(  ' process 0 1 0 1'+cr)
			f.write(  'rate  '+str(beta*beta*float(sig[x])) + '  '+str(bg[x]) +'  '+str(0 + (beta<1.0)*((4.0*beta*(1-beta))*float(sig2[x])) ) + '  '+str(bg2[x]) +'  '+cr)
			f.write(  'lumi lnN  1.045 - 1.045 - '+cr)
			#msigerr = (1-((( ( float(sig2[x]))  + float(sigerr2[x]) ) /float(sig2[x]))-1))
			#mbgerr = (1-((( ( float(bg2[x]))  + float(bgerr2[x]) ) /float(bg2[x]) ) -1)) 
			msigerr = ( ( float(sig2[x]))  + float(sigerr2[x]) ) /float(sig2[x])
			mbgerr = ( ( float(bg2[x]))  + float(bgerr2[x]) ) /float(bg2[x]) 
			#f.write(  'allsys lnN ' + str( ( ( float(sig[x]))  + float(sigerr[x]) ) /float(sig[x]) ) +'  ' + str( ( ( float(bg[x]))  + float(bgerr[x]) ) /float(bg[x]) ) +'  '+  str( 1.9999*(msigerr>2.0)+(msigerr < 2.0)*(msigerr) ) +'  ' + str( 1.999*(mbgerr>2.0)+(mbgerr < 2.0)*(mbgerr))  +cr )
			#f.write(  'allsys lnN ' + str( ( ( float(sig[x]))  + float(sigerr[x]) ) /float(sig[x]) ) +'  ' + str( ( ( float(bg[x]))  + float(bgerr[x]) ) /float(bg[x]) ) +'  '+  str( ( ( float(sig2[x]))  + float(sigerr2[x]) ) /float(sig2[x]) ) +'  ' + str( ( ( float(bg2[x]))  + float(bgerr2[x]) ) /float(bg2[x]) )+cr )
			#f.write(  'allsys1 lnN ' + str( ( ( float(sig[x]))  + float(sigerr[x]) ) /float(sig[x]) ) +'  ' + str( ( ( float(bg[x]))  + float(bgerr[x]) ) /float(bg[x]) ) +'  -  - '+cr )
			#f.write(  'allsys2 lnN ' + '  -   -  '+  str( ( ( float(sig2[x]))  + float(sigerr2[x]) ) /float(sig2[x]) ) +'  ' + str( ( ( float(bg2[x]))  + float(bgerr2[x]) ) /float(bg2[x]) )+cr )
			f.write( 'sigsys lnN ' + str( ( ( float(sig[x]))  + float(sigerr[x]) ) /float(sig[x]) ) +'  -  -  - ' +cr )
			f.write( 'sigsys2 lnN - -  '+  str( ( ( float(sig2[x]))  + float(sigerr2[x]) ) /float(sig2[x]) ) +'  - ' +cr )
			f.write( 'stat lnN   -  ' + relstat[x]  + '   -  - ' + cr   )
			f.write( 'stat2 lnN   -  -  -  ' + relstat2[x] + '  ' + cr   )
			f.write( 'norm lnN   -  ' + relnorm[x]  + '   -  -  ' + cr   )
			f.write( 'norm2 lnN   -  -   -  ' + relnorm2[x] + '  ' + cr   )
			f.write( 'jes lnN   -  ' + reljes[x]  + '   -  ' + reljes2[x] + '  ' + cr   )
			f.write( 'lepid lnN   -  ' + rellepid[x]  + '   -  ' + rellepid2[x] + '  ' + cr   )
			f.write( 'lepres lnN   -  ' + rellepres[x]  + '   -  ' + rellepres2[x] + '  ' + cr   )
			#f.write( 'other lnN   -  ' + relother[x]  + '   -  ' + relother2[x] + '  ' + cr   )	
			f.write( 'shape lnN   -  ' + relshape[x]  + '   -  -  ' + cr   )
			f.write( 'shape2 lnN   -  -   -  ' + relshape2[x] + '  ' + cr   )

			f.close()
			limit = os.popen('combine -v 0 -d conf_'+name[x]+'.cfg -M MarkovChainMC --tries 100  -H ProfileLikelihood ').readlines()
			for line in limit:
				if 'r <' in line:
					oline = line
					line = line.split(' ')
					for i in range(len(line)):
						if '<' in line[i]:
							print name[x]+', beta = '+str(beta)+' :  ' +oline
							goodline = line
			line = goodline	
			for i in range(len(line)):
				if  line[i]=='r' and line[i+1] == '<' :
					rat = float(line[i+2].replace(';',''))
					these_ratios.append(rat)
			print these_masses
			print these_ratios

			for i in range(len(M_th)):
				if (these_masses[x] == M_th[i]):
					these_limits.append(X_th[i]*rat)
			#print these_limits

		fitted_limits = logspline(these_masses,these_limits)

		goodm = get_intersection(logtheory,fitted_limits,250,850)
		gooddif = goodm[-1]
		goodm  = goodm[0]
		
		print '\n\n\n***************   Mass Point Found: beta = ' + str(beta) + '    m = ' + str(goodm) + ',   dif = '+  str(gooddif) +'\n\n'
		m_combo.append(goodm)
		dif_combo.append(gooddif)

	masses_comb += str(len(m_combo))+'] = {'
	b_comb += str(len(m_combo))+'] = {'
	for x in range(len(m_combo)):
		masses_comb += str(m_combo[x]) +','
		b_comb += str(beta_combo[x]) +','
	masses_comb += '};\n'
	b_comb += '};\n'
	masses_comb = masses_comb.replace(',}','}')
	b_comb = b_comb.replace(',}','}')
	print 2*cr + masses_comb +cr+ b_comb + 2*cr
	print dif_combo



beta_mumu = []
m_mumu = []
dif_mumu = []
rat = -99.0
precision = .001

if do_mumu == 1:
	kill = 0 
	for beta in betas:
		beta_mumu.append(beta)
		these_masses = []
		these_ratios = []
		these_limits = []
		
		for x in range(len(name)):
			these_masses.append(float(name[x].replace('LQ','')))

			f = open('confmumu_'+name[x]+'.cfg','w')
			f.write( 'imax    1'+cr )
			f.write(  'jmax    1' +cr)
			f.write(  'kmax    8'+cr)
			f.write(  'bin   1  '+cr)
			f.write(  'observation   '+str(data[x])+cr)
			f.write(  'bin 1 1 '+cr)
			f.write(  'process ' +name[x]+ ' bkg_all  ' +cr)
			f.write(  ' process 0 1 '+cr)
			f.write(  'rate  '+str(beta*beta*float(sig[x])) + '  '+str(bg[x])  +'  '+cr)
			f.write(  'lumi lnN  1.045 - '+cr)
			#f.write(  'allsys lnN ' + str( ( ( float(sig[x]))  + float(sigerr[x]) ) /float(sig[x]) ) +'  ' + str( ( ( float(bg[x]))  + float(bgerr[x]) ) /float(bg[x]) ) +'  '+cr )
			#f.write(  'allsys lnN ' + str( ( ( float(sig[x]))  + float(sigerr[x]) ) /float(sig[x]) ) +'  ' + str( ( ( float(bg[x]))  + float(bgerr[x]) ) /float(bg[x]) ) +cr )
			f.write( 'sigsys lnN ' + str( ( ( float(sig[x]))  + float(sigerr[x]) ) /float(sig[x]) ) +'  - ' +cr )
			f.write( 'stat lnN   -  ' + relstat[x]  + '  ' + cr   )
			f.write( 'norm lnN   -  ' + relnorm[x]  + '    ' + cr   )
			f.write( 'jes lnN   -  ' + reljes[x]  + '    ' + cr   )
			f.write( 'lepid lnN   -  ' + rellepid[x]  + '     ' + cr   )
			f.write( 'lepres lnN   -  ' + rellepres[x]  + '    ' + cr   )
			#f.write( 'other lnN   -  ' + relother[x]  + '    ' + cr   )	
			f.write( 'shape lnN   -  ' + relshape[x]  + '     ' + cr   )
			
						
			f.close()
			#limit = os.popen('combine -d confmumu_'+name[x]+'.cfg -M BayesianSimple').readlines()
			limit = os.popen('combine -v 0 -d confmumu_'+name[x]+'.cfg -M MarkovChainMC --tries 100 -H ProfileLikelihood ').readlines()
			for line in limit:
				if 'r <' in line:
					oline = line
					line = line.split(' ')
					for i in range(len(line)):
						if '<' in line[i]:
							print name[x]+', beta = '+str(beta)+' :  ' +oline
							goodline = line
			line = goodline	
			for i in range(len(line)):
				if  line[i]=='r' and line[i+1] == '<' :
					rat = float(line[i+2].replace(';',''))
					these_ratios.append(rat)
			#print these_masses
			##print these_ratios

			for i in range(len(M_th)):
				if (these_masses[x] == M_th[i]):
					these_limits.append(X_th[i]*rat)
			#print these_limits

		fitted_limits = logspline(these_masses,these_limits)

		goodm = get_intersection(logtheory,fitted_limits,250,850)
		gooddif = goodm[-1]
		goodm  = goodm[0]
		print '\n\n\n***************   Mass Point Found: beta = ' + str(beta) + '    m = ' + str(goodm) + ',   dif = '+  str(gooddif) +'\n\n'
		if goodm > 0:
			m_mumu.append(goodm)
			dif_mumu.append(gooddif)
		

	masses_mumu += str(len(m_mumu))+'] = {'
	b_mumu += str(len(m_mumu))+'] = {'
	for x in range(len(m_mumu)):
		masses_mumu += str(m_mumu[x]) +','
		b_mumu += str(beta_mumu[x]) +','
	masses_mumu += '};\n'
	b_mumu += '};\n'
	masses_mumu = masses_mumu.replace(',}','}')
	b_mumu = b_mumu.replace(',}','}')
	print 2*cr + masses_mumu +cr+ b_mumu + 2*cr
	print dif_mumu



beta_munu = []
m_munu = []
dif_munu = []
rat = -99.0
precision = .001

if do_munu == 1:
	kill = 0 
	for beta in betas:
		beta_munu.append(beta)
		these_masses = []
		these_ratios = []
		these_limits = []
		
		for x in range(len(name)):
			these_masses.append(float(name[x].replace('LQ','')))

			f = open('confmunu_'+name[x]+'.cfg','w')
			f.write( 'imax    1'+cr )
			f.write(  'jmax    1' +cr)
			f.write(  'kmax    8'+cr)
			f.write(  'bin   1  '+cr)
			f.write(  'observation   '+str(data2[x])+cr)
			f.write(  'bin 1 1 '+cr)
			f.write(  'process ' +name[x]+ ' bkg_all  ' +cr)
			f.write(  ' process 0 1 '+cr)
			f.write(  'rate  '+str(4.0*beta*(1-beta)*float(sig2[x])) + '  '+str(bg2[x])  +'  '+cr)
			f.write(  'lumi lnN  1.045 - '+cr)
			#f.write(  'allsys lnN ' + str( ( ( float(sig2[x]))  + float(sigerr2[x]) ) /float(sig2[x]) ) +'  ' + str( ( ( float(bg2[x]))  + float(bgerr2[x]) ) /float(bg2[x]) ) +'  '+cr )
			#f.write(  'allsys lnN ' + str( ( ( float(sig2[x]))  + float(sigerr2[x]) ) /float(sig2[x]) ) +'  ' + str( ( ( float(bg2[x]))  + float(bgerr2[x]) ) /float(bg2[x]) ) +cr )
			f.write( 'sigsys lnN ' + str( ( ( float(sig2[x]))  + float(sigerr2[x]) ) /float(sig2[x]) ) +' - ' +cr )
			f.write( 'stat lnN   -  ' + relstat2[x]  + '  ' + cr   )
			f.write( 'norm lnN   -  ' + relnorm2[x]  + '    ' + cr   )
			f.write( 'jes lnN   -  ' + reljes2[x]  + '    ' + cr   )
			f.write( 'lepid lnN   -  ' + rellepid2[x]  + '     ' + cr   )
			f.write( 'lepres lnN   -  ' + rellepres2[x]  + '    ' + cr   )
			#f.write( 'other lnN   -  ' + relother[x]  + '    ' + cr   )	
			f.write( 'shape lnN   -  ' + relshape2[x]  + '     ' + cr   )
			
			f.close()
			#limit = os.popen('combine -d confmunu_'+name[x]+'.cfg -M BayesianSimple').readlines()
			limit = os.popen('combine -v 0 -d confmunu_'+name[x]+'.cfg -M MarkovChainMC --tries 100 -H ProfileLikelihood ').readlines()

			for line in limit:
				if 'r <' in line:
					oline = line
					line = line.split(' ')
					for i in range(len(line)):
						if '<' in line[i]:
							print name[x]+', beta = '+str(beta)+' :  ' +oline
							goodline = line
			line = goodline	
			for i in range(len(line)):
				if  line[i]=='r' and line[i+1] == '<' :
					rat = float(line[i+2].replace(';',''))
					these_ratios.append(rat)
			#print these_masses
			#print these_ratios

			for i in range(len(M_th)):
				if (these_masses[x] == M_th[i]):
					these_limits.append(X_th[i]*rat)
			#print these_limits

		fitted_limits = logspline(these_masses,these_limits)

		goodm = get_intersection(logtheory,fitted_limits,250,850)
		gooddif = goodm[-1]
		goodm  = goodm[0]
		print '\n\n\n***************   Mass Point Found: beta = ' + str(beta) + '    m = ' + str(goodm) + ',   dif = '+  str(gooddif) +'\n\n'
		
		if goodm > 0:
			m_munu.append(goodm)
			dif_munu.append(gooddif)
		

	masses_munu += str(len(m_munu))+'] = {'
	b_munu += str(len(m_munu))+'] = {'
	for x in range(len(m_munu)):
		masses_munu += str(m_munu[x]) +','
		b_munu += str(beta_munu[x]) +','
	masses_munu += '};\n'
	b_munu += '};\n'
	masses_munu = masses_munu.replace(',}','}')
	b_munu = b_munu.replace(',}','}')
	print 2*cr + masses_munu +cr+ b_munu + 2*cr
	print dif_munu


print "\n\n"+'+'*40 + '\n\n'
print 2*cr + masses_comb +cr+ b_comb + 2*cr
print dif_combo
print 2*cr + masses_mumu +cr+ b_mumu + 2*cr
print dif_mumu
print 2*cr + masses_munu +cr+ b_munu + 2*cr
print dif_munu



#beta_mumu = []
#m_mumu = []
#rat = -99.0
#precision = .001

#if do_mumu == 1:
	#kill = 0 
	#for x in range(len(name)):
		#if kill == 1:
			#break
		#rat = 999999.0
		#oldrat = 999999.9	
		#oldbeta = .99
		#beta = 0.0001
		#inc = .2499
		#while abs(rat -1.0) > precision and abs(oldbeta -beta)/oldbeta >.001:
			#if beta>0.9999999:
				#kill = 1
				#break
			#f = open('conf_b_one_'+name[x]+'.cfg','w')
			#f.write( 'imax    1'+cr )
			#f.write(  'jmax    1' +cr)
			#f.write(  'kmax    2'+cr)
			#f.write(  'bin   1  '+cr)
			#f.write(  'observation   '+str(data[x])+cr)
			#f.write(  'bin 1 1  '+cr)
			#f.write(  'process ' +name[x]+ ' bkg_all  '+cr)
			#f.write(  ' process 0 1'+cr)
			#f.write(  'rate  '+str(beta*beta*float(sig[x])) + '  '+str(bg[x]) +cr)
			#f.write(  'lumi lnN  1.06 -  '+cr)
			##f.write(  'allsys lnN ' + str( ( ( float(sig[x]))  + float(sigerr[x]) ) /float(sig[x]) ) +'  ' + str( ( ( float(bg[x]))  + float(bgerr[x]) ) /float(bg[x]) ) +cr )
			#f.write(  'allsys lnN ' + str( ( ( float(sig[x]))  + float(sigerr[x]) ) /float(sig[x]) ) +'  ' + '1.3' +cr )
			
			#f.close()
			#limit = os.popen('combine -d conf_b_one_'+name[x]+'.cfg -M BayesianSimple').readlines()
			#for line in limit:
				#if 'r <' in line:
					#oline = line
					#line = line.split(' ')
					#for i in range(len(line)):
						#if '<' in line[i]:
							#print name[x]+', beta = '+str(beta)+' :  ' +oline
							#goodline = line
			#line = goodline	
			#for i in range(len(line)):
				#if  line[i]=='r' and line[i+1] == '<' :
					#oldrat = rat
					#rat = float(line[i+2].replace(';',''))
					#if (oldrat-1.0)*(rat-1.0)<0:
						#inc = -inc/2.0 		
					#oldbeta = beta	
					#beta = beta + inc
					#if abs(rat -1.0) < precision or abs(oldbeta -beta)/oldbeta <.001:
						#print '***   Limit found for '+name[x]+' :  beta = '+str(oldbeta)
						#beta_mumu.append(oldbeta)
						#m_mumu.append(float(name[x].replace('LQ','')))
	#print m_mumu
	#print beta_mumu
	
	#masses_one += str(len(m_mumu))+'] = {'
	#b_one += str(len(m_mumu))+'] = {'
	#for x in range(len(m_mumu)):
		#masses_one += str(m_mumu[x]) +','
		#b_one += str(beta_mumu[x]) +','
	#masses_one += '};\n'
	#b_one += '};\n'
	#masses_one = masses_one.replace(',}','}')
	#b_one = b_one.replace(',}','}')
	#print 2*cr + masses_one +cr+ b_one + 2*cr

#beta_munu = []
#m_munu = []
#rat = -99.0
#precision = .001

#if do_munu == 1:
	#kill = 0 
	#for x in range(len(name)):
		#if kill == 1:
			#break
		#rat = 999999.0
		#oldrat = 999999.9	
		#oldbeta = .99
		#beta = 0.0001
		#inc = .2499
		#while abs(rat -1.0) > precision and abs(oldbeta -beta)/oldbeta >.001:
			#if beta>0.9999999:
				#kill = 1
				#break
			#f = open('conf_b_half_'+name[x]+'.cfg','w')
			#f.write( 'imax    1'+cr )
			#f.write(  'jmax    1' +cr)
			#f.write(  'kmax    2'+cr)
			#f.write(  'bin   1  '+cr)
			#f.write(  'observation   '+str(data2[x])+cr)
			#f.write(  'bin 1 1  '+cr)
			#f.write(  'process ' +name[x]+ ' bkg_all  '+cr)
			#f.write(  ' process 0 1'+cr)
			#f.write(  'rate  '+str(4.0*beta*(1-beta)*float(sig2[x])) + '  '+str(bg2[x]) +cr)
			#f.write(  'lumi lnN  1.06 -  '+cr)
			##f.write(  'allsys lnN ' + str( ( ( float(sig2[x]))  + float(sigerr2[x]) ) /float(sig2[x]) ) +'  ' + str( ( ( float(bg2[x]))  + float(bgerr2[x]) ) /float(bg2[x]) ) +cr )
			#f.write(  'allsys lnN ' + str( ( ( float(sig2[x]))  + float(sigerr2[x]) ) /float(sig2[x]) ) +'  ' + '1.3' +cr )

			#f.close()
			#limit = os.popen('combine -d conf_b_half_'+name[x]+'.cfg -M BayesianSimple').readlines()
			#for line in limit:
				#if 'r <' in line:
					#oline = line
					#line = line.split(' ')
					#for i in range(len(line)):
						#if '<' in line[i]:
							#print name[x]+', beta = '+str(beta)+' :  ' +oline
							#goodline = line
			#line = goodline	
			#for i in range(len(line)):
				#if  line[i]=='r' and line[i+1] == '<' :
					#oldrat = rat
					#rat = float(line[i+2].replace(';',''))
					#oldbeta = beta
					#if (oldrat-1.0)*(rat-1.0)<0:
						#inc = -inc/2.0 		
					#beta = beta + inc	
					#if abs(rat -1.0) < precision or abs(oldbeta -beta)/beta <.001:
						#print '***   Limit found for '+name[x]+' :  beta = '+str(oldbeta)
						#beta_munu.append(oldbeta)
						#m_munu.append(float(name[x].replace('LQ','')))	
						
	#for x in range(len(m_munu)):
		#m_munu.append((m_munu[-1-2*x])+0.0001)
		#beta_munu.append(1-beta_munu[-1-2*x])
	#print m_munu
	#print beta_munu
	
	#masses_half += str(len(m_munu))+'] = {'
	#b_half += str(len(m_munu))+'] = {'
	#for x in range(len(m_munu)):
		#masses_half += str(m_munu[x]) +','
		#b_half += str(beta_munu[x]) +','
	#masses_half += '};\n'
	#b_half += '};\n'
	#masses_half = masses_half.replace(',}','}')
	#b_half = b_half.replace(',}','}')
	#print 2*cr + masses_half+cr + b_half + 2*cr



#print 2*cr + masses_comb +cr+ b_comb + 2*cr
#print 2*cr + masses_one +cr+ b_one + 2*cr
#print 2*cr + masses_half +cr+ b_half + 2*cr
