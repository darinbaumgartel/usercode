import os,sys

import math
import random

# Directory where root files are kept and the tree you want to get root files from

NormalDirectory = 'NTupleAnalyzer_JBinfirstRun_2012_12_02_20_35_32/SummaryFiles'

TreeName = "PhysicalVariables"


lumi = 12200.0

NormalWeightMuMu = str(lumi)+'*weight_central'
NormalWeightMuNu = str(lumi)+'*weight_central'

passfilter = '*(GoodVertexCount>0)*(passBeamscraping>0)*(pass_HLTMu40_eta2p1>0)*(passBPTX0>0)*(passBeamHaloFilter>0)*(passTrackingFailure>0)'
passfilter = '*(passDataCert > 0)*(GoodVertexCount>0)*(pass_HLTMu40_eta2p1>0)'
preselectionmumu = '((Pt_muon1>45)*(Pt_muon2>45)*(Pt_jet1>125)*(Pt_jet2>45)*(St_uujj>300)*(M_uu>50)*(DR_muon1muon2>0.3))'
preselectionmunu = '((Pt_muon1>45)*(Pt_muon2<45.0)*(Pt_miss>55)*(Pt_jet1>125)*(Pt_jet2>45)*(Pt_ele1<45.0)*(St_uvjj>300)*(DPhi_muon1met>0.8)*(DPhi_jet1met>0.5)*(MT_uv>50.0))'
preselectionmumu_lightjet = '((Pt_muon1>45)*(Pt_muon2>45)*(Pt_jet1>45)*(Pt_jet2>45)*(St_uujj>300)*(M_uu>50)*(DR_muon1muon2>0.3))'
preselectionmunu_lightjet = '((Pt_muon1>45)*(Pt_muon2<45.0)*(Pt_miss>55)*(Pt_jet1>45)*(Pt_jet2>45)*(Pt_ele1<45.0)*(St_uvjj>300)*(DPhi_muon1met>0.8)*(DPhi_jet1met>0.5)*(MT_uv>50.0))'
preselectionmumu+=passfilter
preselectionmunu+=passfilter
preselectionmumu_lightjet+=passfilter
preselectionmunu_lightjet+=passfilter
datafilter = '*(passBPTX0>0)*(passBeamHaloFilter>0)*(passBeamscraping>0)*(passTrackingFailure>0)'

##########################################################################
########      Put all uses of the plotting funcs into main()      ########
##########################################################################



def main():


	ptbinning = [40,60]
	stbinning = [250,275]
	bosonbinning = [50,60,70,80,90,100,110,120]
	lqbinning = [50,60]

	for x in range(40):
		if ptbinning[-1] < 1500:
			ptbinning.append(ptbinning[-1]+(ptbinning[-1] - ptbinning[-2])*1.2)
		if stbinning[-1] < 2800:
			stbinning.append(stbinning[-1]+(stbinning[-1] - stbinning[-2])*1.2)
		if bosonbinning[-1]<1000:
			bosonbinning.append(bosonbinning[-1]+ (bosonbinning[-1] - bosonbinning[-2])*1.2 )
		if lqbinning[-1]<2000:
			lqbinning.append(lqbinning[-1]+(lqbinning[-1] - lqbinning[-2])*1.1)

	# print bosonbinning
	# ptbinning = [50,0,1000]
	# stbinning = [50,0,2500]
	# bosonbinning = [50,50,550]
	# lqbinning = [50,150,1650]
	vbinning = [60,0,60]

	# UpdateFilesWithMVA(NormalDirectory,['Pt_jet1','Pt_jet2','M_muon1muon2','Pt_muon1','Pt_muon2'])
	# exit()

	# PrintRuns()
	# exit()

	# quickplottest(version_name)
	# sys.exit()

	version_name = 'Testing_highpt'
	os.system('mkdir Results_'+version_name)

	[[Rz_uujj,Rz_uujj_err],[Rtt_uujj,Rtt_uujj_err]] = GetMuMuScaleFactors( NormalWeightMuMu+'*'+preselectionmumu, NormalDirectory, '(M_uu>80)*(M_uu<100)', '(M_uu>100)*(Pt_miss>60)')
	[[Rw_uvjj,Rw_uujj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( NormalWeightMuNu+'*'+preselectionmunu, NormalDirectory, '(MT_uv>60)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>60)*(MT_uv<110)*(JetCount>3.5)')

	MuMuOptCutFile = OptimizeCuts3D(['St_uujj:250:10:1700','M_uujj2:100:10:1700','M_uu:120:10:300'],preselectionmumu,NormalWeightMuMu,version_name,[Rz_uujj,Rtt_uujj,Rw_uvjj],'','uujj')
	MuNuOptCutFile = OptimizeCuts3D(['St_uvjj:250:10:1700','M_uvjj:100:10:1700','MT_uv:120:10:300'],preselectionmunu,NormalWeightMuNu,version_name,[Rz_uujj,Rtt_uvjj,Rw_uvjj],'','uvjj')



	version_name = 'Testing_lowpt'
	os.system('mkdir Results_'+version_name)

	[[Rz_uujj,Rz_uujj_err],[Rtt_uujj,Rtt_uujj_err]] = GetMuMuScaleFactors( NormalWeightMuMu+'*'+preselectionmumu_lightjet, NormalDirectory, '(M_uu>80)*(M_uu<100)', '(M_uu>100)*(Pt_miss>60)')
	[[Rw_uvjj,Rw_uujj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( NormalWeightMuNu+'*'+preselectionmunu_lightjet, NormalDirectory, '(MT_uv>60)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>60)*(MT_uv<110)*(JetCount>3.5)')

	MuMuOptCutFile = OptimizeCuts3D(['St_uujj:250:10:1700','M_uujj2:100:10:1700','M_uu:120:10:300'],preselectionmumu_lightjet,NormalWeightMuMu,version_name,[Rz_uujj,Rtt_uujj,Rw_uvjj],'','uujj')
	MuNuOptCutFile = OptimizeCuts3D(['St_uvjj:250:10:1700','M_uvjj:100:10:1700','MT_uv:120:10:300'],preselectionmunu_lightjet,NormalWeightMuNu,version_name,[Rz_uujj,Rtt_uvjj,Rw_uvjj],'','uvjj')

	# [[Rw_uvjj,Rw_uujj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( NormalWeightMuNu+'*'+preselectionmunu, NormalDirectory, '(MT_uv>60)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>60)*(MT_uv<110)*(JetCount>3.5)')
	# CreateMuMuBDTs(['Pt_jet1','Pt_jet2','M_muon1muon2','Pt_muon1','Pt_muon2'],preselectionmumu,NormalWeightMuMu,NormalDirectory,Rz_uujj, Rw_uvjj,Rtt_uujj)

	# MuMuOptCutFile = 'cuttest.txt'
	# QuickTable(MuMuOptCutFile, preselectionmumu,NormalWeightMuMu,1.0,1.0,1.0)

	# QuickTable(MuMuOptCutFile, preselectionmumu,NormalWeightMuMu,Rz_uujj, Rw_uvjj,Rtt_uujj)

	sys.exit()
	lqmass = 700

	MakeBasicPlot("Pt_jet1","p_{T}(jet_{1}) [GeV]",ptbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'final','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,MuMuOptCutFile,lqmass)
	MakeBasicPlot("Pt_jet2","p_{T}(jet_{2}) [GeV]",ptbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'final','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,MuMuOptCutFile,lqmass)
	MakeBasicPlot("Pt_muon1","p_{T}(#mu_{1}) [GeV]",ptbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'final','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,MuMuOptCutFile,lqmass)
	MakeBasicPlot("Pt_muon2","p_{T}(#mu_{2}) [GeV]",ptbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'final','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,MuMuOptCutFile,lqmass)
	MakeBasicPlot("St_uujj","S_{T}^{#mu #mu j j} [GeV]",stbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'final','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,MuMuOptCutFile,lqmass)
	MakeBasicPlot("M_uu","M^{#mu #mu} [GeV]",bosonbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'final','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,MuMuOptCutFile,lqmass)
	MakeBasicPlot("M_uujj1","M^{#mu j}_{1} [GeV]",lqbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'final','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,MuMuOptCutFile,lqmass)
	MakeBasicPlot("M_uujj2","M^{#mu j}_{2} [GeV]",lqbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'final','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,MuMuOptCutFile,lqmass)
	MakeBasicPlot("GoodVertexCount","N_{Vertices}",vbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'final','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,MuMuOptCutFile,lqmass)

	sys.exit()


	# MakeBasicPlot("Pt_jet1","p_{T}(jet_{1}) [GeV]",ptbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','lljj',Rz_uujj, Rw_uvjj,Rtt_uujj)
	# MakeBasicPlot("Pt_jet2","p_{T}(jet_{2}) [GeV]",ptbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','lljj',Rz_uujj, Rw_uvjj,Rtt_uujj)
	# MakeBasicPlot("Pt_muon1","p_{T}(#mu_{1}) [GeV]",ptbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','lljj',Rz_uujj, Rw_uvjj,Rtt_uujj)
	# MakeBasicPlot("Pt_muon2","p_{T}(#mu_{2}) [GeV]",ptbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','lljj',Rz_uujj, Rw_uvjj,Rtt_uujj)
	# MakeBasicPlot("St_uujj","S_{T}^{#mu #mu j j} [GeV]",stbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','lljj',Rz_uujj, Rw_uvjj,Rtt_uujj)
	# MakeBasicPlot("M_uu","M^{#mu #mu} [GeV]",bosonbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','lljj',Rz_uujj, Rw_uvjj,Rtt_uujj)
	# MakeBasicPlot("M_uujj1","M^{#mu j}_{1} [GeV]",lqbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','lljj',Rz_uujj, Rw_uvjj,Rtt_uujj)
	# MakeBasicPlot("M_uujj2","M^{#mu j}_{2} [GeV]",lqbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','lljj',Rz_uujj, Rw_uvjj,Rtt_uujj)
	# MakeBasicPlot("GoodVertexCount","N_{Vertices}",vbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','lljj',Rz_uujj, Rw_uvjj,Rtt_uujj)



	# MakeBasicPlot("Pt_jet1","p_{T}(jet_{1}) [GeV]",ptbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','lvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj)
	# MakeBasicPlot("Pt_jet2","p_{T}(jet_{2}) [GeV]",ptbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','lvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj)
	# MakeBasicPlot("Pt_muon1","p_{T}(#mu_{1}) [GeV]",ptbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','lvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj)
	# MakeBasicPlot("Pt_miss","E_{T}^{miss} [GeV]",ptbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','lvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj)
	# MakeBasicPlot("St_uvjj","S_{T}^{#mu #nu j j} [GeV]",stbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','lvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj)
	# MakeBasicPlot("MT_uv","M_{T}^{#mu #nu} [GeV]",bosonbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','lvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj)
	# MakeBasicPlot("MT_uvjj","M_{T}^{#mu j} [GeV]",lqbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','lvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj)
	# MakeBasicPlot("M_uvjj","M^{#mu j} [GeV]",lqbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','lvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj)
	# MakeBasicPlot("GoodVertexCount","N_{Vertices}",vbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','lvjj',Rz_uujj, Rw_uvjj,Rtt_uujj)



	os.system('echo Combining Figures; convert -density 800 Results_'+version_name+'/*png Results_'+version_name+'/AllPlots.pdf')

####################################################################################################################################################
####################################################################################################################################################
####################################################################################################################################################

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

# os.system('rm -r Results_'+version_name)


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

for f in os.popen('ls '+NormalDirectory+"| grep \".root\"").readlines():
	exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+NormalDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")

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

def QuickIntegral(tree,selection,scalefac):

	h = TH1D('h','h',1,-1,3)
	h.Sumw2()
	tree.Project('h','1.0',selection+'*'+str(scalefac))
	I = h.GetBinContent(1)
	E = h.GetBinError(1)
	return [I,E]

def QuickMultiIntegral(trees,selection,scalefacs):

	h = TH1D('h','h',1,-1,3)
	h.Sumw2()
 	nn = -1
 	for _ib in trees:
 		nn += 1
 		exec('_bb'+str(n)+' = TH1D(\''+'_bb'+str(n)+'\',\'_bb'+str(n)+'\',1,-1,3)')
 		exec('_bb'+str(n)+'.Sumw2()')
		_ib.Project('_bb'+str(n),'1.0',selection+'*'+str(scalefacs[nn]))
 		exec('h.Add(_bb'+str(n)+')')
	I = h.GetBinContent(1)
	E = h.GetBinError(1)
	return [I,E]

def QuickEntries(tree,selection,scalefac):

	h = TH1D('h','h',1,-1,3)
	h.Sumw2()
	tree.Project('h','1.0',selection)
	I = h.GetEntries()
	return [1.0*I*scalefac, math.sqrt(1.0*I*scalefac)]

def texentry(measurement):
	return '$ '+str(round(measurement[0],2))+' \\pm '+str(round(measurement[1],2))+' $'

def csventry(measurement):
	return str(round(measurement[0],2))+' +- '+str(round(measurement[1],2))

def QuickTableLine(treestruc,selection,scalefacs,ftex,fcsv):
	[_stree,_btrees,_dtree] = treestruc
	_s = QuickIntegral(_stree,selection,scalefacs[0])
	_bs = [QuickIntegral(_btrees[b],selection,scalefacs[1][b]) for b in range(len(_btrees))]
	_bt = QuickMultiIntegral(_btrees,selection,scalefacs[1])
	_d = QuickIntegral (_dtree,selection,scalefacs[2])

	texline = ''
	for x in _bs:
		texline += ' '+texentry(x)+' &'
	texline += texentry(_bt)+' & '
	texline += texentry(_d)+' & '
	texline += texentry(_s)+' \\\\ '
	
	csvline = ''
	for x in _bs:
		csvline += ' '+csventry(x)+' ,'
	csvline += csventry(_bt)+' , '
	csvline += csventry(_d)+' , '
	csvline += csventry(_s)+'  '

	f = open(ftex,'a')
	f.write(texline+'\n')
	f.close()

	f = open(fcsv,'a')
	f.write(csvline+'\n')
	f.close()

def QuickTable(optimlog, selection, weight,rz,rw,rt):
	selection = selection+'*'+weight
	texfile = 'Table_'+optimlog.replace('.txt','tex')
	csvfile = 'Table_'+optimlog.replace('.txt','csv')

	for line in open(optimlog,'r'):
		print 'processing table line for optimization:', line
		fsel = line.replace('\n','')
		masschan = fsel.split('=')[0]
		masschan = masschan.replace('\n','')
		masschan = masschan.replace(' ','')
		mass = masschan.split('jj')[-1]
		chan = 't_'+masschan.split('_')[-1]
		fsel = (fsel.split("="))[-1]
		fsel = '*'+fsel.replace(" ","")
		this_sel = '('+selection+fsel+')'

		exec('treefeed = ['+chan+']')
		treefeed.append([t_TTBarDBin,t_ZJetsJBin,t_WJetsJBin,t_SingleTop,t_DiBoson])
		treefeed.append(t_SingleMuData)
		headers = ['TTBar','Z+Jets','sTop','VV','Tot BG','Data','Signal']
		scalefacs = [1,[rt,rz,rw,1,1],1]
		QuickTableLine(treefeed,selection,scalefacs,texfile,csvfile)

	f = open(ftex,'w')
	header = ' -- & '
	for h in headers:
		header += h + '&'
	header = header[:-1]
	header += '\\\\'
	f.write(header+'\n')
	f.close()

	f = open(fcsv,'w')
	header = ' -- ,'
	for h in headers:
		header += h + ','
	header = header[:-1]	
	f.write(header+'\n')
	f.close()


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
	return [av,dev, str(round(av,3)) +' +- '+str(round(dev,3))]

def RR(List):
	return random.gauss(List[0],List[1])

def PrintRuns():
	tmpfile = TFile("tmp.root","RECREATE")
	t_SingleMuData2 = t_SingleMuData.CopyTree(preselectionmunu)
	allruns = []
	NN = t_SingleMuData2.GetEntries()
	for n in range(NN):
		if n%1000 ==0:
			print n,'of',NN
		t_SingleMuData2.GetEntry(n)
		ev = t_SingleMuData2.run_number
		if ev not in allruns:
			allruns.append(ev)

	allruns.sort()
	for a in allruns:
		print a

def GetMuMuScaleFactors( selection, FileDirectory, controlregion_1, controlregion_2):
	# for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
	# 	exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")

	N1 = QuickEntries(t_SingleMuData,selection + '*' + controlregion_1,1.0)
	N2 = QuickEntries(t_SingleMuData,selection + '*' + controlregion_2,1.0)

	Z1 = QuickIntegral(t_ZJetsJBin,selection + '*' + controlregion_1,1.0)
	T1 = QuickIntegral(t_TTBarDBin,selection + '*' + controlregion_1,1.0)
	s1 = QuickIntegral(t_SingleTop,selection + '*' + controlregion_1,1.0)
	w1 = QuickIntegral(t_WJetsInc,selection + '*' + controlregion_1,1.0)
	v1 = QuickIntegral(t_DiBoson,selection + '*' + controlregion_1,1.0)

	Z2 = QuickIntegral(t_ZJetsJBin,selection + '*' + controlregion_2,1.0)
	T2 = QuickIntegral(t_TTBarDBin,selection + '*' + controlregion_2,1.0)
	s2 = QuickIntegral(t_SingleTop,selection + '*' + controlregion_2,1.0)
	w2 = QuickIntegral(t_WJetsInc,selection + '*' + controlregion_2,1.0)
	v2 = QuickIntegral(t_DiBoson,selection + '*' + controlregion_2,1.0)

	Other1 = [ s1[0]+w1[0]+v1[0], math.sqrt( s1[1]*s1[1] + w1[1]*w1[1] + v1[1]*v1[1] ) ]
	Other2 = [ s2[0]+w2[0]+v2[0], math.sqrt( s2[1]*s2[1] + w2[1]*w2[1] + v2[1]*v2[1] ) ]
	zvals = []
	tvals = []

	for x in range(1000):
		variation = (GetScaleFactors(RR(N1),RR(N2),RR(Z1),RR(Z2),RR(T1),RR(T2),Other1[0],Other2[0]))
		zvals.append(variation[0])
		tvals.append(variation[1])

	zout =  GetStats(zvals)
	tout = GetStats(tvals)

	print 'MuMu: RZ  = ', zout[-1]
	print 'MuMu: Rtt = ', tout[-1]
	return [ [ zout[0], zout[1] ] , [ tout[0],tout[1] ] ]



def GetMuNuScaleFactors( selection, FileDirectory, controlregion_1, controlregion_2):
	# for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
	# 	exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")

	N1 = QuickEntries(t_SingleMuData,selection + '*' + controlregion_1,1.0)
	N2 = QuickEntries(t_SingleMuData,selection + '*' + controlregion_2,1.0)

	W1 = QuickIntegral(t_WJetsJBin,selection + '*' + controlregion_1,1.0)
	T1 = QuickIntegral(t_TTBarDBin,selection + '*' + controlregion_1,1.0)
	s1 = QuickIntegral(t_SingleTop,selection + '*' + controlregion_1,1.0)
	z1 = QuickIntegral(t_ZJetsInc,selection + '*' + controlregion_1,1.0)
	v1 = QuickIntegral(t_DiBoson,selection + '*' + controlregion_1,1.0)

	W2 = QuickIntegral(t_WJetsJBin,selection + '*' + controlregion_2,1.0)
	T2 = QuickIntegral(t_TTBarDBin,selection + '*' + controlregion_2,1.0)
	s2 = QuickIntegral(t_SingleTop,selection + '*' + controlregion_2,1.0)
	z2 = QuickIntegral(t_ZJetsInc,selection + '*' + controlregion_2,1.0)
	v2 = QuickIntegral(t_DiBoson,selection + '*' + controlregion_2,1.0)

	Other1 = [ s1[0]+z1[0]+v1[0], math.sqrt( s1[1]*s1[1] + z1[1]*z1[1] + v1[1]*v1[1] ) ]
	Other2 = [ s2[0]+z2[0]+v2[0], math.sqrt( s2[1]*s2[1] + z2[1]*z2[1] + v2[1]*v2[1] ) ]
	wvals = []
	tvals = []

	for x in range(1000):
		variation = (GetScaleFactors(RR(N1),RR(N2),RR(W1),RR(W2),RR(T1),RR(T2),Other1[0],Other2[0]))
		wvals.append(variation[0])
		tvals.append(variation[1])

	wout =  GetStats(wvals)
	tout = GetStats(tvals)

	print 'MuNu: RW  = ', wout[-1]
	print 'MuNu: Rtt = ', tout[-1]
	return [ [ wout[0], wout[1] ] , [ tout[0],tout[1] ] ]



def MakeBasicPlot(recovariable,xlabel,presentationbinning,selection,weight,FileDirectory,tagname,channel, zscale, wscale, ttscale,cutlog,plotmass):

	# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
	# for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
	# 	exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
	tmpfile = TFile("tmp.root","RECREATE")
	print "  Preparing basic histo for "+channel+":"+recovariable+"...  "
	# Create Canvas
	c1 = TCanvas("c1","",800,800)
	gStyle.SetOptStat(0)

	pad1 = TPad( 'pad1', 'pad1', 0.0, 0.28, 1.0, 1.0 )#divide canvas into pads
	pad2 = TPad( 'pad2', 'pad2', 0.0, 0.03, 1.0, 0.25 )
	pad1.Draw()
	pad2.Draw()
	pad1.cd()
	# These are the style parameters for certain plots - [FillStyle,MarkerStyle,MarkerSize,LineWidth,Color]
	MCRecoStyle=[0,20,.00001,1,4]
	DataRecoStyle=[0,20,.7,1,1]
	# X and Y axis labels for plot
	Label=[xlabel,"Events/Bin"]

	WStackStyle=[3007,20,.00001,2,6]
	TTStackStyle=[3005,20,.00001,2,4]
	ZStackStyle=[3004,20,.00001,2,2]
	DiBosonStackStyle=[3006,20,.00001,2,3]
	StopStackStyle=[3008,20,.00001,2,7]
	QCDStackStyle=[3013,20,.00001,2,15]

	SignalStyle=[0,22,0.7,3,28]
	SignalStyle2=[0,22,0.7,3,38]

	if tagname == 'final':
		fsel = ((os.popen('cat '+cutlog+' | grep '+channel+str(plotmass)).readlines())[0]).replace('\n','')
		fsel = (fsel.split("="))[-1]
		fsel = '*'+fsel.replace(" ","")
		selection = '('+selection+fsel+')'
		print selection
	
	##############################################################################
	#######      Top Left Plot - Normal Stacked Distributions              #######
	##############################################################################
	c1.cd(1)
	print 'Projecting trees...  ',
	### Make the plots without variable bins!
	hs_rec_WJets=CreateHisto('hs_rec_WJets','W+Jets',t_WJetsJBin,recovariable,presentationbinning,selection+'*('+str(wscale)+')*'+weight,WStackStyle,Label)
	hs_rec_Data=CreateHisto('hs_rec_Data','Data',t_SingleMuData,recovariable,presentationbinning,selection,DataRecoStyle,Label)
	hs_rec_DiBoson=CreateHisto('hs_rec_DiBoson','DiBoson',t_DiBoson,recovariable,presentationbinning,selection+'*'+weight,DiBosonStackStyle,Label)
	hs_rec_ZJets=CreateHisto('hs_rec_ZJets','Z+Jets',t_ZJetsJBin,recovariable,presentationbinning,selection+'*('+str(zscale)+')*'+weight,ZStackStyle,Label)
	hs_rec_TTBar=CreateHisto('hs_rec_TTBar','t#bar{t}',t_TTBarDBin,recovariable,presentationbinning,selection+'*('+str(ttscale)+')*'+weight,TTStackStyle,Label)
	hs_rec_SingleTop=CreateHisto('hs_rec_SingleTop','SingleTop',t_SingleTop,recovariable,presentationbinning,selection+'*'+weight,StopStackStyle,Label)

	# hs_rec_QCDMu=CreateHisto('hs_rec_QCDMu','QCD #mu-enriched [Pythia]',t_QCDMu,recovariable,presentationbinning,selection+'*'+weight,QCDStackStyle,Label)

	if channel == 'uujj':
		if tagname != 'final':
			hs_rec_Signal=CreateHisto('hs_rec_Signal','LQ, M = 500 GeV',t_LQuujj500,recovariable,presentationbinning,selection+'*'+weight,SignalStyle,Label)
			hs_rec_Signal2=CreateHisto('hs_rec_Signal2','LQ, M = 900 GeV',t_LQuujj900,recovariable,presentationbinning,selection+'*'+weight,SignalStyle2,Label)
		if tagname == 'final':
			exec ("_stree = t_LQ"+channel+str(plotmass))
			hs_rec_Signal=CreateHisto('hs_rec_Signal','LQ, M = '+str(plotmass)+' GeV',_stree,recovariable,presentationbinning,selection+'*'+weight,SignalStyle,Label)

		hs_rec_DiBoson.SetTitle("Other Backgrounds")
		hs_rec_DiBoson.Add(hs_rec_WJets)
		hs_rec_DiBoson.Add(hs_rec_SingleTop)
		SM=[hs_rec_DiBoson,hs_rec_TTBar,hs_rec_ZJets]

	if channel == 'uvjj':
		if tagname != 'final':	
			hs_rec_Signal=CreateHisto('hs_rec_Signal','LQ, M = 400 GeV',t_LQuvjj400,recovariable,presentationbinning,selection+'*'+weight,SignalStyle,Label)
			hs_rec_Signal2=CreateHisto('hs_rec_Signal2','LQ, M = 750 GeV',t_LQuvjj750,recovariable,presentationbinning,selection+'*'+weight,SignalStyle2,Label)
		if tagname == 'final':
			exec ("_stree = t_LQ"+channel+str(plotmass))
			hs_rec_Signal=CreateHisto('hs_rec_Signal','LQ, M = '+str(plotmass)+' GeV',_stree,recovariable,presentationbinning,selection+'*'+weight,SignalStyle,Label)
	
		hs_rec_DiBoson.SetTitle("Other Backgrounds")
		hs_rec_DiBoson.Add(hs_rec_ZJets)
		hs_rec_DiBoson.Add(hs_rec_SingleTop)		
		SM=[hs_rec_DiBoson,hs_rec_TTBar,hs_rec_WJets]
		

	# mcdatascalepres = (1.0*(hs_rec_Data.GetEntries()))/(sum(k.Integral() for k in SM))

	MCStack = THStack ("MCStack","")
	SMIntegral = sum(k.Integral() for k in SM)
	# MCStack.SetMaximum(SMIntegral*100)
	
	print 'Stacking...  ',	
	for x in SM:
		# x.Scale(mcdatascalepres)
		MCStack.Add(x)
		x.SetMaximum(10*hs_rec_Data.GetMaximum())

	MCStack.Draw("HIST")
	c1.cd(1).SetLogy()

	MCStack=BeautifyStack(MCStack,Label)
	hs_rec_Signal.Draw("HISTSAME")
	if tagname != 'final':
		hs_rec_Signal2.Draw("HISTSAME")

	hs_rec_Data.Draw("EPSAME")

	print 'Legend...  ',
	# Create Legend
	FixDrawLegend(c1.cd(1).BuildLegend())

	sqrts = "#sqrt{s} = 8 TeV";
	l1=TLatex()
	l1.SetTextAlign(12)
	l1.SetTextFont(132)
	l1.SetNDC()
	l1.SetTextSize(0.06)
 
	l1.DrawLatex(0.37,0.94,"CMS 2012  "+sqrts+", 12.2 fb^{-1}")
	# l1.DrawLatex(0.13,0.76,sqrts)

	l2=TLatex()
	l2.SetTextAlign(12)
	l2.SetTextFont(132)
	l2.SetNDC()
	l2.SetTextSize(0.06)
	# l2.SetTextAngle(45);	
	l2.DrawLatex(0.52,0.60,"PRELIMINARY")

	gPad.RedrawAxis()

	MCStack.SetMinimum(.03333)
	MCStack.SetMaximum(100*hs_rec_Data.GetMaximum())

	pad2.cd()
	# pad2.SetLogy()

	RatHistDen =CreateHisto('RatHisDen','RatHistDen',t_SingleMuData,recovariable,presentationbinning,'0',DataRecoStyle,Label)

	RatHistDen.Sumw2()
	RatHistNum =CreateHisto('RatHisNum','RatHistNum',t_SingleMuData,recovariable,presentationbinning,'0',DataRecoStyle,Label)
	RatHistNum.Sumw2()
	for hmc in [hs_rec_TTBar , hs_rec_ZJets , hs_rec_WJets , hs_rec_DiBoson , hs_rec_SingleTop]:
		RatHistDen.Add(hmc)

	RatHistNum.Add(hs_rec_Data)
	RatHistNum.Divide(RatHistDen)

	RatHistNum.SetMaximum(2.5)
	RatHistNum.SetMinimum(0.1)


	RatHistNum.GetYaxis().SetTitleFont(132);
	RatHistNum.GetXaxis().SetTitle('');

	RatHistNum.GetXaxis().SetTitleSize(.13);
	RatHistNum.GetYaxis().SetTitleSize(.13);
	RatHistNum.GetXaxis().CenterTitle();
	RatHistNum.GetYaxis().CenterTitle();		
	RatHistNum.GetXaxis().SetTitleOffset(.28);
	RatHistNum.GetYaxis().SetTitleOffset(.28);
	RatHistNum.GetYaxis().SetLabelSize(.09);
	RatHistNum.GetXaxis().SetLabelSize(.09);


	RatHistNum.Draw()
	unity=TLine(RatHistNum.GetXaxis().GetXmin(), 1.0 , RatHistNum.GetXaxis().GetXmax(),1.0)
	unity.Draw("SAME")	
	print 'Saving...  ',
	c1.Print('Results_'+version_name+'/Basic_'+channel+'_'+recovariable+'_'+tagname+'.pdf')
	c1.Print('Results_'+version_name+'/Basic_'+channel+'_'+recovariable+'_'+tagname+'.png')
	print 'Done.'



def MakeBasicPlotOld(recovariable,xlabel,presentationbinning,selection,weight,FileDirectory,tagname,channel, zscale, wscale, ttscale):

	# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
	# for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
	# 	exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
	tmpfile = TFile("tmp.root","RECREATE")
	print "  Preparing basic histo for "+channel+":"+recovariable+"...  ",
	# Create Canvas
	c1 = TCanvas("c1","",1200,800)
	gStyle.SetOptStat(0)

	# These are the style parameters for certain plots - [FillStyle,MarkerStyle,MarkerSize,LineWidth,Color]
	MCRecoStyle=[0,20,.00001,1,4]
	DataRecoStyle=[0,20,.7,1,1]
	# X and Y axis labels for plot
	Label=[xlabel,"Events/Bin"]

	WStackStyle=[3007,20,.00001,2,6]
	TTStackStyle=[3005,20,.00001,2,4]
	ZStackStyle=[3004,20,.00001,2,2]
	DiBosonStackStyle=[3006,20,.00001,2,30]
	StopStackStyle=[3008,20,.00001,2,40]
	QCDStackStyle=[3013,20,.00001,2,15]

	SignalStyle=[0,22,0.7,3,8]


	
	##############################################################################
	#######      Top Left Plot - Normal Stacked Distributions              #######
	##############################################################################
	c1.cd(1)
	print 'Projecting trees...  ',
	### Make the plots without variable bins!
	hs_rec_WJets=CreateHisto('hs_rec_WJets','W+Jets',t_WJetsInc,recovariable,presentationbinning,selection+'*('+str(wscale)+')*'+weight,WStackStyle,Label)
	hs_rec_Data=CreateHisto('hs_rec_Data','Data, 5/fb',t_SingleMuData,recovariable,presentationbinning,selection,DataRecoStyle,Label)
	hs_rec_DiBoson=CreateHisto('hs_rec_DiBoson','DiBoson',t_DiBoson,recovariable,presentationbinning,selection+'*'+weight,DiBosonStackStyle,Label)
	hs_rec_ZJets=CreateHisto('hs_rec_ZJets','Z+Jets',t_ZJetsInc,recovariable,presentationbinning,selection+'*('+str(zscale)+')*'+weight,ZStackStyle,Label)
	hs_rec_TTBar=CreateHisto('hs_rec_TTBar','t#bar{t}',t_TTBarDBin,recovariable,presentationbinning,selection+'*('+str(ttscale)+')*'+weight,TTStackStyle,Label)
	hs_rec_SingleTop=CreateHisto('hs_rec_SingleTop','SingleTop',t_SingleTop,recovariable,presentationbinning,selection+'*'+weight,StopStackStyle,Label)

	# hs_rec_QCDMu=CreateHisto('hs_rec_QCDMu','QCD #mu-enriched [Pythia]',t_QCDMu,recovariable,presentationbinning,selection+'*'+weight,QCDStackStyle,Label)

	if channel == 'lljj':
		hs_rec_Signal=CreateHisto('hs_rec_Signal','LQ, M = 500 GeV',t_LQuujj500,recovariable,presentationbinning,selection+'*'+weight,SignalStyle,Label)
		hs_rec_DiBoson.SetTitle("Other Backgrounds")
		hs_rec_DiBoson.Add(hs_rec_WJets)
		hs_rec_DiBoson.Add(hs_rec_SingleTop)
		SM=[hs_rec_DiBoson,hs_rec_TTBar,hs_rec_ZJets]

	if channel == 'lvjj':
		hs_rec_Signal=CreateHisto('hs_rec_Signal','LQ, M = 500 GeV',t_LQuvjj500,recovariable,presentationbinning,selection+'*'+weight,SignalStyle,Label)
		hs_rec_DiBoson.SetTitle("Other Backgrounds")
		hs_rec_DiBoson.Add(hs_rec_ZJets)
		hs_rec_DiBoson.Add(hs_rec_SingleTop)		
		SM=[hs_rec_DiBoson,hs_rec_TTBar,hs_rec_WJets]
		

	# mcdatascalepres = (1.0*(hs_rec_Data.GetEntries()))/(sum(k.Integral() for k in SM))

	MCStack = THStack ("MCStack","")
	SMIntegral = sum(k.Integral() for k in SM)
	# MCStack.SetMaximum(SMIntegral*100)
	
	print 'Stacking...  ',	
	for x in SM:
		# x.Scale(mcdatascalepres)
		MCStack.Add(x)
		x.SetMaximum(10*hs_rec_Data.GetMaximum())

	MCStack.Draw("HIST")
	c1.cd(1).SetLogy()

	MCStack=BeautifyStack(MCStack,Label)
	hs_rec_Signal.Draw("HISTSAME")

	hs_rec_Data.Draw("EPSAME")

	print 'Legend...  ',
	# Create Legend
	FixDrawLegend(c1.cd(1).BuildLegend())
	gPad.RedrawAxis()

	MCStack.SetMinimum(.03333)
	MCStack.SetMaximum(100*hs_rec_Data.GetMaximum())

	print 'Saving...  ',
	c1.Print('Results_'+version_name+'/Basic_'+channel+'_'+recovariable+'_'+tagname+'.pdf')
	c1.Print('Results_'+version_name+'/Basic_'+channel+'_'+recovariable+'_'+tagname+'.png')
	print 'Done.'

def round_to(n, precission):
    correction = 0.5 if n >= 0 else -0.5
    return int(n/precission+correction)*precission

def TH2toCutRes(th2,thname, addon):
	res = []

	# print th2.Integral()
	nx = th2.GetNbinsX()+1
	ny = th2.GetNbinsY()+1
	for x in range(nx):
		for y in range(ny):
			if x == 0 : continue
			if y == 0 : continue
			res.append([thname,[addon, th2.GetXaxis().GetBinCenter(x) - 0.5*th2.GetXaxis().GetBinWidth(x), th2.GetYaxis().GetBinCenter(y) - 0.5*th2.GetYaxis().GetBinWidth(y)],th2.Integral(x,nx,y,ny)])

	return res


def GetRatesFromTH2(sigs,baks,_presel,_weight,_hvars,addon,scalefac):
	b1 = ConvertBinning(_hvars[0][1])
	b2 = ConvertBinning(_hvars[1][1])
	v1 = (_hvars[0][0])
	v2 = (_hvars[1][0])
	allinfo = []
	for t in sigs+baks:
		print 'Checking: ',t
		h = 'h_'+t
		# print( h + ' = TH2D("'+h+'","'+h+'",len(b1)-1,array(\'d\',b1),len(b2)-1,array(\'d\',b2))')
		exec( h + ' = TH2D("'+h+'","'+h+'",len(b1)-1,array(\'d\',b1),len(b2)-1,array(\'d\',b2))')
		exec( t+'.Project("'+h+'","'+v2+':'+v1+'","'+_presel+'*('+_weight+'*'+scalefac+')")')
		exec( 'allinfo += TH2toCutRes ('+h+',"'+h+'",'+str(addon)+')')
		# break
	return allinfo


def OptimizeCuts3D(variablespace,presel,weight,tag,scalefacs,cutfile,channel):
	outfile = 'Results_'+tag+'/'+channel+'Cuts.txt'
	ftmpname = channel+'_opttmp.root'
	ftmp = TFile.Open(ftmpname,'RECREATE')
	optvars = []
	binnings = []
	for v in variablespace:
		v = v.split(':')
		var = v[0]
		v0 = float(v[1])
		v1 = float(v[3])
		vb = float(v[2])
		bins = [int(round((v1-v0)/vb)),v0,v1]
		optvars.append([var,bins]) 

	minvar = ['',[9999999,0,0]]
	for v in range(len(optvars)):
		if optvars[v][1][0] < minvar[1][0]:
			minvar = optvars[v]
	hvars = []
	for v in range(len(optvars)):
		if optvars[v] != minvar:
			hvars.append(optvars[v])

	minvarcuts = ['('+minvar[0]+'>'+str(x)+')' for x in ConvertBinning(minvar[1])] 

	signals =  [ 't_'+x.replace('.root\n','') for x in  os.popen('ls '+NormalDirectory+'| grep root | grep LQ'+channel+' ').readlines()]
	backgrounds =  [ 't_'+x.replace('\n','') for x in  ['DiBoson','WJetsJBin','TTBarDBin','ZJetsJBin','SingleTop']]

	[_r_z,_r_tt,_r_w] = scalefacs

	if cutfile=='':
		cutinfo = []
		logfile = 'Results_'+tag+'/Log_'+channel+'Cuts.txt'
		l = open(logfile,'w')
		for h in signals+backgrounds:
			l.write('h_'+h+' = [] \n')
		for x in range(len(minvarcuts)):
			print 'Analyzing for case ',minvarcuts[x]
			scalefac = '1.0'
			if 'ZJets' in h:
				scalefac = str(_r_z)
			if 'WJets' in h:
				scalefac = str(_r_w)
			if 'TTBar' in h:
				scalefac = str(_r_tt)
		 	moreinfo = GetRatesFromTH2(signals,backgrounds,presel+'*'+minvarcuts[x],weight,hvars,(ConvertBinning(minvar[1]))[x],scalefac)
		 	for m in  moreinfo:
				l.write(m[0]+'.append(['+str(m[2])+','+str(m[1])+'])\n')
		l.close()

		os.system('rm '+ftmpname)
		cutfile = logfile
	
	for c in open(cutfile):
		exec(c)

	SIGS = []
	BAKS = []

	for h in signals:
		exec('SIGS.append(h_'+h+')')
	for h in backgrounds:
		exec('BAKS.append(h_'+h+')')

	optimlog = open('Results_'+tag+'/Opt_'+channel+'Cuts.txt','w')

	valuetable = []

	for S in range(len(SIGS)):
		_ssbmax = -99999
		_bestcut = 0
		for icut in range(len(SIGS[S])):
			_s = SIGS[S][icut][0]
			_b = 0.0
			for B in BAKS:
				_b += B[icut][0]
			if _s + _b < 0.0001:
				continue
			_ssb = _s/math.sqrt(_s+_b)
			if _ssb > _ssbmax:
				_ssbmax = _ssb
				_bestcut = icut
		opt = 'opt_'+signals[S].replace('t_','')+ ' = (('+minvar[0] +'>' + str(SIGS[S][_bestcut][1][0])+')*('+hvars[0][0]+'>'+str(SIGS[S][_bestcut][1][1])+')*('+hvars[1][0]+'>'+str(SIGS[S][_bestcut][1][2])+'))\n'  
		print opt
		thismass = float(((signals[S].replace('t_','')).split('jj'))[-1])
		valueline = [thismass, (SIGS[S][_bestcut][1][0]), (SIGS[S][_bestcut][1][1]), (SIGS[S][_bestcut][1][2])]
		valuetable.append(valueline)
		optimlog.write(opt)

	optimlog.close()

	cuts = MakeSmoothCuts(valuetable,[minvar[0],hvars[0][0], hvars[1][0]],tag,channel)
	return cuts



def MakeSmoothCuts(vals,vnames,versionname,chan):

	xnames = []
	for x in vnames:
		a = x
		if "Pt_jet1" in a :  x = "p_{T}(jet_{1})"
		if "Pt_jet2" in a :  x = "p_{T}(jet_{2})"
		if "Pt_muon1" in a :  x = "p_{T}(#mu_{1})"
		if "Pt_muon2" in a :  x = "p_{T}(#mu_{2})"
		if "St_uujj" in a :  x = "S_{T}^{#mu #mu j j}"
		if "M_uu" in a :  x = "M^{#mu #mu}"
		if "M_uujj1" in a :  x = "M^{#mu j}_{1}"
		if "M_uujj2" in a :  x = "M^{#mu j}_{2}"
		if "GoodVertexCount" in a :  x = "N_{Vertices}"
		if "Pt_jet1" in a :  x = "p_{T}(jet_{1})"
		if "Pt_jet2" in a :  x = "p_{T}(jet_{2})"
		if "Pt_muon1" in a :  x = "p_{T}(#mu_{1})"
		if "Pt_miss" in a :  x = "E_{T}^{miss}"
		if "St_uvjj" in a :  x = "S_{T}^{#mu #nu j j}"
		if "MT_uv in" in a :  x = "M_{T}^{#mu #nu}"
		if "MT_uvjj" in a :  x = "M_{T}^{#mu j}"
		if "M_uvjj" in a :  x = "M^{#mu j}"
		xnames.append(x)

	n = len(vals)
	_vals = sorted(vals,key=lambda vals: vals[0])

	yinds = []
	masses = []
	for v in range(len(_vals[0])):
		if v == 0: 
			for v in _vals:
				masses.append(v[0])
			continue
		yinds.append(v)

	print masses
	# print '*'
	optim_res=[masses]
	for y in yinds:

		Y = []
		for v in _vals:
			Y.append(v[y])
		print Y		
		X = array("d", masses)
		Y = array("d", Y)

		c1 = TCanvas("c1","",700,500)
		c1.cd(1).SetGrid()

		hout = TGraph(n,X,Y)
		hout.GetYaxis().SetTitle(xnames[y-1]+' Threshold [GeV]')
		hout.GetXaxis().SetTitle('LQ Mass [GeV]')
		hout.SetTitle('')
		hout.SetMarkerStyle(21)
		hout.SetMarkerSize(1)
		hout.SetLineWidth(2)
		hout.SetLineColor(1)
		hout.GetXaxis().SetTitleFont(132)
		hout.GetYaxis().SetTitleFont(132)
		hout.GetXaxis().SetLabelFont(132)
		hout.GetYaxis().SetLabelFont(132)
		hout.GetYaxis().SetTitleFont(132);
		hout.GetXaxis().SetTitleSize(.06);
		hout.GetYaxis().SetTitleSize(.06);
		hout.GetXaxis().CenterTitle();
		hout.GetYaxis().CenterTitle();
		hout.GetXaxis().SetTitleOffset(0.8);
		hout.GetYaxis().SetTitleOffset(0.8);
		hout.GetYaxis().SetLabelSize(.05);
		hout.GetXaxis().SetLabelSize(.05);
		hout.Draw("AP")
		
		# ft = TF1("ft","[0]*(x*x) + [1]*x + [2]", 0, 2); # second degree pol
		# ft = TF1("ft","[0] + [1]*[1]*tanh(x+[2]) + [3]*[3]*x",250,1250)  # linear+tanh monotonic
		ft = TF1("ft","[1]*x + [0]", 250,1250 )  # linear
		hout.Fit('ft')

		betterfits = []
		# print vnames[y-1]
		for m in masses:
			orig_val = ft.Eval(m)
			new_val = round_to(orig_val,5)
			betterfits.append(new_val)
			# print m, hout.Eval(m), ft.Eval(m), round_to(ft.Eval(m),5)
		optim_res.append(betterfits)
		c1.Print('Results_'+versionname+'/Optimization_'+chan+'_'+vnames[y-1]+'.pdf')
		c1.Print('Results_'+versionname+'/Optimization_'+chan+'_'+vnames[y-1]+'.png')

	optimlog = open('Results_'+versionname+'/Opt_'+chan+'Cuts_Smoothed.txt','w')

	for x in range(len(optim_res[0])):
		cutstr = ''
		for y in range(len(vnames)):
			cutstr += '('+vnames[y]+ '>'+str(optim_res[y+1][x])+ ')*'
		optline =  'opt_LQ'+chan+str(int(optim_res[0][x]))+ ' = ('+cutstr[:-1]+')'
		print optline
		optimlog.write(optline+'\n')
	optimlog.close()
	return 'Results_'+versionname+'/Opt_'+chan+'Cuts_Smoothed.txt'

def QuickBDT(identifier,signal_tree, z_tree, w_tree, vv_tree, st_tree, t_ttree, variables,preselection,channel,weight,zscale,ttscale,wscale):

	fout = TFile('Results_'+version_name+'/Output_'+channel+'_BDT.root',"RECREATE")
	factory = TMVA.Factory("TMVAClassification", fout,":".join([ "!V","!Silent","Color", "DrawProgressBar","Transformations=I;D;P;G,D", "AnalysisType=Classification"]))

	trainweight = ('3.0*'+weight)

	for v in variables:
		factory.AddVariable(v,"F")

	factory.AddSignalTree(signal_tree,1.0)
	factory.AddBackgroundTree(z_tree,zscale)
	factory.AddBackgroundTree(t_ttree,ttscale)
	factory.AddBackgroundTree(w_tree,wscale)
	factory.AddBackgroundTree(vv_tree,1.0)
	factory.AddBackgroundTree(st_tree,1.0)

	# cuts defining the signal and background sample
	sigCut =TCut(preselection+'*(Rand1<0.333333)')
	bgCut = TCut(preselection+'*(Rand1<0.333333)')

	factory.SetBackgroundWeightExpression(trainweight);
	factory.SetSignalWeightExpression(trainweight);

	factory.PrepareTrainingAndTestTree(sigCut,  bgCut,   ":".join([ "nTrain_Signal=0", "nTrain_Background=0", "SplitMode=Random", "NormMode=NumEvents","!V"]))
	method = factory.BookMethod(TMVA.Types.kBDT, "BDT",":".join(["!H", "!V", "NTrees=850", "nEventsMin=150","MaxDepth=3", "BoostType=AdaBoost", "AdaBoostBeta=0.5","SeparationType=GiniIndex","nCuts=20","PruneMethod=NoPruning",]))

	factory.TrainAllMethods()
	factory.TestAllMethods()
	factory.EvaluateAllMethods()

	os.system('mv weights Results_'+version_name+'/weights_'+identifier)

def UpdateFilesWithMVA(FileDirectory,variables):

	alltrees = []
	treenames = []
	for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
		exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")	
		exec('alltrees.append(t_'+f.replace(".root\n","")+')')
		treenames.append('t_'+f.replace(".root\n",""))

	allfiles = os.listdir("Results_"+version_name)
	mvas = []
	for a in allfiles:
		if 'weights' in a:
			mvas.append("Results_"+version_name+'/'+a.replace('\n',''))
	print mvas

	for M in mvas:
		reader=TMVA.Reader()
		for v in variables:
			print('v_'+v+' = array(\'f\',[0])')
			print('reader.AddVariable("'+v+'",v_'+v+')')
			exec('v_'+v+' = array(\'f\',[0])')
			exec('reader.AddVariable("'+v+'",v_'+v+')')
		reader.BookMVA("BDT",M+"/TMVAClassification_BDT.weights.xml")


		for t in range(len(alltrees)):
			tname = treenames[t]
			t = alltrees[t]

			N = t.GetEntries()

			for n in range(N):
				t.GetEntry(n)
				for v in variables:
					exec('v_'+v+'[0] = t.'+v)
				print tname,reader.EvaluateMVA("BDT")

def CreateMuMuBDTs(variables,preselection,weight,FileDirectory,zscale,ttscale,wscale):
	# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
	for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
		exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")	

	QuickBDT('LQToCMu_M_600',t_LQToCMu_M_600,t_ZJets_Sherpa, t_WJets_Sherpa, t_DiBoson, t_SingleTop, t_TTBar,  variables,preselection,'lljj',weight,zscale,ttscale,wscale)

	QuickBDT('LQToCMu_M_500',t_LQToCMu_M_500,t_ZJets_Sherpa, t_WJets_Sherpa, t_DiBoson, t_SingleTop, t_TTBar,  variables,preselection,'lljj',weight,zscale,ttscale,wscale)


main()
