import sys
import os

genvalues = [0.0698146584,0.0698146584,0.0698146584,0.0698146584,0.0698146584,0.0698146584,0.0698146584,0.0698146584,0.0698146584,
              0.0698146584,0.0698146584,0.0630151648,0.0526654164,0.0402754482,0.0292988928,0.0194384503,0.0122016783,0.007207042,
              0.004003637,0.0020278322,0.0010739954,0.0004595759,0.0002229748,0.0001028162,4.58337152809607E-05]


rootfile = sys.argv[1]

f = open('GetDataValues.C','w')
f.write('{\n\n')

f.write('TFile f("'+rootfile+'");\n\n')
f.write('TH1D *h = (TH1D*)f->Get("pileup");\n\n')
#f.write('h->Draw();\n\n')

f.write('int nbinsx = h->GetXaxis()->GetNbins();\n\n')
f.write('Double_t ndat = -1.0;\n\nDouble_t ncenter = -1.0;')
f.write('for (int ibin=0;ibin<nbinsx;ibin++)\n	{\n	 ndat = 1.0*(h->GetBinContent(ibin));\n	 ncenter = 1.0*(h->GetBinCenter(ibin));\n  std::cout<<ncenter<<"  "<<ndat<<std::endl;\n\n  }\n\n')

f.write('	gROOT->Reset(); gROOT->ProcessLine(".q;");')
f.write('\n\n}\n\n')
f.close()

fileinfo = os.popen('root -l GetDataValues.C').readlines()

shortfileinfo = []

for x in  fileinfo:
  shortfileinfo.append(x.replace('\n',''))


datavalues = []

save = 0
for x in shortfileinfo:
  if save:
    center =  x.split()[0]
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


for x in range(len(normvalues)):
  factor =  normvalues[x]/genvalues[x]
  print 'cut_mc += *((N_PileUpInteractions > '+str(x-.5)+')*(N_PileUpInteractions < '+str(x+.5)+')*('+str(factor)+'))'
  



