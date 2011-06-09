import sys
import os

genvalues = [0.0698146584,0.0698146584,0.0698146584,0.0698146584,0.0698146584,0.0698146584,0.0698146584,0.0698146584,0.0698146584,
							0.0698146584,0.0698146584,0.0630151648,0.0526654164,0.0402754482,0.0292988928,0.0194384503,0.0122016783,0.007207042,
							0.004003637,0.0020278322,0.0010739954,0.0004595759,0.0002229748,0.0001028162,4.58337152809607E-05]

a = sys.argv
rootfile = ''
newgenvalues = []
distfile = ''
for x in range(len(a)):
	if a[x] == '-r':
		rootfile = a[x+1]

	if a[x] == '-f':
		distfile = a[x+1]
		os.system('wget '+distfile)
		distfile = distfile.split('/')[-1]
		info = os.popen('cat '+distfile).readlines()
		print info
		for y in info:
			if 'probValue' in y:
				genvalues2 = y
		genvalues2 = genvalues2.split('(')[-1]
		genvalues2 = genvalues2.split(')')[0]
		genvalues2 = genvalues2.split(',')
		for y in genvalues2:
			newgenvalues.append[float(y)]
		os.system('rm '+distfile)
		genvalues = newgenvalues
		
if rootfile == '':
	print 'No root file specified. Specify root file (from estimatePileUpD.py) with "-r rootfile.root".'
	sys.exit()
	
if distfile == '':
	print 'No generator distribution specified. Using default gen values for Spring11 MC'
	os.system('sleep 0')
	
#print rootfile
#print newgenvalues
#print distfile
	

f = open('GetDataValues.C','w')
f.write('{\n\n')

f.write('TFile f("'+rootfile+'");\n\n')
f.write('TH1D *h = (TH1D*)f->Get("pileup");\n\n')
#f.write('h->Draw();\n\n')

f.write('int nbinsx = h->GetXaxis()->GetNbins();\n\n')
f.write('Double_t ndat = -1.0;\n\nDouble_t ncenter = -1.0;')
f.write('for (int ibin=0;ibin<nbinsx;ibin++)\n	{\n	 ndat = 1.0*(h->GetBinContent(ibin));\n	 ncenter = 1.0*(h->GetBinCenter(ibin));\n	std::cout<<ncenter<<"	"<<ndat<<std::endl;\n\n	}\n\n')

f.write('	gROOT->Reset(); gROOT->ProcessLine(".q;");')
f.write('\n\n}\n\n')
f.close()

fileinfo = os.popen('root -l GetDataValues.C').readlines()

shortfileinfo = []

for x in	fileinfo:
	shortfileinfo.append(x.replace('\n',''))


datavalues = []

save = 0

for x in shortfileinfo:
	if save:
		center =	x.split()[0]
		if float(center) >=0:
			datavalues.append(float(x.split()[1]))
	if 'Processing GetDataValues.C' in x:
		save = 1

total = 0.0
for x in datavalues:
	total += x

normvalues = []

n = 0
for x in datavalues:

	if n<len(genvalues):
		normvalues.append(x/total)
	n = n + 1;

print 'cut_mc += "*(";';
makeplus = 1
n = 0
for x in range(len(normvalues)):
	n = n + 1
	factor =	normvalues[x]/genvalues[x]
	print 'cut_mc += "((N_PileUpInteractions > '+str(x-.5)+')*(N_PileUpInteractions < '+str(x+.5)+')*('+str(factor)+'))'+makeplus*'+'+'";'
	if n == (len(normvalues))-1:
		makeplus = 0
print 'cut_mc += ")";'


