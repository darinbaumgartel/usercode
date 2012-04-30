import os
import sys
import math
sys.argv.append( '-b' )
from ROOT import *
gROOT.ProcessLine("gErrorIgnoreLevel = 2001;")
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

# Directory where root files are kept and the tree you want to get root files from
#FileDirectory = 
'/afs/cern.ch/user/d/darinb/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_QCD_QCDSelections_4p7fb_Jan20_2012_01_25_21_20_57/SummaryFiles/'
FileDirectory = '/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_WPlusJets_WJetsV2_2012_04_27_19_09_02/SummaryFiles/'
TreeName = "PhysicalVariables"

selection = '((Pt_muon1>45)*(Pt_MET>30)*(abs(Eta_muon1)<2.1)*(MT_muon1MET>50))'
selectiondata='((Pt_muon1>45)*(Pt_MET>30)*(abs(Eta_muon1)<2.1)*(MT_muon1MET>50))'
weight = '*weight_pu_central*4980*0.92'

# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
	exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
#tmpfile = TFile("tmp.root","RECREATE")

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

def Create2DHisto(name,legendname,tree,variable1,variable2,binning,selection,label):
	hout= TH2D(name,legendname,binning[0],binning[1],binning[2],binning[0],binning[1],binning[2])
	tree.Project(name,variable2+":"+variable1,selection)
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

def SmearOffsetHisto(histo,newname,binning):
	hout= TH1D(newname,"",binning[0],binning[1],binning[2])
	bincontent=[]
	binx=[]
	for x in range(binning[0]):
		bincontent.append(int(round(histo.GetBinContent(x))))
		binx.append(histo.GetBinCenter(x))
	
	offset=(numpy.random.normal(1.0,0.1))-1.0
	resolution=abs((numpy.random.normal(1.0,0.1))-1.0)

	for n in range(len(binx)):
		for y in range(bincontent[n]):
			outputx=(1.0+offset)*(rnd.Gaus(binx[n],resolution*binx[n]))
			if outputx<=binning[2] and outputx>=binning[1]:
				hout.Fill(outputx)
	
	hout.Scale(histo.Integral()/hout.Integral())
	return hout

def GetSVD(data_histo,Params, tau):
	TheUnfolding= TSVDUnfold( data_histo, Params[0], Params[1], Params[2] )
	output = TheUnfolding.Unfold( tau )
	return output

def SimpleDifFromTwoHistos(histo1,histo2,binning):
	dif = 0
	for x in range(binning[0]-1):
		if x<1:
			continue
		b1 = histo1.GetBinContent(x)
		b2 = histo2.GetBinContent(x)
		dif += (b1-b2)*(b1-b2)

	return dif

def TestSVDTau( Params, tau ,binning,N):
	DifValues = []
	for x in range(N):
		hsmear = SmearOffsetHisto(Params[0],'hsmear',binning)
		hunf = GetSVD(hsmear,Params,tau)
		DifValues.append(SimpleDifFromTwoHistos(hunf,Params[0],binning))
		
		del hsmear,hunf
	DifAverage = sum(DifValues)/(1.0*N)
	return DifAverage
	
def FindOptimalTauWithPseudoExp(Params,binning):
	n = binning[0]
	bestdif = 9999999999
	bsettau=9999999999
	n = int(round(.25*n))
	for t in range(n):
		if t<1: 
			continue
		if t>n-1:
			continue
		dif=(TestSVDTau(Params,t,binning,25))
		print '      ...Initial test of tau = '+str(t)+'   ChiSquared = '+str(dif)

		if dif<bestdif:
			bestdif=dif
			besttau=t
			
	centertau=besttau
	testtaus=[centertau-1,centertau,centertau+1]
	
	bestdif2 = 9999999999
	bsettau2=9999999999
	for t in testtaus:
		if t<1: 
			continue
		dif=(TestSVDTau(Params,t,binning,250))
		print '      ...Further checks on tau = '+str(t)+'   ChiSquared = '+str(dif)

		if dif<bestdif2:
			bestdif2=dif
			besttau2=t	
	
	
	print '      Optimal tau found at tau = '+str(besttau2)+'.\n'
	return besttau2
	

def FindOptimalTauFromWithDVals(data_histo,Params):
	TheUnfolding= TSVDUnfold( data_histo, Params[0], Params[1], Params[2] )
	output = TheUnfolding.Unfold( 1 )
	d=TheUnfolding.GetD()
	sv = TheUnfolding.GetSV()
	n = d.GetSize()-2

	lastd=999999999999999999
	
	for x in range(n):
		if x<1:
			continue
		dbin = d.GetBinContent(x)
		svbin = sv.GetBinContent(x)

		#print str(x)+' '*(6-len(str(x)))+str(dbin)
		#print str(x)+' '*(6-len(str(x)))+str(svbin)

		#if lastd<dbin:
		if dbin<1.0:
			print "\n    Choosing optimal tau = "+str(int(round(svbin)))+'\n'
			return int(round(svbin))
		lastd=dbin
		
		
def MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,selection):
	print "\n     Performing unfolding analysis for "+recovariable+" in "+str(binning[0]) +" bins from "+str(binning[1])+" to "+str(binning[2])+"  ... \n"
	# Create Canvas
	c1 = TCanvas("c1","",1000,700)
	c1.Divide(2,2)
	gStyle.SetOptStat(0)

	# These are teh style parameters for certain plots - [FillStyle,MarkerStyle,MarkerSize,LineWidth,Color]
	MCGenStyle=[0,20,.00001,2,2]
	MCGenSmearStyle=[0,20,.00001,2,9]

	MCRecoStyle=[0,20,.00001,2,4]
	DataRecoStyle=[0,20,.7,2,1]
	BlankRecoStyle=[0,20,.00001,2,0]
	DataUnfoldedStyle=[0,20,0.7,2,2]
	# X and Y axis labels for plot
	Label=[xlabel,"Events/Bin"]

	WStackStyle=[3007,20,.00001,2,6]
	TTStackStyle=[3005,20,.00001,2,4]
	ZStackStyle=[3004,20,.00001,2,2]
	DiBosonStackStyle=[3006,20,.00001,2,3]
	StopStackStyle=[3008,20,.00001,2,9]


	##############################################################################
	#######      First Plot - Background Subtracted Distributions          #######
	##############################################################################
	# Go to first canvas spot
	c1.cd(2)
	#c1.cd(2).SetLogy()
	# Below the CreateHisto function is used to get 1D histograms.
	# WJets Gen + Reco
	h_gen_WJets=CreateHisto('h_gen_WJets','W+Jets [Truth]',t_WJets_MG,genvariable,binning,selection+weight,MCGenStyle,Label)
	h_rec_WJets=CreateHisto('h_rec_WJets','W+Jets [Reco]',t_WJets_MG,recovariable,binning,selection+weight,MCRecoStyle,Label)
	# Data
	h_rec_Data=CreateHisto('h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recovariable,binning,selection,DataRecoStyle,Label)
	# Other Backgrounds
	h_rec_DiBoson=CreateHisto('h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recovariable,binning,selection+weight,DiBosonStackStyle,Label)
	h_rec_ZJets=CreateHisto('h_rec_ZJets','Z+Jets [Alpgen]',t_ZJets_MG,recovariable,binning,selection+weight,ZStackStyle,Label)
	h_rec_TTBar=CreateHisto('h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recovariable,binning,selection+weight,TTStackStyle,Label)
	h_rec_SingleTop=CreateHisto('h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recovariable,binning,selection+weight,StopStackStyle,Label)
	
	SM = [h_rec_WJets,h_rec_DiBoson,h_rec_ZJets,h_rec_TTBar,h_rec_SingleTop]
	SMInt = sum(k.Integral() for k in SM)
	
	scale = (1.0*(h_rec_Data.GetEntries()))/SMInt
	for x in SM:
		x.Scale(scale)
	
	print "MC Global Scale Factor: "+str(scale)
	print "Gen-Reco Scale Factor: "+str(h_rec_WJets.Integral()/h_gen_WJets.Integral())

	h_gen_WJets.Scale(h_rec_WJets.Integral()/h_gen_WJets.Integral())

	#Draw
	h_rec_WJets.Draw("")
	h_gen_WJets.Draw("SAME")

	# Create Legend
	FixDrawLegend(c1.cd(2).BuildLegend())
	
	##############################################################################
	#######      Second Plot - Normal Stacked Distributions                #######
	##############################################################################
	# Go to first canvas spot
	c1.cd(1)
	c1.cd(1).SetLogy()
	MCStack = THStack ("MCStack","")
	
	h_rec_WJets2 = h_rec_WJets.Clone()
	h_rec_WJets2 = BeautifyHisto(h_rec_WJets2,WStackStyle,Label,"W+Jets [MG]")
	MCStack.Add(h_rec_SingleTop)
	MCStack.Add(h_rec_DiBoson)
	MCStack.Add(h_rec_ZJets)
	MCStack.Add(h_rec_TTBar)
	MCStack.Add(h_rec_WJets2)
	
	MCStack.Draw("")
	MCStack=BeautifyStack(MCStack,Label)
	gPad.RedrawAxis()
	h_rec_Data.Draw("EPSAME")

	
	# Create Legend
	FixDrawLegend(c1.cd(1).BuildLegend())


	##############################################################################
	#######      Second Plot - Gen Versus Reco Response Matrix             #######
	##############################################################################	
	c1.cd(3)
	#c1.cd(3).SetLogx()
	#c1.cd(3).SetLogy()
	#GlobalScale = '*'+str((h_rec_Data.Integral())/(h_rec_WJets.Integral()))
	h_response_WJets=Create2DHisto('h_response_WJets','ResponseMatrix',t_WJets_MG,genvariable,recovariable,binning,selection+weight,[xlabel+" Truth",xlabel+" Reco"])
	h_response_WJets.Draw("COL")
	
	
	##############################################################################
	#######      Fourth Plot  - UnFolded Distribution                      #######
	##############################################################################	
	c1.cd(4)
	#c1.cd(4).SetLogy()
	# Subtract other backgrounds from Data using the BackgroundSubtractedHistogram function.
	h_rec_Data2= h_rec_Data.Clone()
	h_rec_Data2 = BackgroundSubtractedHistogram(h_rec_Data2,[ h_rec_DiBoson, h_rec_ZJets,h_rec_TTBar,h_rec_SingleTop])
		
	Params = [h_gen_WJets, h_rec_WJets, h_response_WJets]
	#tau = FindOptimalTauWithPseudoExp(Params,binning)
	tau = FindOptimalTauFromWithDVals(h_rec_Data2,Params)
	#tau=3
	SVD= TSVDUnfold( h_rec_Data2, h_gen_WJets, h_rec_WJets, h_response_WJets )
	h_unf_Data = SVD.Unfold( tau )

	UnfScale=(h_rec_Data2.Integral()/h_unf_Data.Integral())
	h_unf_Data = BeautifyHisto(h_unf_Data,DataUnfoldedStyle,Label,"Data, 5/fb [Unfolded, #tau = "+str(tau)+",R="+str(round(UnfScale,2))+"]")

	print "Scaling of Unfolded Dist: "+str(UnfScale)

	#h_unf_Data.Scale(h_rec_Data2.Integral()/h_unf_Data.Integral())

	h_unf_Data.Draw("")
	h_rec_Data2.Draw("EPSAME")
	FixDrawLegend(c1.cd(4).BuildLegend())


	c1.Print('pyplots/'+recovariable+'.pdf')
	c1.Print('pyplots/'+recovariable+'.png')

j1="*(Pt_pfjet1>30)"
j2=j1+"*(Pt_pfjet2>30)"
j3=j2+"*(Pt_pfjet3>30)"
j4=j3+"*(Pt_pfjet4>30)"


MakeUnfoldedPlots('Pt_genmuon1','Pt_muon1',"p_{T}(#mu) [GeV]",[50,00,500],selection)
MakeUnfoldedPlots('MT_genmuon1genMET','MT_muon1MET',"M_{T}(#mu,E_{T}^{miss}) [GeV]",[50,00,500],selection)
MakeUnfoldedPlots('Pt_genMET','Pt_MET',"E_{T}^{miss} [GeV]",[50,00,500],selection)


MakeUnfoldedPlots('Pt_genjet1','Pt_pfjet1',"p_{T}(jet_{1}) [GeV]",[50,00,500],selection+j1)
MakeUnfoldedPlots('Pt_genjet2','Pt_pfjet2',"p_{T}(jet_{2}) [GeV]",[50,00,500],selection+j2)
MakeUnfoldedPlots('Pt_genjet3','Pt_pfjet3',"p_{T}(jet_{3}) [GeV]",[50,00,500],selection+j3)
MakeUnfoldedPlots('Pt_genjet4','Pt_pfjet4',"p_{T}(jet_{4}) [GeV]",[50,00,500],selection+j4)

