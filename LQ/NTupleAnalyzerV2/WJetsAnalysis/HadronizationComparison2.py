import os
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

RIVETMadGraph='/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVET/Madgraph_tree_NEvents_93530000.root'
# RIVETMadGraphNonHad='/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVETNonHadronized/Madgraph_tree_NEvents_93530000.root'
# RIVETMadGraphNonHad='/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVETNonHadronized/Madgraph_treeV2_NEvents_93932145.root'
# RIVETShoweredNonHadronized='/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVETShoweredNonHadronized/Madgraph_tree_NEvents_91939543.root'
RIVETMadGraphModA = '/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVETNonHadronized/Madgraph_ModA_tree_NEvents_92146299.root'
RIVETMadGraphModB = '/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVETNonHadronized/Madgraph_ModB_tree_NEvents_92213415.root'

t_norm = TFile.Open(RIVETMadGraph,'READ').Get('RivetTree')
t_A = TFile.Open(RIVETMadGraphModA,'READ').Get("RivetTree")
t_B = TFile.Open(RIVETMadGraphModB,'READ').Get("RivetTree")


n_norm = 1.0*float(RIVETMadGraph.split('_')[-1].replace('.root',''))
n_A = 1.0*float(RIVETMadGraphModA.split('_')[-1].replace('.root',''))
n_B = 1.0*float(RIVETMadGraphModB.split('_')[-1].replace('.root',''))


w_norm = '*(evweight)*(31314.0*5000.0/'+str(n_norm)+')'
w_A = '*(evweight)*(31314.0*5000.0/'+str(n_A)+')'
w_B = '*(evweight)*(31314.0*5000.0/'+str(n_B)+')'


sel = '(mt_mumet>50)*(ptmuon>25)*(abs(etamuon)<2.1)'
gj1="*(ptjet1>30.0)*(etajet1>-2.4)*(etajet1<2.4)"
gj2="*(ptjet2>30.0)*(etajet2>-2.4)*(etajet2<2.4)"
gj3="*(ptjet3>30.0)*(etajet3>-2.4)*(etajet3<2.4)"
gj4="*(ptjet4>30.0)*(etajet4>-2.4)*(etajet4<2.4)"

sel += gj1

def main():
	setTDRStyle()

	HadPlot('ptjet1',"p_{T}(jet_{1}) [GeV]",[30,50,70,90,110,150,190,250,310,400,750],sel)
	HadPlot('ptjet2',"p_{T}(jet_{2}) [GeV]",[30,50,70,90,110,150,190,250,550],sel+gj2)
	HadPlot('ptjet3',"p_{T}(jet_{3}) [GeV]",[30,50,70,90,110,150,210,450],sel+gj2+gj3)
	HadPlot('ptjet4',"p_{T}(jet_{4}) [GeV]",[30,50,70,90,350],sel+gj2+gj3+gj4)

	HadPlot('etajet1',"#eta(jet_{1})",[24,-2.4,2.4],sel)
	HadPlot('etajet2',"#eta(jet_{2})",[24,-2.4,2.4],sel+gj2)
	HadPlot('etajet3',"#eta(jet_{3})",[8,-2.4,2.4],sel+gj2+gj3)
	HadPlot('etajet4',"#eta(jet_{4})",[6,-2.4,2.4],sel+gj2+gj3+gj4)

	HadPlot('dphijet1muon',"#Delta#phi(jet_{1},#mu) [GeV]",[20,0,3.1415927],sel)
	HadPlot('dphijet2muon',"#Delta#phi(jet_{2},#mu) [GeV]",[15,0,3.1415927],sel+gj2)
	HadPlot('dphijet3muon',"#Delta#phi(jet_{3},#mu) [GeV]",[10,0,3.1415927],sel+gj2+gj3)
	HadPlot('dphijet4muon',"#Delta#phi(jet_{4},#mu) [GeV]",[6,0,3.1415927],sel+gj2+gj3+gj4)

	HadPlot('njet_WMuNu',"N_{Jet}",[4 ,0.5,4.5],sel)	


ttmp = TFile.Open("ttmp.root","REACREATE")


# All binning is passed as variable binning. This converts constant to variable.
def ConvertBinning(binning):
	binset=[]
	if len(binning)==3:
		for x in range(binning[0]+1):
			binset.append(((binning[2]-binning[1])/(1.0*binning[0]))*x*1.0+binning[1])
	else:
		binset=binning
	return binset

def CreateHisto(name,legendname,tree,variable,binning,selection,style,label,plottype):
	# tmpfile = TFile.Open('tmp'+str(random.randint(0,100000000))+str(random.randint(0,100000000))+'.root',"RECREATE")
	# print 'Creating histo for ',name, legendname,
	binset=ConvertBinning(binning) # Assure variable binning
	n = len(binset)-1 # carry the 1
	# print '   ... bins created.'
	hout= TH1D(name,legendname,n,array('d',binset)) # Declar empty TH1D
	hout.Sumw2() # Store sum of squares
	# print '   ... histo initialized.'
	print 'Using:',selection
	tree.Project(name,variable,selection) # Project from branch to histo
	print 'Found entries,integral:',hout.GetEntries(),hout.Integral()
	# print '   ... projection complete.'
	
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
		hout.GetXaxis().SetTitleSize(.07);
		hout.GetYaxis().SetTitleSize(.07);
		hout.GetXaxis().CenterTitle();
		hout.GetYaxis().CenterTitle();		
		hout.GetXaxis().SetTitleOffset(.33);
		hout.GetYaxis().SetTitleOffset(.33);
		hout.GetYaxis().SetLabelSize(.04);
		hout.GetXaxis().SetLabelSize(.04);

	# Good old-fashioned times new roman.
	hout.GetXaxis().SetTitleFont(42)
	# print '  ... set title font x'
	hout.GetYaxis().SetTitleFont(42)
	# print '  ... set title font y'
	hout.GetXaxis().SetLabelFont(42)
	# print '  ... set label font x'
	hout.GetYaxis().SetLabelFont(42)
	# print '  ... set label font y'

	# print '   ... style modified.'
	# os.system('sleep 1')
	# print '   ... Histogram complete:',name, legendname
	# tmpfile.Write()
	# tmpfile.Close()

	return hout

# Small function to clean up a TLegend style
def FixDrawLegend(legend):
	legend.SetTextFont(42)
	legend.SetFillColor(0)
	legend.SetBorderSize(0)
	legend.Draw()
	return legend


def HadPlot(var,name,bins,sel):
	style_norm =[0,20,1,1,1]
	style_A =	[0,21,1,1,2]
	style_B =	[0,22,1,1,4]

	h_norm = CreateHisto("h_norm","[Normal]",t_norm,var,bins,sel+w_norm,style_norm,[name,"Events/Bin"],"TopPlot")
	h_A = CreateHisto("h_A","[Mod A]",t_A,var,bins,sel+w_A,style_A,[name,"Events/Bin"],"TopPlot")
	h_B = CreateHisto("h_B","[Mod B]",t_B,var,bins,sel+w_B,style_B,[name,"Events/Bin"],"TopPlot")


	c1 = TCanvas("c1","",700,800)

	pad1 = TPad( 'pad1', 'pad1', 0.0, 0.41, 1.0, 1.0 )#divide canvas into pads
	pad2 = TPad( 'pad2', 'pad2', 0.0, 0.02, 1.0, 0.41 )

	pad1.SetBottomMargin(0.0)
	pad1.SetTopMargin(0.1)
	pad1.SetLeftMargin(0.12)
	pad1.SetRightMargin(0.1)

	pad2.SetBottomMargin(0.3)
	pad2.SetTopMargin(0.0)
	pad2.SetLeftMargin(0.12)
	pad2.SetRightMargin(0.1)

	pad1.SetGridx()
	pad1.SetGridy()


	pad1.Draw()
	pad2.Draw()

	# pad1.SetGrid()
	pad1.SetLogy()
	pad1.cd()

	h_norm.Draw("EPHIST")
	h_A.Draw("EPHISTSAME")
	h_B.Draw("EPHISTSAME")

	h_norm.Draw("HISTSAME")
	h_A.Draw("HISTSAME")
	h_B.Draw("HISTSAME")

	leg = TLegend(0.67,0.73,0.86,0.86,"","brNDC");
	leg.SetTextFont(42);
	leg.SetFillColor(0);
	leg.SetBorderSize(0);
	leg.SetTextSize(.04)
	leg.AddEntry(h_norm,"[Normal]");
	leg.AddEntry(h_A,"[Mod A]");
	leg.AddEntry(h_B,"[Mod B]");

	leg.Draw()

	pad2.cd()
	pad2.SetGridy()
	pad2.Draw()



	h_norm2 = CreateHisto("h_norm2","[Normal]",t_norm,var,bins,sel+w_norm,style_norm,[name,"Events/Bin"],"SubPlot")
	h_A2 = CreateHisto("h_A2","[Mod A]",t_A,var,bins,sel+w_A,style_A,[name,"Events/Bin"],"SubPlot")
	h_B2 = CreateHisto("h_B2","[Mod B]",t_B,var,bins,sel+w_B,style_B,[name,"Events/Bin"],"SubPlot")

	h_A2.SetMaximum(1.299)
	h_A2.SetMinimum(0.75)
	h_A2.GetXaxis().SetTitle(name)
	h_A2.GetYaxis().SetTitle("Ratio")
	h_A2.GetXaxis().SetTitleOffset(.73);

	h_A2.GetYaxis().SetTitleFont(42);
	h_A2.GetXaxis().SetTitleSize(.08);
	h_A2.GetYaxis().SetTitleSize(.08);
	h_A2.GetXaxis().CenterTitle(0);
	h_A2.GetYaxis().CenterTitle(1);
	h_A2.GetXaxis().SetTitleOffset(0.88);
	h_A2.GetYaxis().SetTitleOffset(0.45);
	h_A2.GetYaxis().SetLabelSize(.06);
	h_A2.GetXaxis().SetLabelSize(.06);
	unity=TLine(h_A2.GetXaxis().GetXmin(), 1.0 , h_A2.GetXaxis().GetXmax(),1.0)




	h_A2.Divide(h_norm2)
	h_B2.Divide(h_norm2)

	h_A2.Draw("EPHIST")
	h_B2.Draw("EPHISTSAME")
	h_A2.Draw("HISTSAME")
	h_B2.Draw("HISTSAME")
	unity.Draw("SAME")

	leg2= TLegend(0.65,0.85,0.88,0.95,"","brNDC");
	leg2.SetTextFont(42);
	leg2.SetFillColor(0);
	leg2.SetBorderSize(0);
	leg2.SetTextSize(.05)
	leg2.AddEntry(h_A2,"[Mod A]/[Normal]");
	leg2.AddEntry(h_B2,"[Mod B]/[Normal]");

	leg2.Draw()


	c1.Print('HadronizationPlots/'+var+'.pdf')
	c1.Print('HadronizationPlots/'+var+'.png')





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
