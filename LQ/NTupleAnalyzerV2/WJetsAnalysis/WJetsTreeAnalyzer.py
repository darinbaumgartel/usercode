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

selection = '(Pt_muon1>45)*(Pt_MET>30)*(abs(Eta_muon1)<2.1)*(MT_muon1MET>50)'
#selectiondata='((Pt_muon1>45)*(Pt_MET>30)*(abs(Eta_muon1)<2.1)*(MT_muon1MET>50))'
weight = '*weight_pu_central*4980*0.92'

# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
	exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
tmpfile = TFile("tmp.root","RECREATE")

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
	tree.Project(name,variable,selection)
	hout.SetFillStyle(style[0])
	hout.SetMarkerStyle(style[1])
	hout.SetMarkerSize(style[2])
	hout.SetLineWidth(style[3])
	hout.SetMarkerColor(style[4])
	hout.SetLineColor(style[4])
	hout.SetFillColor(style[4])
	hout.SetFillColor(style[4])
	hout.SetMaximum(2.0*hout.GetMaximum())
	hout.GetXaxis().SetTitle(label[0])
	hout.GetYaxis().SetTitle(label[1])
	hout.GetXaxis().SetTitleFont(132)
	hout.GetYaxis().SetTitleFont(132)
	hout.GetXaxis().SetLabelFont(132)
	hout.GetYaxis().SetLabelFont(132)
	return hout

def CreateRandomWeightlessHisto(name,legendname,tree,variable,binning,selection,weight,style,label):
	htest= TH1D("htest",legendname,1,0,2)
	ttest = tree.CopyTree(selection)

	ttest.Project('htest',"1",selection+'*('+variable+'>'+str(binning[1])+')*('+variable+'<'+str(binning[2])+')')
	TargetN=htest.Integral()
	print htest.GetEntries()
	print TargetN
	W=[]
	V=[]
	for x in range(ttest.GetEntries()):
		ttest.GetEntry(x)
		exec('W.append(ttest.'+weight+')')
		exec('V.append(ttest.'+variable+')')
	
	s = sum(W)
	P=[TargetN*k/s for k in W]

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
	binset=ConvertBinning(binning)
	n = len(binset)-1
	hout= TH2D(name,legendname,n,array('d',binset),n,array('d',binset))
	tree.Project(name,variable1+":"+variable2,selection)
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
	binset=ConvertBinning(binning)
	n = len(binset)-1
	
	hout= TH1D(newname,"",n,array('d',binset))
	bincontent=[]
	binx=[]
	for x in range(n):
		bincontent.append(int(round(histo.GetBinContent(x))))
		binx.append(histo.GetBinCenter(x))
	
	offset=(numpy.random.normal(1.0,0.10))-1.0
	#resolution=abs((numpy.random.normal(1.0,0.03))-1.0)
	resolution = 0.1
	maxbin=max(binset)
	minbin=min(binset)
	
	for a in range(len(binx)):
		for y in range(bincontent[a]):
			outputx=(1.0+offset)*(rnd.Gaus(binx[a],resolution*binx[a]))
			if outputx<=maxbin and outputx>=minbin:
				hout.Fill(outputx)
	#hout.Scale(histo.Integral()/hout.Integral())
	return hout
	
def GetSVD(data_histo,Params, tau, binning):
	data=data_histo.Clone()
	binset=ConvertBinning(binning)
	n = len(binset)-1
	statcov = TH2D("statcov", "covariance matrix", n, array('d',binset),n,array('d',binset))	
	for i in range(data.GetNbinsX()):
		 statcov.SetBinContent(i,i,data.GetBinError(i)*data.GetBinError(i)) 
		 	
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

def GetSmartSVD(data_histo,Params, binning,forcetau):
	data=data_histo.Clone()
	binset=ConvertBinning(binning)
	n = len(binset)-1
	statcov = TH2D("statcov", "covariance matrix", n, array('d',binset),n,array('d',binset))	
	for i in range(data.GetNbinsX()):
		 statcov.SetBinContent(i,i,data.GetBinError(i)*data.GetBinError(i)) 
		 	
	tsvdunf_prep= TSVDUnfold( data_histo, statcov, Params[0], Params[1], Params[2] )
	tsvdunf_prep.SetNormalize( kFALSE ) 
	unfres_prep = tsvdunf_prep.Unfold( 1 )	
	# Get the distribution of the d to cross check the regularization
	# - choose kreg to be the point where |d_i| stop being statistically significantly >>1
	ddist_prep = tsvdunf_prep.GetD()
	svdist_prep = tsvdunf_prep.GetSV()

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

def GetNSmearedHistos(inputhisto,binning,N):
	histos=[]
	for x in range(N):
		print 'generating smeared histogram '+str(x)
		name='hsmear'+str(x)
		histos.append(SmearOffsetHisto(inputhisto,name,binning))
	return histos

def TestSVDTau( Params, tau ,histos,binning):
	DifValues = []
	InitialDifs=[]
	N=0.0
	for hsmear in histos:
		N+=1.0
		hsmear
		hunf = GetSVD(hsmear,Params,tau,binning)[0]
		DifValues.append(SimpleDifFromTwoHistos(hunf,Params[1],binning))
		InitialDifs.append(SimpleDifFromTwoHistos(hsmear,Params[1],binning))
	
	#for x in range(len(InitialDifs)):
		#print str((DifValues[x])/(InitialDifs[x]))
	Improvements = [100.00*(InitialDifs[k]-DifValues[k])/InitialDifs[k] for k in range(len(DifValues))]
	DifAverage = sum(Improvements)/(1.0*N)
	return DifAverage
	

def FindOptimalTauWithPseudoExp(Params,binning):
	binset=ConvertBinning(binning)
	n = len(binset)-1
	bestdif = -9999999999
	bsettau=9999999999
	n = int(round(n-1))
	histoset=GetNSmearedHistos(Params[1],binning,10)
	for t in range(int(round(n/4))):
		if t<1: 
			continue
		if t>n-1:
			continue
		dif=(TestSVDTau(Params,t,histoset,binning))
		print '      ...Initial test of tau = '+str(t)+' '*(5-len(str(t)))+'   Chi Improvement = '+str(round(dif,2))+'%'

		if dif>bestdif:
			bestdif=dif
			besttau=t
			

	return besttau
	
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

		if dbin<1.0:
			print "\n    Choosing optimal tau = "+str(int(round(svbin)))+'\n'
			return int(round(svbin))
		lastd=dbin
		
def GetIdealBinStructure(inputhisto,idealbins):
	N=inputhisto.GetSize()
	X = []
	Y=[]
	for x in range(N-1):
		if x==0:
			continue
		X.append(inputhisto.GetBinCenter(x))
		Y.append(inputhisto.GetBinContent(x))
	Width = X[1]-X[0]
	Markers = []
	runsum=0
	
	maxbin=inputhisto.Integral()/(1.0*idealbins)
	
	for y in (Y):
		runsum += y
		if runsum>maxbin:
			Markers.append(1)
			runsum=0
		else:
			Markers.append(0)

	CorrectMarkers=[]
	CorrectMarkers=Markers
	CorrectMarkers[0]=1
	
	OutputBins=[]
	for a in range(len(X)):
		if Markers[a]==1:
			OutputBins.append(X[a]-Width/2)
	OutputBins.append(X[-1]+Width/2)
	OutputBins[0]=inputhisto.GetBinCenter(1)-inputhisto.GetBinWidth(1)/2.0
	return OutputBins
	
def GetConstBinStructure(binning):
	Width=(1.0*(binning[2]-binning[1]))/(1.0*binning[0])
	outputbins=[]
	for x in range(binning[0]+1):
		outputbins.append(binning[1]+Width*x)
	return outputbins
		
def MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,selection,optvar):
	print "\n     Performing unfolding analysis for "+recovariable+" in "+str(binning[0]) +" bins from "+str(binning[1])+" to "+str(binning[2])+"  ... \n"
	# Create Canvas
	c1 = TCanvas("c1","",1000,700)
	c1.Divide(2,2)
	gStyle.SetOptStat(0)

	# These are teh style parameters for certain plots - [FillStyle,MarkerStyle,MarkerSize,LineWidth,Color]
	MCGenStyle=[0,20,.00001,1,2]
	MCGenSmearStyle=[0,20,.00001,1,9]

	MCRecoStyle=[0,20,.00001,1,4]
	DataRecoStyle=[0,20,.7,1,1]
	DataCompStyle=[0,20,0.7,1,4]
	BlankRecoStyle=[0,20,.00001,1,0]
	DataUnfoldedStyle=[0,21,0.9,1,2]
	# X and Y axis labels for plot
	Label=[xlabel,"Events/Bin"]

	WStackStyle=[3007,20,.00001,2,6]
	TTStackStyle=[3005,20,.00001,2,4]
	ZStackStyle=[3004,20,.00001,2,2]
	DiBosonStackStyle=[3006,20,.00001,2,3]
	StopStackStyle=[3008,20,.00001,2,9]

	# Get optimal variable binning binning
	#varbinning=GetIdealBinStructure(CreateHisto('h_forrebin_WJets','temptest',t_WJets_MG,recovariable,[10000*binning[0],binning[1],binning[2]],selection+weight,MCGenStyle,Label),binning[0])
	varbinning=GetConstBinStructure(binning)
	if (optvar=="v" or optvar=="V"):
		varbinning=GetIdealBinStructure(CreateHisto('h_forrebin_WJets','temptest',t_WJets_MG,recovariable,[10000*binning[0],binning[1],binning[2]],selection+weight,MCGenStyle,Label),binning[0])

	##############################################################################
	#######     To Right - Background Subtracted Distributions          #######
	##############################################################################
	c1.cd(2)
	if (optvar=="v" or optvar=="V"):
		c1.cd(2).SetLogx()

	selection+='*('+recovariable+'<'+str(binning[2])+')*('+recovariable+'>'+str(binning[1])+')'
	selection_response=str(selection)
	#selection_response+='*('+genvariable+'<'+str(binning[2])+')*('+genvariable+'>'+str(binning[1])+')'
	#selection_response +='*'+ selection_response.replace('muon','genmuon').replace('pfjet','genjet').replace('MET','genMET')
	print selection
	print selection_response
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

	## Rescaling Factor Calculation
	SM = [h_rec_WJets,h_rec_DiBoson,h_rec_ZJets,h_rec_TTBar,h_rec_SingleTop]
	SMInt = sum(k.Integral() for k in SM)
	mcdatascale = (1.0*(h_rec_Data.GetEntries()))/SMInt
	genmcscale = (h_rec_WJets.Integral()/h_gen_WJets.Integral())
	
	for x in SM:
		x.Scale(mcdatascale)

	#h_gen_WJets.Scale(genmcscale*mcdatascale)

	print "MC Global Scale Factor: "+str(mcdatascale)
	print "Gen-Reco Scale Factor: "+str(genmcscale)

	h_rec_WJets.SetMaximum(2.0*h_rec_WJets.GetMaximum())
	h_gen_WJets.SetMaximum(2.0*h_gen_WJets.GetMaximum())

	## Do the Drawing
	h_gen_WJets.Draw("")
	h_rec_WJets.Draw("SAME")

	# Create Legend
	FixDrawLegend(c1.cd(2).BuildLegend())
	
	##############################################################################
	#######      Top Left Plot - Normal Stacked Distributions                #######
	##############################################################################
	c1.cd(1)
	c1.cd(1).SetLogy()
	MCStack = THStack ("MCStack","")
	
	MCStack.SetMinimum(1.0)
	MCStack.SetMaximum(SMInt*100)
	
	## Make the plots without variable bins!
	hs_rec_WJets=CreateHisto('hs_rec_WJets','W+Jets [Reco]',t_WJets_MG,recovariable,binning,selection+weight,WStackStyle,Label)
	hs_rec_Data=CreateHisto('hs_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recovariable,binning,selection,DataRecoStyle,Label)
	hs_rec_DiBoson=CreateHisto('hs_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recovariable,binning,selection+weight,DiBosonStackStyle,Label)
	hs_rec_ZJets=CreateHisto('hs_rec_ZJets','Z+Jets [Alpgen]',t_ZJets_MG,recovariable,binning,selection+weight,ZStackStyle,Label)
	hs_rec_TTBar=CreateHisto('hs_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recovariable,binning,selection+weight,TTStackStyle,Label)
	hs_rec_SingleTop=CreateHisto('hs_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recovariable,binning,selection+weight,StopStackStyle,Label)
	
	SM=[hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar,hs_rec_WJets]
	mcdatascale = (1.0*(hs_rec_Data.GetEntries()))/(sum(k.Integral() for k in SM))
	
	for x in SM:
		#x.Scale(mcdatascale)
		MCStack.Add(x)
	
	MCStack.Draw("")
	MCStack=BeautifyStack(MCStack,Label)
	hs_rec_Data.Draw("EPSAME")

	# Create Legend
	FixDrawLegend(c1.cd(1).BuildLegend())
	gPad.RedrawAxis()


	##############################################################################
	#######      Bottom Left - Gen Versus Reco Response Matrix             #######
	##############################################################################	
	c1.cd(3)
	h_response_WJets=Create2DHisto('h_response_WJets','ResponseMatrix',t_WJets_MG,genvariable,recovariable,varbinning,selection_response+weight+"*"+str(mcdatascale),[xlabel+" Reco",xlabel+" Truth"])
	
	h_response_WJets.Draw("COL")

	
	##############################################################################
	#######      Top Right Addition  - UnFolded Distribution               #######
	##############################################################################	
	c1.cd(2)
	# Subtract other backgrounds from Data using the BackgroundSubtractedHistogram function.
	h_rec_Data2= h_rec_Data.Clone()
	h_rec_Data2 = BackgroundSubtractedHistogram(h_rec_Data2,[ h_rec_DiBoson, h_rec_ZJets,h_rec_TTBar,h_rec_SingleTop])
	h_rec_Data2 = BeautifyHisto(h_rec_Data2,DataCompStyle,Label,"Data, 5/fb [Reco]")

	Params = [ h_rec_WJets, h_gen_WJets, h_response_WJets]

	tau = FindOptimalTauWithPseudoExp(Params,varbinning)
	#tau = FindOptimalTauFromWithDVals(h_rec_Data2,Params)
	#tau=3


	[h_unf_Data,h_dd,h_sv,optimal_tau,optimal_i] = GetSmartSVD(h_rec_Data2,Params,  binning,tau)

	UnfScale=(h_rec_Data2.Integral()/h_unf_Data.Integral())
	h_unf_Data = BeautifyHisto(h_unf_Data,DataUnfoldedStyle,Label,"Data, 5/fb [Unfolded, #tau = "+str(optimal_tau)+",R="+str(round(UnfScale,2))+"]")


	print "Scaling of Unfolded Dist: "+str(UnfScale)

	h_unf_Data.Draw("EPSAME")
	
	h_rec_Data2.Draw("EPSAME")
	FixDrawLegend(c1.cd(2).BuildLegend())



	c1.cd(4)
	c1.cd(4).SetLogy()

	h_dd.SetMaximum(10*(h_dd.GetMaximum()+h_sv.GetMaximum()))
	h_dd.SetMinimum(0.01)
	h_dd=BeautifyHisto(h_dd,[0,20,.00001,1,1],["Index i","Values"],"Diagonal Values")
	h_sv=BeautifyHisto(h_sv,[0,20,.00001,1,2],["Index i","Values"],"Singular Values")
	h_dd.Draw("")
	h_sv.Draw("SAME")
	legend=FixDrawLegend(c1.cd(4).BuildLegend())
	#line =  TLine( 0,1.,binning[0],1. )
	#line.SetLineStyle(2)
	#line.Draw("SAME")

	#line2 =  TLine( optimal_i,h_dd.GetMinimum(),optimal_i,h_dd.GetMaximum() )
	#line2.SetLineStyle(2)	
	#line2.SetLineColor(4)	
	#line2.Draw("SAME")	

	#line3 =  TLine( 0,optimal_tau,binning[0],optimal_tau )
	#line3.SetLineStyle(2)	
	#line3.SetLineColor(2)	
	#line3.Draw("SAME")	
	
	#legend.AddEntry(line,"d[i] Threshold","l")
	#legend.AddEntry(line2,"Max Significant i","l")
	#legend.AddEntry(line3,"#tau from SV[i]","l")


	#line.SetTitle("d_{i} Significace Thresold")
	#line2.SetTitle("Chosen #tau")

	c1.Print('pyplots/'+recovariable+'.pdf')
	c1.Print('pyplots/'+recovariable+'.png')


j1="*(Pt_pfjet1>30)"
j2=j1+"*(Pt_pfjet2>30)"
j3=j2+"*(Pt_pfjet3>30)"
j4=j3+"*(Pt_pfjet4>30)"


#MakeUnfoldedPlots('Pt_genmuon1','Pt_muon1',"p_{T}(#mu) [GeV]",[25,45,145],selection,'')
#MakeUnfoldedPlots('MT_genmuon1genMET','MT_muon1MET',"M_{T}(#mu,E_{T}^{miss}) [GeV]",[25,50,150],selection,'')
#MakeUnfoldedPlots('Pt_genMET','Pt_MET',"E_{T}^{miss} [GeV]",[25,30,530],selection,'')


#MakeUnfoldedPlots('Pt_genjet1','Pt_pfjet1',"p_{T}(jet_{1}) [GeV]",[25,30,530],selection+j1,'')
MakeUnfoldedPlots('Pt_genjet2','Pt_pfjet2',"p_{T}(jet_{2}) [GeV]",[25,10,510],selection+j2,'v')
MakeUnfoldedPlots('Pt_genjet3','Pt_pfjet3',"p_{T}(jet_{3}) [GeV]",[25,30,530],selection+j3,'v')
#MakeUnfoldedPlots('Pt_genjet4','Pt_pfjet4',"p_{T}(jet_{4}) [GeV]",[50,30,230],selection+j4,'')













