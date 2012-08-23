import os,sys
import math
import random


# Directory where root files are kept and the tree you want to get root files from

NormalDirectory = '~/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Aug15_2012_08_16_05_27_58/SummaryFiles'
JetScaleUpDirectory = '~/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Aug15_JetScaleUp_2012_08_16_08_01_06/SummaryFiles'
JetScaleDownDirectory = '~/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Aug15_JetScaleDown_2012_08_16_08_45_31/SummaryFiles'
MuScaleUpDirectory = '~/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Aug19V1_MuScaleUp_2012_08_20_15_40_10/SummaryFiles'
MuScaleDownDirectory = '~/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Mar13_MuScaleDown_2012_08_14_08_10_51/SummaryFiles'
JetSmearDirectory = '~/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Mar13_JetSmear_2012_08_14_09_59_23/SummaryFiles'
JetSclaeDirectory = '~/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Aug19V1_MuSmear_2012_08_20_03_56_29/SummaryFiles'

TreeName = "PhysicalVariables"

passfilter = "*(pass_HBHENoiseFilter>0.5)*(pass_passBeamHaloFilterTight>0.5)*(pass_isTrackingFailure>0.5)"

lumi = 4980.0

NormalWeightMuMu = str(lumi)+'*0.9936*weight_pileup4p7fb_higgs'
NormalWeightMuNu = str(lumi)+'*0.92*weight_pileup4p7fb_higgs'


preselectionmumu = '((Pt_muon1>40)*(Pt_muon2>40)*(Pt_pfjet1>40)*(Pt_pfjet2>40)*(ST_pf_mumu>250)*(deltaR_muon1muon2>0.5)*(M_muon1muon2>50)*((abs(Eta_muon1)<2.1)&&(abs(Eta_muon2)<2.1)))'
preselectionmunu = '((Pt_muon1>40)*((Pt_muon2<40.0)*(MET_pf>55)*(Pt_pfjet1>40)*(Pt_pfjet2>40)*(Pt_HEEPele1<40.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(abs(deltaPhi_muon1pfMET)>0.8)*(abs(deltaPhi_pfjet1pfMET)>.5)*(FailIDPFThreshold<25.0)*(deltaR_muon1pfjet1>0.7)*(deltaR_muon1pfjet2>0.7)*(MT_muon1pfMET>50.0))'
preselectionmumu+=passfilter
preselectionmunu+=passfilter


##########################################################################
########      Put all uses of the plotting funcs into main()      ########
##########################################################################

def main():

	jetbinning = [40]
	for x in range(20):
		jetbinning.append(jetbinning[-1]+5*x)

	GetMuMuScaleFactors( NormalWeightMuMu+'*'+preselectionmumu, NormalDirectory, '(M_muon1muon2>80)*(M_muon1muon2<100)*(PFJetCount<3.5)*(MET_pf<50)', '(M_muon1muon2>100)*(M_muon1muon2<130)*(MET_pf>50)')

	# MakeBasicPlot('Pt_pfjet1',"p_{T}(jet_{1}) [GeV]",jetbinning,preselectionmumu,NormalWeight,NormalDirectory,'standard','lljj')
	# MakeBasicPlot('Pt_pfjet2',"p_{T}(jet_{2}) [GeV]",jetbinning,preselectionmumu,NormalWeight,NormalDirectory,'standard','lljj')

	# MakeBasicPlot('Pt_pfjet1',"p_{T}(jet_{1}) [GeV]",jetbinning,preselectionmunu,NormalWeight,NormalDirectory,'standard','lvjj')
	# MakeBasicPlot('Pt_pfjet2',"p_{T}(jet_{2}) [GeV]",jetbinning,preselectionmunu,NormalWeight,NormalDirectory,'standard','lvjj')

	

####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

version_name = 'Testing'
signal = 'LQToCMu_M_250'

for n in range(len(sys.argv)):
	if sys.argv[n]=='-v' or sys.argv[n]=='--version_name':
		if len(sys.argv)<=n+1:
			print 'No version name specified. Exiting.'
			exit()
		version_name=sys.argv[n+1]
	if sys.argv[n]=='-s' or sys.argv[n]=='--signal':
		if len(sys.argv)<=n+1:
			print 'No signal specified. Exiting.'
			exit()
		signal=sys.argv[n+1]

os.system('mkdir Results_'+version_name)

##########################################################################
########            All functions and Details Below               ########
##########################################################################

import math
sys.argv.append( '-b' )
from ROOT import *
gROOT.ProcessLine("gErrorIgnoreLevel = 2001;")
TFormula.SetMaxima(100000,1000,1000000)
import numpy
import math
rnd= TRandom3()
##########################################################################
########              Clean up ROOT  Style                        ########
##########################################################################
gROOT.SetStyle('Plain')
gStyle.SetOptTitle(0)
from array import array
NCont = 50
NRGBs = 5
stops = array("d",[ 0.00, 0.34, 0.61, 0.84, 1.00])
red= array("d",[ 0.00, 0.00, 0.87, 1.00, 0.51 ])
green= array("d",[ 0.00, 0.81, 1.00, 0.20, 0.00 ])
blue= array("d",[ 0.51, 1.00, 0.12, 0.00, 0.00 ])
TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)
gStyle.SetNumberContours(NCont)
##########################################################################
##########################################################################


def FixDrawLegend(legend):
	legend.SetTextFont(132)
	legend.SetFillColor(0)
	legend.SetBorderSize(0)
	legend.Draw()
	return legend

def ConvertBinning(binning):
	binset=[]
	if len(binning)==3:
		for x in range(binning[0]+1):
			binset.append(((binning[2]-binning[1])/(1.0*binning[0]))*x*1.0+binning[1])
	else:
		binset=binning
	return binset

def CreateHisto(name,legendname,tree,variable,binning,selection,style,label):
	binset=ConvertBinning(binning)
	n = len(binset)-1
	hout= TH1D(name,legendname,n,array('d',binset))
	hout.Sumw2()
	tree.Project(name,variable,selection)
	hout.SetFillStyle(style[0])
	hout.SetMarkerStyle(style[1])
	hout.SetMarkerSize(style[2])
	hout.SetLineWidth(style[3])
	hout.SetMarkerColor(style[4])
	hout.SetLineColor(style[4])
	hout.SetFillColor(style[4])
	hout.SetFillColor(style[4])
	# hout.SetMaximum(2.0*hout.GetMaximum())
	hout.GetXaxis().SetTitle(label[0])
	hout.GetYaxis().SetTitle(label[1])
	hout.GetXaxis().SetTitleFont(132)
	hout.GetYaxis().SetTitleFont(132)
	hout.GetXaxis().SetLabelFont(132)
	hout.GetYaxis().SetLabelFont(132)
	return hout

def BeautifyHisto(histo,style,label,newname):
	histo.SetTitle(newname)	
	histo.SetFillStyle(style[0])
	histo.SetMarkerStyle(style[1])
	histo.SetMarkerSize(style[2])
	histo.SetLineWidth(style[3])
	histo.SetMarkerColor(style[4])
	histo.SetLineColor(style[4])
	histo.SetFillColor(style[4])
	histo.SetFillColor(style[4])
	histo.GetXaxis().SetTitle(label[0])
	histo.GetYaxis().SetTitle(label[1])
	histo.GetXaxis().SetTitleFont(132)
	histo.GetYaxis().SetTitleFont(132)
	histo.GetXaxis().SetLabelFont(132)
	histo.GetYaxis().SetLabelFont(132)
	return histo

def BeautifyStack(stack,label):
	stack.GetHistogram().GetXaxis().SetTitleFont(132)
	stack.GetHistogram().GetYaxis().SetTitleFont(132)
	stack.GetHistogram().GetXaxis().SetLabelFont(132)
	stack.GetHistogram().GetYaxis().SetLabelFont(132)
	stack.GetHistogram().GetXaxis().SetTitle(label[0])
	stack.GetHistogram().GetYaxis().SetTitle(label[1])

	return stack

def QuickIntegral(tree,selection):

	h = TH1D('h','h',1,-1,3)
	h.Sumw2()
	tree.Project('h','1.0',selection)
	I = h.GetBinContent(1)
	E = h.GetBinError(1)
	return [I,E]

def QuickEntries(tree,selection):

	h = TH1D('h','h',1,-1,3)
	h.Sumw2()
	tree.Project('h','1.0',selection)
	I = h.GetEntries()
	return [1.0*I, math.sqrt(1.0*I)]

def GetScaleFactors(n1,n2,a1,a2,b1,b2,o1,o2):
	Ra = 1.0
	Rb = 1.0

	for x in range(10):
		Ra = (n1 - Rb*b1 - o1)/(a1)
		Rb = (n2 - Ra*a2 - o2)/(b2) 
	return [Ra, Rb]


def GetStats(List):
	av = 0.0
	n = 1.0*len(List)
	for x in List:
		av += x
	av = av/n
	dev = 0.0
	while True:
		N=0
		dev += 0.00001
		for x in List:
			if abs(x-av)<dev:
				N+= 1
		if N>.68*len(List):
			break
	return (av,dev)

def RR(List):
	return random.gauss(List[0],List[1])


def GetMuMuScaleFactors( selection, FileDirectory, controlregion_1, controlregion_2):
	for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
		exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")

	N1 = QuickEntries(t_SingleMuData,selection + '*' + controlregion_1)
	N2 = QuickEntries(t_SingleMuData,selection + '*' + controlregion_2)

	Z1 = QuickIntegral(t_ZJets_Sherpa,selection + '*' + controlregion_1)
	T1 = QuickIntegral(t_TTBar,selection + '*' + controlregion_1)
	s1 = QuickIntegral(t_SingleTop,selection + '*' + controlregion_1)
	w1 = QuickIntegral(t_WJets_Sherpa,selection + '*' + controlregion_1)
	v1 = QuickIntegral(t_DiBoson,selection + '*' + controlregion_1)

	Z2 = QuickIntegral(t_ZJets_Sherpa,selection + '*' + controlregion_2)
	T2 = QuickIntegral(t_TTBar,selection + '*' + controlregion_2)
	s2 = QuickIntegral(t_SingleTop,selection + '*' + controlregion_2)
	w2 = QuickIntegral(t_WJets_Sherpa,selection + '*' + controlregion_2)
	v2 = QuickIntegral(t_DiBoson,selection + '*' + controlregion_2)

	Other1 = [ s1[0]+w1[0]+v1[0], math.sqrt( s1[1]*s1[1] + w1[1]*w1[1] + v1[1]*v1[1] ) ]
	Other2 = [ s2[0]+w2[0]+v2[0], math.sqrt( s2[1]*s2[1] + w2[1]*w2[1] + v2[1]*v2[1] ) ]

	output = GetScaleFactors( N1[0], N2[0], Z1[0], Z2[0], T1[0], T2[0], Other1[0], Other2[0] )

	zvals = []
	tvals = []

	for x in range(10000):
		variation = (GetScaleFactors(RR(N1),RR(N2),RR(Z1),RR(Z2),RR(T1),RR(T2),Other1[0],Other2[0]))
		zvals.append(variation[0])
		tvals.append(variation[1])

	print GetStats(zvals)
	print GetStats(tvals)



	print output

def MakeBasicPlot(recovariable,xlabel,presentationbinning,selection,weight,FileDirectory,tagname,channel):

	# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
	for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
		exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
	tmpfile = TFile("tmp.root","RECREATE")
	print "\n     Making basic histogram for "+recovariable+". \n"
	# Create Canvas
	c1 = TCanvas("c1","",700,500)
	gStyle.SetOptStat(0)

	# These are teh style parameters for certain plots - [FillStyle,MarkerStyle,MarkerSize,LineWidth,Color]
	MCRecoStyle=[0,20,.00001,1,4]
	DataRecoStyle=[0,20,.7,1,1]
	# X and Y axis labels for plot
	Label=[xlabel,"Events/Bin"]

	WStackStyle=[3007,20,.00001,2,6]
	TTStackStyle=[3005,20,.00001,2,4]
	ZStackStyle=[3004,20,.00001,2,2]
	DiBosonStackStyle=[3006,20,.00001,2,3]
	StopStackStyle=[3008,20,.00001,2,9]
	QCDStackStyle=[3013,20,.00001,2,15]


	
	##############################################################################
	#######      Top Left Plot - Normal Stacked Distributions                #######
	##############################################################################
	c1.cd(1)
	### Make the plots without variable bins!
	hs_rec_WJets=CreateHisto('hs_rec_WJets','W+Jets',t_WJets_Sherpa,recovariable,presentationbinning,selection+'*'+weight,WStackStyle,Label)
	hs_rec_Data=CreateHisto('hs_rec_Data','Data, 5/fb',t_SingleMuData,recovariable,presentationbinning,selection,DataRecoStyle,Label)
	hs_rec_DiBoson=CreateHisto('hs_rec_DiBoson','DiBoson',t_DiBoson,recovariable,presentationbinning,selection+'*'+weight,DiBosonStackStyle,Label)
	hs_rec_ZJets=CreateHisto('hs_rec_ZJets','Z+Jets',t_ZJets_Sherpa,recovariable,presentationbinning,selection+'*'+weight,ZStackStyle,Label)
	hs_rec_TTBar=CreateHisto('hs_rec_TTBar','t#bar{t}',t_TTBar,recovariable,presentationbinning,selection+'*'+weight,TTStackStyle,Label)
	hs_rec_SingleTop=CreateHisto('hs_rec_SingleTop','SingleTop',t_SingleTop,recovariable,presentationbinning,selection+'*'+weight,StopStackStyle,Label)
	# hs_rec_QCDMu=CreateHisto('hs_rec_QCDMu','QCD #mu-enriched [Pythia]',t_QCDMu,recovariable,presentationbinning,selection+'*'+weight,QCDStackStyle,Label)

	if channel == 'lljj':
		SM=[hs_rec_WJets,hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_TTBar,hs_rec_ZJets]

	if channel == 'lvjj':
		SM=[hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar,hs_rec_WJets]
	
	# mcdatascalepres = (1.0*(hs_rec_Data.GetEntries()))/(sum(k.Integral() for k in SM))

	MCStack = THStack ("MCStack","")
	SMIntegral = sum(k.Integral() for k in SM)
	# MCStack.SetMaximum(SMIntegral*100)
		
	for x in SM:
		# x.Scale(mcdatascalepres)
		MCStack.Add(x)
		x.SetMaximum(10*hs_rec_Data.GetMaximum())

	MCStack.Draw("HIST")
	c1.cd(1).SetLogy()

	MCStack=BeautifyStack(MCStack,Label)
	hs_rec_Data.Draw("EPSAME")

	# Create Legend
	FixDrawLegend(c1.cd(1).BuildLegend())
	gPad.RedrawAxis()

	MCStack.SetMinimum(.03333)
	MCStack.SetMaximum(100*hs_rec_Data.GetMaximum())

	c1.Print('Results_'+version_name+'/Basic_'+channel+'_'+recovariable+'_'+tagname+'.pdf')
	c1.Print('Results_'+version_name+'/Basic_'+channel+'_'+recovariable+'_'+tagname+'.png')














main()