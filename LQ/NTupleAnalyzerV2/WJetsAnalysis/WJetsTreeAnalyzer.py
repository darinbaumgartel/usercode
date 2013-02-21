import os

# Directory where root files are kept and the tree you want to get root files from. Normal is for standard analysis, the jet rescaling, jet smearing, muon PT rescaling ,and muon PT smearing. 

QCDDirectory = 'NTupleAnalyzer_V00_02_06_WPlusJets_NonIso_WJetsAnalysis_5fb_Feb05_NonIso_2013_02_08_06_12_50/SummaryFiles'
NormalDirectory = 'NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Feb05_2013_02_06_05_08_21/SummaryFiles'
JetScaleDownDirectory = 'NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Feb05_JetScaleDown_2013_02_06_07_22_32/SummaryFiles'
JetScaleUpDirectory = 'NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Feb05_JetScaleUp_2013_02_06_06_42_50/SummaryFiles'
JetSmearDirectory = 'NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Feb18_JetSmear_2013_02_18_22_54_25/SummaryFiles'
MuScaleDownDirectory = 'NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Feb05_MuScaleDown_2013_02_06_18_02_10/SummaryFiles'
MuScaleUpDirectory = 'NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Feb05_MuScaleUp_2013_02_06_14_34_06/SummaryFiles'
MuSmearDirectory = 'NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Feb05_MuSmear_2013_02_07_00_46_34/SummaryFiles'

# MuSmearDirectory = JetSmearDirectory

# This is the Rivet NTuple for MadGraph
RIVETMadGraph='/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVET/Madgraph_tree_NEvents_93530000.root'
# RIVETSherpa='/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVET/Sherpa_tree_NEvents_152160.root'
RIVETSherpa='/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVET/Sherpa_tree_NEvents_152160.root'

SHERPAFILE=NormalDirectory+'/WJets_Sherpa.root'

# This maps the LQAnalyzer branch names to the Rivet branch names due to my total lack of foresight.
RivetBranchMap=[  ]
RivetBranchMap.append(['Eta_pfjet','etajet'])
RivetBranchMap.append(['Pt_pfjet','ptjet'])
# RivetBranchMap.append(['Phi_pfjet','phijet'])
RivetBranchMap.append(['Eta_muon1','etamuon'])
RivetBranchMap.append(['Pt_muon1','ptmuon'])
# RivetBranchMap.append(['Phi_muon1','phimuon'])
# RivetBranchMap.append(['DeltaPhi_pfjet1muon1','dphijet1muon'])
RivetBranchMap.append(['DeltaPhi_pfjet1muon1','dphijet1muon'])
RivetBranchMap.append(['DeltaPhi_pfjet2muon1','dphijet2muon'])
RivetBranchMap.append(['DeltaPhi_pfjet3muon1','dphijet3muon'])
RivetBranchMap.append(['DeltaPhi_pfjet4muon1','dphijet4muon'])
RivetBranchMap.append(['DeltaPhi_pfjet5muon1','dphijet5muon'])

# RivetBranchMap.append(['pfjet','jet'])
# RivetBranchMap.append(['muon1','muon'])
RivetBranchMap.append(['PFJet30Count','njet_WMuNu'])
RivetBranchMap.append(['MT_muon1MET','mt_mumet'])
RivetBranchMap.append(['Pt_MET','ptmet'])

# This maps the LQAnalyzer branch names to the Rivet branch names due to my total lack of foresight.
GenBranchMap=[  ]
GenBranchMap.append(['Eta_pfjet','Eta_genjet'])
GenBranchMap.append(['Pt_pfjet','Pt_genjet'])
GenBranchMap.append(['PFJet40Count','GenJet40Count'])
GenBranchMap.append(['MT_muon1MET','MT_genmuon1genMET'])
GenBranchMap.append(['Pt_MET','Pt_genMET'])

RivetGenBranchMap = []
RivetGenBranchMap.append(['MT_genmuon1genMET','mt_mumet'])
RivetGenBranchMap.append(['GenJet30Count','njet_WMuNu'])
RivetGenBranchMap.append(['Pt_genMET','ptmet'])
RivetGenBranchMap.append(['Eta_','eta'])
RivetGenBranchMap.append(['Pt_','pt'])
RivetGenBranchMap.append(['DeltaPhi_','dphi'])
RivetGenBranchMap.append(['genjet','jet'])
RivetGenBranchMap.append(['genmuon','muon'])
RivetGenBranchMap.append(['muon1','muon'])


# This is the main (and only) tree in the root files, storing single-valued branches (basically an NTuple, but made as TTree)
TreeName = "PhysicalVariables"

j1="*(Pt_pfjet1>30.0)"
j2="*(Pt_pfjet2>30.0)"
j3="*(Pt_pfjet3>30.0)"
j4="*(Pt_pfjet4>30.0)"
j5="*(Pt_pfjet5>30.0)"

gj1="*(Pt_genjet1>30.0)"
gj2="*(Pt_genjet2>30.0)"
gj3="*(Pt_genjet3>30.0)"
gj4="*(Pt_genjet4>30.0)"
gj5="*(Pt_genjet5>30.0)"


##########################################################################
########      Put all uses of the plotting funcs into main()      ########
##########################################################################

# The main function, called at the end of the script after all other function definitions. If just running analysis on a variable, modify only here.
def main():
	#os.system("rm pyplots/*.*")
	setTDRStyle()
	# Requirements on jet pT, to be implemented when looking at higher jet multiplicities, stored as strings for insertion in TCuts/projections.

	
	
	#MakeUnfoldedPlots('Pt_genmuon1','Pt_muon1',"p_{T}(#mu) [GeV]",[25,45,145],selection,'')
	
	# This is the baseline selection - only one muon, fiducial region, MT in W window.
	selection_noMTcut = '(Pt_muon1>25)*(Pt_muon2<25)*(abs(Eta_muon1)<2.1)'
	basic_selection = '(PFJet30TCHPTCountMod<0.5)*(Pt_muon1>25)*(Pt_muon2<25)*(abs(Eta_muon1)<2.1)*(MT_muon1MET>50)'
	qcd_selection = '(Pt_muon1>45)*(Pt_muon2<45)*(abs(Eta_muon1)<2.1)'

	gen_selection = '(MT_genmuon1genMET>50)*(Pt_genmuon1>25)*(abs(Eta_genmuon1)<2.1)'
	ttbar_selection = '(PFJet30TCHPTCountMod>1.5)*(Muon25Count>0.5)*(HEEPEle25Count>0.5)*(PFJet30Count>1.5)'

	# This is the baseline weight. Central PU (Not modified for systematics), ILum = 4980/pb, muon HLT eff of 0.92.
	weight = '*weight_pu_central*4980*(0.89*abs(Eta_muon1<=0.9) + 0.81*abs(Eta_muon1>0.9))'
	# FullAnalysisWithUncertainty('MT_genmuon1genMET','MT_muon1MET',0,"M_{T}(#mu,E_{T}^{miss}) [GeV]",[50,0,350],[50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,130,150,200],basic_selection,gen_selection,weight,'v')

	# MakeUnfoldedPlots('MT_genmuon1genMET','MT_muon1MET',0,"M_{T}(#mu,E_{T}^{miss}) [GeV]",[50,0,350],[50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,130,150,200],basic_selection,gen_selection,weight,'v',NormalDirectory,'',-1,'standard')
	# sys.exit()
	
	# BTagEffStudy(NormalDirectory,ttbar_selection,gen_selection,weight)


	# # Calling on FullAnalysisWithUncertainty - creates all plots, tables, with unfolding, etc. Examples for Jet PT.  
	# # To detail the arguments:
	# # # # .........................(Gen Variable, Reco Var , X Label, Unfolding Binning, Presentation Binning, selection, weight, switch: 'v'= use ideal variable bins for unfolding, 'c' = use unmodified binning)                                                                                     

	# [JetScaleFactors,JetRescaleString] = GetJetMultFactors('GenJet30Count','PFJet30Count',"N_{Jet}",[9,-1.5,7.5],[5,-0.5,4.5],basic_selection,gen_selection,weight,'c')

	# print JetRescaleString

	# selection = JetRescaleString+'*'+basic_selection
	selection = basic_selection
	FullAnalysisWithUncertainty('DeltaPhi_genjet1genmuon1','DeltaPhi_pfjet1muon1',-0.05,"#Delta#phi(jet_{1},#mu) [GeV]",[20,0,3.1415927],[20,0,3.1415927],selection+j1,gen_selection+gj1,weight,'c')
	FullAnalysisWithUncertainty('DeltaPhi_genjet2genmuon1','DeltaPhi_pfjet2muon1',-0.05,"#Delta#phi(jet_{2},#mu) [GeV]",[15,0,3.1415927],[15,0,3.1415927],selection+j2,gen_selection+gj2,weight,'c')
	FullAnalysisWithUncertainty('DeltaPhi_genjet3genmuon1','DeltaPhi_pfjet3muon1',-0.05,"#Delta#phi(jet_{3},#mu) [GeV]",[10,0,3.1415927],[10,0,3.1415927],selection+j3,gen_selection+gj3,weight,'c')
	FullAnalysisWithUncertainty('DeltaPhi_genjet4genmuon1','DeltaPhi_pfjet4muon1',-0.05,"#Delta#phi(jet_{4},#mu) [GeV]",[6,0,3.1415927],[6,0,3.1415927],selection+j4,gen_selection+gj4,weight,'c')

	FullAnalysisWithUncertainty('Pt_genjet1','Pt_pfjet1',0,"p_{T}(jet_{1}) [GeV]",[40,10,810],[30,50,70,90,110,150,190,250,310,400,750],selection+j1,gen_selection+gj1,weight,'c')
	FullAnalysisWithUncertainty('Pt_genjet2','Pt_pfjet2',0,"p_{T}(jet_{2}) [GeV]",[30,10,610],[30,50,70,90,110,150,190,250,550],selection+j2,gen_selection+gj2,weight,'c')
	FullAnalysisWithUncertainty('Pt_genjet3','Pt_pfjet3',0,"p_{T}(jet_{3}) [GeV]",[25,10,510],[30,50,70,90,110,150,210,450],selection+j3,gen_selection+gj3,weight,'c')
	FullAnalysisWithUncertainty('Pt_genjet4','Pt_pfjet4',0,"p_{T}(jet_{4}) [GeV]",[20,10,410],[30,50,70,90,350],selection+j4,gen_selection+gj4,weight,'c')
	# # # Further examples  - Jet Count, Transverse Mass, MET
	FullAnalysisWithUncertainty('GenJet30Count','PFJet30Count',-1,"N_{Jet}",[8,-.5,7.5],[5 ,-0.5,4.5],basic_selection,gen_selection,weight,'c')	
	FullAnalysisWithUncertainty('MT_genmuon1genMET','MT_muon1MET',25,"M_{T}(#mu,E_{T}^{miss}) [GeV]",[60,10,310],[50,55,60,65,70,75,80,85,90,95,100,110,120,130,145,160,180,200,250],selection,gen_selection,weight,'c')
	FullAnalysisWithUncertainty('Pt_genMET','Pt_MET',-1,"E_{T}^{miss} [GeV]",[50,0,500],[0,10,20,30,40,50,60,70,80,90,100,115,130,150,170,200,250,400],selection,gen_selection,weight,'c')
	# # # # # Further examples - Jet Etas	
	FullAnalysisWithUncertainty('Eta_genjet1','Eta_pfjet1',-2.5,"#eta(jet_{1}) ",[24,-2.4,2.4],[24,-2.4,2.4],selection+j1,gen_selection+gj1,weight,'c')
	FullAnalysisWithUncertainty('Eta_genjet2','Eta_pfjet2',-2.5,"#eta(jet_{2}) ",[24,-2.4,2.4],[24,-2.4,2.4],selection+j2,gen_selection+gj2,weight,'c')
	FullAnalysisWithUncertainty('Eta_genjet3','Eta_pfjet3',-2.5,"#eta(jet_{3}) ",[8,-2.4,2.4],[8,-2.4,2.4],selection+j3,gen_selection+gj3,weight,'c')
	FullAnalysisWithUncertainty('Eta_genjet4','Eta_pfjet4',-2.5,"#eta(jet_{4}) ",[6,-2.4,2.4],[6,-2.4,2.4],selection+j4,gen_selection+gj4,weight,'c')



	# Fu#llAnalysisWithUncertainty will create .txt files in the pyplots directory. This is the final results. 
	# Calling ParseTablesToFinalResults() will read these tables and produce fancier TeX tables and root plots.		
	
	# Get W Renormalization for RIVET
	# WRenorm = GetMTWindowRenormalization('MT_genmuon1genMET',"M_{T}(#mu,E_{T}^{miss}) [GeV]",[40,50,60,70,75,80,85,90,95,100,110,140,200,1000],basic_selection,gen_selection,weight,NormalDirectory,'renormalization_controlregion')[0]
	# WRenorm = "(1.0)"
	# # # print WRenorm

	# ParseTablesToFinalResults(WRenorm,basic_selection)	
	# os.system("convert pyplots/*.png pyplots/AllPlots.pdf")
	# os.system("convert pyplots/*FINAL*Count.png pyplots/AllFinalCountPlots.pdf")
	# os.system("convert pyplots/*FINAL*XSec.png pyplots/AllFinalXSecPlots.pdf")
	# QCDStudy(QCDDirectory,qcd_selection,gen_selection,weight)


	# Below are just some calls of MakeUnfoldedPlots() - this function is called multiple times in FullAnalysisWithUncertainty. 
	# MakeUnfoldedPlots('MT_genmuon1genMET','MT_muon1MET',"M_{T}(#mu,E_{T}^{miss}) [GeV]",[50,50,150],[20,60,100],selection,gen_selection,weight,'v',NormalDirectory,'',2,'standard')
	#sys.exit()
	#MakeUnfoldedPlots('GenJet40Count','PFJet40Count',"N_{Jet}",[12,-1.5,10.5],[5,-0.5,4.5],selection,gen_selection,weight,'c',NormalDirectory,-1,'standard')	
	#MakeUnfoldedPlots('MT_genmuon1genMET','MT_muon1MET',"M_{T}(#mu,E_{T}^{miss}) [GeV]",[50,50,150],[20,60,100],selection,gen_selection,weight,'v',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Pt_genMET','Pt_MET',"E_{T}^{miss} [GeV]",[100,0,430],[15,30,330],selection,gen_selection,weight,'v',NormalDirectory,-1,'standard')

	#MakeUnfoldedPlots('Pt_genjet2','Pt_pfjet2',"p_{T}(jet_{2}) [GeV]",[50,0,500],[26,40,300],selection+j1,gen_selection,weight,'v',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Pt_genjet3','Pt_pfjet3',"p_{T}(jet_{3}) [GeV]",[25,0,500],[13,40,300],selection+j2,gen_selection,weight,'v',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Pt_genjet4','Pt_pfjet4',"p_{T}(jet_{4}) [GeV]",[25,0,500],[13,40,300],selection+j3,gen_selection,weight,'v',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Pt_genjet5','Pt_pfjet5',"p_{T}(jet_{5}) [GeV]",[10,0,500],[5,40,300],selection+j4,gen_selection,weight,'v',NormalDirectory,-1,'standard')

	#MakeUnfoldedPlots('Eta_genjet1','Eta_pfjet1',"#eta(jet_{1}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j1,gen_selection,weight,'c',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Eta_genjet2','Eta_pfjet2',"#eta(jet_{2}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j2,gen_selection,weight,'c',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Eta_genjet3','Eta_pfjet3',"#eta(jet_{3}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j3,gen_selection,weight,'c',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Eta_genjet4','Eta_pfjet4',"#eta(jet_{4}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j4,gen_selection,weight,'c',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Eta_genjet5','Eta_pfjet5',"#eta(jet_{5}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j5,gen_selection,weight,'c',NormalDirectory,-1,'standard')


	# There is also a basic histogram maker... No unfolding, bells, nor whistles.

	#MakeBasicPlot('PFJetCount',"N_{Jet} (Inclusive) [GeV]",[10,-0.5,9.5],selection,gen_selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('PFJetCount',"N_{Jet} (Inclusive) [GeV]",[10,-0.5,9.5],selection,gen_selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('PFJet30Count',"N_{Jet} (Inclusive) [GeV] - 30 GeV Threshold",[10,-0.5,9.5],selection,gen_selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('PFJet40Count',"N_{Jet} (Inclusive) [GeV] - 40 GeV Threshold",[10,-0.5,9.5],selection,gen_selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('MT_muon1MET',"M_{T}(#mu,E_{T}^{miss}) [GeV]",[40,60,160],selection,gen_selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Pt_MET',"E_{T}^{miss} [GeV]",[80,0,400],selection,gen_selection,weight,NormalDirectory,-1,'standard')
	
	#MakeBasicPlot('MET_pfsig',"E_{T}^{miss} Signif [GeV]",[50,0,250],selection,gen_selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Pt_pfjet1',"p_{T}(jet_{1}) [GeV]",[40,40,440],selection+j1,gen_selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Pt_pfjet2',"p_{T}(jet_{2}) [GeV]",[40,40,440],selection+j2,gen_selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Pt_pfjet3',"p_{T}(jet_{3}) [GeV]",[40,40,440],selection+j3,gen_selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Pt_pfjet4',"p_{T}(jet_{4}) [GeV]",[40,40,440],selection+j4,gen_selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Pt_pfjet5',"p_{T}(jet_{5}) [GeV]",[40,40,440],selection+j5,gen_selection,weight,NormalDirectory,-1,'standard')
	
	#MakeBasicPlot('Eta_pfjet1',"#eta(jet_{1})",[24,-2.4,2.4],selection+j1,gen_selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Eta_pfjet2',"#eta(jet_{2})",[24,-2.4,2.4],selection+j2,gen_selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Eta_pfjet3',"#eta(jet_{3})",[24,-2.4,2.4],selection+j3,gen_selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Eta_pfjet4',"#eta(jet_{4})",[24,-2.4,2.4],selection+j4,gen_selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Eta_pfjet5',"#eta(jet_{5})",[24,-2.4,2.4],selection+j5,gen_selection,weight,NormalDirectory,-1,'standard')	
	
	
	# # Just saving tons of PNG output into a single PDF for easier viewing.
	# os.system("convert pyplots/*.png pyplots/AllPlots.pdf")
	# os.system("convert pyplots/*FINAL*Count.png pyplots/AllFinalCountPlots.pdf")
	# os.system("convert pyplots/*FINAL*XSec.png pyplots/AllFinalXSecPlots.pdf")
	

####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

##########################################################################
########            Import libraries                              ########
##########################################################################

import sys
import math
sys.argv.append( '-b' )  # Batch mode - no XWindows - much faster
from ROOT import * # Load root
from glob import * # For table parsing
import csv         # For table parsing
from itertools import izip  # More for table parsing
from array import array    
import numpy
import random

##########################################################################
########              CleanUp/SetUp ROOT                          ########
##########################################################################
gROOT.ProcessLine("gErrorIgnoreLevel = 2001;") # Suppress warnings
TFormula.SetMaxima(100000,1000,1000000) # Allow big strings for tcuts
rnd= TRandom3() # Using TRandom3 for random numbers - no profound impact
gROOT.SetStyle('Plain')  # Plain white default for plots
gStyle.SetOptTitle(0) # No titles
# Below is for setting TH2D color plots to red-blue heat spectrum
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

# Small function to clean up a TLegend style
def FixDrawLegend(legend):
	legend.SetTextFont(42)
	legend.SetFillColor(0)
	legend.SetBorderSize(0)
	legend.Draw()
	return legend

# All binning is passed as variable binning. This converts constant to variable.
def ConvertBinning(binning):
	binset=[]
	if len(binning)==3:
		for x in range(binning[0]+1):
			binset.append(((binning[2]-binning[1])/(1.0*binning[0]))*x*1.0+binning[1])
	else:
		binset=binning
	return binset

# Make basic TH1D for a branch. Projects branch to histo for given binning and selection. 
def CreateHisto(name,legendname,tree,variable,binning,selection,style,label):
	print 'Creating histo for ',name, legendname,
	binset=ConvertBinning(binning) # Assure variable binning
	n = len(binset)-1 # carry the 1
	print '   ... bins created.',
	hout= TH1D(name,legendname,n,array('d',binset)) # Declar empty TH1D
	hout.Sumw2() # Store sum of squares
	print '   ... histo initialized.',
	tree.Project(name,variable,selection) # Project from branch to histo
	print '   ... projection complete.',
	
	# Below is all style. Style is list of arguments passed:
	# [FillStyle, MarkerStyle, MarkerSize, Global Color]
	hout.SetFillStyle(style[0])
	hout.SetMarkerStyle(style[1])
	hout.SetMarkerSize(style[2])
	hout.SetLineWidth(style[3])
	hout.SetMarkerColor(style[4])
	hout.SetLineColor(style[4])
	hout.SetFillColor(style[4])
	hout.SetFillColor(style[4])
	hout.SetMaximum(2.0*hout.GetMaximum()) # Better looking maximum

	# label is a list [XLabel, YLabel]
	hout.GetXaxis().SetTitle(label[0]) 
	hout.GetYaxis().SetTitle(label[1])

	# Good old-fashioned times new roman.
	hout.GetXaxis().SetTitleFont(42)
	hout.GetYaxis().SetTitleFont(42)
	hout.GetXaxis().SetLabelFont(42)
	hout.GetYaxis().SetLabelFont(42)
	print '   ... style modified.',
	print '   ... Histogram complete:',name, legendname


	return hout

# Converts ugly histo to pretty histo, or can change style of any histo.
def BeautifyHisto(histo,style,label,newname):
	histo.SetTitle(newname)	# New legend name

	# And the same style setup as above.
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
	histo.GetXaxis().SetTitleFont(42)
	histo.GetYaxis().SetTitleFont(42)
	histo.GetXaxis().SetLabelFont(42)
	histo.GetYaxis().SetLabelFont(42)
	return histo

# Cleans up a stacked histogram
def BeautifyStack(stack,label):
	# Fix Font
	stack.GetHistogram().GetXaxis().SetTitleFont(42)
	stack.GetHistogram().GetYaxis().SetTitleFont(42)
	stack.GetHistogram().GetXaxis().SetLabelFont(42)
	stack.GetHistogram().GetYaxis().SetLabelFont(42)
	#Fix Label
	stack.GetHistogram().GetXaxis().SetTitle(label[0])
	stack.GetHistogram().GetYaxis().SetTitle(label[1])
	return stack

def Create2DHisto(name,legendname,tree,variable1,variable2,binning,selection,label):
	binset=ConvertBinning(binning) # Variable binning
	n = len(binset)-1 # Carry the 1
	hout= TH2D(name,legendname,n,array('d',binset),n,array('d',binset)) # Declare empty histo
	hout.Sumw2() # Store sum of squares
	tree.Project(name,variable1+":"+variable2,selection) # Project branch1:branch2 with selection 
	# Clean up font and labels.
	hout.GetXaxis().SetTitle(label[0])
	hout.GetYaxis().SetTitle(label[1])
	hout.GetXaxis().SetTitleFont(42)
	hout.GetYaxis().SetTitleFont(42)
	hout.GetXaxis().SetLabelFont(42)
	hout.GetYaxis().SetLabelFont(42)
	
	#Feeble attempt to convert TH2 to integrated TH2 for inclusive jet count. Not working yet.

	#if "Count" in variable:
		#num=0.0
		#err=0.0
		#thisbinx=hout.GetNbinsX()
		#thisbiny=hout.GetNbinsY()

		#for x in range(hout.GetNbinsX()+1):
			#for y in range(hout.GetNbinsY()+1):

				#num+=hout.GetBinContent(thisbinx,thisbiny)
				#if hout.GetXaxis.GetBinCenter(thisbinx) <0:
					#continue
				#if hout.GetYaxis.GetBinCenter(thisbiny) <0:
					#continue
				#err=math.sqrt(hout.GetBinError(thisbinx,thisbiny)*hout.GetBinError(thisbinx,thisbiny) + err*err)
				#hout.SetBinContent(thisbinx,thisbiny,num)
				#hout.SetBinError(thisbin,err)
				#thisbin+=-1	
	
	return hout

# Function to take data histogram and subtract list of background histograms.
def BackgroundSubtractedHistogram(data,backgrounds):
	for b in backgrounds:
		b.Scale(-1)
		data.Add(b)
		b.Scale(-1)
	return data

# This will take a weight MC histogram and create an unweighted data-like histogram. 
# Used for closure test on Madgraph MC. 
def PseudoDataHisto(histo,newname,binning):
	# Convert to var binning
	binset=ConvertBinning(binning)
	# print binset
	N = len(binset)+1
	# Make new histogram
	hout= TH1D(newname,"",N-2,array('d',binset))	
	for n in range(N):
		binval = histo.GetBinCenter(n)
		bincont = int(round(histo.GetBinContent(n)))
		# print n,binval,bincont
		tot = 0
		for ii in range(bincont):
			hout.Fill(binval)
			tot += 1
		# print tot
	return hout

	


	# # Make new histogram
	# hout= TH1D(newname,"",n,array('d',binset))
	
	# # Get bin content and round to integer.
	# bincontent=[]
	# binx=[]
	# for x in range(n):
	# 	bincontent.append(int(round(histo.GetBinContent(x))))
	# 	binx.append(histo.GetBinCenter(x))
	# 	#print x, bincontent[x]

	# # No offset or resolution needed like in smeared histos in next function. Ignore.
	# offset = 0.0
	# resolution = 0.0

	# # Bin ranges. 
	# maxbin=max(binset)
	# minbin=min(binset)
	
	# # Fill.
	# for a in range(len(binx)):
	# 	for y in range(bincontent[a]):
	# 		hout.Fill(binx[a])
	# return hout

# This will take an MC histo and created a smeared data-like histo. For running pseudo-experiments for tau opt.
def SmearOffsetHisto(histo,newname,binning,should_offset):

	# Make variable binning
	binset=ConvertBinning(binning)
	n = len(binset)-1
	
	# empty histogram
	hout= TH1D(newname,"",n,array('d',binset))

	# Get bins of (rounded) integer size
	bincontent=[]
	binx=[]
	for x in range(n):
		bincontent.append(int(round(histo.GetBinContent(x))))
		binx.append(histo.GetBinCenter(x))
		#print '**',n, bincontent[x], binx[x]
	
	# SMearing and offseting histo
	offset = 0.0
	if should_offset==True: # No offset for Eta histos
		offset=abs((numpy.random.normal(1.0,0.05))-1.0)
	resolution = 0.05 # Just 5%, arbitrary choice
	maxbin=max(binset)
	minbin=min(binset)
	
	# Fill output Histogram
	for a in range(len(binx)):
		for y in range(bincontent[a]):
			#print binx[a], resolution
			#print 'numpy.random.normal(',binx[a],(resolution*binx[a])  + (binx[a]==0)*0.1  
			outputx=(numpy.random.normal(binx[a],abs(resolution*binx[a])  + (binx[a]==0)*0.1  ))
			outputx = outputx+ abs(outputx*offset)
			if outputx<=maxbin and outputx>=minbin:
				hout.Fill(outputx)
	#hout.Scale(histo.Integral()/hout.Integral())
	return hout



# Basic SVD for a given Tau. 
def GetBasicSVD(data_histo,Params, tau, binning):
	data=data_histo.Clone() # Data histogram, cloned for safe keeping
	binset=ConvertBinning(binning) # Binning
	n = len(binset)-1 # Carry the 1
	tsvdunf= TSVDUnfold( data_histo, Params[0], Params[1], Params[2] ) # Do the unfolding. Params is [ reco 1D, gen 1D, response 2D]
	unfres = tsvdunf.Unfold( tau )	# Unfold for given tau
	return unfres

# This is the basic SVD with full uncertainty using covariance matrix	
def GetSVD(data_histo,Params, tau, binning):
	# Clone data histogram and get binning
	data=data_histo.Clone() 
	binset=ConvertBinning(binning) 
	n = len(binset)-1
	statcov = TH2D("statcov", "covariance matrix", n, array('d',binset),n,array('d',binset)) # Declare covariance matrix

	# Fill covariance matrix histogram
	for i in range(data.GetNbinsX()):
		 statcov.SetBinContent(i,i,data.GetBinError(i)*data.GetBinError(i)) 
	
	# Get the unfolding object
	tsvdunf= TSVDUnfold( data_histo, statcov, Params[0], Params[1], Params[2] )

	unfres = tsvdunf.Unfold( tau )	
	# Get the distribution of the d to cross check the regularization
	# - choose kreg to be the point where |d_i| stop being statistically significantly >>1
	ddist = tsvdunf.GetD()
	# Get the distribution of the singular values
	svdist = tsvdunf.GetSV()
	# Compute the error matrix for the unfolded spectrum using toy MC
	# using the measured covariance matrix as input to generate the toys
	# 100 toys should usually be enough
	# The same method can be used for different covariance matrices separately.
	ustatcov = tsvdunf.GetUnfoldCovMatrix( statcov, 100 )	
	# Now compute the error matrix on the unfolded distribution originating
	# from the finite detector matrix statistics
	uadetcov = tsvdunf.GetAdetCovMatrix( 100 )	
	# Sum up the two (they are uncorrelated)
	ustatcov.Add( uadetcov )
	#Get the computed regularized covariance matrix (always corresponding to total uncertainty passed in constructor) and add uncertainties from finite MC statistics. 
	utaucov = tsvdunf.GetXtau()
	utaucov.Add( uadetcov )
	#Get the computed inverse of the covariance matrix
	uinvcov = tsvdunf.GetXinv()
	# Errors on unfolding result.
	for i in range(unfres.GetNbinsX()):
		unfres.SetBinError(i, math.sqrt(utaucov.GetBinContent(i,i)))
	
	return [unfres,ddist,svdist]

# This is the "Smart" SVD - optimizes tau on the fly. This version is not used. Pseudoexperiments are used.
def GetSmartSVD(data_histo,Params, binning,forcetau):
	# Clone data histogram and get binning
	data=data_histo.Clone()
	binset=ConvertBinning(binning)
	n = len(binset)-1

	# Declare and fill covariance
	statcov = TH2D("statcov", "covariance matrix", n, array('d',binset),n,array('d',binset))	
	for i in range(data.GetNbinsX()):
		 statcov.SetBinContent(i,i,data.GetBinError(i)*data.GetBinError(i)) 
	
	# Do an initial unfolding.	 	
	tsvdunf_prep= TSVDUnfold( data_histo, statcov, Params[0], Params[1], Params[2] )
	tsvdunf_prep.SetNormalize( kFALSE ) 
	unfres_prep = tsvdunf_prep.Unfold( 1 )	

	# Get the distribution of the d to cross check the regularization
	# - choose kreg to be the point where |d_i| stop being statistically significantly >>1
	ddist_prep = tsvdunf_prep.GetD()
	svdist_prep = tsvdunf_prep.GetSV()

	# 
	OptTau=1
	OptI=1
	OptSV=1
	for i in range(ddist_prep.GetNbinsX()):
		if i<1:
			continue
		if ddist_prep.GetBinContent(i)<1.0:
			OptI=i-2
			OptSV=svdist_prep.GetBinContent(OptI)
			OptTau=int(round(svdist_prep.GetBinContent(OptI)*svdist_prep.GetBinContent(OptI)))
			#OptTau=OptI
			if OptTau==0:
				OptTau=1
			break

	if forcetau>0:
		OptTau=forcetau
	
	tsvdunf= TSVDUnfold( data_histo, statcov, Params[0], Params[1], Params[2] )
	tsvdunf.SetNormalize( kFALSE ) 
	unfres = tsvdunf.Unfold( OptTau )	
	# Get the distribution of the d to cross check the regularization
	# - choose kreg to be the point where |d_i| stop being statistically significantly >>1
	ddist = tsvdunf.GetD()
	ddist.SetTitle("Diagonal Values")
		
	# Get the distribution of the singular values
	svdist = tsvdunf.GetSV()
	svdist.SetTitle("Singular Values")
	# Compute the error matrix for the unfolded spectrum using toy MC
	# using the measured covariance matrix as input to generate the toys
	# 100 toys should usually be enough
	# The same method can be used for different covariance matrices separately.
	ustatcov = tsvdunf.GetUnfoldCovMatrix( statcov, 100 )	
	# Now compute the error matrix on the unfolded distribution originating
	# from the finite detector matrix statistics
	uadetcov = tsvdunf.GetAdetCovMatrix( 100 )	
	# Sum up the two (they are uncorrelated)
	ustatcov.Add( uadetcov )
	#Get the computed regularized covariance matrix (always corresponding to total uncertainty passed in constructor) and add uncertainties from finite MC statistics. 
	utaucov = tsvdunf.GetXtau()
	utaucov.Add( uadetcov )
	#Get the computed inverse of the covariance matrix
	uinvcov = tsvdunf.GetXinv()
	# Errors on unfolding result.
	for i in range(unfres.GetNbinsX()):
		unfres.SetBinError(i, math.sqrt(utaucov.GetBinContent(i,i)))
	
	return [unfres,ddist,svdist,OptTau,OptI]

# Basic function for getting a value of difference between two histos (summed absolute difference of bins)
def SimpleDifFromTwoHistos(histo1,histo2,binning):
	binset=ConvertBinning(binning)
	n = len(binset)-1	
	dif = 0
	for x in range(n+1):
		if x<1:
			continue
		b1 = histo1.GetBinContent(x)
		b2 = histo2.GetBinContent(x)
		if b1>0 and b2>0:
			dif += abs(b1-b2)

	return dif

# This will return N histograms with the smearing and offset from SmearOffsetHisto - for tau optimization
def GetNSmearedHistos(inputhisto,binning,N,should_offset):
	histos=[]
	for x in range(N):
		print 'generating smeared histogram '+str(x),", with input-output integrals:", inputhisto.Integral(), 
		name='hsmear'+str(x)
		histos.append(SmearOffsetHisto(inputhisto,name,binning,should_offset))
		print histos[-1].Integral()
		print " "
	return histos

# For a given tau, get a basic SVD for several smeared histos (above), find the average difference for that tau. 
def TestSVDTau( Params, tau ,histos,binning):
	DifValues = []
	InitialDifs=[]
	N=0.0
	for hsmear in histos:
		N+=1.0
		hsmear
		hunf = GetBasicSVD(hsmear,Params,tau,binning)
		# print "  -- TestInfo: Original unf integral: ",hunf.Integral()
		# hunf.Scale(Params[1].Integral()/hunf.Integral())  # TESTING FOR NJets
		DifValues.append(SimpleDifFromTwoHistos(hunf,Params[1],binning))
		InitialDifs.append(SimpleDifFromTwoHistos(hsmear,Params[1],binning))
		print "  -- TestInfo: [smeared pseudodata, reco MC, gen MC , unf] = ", hsmear.Integral(), Params[0].Integral(), Params[1].Integral(), hunf.Integral()
	#for x in range(len(InitialDifs)):
		#print str((DifValues[x])/(InitialDifs[x]))
	Improvements = []
	for k in range(len(DifValues)):
		if InitialDifs[k]  > 0:
			Improvements.append(100.00*(InitialDifs[k]-DifValues[k])/InitialDifs[k])
		else:
			Improvements.append(0.0)
	# Improvements = [100.00*(InitialDifs[k]-DifValues[k])/InitialDifs[k] for k in range(len(DifValues))]
	DifAverage = sum(Improvements)/(1.0*N)
	return DifAverage
	
# This will test multiple values of tau with TestSVDTau, and find the best tau as the smallest difference of GEN wrt controlled unfoldings.
def FindOptimalTauWithPseudoExpOld(Params,binning,should_offset):
	binset=ConvertBinning(binning)
	n = len(binset)-1
	bestdif = -9999999999 # Dummy values to start
	besttau=9999999999
	n = int(round(n-1))

	# Get N histograms with smearing and offset to use for comparison of tau values
	print "Performing offset: ", should_offset
	histoset=GetNSmearedHistos(Params[0],binning,3,should_offset)
	olddif=99999999999999999999999999
	for t in range(int(round(n))): # Only testing taus up to NBins/2. 
		if t<1: 
			continue
		if t>n-1:
			continue
		dif=(TestSVDTau(Params,t,histoset,binning)) # Get average dif for this tau. 
		print '      ...Initial test of tau = '+str(t)+' '*(5-len(str(t)))+'   Chi Improvement = '+str(round(dif,5))+'%'
		if olddif<0.0 and dif<1.1*olddif and besttau < 9999999 and bestdif>0: # See if difs are diverging - then you can stop the loop
			print "        Best tau found at: tau = "+str(int(besttau))+"  ... Terminating tau serach"
			break		
		if dif>bestdif and dif > 0: # Seeif this tau is best
			bestdif=dif
			besttau=t
		olddif=dif
	if besttau > 9999999:
		besttau = -1
	return besttau # Return the best tau value


# This will test multiple values of tau with TestSVDTau, and find the best tau as the smallest difference of GEN wrt controlled unfoldings.
def FindOptimalTauWithPseudoExp(Params,binning,should_offset):
	binset=ConvertBinning(binning)
	n = len(binset)-1

	binwidth = (1.0*(binset[-1] - binset[0]))/(1.0*len(binset)-1.0)
	_smearwidth = binwidth
	xlength = abs((1.0*(binning[-1]-binning[0])) )
	if (_smearwidth/xlength) < 0.05:
		_smearwidth = xlength*0.05

	hreco = Params[0]
	hgen = Params[1]
	hresp = Params[2]

	cuteff = hreco.Integral()/hgen.Integral()

	smearedhistos = []
	# responses = []

	for trial in range(50):

		hsmear= TH1D('hsmear','hsmear',n,array('d',binset))
		# hresponse= TH2D('hresponse','hresponse',n,array('d',binset),n,array('d',binset))

		print 'Generating pseudo-efficiency based on cut efficiency:',cuteff
		pseudoeff = 2.0
		while pseudoeff>=1.0:
			pseudoeff = rnd.Gaus(cuteff, 0.3*(abs(1-cuteff)))
		print 'Got pseudo-efficiency:',pseudoeff

		offset = 1.0

		if should_offset:
			offset = rnd.Gaus(should_offset, 0.02)
			print "Using distribution offset:",offset


		def PseudoReco(genval,smearwidth,efficiency):
			passcut = rnd.Rndm() < efficiency
			if passcut <0.5: 
				return [passcut, 99]
			else:
				return [passcut, rnd.Gaus(genval, smearwidth)]

		for a in range(hgen.GetNbinsX()+2):
			content = int(round(hgen.GetBinContent(a)))
			if content <1:
				continue

			centralval = hgen.GetBinCenter(a)*offset
			if centralval < binning[0] or centralval > binning[-1]: 
				continue

			mult = 1

			if content > 1000000:
				mult = 1000
				content = int(round(0.001*content))

			if content > 100000 and content <= 1000000:
				mult = 100
				content = int(round(0.01*content))

			if  content > 10000 and content <= 100000:
				mult = 10
				content = int(round(0.1*content))

			for y in range(content):
				
				[cutpass,reco] = PseudoReco(centralval,_smearwidth,pseudoeff)

				if reco < binning[0]: 
					reco = centralval 
				if reco > binning[-1]: 
					reco = centralval 

				if cutpass>0 :
					hsmear.Fill(reco,mult)
					# hresponse.Fill(reco[1],centralval)
		smearedhistos.append(hsmear)
		# responses.append(hresponse)



	bestimprovement = -9999999
	besttau = -1
	bestdif = 9999999999999.9


	for tau in range(int(round(n))): # Only testing taus up to NBins/2. 
		if tau < 1:
			continue
		improvements = []
		difs = []
		for ii in range(len(smearedhistos)):
			hunf = GetBasicSVD(smearedhistos[ii],[hreco,hgen,hresp],tau,binning)
			recdif = SimpleDifFromTwoHistos(smearedhistos[ii],hgen,binning)
			unfdif = SimpleDifFromTwoHistos(hunf,hgen,binning)
			improvementperc = 100.0*((recdif - unfdif )/recdif)
			improvements.append(improvementperc)
			difs.append(unfdif)
		avgimprovement = sum(improvements)/(1.0*len(smearedhistos))
		totaldif = sum(difs)
		print "Tau = ",tau, "Improvement = ",avgimprovement," %"
		print "       ..... DifVal = ",totaldif
		# if avgimprovement>1.0001*bestimprovement:
		if totaldif<0.999*bestdif:
			bestdif = totaldif
			bestimprovement = avgimprovement
			besttau = tau

	if besttau < 0: 
		print "Error: No tau found with positive improvement. Exiting. "
		sys.exit()
	else:
		print "Choosing best tau = ",besttau
		return besttau
				

# Function to take a finely binned histogram and an ideal bin range, and return a new variable
# binning which is has even bin content through the range	
def GetIdealBinStructure(inputhisto,idealbins):
	N=inputhisto.GetSize() # Number of bins in the finely binned input histo
	X = []
	Y=[]
	for x in range(N-1):  # Loop to get the bin content and center of each bin into a list
		if x==0:
			continue
		X.append(inputhisto.GetBinCenter(x))  
		Y.append(inputhisto.GetBinContent(x))
	Width = X[1]-X[0]
	Markers = []
	runsum=0
	
	# Fine the target bin content
	maxbin=inputhisto.Integral()/((1.0*idealbins[0]-2.0))
	
	# Create bin borders by incrementing until the content becomes greater than maxbin
	# Markets indicate bins of the input histo where final bin borders will be
	for y in (Y):
		runsum += y
		if runsum>maxbin:
			Markers.append(1)
			runsum=0
		else:
			Markers.append(0)

	# The rest is just to assign bin edges based on the x axis markers created above.
	CorrectMarkers=[]
	CorrectMarkers=Markers
	CorrectMarkers[0]=1
	
	modbins=[0,0]
	closesttomod=[9999999999999,999999999999]
	OutputBins=[]
	n=-1
	for a in range(len(X)):
		if Markers[a]==1:
			thisbin=X[a]-(1.0*Width)/2.0
			OutputBins.append(thisbin)
			n+=1

	# A couple tricks to handle the first/last bin correctly
	OutputBins.append(X[-1]+Width/2)
	OutputBins.append(idealbins[2])
	OutputBins[0]=inputhisto.GetBinCenter(1)-inputhisto.GetBinWidth(1)/2.0
	OutputBins.reverse()
	OutputBins.append(idealbins[1])
	OutputBins.reverse()
	return OutputBins

# Here we convert a constant bin structure like 5 bins from 0 to 5 i.e. [5,0,5]
# to a variable binning structure i.e. [0,1,2,3,4,5]
# This is just so we can use variable binning everywhere.	
def GetConstBinStructure(binning):
	# If it is already variably binned, return the binning itself.
	if len(binning)>3:
		return binning
	# Otherwise, return a variably binned structure.
	Width=(1.0*(binning[2]-binning[1]))/(1.0*binning[0])
	outputbins=[]
	for x in range(binning[0]+1):
		outputbins.append(binning[1]+Width*x)
	return outputbins

# The purpose of GetRescaling is to take two histograms (histo1 and histo2), given their binning, and return
# a string which can be used to rescale the histo2 to histo1, with errors.
def GetRescaling(histo1, histo2,binning,variable):
	# Initial lists to store histo information
	bincontent1=[]
	bincontent2=[]
	scalefactors=[]
	errors = []
	bindown=[]
	binup=[]

	# Convert binning to vairable binning
	binset=ConvertBinning(binning)
	n = len(binset)-1
	
	# Clone histo1 to the division histogram hdiv, and divide by histo2
	hdiv= histo1.Clone()
	hdiv.Sumw2()
	hdiv.Divide(histo2)
	scalefactors2=[]
	
	# Get the scale factors an errors
	for x in range(histo1.GetNbinsX()+1):
		if x==0:
			continue
		# histo1 and histo2 content
		bincontent1.append(histo1.GetBinContent(x))
		bincontent2.append(histo2.GetBinContent(x))
		# print histo1.GetBinCenter(x), histo2.GetBinCenter(x)
		# print histo1.GetBinContent(x), histo2.GetBinContent(x)
		# print ' ------------------------------------------- '
		scalefactors.append(1.0)
		# Relative errors for hdiv
		if hdiv.GetBinContent(x)>0:
			errors.append(hdiv.GetBinError(x)/hdiv.GetBinContent(x))
		else:
			errors.append(0.0)
		# Scale factors are just hdiv bins
		scalefactors2.append(hdiv.GetBinContent(x))
		if (bincontent2[x-1]>0.0):
			scalefactors[x-1]=(1.0*bincontent1[x-1])/(1.0*bincontent2[x-1])

		# Bin edges	
		bindown.append(histo1.GetBinLowEdge(x))
		binup.append(histo1.GetBinLowEdge(x)+histo1.GetBinWidth(x))
	
	# initiate the rescaling nad error strings
	scalestring='(0.0'	
	errorstring='(0.0'
	for x in range(len(bincontent1)):
		#print str(bindown[x]) + '<' +variable+'<'+ str(binup[x])+' : weight = '+str(round(scalefactors[x],4))+' +- '+str(round(errors[x],4))
		scalestring+=' + '+str(scalefactors[x])+"*("+variable+">"+str(bindown[x])+')*('+variable+'<'+str(binup[x])+')'
		errorstring+=' + '+str(errors[x])+"*("+variable+">"+str(bindown[x])+')*('+variable+'<'+str(binup[x])+')'
	scalestring+=')'
	errorstring+=')'
			
	return [scalestring,errorstring]

# An application of GetRescaling() which gets the rescaling of events as a function of W MT. Used for Rivet.
def GetMTWindowRenormalization(variable,xlabel,fullbinning,selection,gen_selection,weight,FileDirectory,tagname):

	# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
	for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
		fin=f.replace("\n","")
		exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+fin.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
	
	tmpfile = TFile("tmp.root","RECREATE")	
	Label=[xlabel,"Events/Bin"]

	MCRecoStyle=[0,20,.00001,1,4]
	hs_rec_WJets_all=CreateHisto('hs_rec_WJets_all','W+Jets [Reco] (All)',t_WJets_MG,variable,fullbinning,selection+weight,MCRecoStyle,Label)
	hs_rec_WJets_win=CreateHisto('hs_rec_WJets_win','W+Jets [Reco] (Win)',t_WJets_MG,variable,fullbinning,selection+weight+"*(MT_muon1MET>50)*(MT_muon1MET<300)",MCRecoStyle,Label)

	print hs_rec_WJets_all.Integral()
	print hs_rec_WJets_win.Integral()	

	# return [0]
	the_rescaling = GetRescaling(hs_rec_WJets_win, hs_rec_WJets_all, fullbinning,"mt_mumet")

	return the_rescaling


def GetIntErr(histograms):
	Int = 0
	Err = 0
	for h in histograms:
		ii = h.Integral()
		Int += ii
		if ii < 0.001:
			continue
		Err += ii*ii/h.GetEntries()
	Err = math.sqrt(Err)
	return [Int,Err]


def QCDStudy(FileDirectory,selection,gen_selection,weight):

	selection += ('*(Pt_MET<10.0)')
	jetreq = -1

	scalestring_qcd_central = '('
	scalestring_qcd_up = '('
	scalestring_qcd_down = '('

	table = '\n\nJet Multiplicity | Global Scale Factor | Isolation Fake Rate (Data) | Isolation Fake Rate (QCD MC)| Total Rescaling \\\\ \\hline \n'

	for jetcut in ['*(PFJet30Count==0)','*(PFJet30Count==1)','*(PFJet30Count==2)','*(PFJet30Count==3)','*(PFJet30Count==4)','*(PFJet30Count==5)']:
		jetreq += 1
		nonisovals = MakeBasicPlotQCD('Pt_MET',"E_{T}^{miss} [GeV] (Non-Iso, Non-Rescaled, Njet="+str(jetreq)+')',[50,0,10],selection+jetcut,gen_selection,weight,FileDirectory,'qcdunscaled_noniso_'+str(jetreq)+'jet','(1.0)')
		nonisodata = nonisovals[6][0]
		nonisoqcd = nonisovals[5][0]
		nonisobg = nonisovals[0][0]+nonisovals[1][0]+nonisovals[2][0]+nonisovals[3][0]+nonisovals[4][0]
		nonisodata_err = nonisovals[6][1]
		nonisoqcd_err = nonisovals[5][1]
		nonisobg_err = math.sqrt(nonisovals[0][1]**2+nonisovals[1][1]**2+nonisovals[2][1]**2+nonisovals[3][1]**2+nonisovals[4][1]**2)

		isovals = MakeBasicPlotQCD('Pt_MET',"E_{T}^{miss} [GeV] (Isolated, Non-Rescaled, Njet="+str(jetreq)+')',[50,0,10],selection+jetcut+'*(TrkRelIso_muon1<0.1)',gen_selection,weight,FileDirectory,'qcdunscaled_iso_'+str(jetreq)+'jet','(1.0)')
		# isovals = MakeBasicPlotQCD('Pt_MET',"E_{T}^{miss} [GeV]",[50,0,10],selection+jetcut,gen_selection,weight,FileDirectory,'qcdunscaled_iso_'+str(jetreq)+'jet','(1.0)')
		isodata = isovals[6][0]
		isoqcd = isovals[5][0]
		isobg = isovals[0][0]+isovals[1][0]+isovals[2][0]+isovals[3][0]+isovals[4][0]
		isodata_err = isovals[6][1]
		isoqcd_err = isovals[5][1]
		isobg_err = math.sqrt(isovals[0][1]**2+isovals[1][1]**2+isovals[2][1]**2+isovals[3][1]**2+isovals[4][1]**2)

		# FakeRate = isodata/nonisodata
		# FakeRate_err = (math.sqrt((isodata_err/isodata)**2 + (nonisodata_err/nonisodata)**2))*FakeRate

		DataMinusBG = nonisodata - nonisobg
		DataMinusBG_err = math.sqrt(nonisodata_err**2 + nonisobg_err**2)

		IsoDataMinusBG = isodata - isobg
		IsoDataMinusBG_err = math.sqrt(isodata_err**2 + isobg_err**2)


		FakeRate = IsoDataMinusBG/DataMinusBG
		FakeRate_err = (math.sqrt((IsoDataMinusBG_err/IsoDataMinusBG)**2 + (DataMinusBG_err/DataMinusBG)**2))*FakeRate


		ScaleFactor = DataMinusBG/nonisoqcd
		ScaleFactor_err = (math.sqrt((DataMinusBG_err/DataMinusBG)**2 + (nonisoqcd_err/nonisoqcd)**2))*ScaleFactor

		TotalNorm = FakeRate*ScaleFactor
		TotalNorm_err = (math.sqrt((FakeRate_err/FakeRate)**2 + (ScaleFactor_err/ScaleFactor)**2))*TotalNorm

		MCFakeRate = isoqcd/nonisoqcd
		MCFakeRate_err = (math.sqrt((isoqcd_err/isoqcd)**2 + (nonisoqcd_err/nonisoqcd)**2))*MCFakeRate		


		print FakeRate, FakeRate_err
		print MCFakeRate, MCFakeRate_err
		print ScaleFactor, ScaleFactor_err
		print TotalNorm, TotalNorm_err

		scalestring_qcd_central += ' ('+str(round(TotalNorm,4))+')' +jetcut +' +'*(jetreq!=5) + ' )'*(jetreq ==5)
		scalestring_qcd_up += ' ('+str(round(TotalNorm + TotalNorm_err,4))+')' +jetcut +' +'*(jetreq!=5)+ ' )'*(jetreq ==5)
		scalestring_qcd_down += ' ('+str(round(TotalNorm - TotalNorm_err,4))+')' +jetcut +' +'*(jetreq!=5)+ ' )'*(jetreq ==5)

		table += '$N_{jet} =='+str(jetreq) + ' $  &  '
		table += str(round(ScaleFactor,3)) + '\\pm' + str(round(ScaleFactor_err,3)) + ' & '
		table += str(round(FakeRate,3)) + '\\pm' + str(round(FakeRate_err,3)) + ' & '
		table += str(round(MCFakeRate,3)) + '\\pm' + str(round(MCFakeRate_err,3)) + ' & '
		table += str(round(TotalNorm,3)) + '\\pm' + str(round(TotalNorm_err,3)) + ' \\\\ \\hline \n '


		null = MakeBasicPlotQCD('Pt_MET',"E_{T}^{miss} [GeV](Non-Isolated, Global QCD MC Rescaling = "+str(round(ScaleFactor,2))+" , Njet="+str(jetreq)+')',[50,0,10],selection+jetcut,gen_selection,weight,FileDirectory,'qcdscaled_noniso_'+str(jetreq)+'jet','('+str(ScaleFactor)+')' ) 

		ratednonisovals = MakeBasicPlotQCD('Pt_MET',"E_{T}^{miss} [GeV](Isolated, QCD FakeRate*Rescaling = "+str(round(TotalNorm,2))+", Njet="+str(jetreq)+')',[50,0,10],selection+jetcut+'*(TrkRelIso_muon1<0.1)',gen_selection,weight,FileDirectory,'qcdrated_iso_'+str(jetreq)+'jet','('+str(TotalNorm)+')' ) 
		# ratednonisovals = MakeBasicPlotQCD('Pt_MET',"E_{T}^{miss} [GeV]",[50,0,10],selection,gen_selection+jetcut,weight,FileDirectory,'qcdrated_noniso_'+str(jetreq)+'jet','('+str(FakeRate)+')' ) 
		ratednonisodata = ratednonisovals[6][0]
		ratednonisoqcd = ratednonisovals[5][0]
		ratednonisobg = ratednonisovals[0][0]+ratednonisovals[1][0]+ratednonisovals[2][0]+ratednonisovals[3][0]+ratednonisovals[4][0]
		ratednonisodata_err = ratednonisovals[6][1]
		ratednonisoqcd_err = ratednonisovals[5][1]
		ratednonisobg_err = math.sqrt(ratednonisovals[0][1]**2+ratednonisovals[1][1]**2+ratednonisovals[2][1]**2+ratednonisovals[3][1]**2+ratednonisovals[4][1]**2)

		# break

	print table 
	print '\n'
	print scalestring_qcd_central
	print scalestring_qcd_up
	print scalestring_qcd_down
	print '\n'

	os.system('montage pyplots/*qcdrated_iso*png -geometry +2+2 pyplots/qcdratediso.png')
	os.system('montage pyplots/*qcdunscaled_iso*png -geometry +2+2 pyplots/qcdunscalediso.png')
	os.system('montage pyplots/*qcdunscaled_noniso*png -geometry +2+2 pyplots/qcdunscalednoniso.png')
	os.system('montage pyplots/*qcdscaled_noniso*png -geometry +2+2 pyplots/qcdscalednoniso.png')
	os.system('convert -density 800 pyplots/qcdunscalednoniso.png pyplots/qcdscalednoniso.png pyplots/qcdunscalediso.png pyplots/qcdratediso.png    pyplots/QCDStudy.pdf')


	return [scalestring_qcd_central , scalestring_qcd_up , scalestring_qcd_down]


# This is basic plot code for a data vs MC histogram. It is not used much on it's own, but was a precursor to parts of MakeUnfoldedPlots.
def MakeBasicPlotQCD(recovariable,xlabel,presentationbinning,selection,gen_selection,weight,FileDirectory,tagname,qcdrescaling):

	# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
	allfiles = [x.replace('\n','') for x in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines()]
	if 'SingleMuData.root' not in allfiles:
		allfiles.append('SingleMuData.root')
	for f in allfiles:
		fin = f.replace('\n','')
		# file_override is just a means of replacing the normal file with files for shape-varied systematics which have different names.
		exec('t_'+f.replace(".root","")+" = TFile.Open(\""+FileDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")

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


	# print ' declared styles'
	##############################################################################
	#######      Top Left Plot - Normal Stacked Distributions              #######
	##############################################################################
	c1.cd(1)

	qcdselection = selection
	if 'rated' in tagname:
		qcdselection = qcdselection.replace('*(TrkRelIso_muon1<0.1)','')

	### Make the plots without variable bins!
	hs_rec_WJets=CreateHisto('hs_rec_WJets','W+Jets [Reco]',t_WJets_MG,recovariable,presentationbinning,selection+weight,WStackStyle,Label)
	# print 'got wjets', hs_rec_WJets.Integral()
	hs_rec_Data=CreateHisto('hs_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recovariable,presentationbinning,selection,DataRecoStyle,Label)
	# print 'got data', hs_rec_Data.Integral()
	hs_rec_DiBoson=CreateHisto('hs_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recovariable,presentationbinning,selection+weight,DiBosonStackStyle,Label)
	# print 'got DiBoson'
	hs_rec_ZJets=CreateHisto('hs_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recovariable,presentationbinning,selection+weight,ZStackStyle,Label)
	# print 'got ZJets'
	hs_rec_TTBar=CreateHisto('hs_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recovariable,presentationbinning,selection+weight,TTStackStyle,Label)
	# print 'got TTBar'
	hs_rec_SingleTop=CreateHisto('hs_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recovariable,presentationbinning,selection+weight,StopStackStyle,Label)
	# print 'got stop'
	hs_rec_QCDMu=CreateHisto('hs_rec_QCDMu','QCD #mu-enriched [Pythia]',t_QCDMu,recovariable,presentationbinning,qcdselection+weight+'*'+qcdrescaling,QCDStackStyle,Label)
	# print 'got QCD'
	
	# All the standard model contribution histograms
	SM=[hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar,hs_rec_WJets,hs_rec_QCDMu]

	# You could scale the mc but the factor computed below to have Integral(MC) == Integral(data)
	mcdatascalepres = (1.0*(hs_rec_Data.GetEntries()))/(sum(k.Integral() for k in SM))

	# Stack for all the mc
	MCStack = THStack ("MCStack","")
	
	# Integral of the MC
	SMIntegral = sum(k.Integral() for k in SM)
	
	# Set better minima and maxima for a log plot
	MCStack.SetMinimum(1.0)
	MCStack.SetMaximum(SMIntegral*100)
	
	# Add MC to the stack
	for x in SM:
		#x.Scale(mcdatascalepres)
		MCStack.Add(x)
	
	# Draw the stack
	MCStack.Draw("HIST")
	c1.cd(1).SetLogy()

	# Fix up stack style
	MCStack=BeautifyStack(MCStack,Label)
	hs_rec_Data.Draw("EPSAME")

	# Create Legend
	FixDrawLegend(c1.cd(1).BuildLegend())
	gPad.RedrawAxis()

	# Print plot
	c1.Print('pyplots/Basic_'+recovariable+'_'+tagname+'.pdf')
	c1.Print('pyplots/Basic_'+recovariable+'_'+tagname+'.png')

	w = GetIntErr([hs_rec_WJets])
	tt = GetIntErr([hs_rec_TTBar])
	z = GetIntErr([hs_rec_ZJets]) 
	vv = GetIntErr([hs_rec_DiBoson])
	st = GetIntErr([hs_rec_SingleTop]) 
	q = GetIntErr([hs_rec_QCDMu])
	dat = GetIntErr([hs_rec_Data])
	return [w,tt,z,vv,st,q,dat]


def DivWithErr(a,b):
	av = a[0]
	ae = a[1]
	bv = b[0]
	be = b[1]
	div = av/bv
	err = math.sqrt( (ae/av)**2 + (be/bv)**2 )
	err = err*div
	return [div,err]

# def BTagEffStudy(FileDirectory,starting_selection,gen_selection,weight):
# 	# starting_selection += '*(PFJet30Count>1.5)'#*(PFJet30TCHPTCount>0.5)'
# 	[w,tt,ot,dat] = MakeBasicPlot('PFJet30Count',"N_{Jet} (Inclusive) [GeV]",[7,-0.5,6.5],starting_selection,gen_selection,weight,FileDirectory,'_btageff')
# 	[w2,tt2,ot2,dat2] = MakeBasicPlot('PFJet30Count',"N_{Jet} (Inclusive) [GeV]",[7,-0.5,6.5],starting_selection+'*(PFJet30TCHPTCount>1.5)',gen_selection,weight,FileDirectory,'_btageff')

# 	tot = w[0] + tt[0] + ot[0]		
# 	print 'Data-MC Diff:', 100*(tot-dat[0])/dat[0],'%'
# 	print 'Est % tt:', 100*tt[0]/tot,'%'
# 	print 'Est % w:', 100*w[0]/tot,'%'

# 	eff_d = DivWithErr(dat2,dat)
# 	eff_Mc = DivWithErr(tt2,tt)
# 	eff_Rat = DivWithErr(eff_d,eff_Mc)

# 	print 'Est Efficiency in Data: ',eff_d
# 	print 'Est Efficiency in Mc: ',eff_Mc
# 	print 'Eff Ratio: ',eff_Rat



# This is basic plot code for a data vs MC histogram. It is not used much on it's own, but was a precursor to parts of MakeUnfoldedPlots.
def MakeBasicPlot(recovariable,xlabel,presentationbinning,selection,gen_selection,weight,FileDirectory,tagname):

	# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
	allfiles = [x.replace('\n','') for x in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines()]
	if 'SingleMuData.root' not in allfiles:
		allfiles.append('SingleMuData.root')
	for f in allfiles:
		fin = f.replace('\n','')
		# file_override is just a means of replacing the normal file with files for shape-varied systematics which have different names.
		if 'Data' not in fin:
			exec('t_'+f.replace(".root","")+" = TFile.Open(\""+FileDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")
		if 'Data' in fin:
			exec('t_'+f.replace(".root","")+" = TFile.Open(\""+NormalDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")

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


	print ' declared styles'
	##############################################################################
	#######      Top Left Plot - Normal Stacked Distributions              #######
	##############################################################################
	c1.cd(1)

	### Make the plots without variable bins!
	hs_rec_WJets=CreateHisto('hs_rec_WJets','W+Jets [Reco]',t_WJets_MG,recovariable,presentationbinning,selection+weight,WStackStyle,Label)
	print 'got wjets', hs_rec_WJets.Integral()
	hs_rec_Data=CreateHisto('hs_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recovariable,presentationbinning,selection+'*(IsoMu24Pass>0.5)',DataRecoStyle,Label)
	print 'got data', hs_rec_Data.Integral()
	hs_rec_DiBoson=CreateHisto('hs_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recovariable,presentationbinning,selection+weight,DiBosonStackStyle,Label)
	print 'got DiBoson'
	hs_rec_ZJets=CreateHisto('hs_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recovariable,presentationbinning,selection+weight,ZStackStyle,Label)
	print 'got ZJets'
	hs_rec_TTBar=CreateHisto('hs_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recovariable,presentationbinning,selection+weight,TTStackStyle,Label)
	print 'got TTBar'
	hs_rec_SingleTop=CreateHisto('hs_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recovariable,presentationbinning,selection+weight,StopStackStyle,Label)
	print 'got stop'
	hs_rec_QCDMu=CreateHisto('hs_rec_QCDMu','QCD #mu-enriched [Pythia]',t_QCDMu,recovariable,presentationbinning,selection+weight,QCDStackStyle,Label)
	print 'got QCD'
	
	# All the standard model contribution histograms
	SM=[hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar,hs_rec_WJets,hs_rec_QCDMu]

	# You could scale the mc but the factor computed below to have Integral(MC) == Integral(data)
	mcdatascalepres = (1.0*(hs_rec_Data.GetEntries()))/(sum(k.Integral() for k in SM))

	# Stack for all the mc
	MCStack = THStack ("MCStack","")
	
	# Integral of the MC
	SMIntegral = sum(k.Integral() for k in SM)
	
	# Set better minima and maxima for a log plot
	MCStack.SetMinimum(1.0)
	MCStack.SetMaximum(SMIntegral*100)
	
	# Add MC to the stack
	for x in SM:
		#x.Scale(mcdatascalepres)
		MCStack.Add(x)
	
	# Draw the stack
	MCStack.Draw("HIST")
	c1.cd(1).SetLogy()

	# Fix up stack style
	MCStack=BeautifyStack(MCStack,Label)
	hs_rec_Data.Draw("EPSAME")

	# Create Legend
	FixDrawLegend(c1.cd(1).BuildLegend())
	gPad.RedrawAxis()

	# Print plot
	c1.Print('pyplots/Basic_'+recovariable+'_'+tagname+'.pdf')
	c1.Print('pyplots/Basic_'+recovariable+'_'+tagname+'.png')

	w = GetIntErr([hs_rec_WJets])
	tt = GetIntErr([hs_rec_TTBar])
	ot = GetIntErr([hs_rec_ZJets, hs_rec_DiBoson, hs_rec_SingleTop]) 
	dat = GetIntErr([hs_rec_Data])
	return [w,tt,ot,dat]


def DivWithErr(a,b):
	av = a[0]
	ae = a[1]
	bv = b[0]
	be = b[1]
	div = av/bv
	err = math.sqrt( (ae/av)**2 + (be/bv)**2 )
	err = err*div
	return [div,err]

# def BTagEffStudy(FileDirectory,starting_selection,gen_selection,weight):
# 	# starting_selection += '*(PFJet30Count>1.5)'#*(PFJet30TCHPTCount>0.5)'
# 	[w,tt,ot,dat] = MakeBasicPlot('PFJet30Count',"N_{Jet} (Inclusive) [GeV]",[7,-0.5,6.5],starting_selection,gen_selection,weight,FileDirectory,'_btageff')
# 	[w2,tt2,ot2,dat2] = MakeBasicPlot('PFJet30Count',"N_{Jet} (Inclusive) [GeV]",[7,-0.5,6.5],starting_selection+'*(PFJet30TCHPTCount>1.5)',gen_selection,weight,FileDirectory,'_btageff')

# 	tot = w[0] + tt[0] + ot[0]		
# 	print 'Data-MC Diff:', 100*(tot-dat[0])/dat[0],'%'
# 	print 'Est % tt:', 100*tt[0]/tot,'%'
# 	print 'Est % w:', 100*w[0]/tot,'%'

# 	eff_d = DivWithErr(dat2,dat)
# 	eff_Mc = DivWithErr(tt2,tt)
# 	eff_Rat = DivWithErr(eff_d,eff_Mc)

# 	print 'Est Efficiency in Data: ',eff_d
# 	print 'Est Efficiency in Mc: ',eff_Mc
# 	print 'Eff Ratio: ',eff_Rat


def MakeUnfoldedPlots(genvariable,recovariable, default_value, xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,FileDirectory,file_override,tau_override,tagname):


	##############################################################################
	#######     Basic setup - Get the files and trees, designate styles    #######
	##############################################################################

	# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
	allfiles = [x.replace('\n','') for x in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines()]
	if 'SingleMuData.root' not in allfiles:
		allfiles.append('SingleMuData.root')
	for f in allfiles:
		if 'Scale' in f or 'Match' in f:
			continue
		fin = f.replace('\n','')
		# file_override is just a means of replacing the normal file with files for shape-varied systematics which have different names.
		if file_override != '':
			if fin=='ZJets_MG.root':
				fin=fin.replace('_MG.root','_'+file_override+'.root')
			if fin=='WJets_MG.root':
				fin=fin.replace('_MG.root','_'+file_override+'.root')
			if fin=='TTBar.root':
				fin=fin.replace('Bar.root','Jets_'+file_override+'.root')
		if 'Data' not in fin:
			exec('t_'+f.replace(".root","")+" = TFile.Open(\""+FileDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")
		if 'Data' in fin:
			exec('t_'+f.replace(".root","")+" = TFile.Open(\""+NormalDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")


	allqcdfiles = [x.replace('\n','') for x in os.popen('ls '+QCDDirectory+"| grep \".root\"").readlines()]
	if 'SingleMuData.root' not in allqcdfiles:
		allfiles.append('SingleMuData.root')
	for f in allqcdfiles:
		fin = f.replace('\n','')
		if 'QCD' in fin:
			print('t_QCDMuNonIso = TFile.Open(\"'+QCDDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")			
			exec('t_QCDMuNonIso = TFile.Open(\"'+QCDDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")


	QCDScale_Central = '( (0.1834)*(PFJet30Count==0) +(0.1355)*(PFJet30Count==1) + (0.0804)*(PFJet30Count==2) +(0.0564)*(PFJet30Count==3) + (0.0613)*(PFJet30Count==4) +(0.0599)*(PFJet30Count==5) )'


	print 'Doing: ',file_override

	tmpname = "tmp"+str(random.randint(0,1000000))+".root"
	tmpfile = TFile(tmpname,"RECREATE") # temporary root file. Named with random number so you can run several versions of this script at once if needed.
		
	print "\n     Performing unfolding analysis for "+recovariable+" in "+str(binning[0]) +" bins from "+str(binning[1])+" to "+str(binning[2])+"  ... \n"
	# Create Canvas
	c1 = TCanvas("c1","",1200,900)
	c1.Divide(2,2)
	gStyle.SetOptStat(0)

	# These are teh style parameters for certain plots - [FillStyle,MarkerStyle,MarkerSize,LineWidth,Color]
	MCGenStyle=[0,20,.00001,1,2]
	MCGenSmearStyle=[0,20,.00001,1,9]

	MCRecoStyle=[0,21,.00001,1,4]
	DataRecoStyle=[0,21,.6,1,1]
	DataCompStyle=[0,21,0.5,1,6]
	BlankRecoStyle=[0,21,.00001,1,0]
	DataUnfoldedStyle=[0,21,0.5,1,1]
	DataUnfoldedStyle_pseudo=[0,20,0.5,1,9]
	DataUnfoldedStyle_pseudo2=[0,20,0.5,1,2]

	# X and Y axis labels for plot
	Label=[xlabel,"Events/Bin"]

	WStackStyle=[3007,20,.00001,2,6]
	TTStackStyle=[3005,20,.00001,2,4]
	ZStackStyle=[3004,20,.00001,2,2]
	DiBosonStackStyle=[3006,20,.00001,2,3]
	StopStackStyle=[3008,20,.00001,2,9]
	QCDStackStyle=[3013,20,.00001,2,15]

	# Convert to variable binning.
	presentationbinning=ConvertBinning(presentationbinning)


	##############################################################################
	#######     Top Right - Background Subtracted Distributions            #######
	##############################################################################
	c1.cd(2)

	# The selection for the reco variable, constrained to the range the final distribution will be shown.
	# selection+='*('+recovariable+'<'+str(presentationbinning[-1])+')*('+recovariable+'>'+str(presentationbinning[0])+')'
	# The selection for the gen variable. Larger range for the underflow/overflow. '(Pt_genmuon1>1.0)' also demands that a gen-muon is present. 
	# The trees should otherwise be skimmed for a reco muon to be present.
	selection_response=str(gen_selection)#+'*('+genvariable+'<'+str(binning[-1])+')*('+genvariable+'>'+str(binning[1])+')*(Pt_genmuon1>1.0)'

	recomodvariable = recovariable
	# '( ('+selection+')*('+recovariable+ ') + (1-'+selection+')*('+str(default_value)+') )'
	

	genmodvariable = genvariable
	if genvariable == 'GenJet30Count':
		genmodvariable = '(1.0*(Pt_genjet1>30.0 + Pt_genjet2>30.0 + Pt_genjet3>30.0 + Pt_genjet4>30.0 + Pt_genjet5>30.0 ))'

	 # '( ('+gen_selection+')*('+genvariable+ ') + (1-'+gen_selection+')*('+str(default_value)+') )'

	print genmodvariable
	exec('rivetselection = "'+gen_selection+'"')
	exec('rivetmodvariable = "'+genmodvariable+'"')

	print rivetselection
	for x in RivetGenBranchMap:
		if x[0] in rivetselection:
			rivetselection = rivetselection.replace(x[0],x[1])
		if x[0] in rivetmodvariable:
			rivetmodvariable = rivetmodvariable.replace(x[0],x[1])

	
	nrivet = (RIVETMadGraph.split('_')[-1]).replace('.root','')+'.0'
	rivetselection = 'evweight*(31314*4980.0/'+nrivet+')*'+rivetselection
	t_rivet = TFile.Open(RIVETMadGraph,'READ').Get('RivetTree')
	print rivetselection
	print rivetmodvariable
	# print recomodvariable
	# Get optimal variable binning binning
	varbinning=GetConstBinStructure(binning)
	if (optvar=="v" or optvar=="V"):
		print 'Getting optimal binning...'
		varbinning=GetIdealBinStructure(CreateHisto('h_forrebin_WJets','temptest',t_WJets_MG,recomodvariable,[100000*len(presentationbinning),presentationbinning[0],presentationbinning[-1]],selection+weight,MCGenStyle,Label),binning)

	nvbin = len(varbinning)
	vbinmin = 1
	vbinmax = nvbin-1

	npbin = len(presentationbinning)
	pbinmin = 1
	pbinmax = npbin-1

	# WJets Gen + Reco

	shapesysnames = ['scaleup','scaledown','matchup','matchdown']

	if tagname in shapesysnames:
		print ' ################### SHAPE SYS, USING MODIFIED SAMPLE ##########################'
		h_gen_WJets=CreateHisto('h_gen_WJets','W+Jets [Truth]',t_WJets_MG,genmodvariable,varbinning,gen_selection+weight,MCGenStyle,Label)
	else:
		h_gen_WJets=CreateHisto('h_gen_WJets','W+Jets [Truth]',t_rivet,rivetmodvariable,varbinning,rivetselection,MCGenStyle,Label)
	# '(MT_genmuon1genMET>50)*(Pt_genmuon1>25)*(abs(Eta_genmuon1)<2.1)'
		h_gen_WJets_aod=CreateHisto('h_gen_WJets_aod','W+Jets [Truth]',t_WJets_MG,genmodvariable,varbinning,'(MT_genmuon1genMET>50)*(Pt_genmuon1>25)*(abs(Eta_genmuon1)<2.1)'+weight,MCGenStyle,Label)
	h_rec_WJets=CreateHisto('h_rec_WJets','W+Jets [Reco]',t_WJets_MG,recomodvariable,varbinning,selection+weight,MCRecoStyle,Label)


	print "WJETS AOD:", h_gen_WJets_aod.Integral(), h_gen_WJets_aod.GetEntries()
	print "WJETS RIV:", h_gen_WJets.Integral(), h_gen_WJets.GetEntries()
	print "WJETS REC:", h_rec_WJets.Integral(), h_rec_WJets.GetEntries()
	# Data
	h_rec_Data=CreateHisto('h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,varbinning,selection+'*(IsoMu24Pass>0.5)',DataRecoStyle,Label)
	# Other Backgrounds
	h_rec_DiBoson=CreateHisto('h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,varbinning,selection+weight,DiBosonStackStyle,Label)
	h_rec_ZJets=CreateHisto('h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,varbinning,selection+weight,ZStackStyle,Label)
	h_rec_TTBar=CreateHisto('h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,varbinning,selection+weight,TTStackStyle,Label)
	h_rec_SingleTop=CreateHisto('h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,varbinning,selection+weight,StopStackStyle,Label)
	# h_rec_QCDMu=CreateHisto('h_rec_QCDMu','QCD #mu-enriched [Pythia]',t_QCDMu,recomodvariable,varbinning,selection+weight,QCDStackStyle,Label)
	h_rec_QCDMu=CreateHisto('h_rec_QCDMu','QCD #mu-enriched [Pythia]',t_QCDMuNonIso,recomodvariable,varbinning,selection+weight+'*'+QCDScale_Central,QCDStackStyle,Label)

	h_rec_Data_pseudo=PseudoDataHisto(h_rec_WJets,'h_rec_PseudoData',varbinning)
	print 'PseudoData Scale Comparison', h_rec_Data_pseudo.Integral(vbinmin,vbinmax), h_rec_WJets.Integral(vbinmin,vbinmax), h_gen_WJets.Integral(vbinmin,vbinmax), h_rec_Data.Integral(vbinmin,vbinmax)
	# sys.exit()
	## Rescaling Factor Calculation, not implemented!
	SM = [h_rec_WJets,h_rec_DiBoson,h_rec_ZJets,h_rec_TTBar,h_rec_SingleTop,h_rec_QCDMu]
	SMInt = sum([k.Integral(vbinmin,vbinmax) for k in SM])
	mcdatascale = (1.0*(h_rec_Data.Integral(vbinmin,vbinmax)))/SMInt
	genmcscale = (h_rec_WJets.Integral(vbinmin,vbinmax)/h_gen_WJets.Integral(vbinmin,vbinmax))

	# Print the scale factors to screen for sanity check.
	print "MC Global Scale Factor: "+str(mcdatascale)
	print "Gen-Reco Scale Factor: "+str(genmcscale)

	## Do the Drawing
	h_gen_WJets.Draw("HIST")	
	h_rec_WJets.Draw("HISTSAME")

	# Create Legend
	FixDrawLegend(c1.cd(2).BuildLegend( 0.5,  0.6,  0.9,  0.88,'' ))
	
	##############################################################################
	#######      Independent Plot - Normal Stacked Distributions                #######
	##############################################################################

	c2 = TCanvas("c2","",700,800)

	cpad1 = TPad( 'cpad1', 'cpad1', 0.0, 0.31, 1.0, 1.0 )#divide canvas into pads
	cpad2 = TPad( 'cpad2', 'cpad2', 0.0, 0.02, 1.0, 0.31 )

	cpad1.SetBottomMargin(0.0)
	cpad1.SetTopMargin(0.1)
	cpad1.SetLeftMargin(0.12)
	cpad1.SetRightMargin(0.1)

	cpad2.SetBottomMargin(0.3)
	cpad2.SetTopMargin(0.0)
	cpad2.SetLeftMargin(0.12)
	cpad2.SetRightMargin(0.1)


	cpad1.Draw()
	cpad2.Draw()

	cpad1.SetLogy()
	cpad1.cd()



	
	### Make the plots without variable bins!
	hs_rec_WJets=CreateHisto('hs_rec_WJets','W+Jets',t_WJets_MG,recovariable,presentationbinning,selection+weight,WStackStyle,Label)
	hs_rec_Data=CreateHisto('hs_rec_Data','Data, 5/fb',t_SingleMuData,recovariable,presentationbinning,selection+'*(IsoMu24Pass>0.5)',DataRecoStyle,Label)
	hs_rec_DiBoson=CreateHisto('hs_rec_DiBoson','DiBoson',t_DiBoson,recovariable,presentationbinning,selection+weight,DiBosonStackStyle,Label)
	hs_rec_ZJets=CreateHisto('hs_rec_ZJets','Z+Jets',t_ZJets_MG,recovariable,presentationbinning,selection+weight,ZStackStyle,Label)
	hs_rec_TTBar=CreateHisto('hs_rec_TTBar','t#bar{t}',t_TTBar,recovariable,presentationbinning,selection+weight,TTStackStyle,Label)
	hs_rec_SingleTop=CreateHisto('hs_rec_SingleTop','SingleTop',t_SingleTop,recovariable,presentationbinning,selection+weight,StopStackStyle,Label)
	hs_rec_QCDMu=CreateHisto('h_rec_QCDMu','QCD',t_QCDMuNonIso,recovariable,presentationbinning,selection+weight+'*'+QCDScale_Central,QCDStackStyle,Label)

	qcdmin = hs_rec_QCDMu.GetMinimum()
	stopmin = hs_rec_SingleTop.GetMinimum()
	plotmin = qcdmin
	if qcdmin < 0.001:
		plotmin =stopmin
	plotmin = 0.5*plotmin
	plotmax = 100*hs_rec_Data.GetMaximum()

	MCStack = THStack ("MCStack","")
	
	MCStack.SetMinimum(plotmin)
	MCStack.SetMaximum(plotmax)

	SM=[hs_rec_QCDMu,hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar,hs_rec_WJets]

	print '\nBin','W','TTbar'
	for nn in range(hs_rec_WJets.GetNbinsX()+1):
		totsm = 0.0
		for ss in SM:
			totsm += ss.GetBinContent(nn)
		print hs_rec_WJets.GetBinCenter(nn),hs_rec_WJets.GetBinContent(nn), hs_rec_TTBar.GetBinContent(nn), totsm
	

	for x in SM + [hs_rec_Data]:
		x.GetYaxis().SetTitleOffset(0.9)

	for x in SM:
		MCStack.Add(x)
	
	# Draw the stack
	MCStack.Draw()

	MCStack.GetYaxis().SetTitleOffset(0.9)
	MCStack.Draw("HIST")
	cpad1.SetLogy()

	cpad1.Update()
	# Make the stack look better.
	MCStack=BeautifyStack(MCStack,Label)

	# Draw the data.
	hs_rec_Data.Draw("EPSAME")

	# Create Legend
	# FixDrawLegend(c1.cd(1).BuildLegend(0.5,  0.6,  0.9,  0.88,''))
	
	leg = TLegend(0.69,0.61,0.86,0.86,"","brNDC");
	leg.SetTextFont(42);
	leg.SetFillColor(0);
	leg.SetBorderSize(0);
	leg.SetTextSize(.03)
	leg.AddEntry(hs_rec_Data)
	ind = -1
	for s in SM:
		leg.AddEntry(SM[ind])
		ind += -1

	leg.Draw()

	# Stamp on top
	sqrts = "#sqrt{s} = 7 TeV";
	l1=TLatex()
	l1.SetTextAlign(12)
	l1.SetTextFont(42)
	l1.SetNDC()
	l1.SetTextSize(0.05)
	l1.DrawLatex(0.22,0.94,"CMS 2011  "+sqrts+" PRELIMINARY ")

	gPad.RedrawAxis()


	############################
	### GO TO SUBPLOT        ###
	############################
	cpad2.cd()
	# pad2.SetGrid()
	cpad2.Draw()


	hs_rec_total=CreateHisto('hs_rec_total','total',t_WJets_MG,recovariable,presentationbinning,selection+weight,WStackStyle,Label)
	hs_rec_total.Sumw2()
	for s in [hs_rec_QCDMu,hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar]:
		hs_rec_total.Add(s)

	hs_rec_ratio=CreateHisto('hs_rec_ratio','Data Ratio',t_SingleMuData,recovariable,presentationbinning,selection+'*(IsoMu24Pass>0.5)',DataRecoStyle,Label)
	hs_rec_ratio.Sumw2()

	hs_rec_ratio.Divide(hs_rec_total)

	unity=TLine(hs_rec_WJets.GetXaxis().GetXmin(), 1.0 , hs_rec_WJets.GetXaxis().GetXmax(),1.0)

	ratmin = 0
	ratmax = 2

	posvals = []
	for b in range(hs_rec_ratio.GetNbinsX()+1):
		if b == 0:
			continue
		val = hs_rec_ratio.GetBinContent(b)
		dev = hs_rec_ratio.GetBinError(b)
		posvals.append(val + dev)
		posvals.append(val-dev)

	if 0.9*min(posvals) >ratmin:
		ratmin = min(posvals) *0.9	
	if 1.1*max(posvals) <ratmax:
		ratmax = 1.1*max(posvals)

	ratmin = round(ratmin,2)
	ratmax = round(ratmax,2)
	hs_rec_ratio.SetMaximum(2)
	hs_rec_ratio.SetMinimum(0)


	hs_rec_ratio.GetXaxis().SetTitle(Label[0])
	hs_rec_ratio.GetYaxis().SetTitle("Data/Theory")
	hs_rec_ratio.GetXaxis().SetTitleOffset(.73);

	hs_rec_ratio.GetYaxis().SetTitleFont(42);
	hs_rec_ratio.GetXaxis().SetTitleSize(.12);
	hs_rec_ratio.GetYaxis().SetTitleSize(.12);
	hs_rec_ratio.GetXaxis().CenterTitle(0);
	hs_rec_ratio.GetYaxis().CenterTitle(1);
	hs_rec_ratio.GetXaxis().SetTitleOffset(0.88);
	hs_rec_ratio.GetYaxis().SetTitleOffset(0.45);
	hs_rec_ratio.GetYaxis().SetLabelSize(.1);
	hs_rec_ratio.GetXaxis().SetLabelSize(.1);


	hs_rec_ratio.Draw("EP")
	unity.Draw("SAME")


	c2.Print('pyplots/'+recovariable+'_'+tagname+'_simplehisto.png')
	c2.Print('pyplots/'+recovariable+'_'+tagname+'_simplehisto.pdf')

	if ('--quickplots' in sys.argv):
		return [0,0,0]


	##############################################################################
	#######      Top Left Plot - Normal Stacked Distributions                #######
	##############################################################################
	c1.cd(1)

	# MCStack = THStack ("MCStack","")
	
	# MCStack.SetMinimum(1.0)
	# MCStack.SetMaximum(SMInt*100)
	
	### Make the plots without variable bins!
	# hs_rec_WJets=CreateHisto('hs_rec_WJets','W+Jets',t_WJets_MG,recovariable,presentationbinning,selection+weight,WStackStyle,Label)
	# hs_rec_Data=CreateHisto('hs_rec_Data','Data, 5/fb',t_SingleMuData,recovariable,presentationbinning,selection,DataRecoStyle,Label)
	# hs_rec_DiBoson=CreateHisto('hs_rec_DiBoson','DiBoson',t_DiBoson,recovariable,presentationbinning,selection+weight,DiBosonStackStyle,Label)
	# hs_rec_ZJets=CreateHisto('hs_rec_ZJets','Z+Jets',t_ZJets_MG,recovariable,presentationbinning,selection+weight,ZStackStyle,Label)
	# hs_rec_TTBar=CreateHisto('hs_rec_TTBar','t#bar{t}',t_TTBar,recovariable,presentationbinning,selection+weight,TTStackStyle,Label)
	# hs_rec_SingleTop=CreateHisto('hs_rec_SingleTop','SingleTop',t_SingleTop,recovariable,presentationbinning,selection+weight,StopStackStyle,Label)
	# hs_rec_QCDMu=CreateHisto('h_rec_QCDMu','QCD',t_QCDMuNonIso,recovariable,presentationbinning,selection+weight+'*'+QCDScale_Central,QCDStackStyle,Label)

	
	# Again, scale factor calculations. Not implemented, just calculated.
	# SM=[hs_rec_QCDMu,hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar,hs_rec_WJets]
	mcdatascalepres = (1.0*(hs_rec_Data.Integral(pbinmin,pbinmax)))/(sum([k.Integral(pbinmin,pbinmax) for k in SM]))
	print 'MC Data Presentation Scale: ',mcdatascalepres
	# Make a stack of SM.
	# for x in SM:
	# 	#x.Scale(mcdatascalepres) 
	# 	MCStack.Add(x)
	
	# Draw the stack
	MCStack.Draw("HIST")
	c1.cd(1).SetLogy()

	# Make the stack look better.
	# MCStack=BeautifyStack(MCStack,Label)

	# Draw the data.
	hs_rec_Data.Draw("EPSAME")

	# Create Legend
	FixDrawLegend(c1.cd(1).BuildLegend(0.7,  0.6,  0.92,  0.88,''))
	gPad.RedrawAxis()
	# c1.cd(1).Print('pyplots/'+recovariable+'_'+tagname+'_simplehisto.png')
	# c1.cd(1).Print('pyplots/'+recovariable+'_'+tagname+'_simplehisto.pdf')


	##############################################################################
	#######      Bottom Left - Gen Versus Reco Response Matrix             #######
	##############################################################################	
	c1.cd(3)

	# 2D Histogram for WJets MC vs Reco - the response matrix.
	h_response_WJets=Create2DHisto('h_response_WJets','ResponseMatrix',t_WJets_MG,genmodvariable,recomodvariable,varbinning,selection+weight,[xlabel+" Reco",xlabel+" Truth"])
	# h_response_WJets.SetMarkerSize(0.2)
	h_response_WJets.Draw("COLZ") # Draw it with color scheme
	# if (optvar=="v" or optvar=="V"): # Set log if using variable binning (i.e. large bin variations)
	# 	c1.cd(3).SetLogx()	
	# 	c1.cd(3).SetLogy()
	# Just some gridlines to show where the presentation binning and underflow/overflow regions are.
	l_bottom=TLine(binning[1], presentationbinning[0] ,binning[2],presentationbinning[0])
	l_top=TLine(binning[1], presentationbinning[-1] ,binning[2],presentationbinning[-1])
	l_left=TLine(presentationbinning[0], binning[1] ,presentationbinning[0],binning[2])
	l_right=TLine(presentationbinning[-1], binning[1] ,presentationbinning[-1],binning[2])
	bounds = [l_bottom,l_top,l_right,l_left]
	
	for x in bounds:
		x.SetLineStyle(2)
		x.Draw("SAME")


	##############################################################################
	#######      Top Right Addition  - UnFolded Distribution               #######
	##############################################################################	
	c1.cd(2)
	# Subtract other backgrounds from Data using the BackgroundSubtractedHistogram function.
	h_rec_Data2= h_rec_Data.Clone()
	h_rec_Data2 = BackgroundSubtractedHistogram(h_rec_Data2,[ h_rec_DiBoson, h_rec_ZJets,h_rec_TTBar,h_rec_SingleTop,h_rec_QCDMu])
	h_rec_Data2 = BeautifyHisto(h_rec_Data2,DataCompStyle,Label,"Data, 5/fb [Reco]")

	# These are the paramters for the unfolding [reco, gen, response]
	Params = [ h_rec_WJets, h_gen_WJets, h_response_WJets]

	# The tau optimization requires some smeared/offset histograms. Offsetting PT makes sense, but Eta does not. 
	# Turn off offsets for Eta distributions.
	should_offset=True
	if "Eta" in recovariable:
		should_offset=False
	print "Using offset? RecoVaraiable = ",recovariable, "should_offset = ",should_offset
	
	# Tau is calculated only for the real unfolding. Systematics use that tau. This allows an overridee of the tau value as an argument.
	if tau_override>0:
		tau=tau_override
	else:
		#tau=2  # For quick tests only!
		tau = FindOptimalTauWithPseudoExp(Params,varbinning,should_offset) # Get the optimal tau value.

	if tau < 0 : 
		print 'FAILED TO FIND OPTIMAL TAU - NO IMPROVEMENT MADE. EXITING.'
		sys.exit()

	# Perform the unfolding. Returns unfolded data histo, some unfolding parameters not currently used
	[h_unf_Data,h_dd,h_sv,optimal_tau,optimal_i] = GetSmartSVD(h_rec_Data2,Params, varbinning,tau)

	# Samme as above, but using pseudo-data from the WJets MC - this is the closure test!
	[h_unf_Data_pseudo,h_dd,h_sv_pseudo,optimal_tau_pseudo,optimal_i_pseudo] = GetSmartSVD(h_rec_Data_pseudo,Params, varbinning,tau)

	# How much would you have to scale the unfolded data to meet the reco data? Should be ~1.
	UnfScale=(h_rec_Data2.Integral(vbinmin,vbinmax)/h_unf_Data.Integral(vbinmin,vbinmax))
	UnfScale_pseudo=(h_rec_Data_pseudo.Integral(vbinmin,vbinmax)/h_unf_Data_pseudo.Integral(vbinmin,vbinmax))

	# print 'Boundary Sanity Check:', h_rec_Data2.GetBinCenter(vbinmin) - 0.5*h_rec_Data2.GetBinWidth(vbinmin)
	# print 'Boundary Sanity Check:', h_unf_Data.GetBinCenter(vbinmin) - 0.5*h_unf_Data.GetBinWidth(vbinmin)
	# print 'Boundary Sanity Check:', h_rec_Data_pseudo.GetBinCenter(vbinmin) - 0.5*h_rec_Data_pseudo.GetBinWidth(vbinmin)
	# print 'Boundary Sanity Check:', h_unf_Data_pseudo.GetBinCenter(vbinmin) - 0.5*h_unf_Data_pseudo.GetBinWidth(vbinmin)

	print 'Data    Rec Integral:',h_rec_Data2.Integral(vbinmin,vbinmax)
	print 'Data    Unf Integral:',h_unf_Data.Integral(vbinmin,vbinmax)
	print 'Closure Unf Integral:',h_rec_Data_pseudo.Integral(vbinmin,vbinmax)
	print 'Closure Unf Integral:',h_unf_Data_pseudo.Integral(vbinmin,vbinmax)

	# sys.exit()

	# Creates plots, with extra label giving the optimal tau and unfolding scale above.
	h_unf_Data = BeautifyHisto(h_unf_Data,DataUnfoldedStyle,Label,"Data, 5/fb [Unfolded, #tau = "+str(optimal_tau)+",R="+str(round(UnfScale,2))+"]")
	h_unf_Data_pseudo = BeautifyHisto(h_unf_Data_pseudo,DataUnfoldedStyle_pseudo,Label,"WJets Closure [Unfolded, #tau = "+str(optimal_tau)+",R="+str(round(UnfScale_pseudo,2))+"]")

	# Using the unfolded data and reeco data, get a rescaling string to convert between the two types of binning.
	[DataRescalingString,DataErrorString] = GetRescaling(h_unf_Data,h_rec_Data2,varbinning,recovariable)
	# Same as above, but for the closure test.
	print ' UNFOLDED, RECO'
	[DataRescalingString_pseudo,DataErrorString_pseudo] = GetRescaling(h_unf_Data_pseudo,h_rec_Data_pseudo,varbinning,recovariable)
	print 'Closure Rescaling:',DataRescalingString_pseudo
	# Prints the unfolding scale as a sanity check
	print "Scaling of Unfolded Dist: "+str(UnfScale)

	# sys.exit()
	# Draw the unfolded data, reco data, and pseudo (closure) data
	h_unf_Data.Draw("EPSAME")
	h_rec_Data2.Draw("EPSAME")
	h_unf_Data_pseudo.Draw("EPSAME")

	# Legend
	FixDrawLegend(c1.cd(2).BuildLegend(0.5,  0.6,  0.9,  0.88,''))

	# This is just a fancy way of getting decent plot axis dimensions
	CompMin = 99999999999999
	CompMax= 0
	for x in range(h_gen_WJets.GetNbinsX()):
		v = h_gen_WJets.GetBinContent(x+1)
		if x>=(h_gen_WJets.GetNbinsX() -1):
			continue
		if v<0.1:
			continue
		if v>999999999:
			continue
		if v<CompMin:
			CompMin=v
		if v>CompMax:
			CompMax=v

	CompMin = 0.8*CompMin
	CompMax = 1.3*CompMax
	if "Eta" in recovariable or 'Count' in recovariable:
		CompMax = 500*CompMax	
	if "DeltaPhi" in recovariable:
		CompMax = 1000*CompMax
	
	leftborder =  TLine( presentationbinning[0],CompMin,presentationbinning[0],CompMax )
	rightborder =  TLine( presentationbinning[-1],CompMin,presentationbinning[-1],CompMax )
	leftborder.SetLineStyle(2)
	rightborder.SetLineStyle(2)
	h_gen_WJets.SetMaximum(CompMax)
	h_gen_WJets.SetMinimum(CompMin)
	leftborder.Draw("SAME")
	rightborder.Draw("SAME")	
	if (optvar=="v" or optvar=="V" or optvar=="c"):
		#c1.cd(2).SetLogx()
		c1.cd(2).SetLogy()
	# if "Pt" in recovariable and 'MET' not in recovariable:
		# c1.cd(2).SetLogx()
	
	c1.cd(3).Update()


	##############################################################################
	#######      Bottom Right - More legible ratio plots                   #######
	##############################################################################	
	c1.cd(4)
	#c1.cd(4).SetLogy()

	# WJets Gen + Reco
	if tagname in shapesysnames:
		h_pres_gen_WJets=CreateHisto('h_pres_gen_WJets','W+Jets MadGraph [Truth/Reco]',t_WJets_MG,genmodvariable,presentationbinning,gen_selection+weight,MCRecoStyle,Label)
	else:
		h_pres_gen_WJets=CreateHisto('h_pres_gen_WJets','W+Jets MadGraph [Truth/Reco]',t_rivet,rivetmodvariable,presentationbinning,rivetselection,MCRecoStyle,Label)

	h_pres_rec_WJets=CreateHisto('h_pres_rec_WJets','W+Jets  MadGraph [Truth/Reco]',t_WJets_MG,recomodvariable,presentationbinning,selection+weight,MCRecoStyle,Label)


	# Data
	h_pres_rec_Data=CreateHisto('h_pres_rec_Data','Data, 5/fb [Unfolded/Reco]',t_SingleMuData,recomodvariable,presentationbinning,selection+'*(IsoMu24Pass>0.5)',DataCompStyle,Label)
	h_pres_rec_Data_err=CreateHisto('h_pres_rec_Data_err','Data, 5/fb [Unfolded/Reco]',t_SingleMuData,recomodvariable,presentationbinning,selection+'*(IsoMu24Pass>0.5)',DataCompStyle,Label)

	h_pres_unf_Data=CreateHisto('h_pres_unf_Data','Data, 5/fb [Unfolded/Reco]',t_SingleMuData,recomodvariable,presentationbinning,selection+'*'+DataRescalingString+'*(IsoMu24Pass>0.5)',DataUnfoldedStyle,Label)
	h_pres_unf_Data_err=CreateHisto('h_pres_unf_Data_err','Data, 5/fb [Unfolded/Reco]',t_SingleMuData,recomodvariable,presentationbinning,selection+'*'+DataErrorString+'*(IsoMu24Pass>0.5)',DataUnfoldedStyle,Label)

	# Closure
	h_pres_unf_Data_pseudo=CreateHisto('h_pres_unf_Data_pseudo','MC Closure [Unf. Reco/ Gen]',t_WJets_MG,recomodvariable,presentationbinning,selection+weight+'*'+DataRescalingString_pseudo,DataUnfoldedStyle_pseudo,Label)
	h_pres_unf_Data_err_pseudo=CreateHisto('h_pres_unf_Data_err_pseudo','MC Closure [Unf. Reco/ Gen]',t_WJets_MG,recomodvariable,presentationbinning,selection+weight+'*'+DataErrorString_pseudo,DataUnfoldedStyle_pseudo,Label)

	# Other Backgrounds Rescaled
	h_pres_rec_DiBoson_res=CreateHisto('h_pres_rec_DiBoson_res','DiBoson [MadGraph]',t_DiBoson,recomodvariable,presentationbinning,selection+weight+'*'+DataRescalingString,DiBosonStackStyle,Label)
	h_pres_rec_ZJets_res=CreateHisto('h_pres_rec_ZJets_res','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,presentationbinning,selection+weight+'*'+DataRescalingString,ZStackStyle,Label)
	h_pres_rec_TTBar_res=CreateHisto('h_pres_rec_TTBar_res','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,presentationbinning,selection+weight+'*'+DataRescalingString,TTStackStyle,Label)
	h_pres_rec_SingleTop_res=CreateHisto('h_pres_rec_SingleTop_res','SingleTop [MadGraph]',t_SingleTop,recomodvariable,presentationbinning,selection+weight+'*'+DataRescalingString,StopStackStyle,Label)	
	h_pres_rec_QCDMu_res=CreateHisto('h_pres_rec_QCDMu_res','QCDMu [MadGraph]',t_QCDMuNonIso,recomodvariable,presentationbinning,selection+weight+'*'+QCDScale_Central+'*'+DataRescalingString,QCDStackStyle,Label)	


	# Other Backgrounds Unrescaled
	h_pres_rec_DiBoson=CreateHisto('h_pres_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,presentationbinning,selection+weight,DiBosonStackStyle,Label)
	h_pres_rec_ZJets=CreateHisto('h_pres_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,presentationbinning,selection+weight,ZStackStyle,Label)
	h_pres_rec_TTBar=CreateHisto('h_pres_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,presentationbinning,selection+weight,TTStackStyle,Label)
	h_pres_rec_SingleTop=CreateHisto('h_pres_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,presentationbinning,selection+weight,StopStackStyle,Label)	
	h_pres_rec_QCDMu=CreateHisto('h_pres_rec_QCDMu','QCDMu [MadGraph]',t_QCDMuNonIso,recomodvariable,presentationbinning,selection+weight+'*'+QCDScale_Central,QCDStackStyle,Label)	


	# Make background subtracted histos.
	h_pres_rec_Data = BackgroundSubtractedHistogram(h_pres_rec_Data,[ h_pres_rec_DiBoson_res, h_pres_rec_ZJets_res,h_pres_rec_TTBar_res,h_pres_rec_SingleTop_res,h_pres_rec_QCDMu_res])
	h_pres_unf_Data = BackgroundSubtractedHistogram(h_pres_unf_Data,[ h_pres_rec_DiBoson, h_pres_rec_ZJets,h_pres_rec_TTBar,h_pres_rec_SingleTop,h_pres_rec_QCDMu])

	DataBinInfo=[]
	MCBinInfo=[]

	# Loop to get the data and MC bin info as lists - need for tables and so forth.
	for x in range(h_pres_rec_Data.GetNbinsX()+1):
		if x==0:
			continue
		if h_pres_unf_Data.GetBinContent(x) != 0:
			h_pres_unf_Data.SetBinError(x,h_pres_unf_Data_err.GetBinContent(x)/h_pres_unf_Data.GetBinContent(x))
		else: 
			h_pres_unf_Data.SetBinError(x,0)

		lhs=h_pres_unf_Data.GetBinCenter(x)-0.5*(h_pres_unf_Data.GetBinWidth(x))
		rhs=h_pres_unf_Data.GetBinCenter(x)+0.5*(h_pres_unf_Data.GetBinWidth(x))
		content=h_pres_unf_Data.GetBinContent(x)
		error=h_pres_unf_Data_err.GetBinContent(x)
		lhs=str(lhs)
		rhs=str(rhs)
		content=str(round(content,2))
		error=str(round(error,2))
		DataBinInfo.append([lhs+' - '+str(rhs),content+' +- '+error])

		lhs=h_pres_gen_WJets.GetBinCenter(x)-0.5*(h_pres_gen_WJets.GetBinWidth(x))
		rhs=h_pres_gen_WJets.GetBinCenter(x)+0.5*(h_pres_gen_WJets.GetBinWidth(x))
		content=h_pres_gen_WJets.GetBinContent(x)
		error=h_pres_gen_WJets.GetBinError(x)
		lhs=str(lhs)
		rhs=str(rhs)
		content=str(round(content,2))
		error=str(round(error,2))
		MCBinInfo.append([lhs+' - '+rhs,content+' +- '+error])
		

	# For closure test, get the appropriate bin errors for the ratio. 
	for x in range(h_pres_rec_Data.GetNbinsX()+1):
		if x==0:
			continue
		if h_pres_unf_Data_pseudo.GetBinContent(x) != 0:
			# print h_pres_unf_Data_pseudo.GetBinContent(x), h_pres_gen_WJets.GetBinContent(x), h_pres_unf_Data_pseudo.GetBinContent(x)/h_pres_gen_WJets.GetBinContent(x) 
			h_pres_unf_Data_pseudo.SetBinError(x,h_pres_unf_Data_err_pseudo.GetBinContent(x)/h_pres_unf_Data_pseudo.GetBinContent(x))
		else: 
			h_pres_unf_Data_pseudo.SetBinError(x,0)
	
	# For closure test, divide by MC to convert to a ratio plot
	h_pres_unf_Data_pseudo.Divide(h_pres_gen_WJets)

	## Divide gen by reco for MC, and unfolded by reco for data.
	h_pres_gen_WJets.Divide(h_pres_rec_WJets)
	h_pres_unf_Data.Divide(h_pres_rec_Data)

	# Clean up style for closure test
	h_pres_unf_Data_pseudo = BeautifyHisto(h_pres_unf_Data_pseudo,DataUnfoldedStyle_pseudo2,Label,"MC Closure [Unf. Reco/ Gen]")

	# Dashed line at unity for closure test
	l_one=TLine(presentationbinning[0], 1 ,presentationbinning[-1],1)
	l_one.SetLineStyle(2)
	
	# Appropriate y axis ranges...
	RelMax=0.0
	RelMin=990.0
	for x in range(len(binset)):
		if x == 0:
			continue
		M=max([h_pres_gen_WJets.GetBinContent(x),h_pres_unf_Data.GetBinContent(x)])
		m=min([h_pres_gen_WJets.GetBinContent(x),h_pres_unf_Data.GetBinContent(x)])
		if M>RelMax and M<10:
			RelMax=M
		if m<RelMin and m<10:
			RelMin=m
	RelMax*=2.0
	RelMin*=0.75
	if RelMin < 0.0:
		RelMin = 0.0
	h_pres_gen_WJets.GetYaxis().SetTitle("Ratio")
	h_pres_gen_WJets.SetMarkerSize(0.000001)
	h_pres_gen_WJets.SetLineStyle(1)
	h_pres_gen_WJets.SetLineWidth(1)

	h_pres_gen_WJets.Draw("HIST")
	h_pres_gen_WJets.SetMaximum(RelMax)
	h_pres_gen_WJets.SetMinimum(RelMin)

	# Do the drawing
	h_pres_unf_Data.GetYaxis().SetTitle("Ratio")
	h_pres_unf_Data_pseudo.GetYaxis().SetTitle("Ratio")

	h_pres_unf_Data.Draw("EPHISTSAME")
	h_pres_unf_Data_pseudo.Draw("EPHISTSAME")
	# Create Legend
	FixDrawLegend(c1.cd(4).BuildLegend(0.5,  0.6,  0.9,  0.88,''))
	l_one.Draw("SAME")


	# Finally, print the plots as pdf and png
	c1.Print('pyplots/'+recovariable+'_'+tagname+'.pdf')
	c1.Print('pyplots/'+recovariable+'_'+tagname+'.png')

	# clear tmp file
	os.system("rm "+tmpname)

	#return the optimal dau, the bin-by-bin unfolded data and MC.
	return [tau,DataBinInfo,MCBinInfo]




# FullAnalysisWithUncertainty just runs MakeUnfoldedPlots several times for each systematic variation. The goal is to return final distributions.
def GetJetMultFactors(genvariable,recovariable,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar):

	# This is the standard plot. here we get the optimal tau value. 
	[tau,data_standard,mc_standard]=MakeUnfoldedPlots(genvariable,recovariable,-1,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',-1,'JetScaleFactors')

	scalestring = '('
	scalefactors = []

	for x in range(len(data_standard)): # Loop over bins of the original output table
		thisbin=(data_standard[x])[0]    # this is the bin X1--X2
		center = (data_standard[x])[1]   # The is the central value of the unfolded data
		prediction = (mc_standard[x])[1] # This is the MC prediction

		data = float(center.split()[0])
		mc = float(prediction.split()[0])
		scalefactor = 1.0
		if mc > 0:
			scalefactor = data/mc
		scalefactor = str(round(scalefactor,3)) 
		[binL,binR] = thisbin.split(' - ')
		bincondition = '*('+genvariable + '>'+binL+')*('+genvariable+'<'+binR+')'
		scalestring += (x==0)*("1.0*("+genvariable+"<"+binL+")")
		scalestring += '+'+scalefactor+bincondition
		scalefactors.append(scalefactor)
	scalestring += ')'
	return [scalefactors,scalestring]


# FullAnalysisWithUncertainty just runs MakeUnfoldedPlots several times for each systematic variation. The goal is to return final distributions.
def FullAnalysisWithUncertainty(genvariable,recovariable,default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar):

	# This is the standard plot. here we get the optimal tau value. 
	[tau,data_standard,mc_standard]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',-1,'standard')

	if ('--quickplots') in sys.argv:
		return 0

	# Replacing with ScaleUp/ScaleDown samples. 
	# [null,data_scale_plus,mc_scale_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'ScaleUp',tau,'scaleup')
	# [null,data_scale_minus,mc_scale_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'ScaleDown',tau,'scaledown')
	# [null,data_match_plus,mc_match_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'MatchUp',tau,'matchup')
	# [null,data_match_minus,mc_match_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'MatchDown',tau,'matchdown')
	
	# Plleup variations
	[null,data_pileup_plus,mc_pileup_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('central','sysplus8'),optvar,NormalDirectory,'',tau,'pileup_plus')
	[null,data_pileup_minus,mc_pileup_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('central','sysminus8'),optvar,NormalDirectory,'',tau,'pileup_minus')

	# Integrated luminosity up/down
	[null,data_lumi_plus,mc_lumi_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('4980','5090'),optvar,NormalDirectory,'',tau,'lumi_plus')
	[null,data_lumi_minus,mc_lumi_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('4980','4870'),optvar,NormalDirectory,'',tau,'lumi_minus')

	# Jet energy scale up/down, and smeared
	[null,data_jetscale_plus,mc_jetscale_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,JetScaleUpDirectory,'',tau,'jetscale_plus')
	[null,data_jetscale_minus,mc_jetscale_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,JetScaleDownDirectory,'',tau,'jetscale_minus')
	[null,data_jetsmear,mc_jetsmear]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,JetSmearDirectory,'',tau,'jetsmear')

	# Muon energy scale up/down and smeared.
	[null,data_muscale_plus,mc_muscale_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,MuScaleUpDirectory,'',tau,'muscale_plus')
	[null,data_muscale_minus,mc_muscale_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,MuScaleDownDirectory,'',tau,'muscale_minus')
	[null,data_musmear,mc_musmear]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,MuSmearDirectory,'',tau,'musmear')	

	# BTag Efficiency Up/Down
	[null,data_btag_plus,mc_btag_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection.replace('PFJet30TCHPTCountMod','PFJet30TCHPTCountEffUp'),gen_selection,weight,optvar,NormalDirectory,'',tau,'btag_plus')
	[null,data_btag_minus,mc_btag_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection.replace('PFJet30TCHPTCountMod','PFJet30TCHPTCountEffDown'),gen_selection,weight,optvar,NormalDirectory,'',tau,'btag_minus')


	# Here we make a vary verbose table.	
	data_table=[['|','Bin','|','Prediction','|','DataMean','|','PU(+)','PU(-)','|','Lumi(+)','Lumi(-)','|','BTag(+)','BTag(-)','|','JScale(+)','JScale(-)','JetSmear','|','MuScale(+)','MuScale(-)','MuSmear']]#,'|','Scale(+)','Scale(-)','Match(+)','Match(-)','|']]
	for x in range(len(data_standard)): # Loop over bins of the original output table
		thisbin=(data_standard[x])[0]    # this is the bin X1--X2
		center = (data_standard[x])[1]   # The is the central value of the unfolded data
		prediction = (mc_standard[x])[1] # This is the MC prediction

		# everything below are values of the data unfolded for the various systematic variations
		# scale_up = (data_scale_plus[x])[1]
		# scale_down = (data_scale_minus[x])[1]
		# match_up = (data_match_plus[x])[1]
		# match_down = (data_match_minus[x])[1]				

		pu_up = (data_pileup_plus[x])[1]
		pu_down = (data_pileup_minus[x])[1]

		lumi_up = (data_lumi_plus[x])[1]
		lumi_down = (data_lumi_minus[x])[1]

		btag_up = (data_btag_plus[x])[1]
		btag_down = (data_btag_minus[x])[1]
		
		jet_up = (data_jetscale_plus[x])[1]
		jet_down = (data_jetscale_minus[x])[1]
		jet_smear = (data_jetsmear[x])[1]
		
		mu_up = (data_muscale_plus[x])[1]
		mu_down = (data_muscale_minus[x])[1]
		mu_smear = (data_musmear[x])[1]

		# Strip out the +- statistical uncertainty for the various systematics. We will only consider statistical uncertainties on the central values. 
		for v in ['pu_up','pu_down','jet_up','jet_down','jet_smear','mu_up','mu_down','mu_smear','lumi_up','lumi_down','btag_up','btag_down']:
			exec(v+'='+v+'.split("+-")[0]')
		
		# Add a line to the data table.
		data_table.append(['|',thisbin,'|',prediction,'|',center,'|',pu_up,pu_down,'|',lumi_up,lumi_down,'|',btag_up,btag_down,'|',jet_up,jet_down,jet_smear,'|',mu_up,mu_down,mu_smear])#,'|',scale_up,scale_down,match_up,match_down,'|'])
	
	# Here we print a cleaned-up table.
	f = open('table_tmp.txt','w')
	for line in data_table:
		line=str(line)
		line=line.replace('[','')
		line=line.replace(']','')
		line=line.replace('\'','')
		line=line.replace('\t',' ')
		#line=line.replace('|','-')

		for x in range(10):
			line=line.replace('  ',' ')

		f.write(line+'\n')
	f.close()
	
	# Save the table to a txt file.
	os.system('cat table_tmp.txt | column -t -s"," > pyplots/'+recovariable+'.txt')
	os.system('rm table_tmp.txt')


# # FullAnalysisWithUncertainty just runs MakeUnfoldedPlots several times for each systematic variation. The goal is to return final distributions.
# def FullAnalysisWithUncertainty(genvariable,recovariable,default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar):

# 	# This is the standard plot. here we get the optimal tau value. 
# 	[tau,data_standard,mc_standard]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',-1,'standard')

# 	# Replacing with ScaleUp/ScaleDown samples. 
# 	[null,data_scale_plus,mc_scale_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'ScaleUp',tau,'scaleup')
# 	[null,data_scale_minus,mc_scale_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'ScaleDown',tau,'scaledown')
# 	[null,data_match_plus,mc_match_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'MatchUp',tau,'matchup')
# 	[null,data_match_minus,mc_match_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'MatchDown',tau,'matchdown')
	
# 	# Plleup variations
# 	[null,data_pileup_plus,mc_pileup_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('central','sysplus8'),optvar,NormalDirectory,'',tau,'pileup_plus')
# 	[null,data_pileup_minus,mc_pileup_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('central','sysminus8'),optvar,NormalDirectory,'',tau,'pileup_minus')

# 	# Integrated luminosity up/down
# 	[null,data_lumi_plus,mc_lumi_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('4980','5090'),optvar,NormalDirectory,'',tau,'lumi_plus')
# 	[null,data_lumi_minus,mc_lumi_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('4980','4870'),optvar,NormalDirectory,'',tau,'lumi_minus')

# 	# Jet energy scale up/down, and smeared
# 	[null,data_jetscale_plus,mc_jetscale_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,JetScaleUpDirectory,'',tau,'jetscale_plus')
# 	[null,data_jetscale_minus,mc_jetscale_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,JetScaleDownDirectory,'',tau,'jetscale_minus')
# 	[null,data_jetsmear,mc_jetsmear]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,JetSmearDirectory,'',tau,'jetsmear')

# 	# Muon energy scale up/down and smeared.
# 	[null,data_muscale_plus,mc_muscale_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,MuScaleUpDirectory,'',tau,'muscale_plus')
# 	[null,data_muscale_minus,mc_muscale_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,MuScaleDownDirectory,'',tau,'muscale_minus')
# 	[null,data_musmear,mc_musmear]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,MuSmearDirectory,'',tau,'musmear')	


# 	# Here we make a vary verbose table.	
# 	data_table=[['|','Bin','|','Prediction','|','DataMean','|','PU(+)','PU(-)','|','Lumi(+)','Lumi(-)','|','JScale(+)','JScale(-)','JetSmear','|','MuScale(+)','MuScale(-)','MuSmear','|','Scale(+)','Scale(-)','Match(+)','Match(-)','|']]
# 	for x in range(len(data_standard)): # Loop over bins of the original output table
# 		thisbin=(data_standard[x])[0]    # this is the bin X1--X2
# 		center = (data_standard[x])[1]   # The is the central value of the unfolded data
# 		prediction = (mc_standard[x])[1] # This is the MC prediction

# 		# everything below are values of the data unfolded for the various systematic variations
# 		scale_up = (data_scale_plus[x])[1]
# 		scale_down = (data_scale_minus[x])[1]
# 		match_up = (data_match_plus[x])[1]
# 		match_down = (data_match_minus[x])[1]				

# 		pu_up = (data_pileup_plus[x])[1]
# 		pu_down = (data_pileup_minus[x])[1]

# 		lumi_up = (data_lumi_plus[x])[1]
# 		lumi_down = (data_lumi_minus[x])[1]
		
# 		jet_up = (data_jetscale_plus[x])[1]
# 		jet_down = (data_jetscale_minus[x])[1]
# 		jet_smear = (data_jetsmear[x])[1]
		
# 		mu_up = (data_muscale_plus[x])[1]
# 		mu_down = (data_muscale_minus[x])[1]
# 		mu_smear = (data_musmear[x])[1]

# 		# Strip out the +- statistical uncertainty for the various systematics. We will only consider statistical uncertainties on the central values. 
# 		for v in ['pu_up','pu_down','jet_up','jet_down','jet_smear','mu_up','mu_down','mu_smear','lumi_up','lumi_down']:
# 			exec(v+'='+v+'.split("+-")[0]')
		
# 		# Add a line to the data table.
# 		data_table.append(['|',thisbin,'|',prediction,'|',center,'|',pu_up,pu_down,'|',lumi_up,lumi_down,'|',jet_up,jet_down,jet_smear,'|',mu_up,mu_down,mu_smear,'|',scale_up,scale_down,match_up,match_down,'|'])
	
# 	# Here we print a cleaned-up table.
# 	f = open('table_tmp.txt','w')
# 	for line in data_table:
# 		line=str(line)
# 		line=line.replace('[','')
# 		line=line.replace(']','')
# 		line=line.replace('\'','')
# 		line=line.replace('\t',' ')
# 		#line=line.replace('|','-')

# 		for x in range(10):
# 			line=line.replace('  ',' ')

# 		f.write(line+'\n')
# 	f.close()
	
# 	# Save the table to a txt file.
# 	os.system('cat table_tmp.txt | column -t -s"," > pyplots/'+recovariable+'.txt')
# 	os.system('rm table_tmp.txt')

# This is a quick utility to take a table from above, and return it as a python list which is more easy to handle.
def tabletolist(table):
	output=[]
	Nvertical=0
	Nhorizontal=0
	
	for line in open(table,'r'): # Loop on lines in the text table

		# Remove characters to make the table space-delimited
		line=line.replace('|','')
		line=line.replace('\t',' ')
		line=line.replace(' +- ','+-')
		line=line.replace(' - ','TO')
		line=line.replace('\n','')
		for x in range(20):
			line=line.replace('  ',' ')
			if line[0]==' ':
				line=line[1:]
			if line[-1]==' ':
				line=line[:-2]

		# Split space-delimited line into list
		line=line.split(' ')
		# Add line to the list output
		output.append(line)
		# Add one to the verticle dimension (number of lines)
		Nvertical += 1
	# Horizontal dimension is the number of columns
	Nhorizontal = len(output[0])
	
	# returned output is the Vertical and horizontal dimension, and the output itself.
	return [Nvertical,Nhorizontal,output]

# Quickly get a cell from a tabletolist type of table.
def getcell(listedtable,V,H):
	# Vertical and horizontal dimension
	Nvertical = listedtable[0]
	Nhorizontal=listedtable[1]
	# This is the "output" of tabletolist, or the actual table content
	table=listedtable[2]
	# Sanity check that the dimensions are ok
	if V>=Nvertical or H>=Nhorizontal:
		return 'NA'
	# Get the cell content
	content = table[V][H]
	return content

# This loops on a "tabletolist" type of table, and returns the binning on text or TeX formmat
def getbinning(listedtable):
	element = ''
	contents=[]
	n=0
	# While loop over rows. 
	while True:
		n+= 1
		# The binning is the first (zeroth) element.
		element =getcell(listedtable,n,0) 
		if element=='NA': # Problem with the table or dimensions
			break
		# Add the binning value to the list of elements.
		contents.append(element)
	binning = []
	# Here we convert the binning to a real numerical list
	for c in contents:
		edges=c.split('TO')
		for e in edges:
			if float(e) not in binning:
				binning.append(float(e))
	# Also convert to LaTeX style
	texcontents = ['$ '+ c+ ' $' for c in contents]
	return [texcontents,binning]

# Here we can get an entire column of a "tabletolist" tpe of table, and return as a latex entry or list of means and errors.
def getcolumn(listedtable,column):
	element = ''
	contents=[]
	n=0
	while True:
		n+= 1
		element =getcell(listedtable,n,column) 
		if element=='NA':
			break
		contents.append(element)	
	mean = []
	error=[]
	for c in contents:
		if '+-' in c:
			m,e = float(c.split('+-')[0]), float(c.split('+-')[1])
		else:
			m,e = float(c),0.0
		mean.append(m)
		error.append(e)
	texcontents=[ '$ ' +c.replace('+-', '\pm')+' $' for c in contents]
	return [texcontents,mean,error]

# Here we get the measurement (data unfolded column) of a table as tex and mean with assym errors.
def getmeasurement(listedtable):
	[meas_tex, meas_mean, meas_staterr] = getcolumn(listedtable,2)
	m=3
	variations=[]
	while True:
		[null, variation, variation_staterr] = getcolumn(listedtable,m)
		#print variation
		if 'NA' in str(variation) or len(str(variation)) < 5:
			break
		variations.append(variation)
		m+=1

	num = len(variations[0])
	
	tex = []
	means=[]
	err_plus=[]
	err_minus=[]
	verbose_errors = []
	for n in range(num):
		plus_err = []
		minus_err = []
		mean = meas_mean[n]
		errors=[]
		rel_err = 0
		for v in range(len(variations)):
			if mean>0:
				errors.append((variations[v][n] - mean)/mean)
				rel_err = (meas_staterr[n])/(meas_mean[n])
			else: 
				errors.append(0)
		#print mean,errors
		
		filtered_errors=[]
		def filter_pair(values):
			output = []
			if values[0] * values[1] < 0:
				return values
			else:
				if abs(values[0]) > abs(values[1]):
					return [values[0]]
				else:
					return [values[1]]
		
		PUerrors = filter_pair([errors[0],errors[1]])
		LUMIerrors=filter_pair([errors[2],errors[3]])
		BTAGerrors=filter_pair([errors[4],errors[5]])

		JESerrors=filter_pair([errors[6],errors[7]])
		JERerrors=[errors[8]]
		MESerrors=filter_pair([errors[9],errors[10]])
		MERerrors=[errors[11]]
		# SCALEerrors=filter_pair([errors[12],errors[13]])
		# MATCHerrors=filter_pair([errors[14],errors[15]])
		STATerrors=[rel_err, -rel_err]
		
		allerrors=PUerrors+LUMIerrors+BTAGerrors+JESerrors+JERerrors+MESerrors+MERerrors+STATerrors#SCALEerrors+MATCHerrors+STATerrors
		# Quick hack to ignore shape systematics
		# allerrors=PUerrors+LUMIerrors+JESerrors+JERerrors+MESerrors+MERerrors+STATerrors

		standard_errorset = [PUerrors,LUMIerrors,BTAGerrors,JESerrors,JERerrors,MESerrors,MERerrors,STATerrors]#SCALEerrors,MATCHerrors,STATerrors]

		def verbose_errorset(errset):
			outerrs = []
			for e in errset:
				maxerr = 0
				for error in e:
					if abs(error) > maxerr:
						maxerr = abs(error)
				maxerr = 100*maxerr
				maxerr = str(round(maxerr,2))
				outerrs.append(maxerr)
			return outerrs

		verbose_errors.append(verbose_errorset(standard_errorset))

		pos_error = 0
		neg_error = 0
		for x in allerrors:
			if x>0:
				pos_error += x*x
			if x<0:
				neg_error += x*x
		pos_error = float(str(round(mean*math.sqrt(pos_error),2)))
		neg_error = float(str(round(-mean*math.sqrt(neg_error),2)))
		
		#print  mean, pos_error,neg_error
		
		tex.append('$ ' + str(mean) +'_{'+ str(neg_error) +'}'+'^{+'+str(pos_error)  +'}'  ' $')
		means.append(mean)
		err_plus.append(pos_error)
		err_minus.append(neg_error) 
	
	verbose_errors_out = zip(*verbose_errors)

	return [tex,means,err_plus, err_minus,verbose_errors_out]

def roundnumbers(astring,nround):

	nums='.0123456789'

	allnumstrings = []

	numstring = ''
	for x in astring:
		if x in nums:
			numstring += (x)
		else:
			numstring += ','
	for z in range(20):
		numstring = numstring.replace(',,',',')
	numstring = numstring.split(',')
	# print numstring
	converts = []
	for n in numstring:
		if len(n)>2:
			n_in = n
			n_out = str(round((float(n)),nround))
			converts.append([n_in,n_out])
	# maxdec = 0

	# for c in converts:
	# 	if len(c[1])>maxdec:
	# 		maxdec = len(c[1])
	# for n in range(5):
	# 	for c in range(len(converts)):
	# 		if len(converts[c][1])<maxdec:
	# 			converts[c][1] += '0'
	for c in converts:
		astring = astring.replace(c[0],c[1])


	return astring


# Here we can convert a nummber of colums to a latex  style table.
def TexTableFromColumns(columns):
	global_length = len(columns[0])
	for c in columns:
		if len(c) != global_length:
			return 'ERROR: Columns not of equal length!!!'
	table = '\n'
	for x in range(global_length):
		line=''
		for c in columns:
			line+=c[x] + ' ,& '
			
		line+='\n'
		line=line.replace('TO',' -- ')
		line=line.replace('& \n',' \\\\\n')
		table+= line
	table+='\n'
	table = roundnumbers(table,3)
	return table	

# Quickly write a python string to a text file, creating neat spacing with whatever spacer character
def StringToFile(string,afile, spacer):
	f = open(afile,'w')
	for line in string:
		f.write(line)
	f.close()
	
	if spacer != '':
		os.system('cat '+afile+' | column -t -s"'+spacer+'" > '+afile+'edit')
		os.system('mv '+afile+'edit '+afile)
		
	print 'File ', file, ' has been written.'

# Normalize all numbers in a text file with a given norm factor. Useful for dividing by the integrated luminosity
# to get a table of cross-sections instead of event counts. 
def NormalizeTexTable(file,norm):
	nums='.0123456789'
	
	def IsNumber(Character):
		if Character in nums:
			return True
		else:
			return False
	newtable=''
	for line in open(file):
		line=line.split('&')
		#print line
		newline = ''
		for element in range(len(line)):
			if element==0:
				newline += line[element]
				continue
			element = line[element]
			isnumber=False
			runningnumber=''
			
			for x in element:
				isnumber = IsNumber(x)
				if (isnumber):
					runningnumber+=x
				else: 
					if runningnumber!='':
						runningnumber = str(round(float(runningnumber)/norm,2))
						newline+=runningnumber
						runningnumber=''
						newline += x
					else:
						newline+=x
						#print newline
				#print newline
			newline += ' ,& '
		newline = newline.replace('\n ,& ','\n')
		newtable += newline
	return newtable

# Take a given binning, and means with errors, and create a TGraphAsymErrors output.
def CreateHistoFromLists(binning, name, label, mean, up, down, style,normalization,plottype):

	binset=ConvertBinning(binning)
	n = len(binset)-1
	htest= TH1D('htest','htest',n,array('d',binset))

	for a in range(len(mean)):
		mean[a] = abs(mean[a])
	for a in range(len(up)):
		up[a] = abs(up[a])
	for a in range(len(down)):
		down[a] = abs(down[a])


	X = []
	Y = []
	Xplus=[]
	Xminus=[]
	Yplus=[]
	Yminus=[]

	if normalization==0:
		N=1.0
	else:
		N=normalization

	for x in range(len(binset)-1):
		c = htest.GetBinCenter(x+1)
		d = 0.5*htest.GetBinWidth(x+1)
		center = mean[x]
		upper = up[x]
		lower=down[x]
		
		X.append(c)
		Xplus.append(abs(d))
		Xminus.append(abs(d))
		
		Y.append(center/N)
		Yplus.append(abs(upper)/N)
		Yminus.append(abs(lower)/N)
			
	X = array("d", X)
	Xplus = array("d", Xplus)
	Xminus = array("d", Xminus)


	Y = array("d", Y)
	Yplus = array("d", Yplus)
	Yminus = array("d", Yminus)	

	hout = TGraphAsymmErrors(n,X,Y,Xminus,Xplus,Yminus,Yplus)
	
	hout.SetTitle(name)
	
	hout.SetFillStyle(style[0])
	hout.SetMarkerStyle(style[1])
	hout.SetMarkerSize(style[2])
	hout.SetLineWidth(style[3])
	hout.SetMarkerColor(style[4])
	hout.SetLineColor(style[4])
	hout.SetFillColor(style[4])
	hout.SetFillColor(style[4])
	#hout.SetMaximum(2.0*hout.GetMaximum())
	hout.GetXaxis().SetTitle(label[0])
	hout.GetYaxis().SetTitle(label[1])
	hout.GetXaxis().SetTitleFont(42)
	hout.GetYaxis().SetTitleFont(42)
	hout.GetXaxis().SetLabelFont(42)
	hout.GetYaxis().SetLabelFont(42)

	if plottype=="TopPlot":
		hout.GetYaxis().SetTitleFont(42);
		hout.GetXaxis().SetTitleSize(.05);
		hout.GetYaxis().SetTitleSize(.05);
		hout.GetXaxis().CenterTitle();
		hout.GetYaxis().CenterTitle();
		hout.GetXaxis().SetTitleOffset(0.9);
		hout.GetYaxis().SetTitleOffset(1.15);
		hout.GetYaxis().SetLabelSize(.05);
		hout.GetXaxis().SetLabelSize(.05);


	if plottype=="SubPlot":
		hout.GetYaxis().SetTitleFont(42);
		hout.GetXaxis().SetTitleSize(.13);
		hout.GetYaxis().SetTitleSize(.13);
		hout.GetXaxis().CenterTitle();
		hout.GetYaxis().CenterTitle();		
		hout.GetXaxis().SetTitleOffset(.33);
		hout.GetYaxis().SetTitleOffset(.33);
		hout.GetYaxis().SetLabelSize(.09);
		hout.GetXaxis().SetLabelSize(.09);

	return [hout,[mean,up,down,binset]]

# Use CreateHistoFromLists to quickly cast a Rivet NTuple into a tGraph for overlay with other plots. 
def RivetHisto(rivetfile, rivetvariable, binning,selection, label, style,original_events,normalization, ncompare, quantity, WRenormalizationForRivet):

	frivet = TFile.Open(rivetfile)
	trivet = frivet.Get("RivetTree")
	Name = "MadGraph"*("Madgraph" in rivetfile) + "Pythia"*("Pythia" in rivetfile)  + "Sherpa"*("Sherpa" in rivetfile) + ("PROBLEM")*(("Madgraph" not in rivetfile)*("Pythia" not in rivetfile)*("Sherpa" not in rivetfile))
	hrivet = CreateHisto(Name,Name,trivet,rivetvariable,binning,selection+'*'+WRenormalizationForRivet,style,label)
	hrivet.Scale(4980.0*31314.0/(1.0*original_events))

	means=[]
	errs=[]
	rivetscale = ncompare/(hrivet.Integral())
	# hrivet.Scale(rivetscale)
	scalefactor=1.0


	for x in range(len(binning)-1):
		means.append(scalefactor*(hrivet.GetBinContent(x+1)))
		errs.append(scalefactor*(hrivet.GetBinError(x+1)))

	if normalization==0:
		label = [label, 'Events/Bin']
	else:
		label = [label, '#sigma [pb]']

	RivetOutputHisto = CreateHistoFromLists(binning, Name,label, means, errs, errs, style,normalization,"SubPlot")

	RivetOutputHisto[0].GetXaxis().SetTitle(label[0])
	RivetOutputHisto[0].GetYaxis().SetTitle(label[1])
	RivetOutputHisto[0].GetXaxis().SetTitleFont(42)
	RivetOutputHisto[0].GetYaxis().SetTitleFont(42)
	RivetOutputHisto[0].GetXaxis().SetLabelFont(42)
	RivetOutputHisto[0].GetYaxis().SetLabelFont(42)

	RivetOutputHisto[0].GetYaxis().SetTitleFont(42);
	RivetOutputHisto[0].GetXaxis().SetTitleSize(.1);
	RivetOutputHisto[0].GetYaxis().SetTitleSize(.1);
	RivetOutputHisto[0].GetXaxis().CenterTitle();
	RivetOutputHisto[0].GetYaxis().CenterTitle();
	RivetOutputHisto[0].GetXaxis().SetTitleOffset(1.1);
	RivetOutputHisto[0].GetYaxis().SetTitleOffset(1.1);
	RivetOutputHisto[0].GetYaxis().SetLabelSize(.1);
	RivetOutputHisto[0].GetXaxis().SetLabelSize(.1);
	return [RivetOutputHisto,rivetscale]



# def RivetHisto(rivetfile, rivetvariable, binning,selection, label, style,original_events,normalization, nmadgraph, quantity, WRenormalizationForRivet):

# 	frivet = TFile.Open(rivetfile)
# 	trivet = frivet.Get("RivetTree")
# 	Name = "MadGraph"*("Madgraph" in rivetfile) + "Pythia"*("Pythia" in rivetfile)  + "Sherpa"*("Sherpa" in rivetfile) + ("PROBLEM")*(("Madgraph" not in rivetfile)*("Pythia" not in rivetfile)*("Sherpa" not in rivetfile))
# 	print '************** ',Name
# 	hrivet = CreateHisto(Name,Name,trivet,rivetvariable,binning,selection+'*'+WRenormalizationForRivet,style,label)
# 	# print 'Total Entries: ', trivet.GetEntries()
# 	print ' hrivet stats:    ', hrivet.GetEntries(), hrivet.Integral(), 
# 	print ' In Madgraph:  ', nmadgraph
# 	acceptance = (1.0*(hrivet.Integral()))/(1.0*original_events)
# 	print  '*** ',acceptance

# 	acceptance = 1.0
# 	# print 'Acceptance: ', acceptance,
# 	scalefactor = (4980.0*31314.0)*acceptance
# 	# print 'Scale: ', scalefactor
# 	if hrivet.Integral()>0:
# 		hrivet.Scale(1.0/hrivet.Integral())
# 	means=[]
# 	errs=[]
# 	if (scalefactor <=0):
# 		scalefactor=1
# 	rivetscale = nmadgraph/(scalefactor)

# 	if True:
# 		scalefactor=nmadgraph

# 	for x in range(len(binning)-1):
# 		means.append(scalefactor*(hrivet.GetBinContent(x+1)))
# 		errs.append(scalefactor*(hrivet.GetBinError(x+1)))
# 		# print binning[x],'-',binning[x+1],'  ', means[x], '+-',errs[x]

# 	if normalization==0:
# 		label = [label, 'Events/Bin']
# 	else:
# 		label = [label, 'd#sigma/d'+quantity+' [pb/GeV]']


# 	RivetOutputHisto = CreateHistoFromLists(binning, Name,label, means, errs, errs, style,normalization,"SubPlot")

# 	return [RivetOutputHisto,rivetscale]

def SherpaHisto(sherpafile, sherpavariable, binning,sel, label, style,original_events,normalization, nmadgraph, quantity, WRenormalizationForSherpa):

	# print sherpafile
	fsherpa = TFile.Open(sherpafile)
	tsherpa = fsherpa.Get("PhysicalVariables")
	# print "Sherpa Entries: ",tsherpa.GetEntries()
	# print "WRenorm:  ",WRenormalizationForSherpa, '--'
	Name = "MadGraph"*("MadGraph" in sherpafile) + "Pythia"*("Pythia" in sherpafile) +"Sherpa"*("Sherpa" in sherpafile)+ "PROBLEM"*("MadGraph" not in sherpafile and "Pythia" not in sherpafile)
	# print "LABELS: ", label
	# print "Label Check: ", label[0]
	# print "Var: ", sherpavariable
	if 'jet1' in sherpavariable:
		sel += j1
		print "Adding selection:",j1
	if 'jet2' in sherpavariable:
		sel += j2
		print "Adding selection:",j2
	if 'jet3' in sherpavariable:
		sel += j3
		print "Adding selection:",j3
	if 'jet4' in sherpavariable:
		sel += j4
		print "Adding selection:",j4
	if 'jet5' in sherpavariable:
		sel += j5							
		print "Adding selection:",j5
	hsherpa = CreateHisto(Name,Name,tsherpa,sherpavariable,binning,sel+'*(Pt_genmuon1>1.0)*weight_pu_central*4980*0.92*'+WRenormalizationForSherpa,style,label)
	# print 'Using Selection For Sherpa: ',sel+'*weight_pu_central*4980*0.92*'+WRenormalizationForSherpa, sherpavariable
	# print hsherpa.Integral()

	means=[]
	errs=[]
	
	sherpascale = nmadgraph/hsherpa.Integral()
	# sherpascale=1.0
	
	for x in range(len(binning)-1):
		means.append(sherpascale*(hsherpa.GetBinContent(x+1)))
		errs.append(sherpascale*(hsherpa.GetBinError(x+1)))
		# print binning[x],'-',binning[x+1],'  ', means[x], '+-',errs[x]

	if normalization==0:
		label = [label[0], 'Events/Bin']
	else:
		# label = [label[0], 'd#sigma/d'+quantity+' [pb/GeV]']
		label = [label[0], '#sigma [pb]']


	SherpaOutputHisto = CreateHistoFromLists(binning, Name,label, means, errs, errs, style,normalization,"SubPlot")

	return [SherpaOutputHisto,sherpascale]

# There is no built-in division for tgraphs. This does the trick. 
# For now, errors are converted into symetric errors conservatively, as one must make a choice of handling such errors. 
def DivideTGraphs_naively(gv1, gv2,style):

	[mean1,up1,down1,binset1]=gv1
	[mean2,up2,down2,binset2]=gv2

	if binset1!=binset2:
		print "ERROR: CAN'T DIVIDE GRAPHS, EXITING."
		sys.exit()
	binset=binset1

	ratmean = []
	raterr = []

	for x in range(len(binset)-1):
		m1=mean1[x]
		m2=mean2[x]
		u1=up1[x]
		u2=up2[x]
		d1=down1[x]
		d2=down2[x]

		if m2 != 0:
			rat = m1/m2
		else: 
			rat = 1.0 
		if m1==0:
			rat = 1

		err_1 = max([u1,d1])
		err_2 = max([u2,d2])

		frac1 = 0
		if m1 !=0:
			frac1 = err_1/m1


		frac2 = 0
		if m2 !=0:
			frac2 = err_2/m2

		err = rat*( math.sqrt( (frac1)**2 + (frac2)**2  ))

		ratmean.append(rat)
		raterr.append(err)

		# print  m1,m2,' || ',u1,u2,' || ', d1,d2, ' || ', rat, err, ' || ',err_1, err_2,' || ', frac1, frac2


	n = 0

	return CreateHistoFromLists(binset, "example",["","Data / Theory"], ratmean,raterr,raterr,style,1.0,"SubPlot")[0]

# Using basic asymmetric errors.
def DivideTGraphs(gv1, gv2,style):

	[mean1,up1,down1,binset1]=gv1
	[mean2,up2,down2,binset2]=gv2

	if binset1!=binset2:
		print "ERROR: CAN'T DIVIDE GRAPHS, EXITING."
		sys.exit()
	binset=binset1

	ratmean = []
	raterr_up = []
	raterr_down = []

	yvalues = []

	for x in range(len(binset)-1):
		m1=mean1[x]
		m2=mean2[x]
		u1=up1[x]
		u2=up2[x]
		d1=down1[x]
		d2=down2[x]

		if m2 != 0:
			rat = m1/m2
		else: 
			rat = 1.0 
		if m1==0:
			rat = 1

		u1 = m1 +u1
		u2 = m2 +u2
		d1 = m1 -d1
		d2 = m2 -d2

		if u1<0.0001:  u1 = 0.0001
		if u2<0.0001:  u2 = 0.0001
		if d1<0.0001:  d1 = 0.0001
		if d2<0.0001:  d2 = 0.0001


		possible_window_values = [u1/u2,u1/d2,d1/u2,d1/d2]
		window = [abs(rat-max(possible_window_values)), abs(rat-min(possible_window_values))]
		ratmean.append(rat)
		raterr_up.append(window[0])
		raterr_down.append(window[1])
		
		yvalues+= [rat+window[0],rat-window[1]]


	yup = round((1.2*max(yvalues)),2)
	ydown = round((0.8*min(yvalues)),2)
	if yup>5: yup=5
	if ydown<-5: ydown=-5
	return [CreateHistoFromLists(binset, "example",["","Data / Theory"], ratmean,raterr_up,raterr_down,style,1.0,"SubPlot")[0] ,[yup,ydown]]



# Using basic asymmetric errors.
def DivideTGraphsFlatRel(gv1, gv2,style):

	[mean1,up1,down1,binset1]=gv1
	[mean2,up2,down2,binset2]=gv2


	if binset1!=binset2:
		print "ERROR: CAN'T DIVIDE GRAPHS, EXITING."
		sys.exit()
	binset=binset1

	ratmean = []
	raterr_up = []
	raterr_down = []

	yvalues = []

	for x in range(len(binset)-1):
		m1=mean1[x]
		m2=mean2[x]
		u1=up1[x]
		u2=up2[x]
		d1=down1[x]
		d2=down2[x]

		rat = 5.0
		ratup = rat
		ratdown = rat

		if m2 != 0:
			rat = m1/m2
			ratup = m1/(m2 + u2)
			ratdown = m1/(m2 - d2)


		if m1==0:
			rat = 5.0

		window = [0,0]


		window = [ratup - rat, ratdown - rat]
		window.sort()


		ratmean.append(rat)
		raterr_down.append(abs(window[0]))
		raterr_up.append(abs(window[1]))
		
		# print rat, ratup, ratdown, window

		raterr_up.append(window[0])
		raterr_down.append(window[1])

	return [CreateHistoFromLists(binset, "example",["","Data / MC"], ratmean,raterr_up,raterr_down,style,1.0,"SubPlot")[0] ,[2,0]]



# Using basic asymmetric errors.
def CentralRatioBand(gv, style):

	[mean,up,down,binset]=gv


	ratmean = []
	raterr_up = []
	raterr_down = []

	yvalues = []

	for x in range(len(binset)-1):
		m1=mean[x]
		u1=up[x]
		d1=down[x]

		uval = 1.0
		dval = 1.0
		if m1 > 0:
			uval = u1/m1
			dval = d1/m1
		ratmean.append(1.0)
		raterr_up.append(uval)
		raterr_down.append(dval)
		
		yvalues+= [uval,dval]


	yup = round((1.2*max(yvalues)),2)
	ydown = round((0.8*min(yvalues)),2)
	if yup>5: yup=5
	if ydown<-5: ydown=-5
	yup = 2
	ydown = 0
	return [CreateHistoFromLists(binset, "example",["","Data / MC"], ratmean,raterr_up,raterr_down,style,1.0,"SubPlot")[0] ,[yup,ydown]]

# This creates the final "results"-style plot!
def FinalHisto(binning, label, quantity, filename ,expectation_means, expectation_errors, expectation_names, measurement, measurement_error_up, measurement_error_down, normalization,WRenormalization,sel):

	c1 = TCanvas("c1","",700,800)

	pad1 = TPad( 'pad1', 'pad1', 0.0, 0.31, 1.0, 1.0 )#divide canvas into pads
	pad2 = TPad( 'pad2', 'pad2', 0.0, 0.02, 1.0, 0.31 )

	pad1.SetBottomMargin(0.0)
	pad1.SetTopMargin(0.1)
	pad1.SetLeftMargin(0.12)
	pad1.SetRightMargin(0.1)


	pad2.SetBottomMargin(0.3)
	pad2.SetTopMargin(0.0)
	pad2.SetLeftMargin(0.12)
	pad2.SetRightMargin(0.1)


	# pad1.SetTopMargin(0)

	# pad2.SetBottomMargin(0)
	# pad2.SetTopMargin(0)


	pad1.Draw()
	pad2.Draw()

	# pad1.SetGrid()
	pad1.SetLogy()
	pad1.cd()

	gStyle.SetOptStat(0)
	MadGraphStyle=[3254,21,.9,1,4]
	MadGraphSubStyle=[3254,21,.9,1,4]

	SherpaStyle=[3254+1001,22,.9,1,2]

	SherpaRivetStyle=[3254,22,.9,1,2]
	# SherpaRivetSubStyle=[3254,22,.9,1,2]
	SherpaRivetSubStyle=[0,22,1,1,2]


	# MadGraphRivetSubStyle=[3245,21,.9,1,4]
	MadGraphRivetSubStyle=[0,21,1,1,4]

	MadGraphRivetStyle=[3245,21,.9,1,4]

	DataRecoStyle=[0,20,1,1,1]	

	CentralBandStyle = [1001,20,0.00001,1,30]
	
	rivetname = (filename.split('/')[-1]).split('FINAL')[0]
	standardname= (filename.split('/')[-1]).split('FINAL')[0]
	# print "USING  VARIABLE:  ",standardname

	for x in RivetBranchMap:
		if x[0] in rivetname:
			rivetname = rivetname.replace(x[0],x[1])

	for x in GenBranchMap:
		if x[0] in standardname:
			standardname=standardname.replace(x[0],x[1])
	
	madgraph_NOriginal = float(((RIVETMadGraph.split('/')[-1]).split('NEvents_')[-1]).split('.root')[0])
	sherpa_NOriginal   = float(((RIVETSherpa.split('/')[-1]).split('NEvents_')[-1]).split('.root')[0])

	rivetlabel=label	
	
	Max = max(measurement)*10
	Min = min(measurement)*.7
	
	if normalization==0:
		label = [label, 'Events/Bin']
	else:
		label = [label, '#sigma [pb]']
		Max=Max/normalization
		Min=Min/normalization

	for nn in range(6):
		nn+=2
		if 'pfjet'+str(nn) in standardname:
			exec ('sel+=j'+str(nn-1))
	
	# Get Measured Histo
	name="Measured"
	mean_value = measurement
	plus_errors=measurement_error_up
	minus_errors=measurement_error_down
	style=DataRecoStyle
	[Meas,Meas_verbose] = CreateHistoFromLists(binning, name,label, mean_value, plus_errors, minus_errors, CentralBandStyle,normalization,"TopPlot")
	ndataunf = sum(Meas_verbose[0])

	# Get Rivet Histos
	[[Rivet_MadGraph_Result,Rivet_MadGraph_Result_verbose], rivetrescale] = RivetHisto(RIVETMadGraph,rivetname,binning,"(evweight)*(mt_mumet>50)*(ptmuon>25)*(abs(etamuon)<2.1)",rivetlabel,MadGraphRivetSubStyle,madgraph_NOriginal,normalization,ndataunf,quantity,WRenormalization)
	[[Rivet_Sherpa_Result,Rivet_Sherpa_Result_verbose], sherparescale]    = RivetHisto(RIVETSherpa,  rivetname,binning,"(evweight)*(mt_mumet>50)*(ptmuon>25)*(abs(etamuon)<2.1)",rivetlabel,  SherpaRivetSubStyle,sherpa_NOriginal  ,normalization,ndataunf,quantity,WRenormalization)

	# Storing stuff...
	fplot = TFile.Open(filename+'root',"RECREATE")

	Meas.Write("Meas")
	# Exp.Write("Exp")
	fplot.Close()

	flog = open(filename+'_TGraphContent.txt','w')
	flog.write('\n,Meas_verbose = '+str(Meas_verbose)+'\n')
	# flog.write('\n,Exp_verbose = '+str(Exp_verbose)+'\n')
	flog.close()


	# Draw Two Rivet Histos and one Measured Histo
	Meas.SetMaximum(Max)
	Meas.SetMinimum(Min)
	Rivet_MadGraph_Result.SetMaximum(Max)
	Rivet_MadGraph_Result.SetMinimum(Min)
	Rivet_Sherpa_Result.SetMaximum(Max)
	Rivet_Sherpa_Result.SetMinimum(Min)		

	Meas.SetMarkerSize(0.7)
	Meas.SetLineColor(20)

	Meas.SetMarkerColor(20)
	Meas.Draw("A2")
	Meas.Draw("P")

	Rivet_MadGraph_Result.Draw("P")
	Rivet_Sherpa_Result.Draw("P")

	leg = TLegend(0.65,0.73,0.86,0.86,"","brNDC");
	leg.SetTextFont(42);
	leg.SetFillColor(0);
	leg.SetBorderSize(0);
	leg.SetTextSize(.04)
	leg.AddEntry(Meas,"Data");
	leg.AddEntry(Rivet_MadGraph_Result,"MadGraph");
	leg.AddEntry(Rivet_Sherpa_Result,"Sherpa");
	leg.Draw()

	# Stamp on top
	sqrts = "#sqrt{s} = 7 TeV";
	l1=TLatex()
	l1.SetTextAlign(12)
	l1.SetTextFont(42)
	l1.SetNDC()
	l1.SetTextSize(0.05)
	l1.DrawLatex(0.22,0.94,"CMS 2011  "+sqrts+" PRELIMINARY ")

	# Labels
	l2=TLatex()
	l2.SetTextAlign(12)
	l2.SetTextFont(42)
	l2.SetNDC()
	l2.SetTextSize(0.05)
	# l2.SetTextAngle(45);	
	# l2.DrawLatex(0.64,0.60,"PRELIMINARY")
	if False:
		# l2.DrawLatex(0.6,0.50,"R_{Rivet} = "+ str(round(rivetrescale,3)))
		l2.DrawLatex(0.64,0.65,"Data/MadGraph = "+ str(round(rivetrescale,3)))
		l2.DrawLatex(0.64,0.57,"Data/Sherpa   = "+ str(round(sherparescale,3)))


	############################
	### GO TO SUBPLOT        ###
	############################
	pad2.cd()
	# pad2.SetGrid()
	pad2.Draw()

	[cent1,[cent2up,cent2down]] = CentralRatioBand(Meas_verbose, CentralBandStyle)


	[grat2,[grat2up,grat2down]] = DivideTGraphsFlatRel(Meas_verbose,Rivet_Sherpa_Result_verbose,SherpaRivetSubStyle)
	unity=TLine(grat2.GetXaxis().GetXmin(), 1.0 , grat2.GetXaxis().GetXmax(),1.0)




	[grat3,[grat3up,grat3down]] = DivideTGraphsFlatRel(Meas_verbose,Rivet_MadGraph_Result_verbose,MadGraphRivetSubStyle)

	if grat3up > grat2up: grat2up = grat3up
	if grat3down < grat2down: grat2down = grat3down

	grat2up *= 1.3
	grat2down *= 0.7
	if grat2down < 0 : grat2down = 0
	if grat2up > 5: grat2up = 5

	grat2down = 0
	grat2up = 1.9999
	
	cent1.SetMaximum(grat2up)
	cent1.SetMinimum(grat2down)
	cent1.GetXaxis().SetTitle(label[0])
	cent1.GetYaxis().SetTitle("Data/Theory")
	cent1.GetXaxis().SetTitleOffset(.73);

	cent1.GetYaxis().SetTitleFont(42);
	cent1.GetXaxis().SetTitleSize(.12);
	cent1.GetYaxis().SetTitleSize(.12);
	cent1.GetXaxis().CenterTitle(0);
	cent1.GetYaxis().CenterTitle(1);
	cent1.GetXaxis().SetTitleOffset(0.88);
	cent1.GetYaxis().SetTitleOffset(0.45);
	cent1.GetYaxis().SetLabelSize(.1);
	cent1.GetXaxis().SetLabelSize(.1);

	grat2.SetMinimum(grat2down)
	grat2.SetMaximum(grat2up)
	grat3.SetMinimum(grat2down)
	grat3.SetMaximum(grat2up)
	
	cent1.Draw("A2")
	grat2.Draw("p")
	grat3.Draw("p")
	unity.Draw("SAME")

	c1.Print(filename+'pdf')
	c1.Print(filename+'png')


def ParseTablesToFinalResults(WRenorm,sel):
	allfiles = glob('pyplots/*txt')
	for f in allfiles:
		if 'FINAL' in f:
			continue
		# if 'Count' not in f:
		# 	continue
		# if "Pt" not in f or 'et4' not in f:
		# 	continue
			
		print '\n\nAnalyzing table: ',f
		output = f.replace('.txt','FINAL.')
		table = tabletolist(f)

		[tablebinning,rootbinning] = getbinning(table)
		[pred_tex, pred_mean, pred_err] = getcolumn(table,1)
		[meas_tex, meas_mean, meas_err_plus, meas_err_minus,meas_err_verbose] = getmeasurement(table)
		# print '-----'
		# print tablebinning
		# print '-----'
		# print pred_tex
		# print '-----'
		# print pred_mean
		# print '-----'
		# print meas_err_plus
		# print '-----'
		# print meas_err_verbose				
		# print '-----'


		StringToFile(TexTableFromColumns([tablebinning,pred_tex,meas_tex]), output+'TexCount.txt', ',') 

		systablesetup = [tablebinning]
		for x in meas_err_verbose:
			systablesetup.append(x)
		StringToFile(TexTableFromColumns(systablesetup), output+'TexVerboseError.txt', ',') 

		# sys.exit()
		StringToFile(NormalizeTexTable(output+'TexCount.txt',4980.0), output+'TexXSec.txt',',')

		prediction_means = [pred_mean]
		prediction_errors = [pred_err]
		prediction_names = ['MADGRAPH']
		
		label = f.split('/')[-1]
		label = label.split('.')[0]
		
		quantity = ' BLANK '
		
		if label=='Pt_pfjet1':
			label = 'Leading Jet p_{T} [GeV]'
			quantity = 'p_{T}'

		if label=='Pt_pfjet2':
			label = 'Second Leading Jet p_{T} [GeV]'
			quantity = 'p_{T}'

		if label=='Pt_pfjet3':
			label = 'Third Leading Jet p_{T} [GeV]'
			quantity = 'p_{T}'

		if label=='Pt_pfjet4':
			label = 'Fourth Leading Jet p_{T} [GeV]'
			quantity = 'p_{T}'

		if label=='Pt_pfjet5':
			label = 'Fifth Leading Jet p_{T} [GeV]'
			quantity = 'p_{T}'			
			
		if label=='Eta_pfjet1':
			label = 'Leading Jet #eta'
			quantity = '#eta'
			
		if label=='Eta_pfjet2':
			label = 'Second Leading Jet #eta'
			quantity = '#eta'						

		if label=='Eta_pfjet3':
			label = 'Third Leading Jet #eta'
			quantity = '#eta'	

		if label=='Eta_pfjet4':
			label = 'Fourth Leading Jet #eta'
			quantity = '#eta'	

		if label=='Eta_pfjet5':
			label = 'Fifth Leading Jet #eta'
			quantity = '#eta'				

		if label=='PFJet30Count':
			label = 'Jet Count (Exclusive)'
			quantity = 'N_{Jet}'

		if label=='MT_muon1MET':
			label = 'M_{T}(#mu,E_{T}^{miss}) [GeV]'
			quantity = 'M_{T}'

		if label=='Pt_MET':
			label = 'E_{T}^{miss} [GeV]'
			quantity = 'E_{T}^{miss}'

		if label=='DeltaPhi_pfjet1muon1':
			label = '#Delta #phi(jet_{1},#mu)'	
			quantity = '#Delta #phi(jet_{1},#mu)'

		if label=='DeltaPhi_pfjet2muon1':
			label = '#Delta #phi(jet_{2},#mu)'	
			quantity = '#Delta #phi(jet_{2},#mu)'

		if label=='DeltaPhi_pfjet3muon1':
			label = '#Delta #phi(jet_{3},#mu)'	
			quantity = '#Delta #phi(jet_{3},#mu)'

		if label=='DeltaPhi_pfjet4muon1':
			label = '#Delta #phi(jet_{4},#mu)'	
			quantity = '#Delta #phi(jet_{4},#mu)'

		if label=='DeltaPhi_pfjet5muon1':
			label = '#Delta #phi(jet_{5},#mu)'	
			quantity = '#Delta #phi(jet_{5},#mu)'

		
		# print "USING W RENORMALIZATION: ",WRenorm
		# print " -"*40
		FinalHisto(rootbinning,label,quantity, output+'PlotCount.', prediction_means, prediction_errors, prediction_names, meas_mean, meas_err_plus, meas_err_minus,0,WRenorm,sel)
		FinalHisto(rootbinning,label,quantity, output+'PlotXSec.', prediction_means, prediction_errors, prediction_names, meas_mean, meas_err_plus, meas_err_minus,4980.0,WRenorm,sel)
		# sys.exit()

		#os.system('cat pyplots/Pt_pfjet1FINAL.TexCount.txt')

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

main()





