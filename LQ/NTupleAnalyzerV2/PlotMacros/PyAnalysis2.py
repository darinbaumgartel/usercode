import os
import sys
import math
sys.argv.append( '-b' )
from ROOT import *

# Clean up root style
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

# Directory where root files are kept and the tree you want to get root files from
FileDirectory = '/afs/cern.ch/user/d/darinb/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_QCD_QCDSelections_4p7fb_Jan20_2012_01_25_21_20_57/SummaryFiles/'
TreeName = "PhysicalVariables"

selection = '((Pt_muon1>40)*(Pt_muon2<40.0)*(MET_pf>20)*(MET_pfsig>50)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(abs(Eta_muon1)<2.1))*(MT_muon1pfMET>50)*(MT_muon1pfMET<110)*((TrkIso_muon1/Pt_muon1) < 0.1)'
weight = '*weight_pileup4p7fb_higgs*4700'

# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
	exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
tmpfile = TFile("tmp.root","RECREATE")

def FixDrawLegend(legend):
	legend.SetTextFont(132)
	legend.SetFillColor(0)
	legend.SetBorderSize(0)
	legend.Draw()

def CreateHisto(name,legendname,tree,variable,binning,selection,style,label):
	hout= TH1D(name,legendname,binning[0],binning[1],binning[2])
	tree.Project(name,variable,selection)

	hout.SetFillStyle(style[0])
	hout.SetMarkerStyle(style[1])
	hout.SetMarkerSize(style[2])
	hout.SetLineWidth(style[3])
	hout.SetMarkerColor(style[4])
	hout.SetLineColor(style[4])
	hout.SetFillColor(style[4])
	hout.SetFillColor(style[4])

	hout.GetXaxis().SetTitle(label[0])
	hout.GetYaxis().SetTitle(label[1])
	hout.GetXaxis().SetTitleFont(132)
	hout.GetYaxis().SetTitleFont(132)
	hout.GetXaxis().SetLabelFont(132)
	hout.GetYaxis().SetLabelFont(132)
	
	return hout

def BackgroundSubtractedHistogram(data,backgrounds):
	for b in backgrounds:
		b.Scale(-1)
		data.Add(b)
		b.Scale(-1)
	return data

def MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,selection):
	c1 = TCanvas("c1","",1200,1000)
	c1.Divide(2,2)
	gStyle.SetOptStat(0)

	c1.cd(1)
	
	MCGenStyle=[0,20,.00001,2,2]
	MCRecoStyle=[0,20,.00001,2,4]
	DataRecoStyle=[0,20,.7,2,1]
	BlankRecoStyle=[0,20,.00001,2,0]

	Label=[xlabel,"Events/Bin"]

	# WJets Gen + Reco
	h_gen_WJets=CreateHisto('h_gen_WJets','W+Jets [Truth]',t_WJets_Sherpa,genvariable,binning,selection+weight,MCGenStyle,Label)
	h_rec_WJets=CreateHisto('h_rec_WJets','W+Jets [Reco]',t_WJets_Sherpa,recovariable,binning,selection+weight,MCRecoStyle,Label)
	
	# Data
	h_rec_Data=CreateHisto('h_rec_Data','CMS Data, 5/fb [Reco]',t_SingleMuData,recovariable,binning,selection,DataRecoStyle,Label)
	
	# Other Backgrounds
	h_rec_DiBoson=CreateHisto('h_rec_DiBoson','',t_DiBoson,recovariable,binning,selection+weight,BlankRecoStyle,Label)
	h_rec_ZJets=CreateHisto('h_rec_ZJets','',t_ZJets_Sherpa,recovariable,binning,selection+weight,BlankRecoStyle,Label)
	h_rec_TTBar=CreateHisto('h_rec_TTBar','',t_TTBar,recovariable,binning,selection+weight,BlankRecoStyle,Label)
	h_rec_SingleTop=CreateHisto('h_rec_SingleTop','',t_SingleTop,recovariable,binning,selection+weight,BlankRecoStyle,Label)

	# Subtract other backgrounds from Data
	h_rec_Data=BackgroundSubtractedHistogram(h_rec_Data,[ h_rec_DiBoson, h_rec_ZJets,h_rec_TTBar,h_rec_SingleTop])

	#Draw
	h_gen_WJets.Draw()
	h_rec_WJets.Draw("SAME")
	h_rec_Data.Draw("EPSAME")


	FixDrawLegend(c1.cd(1).BuildLegend())
	
	c1.Print('pyplots/test'+recovariable+'.pdf')

MakeUnfoldedPlots('Pt_genjet1','Pt_pfjet1',"p_{T}(jet_{1}) [GeV]",[50,30,530],selection)