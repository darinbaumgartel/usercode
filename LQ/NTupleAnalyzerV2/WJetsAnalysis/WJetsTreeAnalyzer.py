import os

# Directory where root files are kept and the tree you want to get root files from
NormalDirectory = '/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_WPlusJets_StandardMuonDefs_2012_05_25_03_46_08/SummaryFiles/'
TreeName = "PhysicalVariables"


##########################################################################
########      Put all uses of the plotting funcs into main()      ########
##########################################################################

def main():
	os.system("rm pyplots/*.*")

	j1="*(Pt_pfjet1>40.0)"
	j2="*(Pt_pfjet2>40.0)"
	j3="*(Pt_pfjet3>40.0)"
	j4="*(Pt_pfjet4>40.0)"
	j5="*(Pt_pfjet5>40.0)"
	
	
	#MakeUnfoldedPlots('Pt_genmuon1','Pt_muon1',"p_{T}(#mu) [GeV]",[25,45,145],selection,'')
	
	selection = '(Pt_muon1>45)*(Pt_muon2<15)*(abs(Eta_muon1)<2.1)*(MT_muon1MET>50)*(MT_muon1MET<110)'
	weight = '*weight_pu_central*4980*0.92'
	
	FullAnalysisWithUncertainty('Pt_genjet1','Pt_pfjet1',"p_{T}(jet_{1}) [GeV]",[50,0,700],[40,50,60,70,80,90,100,110,125,140,170,200,250,350],selection,weight,'v')
		
	#MakeUnfoldedPlots('GenJet40Count','PFJet40Count',"N_{Jet}",[12,-1.5,10.5],[5,-0.5,4.5],selection,weight,'c',NormalDirectory,-1,'standard')	
	#MakeUnfoldedPlots('MT_genmuon1genMET','MT_muon1MET',"M_{T}(#mu,E_{T}^{miss}) [GeV]",[50,50,150],[20,60,100],selection,weight,'v',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Pt_genMET','Pt_MET',"E_{T}^{miss} [GeV]",[100,0,430],[15,30,330],selection,weight,'v',NormalDirectory,-1,'standard')
	#[tau,data,mc]=MakeUnfoldedPlots('Pt_genjet1','Pt_pfjet1',"p_{T}(jet_{1}) [GeV]",[50,0,700],[40,50,60,70,80,90,100,110,125,140,170,200,250,350],selection,weight,'v',NormalDirectory,2,'standard')
	#print tau
	#print ' '
	#for x in data:
		#print x
	#print ' '
	#for x in mc:
		#print x
	#MakeUnfoldedPlots('Pt_genjet2','Pt_pfjet2',"p_{T}(jet_{2}) [GeV]",[50,0,500],[26,40,300],selection+j1,weight,'v',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Pt_genjet3','Pt_pfjet3',"p_{T}(jet_{3}) [GeV]",[25,0,500],[13,40,300],selection+j2,weight,'v',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Pt_genjet4','Pt_pfjet4',"p_{T}(jet_{4}) [GeV]",[25,0,500],[13,40,300],selection+j3,weight,'v',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Pt_genjet5','Pt_pfjet5',"p_{T}(jet_{5}) [GeV]",[10,0,500],[5,40,300],selection+j4,weight,'v',NormalDirectory,-1,'standard')

	#MakeUnfoldedPlots('Eta_genjet1','Eta_pfjet1',"#eta(jet_{1}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j1,weight,'c',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Eta_genjet2','Eta_pfjet2',"#eta(jet_{2}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j2,weight,'c',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Eta_genjet3','Eta_pfjet3',"#eta(jet_{3}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j3,weight,'c',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Eta_genjet4','Eta_pfjet4',"#eta(jet_{4}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j4,weight,'c',NormalDirectory,-1,'standard')
	#MakeUnfoldedPlots('Eta_genjet5','Eta_pfjet5',"#eta(jet_{5}) ",[30,-3.0,3.0],[12,-2.4,2.4],selection+j5,weight,'c',NormalDirectory,-1,'standard')

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
	
	

	os.system("convert pyplots/*.png pyplots/AllPlots.pdf")



####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################



##########################################################################
########            All functions and Details Below               ########
##########################################################################

import sys
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
	#if "Count" in variable:
		#num=0.0
		#err=0.0
		#thisbin=hout.GetNbinsX()
		#for x in range(hout.GetNbinsX()+1):
			#num+=hout.GetBinContent(thisbin)
			#if hout.GetBinCenter(thisbin) <0:
				#continue
			#err=math.sqrt(hout.GetBinError(thisbin)*hout.GetBinError(thisbin) + err*err)
			#hout.SetBinContent(thisbin,num)
			#hout.SetBinError(thisbin,err)
			#thisbin+=-1
		
	
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
	hout.Sumw2()
	tree.Project(name,variable1+":"+variable2,selection)
	hout.GetXaxis().SetTitle(label[0])
	hout.GetYaxis().SetTitle(label[1])
	hout.GetXaxis().SetTitleFont(132)
	hout.GetYaxis().SetTitleFont(132)
	hout.GetXaxis().SetLabelFont(132)
	hout.GetYaxis().SetLabelFont(132)
	
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

def BackgroundSubtractedHistogram(data,backgrounds):
	for b in backgrounds:
		b.Scale(-1)
		data.Add(b)
		b.Scale(-1)
	return data

def PseudoDataHisto(histo,newname,binning):
	binset=ConvertBinning(binning)
	n = len(binset)-1
	
	hout= TH1D(newname,"",n,array('d',binset))
	bincontent=[]
	binx=[]
	for x in range(n):
		bincontent.append(int(round(histo.GetBinContent(x))))
		binx.append(histo.GetBinCenter(x))
	
	offset = 0.0
	resolution = 0.0
	maxbin=max(binset)
	minbin=min(binset)
	
	for a in range(len(binx)):
		for y in range(bincontent[a]):
			hout.Fill(binx[a])
	return hout

def SmearOffsetHisto(histo,newname,binning,should_offset):
	binset=ConvertBinning(binning)
	n = len(binset)-1
	
	hout= TH1D(newname,"",n,array('d',binset))
	bincontent=[]
	binx=[]
	for x in range(n):
		bincontent.append(int(round(histo.GetBinContent(x))))
		binx.append(histo.GetBinCenter(x))
		#print '**',n, bincontent[x], binx[x]
	
	offset = 0.0
	if should_offset==True:
		offset=abs((numpy.random.normal(1.0,0.05))-1.0)
	resolution = 0.05
	maxbin=max(binset)
	minbin=min(binset)
	
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

	
def GetBasicSVD(data_histo,Params, tau, binning):
	data=data_histo.Clone()
	binset=ConvertBinning(binning)
	n = len(binset)-1
	tsvdunf= TSVDUnfold( data_histo, Params[0], Params[1], Params[2] )
	unfres = tsvdunf.Unfold( tau )	
	return unfres
	
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

def GetNSmearedHistos(inputhisto,binning,N,should_offset):
	histos=[]
	for x in range(N):
		print 'generating smeared histogram '+str(x)
		name='hsmear'+str(x)
		histos.append(SmearOffsetHisto(inputhisto,name,binning,should_offset))
	return histos

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
	

def FindOptimalTauWithPseudoExp(Params,binning,should_offset):
	binset=ConvertBinning(binning)
	n = len(binset)-1
	bestdif = -9999999999
	bsettau=9999999999
	n = int(round(n-1))
	histoset=GetNSmearedHistos(Params[0],binning,10,should_offset)
	olddif=99999999999999999999999999
	for t in range(int(round(n/2))):
		if t<1: 
			continue
		if t>n-1:
			continue
		dif=(TestSVDTau(Params,t,histoset,binning))
		print '      ...Initial test of tau = '+str(t)+' '*(5-len(str(t)))+'   Chi Improvement = '+str(round(dif,2))+'%'
		if olddif<0.0 and dif<2.0*olddif:
			print "        Best tau found at: tau = "+str(int(besttau))+"  ... Terminating tau serach"
			break		
		if dif>bestdif:
			bestdif=dif
			besttau=t
		olddif=dif
	return besttau
	
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
	
	maxbin=inputhisto.Integral()/((1.0*idealbins[0]-2.0))
	
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
	
	modbins=[0,0]
	closesttomod=[9999999999999,999999999999]
	OutputBins=[]
	n=-1
	for a in range(len(X)):
		if Markers[a]==1:
			thisbin=X[a]-(1.0*Width)/2.0
			OutputBins.append(thisbin)
			n+=1
			#if (abs(thisbin-forcebins[0])<closesttomod[0]):
				#closesttomod[0] = abs(thisbin-forcebins[0])
				#modbins[0]=n
			#if (abs(thisbin-forcebins[1])<closesttomod[1]):
				#closesttomod[1] = abs(thisbin-forcebins[1])
				#modbins[1]=n			
	#OutputBins[modbins[0]] = forcebins[0]
	#OutputBins[modbins[1]] = forcebins[1]
		
	OutputBins.append(X[-1]+Width/2)
	OutputBins.append(idealbins[2])
	OutputBins[0]=inputhisto.GetBinCenter(1)-inputhisto.GetBinWidth(1)/2.0
	OutputBins.reverse()
	OutputBins.append(idealbins[1])
	OutputBins.reverse()
	return OutputBins
	
def GetConstBinStructure(binning):
	Width=(1.0*(binning[2]-binning[1]))/(1.0*binning[0])
	outputbins=[]
	for x in range(binning[0]+1):
		outputbins.append(binning[1]+Width*x)
	return outputbins

def GetRescaling(histo1, histo2,binning,variable):
	bincontent1=[]
	bincontent2=[]
	scalefactors=[]
	errors = []
	bindown=[]
	binup=[]

	binset=ConvertBinning(binning)
	n = len(binset)-1
	
	hdiv= histo1.Clone()
	hdiv.Sumw2()
	hdiv.Divide(histo2)
	scalefactors2=[]
	
	#print binset 
	
	for x in range(histo1.GetNbinsX()+1):
		if x==0:
			continue
		bincontent1.append(histo1.GetBinContent(x))
		bincontent2.append(histo2.GetBinContent(x))
		scalefactors.append(1.0)
		if hdiv.GetBinContent(x)>0:
			errors.append(hdiv.GetBinError(x)/hdiv.GetBinContent(x))
		else:
			errors.append(0.0)
		scalefactors2.append(hdiv.GetBinContent(x))

		if (bincontent2[x-1]>0.0):
			scalefactors[x-1]=(1.0*bincontent1[x-1])/(1.0*bincontent2[x-1])
		bindown.append(histo1.GetBinLowEdge(x))
		binup.append(histo1.GetBinLowEdge(x)+histo1.GetBinWidth(x))
	
	scalestring='(0.0'	
	errorstring='(0.0'
	for x in range(len(bincontent1)):
		#print str(bindown[x]) + '<' +variable+'<'+ str(binup[x])+' : weight = '+str(round(scalefactors[x],4))+' +- '+str(round(errors[x],4))
		scalestring+=' + '+str(scalefactors[x])+"*("+variable+">"+str(bindown[x])+')*('+variable+'<'+str(binup[x])+')'
		errorstring+=' + '+str(errors[x])+"*("+variable+">"+str(bindown[x])+')*('+variable+'<'+str(binup[x])+')'
	scalestring+=')'
	errorstring+=')'
			
	return [scalestring,errorstring]


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


	
	##############################################################################
	#######      Top Left Plot - Normal Stacked Distributions                #######
	##############################################################################
	c1.cd(1)

	### Make the plots without variable bins!
	hs_rec_WJets=CreateHisto('hs_rec_WJets','W+Jets [Reco]',t_WJets_MG,recovariable,presentationbinning,selection+weight,WStackStyle,Label)
	hs_rec_Data=CreateHisto('hs_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recovariable,presentationbinning,selection,DataRecoStyle,Label)
	hs_rec_DiBoson=CreateHisto('hs_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recovariable,presentationbinning,selection+weight,DiBosonStackStyle,Label)
	hs_rec_ZJets=CreateHisto('hs_rec_ZJets','Z+Jets [Alpgen]',t_ZJets_MG,recovariable,presentationbinning,selection+weight,ZStackStyle,Label)
	hs_rec_TTBar=CreateHisto('hs_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recovariable,presentationbinning,selection+weight,TTStackStyle,Label)
	hs_rec_SingleTop=CreateHisto('hs_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recovariable,presentationbinning,selection+weight,StopStackStyle,Label)
	hs_rec_QCDMu=CreateHisto('hs_rec_QCDMu','QCD #mu-enriched [Pythia]',t_QCDMu,recovariable,presentationbinning,selection+weight,QCDStackStyle,Label)
	
	SM=[hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar,hs_rec_WJets,hs_rec_QCDMu]
	mcdatascalepres = (1.0*(hs_rec_Data.GetEntries()))/(sum(k.Integral() for k in SM))

	MCStack = THStack ("MCStack","")
	
	SMIntegral = sum(k.Integral() for k in SM)
	
	MCStack.SetMinimum(1.0)
	MCStack.SetMaximum(SMIntegral*100)
	
	
	for x in SM:
		#x.Scale(mcdatascalepres)
		MCStack.Add(x)
	
	MCStack.Draw("HIST")
	c1.cd(1).SetLogy()

	MCStack=BeautifyStack(MCStack,Label)
	hs_rec_Data.Draw("EPSAME")

	# Create Legend
	FixDrawLegend(c1.cd(1).BuildLegend())
	gPad.RedrawAxis()

	c1.Print('pyplots/Basic_'+recovariable+'_'+tagname+'.pdf')
	c1.Print('pyplots/Basic_'+recovariable+'_'+tagname+'.png')

			
def MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight,optvar,FileDirectory,tau_override,tagname):
	
	# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
	for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
		exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
	tmpfile = TFile("tmp.root","RECREATE")
		
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

	presentationbinning=ConvertBinning(presentationbinning)


	##############################################################################
	#######     To Right - Background Subtracted Distributions          #######
	##############################################################################
	c1.cd(2)
	selection+='*('+recovariable+'<'+str(presentationbinning[-1])+')*('+recovariable+'>'+str(presentationbinning[0])+')'
	selection_response=str(selection)+'*('+genvariable+'<'+str(binning[-1])+')*('+genvariable+'>'+str(binning[1])+')'


	# Get optimal variable binning binning
	#varbinning=GetIdealBinStructure(CreateHisto('h_forrebin_WJets','temptest',t_WJets_MG,recovariable,[10000*binning[0],binning[1],binning[2]],selection+weight,MCGenStyle,Label),binning[0])
	varbinning=GetConstBinStructure(binning)
	if (optvar=="v" or optvar=="V"):
		varbinning=GetIdealBinStructure(CreateHisto('h_forrebin_WJets','temptest',t_WJets_MG,recovariable,[100000*len(presentationbinning),presentationbinning[0],presentationbinning[-1]],selection_response+weight,MCGenStyle,Label),binning)
	#print varbinning

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
	h_rec_QCDMu=CreateHisto('h_rec_QCDMu','QCD #mu-enriched [Pythia]',t_QCDMu,recovariable,varbinning,selection_response+weight,QCDStackStyle,Label)

	h_rec_Data_pseudo=PseudoDataHisto(h_rec_WJets,'h_rec_PseudoData',varbinning)

	#print '********************',h_rec_WJets.Integral(),h_rec_PseudoData.Integral()
	#sys.exit()
	

	## Rescaling Factor Calculation
	SM = [h_rec_WJets,h_rec_DiBoson,h_rec_ZJets,h_rec_TTBar,h_rec_SingleTop,h_rec_QCDMu]
	SMInt = sum(k.Integral() for k in SM)
	print SMInt
	print h_rec_Data.GetEntries()
	print h_rec_Data.Integral()
	#sys.exit()
	mcdatascale = (1.0*(h_rec_Data.GetEntries()))/SMInt
	genmcscale = (h_rec_WJets.Integral()/h_gen_WJets.Integral())
	
	#for x in SM:
		#x.Scale(mcdatascale)

	#h_gen_WJets.Scale(genmcscale)

	print "MC Global Scale Factor: "+str(mcdatascale)
	print "Gen-Reco Scale Factor: "+str(genmcscale)

	#h_rec_WJets.SetMaximum(2.0*h_rec_WJets.GetMaximum())
	#h_gen_WJets.SetMaximum(2.0*h_rec_WJets.GetMaximum())

	#if (optvar=="v" or optvar=="V" or optvar=="c"):
		##c1.cd(2).SetLogx()
		#c1.cd(2).SetLogy()


	## Do the Drawing
	h_gen_WJets.Draw("HIST")	
	#h_gen_WJets.SetMaximum(2.0*h_gen_WJets.GetMaximum())
	#h_gen_WJets.SetMinimum(0.6*h_gen_WJets.GetMinimum())
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
	
	SM=[hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar,hs_rec_WJets]
	mcdatascalepres = (1.0*(hs_rec_Data.GetEntries()))/(sum(k.Integral() for k in SM))
	
	for x in SM:
		#x.Scale(mcdatascalepres)
		MCStack.Add(x)
	
	MCStack.Draw("HIST")
	c1.cd(1).SetLogy()

	MCStack=BeautifyStack(MCStack,Label)
	hs_rec_Data.Draw("EPSAME")

	# Create Legend
	FixDrawLegend(c1.cd(1).BuildLegend())
	gPad.RedrawAxis()


	##############################################################################
	#######      Bottom Left - Gen Versus Reco Response Matrix             #######
	##############################################################################	
	c1.cd(3)
	h_response_WJets=Create2DHisto('h_response_WJets','ResponseMatrix',t_WJets_MG,genvariable,recovariable,varbinning,selection_response+weight,[xlabel+" Reco",xlabel+" Truth"])
	h_response_WJets.Draw("COL")
	if (optvar=="v" or optvar=="V"):
		c1.cd(3).SetLogx()	
		c1.cd(3).SetLogy()
	l_bottom=TLine(binning[1], presentationbinning[0] ,binning[2],presentationbinning[0])
	l_top=TLine(binning[1], presentationbinning[0] ,binning[2],presentationbinning[0])
	l_left=TLine(presentationbinning[0], binning[1] ,presentationbinning[0],binning[2])
	l_right=TLine(presentationbinning[-1], binning[1] ,presentationbinning[-1],binning[2])
	bounds = [l_bottom,l_top,l_right,l_left]
	#bounds = [l_bottom,l_top,l_left]
	
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

	Params = [ h_rec_WJets, h_gen_WJets, h_response_WJets]

	should_offset=True
	if "Eta" in recovariable:
		should_offset=False
	
	if tau_override>0:
		tau=tau_override
	else:
		tau = FindOptimalTauWithPseudoExp(Params,varbinning,should_offset)

	[h_unf_Data,h_dd,h_sv,optimal_tau,optimal_i] = GetSmartSVD(h_rec_Data2,Params, varbinning,tau)

	[h_unf_Data_pseudo,h_dd,h_sv_pseudo,optimal_tau_pseudo,optimal_i_pseudo] = GetSmartSVD(h_rec_Data_pseudo,Params, varbinning,tau)

	UnfScale=(h_rec_Data2.Integral()/h_unf_Data.Integral())
	h_unf_Data = BeautifyHisto(h_unf_Data,DataUnfoldedStyle,Label,"Data, 5/fb [Unfolded, #tau = "+str(optimal_tau)+",R="+str(round(UnfScale,2))+"]")
	h_unf_Data_pseudo = BeautifyHisto(h_unf_Data_pseudo,DataUnfoldedStyle_pseudo,Label,"WJets Closure [Unfolded, #tau = "+str(optimal_tau)+",R="+str(round(UnfScale,2))+"]")


	[DataRescalingString,DataErrorString] = GetRescaling(h_unf_Data,h_rec_Data2,varbinning,recovariable)
	[DataRescalingString_pseudo,DataErrorString_pseudo] = GetRescaling(h_unf_Data_pseudo,h_rec_Data_pseudo,varbinning,recovariable)


	print "Scaling of Unfolded Dist: "+str(UnfScale)

	h_unf_Data.Draw("EPSAME")
	h_rec_Data2.Draw("EPSAME")
	h_unf_Data_pseudo.Draw("EPSAME")

	
	FixDrawLegend(c1.cd(2).BuildLegend())

	CompMin = 99999999999999
	CompMax= 0
	for x in range(h_gen_WJets.GetNbinsX()):
		v = h_gen_WJets.GetBinContent(x+1)
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
	#######      Bottom Right - D Value And SV Value Dists                 #######
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


	h_pres_unf_Data_pseudo=CreateHisto('h_pres_unf_Data_pseudo','MC Closure [Unf. Reco/ Gen]',t_WJets_MG,recovariable,presentationbinning,selection_response+weight+"*"+DataRescalingString_pseudo,DataUnfoldedStyle_pseudo,Label)
	h_pres_unf_Data_err_pseudo=CreateHisto('h_pres_unf_Data_err_pseudo','MC Closure [Unf. Reco/ Gen]',t_WJets_MG,recovariable,presentationbinning,selection_response+weight+"*"+DataErrorString_pseudo,DataUnfoldedStyle_pseudo,Label)

	# Other Backgrounds
	h_pres_rec_DiBoson=CreateHisto('h_pres_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recovariable,presentationbinning,selection_response+weight,DiBosonStackStyle,Label)
	h_pres_rec_ZJets=CreateHisto('h_pres_rec_ZJets','Z+Jets [Alpgen]',t_ZJets_MG,recovariable,presentationbinning,selection_response+weight,ZStackStyle,Label)
	h_pres_rec_TTBar=CreateHisto('h_pres_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recovariable,presentationbinning,selection_response+weight,TTStackStyle,Label)
	h_pres_rec_SingleTop=CreateHisto('h_pres_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recovariable,presentationbinning,selection_response+weight,StopStackStyle,Label)	


	h_pres_rec_Data = BackgroundSubtractedHistogram(h_pres_rec_Data,[ h_pres_rec_DiBoson, h_pres_rec_ZJets,h_pres_rec_TTBar,h_pres_rec_SingleTop])
	h_pres_unf_Data = BackgroundSubtractedHistogram(h_pres_unf_Data,[ h_pres_rec_DiBoson, h_pres_rec_ZJets,h_pres_rec_TTBar,h_pres_rec_SingleTop])

	DataBinInfo=[]
	MCBinInfo=[]

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
		
		#print h_pres_unf_Data.GetBinCenter(x),h_pres_unf_Data_err.GetBinContent(x)

	for x in range(h_pres_rec_Data.GetNbinsX()+1):
		if x==0:
			continue
		if h_pres_unf_Data_pseudo.GetBinContent(x) != 0:
			h_pres_unf_Data_pseudo.SetBinError(x,h_pres_unf_Data_err_pseudo.GetBinContent(x)/h_pres_unf_Data_pseudo.GetBinContent(x))
		else: 
			h_pres_unf_Data_pseudo.SetBinError(x,0)
	
	h_pres_unf_Data_pseudo.Divide(h_pres_gen_WJets)

	## Do the Drawing
	h_pres_gen_WJets.Divide(h_pres_rec_WJets)
	h_pres_unf_Data.Divide(h_pres_rec_Data)

	h_pres_unf_Data_pseudo = BeautifyHisto(h_pres_unf_Data_pseudo,DataUnfoldedStyle_pseudo2,Label,"MC Closure [Unf. Reco/ Gen]")


	l_one=TLine(presentationbinning[0], 1 ,presentationbinning[-1],1)
	l_one.SetLineStyle(2)
	
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
	l_one.Draw("SAME")
	h_pres_gen_WJets.SetMaximum(RelMax)
	h_pres_gen_WJets.SetMinimum(RelMin)
	h_pres_unf_Data.Draw("EPSAME")
	h_pres_unf_Data_pseudo.Draw("EPSAME")
	# Create Legend
	FixDrawLegend(c1.cd(4).BuildLegend())

	#h_dd.SetMaximum(10*(h_dd.GetMaximum()+h_sv.GetMaximum()))
	#h_dd.SetMinimum(0.01)
	#h_dd=BeautifyHisto(h_dd,[0,20,.00001,1,1],["Index i","Values"],"Diagonal Values")
	#h_sv=BeautifyHisto(h_sv,[0,20,.00001,1,2],["Index i","Values"],"Singular Values")
	#h_dd.Draw("")
	#h_sv.Draw("SAME")
	#legend=FixDrawLegend(c1.cd(4).BuildLegend())

	c1.Print('pyplots/'+recovariable+'_'+tagname+'.pdf')
	c1.Print('pyplots/'+recovariable+'_'+tagname+'.png')

	return [tau,DataBinInfo,MCBinInfo]


def FullAnalysisWithUncertainty(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight,optvar):

	[tau,data_standard,mc_standard]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight,optvar,NormalDirectory,-1,'standard')
	[null,data_pileup_plus,_pileup_plus]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight.replace('central','sysplus8'),optvar,NormalDirectory,tau,'pileup_plus')
	[null,data_pileup_minus,mc_pileup_minus]=MakeUnfoldedPlots(genvariable,recovariable,xlabel, binning,presentationbinning,selection,weight.replace('central','sysminus8'),optvar,NormalDirectory,tau,'pileup_minus')

	
	data_table=[['|','Bin','|','Prediction','|','DataMean','|','PU_plus','PU_minus','|']]
	for x in range(len(data_standard)):
		thisbin=(data_standard[x])[0]
		center = (data_standard[x])[1]
		prediction = (mc_standard[x])[1]
		pu_up = (data_pileup_plus[x])[1]
		pu_down = (data_pileup_minus[x])[1]
		data_table.append(['|',thisbin,'|',prediction,'|',center,'|',pu_up,pu_down,'|'])
	
	f = open('table_tmp.txt','w')
	for line in data_table:
		line=str(line)
		line=line.replace('[','')
		line=line.replace(']','')
		line=line.replace('\'','')
		line=line.replace('\t',' ')
		for x in range(5):
			line=line.replace('  ','')

		f.write(line+'\n')
	f.close()
	
	os.system('cat table_tmp.txt | column -t -s"," > pyplots/'+recovariable+'.txt')
	os.system('rm table_tmp.txt')
	


main()





