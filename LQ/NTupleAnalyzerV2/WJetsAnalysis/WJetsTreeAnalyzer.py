import os

# Directory where root files are kept and the tree you want to get root files from. Normal is for standard analysis, the jet rescaling, jet smearing, muon PT rescaling ,and muon PT smearing. 


NormalDirectory       = './NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Oct26_2012_10_26_18_47_26/SummaryFiles'
JetScaleUpDirectory   = './NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Oct26_JetScaleUp_2012_10_26_22_14_14/SummaryFiles'
JetScaleDownDirectory = './NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Oct26_JetScaleDown_2012_10_27_01_32_33/SummaryFiles'
MuScaleUpDirectory    = './NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Oct26_MuScaleUp_2012_10_27_03_26_43/SummaryFiles'
MuScaleDownDirectory  = './NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Oct26_MuScaleDown_2012_10_27_04_50_05/SummaryFiles'
JetSmearDirectory     = './NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Oct26_JetSmear_2012_10_27_06_24_39/SummaryFiles'
MuSmearDirectory      = './NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_Oct26_MuSmear_2012_10_27_09_36_52/SummaryFiles'


# This is the Rivet NTuple for MadGraph
RIVETMadGraph='/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVET/MadGraphWithBdPhi_tree_NEvents_37534534.root'

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
RivetBranchMap.append(['PFJet40Count','njet_WMuNu'])
RivetBranchMap.append(['MT_muon1MET','mt_munu'])
RivetBranchMap.append(['Pt_MET','ptneutrino'])


# This is the main (and only) tree in the root files, storing single-valued branches (basically an NTuple, but made as TTree)
TreeName = "PhysicalVariables"


##########################################################################
########      Put all uses of the plotting funcs into main()      ########
##########################################################################

# The main function, called at the end of the script after all other function definitions. If just running analysis on a variable, modify only here.
def main():
	#os.system("rm pyplots/*.*")

	# Requirements on jet pT, to be implemented when looking at higher jet multiplicities, stored as strings for insertion in TCuts/projections.
	j1="*(Pt_pfjet1>40.0)"
	j2="*(Pt_pfjet2>40.0)"
	j3="*(Pt_pfjet3>40.0)"
	j4="*(Pt_pfjet4>40.0)"
	j5="*(Pt_pfjet5>40.0)"
	
	
	#MakeUnfoldedPlots('Pt_genmuon1','Pt_muon1',"p_{T}(#mu) [GeV]",[25,45,145],selection,'')
	
	# This is the baseline selection - only one muon, fiducial region, MT in W window.
	selection_noMTcut = '(Pt_muon1>45)*(Pt_muon2<15)*(abs(Eta_muon1)<2.1)'
	selection = '(Pt_muon1>45)*(Pt_muon2<15)*(abs(Eta_muon1)<2.1)*(MT_muon1MET>60)*(MT_muon1MET<100)'

	# This is the baseline weight. Central PU (Not modified for systematics), ILum = 4980/pb, muon HLT eff of 0.92.
	weight = '*weight_pu_central*4980*0.92'
	        
	# Calling on FullAnalysisWithUncertainty - creates all plots, tables, with unfolding, etc. Examples for Jet PT.  
	# To detail the arguments:
	# .........................(Gen Variable, Reco Var , X Label, Unfolding Binning, Presentation Binning, selection, weight, switch: 'v'= use ideal variable bins for unfolding, 'c' = use unmodified binning)                                                                                     


	FullAnalysisWithUncertainty('DeltaPhi_genjet1genmuon1','DeltaPhi_pfjet1muon1',"#Delta#phi(jet_{1},#mu) [GeV]",[50,0,3.1414927],[16,0,3.1414927],selection+j1,weight,'c')
	FullAnalysisWithUncertainty('DeltaPhi_genjet2genmuon1','DeltaPhi_pfjet2muon1',"#Delta#phi(jet_{2},#mu) [GeV]",[50,0,3.1414927],[16,0,3.1414927],selection+j2,weight,'c')
	FullAnalysisWithUncertainty('DeltaPhi_genjet3genmuon1','DeltaPhi_pfjet3muon1',"#Delta#phi(jet_{3},#mu) [GeV]",[25,0,3.1414927],[8,0,3.1414927],selection+j3,weight,'c')
	FullAnalysisWithUncertainty('DeltaPhi_genjet4genmuon1','DeltaPhi_pfjet4muon1',"#Delta#phi(jet_{4},#mu) [GeV]",[25,0,3.1414927],[8,0,3.1414927],selection+j4,weight,'c')
	FullAnalysisWithUncertainty('DeltaPhi_genjet5genmuon1','DeltaPhi_pfjet5muon1',"#Delta#phi(jet_{5},#mu) [GeV]",[25,0,3.1414927],[8,0,3.1414927],selection+j5,weight,'c')

	FullAnalysisWithUncertainty('Pt_genjet1','Pt_pfjet1',"p_{T}(jet_{1}) [GeV]",[140,20,720],[40,50,65,85,110,140,175,215,260,310,365],selection,weight,'v')
	FullAnalysisWithUncertainty('Pt_genjet2','Pt_pfjet2',"p_{T}(jet_{2}) [GeV]",[70,20,720],[40,50,65,85,110,140,175,215,260,310,365],selection+j1,weight,'v')
	FullAnalysisWithUncertainty('Pt_genjet3','Pt_pfjet3',"p_{T}(jet_{3}) [GeV]",[35,2,720],[40,50,65,85,110,140,175,215,260,310,365],selection+j2,weight,'v')
	FullAnalysisWithUncertainty('Pt_genjet4','Pt_pfjet4',"p_{T}(jet_{4}) [GeV]",[35,2,720],[40,50,65,85,110,140,175,215,260,310,365],selection+j4,weight,'v')
	FullAnalysisWithUncertainty('Pt_genjet5','Pt_pfjet5',"p_{T}(jet_{5}) [GeV]",[35,2,720],[40,50,65,85,110,140,175,215,260,310,365],selection+j5,weight,'v')
	# Further examples  - Jet Count, Transverse Mass, MET
	FullAnalysisWithUncertainty('GenJet40Count','PFJet40Count',"N_{Jet}",[12,-1.5,10.5],[5,-0.5,4.5],selection,weight,'c')	
	FullAnalysisWithUncertainty('MT_genmuon1genMET','MT_muon1MET',"M_{T}(#mu,E_{T}^{miss}) [GeV]",[44,40,150],[60,65,70,75,80,85,90,95,100],selection,weight,'v')
	FullAnalysisWithUncertainty('Pt_genMET','Pt_MET',"E_{T}^{miss} [GeV]",[100,0,430],[30,40,50,60,70,80,90,100,115,130,150,170,200,240,280,350],selection,weight,'v')
	
	# Further examples - Jet Etas	
	FullAnalysisWithUncertainty('Eta_genjet1','Eta_pfjet1',"#eta(jet_{1}) ",[60,-3.0,3.0],[24,-2.4,2.4],selection+j1,weight,'c')
	FullAnalysisWithUncertainty('Eta_genjet2','Eta_pfjet2',"#eta(jet_{2}) ",[60,-3.0,3.0],[24,-2.4,2.4],selection+j2,weight,'c')
	FullAnalysisWithUncertainty('Eta_genjet3','Eta_pfjet3',"#eta(jet_{3}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j3,weight,'c')
	FullAnalysisWithUncertainty('Eta_genjet4','Eta_pfjet4',"#eta(jet_{4}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j3,weight,'c')
	FullAnalysisWithUncertainty('Eta_genjet5','Eta_pfjet5',"#eta(jet_{5}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j4,weight,'c')



	# FullAnalysisWithUncertainty will create .txt files in the pyplots directory. This is the final results. 
	# Calling ParseTablesToFinalResults() will read these tables and produce fancier TeX tables and root plots.		
	
	# def GetMTWindowRenormalization(recovariable,xlabel,fullbinning,selection,weight,FileDirectory,tagname):
	# WRenorm = GetMTWindowRenormalization('MT_genmuon1genMET',"M_{T}(#mu,E_{T}^{miss}) [GeV]",[40,50,60,70,75,80,85,90,95,100,110,140,200,1000],selection_noMTcut,weight,NormalDirectory,'renormalization_controlregion')[0]

	# print WRenorm

	# ParseTablesToFinalResults(WRenorm)	
		


	# Below are just some calls of MakeUnfoldedPlots() - this function is called multiple times in FullAnalysisWithUncertainty. 
	# MakeUnfoldedPlots('MT_genmuon1genMET','MT_muon1MET',"M_{T}(#mu,E_{T}^{miss}) [GeV]",[50,50,150],[20,60,100],selection,weight,'v',NormalDirectory,'',2,'standard')
	#sys.exit()
	#MakeUnfoldedPlots('GenJet40Count','PFJet40Count',"N_{Jet}",[12,-1.5,10.5],[5,-0.5,4.5],selection,weight,'c',NormalDirectory,-1,'standard')	
	#MakeUnfoldedPlots('MT_genmuon1genMET','MT_muon1MET',"M_{T}(#mu,E_{T}^{miss}) [GeV]",[50,50,150],[20,60,100],selection,weight,'v',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Pt_genMET','Pt_MET',"E_{T}^{miss} [GeV]",[100,0,430],[15,30,330],selection,weight,'v',NormalDirectory,-1,'standard')

	#MakeUnfoldedPlots('Pt_genjet2','Pt_pfjet2',"p_{T}(jet_{2}) [GeV]",[50,0,500],[26,40,300],selection+j1,weight,'v',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Pt_genjet3','Pt_pfjet3',"p_{T}(jet_{3}) [GeV]",[25,0,500],[13,40,300],selection+j2,weight,'v',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Pt_genjet4','Pt_pfjet4',"p_{T}(jet_{4}) [GeV]",[25,0,500],[13,40,300],selection+j3,weight,'v',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Pt_genjet5','Pt_pfjet5',"p_{T}(jet_{5}) [GeV]",[10,0,500],[5,40,300],selection+j4,weight,'v',NormalDirectory,-1,'standard')

	#MakeUnfoldedPlots('Eta_genjet1','Eta_pfjet1',"#eta(jet_{1}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j1,weight,'c',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Eta_genjet2','Eta_pfjet2',"#eta(jet_{2}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j2,weight,'c',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Eta_genjet3','Eta_pfjet3',"#eta(jet_{3}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j3,weight,'c',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Eta_genjet4','Eta_pfjet4',"#eta(jet_{4}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j4,weight,'c',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Eta_genjet5','Eta_pfjet5',"#eta(jet_{5}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j5,weight,'c',NormalDirectory,-1,'standard')


	# There is also a basic histogram maker... No unfolding, bells, nor whistles.

	#MakeBasicPlot('PFJetCount',"N_{Jet} (Inclusive) [GeV]",[10,-0.5,9.5],selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('PFJetCount',"N_{Jet} (Inclusive) [GeV]",[10,-0.5,9.5],selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('PFJet30Count',"N_{Jet} (Inclusive) [GeV] - 30 GeV Threshold",[10,-0.5,9.5],selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('PFJet40Count',"N_{Jet} (Inclusive) [GeV] - 40 GeV Threshold",[10,-0.5,9.5],selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('MT_muon1MET',"M_{T}(#mu,E_{T}^{miss}) [GeV]",[40,60,160],selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Pt_MET',"E_{T}^{miss} [GeV]",[80,0,400],selection,weight,NormalDirectory,-1,'standard')
	
	#MakeBasicPlot('MET_pfsig',"E_{T}^{miss} Signif [GeV]",[50,0,250],selection,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Pt_pfjet1',"p_{T}(jet_{1}) [GeV]",[40,40,440],selection+j1,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Pt_pfjet2',"p_{T}(jet_{2}) [GeV]",[40,40,440],selection+j2,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Pt_pfjet3',"p_{T}(jet_{3}) [GeV]",[40,40,440],selection+j3,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Pt_pfjet4',"p_{T}(jet_{4}) [GeV]",[40,40,440],selection+j4,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Pt_pfjet5',"p_{T}(jet_{5}) [GeV]",[40,40,440],selection+j5,weight,NormalDirectory,-1,'standard')
	
	#MakeBasicPlot('Eta_pfjet1',"#eta(jet_{1})",[24,-2.4,2.4],selection+j1,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Eta_pfjet2',"#eta(jet_{2})",[24,-2.4,2.4],selection+j2,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Eta_pfjet3',"#eta(jet_{3})",[24,-2.4,2.4],selection+j3,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Eta_pfjet4',"#eta(jet_{4})",[24,-2.4,2.4],selection+j4,weight,NormalDirectory,-1,'standard')
	#MakeBasicPlot('Eta_pfjet5',"#eta(jet_{5})",[24,-2.4,2.4],selection+j5,weight,NormalDirectory,-1,'standard')	
	
	
	# Just saving tons of PNG output into a single PDF for easier viewing.
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
	legend.SetTextFont(132)
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
	binset=ConvertBinning(binning) # Assure variable binning
	n = len(binset)-1 # carry the 1
	hout= TH1D(name,legendname,n,array('d',binset)) # Declar empty TH1D
	hout.Sumw2() # Store sum of squares
	tree.Project(name,variable,selection) # Project from branch to histo
	
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
	hout.GetXaxis().SetTitleFont(132)
	hout.GetYaxis().SetTitleFont(132)
	hout.GetXaxis().SetLabelFont(132)
	hout.GetYaxis().SetLabelFont(132)
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
	histo.GetXaxis().SetTitleFont(132)
	histo.GetYaxis().SetTitleFont(132)
	histo.GetXaxis().SetLabelFont(132)
	histo.GetYaxis().SetLabelFont(132)
	return histo

# Cleans up a stacked histogram
def BeautifyStack(stack,label):
	# Fix Font
	stack.GetHistogram().GetXaxis().SetTitleFont(132)
	stack.GetHistogram().GetYaxis().SetTitleFont(132)
	stack.GetHistogram().GetXaxis().SetLabelFont(132)
	stack.GetHistogram().GetYaxis().SetLabelFont(132)
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
	hout.GetXaxis().SetTitleFont(132)
	hout.GetYaxis().SetTitleFont(132)
	hout.GetXaxis().SetLabelFont(132)
	hout.GetYaxis().SetLabelFont(132)
	
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
	n = len(binset)-1
	
	# Make new histogram
	hout= TH1D(newname,"",n,array('d',binset))
	
	# Get bin content and round to integer.
	bincontent=[]
	binx=[]
	for x in range(n):
		bincontent.append(int(round(histo.GetBinContent(x))))
		binx.append(histo.GetBinCenter(x))
		#print x, bincontent[x]

	# No offset or resolution needed like in smeared histos in next function. Ignore.
	offset = 0.0
	resolution = 0.0

	# Bin ranges. 
	maxbin=max(binset)
	minbin=min(binset)
	
	# Fill.
	for a in range(len(binx)):
		for y in range(bincontent[a]):
			hout.Fill(binx[a])
	return hout

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
	for x in range(n-2):
		if x<2:
			continue
		b1 = histo1.GetBinContent(x)
		b2 = histo2.GetBinContent(x)
		dif += abs(b1-b2)

	return dif

# This will return N histograms with the smearing and offset from SmearOffsetHisto - for tau optimization
def GetNSmearedHistos(inputhisto,binning,N,should_offset):
	histos=[]
	for x in range(N):
		print 'generating smeared histogram '+str(x)
		name='hsmear'+str(x)
		histos.append(SmearOffsetHisto(inputhisto,name,binning,should_offset))
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
		DifValues.append(SimpleDifFromTwoHistos(hunf,Params[1],binning))
		InitialDifs.append(SimpleDifFromTwoHistos(hsmear,Params[1],binning))
	
	#for x in range(len(InitialDifs)):
		#print str((DifValues[x])/(InitialDifs[x]))
	Improvements = [100.00*(InitialDifs[k]-DifValues[k])/InitialDifs[k] for k in range(len(DifValues))]
	DifAverage = sum(Improvements)/(1.0*N)
	return DifAverage
	
# This will test multiple values of tau with TestSVDTau, and find the best tau as the smallest difference of GEN wrt controlled unfoldings.
def FindOptimalTauWithPseudoExp(Params,binning,should_offset):
	binset=ConvertBinning(binning)
	n = len(binset)-1
	bestdif = -9999999999 # Dummy values to start
	bsettau=9999999999
	n = int(round(n-1))

	# Get N histograms with smearing and offset to use for comparison of tau values
	histoset=GetNSmearedHistos(Params[0],binning,10,should_offset)
	olddif=99999999999999999999999999
	for t in range(int(round(n/1.3))): # Only testing taus up to NBins/2. 
		if t<1: 
			continue
		if t>n-1:
			continue
		dif=(TestSVDTau(Params,t,histoset,binning)) # Get average dif for this tau. 
		print '      ...Initial test of tau = '+str(t)+' '*(5-len(str(t)))+'   Chi Improvement = '+str(round(dif,2))+'%'
		if olddif<0.0 and dif<2.0*olddif: # See if difs are diverging - then you can stop the loop
			print "        Best tau found at: tau = "+str(int(besttau))+"  ... Terminating tau serach"
			break		
		if dif>bestdif: # Seeif this tau is best
			bestdif=dif
			besttau=t
		olddif=dif
	return besttau # Return the best tau value


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
def GetMTWindowRenormalization(variable,xlabel,fullbinning,selection,weight,FileDirectory,tagname):

	# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
	for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
		exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
	tmpfile = TFile("tmp.root","RECREATE")	
	Label=[xlabel,"Events/Bin"]

	MCRecoStyle=[0,20,.00001,1,4]
	hs_rec_WJets_all=CreateHisto('hs_rec_WJets_all','W+Jets [Reco] (All)',t_WJets_MG,variable,fullbinning,selection+weight,MCRecoStyle,Label)
	hs_rec_WJets_win=CreateHisto('hs_rec_WJets_win','W+Jets [Reco] (Win)',t_WJets_MG,variable,fullbinning,selection+weight+"*(MT_muon1MET>50)*(MT_muon1MET<110)",MCRecoStyle,Label)

	print hs_rec_WJets_all.Integral()
	print hs_rec_WJets_win.Integral()	

	# return [0]
	the_rescaling = GetRescaling(hs_rec_WJets_win, hs_rec_WJets_all, fullbinning,"mt_munu")

	return the_rescaling

# This is basic plot code for a data vs MC histogram. It is not used much on it's own, but was a precursor to parts of MakeUnfoldedPlots.
def MakeBasicPlot(recovariable,xlabel,presentationbinning,selection,weight,FileDirectory,tagname):

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

	c1.cd(1)

	### Make the plots without variable bins!
	hs_rec_WJets=CreateHisto('hs_rec_WJets','W+Jets [Reco]',t_WJets_MG,recovariable,presentationbinning,selection+weight,WStackStyle,Label)
	hs_rec_Data=CreateHisto('hs_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recovariable,presentationbinning,selection,DataRecoStyle,Label)
	hs_rec_DiBoson=CreateHisto('hs_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recovariable,presentationbinning,selection+weight,DiBosonStackStyle,Label)
	hs_rec_ZJets=CreateHisto('hs_rec_ZJets','Z+Jets [Alpgen]',t_ZJets_MG,recovariable,presentationbinning,selection+weight,ZStackStyle,Label)
	hs_rec_TTBar=CreateHisto('hs_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recovariable,presentationbinning,selection+weight,TTStackStyle,Label)
	hs_rec_SingleTop=CreateHisto('hs_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recovariable,presentationbinning,selection+weight,StopStackStyle,Label)
	hs_rec_QCDMu=CreateHisto('hs_rec_QCDMu','QCD #mu-enriched [Pythia]',t_QCDMu,recovariable,presentationbinning,selection+weight,QCDStackStyle,Label)
	
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


			
def MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight,optvar,FileDirectory,file_override,tau_override,tagname):


	##############################################################################
	#######     Basic setup - Get the files and trees, designate styles    #######
	##############################################################################

	# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
	for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
		if 'Scale' in f or 'Match' in f:
			continue
		fin=f.replace("\n","")
		# file_override is just a means of replacing the normal file with files for shape-varied systematics which have different names.
		if file_override != '':
			if fin=='ZJets_MG.root':
				fin=fin.replace('_MG.root','_'+file_override+'.root')
			if fin=='WJets_MG.root':
				fin=fin.replace('_MG.root','_'+file_override+'.root')
			if fin=='TTBar.root':
				fin=fin.replace('Bar.root','Jets_'+file_override+'.root')				
		exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+fin.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")

	tmpfile = TFile("tmp"+str(random.randint(0,1000000))+".root","RECREATE") # temporary root file. Named with random number so you can run several versions of this script at once if needed.
		
	print "\n     Performing unfolding analysis for "+recovariable+" in "+str(binning[0]) +" bins from "+str(binning[1])+" to "+str(binning[2])+"  ... \n"
	# Create Canvas
	c1 = TCanvas("c1","",1200,900)
	c1.Divide(2,2)
	gStyle.SetOptStat(0)

	# These are teh style parameters for certain plots - [FillStyle,MarkerStyle,MarkerSize,LineWidth,Color]
	MCGenStyle=[0,20,.00001,1,2]
	MCGenSmearStyle=[0,20,.00001,1,9]

	MCRecoStyle=[0,20,.00001,1,4]
	DataRecoStyle=[0,20,.3,1,1]
	DataCompStyle=[0,20,0.3,1,6]
	BlankRecoStyle=[0,20,.00001,1,0]
	DataUnfoldedStyle=[0,21,0.4,1,1]
	DataUnfoldedStyle_pseudo=[0,21,0.4,1,9]
	DataUnfoldedStyle_pseudo2=[0,20,0.4,1,2]

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
	selection+='*('+recovariable+'<'+str(presentationbinning[-1])+')*('+recovariable+'>'+str(presentationbinning[0])+')'
	# The selection for the gen variable. Larger range for the underflow/overflow. '(Pt_genmuon1>1.0)' also demands that a gen-muon is present. 
	# The trees should otherwise be skimmed for a reco muon to be present.
	selection_response=str(selection)+'*('+genvariable+'<'+str(binning[-1])+')*('+genvariable+'>'+str(binning[1])+')*(Pt_genmuon1>1.0)'

	# Get optimal variable binning binning
	varbinning=GetConstBinStructure(binning)
	if (optvar=="v" or optvar=="V"):
		varbinning=GetIdealBinStructure(CreateHisto('h_forrebin_WJets','temptest',t_WJets_MG,recovariable,[100000*len(presentationbinning),presentationbinning[0],presentationbinning[-1]],selection_response+weight,MCGenStyle,Label),binning)

	# WJets Gen + Reco
	h_gen_WJets=CreateHisto('h_gen_WJets','W+Jets [Truth]',t_WJets_MG,genvariable,varbinning,selection_response+weight,MCGenStyle,Label)
	h_rec_WJets=CreateHisto('h_rec_WJets','W+Jets [Reco]',t_WJets_MG,recovariable,varbinning,selection_response+weight,MCRecoStyle,Label)
	# Data
	h_rec_Data=CreateHisto('h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recovariable,varbinning,selection,DataRecoStyle,Label)

	# Other Backgrounds
	h_rec_DiBoson=CreateHisto('h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recovariable,varbinning,selection_response+weight,DiBosonStackStyle,Label)
	h_rec_ZJets=CreateHisto('h_rec_ZJets','Z+Jets [Alpgen]',t_ZJets_MG,recovariable,varbinning,selection_response+weight,ZStackStyle,Label)
	h_rec_TTBar=CreateHisto('h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recovariable,varbinning,selection_response+weight,TTStackStyle,Label)
	h_rec_SingleTop=CreateHisto('h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recovariable,varbinning,selection_response+weight,StopStackStyle,Label)
	h_rec_QCDMu=CreateHisto('h_rec_QCDMu','QCD #mu-enriched [Pythia]',t_QCDMu,recovariable,varbinning,selection_response+weight,QCDStackStyle,Label)

	h_rec_Data_pseudo=PseudoDataHisto(h_rec_WJets,'h_rec_PseudoData',varbinning)
	
	## Rescaling Factor Calculation, not implemented!
	SM = [h_rec_WJets,h_rec_DiBoson,h_rec_ZJets,h_rec_TTBar,h_rec_SingleTop,h_rec_QCDMu]
	SMInt = sum(k.Integral() for k in SM)
	mcdatascale = (1.0*(h_rec_Data.GetEntries()))/SMInt
	genmcscale = (h_rec_WJets.Integral()/h_gen_WJets.Integral())

	# Print the scale factors to screen for sanity check.
	print "MC Global Scale Factor: "+str(mcdatascale)
	print "Gen-Reco Scale Factor: "+str(genmcscale)

	## Do the Drawing
	h_gen_WJets.Draw("HIST")	
	h_rec_WJets.Draw("SAME")

	# Create Legend
	FixDrawLegend(c1.cd(2).BuildLegend())
	
	##############################################################################
	#######      Top Left Plot - Normal Stacked Distributions                #######
	##############################################################################
	c1.cd(1)
	MCStack = THStack ("MCStack","")
	
	MCStack.SetMinimum(1.0)
	MCStack.SetMaximum(SMInt*100)
	
	### Make the plots without variable bins!
	hs_rec_WJets=CreateHisto('hs_rec_WJets','W+Jets [Reco]',t_WJets_MG,recovariable,presentationbinning,selection+weight,WStackStyle,Label)
	hs_rec_Data=CreateHisto('hs_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recovariable,presentationbinning,selection,DataRecoStyle,Label)
	hs_rec_DiBoson=CreateHisto('hs_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recovariable,presentationbinning,selection+weight,DiBosonStackStyle,Label)
	hs_rec_ZJets=CreateHisto('hs_rec_ZJets','Z+Jets [Alpgen]',t_ZJets_MG,recovariable,presentationbinning,selection+weight,ZStackStyle,Label)
	hs_rec_TTBar=CreateHisto('hs_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recovariable,presentationbinning,selection+weight,TTStackStyle,Label)
	hs_rec_SingleTop=CreateHisto('hs_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recovariable,presentationbinning,selection+weight,StopStackStyle,Label)
	
	# Again, scale factor calculations. Not implemented, just calculated.
	SM=[hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar,hs_rec_WJets]
	mcdatascalepres = (1.0*(hs_rec_Data.GetEntries()))/(sum(k.Integral() for k in SM))
	
	# Make a stack of SM.
	for x in SM:
		#x.Scale(mcdatascalepres) 
		MCStack.Add(x)
	
	# Draw the stack
	MCStack.Draw("HIST")
	c1.cd(1).SetLogy()

	# Make the stack look better.
	MCStack=BeautifyStack(MCStack,Label)

	# Draw the data.
	hs_rec_Data.Draw("EPSAME")

	# Create Legend
	FixDrawLegend(c1.cd(1).BuildLegend())
	gPad.RedrawAxis()


	##############################################################################
	#######      Bottom Left - Gen Versus Reco Response Matrix             #######
	##############################################################################	
	c1.cd(3)

	# 2D Histogram for WJets MC vs Reco - the response matrix.
	h_response_WJets=Create2DHisto('h_response_WJets','ResponseMatrix',t_WJets_MG,genvariable,recovariable,varbinning,selection_response+weight,[xlabel+" Reco",xlabel+" Truth"])
	h_response_WJets.Draw("COL") # Draw it with color scheme
	if (optvar=="v" or optvar=="V"): # Set log if using variable binning (i.e. large bin variations)
		c1.cd(3).SetLogx()	
		c1.cd(3).SetLogy()

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
	h_rec_Data2 = BackgroundSubtractedHistogram(h_rec_Data2,[ h_rec_DiBoson, h_rec_ZJets,h_rec_TTBar,h_rec_SingleTop])
	h_rec_Data2 = BeautifyHisto(h_rec_Data2,DataCompStyle,Label,"Data, 5/fb [Reco]")

	# These are the paramters for the unfolding [reco, gen, response]
	Params = [ h_rec_WJets, h_gen_WJets, h_response_WJets]

	# The tau optimization requires some smeared/offset histograms. Offsetting PT makes sense, but Eta does not. 
	# Turn off offsets for Eta distributions.
	should_offset=True
	if "Eta" in recovariable:
		should_offset=False
	
	# Tau is calculated only for the real unfolding. Systematics use that tau. This allows an overridee of the tau value as an argument.
	if tau_override>0:
		tau=tau_override
	else:
		#tau=2  # For quick tests only!
		tau = FindOptimalTauWithPseudoExp(Params,varbinning,should_offset) # Get the optimal tau value.

	# Perform the unfolding. Returns unfolded data histo, some unfolding parameters not currently used
	[h_unf_Data,h_dd,h_sv,optimal_tau,optimal_i] = GetSmartSVD(h_rec_Data2,Params, varbinning,tau)

	# Samme as above, but using pseudo-data from the WJets MC - this is the closure test!
	[h_unf_Data_pseudo,h_dd,h_sv_pseudo,optimal_tau_pseudo,optimal_i_pseudo] = GetSmartSVD(h_rec_Data_pseudo,Params, varbinning,tau)

	# How much would you have to scale the unfolded data to meet the reco data? Should be ~1.
	UnfScale=(h_rec_Data2.Integral()/h_unf_Data.Integral())

	# Creates plots, with extra label fiving the optimal tau and unfolding scale above.
	h_unf_Data = BeautifyHisto(h_unf_Data,DataUnfoldedStyle,Label,"Data, 5/fb [Unfolded, #tau = "+str(optimal_tau)+",R="+str(round(UnfScale,2))+"]")
	h_unf_Data_pseudo = BeautifyHisto(h_unf_Data_pseudo,DataUnfoldedStyle_pseudo,Label,"WJets Closure [Unfolded, #tau = "+str(optimal_tau)+",R="+str(round(UnfScale,2))+"]")

	# Using the unfolded data and reeco data, get a rescaling string to convert between the two types of binning.
	[DataRescalingString,DataErrorString] = GetRescaling(h_unf_Data,h_rec_Data2,varbinning,recovariable)
	# Same as above, but for the closure test.
	[DataRescalingString_pseudo,DataErrorString_pseudo] = GetRescaling(h_unf_Data_pseudo,h_rec_Data_pseudo,varbinning,recovariable)

	# Prints the unfolding scale as a sanity check
	print "Scaling of Unfolded Dist: "+str(UnfScale)

	# Draw the unfolded data, reco data, and pseudo (closure) data
	h_unf_Data.Draw("EPSAME")
	h_rec_Data2.Draw("EPSAME")
	h_unf_Data_pseudo.Draw("EPSAME")

	# Legend
	FixDrawLegend(c1.cd(2).BuildLegend())

	# This is just a fancy way of getting decent plot axis dimensions
	CompMin = 99999999999999
	CompMax= 0
	for x in range(h_gen_WJets.GetNbinsX()):
		v = h_gen_WJets.GetBinContent(x+1)
		if x==0 or x>=(h_gen_WJets.GetNbinsX() -1):
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
	if "Eta" in recovariable:
		CompMax = 5*CompMax
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
	
	c1.cd(3).Update()


	##############################################################################
	#######      Bottom Right - More legible ratio plots                   #######
	##############################################################################	
	c1.cd(4)
	#c1.cd(4).SetLogy()

	# WJets Gen + Reco
	h_pres_gen_WJets=CreateHisto('h_pres_gen_WJets','W+Jets MadGraph [Truth/Reco]',t_WJets_MG,genvariable,presentationbinning,selection_response+weight,MCRecoStyle,Label)
	h_pres_rec_WJets=CreateHisto('h_pres_rec_WJets','W+Jets  MadGraph [Truth/Reco]',t_WJets_MG,recovariable,presentationbinning,selection_response+weight,MCRecoStyle,Label)
	# Data
	h_pres_rec_Data=CreateHisto('h_pres_rec_Data','Data, 5/fb [Unfolded/Reco]',t_SingleMuData,recovariable,presentationbinning,selection,DataCompStyle,Label)
	h_pres_rec_Data_err=CreateHisto('h_pres_rec_Data_err','Data, 5/fb [Unfolded/Reco]',t_SingleMuData,recovariable,presentationbinning,selection,DataCompStyle,Label)

	h_pres_unf_Data=CreateHisto('h_pres_unf_Data','Data, 5/fb [Unfolded/Reco]',t_SingleMuData,recovariable,presentationbinning,selection+"*"+DataRescalingString,DataUnfoldedStyle,Label)
	h_pres_unf_Data_err=CreateHisto('h_pres_unf_Data_err','Data, 5/fb [Unfolded/Reco]',t_SingleMuData,recovariable,presentationbinning,selection+"*"+DataErrorString,DataUnfoldedStyle,Label)

	# Closure
	h_pres_unf_Data_pseudo=CreateHisto('h_pres_unf_Data_pseudo','MC Closure [Unf. Reco/ Gen]',t_WJets_MG,recovariable,presentationbinning,selection_response+weight+"*"+DataRescalingString_pseudo,DataUnfoldedStyle_pseudo,Label)
	h_pres_unf_Data_err_pseudo=CreateHisto('h_pres_unf_Data_err_pseudo','MC Closure [Unf. Reco/ Gen]',t_WJets_MG,recovariable,presentationbinning,selection_response+weight+"*"+DataErrorString_pseudo,DataUnfoldedStyle_pseudo,Label)

	# Other Backgrounds
	h_pres_rec_DiBoson=CreateHisto('h_pres_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recovariable,presentationbinning,selection_response+weight,DiBosonStackStyle,Label)
	h_pres_rec_ZJets=CreateHisto('h_pres_rec_ZJets','Z+Jets [Alpgen]',t_ZJets_MG,recovariable,presentationbinning,selection_response+weight,ZStackStyle,Label)
	h_pres_rec_TTBar=CreateHisto('h_pres_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recovariable,presentationbinning,selection_response+weight,TTStackStyle,Label)
	h_pres_rec_SingleTop=CreateHisto('h_pres_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recovariable,presentationbinning,selection_response+weight,StopStackStyle,Label)	

	# Make background subtracted histos.
	h_pres_rec_Data = BackgroundSubtractedHistogram(h_pres_rec_Data,[ h_pres_rec_DiBoson, h_pres_rec_ZJets,h_pres_rec_TTBar,h_pres_rec_SingleTop])
	h_pres_unf_Data = BackgroundSubtractedHistogram(h_pres_unf_Data,[ h_pres_rec_DiBoson, h_pres_rec_ZJets,h_pres_rec_TTBar,h_pres_rec_SingleTop])

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
	for x in range(binning[0]):
		M=max([h_pres_gen_WJets.GetBinContent(x),h_pres_unf_Data.GetBinContent(x)])
		m=min([h_pres_gen_WJets.GetBinContent(x),h_pres_unf_Data.GetBinContent(x)])
		if M>RelMax and M<10:
			RelMax=M
		if m<RelMin and m<10:
			RelMin=m
	RelMax*=1.5
	RelMin*=0.85
	h_pres_gen_WJets.Draw("EP")
	h_pres_gen_WJets.SetMaximum(RelMax)
	h_pres_gen_WJets.SetMinimum(RelMin)

	# Do the drawing
	h_pres_unf_Data.Draw("EPSAME")
	h_pres_unf_Data_pseudo.Draw("EPSAME")
	# Create Legend
	FixDrawLegend(c1.cd(4).BuildLegend())
	l_one.Draw("SAME")


	# Finally, print the plots as pdf and png
	c1.Print('pyplots/'+recovariable+'_'+tagname+'.pdf')
	c1.Print('pyplots/'+recovariable+'_'+tagname+'.png')

	#return the optimal dau, the bin-by-bin unfolded data and MC.
	return [tau,DataBinInfo,MCBinInfo]


# FullAnalysisWithUncertainty just runs MakeUnfoldedPlots several times for each systematic variation. The goal is to return final distributions.
def FullAnalysisWithUncertainty(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight,optvar):

	# This is the standard plot. here we get the optimal tau value. 
	[tau,data_standard,mc_standard]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight,optvar,NormalDirectory,'',-1,'standard')

	# Replacing with ScaleUp/ScaleDown samples. 
	[null,data_scale_plus,mc_scale_plus]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight,optvar,NormalDirectory,'ScaleUp',tau,'scaleup')
	[null,data_scale_minus,mc_scale_minus]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight,optvar,NormalDirectory,'ScaleDown',tau,'scaledown')
	[null,data_match_plus,mc_match_plus]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight,optvar,NormalDirectory,'MatchUp',tau,'matchup')
	[null,data_match_minus,mc_match_minus]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight,optvar,NormalDirectory,'MatchDown',tau,'matchdown')
	
	# Plleup variations
	[null,data_pileup_plus,mc_pileup_plus]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight.replace('central','sysplus8'),optvar,NormalDirectory,'',tau,'pileup_plus')
	[null,data_pileup_minus,mc_pileup_minus]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight.replace('central','sysminus8'),optvar,NormalDirectory,'',tau,'pileup_minus')

	# Integrated luminosity up/down
	[null,data_lumi_plus,mc_lumi_plus]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight.replace('4980','5090'),optvar,NormalDirectory,'',tau,'lumi_plus')
	[null,data_lumi_minus,mc_lumi_minus]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight.replace('4980','4870'),optvar,NormalDirectory,'',tau,'lumi_minus')

	# Jet energy scale up/down, and smeared
	[null,data_jetscale_plus,mc_jetscale_plus]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight,optvar,JetScaleUpDirectory,'',tau,'jetscale_plus')
	[null,data_jetscale_minus,mc_jetscale_minus]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight,optvar,JetScaleDownDirectory,'',tau,'jetscale_minus')
	[null,data_jetsmear,mc_jetsmear]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight,optvar,JetSmearDirectory,'',tau,'jetsmear')

	# Muon energy scale up/down and smeared.
	[null,data_muscale_plus,mc_muscale_plus]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight,optvar,MuScaleUpDirectory,'',tau,'muscale_plus')
	[null,data_muscale_minus,mc_muscale_minus]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight,optvar,MuScaleDownDirectory,'',tau,'muscale_minus')
	[null,data_musmear,mc_musmear]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight,optvar,MuSmearDirectory,'',tau,'musmear')	


	# Here we make a vary verbose table.	
	data_table=[['|','Bin','|','Prediction','|','DataMean','|','PU(+)','PU(-)','|','Lumi(+)','Lumi(-)','|','JScale(+)','JScale(-)','JetSmear','|','MuScale(+)','MuScale(-)','MuSmear','|','Scale(+)','Scale(-)','Match(+)','Match(-)','|']]
	for x in range(len(data_standard)): # Loop over bins of the original output table
		thisbin=(data_standard[x])[0]    # this is the bin X1--X2
		center = (data_standard[x])[1]   # The is the central value of the unfolded data
		prediction = (mc_standard[x])[1] # This is the MC prediction

		# everything below are values of the data unfolded for the various systematic variations
		scale_up = (data_scale_plus[x])[1]
		scale_down = (data_scale_minus[x])[1]
		match_up = (data_match_plus[x])[1]
		match_down = (data_match_minus[x])[1]				

		pu_up = (data_pileup_plus[x])[1]
		pu_down = (data_pileup_minus[x])[1]

		lumi_up = (data_lumi_plus[x])[1]
		lumi_down = (data_lumi_minus[x])[1]
		
		jet_up = (data_jetscale_plus[x])[1]
		jet_down = (data_jetscale_minus[x])[1]
		jet_smear = (data_jetsmear[x])[1]
		
		mu_up = (data_muscale_plus[x])[1]
		mu_down = (data_muscale_minus[x])[1]
		mu_smear = (data_musmear[x])[1]

		# Strip out the +- statistical uncertainty for the various systematics. We will only consider statistical uncertainties on the central values. 
		for v in ['pu_up','pu_down','jet_up','jet_down','jet_smear','mu_up','mu_down','mu_smear','lumi_up','lumi_down']:
			exec(v+'='+v+'.split("+-")[0]')
		
		# Add a line to the data table.
		data_table.append(['|',thisbin,'|',prediction,'|',center,'|',pu_up,pu_down,'|',lumi_up,lumi_down,'|',jet_up,jet_down,jet_smear,'|',mu_up,mu_down,mu_smear,'|',scale_up,scale_down,match_up,match_down,'|'])
	
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
		JESerrors=filter_pair([errors[4],errors[5]])
		JERerrors=[errors[6]]
		MESerrors=filter_pair([errors[7],errors[8]])
		MERerrors=[errors[9]]
		SCALEerrors=filter_pair([errors[10],errors[11]])
		MATCHerrors=filter_pair([errors[12],errors[13]])
		STATerrors=[rel_err, -rel_err]
		
		allerrors=PUerrors+LUMIerrors+JESerrors+JERerrors+MESerrors+MERerrors+SCALEerrors+MATCHerrors+STATerrors
		
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
		
	return [tex,means,err_plus, err_minus]

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
	return table	

# Quickly write a python string to a text file, creating neat spacing with whatever spacer character
def StringToFile(string,file, spacer):
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
	hout.GetXaxis().SetTitleFont(132)
	hout.GetYaxis().SetTitleFont(132)
	hout.GetXaxis().SetLabelFont(132)
	hout.GetYaxis().SetLabelFont(132)

	if plottype=="TopPlot":
		hout.GetYaxis().SetTitleFont(132);
		hout.GetXaxis().SetTitleSize(.06);
		hout.GetYaxis().SetTitleSize(.06);
		hout.GetXaxis().CenterTitle();
		hout.GetYaxis().CenterTitle();
		hout.GetXaxis().SetTitleOffset(0.8);
		hout.GetYaxis().SetTitleOffset(0.8);
		hout.GetYaxis().SetLabelSize(.05);
		hout.GetXaxis().SetLabelSize(.05);


	if plottype=="SubPlot":
		hout.GetYaxis().SetTitleFont(132);
		hout.GetXaxis().SetTitleSize(.13);
		hout.GetYaxis().SetTitleSize(.13);
		hout.GetXaxis().CenterTitle();
		hout.GetYaxis().CenterTitle();		
		hout.GetXaxis().SetTitleOffset(.28);
		hout.GetYaxis().SetTitleOffset(.28);
		hout.GetYaxis().SetLabelSize(.09);
		hout.GetXaxis().SetLabelSize(.09);

	return [hout,[mean,up,down,binset]]

# Use CreateHistoFromLists to quickly cast a Rivet NTuple into a tGraph for overlay with other plots. 
def RivetHisto(rivetfile, rivetvariable, binning,selection, label, style,original_events,normalization, nmadgraph, quantity, WRenormalizationForRivet):

	frivet = TFile.Open(rivetfile)
	trivet = frivet.Get("RivetTree")
	Name = "MadGraph"*("MadGraph" in rivetfile) + "Pythia"*("Pythia" in rivetfile) + "PROBLEM"*("MadGraph" not in rivetfile and "Pythia" not in rivetfile)
	hrivet = CreateHisto(Name,Name,trivet,rivetvariable,binning,selection+'*'+WRenormalizationForRivet,style,label)
	print 'Total Entries: ', trivet.GetEntries()
	print ' hrivet stats:    ', hrivet.GetEntries(), hrivet.Integral(), 
	print ' In Madgraph:  ', nmadgraph
	acceptance = (1.0*(hrivet.Integral()))/(1.0*original_events)
	# print 'Acceptance: ', acceptance,
	scalefactor = (4980.0*31314.0)*acceptance
	# print 'Scale: ', scalefactor
	if hrivet.Integral()>0:
		hrivet.Scale(1.0/hrivet.Integral())
	means=[]
	errs=[]
	if (scalefactor <=0):
		scalefactor=1
	rivetscale = nmadgraph/(scalefactor)

	if True:
		scalefactor=nmadgraph

	for x in range(len(binning)-1):
		means.append(scalefactor*(hrivet.GetBinContent(x+1)))
		errs.append(scalefactor*(hrivet.GetBinError(x+1)))
		# print binning[x],'-',binning[x+1],'  ', means[x], '+-',errs[x]

	if normalization==0:
		label = [label, 'Events/Bin']
	else:
		label = [label, 'd#sigma/d'+quantity+' [pb/GeV]']


	RivetOutputHisto = CreateHistoFromLists(binning, Name,label, means, errs, errs, style,normalization,"SubPlot")

	return [RivetOutputHisto,rivetscale]

# There is no built-in division for tgraphs. This does the trick. 
# For now, errors are converted into symetric errors conservatively, as one must make a choice of handling such errors. 
def DivideTGraphs(gv1, gv2,style):

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

	return CreateHistoFromLists(binset, "example",["","Data / MC"], ratmean,raterr,raterr,style,1.0,"SubPlot")[0]


# This creates the final "results"-style plot!
def FinalHisto(binning, label, quantity, filename ,expectation_means, expectation_errors, expectation_names, measurement, measurement_error_up, measurement_error_down, normalization,WRenormalizationForRivet):

	c1 = TCanvas("c1","",700,800)

	pad1 = TPad( 'pad1', 'pad1', 0.0, 0.53, 1.0, 1.0 )#divide canvas into pads
	pad2 = TPad( 'pad2', 'pad2', 0.0, 0.28, 1.0, 0.50 )
	pad3 = TPad( 'pad3', 'pad3', 0.0, 0.03, 1.0, 0.25 )


	pad1.Draw()
	pad2.Draw()
	pad3.Draw()

	pad1.SetGrid()
	pad1.SetLogy()
	pad1.cd()

	gStyle.SetOptStat(0)
	MadGraphStyle=[1001,20,.00001,1,4]
	MadGraphSubStyle=[3254,21,.7,1,4]

	MadGraphRivetSubStyle=[0*3004+3254,21,.7,1,6]


	MadGraphRivetStyle=[0*3004+1001,20,.00001,1,6]

	DataRecoStyle=[0,20,.7,1,1]	
	
	rivetname = (filename.split('/')[-1]).split('FINAL')[0]
	for x in RivetBranchMap:
		if x[0] in rivetname:
			rivetname = rivetname.replace(x[0],x[1])
	
	madgraph_NOriginal = float(((RIVETMadGraph.split('/')[-1]).split('NEvents_')[-1]).split('.root')[0])
	# print 'Rivet Origianl Events: '  , madgraph_NOriginal
	# if rivetname == 'njet_WMuNu' or rivetname=='ptjet1' or rivetname=='etajet1':
	# 	print 'NJET FOUND ' + '*'*50
	
	rivetlabel=label	
	
	Max = max(measurement)*10
	Min = min(measurement)*.5
	
	if normalization==0:
		label = [label, 'Events/Bin']
	else:
		label = [label, 'd#sigma/d'+quantity+' [pb/GeV]']
		Max=Max/normalization
		Min=Min/normalization
	
	for x in range(len(expectation_names)):
		name = expectation_names[x]
		mean_value = expectation_means[x]
		plus_errors = expectation_errors[x]
		minus_errors = expectation_errors[x]
		style=MadGraphStyle
		[Exp,Exp_verbose] = CreateHistoFromLists(binning, name,label, mean_value, plus_errors, minus_errors, style,normalization,"TopPlot")

		Exp.SetMaximum(Max)
		Exp.SetMinimum(Min)

		if x==0:
			Exp.Draw("A2")
		else:
			Exp.Draw("2")

	nmadgraph = sum(Exp_verbose[0])
	[[Rivet_MadGraph_Result,Rivet_MadGraph_Result_verbose], rivetrescale] = RivetHisto(RIVETMadGraph,rivetname,binning,"(ptmuon>45)*(abs(etamuon)<2.1)",rivetlabel,MadGraphRivetStyle,madgraph_NOriginal,normalization,nmadgraph,quantity,WRenormalizationForRivet)
	
	name="Measured"
	mean_value = measurement
	plus_errors=measurement_error_up
	minus_errors=measurement_error_down
	style=DataRecoStyle
	[Meas,Meas_verbose] = CreateHistoFromLists(binning, name,label, mean_value, plus_errors, minus_errors, style,normalization,"TopPlot")
	# if rivetname == 'njet_WMuNu' or rivetname=='ptjet1'or rivetname=='etajet1':
	Rivet_MadGraph_Result.Draw("2")
	Meas.Draw("P")

	# FixDrawLegend(c1.cd(1).BuildLegend())

	leg = TLegend(0.63,0.68,0.89,0.88,"","brNDC");
	leg.SetTextFont(132);
	leg.SetFillColor(0);
	leg.SetBorderSize(0);
	leg.SetTextSize(.04)
	leg.AddEntry(Meas,"Data (Unfolded)");
	leg.AddEntry(Exp,"MadGraph (Unfolding)");
	leg.AddEntry(Rivet_MadGraph_Result,"MadGraph (Rivet)");

	leg.Draw()

	
	sqrts = "#sqrt{s} = 7 TeV";
	l1=TLatex()
	l1.SetTextAlign(12)
	l1.SetTextFont(132)
	l1.SetNDC()
	l1.SetTextSize(0.06)
 
	l1.DrawLatex(0.37,0.94,"CMS 2011  "+sqrts)
	# l1.DrawLatex(0.13,0.76,sqrts)

	l2=TLatex()
	l2.SetTextAlign(12)
	l2.SetTextFont(132)
	l2.SetNDC()
	l2.SetTextSize(0.08)
	# l2.SetTextAngle(45);	
	l2.DrawLatex(0.6,0.60,"PRELIMINARY")
	if True:
		l2.DrawLatex(0.6,0.50,"R_{Rivet} = "+ str(round(rivetrescale,3)))


	pad2.cd()
	pad2.SetGrid()
	pad2.Draw()

	grat = DivideTGraphs(Meas_verbose,Exp_verbose,MadGraphSubStyle)

	grat.SetMinimum(0)
	grat.SetMaximum(2)


	grat.Draw("ap2")




	# if rivetname == 'njet_WMuNu' or rivetname=='ptjet1'or rivetname=='etajet1':

	pad3.cd()
	pad3.SetGrid()
	pad3.Draw()

	grat2 = DivideTGraphs(Meas_verbose,Rivet_MadGraph_Result_verbose,MadGraphRivetSubStyle)
	grat2.SetMinimum(0)
	grat2.SetMaximum(2)
	grat2.Draw("ap2")


	c1.Print(filename+'pdf')
	c1.Print(filename+'png')

	# if 'jet1' in filename:
	# sys.exit()

def ParseTablesToFinalResults(WRenormalizationForRivet):
	allfiles = glob('pyplots/*txt')
	for f in allfiles:
		if 'FINAL' in f:
			continue
			
		print 'Analyzing table: ',f
		output = f.replace('.txt','FINAL.')
		table = tabletolist(f)

		[tablebinning,rootbinning] = getbinning(table)
		[pred_tex, pred_mean, pred_err] = getcolumn(table,1)
		[meas_tex, meas_mean, meas_err_plus, meas_err_minus] = getmeasurement(table)
		
		StringToFile(TexTableFromColumns([tablebinning,pred_tex,meas_tex]), output+'TexCount.txt', ',') 
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

		if label=='PFJet40Count':
			label = 'Jet Count (Exclusive)'
			quantity = 'N_{Jet}'

		if label=='MT_muon1MET':
			label = 'M_{T}(#mu,E_{T}^{miss}) [GeV]'
			quantity = 'M_{T}'

		if label=='Pt_MET':
			label = 'E_{T}^{miss} [GeV]'
			quantity = 'E_{T}^{miss}'

		if label=='DeltaPhi_pfjet5muon1':
			label = '#Delta #phi(jet_{1},#mu)'	
			quantity = '#Delta #phi(jet_{1},#mu)'

		if label=='DeltaPhi_pfjet5muon1':
			label = '#Delta #phi(jet_{2},#mu)'	
			quantity = '#Delta #phi(jet_{2},#mu)'

		if label=='DeltaPhi_pfjet5muon1':
			label = '#Delta #phi(jet_{3},#mu)'	
			quantity = '#Delta #phi(jet_{3},#mu)'

		if label=='DeltaPhi_pfjet5muon1':
			label = '#Delta #phi(jet_{4},#mu)'	
			quantity = '#Delta #phi(jet_{4},#mu)'

		if label=='DeltaPhi_pfjet5muon1':
			label = '#Delta #phi(jet_{5},#mu)'	
			quantity = '#Delta #phi(jet_{5},#mu)'

		
		FinalHisto(rootbinning,label,quantity, output+'PlotCount.', prediction_means, prediction_errors, prediction_names, meas_mean, meas_err_plus, meas_err_minus,0,WRenormalizationForRivet)
		FinalHisto(rootbinning,label,quantity, output+'PlotXSec.', prediction_means, prediction_errors, prediction_names, meas_mean, meas_err_plus, meas_err_minus,4980.0,WRenormalizationForRivet)

		#os.system('cat pyplots/Pt_pfjet1FINAL.TexCount.txt')

main()





