import os
import sys
sys.argv.append( '-b' )
from ROOT import *
gROOT.SetStyle('Plain')
gStyle.SetOptTitle(0)

# Directory where root files are kept and the tree you want to get root files from
FileDirectory = '/afs/cern.ch/user/d/darinb/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Mar13_2012_03_13_22_07_28/SummaryFiles/'
TreeName = "PhysicalVariables"

selection = '((Pt_muon1>40)*(Pt_muon2>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_mumu>250)*(deltaR_muon1muon2>0.3)*(M_muon1muon2>50)*((abs(Eta_muon1)<2.1)&&(abs(Eta_muon2)<2.1)))'
weight = '*weight_pileup4p7fb_higgs*4700'


# This details the histogram structure. It has three lists: Backgrounds, Data, and Signal
# Elements of the background list will for a Stack. Left of the colon is the readable name, right is the root file name, sans '.root'
# You can add sources into a single histogram with an '&' - e.g. 'Other : SingleTop & DiBoson & WJets_Sherpa' gives you a single histo called "Other"
# The second element is the Data. THe third is the signal. Signal will not be stacked. 
HistoStructure = [[['Z+Jets : ZJets_Sherpa','t#bar{t} : TTBar','Other : SingleTop & DiBoson & WJets_Sherpa']],
 [['Data 5/fb: SingleMuData']],
 [['LQ Signal, M= 400 GeV: LQToCMu_M_400'],['LQ Signal, M= 650 GeV: LQToCMu_M_650']]]



# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
	exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")


# This gets the list of relevant trees for plotting
def GenHistoCommands(InputList,name,dimension,selection,variable,properties,xname,yname):
	HComs = []
	TComs=[]
	LegComs = []
	stackcount=-1
	for stackset in InputList:
		stackset.reverse()
		histocount = stackcount
		stackcount+=1
		HComs.append('Stack_'+name+str(stackcount)+' = THStack ("'+name+str(stackcount)+'","'+name+str(stackcount)+'")')
		for histolist in stackset:
			histocount+=1
			histolist=histolist.replace(' ','')
			histos = (histolist.split(':'))[-1]
			histolegname = (histolist.split(':'))[0]
			hname = 'H_'+str(stackcount)+'_'+str(histocount)+'_'+name
			histos = histos.split('&')
			HComs.append(hname+' = TH1D("'+hname+'","'+hname+'",'+dimension+')')
			for histo in histos:
				HComs.append('h_'+histo+' = TH1D("h_'+histo+'","h_'+histo+'",'+dimension+')')
				HComs.append('t_'+histo+'.Project("h_'+histo+'","'+variable+'","'+selection+'")')
				HComs.append(hname+'.Add(h_'+histo+')')
			HComs.append('Stack_'+name+str(stackcount)+'.Add('+hname+')')
			HComs.append(hname+'.SetFillStyle('+str(properties[1][histocount])+')')
			HComs.append(hname+'.SetMarkerStyle('+str(properties[2][histocount])+')')
			HComs.append(hname+'.SetMarkerSize('+str(properties[3])+')')
			HComs.append(hname+'.SetLineWidth('+str(properties[4])+')')
			HComs.append(hname+'.SetMarkerColor('+str(properties[0][histocount])+')')
			HComs.append(hname+'.SetLineColor('+str(properties[0][histocount])+')')
			HComs.append(hname+'.SetFillColor('+str(properties[0][histocount])+')')
			HComs.append(hname+'.SetFillColor('+str(properties[0][histocount])+')')
			LegComs.append(properties[6]+'.AddEntry('+hname+',"'+histolegname+'")')
			HComs.append('Stack_'+name+str(stackcount)+'.Draw("'+properties[5]+'SAME'*('Draw' in str(HComs) and 'SAME' not in properties[5])+'")')
		HComs.append('Stack_'+name+str(stackcount)+'.GetHistogram().GetXaxis().SetTitle("'+xname+'")')
		HComs.append('Stack_'+name+str(stackcount)+'.GetHistogram().GetYaxis().SetTitle("'+yname+'")')
		
		HComs.append('Stack_'+name+str(stackcount)+'.GetHistogram().GetXaxis().SetTitleFont(132)')
		HComs.append('Stack_'+name+str(stackcount)+'.GetHistogram().GetYaxis().SetTitleFont(132)')		
		HComs.append('Stack_'+name+str(stackcount)+'.GetHistogram().GetXaxis().SetLabelFont(132)')
		HComs.append('Stack_'+name+str(stackcount)+'.GetHistogram().GetYaxis().SetLabelFont(132)')		
	LegComs.reverse()
	HComs+= LegComs
	HComs+=TComs
	return HComs

def BasicPlot(histogramstructure,variable,binning,selection,externalweight,xname,yname):
	[backgrounds,data,signals] = histogramstructure
	
	legend = 'leg0'
	commands = ['c1 = TCanvas("c1","",800,680)','gStyle.SetOptLogy()',legend+' = TLegend(0.6,0.63,0.88,0.88,"","brNDC")',legend+'.SetTextFont(132)',legend+'.SetFillColor(0)',legend+'.SetBorderSize(0)']
	
	bg_colororder=[3,4,2,9,6,8,7]
	bg_styleorder=[3008,3005,3004,3007,3006,3009,3010]
	bg_markerstyle=[6,6,6,6,6,6,6]
	bg_markersize=0.00001
	bg_linewidth=2
	bg_drawstyle=''
	

	dat_colororder=[1,11,12,13,14,15,16]
	dat_styleorder=[0,0,0,0,0,0,0,0,0]
	dat_markerstyle=[20,21,22,23,24,25,26,27,28,29]
	dat_markersize=0.7
	dat_linewidth=0
	dat_drawstyle='EPSAME'
	

	sig_colororder=[30,38,46,39,42,45,48]
	sig_styleorder=[0,0,0,0,0,0,0]
	sig_markerstyle=[20,21,22,23,24,25,26,27]
	sig_markersize=0.0001
	sig_linewidth=3
	sig_drawstyle='SAME'


	commands += GenHistoCommands(backgrounds,'background',binning,selection+externalweight,variable,[bg_colororder,bg_styleorder,bg_markerstyle,bg_markersize,bg_linewidth,bg_drawstyle,legend],xname,yname)
	commands += GenHistoCommands(signals,'signals',binning,selection+externalweight,variable,[sig_colororder,sig_styleorder,sig_markerstyle,sig_markersize,sig_linewidth,sig_drawstyle,legend],xname,yname)
	commands += GenHistoCommands(data,'data',binning,selection,variable,[dat_colororder,dat_styleorder,dat_markerstyle,dat_markersize,dat_linewidth,dat_drawstyle,legend],xname,yname)

	commands.append(legend+'.Draw("SAME")')
	commands.append('c1.SetLogy()')
	commands.append('gPad.RedrawAxis()')

	commands.append('c1.Print("pyplots/'+variable+'.png")')
	commands.append('c1.Print("pyplots/'+variable+'.pdf")')

	for c in commands:
		exec(c)


def Gen1DUnfoldCommands(InputList,name,dimension,selection,variable,properties,xname,yname):
	HComs = []
	TComs=[]
	LegComs = []
	Omnicount=-1
	for Omniset in InputList:
		histocount = Omnicount
		Omnicount+=1
		HComs.append('Omni_'+name+str(Omnicount)+' = TH1D("Omni_'+name+str(Omnicount)+'","Omni_'+name+str(Omnicount)+'",'+dimension+')')
		for histolist in Omniset:
			histocount+=1
			histolist=histolist.replace(' ','')
			histos = (histolist.split(':'))[-1]
			histolegname = (histolist.split(':'))[0]
			histos = histos.split('&')
			for histo in histos:
				HComs.append('h_'+histo+' = TH1D("h_'+name+histo+'","h_'+histo+'",'+dimension+')')
				HComs.append('t_'+histo+'.Project("h_'+name+histo+'","'+variable+'","'+selection+'")')
				HComs.append('Omni_'+name+str(Omnicount)+'.Add(h_'+histo+')')

		HComs.append('Omni_'+name+str(Omnicount)+'.Draw("'+properties[5]+'SAME'*('Draw' in str(HComs) and 'SAME' not in properties[5])+'")')

		HComs.append('Omni_'+name+str(Omnicount)+'.SetFillStyle('+str(properties[1])+')')
		HComs.append('Omni_'+name+str(Omnicount)+'.SetMarkerStyle('+str(properties[2])+')')
		HComs.append('Omni_'+name+str(Omnicount)+'.SetMarkerSize('+str(properties[3])+')')
		HComs.append('Omni_'+name+str(Omnicount)+'.SetLineWidth('+str(properties[4])+')')
		HComs.append('Omni_'+name+str(Omnicount)+'.SetMarkerColor('+str(properties[0])+')')
		HComs.append('Omni_'+name+str(Omnicount)+'.SetLineColor('+str(properties[0])+')')
		HComs.append('Omni_'+name+str(Omnicount)+'.SetFillColor('+str(properties[0])+')')
		LegComs.append(properties[6]+'.AddEntry('+'Omni_'+name+str(Omnicount)+',"'+name+'")')

		HComs.append('Omni_'+name+str(Omnicount)+'.SetMaximum(1.5*(Omni_'+name+str(Omnicount)+'.GetMaximum()))')

		HComs.append('Omni_'+name+str(Omnicount)+'.GetXaxis().SetTitle("'+xname+'")')
		HComs.append('Omni_'+name+str(Omnicount)+'.GetYaxis().SetTitle("'+yname+'")')
		HComs.append('Omni_'+name+str(Omnicount)+'.GetXaxis().SetTitleFont(132)')
		HComs.append('Omni_'+name+str(Omnicount)+'.GetYaxis().SetTitleFont(132)')		
		HComs.append('Omni_'+name+str(Omnicount)+'.GetXaxis().SetLabelFont(132)')
		HComs.append('Omni_'+name+str(Omnicount)+'.GetYaxis().SetLabelFont(132)')		
	LegComs.reverse()
	HComs+= LegComs
	HComs+=TComs
	return HComs

def Gen2DUnfoldCommands(InputList,name,dimension,selection,variable1,variable2,properties,xname,yname):
	HComs = []
	TComs=[]
	LegComs = []
	Omnicount=-1
	name += "2D"
	for Omniset in InputList:
		histocount = Omnicount
		Omnicount+=1
		HComs.append('Omni_'+name+str(Omnicount)+' = TH2D("Omni_'+name+str(Omnicount)+'","Omni_'+name+str(Omnicount)+'",'+dimension+','+dimension+')')
		for histolist in Omniset:
			histocount+=1
			histolist=histolist.replace(' ','')
			histos = (histolist.split(':'))[-1]
			histolegname = (histolist.split(':'))[0]
			hname = 'H_'+str(Omnicount)+'_'+str(histocount)+'_'+name
			histos = histos.split('&')
			for histo in histos:
				HComs.append('h_'+histo+' = TH2D("h_'+name+histo+'","h_'+histo+'",'+dimension+','+dimension+')')
				HComs.append('t_'+histo+'.Project("h_'+name+histo+'","'+variable1+':'+variable2+'","'+selection+'")')
				HComs.append('Omni_'+name+str(Omnicount)+'.Add(h_'+histo+')')

		HComs.append('Omni_'+name+str(Omnicount)+'.Draw("'+properties[5]+'SAME'*('Draw' in str(HComs) and 'SAME' not in properties[5])+'")')

		#HComs.append('Omni_'+name+str(Omnicount)+'.Add('+hname+')')
		#HComs.append('Omni_'+name+str(Omnicount)+'.SetFillStyle('+str(properties[1])+')')
		#HComs.append('Omni_'+name+str(Omnicount)+'.SetMarkerStyle('+str(properties[2])+')')
		#HComs.append('Omni_'+name+str(Omnicount)+'.SetMarkerSize('+str(properties[3])+')')
		#HComs.append('Omni_'+name+str(Omnicount)+'.SetLineWidth('+str(properties[4])+')')
		#HComs.append('Omni_'+name+str(Omnicount)+'.SetMarkerColor('+str(properties[0])+')')
		#HComs.append('Omni_'+name+str(Omnicount)+'.SetLineColor('+str(properties[0])+')')
		#HComs.append('Omni_'+name+str(Omnicount)+'.SetFillColor('+str(properties[0])+')')
		#LegComs.append(properties[6]+'.AddEntry('+'Omni_'+name+str(Omnicount)+',"'+name+'")')

		HComs.append('Omni_'+name+str(Omnicount)+'.SetMaximum(1.5*(Omni_'+name+str(Omnicount)+'.GetMaximum()))')

		HComs.append('Omni_'+name+str(Omnicount)+'.GetXaxis().SetTitle("'+xname+'")')
		HComs.append('Omni_'+name+str(Omnicount)+'.GetYaxis().SetTitle("'+yname+'")')
		HComs.append('Omni_'+name+str(Omnicount)+'.GetXaxis().SetTitleFont(132)')
		HComs.append('Omni_'+name+str(Omnicount)+'.GetYaxis().SetTitleFont(132)')		
		HComs.append('Omni_'+name+str(Omnicount)+'.GetXaxis().SetLabelFont(132)')
		HComs.append('Omni_'+name+str(Omnicount)+'.GetYaxis().SetLabelFont(132)')		
	#LegComs.reverse()
	HComs+= LegComs
	HComs+=TComs
	return HComs


#ncol = 100
#colors=[]
#dg=1.0/(1.0*ncol)
#grey=0.0
#for i in range(ncol):
	#colors.append(i+100)
	#col = gROOT.GetColor(colors[i])
	#col.SetRGB(grey, grey, grey)
	#grey = grey+dg


from array import array
	
#mTh = array("d",[ 150, 200, 250, 300, 350, 400,450,500,550,600,650,700,750,800,850])

NCont = 50
NRGBs = 5
stops = array("d",[ 0.00, 0.34, 0.61, 0.84, 1.00])
red= array("d",[ 0.00, 0.00, 0.87, 1.00, 0.51 ])
green= array("d",[ 0.00, 0.81, 1.00, 0.20, 0.00 ])
blue= array("d",[ 0.51, 1.00, 0.12, 0.00, 0.00 ])

TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)
gStyle.SetNumberContours(NCont)

def UnfoldedPlots(histogramstructure,GenVar,RecoVar,binning,selection,externalweight,xname,yname):

	[backgrounds,data,signals] = histogramstructure
	
	legend = 'leg0'
	commands = ['c1 = TCanvas("c1","",1200,1000)','c1.Divide(2,2)',legend+' = TLegend(0.6,0.63,0.88,0.88,"","brNDC")',legend+'.SetTextFont(132)',legend+'.SetFillColor(0)',legend+'.SetBorderSize(0)']
	

	commands += ['c1.cd(1)','gStyle.SetOptStat(0)']
	commands += Gen1DUnfoldCommands(backgrounds,'Background_Reco',binning,selection+externalweight,RecoVar,[2,0,0,0.00001,2,'',legend],xname,yname)
	#commands.append(legend+'.Draw("SAME")')
	commands += Gen1DUnfoldCommands(backgrounds,'Background_Gen',binning,selection+externalweight,GenVar,[4,0,0,0.00001,2,'SAME',legend],xname,yname)
	commands.append(legend+'.Draw("SAME")')

	legend = 'leg1'
	commands += ['c1.cd(2)','gStyle.SetOptStat(0)',legend+' = TLegend(0.6,0.63,0.88,0.88,"","brNDC")',legend+'.SetTextFont(132)',legend+'.SetFillColor(0)',legend+'.SetBorderSize(0)']
	commands += Gen2DUnfoldCommands(backgrounds,'Background_Gen',binning,selection+externalweight,RecoVar,GenVar,[4,0,0,0.00001,2,'colz',legend],xname+" Truth",xname+" Reco")



	legend = 'leg2'
	commands += ['c1.cd(3)',legend+' = TLegend(0.6,0.63,0.88,0.88,"","brNDC")',legend+'.SetTextFont(132)',legend+'.SetFillColor(0)',legend+'.SetBorderSize(0)']
	
	bg_colororder=[3,4,2,9,6,8,7]
	bg_styleorder=[3008,3005,3004,3007,3006,3009,3010]
	bg_markerstyle=[6,6,6,6,6,6,6]
	bg_markersize=0.00001
	bg_linewidth=2
	bg_drawstyle='SAME'
	

	dat_colororder=[1,11,12,13,14,15,16]
	dat_styleorder=[0,0,0,0,0,0,0,0,0]
	dat_markerstyle=[20,21,22,23,24,25,26,27,28,29]
	dat_markersize=0.7
	dat_linewidth=0
	dat_drawstyle='EP'
	

	commands += GenHistoCommands(data,'data',binning,selection,RecoVar,[dat_colororder,dat_styleorder,dat_markerstyle,dat_markersize,dat_linewidth,dat_drawstyle,legend],xname,yname)
	commands += GenHistoCommands(backgrounds,'background',binning,selection+externalweight,RecoVar,[bg_colororder,bg_styleorder,bg_markerstyle,bg_markersize,bg_linewidth,bg_drawstyle,legend],xname,yname)
	commands.append(legend+'.Draw("SAME")')
	commands.append('gPad.RedrawAxis()')

	commands.append('tsvdunf = TSVDUnfold( h_SingleMuData, Omni_Background_Gen0, Omni_Background_Reco0, Omni_Background_Gen2D0 )')
	#commands.append('tsvdunf = TSVDUnfold( h_SingleMuData, Omni_Background_Gen0, Omni_Background_Reco0, Omni_Background_Gen2D0 )')
	commands.append('unfresult = tsvdunf.Unfold( 5 )')
	legend='leg3'
	commands+=['c1.cd(4)',legend+' = TLegend(0.6,0.63,0.88,0.88,"","brNDC")',legend+'.SetTextFont(132)',legend+'.SetFillColor(0)',legend+'.SetBorderSize(0)']
	commands+=['h_SingleMuData.SetMarkerStyle(20)','h_SingleMuData.SetMarkerSize(.7)','unfresult.SetMarkerColor(2)','unfresult.SetLineColor(2)','unfresult.Draw("")','h_SingleMuData.Draw("EPSAME")',legend+'.AddEntry(h_SingleMuData,"Data")',legend+'.AddEntry(unfresult,"Data, Unfolded")']
	commands.append('unfresult.GetXaxis().SetTitle("'+xname+'")')
	commands.append('unfresult.GetYaxis().SetTitle("'+yname+'")')
	commands.append('unfresult.GetXaxis().SetTitleFont(132)')
	commands.append('unfresult.GetYaxis().SetTitleFont(132)')		
	commands.append('unfresult.GetXaxis().SetLabelFont(132)')
	commands.append('unfresult.GetYaxis().SetLabelFont(132)')		
	commands.append(legend+'.Draw("SAME")')

	#commands += GenHistoCommands(data,'data',binning,selection,RecoVar,[dat_colororder,dat_styleorder,dat_markerstyle,dat_markersize,dat_linewidth,dat_drawstyle,legend],xname,yname)

	#commands.append('c1.SetLogy()')
	#commands.append('gPad.RedrawAxis()')

	commands.append('c1.Print("pyplots/Unfolded_'+GenVar+'.png")')
	commands.append('c1.Print("pyplots/Unfolded_'+GenVar+'.pdf")')


	for c in commands:
		print c
		exec(c)

	
UnfoldedPlots(HistoStructure,'Pt_genjet1','Pt_pfjet1','100,50,550',selection,weight,"p_{T}(j_{1}) [GeV]","Entries/Bin")





#BasicPlot(HistoStructure,'M_muon1muon2','50,50,550',selection,weight,"M_{#mu#mu}","Entries/Bin")



##### ======================================================================================================



#print t_DiBoson.M_muon1muon2
#exit()

# This gets the list of relevant trees for plotting
#def GetRelevantTrees(InputList):
	#savetrees = []
	#for x in InputList:
		#for z in x:
			#for y in z:
				#y=y.replace(' ','')
				#y = (y.split(':'))[-1]
				#y = y.split('&')
				#for t in y:
					#savetrees.append('t_'+t)
	#return savetrees
	
#from math import log10, floor
#def round_to_1(x):
	#return round(x, -int(floor(log10(x))))
	

#def GetPlotDimensions(treeset,variable,forcedborders):
	#xmin = 999999999999
	#xmax = -999999999999
	#for t in treeset:
		#thismin = eval(t+'.GetMinimum(variable)')
		#thismax = eval(t+'.GetMaximum(variable)')
		#if thismin<xmin:
			#xmin=thismin
		#if thismax>xmax:
			#xmax=thismax
			
	#print xmin
	#print xmax
	#if len(forcedborders)==2:
		#xmin = forcedborders[0]*(forcedborders[0]>xmin)+xmin*(forcedborders[0]<xmin)
		#xmax = forcedborders[1]*(forcedborders[1]<xmax)+xmax*(forcedborders[1]>xmax)
	#xmin=round_to_1(xmin)
	#xmax=round_to_1(xmax)
	#print xmin
	#print xmax


#print t_DiBoson.GetEntries()