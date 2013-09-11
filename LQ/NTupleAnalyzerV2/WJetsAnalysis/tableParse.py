import os
import sys
d = sys.argv[1]
os.system(' python FixFileNames.py '+d)
cont = [d+'/' + x.replace('\n','') for x in os.listdir(d)]

tables = []
systables = []

for c in cont:
	if "FINAL" in c and 'Tex' in c and 'Verbose' not in c:
		tables.append(c)

for c in cont:
	if "FINAL" in c and 'Tex' in c and 'Verbose'  in c:
		systables.append(c)

for t in tables:
	print t
for s in systables:
	print s

pairs = []
for t in tables:
	if "TexCount" not in t:
		continue
	p = []
	p.append(t)
	for tt in tables:
		if tt == t.replace('TexCount','TexXSec'):
			p.append(tt)
	if len(p)==2:
		pairs.append(p)


def TexTableFromPair(pair):
	
	for p in pair:
		if 'TexCount' in p:
			outfile = open(pair[0].replace('TexCount.txt','All.tex'),'w')

	alllines=[]
	for p in pair:	
		for line in open(p):
			line=line.replace('--','-')
			line=line.replace('&','')
			line=line.replace('\\','')
			line=line.replace('pm','\\pm')
			newline = ''
			dcount = 0
			for c in line:
				newline +=(c)
				if c == "$":
					dcount +=1
				if dcount ==2:
					dcount=0
					newline += '&' 
			newline = newline.split("&")
			alllines.append(newline)

	newtable = []
	for a in range(len(alllines)/2):
		c = alllines[a]
		x = alllines[a+len(alllines)/2]
		div = ' & '
		bin = c[0]
		bin = bin.replace('-','')
		bin = bin.replace('$','')
		bin = bin.split()
		outbin = '$'
		outbin += str(round(float(bin[0]),2))
		outbin += '-'
		outbin += str(round(float(bin[1]),2))
		outbin += "$"
		outbin = outbin.replace("$ 0.5 - 1.5 $","1")
		outbin = outbin.replace("$ 1.5 - 2.5 $","2")
		outbin = outbin.replace("$ 2.5 - 3.5 $","3")
		outbin = outbin.replace("$ 3.5 - 4.5 $","4")
		outbin = outbin.replace("$ 4.5 - 5.5 $","5")
		outbin = outbin.replace("$ 5.5 - 6.5 $","6")
		outbin = outbin.replace("$ 6.5 - 7.5 $","7")
		outbin = outbin.replace("$ 7.5 - 8.5 $","8")
		outbin=outbin.replace("$0.5-1.5$","1")
		outbin=outbin.replace("$1.5-2.5$","2")
		outbin=outbin.replace("$2.5-3.5$","3")
		outbin=outbin.replace("$3.5-4.5$","4")
		outbin=outbin.replace("$4.5-5.5$","5")
		outbin=outbin.replace("$5.5-6.5$","6")
		outbin=outbin.replace("$6.5-7.5$","7")
		outbin=outbin.replace("$7.5-8.5$","8")

		newtable.append(outbin+div+c[1]+div+c[2]+div+x[1]+div+x[2]+' \\\\')
	# for n in newtable:
	# 	print n


	vmap = []
	vmap.append(["DeltaPhi_pfjet1muon1","$\\Delta \\phi (jet_1, \mu)$"])
	vmap.append(["DeltaPhi_pfjet2muon1","$\\Delta \\phi (jet_2, \mu)$"])
	vmap.append(["DeltaPhi_pfjet3muon1","$\\Delta \\phi (jet_3, \mu)$"])
	vmap.append(["DeltaPhi_pfjet4muon1","$\\Delta \\phi (jet_4, \mu)$"])
	vmap.append(["Eta_pfjet1","$\\eta(jet_1)$"])
	vmap.append(["Eta_pfjet2","$\\eta(jet_2)$"])
	vmap.append(["Eta_pfjet3","$\\eta(jet_3)$"])
	vmap.append(["Eta_pfjet4","$\\eta(jet_4)$"])
	vmap.append(["MT_muon1MET","$M_T(\\mu,E_T^{miss})$"])
	vmap.append(["PFJet30Count_preexc","Inc Jet Mult"])
	vmap.append(["PFJet30Count","Exc Jet Mult"])
	vmap.append(["Pt_MET","$E_T^{miss}$"])
	vmap.append(["Pt_pfjet1","$p_T(jet_1)$"])
	vmap.append(["Pt_pfjet2","$p_T(jet_2)$"])
	vmap.append(["Pt_pfjet3","$p_T(jet_3)$"])
	vmap.append(["Pt_pfjet4","$p_T(jet_4)$"])
	vmap.append(["HT_pfjets_inc1","$H_T(\\geq 1 jet)$"])
	vmap.append(["HT_pfjets_inc2","$H_T(\\geq 2 jet)$"])
	vmap.append(["HT_pfjets_inc3","$H_T(\\geq 3 jet)$"])
	vmap.append(["HT_pfjets_inc4","$H_T(\\geq 4 jet)$"])

	vmap.append(["Pt_muon1","$p_T(\\mu)$"])
	vmap.append(["Eta_muon1","$\eta(\\mu)$"])

	var = 'Bin'
	for v in vmap:
		if v[0] in str(pair):
			var = v[1]
	outfile.write('\\begin{table}[htb]\n\caption{Bin-by-bin data and uncertainties for the final '+var+' distribution.}\n')
	outfile.write("\\begin{center}\n\\begin{tabular}{|l|ll|ll|}\\hline\n "+var+"     & Predicted Events  & Measured Events & Predicted $\\sigma$ & Measured $\\sigma$ \\\\ \\hline \\hline\n")
	for n in newtable:
		outfile.write(n+'\n')
	outfile.write('\\hline\n\\end{tabular}\n\\end{center}\\end{table}\n')

	outfile.close()

def systablefromfile(sysfile):


	vmap = []
	vmap.append(["DeltaPhi_pfjet1muon1","$\\Delta \\phi (jet_1, \mu)$"])
	vmap.append(["DeltaPhi_pfjet2muon1","$\\Delta \\phi (jet_2, \mu)$"])
	vmap.append(["DeltaPhi_pfjet3muon1","$\\Delta \\phi (jet_3, \mu)$"])
	vmap.append(["DeltaPhi_pfjet4muon1","$\\Delta \\phi (jet_4, \mu)$"])
	vmap.append(["Eta_pfjet1","$\\eta(jet_1)$"])
	vmap.append(["Eta_pfjet2","$\\eta(jet_2)$"])
	vmap.append(["Eta_pfjet3","$\\eta(jet_3)$"])
	vmap.append(["Eta_pfjet4","$\\eta(jet_4)$"])
	vmap.append(["MT_muon1MET","$M_T(\\mu,E_T^{miss})$"])
	vmap.append(["PFJet30Count_preexc","Inc Jet Mult"])
	vmap.append(["PFJet30Count","Exc Jet Mult"])
	vmap.append(["Pt_MET","$E_T^{miss}$"])
	vmap.append(["Pt_pfjet1","$p_T(jet_1)$"])
	vmap.append(["Pt_pfjet2","$p_T(jet_2)$"])
	vmap.append(["Pt_pfjet3","$p_T(jet_3)$"])
	vmap.append(["Pt_pfjet4","$p_T(jet_4)$"])
	vmap.append(["Pt_muon1","$p_T(\\mu)$"])
	vmap.append(["Eta_muon1","$\eta(\\mu)$"])
	vmap.append(["HT_pfjets_inc1","$H_T(\\geq 1 jet)$"])
	vmap.append(["HT_pfjets_inc2","$H_T(\\geq 2 jet)$"])
	vmap.append(["HT_pfjets_inc3","$H_T(\\geq 3 jet)$"])
	vmap.append(["HT_pfjets_inc4","$H_T(\\geq 4 jet)$"])

	print sysfile
	var = 'Bin'
	for v in vmap:
		if v[0] in str(sysfile):
			var = v[1]

	outfile = open(sysfile.replace('TexVerboseError.txt','AllSys.tex'),'w')
	outfile.write('\\begin{table}[htb]\n\caption{Bin-by-bin percent systematic uncertainties on the measured result for the final '+var+' distribution.}\n')
	outfile.write("\\begin{center}\n\\begin{tabular}{|l|cccccccccccc|}\\hline\n "+var+"     &PU    & BG & Lumi   & bTag   & JES    & JER     & MES    & MER   & Stat  & Gen & Evt & MET   \\\\ \\hline \\hline\n")
	for line in open(sysfile,'r'):
		outfile.write(line.replace('--','-'))
	outfile.write('\\hline\n\\end{tabular}\n\\end{center}\n\\end{table}\n')
	outfile.close()


for pair in pairs:
	TexTableFromPair(pair)

for s in systables:
	systablefromfile(s)


print ' -------------- '

cont = [d+'/' + x.replace('\n','') for x in os.popen('ls -1 '+d+'| grep -v Tables | grep tex ')]
cont.sort()
latdoc = d+'/Tables.tex'
os.system('rm '+d+'/Tables.*')


doccont = '\\documentclass[8pt,a4paper]{article}\n\\usepackage[margin=0.25in]{geometry} \n\\begin{document}\n'

for c in cont:
	name = c.split('/')[-1]
	name = name.split('.')[0]
	print name
	# doccont += name.replace('_','\\_') +'\\\\\n'
	doccont += '\\include{'+name+'}\n'
	if 'Sys' in name:
		doccont += '\\clearpage\n\n'

doccont += '\n\\end{document}\n\n'

print doccont

x = open(latdoc,'w')
x.write(doccont)
x.close()

exe = open('mtex.sh','w')
exe.write("#!/bin/sh\n\ncd "+d+"\npdflatex Tables.tex"*2)
exe.close()
os.system('chmod 777 mtex.sh')
os.system('./mtex.sh')
os.system('rm mtex.sh')




import os
import sys
from glob import glob
from array import array
import math
tdir = ''
if len(sys.argv)>=1:
	tdir = sys.argv[1]
else:
	print 'Must specify pyplots directory. Exiting.'
	sys.exit()

sys.argv.append('-b')
from ROOT import *

files = glob(tdir+'/*AllSys.tex')
print files

def FixDrawLegend(legend):
	legend.SetTextFont(42)
	legend.SetTextSize(.04)

	legend.SetFillColor(0)
	legend.SetBorderSize(0)
	legend.Draw()
	return legend

print ' '

def quadsum(vals):
	_s = .0
	for v in vals:
		_s += v*v
	_s = math.sqrt(_s)
	return _s 


def setTDRStyle():

	# For the canvas:
	gStyle.SetCanvasBorderMode(0)
	gStyle.SetCanvasColor(0) # must be kWhite but I dunno how to do that in PyROOT
	gStyle.SetCanvasDefH(600) #Height of canvas
	gStyle.SetCanvasDefW(600) #Width of canvas
	gStyle.SetCanvasDefX(0)   #POsition on screen
	gStyle.SetCanvasDefY(0)


	# For the Pad:
	gStyle.SetPadBorderMode(0);
	# gStyle.SetPadBorderSize(Width_t size = 1);
	gStyle.SetPadColor(0); # kWhite
	gStyle.SetPadGridX(0); #false
	gStyle.SetPadGridY(0); #false
	gStyle.SetGridColor(0);
	gStyle.SetGridStyle(3);
	gStyle.SetGridWidth(1);

	# For the frame:
	gStyle.SetFrameBorderMode(0);
	gStyle.SetFrameBorderSize(1);
	gStyle.SetFrameFillColor(0);
	gStyle.SetFrameFillStyle(0);
	gStyle.SetFrameLineColor(1);
	gStyle.SetFrameLineStyle(1);
	gStyle.SetFrameLineWidth(1);

	# For the histo:
	# gStyle.SetHistFillColor(1);
	# gStyle.SetHistFillStyle(0);
	gStyle.SetHistLineColor(1);
	gStyle.SetHistLineStyle(0);
	gStyle.SetHistLineWidth(1);
	# gStyle.SetLegoInnerR(Float_t rad = 0.5);
	# gStyle.SetNumberContours(Int_t number = 20);

	gStyle.SetEndErrorSize(2);
	#gStyle.SetErrorMarker(20);   #/ I COMMENTED THIS OUT
	gStyle.SetErrorX(0.);

	gStyle.SetMarkerStyle(20);

	#For the fit/function:
	gStyle.SetOptFit(0);
	gStyle.SetFitFormat("5.4g");
	gStyle.SetFuncColor(2);
	gStyle.SetFuncStyle(1);
	gStyle.SetFuncWidth(1);

	#For the date:
	gStyle.SetOptDate(0);
	# gStyle.SetDateX(Float_t x = 0.01);
	# gStyle.SetDateY(Float_t y = 0.01);

	# For the statistics box:
	gStyle.SetOptFile(0);
	gStyle.SetOptStat(0); # To display the mean and RMS:   SetOptStat("mr");
	gStyle.SetStatColor(0); # kWhite
	gStyle.SetStatFont(42);
	gStyle.SetStatFontSize(0.025);
	gStyle.SetStatTextColor(1);
	gStyle.SetStatFormat("6.4g");
	gStyle.SetStatBorderSize(1);
	gStyle.SetStatH(0.1);
	gStyle.SetStatW(0.15);
	# gStyle.SetStatStyle(Style_t style = 1001);
	# gStyle.SetStatX(Float_t x = 0);
	# gStyle.SetStatY(Float_t y = 0);

	# Margins:
	gStyle.SetPadTopMargin(0.05);
	gStyle.SetPadBottomMargin(0.13);
	gStyle.SetPadLeftMargin(0.16);
	#gStyle.SetPadRightMargin(0.12);
	gStyle.SetPadRightMargin(0.02);

	# For the Global title:

	gStyle.SetOptTitle(0);
	gStyle.SetTitleFont(42);
	gStyle.SetTitleColor(1);
	gStyle.SetTitleTextColor(1);
	gStyle.SetTitleFillColor(10);
	gStyle.SetTitleFontSize(0.05);
	# gStyle.SetTitleH(0); # Set the height of the title box
	# gStyle.SetTitleW(0); # Set the width of the title box
	# gStyle.SetTitleX(0); # Set the position of the title box
	# gStyle.SetTitleY(0.985); # Set the position of the title box
	# gStyle.SetTitleStyle(Style_t style = 1001);
	# gStyle.SetTitleBorderSize(2);

	# For the axis titles:

	gStyle.SetTitleColor(1, "XYZ");
	gStyle.SetTitleFont(42, "XYZ");
	gStyle.SetTitleSize(0.06, "XYZ");
	# gStyle.SetTitleXSize(Float_t size = 0.02); # Another way to set the size?
	# gStyle.SetTitleYSize(Float_t size = 0.02);
	gStyle.SetTitleXOffset(0.9);
	gStyle.SetTitleYOffset(1.25);
	# gStyle.SetTitleOffset(1.1, "Y"); # Another way to set the Offset

	# For the axis labels:

	gStyle.SetLabelColor(1, "XYZ");
	gStyle.SetLabelFont(42, "XYZ");
	gStyle.SetLabelOffset(0.007, "XYZ");
	gStyle.SetLabelSize(0.05, "XYZ");

	# For the axis:

	gStyle.SetAxisColor(1, "XYZ");
	gStyle.SetStripDecimals(1); # kTRUE
	gStyle.SetTickLength(0.03, "XYZ");
	gStyle.SetNdivisions(510, "XYZ");
	gStyle.SetPadTickX(1);  # To get tick marks on the opposite side of the frame
	gStyle.SetPadTickY(1);

	# Change for log plots:
	gStyle.SetOptLogx(0);
	gStyle.SetOptLogy(0);
	gStyle.SetOptLogz(0);

	# Postscript options:
	gStyle.SetPaperSize(20.,20.);
	# gStyle.SetLineScalePS(Float_t scale = 3);
	# gStyle.SetLineStyleString(Int_t i, const char* text);
	# gStyle.SetHeaderPS(const char* header);
	# gStyle.SetTitlePS(const char* pstitle);

	# gStyle.SetBarOffset(Float_t baroff = 0.5);
	# gStyle.SetBarWidth(Float_t barwidth = 0.5);
	# gStyle.SetPaintTextFormat(const char* format = "g");
	# gStyle.SetPalette(Int_t ncolors = 0, Int_t* colors = 0);
	# gStyle.SetTimeOffset(Double_t toffset);
	# gStyle.SetHistMinimumZero(kTRUE);

setTDRStyle()



def AnalyzeFile(afile):
	relabels = []
	relabels.append(['Pt_pfjet1','Leading Jet p_{T} [GeV]','p_{T}'])
	relabels.append(['Pt_muon1','Muon p_{T} [GeV]','p_{T}'])
	relabels.append(['N_GoodVertices','N_{Vertices}','N_{Vertices}'])
	relabels.append(['Pt_pfjet2','Second Leading Jet p_{T} [GeV]','p_{T}'])
	relabels.append(['Pt_pfjet3','Third Leading Jet p_{T} [GeV]','p_{T}'])
	relabels.append(['Pt_pfjet4','Fourth Leading Jet p_{T} [GeV]','p_{T}'])
	relabels.append(['Pt_pfjet5','Fifth Leading Jet p_{T} [GeV]','p_{T}'])
	relabels.append(['Eta_pfjet1','Leading Jet #eta','#eta'])
	relabels.append(['Eta_pfjet2','Second Leading Jet #eta','#eta'])
	relabels.append(['Eta_pfjet3','Third Leading Jet #eta','#eta'])
	relabels.append(['Eta_pfjet4','Fourth Leading Jet #eta','#eta'])
	relabels.append(['Eta_pfjet5','Fifth Leading Jet #eta','#eta'])
	relabels.append(['preexc','Jet Count (Inclusive)','N_{Jet}'])
	relabels.append(['PFJet30Count','Jet Count (Exclusive)','N_{Jet}'])
	relabels.append(['MT_muon1METR','M_{T}(#mu,E_{T}^{miss}) [GeV]','M_{T}'])
	relabels.append(['Pt_MET','E_{T}^{miss} [GeV]','E_{T}^{miss}'])
	relabels.append(['DeltaPhi_pfjet1muon1','#Delta #phi(jet_{1},#mu)'	,'#Delta #phi(jet_{1},#mu)'])
	relabels.append(['DeltaPhi_pfjet2muon1','#Delta #phi(jet_{2},#mu)'	,'#Delta #phi(jet_{2},#mu)'])
	relabels.append(['DeltaPhi_pfjet3muon1','#Delta #phi(jet_{3},#mu)'	,'#Delta #phi(jet_{3},#mu)'])
	relabels.append(['DeltaPhi_pfjet4muon1','#Delta #phi(jet_{4},#mu)'	,'#Delta #phi(jet_{4},#mu)'])
	relabels.append(['DeltaPhi_pfjet5muon1','#Delta #phi(jet_{5},#mu)'	,'#Delta #phi(jet_{5},#mu)'])

	label = ''
	for x in relabels:
		if x[0] in afile:
			label = x[1]
	f = open(afile,'r')
	
	headers = ''
	contents = []
	for line in f:
		line = line.replace('hline','')
		line = line.replace('\\','')

		# print line
		if 'Lumi' in line:
			headers = line
		else:
			if '&' in line:
				contents.append(line)

	print ' '
	# print headers
	# for c in contents:
	# 	print c
	nbins = []

	vcont  = []
	for c in contents:
		dolastbin = False
		if c == contents[-1]:
			dolastbin = True
		v = [float(x) for x in c.replace('\n','').split('&')[1:]]
		c = c.split('&')[0]
		c = c.replace('$','')
		c = c.split(' - ')
		nbins.append(float(c[0]))
		vcont.append(v)
		if  dolastbin == True:
			nbins.append(float(c[1]))
	# print nbins

	binset = nbins
	n = len(binset)-1
	T = TH1D('T','Total',n,array('d',binset))
	JJ = TH1D('JJ','JES, JER',n,array('d',binset))
	MM = TH1D('MM','MES, MER, Muon Sel',n,array('d',binset))
	BG = TH1D('BG','Background',n,array('d',binset))
	UN = TH1D('UN','Unfolding',n,array('d',binset))
	Gen = TH1D('Gen','Generator',n,array('d',binset))
	BT = TH1D('BT','BTagging',n,array('d',binset))
	OT = TH1D('OT','All Other',n,array('d',binset))

	allvals = []
	for x in range(len(binset)-1):
		[pu,bg,lu,bt,js,jr,ms,mr,st,gn,hl,mt] = vcont[x]
		nbin = x+1
		_T = math.sqrt(sum([aa*aa for aa in [pu,bg,lu,bt,js,jr,ms,mr,st,gn,hl,mt]]))
		T.SetBinContent(nbin,_T)
		
		_JJ = math.sqrt(js*js+jr*jr)
		_MM = math.sqrt(ms*ms+mr*mr+hl*hl)
		_BG = bg
		_UN = st
		_Gen = gn
		_BT = bt
		# _OT = math.sqrt(lu*lu+pu*pu+hl*hl+mt*mt)

		_OT = quadsum([pu,bg,lu,bt,st,mt])


		JJ.SetBinContent(nbin,_JJ)
		MM.SetBinContent(nbin,_MM)
		BG.SetBinContent(nbin,_BG)
		UN.SetBinContent(nbin,_UN)
		Gen.SetBinContent(nbin,_Gen)
		BT.SetBinContent(nbin,_BT)
		OT.SetBinContent(nbin,_OT)
		# allvals+= [_JJ,_MM,_BG,_UN,_Gen,_BT,_OT]

		allvals += [_JJ,_MM,_Gen,_OT]
	colors = [1,2,28,4,6,7,8,9]
	styles = [1,2,3,4,5,6,7,8]

	# histos = [T,JJ,MM,BG,UN,Gen,BT,OT]
	histos = [T,JJ,MM,Gen,OT]

	# gROOT.SetStyle('Plain')  # Plain white default for plots
	gStyle.SetOptTitle(0) # No titles
	gStyle.SetOptStat(0) # No titles

	c1 = TCanvas("c1","",700,800)
	plotmin = min(allvals)*0.8
	print plotmin
	if plotmin < 0.1:
		plotmin = 0.1
	plotmax = max(allvals)
	plotmax *= 10
	c1.cd(1).SetLogy()


	for x in range(len(histos)):
		histos[x].SetLineColor(colors[x])
		histos[x].SetMarkerColor(colors[x])
		histos[x].SetLineStyle(styles[x])
		histos[x].GetXaxis().SetTitle(label)
		histos[x].SetMarkerSize(0.0)
		histos[x].GetYaxis().SetTitle("Uncertainty (%)")
		histos[x].SetMinimum(plotmin)
		histos[x].SetMaximum(plotmax)
		histos[x].SetLineWidth(2)
		
		histos[x].Draw("HIST"+"SAME"*(x!=0))


	FixDrawLegend(c1.cd(1).BuildLegend())

	pdf = afile.replace('.tex','.pdf')
	png = afile.replace('.tex','.png')
	c1.Print(pdf)
	c1.Print(png)

for f in files:
	AnalyzeFile(f)

for f in files:
	AnalyzeFile(f)	

print ' '