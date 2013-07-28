import os

# Directory where root files are kept and the tree you want to get root files from. Normal is for standard analysis, the jet rescaling, jet smearing, muon PT rescaling ,and muon PT smearing. 

NormalDirectory = "NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_July10_2013_07_10_20_36_08/SummaryFiles"
JetScaleDownDirectory = "NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_July10_JetScaleDown_2013_07_10_22_47_04/SummaryFiles"
JetScaleUpDirectory = "NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_July10_JetScaleUp_2013_07_10_21_35_51/SummaryFiles"
JetSmearDirectory = "NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_July10_JetSmear_2013_07_11_18_13_08/SummaryFiles"
MuScaleDownDirectory = "NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_July10_MuScaleDown_2013_07_11_16_42_31/SummaryFiles"
MuScaleUpDirectory = "NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_July10_MuScaleUp_2013_07_10_23_46_26/SummaryFiles"
MuSmearDirectory = "NTupleAnalyzer_V00_02_06_WPlusJets_WJetsAnalysis_5fb_July10_MuSmear_2013_07_11_19_27_58/SummaryFiles"


# This is the Rivet NTuple for MadGraph
RIVETMadGraph='/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVET/Madgraph_treeV3Dressed_NEvents_93671821.root'
RIVETMadGraphNonHad = '/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVETNonHadronized/Madgraph_ModB_treeV3Dressed_NEvents_92216218.root'
RIVETSherpa='/afs/cern.ch/work/d/darinb/LQAnalyzerOutput/RIVET/Sherpa_treeV3Dressed_NEvents_685972.root'


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

# RivetBranchMap.append(['HT_pfjets','(ptjet1*(ptjet1>0))+(ptjet2*(ptjet2>0))+(ptjet3*(ptjet3>0))+(ptjet4*(ptjet4>0))'])
RivetBranchMap.append(['HT_pfjets','htjets'])


# RivetBranchMap.append(['pfjet','jet'])
# RivetBranchMap.append(['muon1','muon'])
RivetBranchMap.append(['PFJet30Count_preexc','njet_WMuNu'])
RivetBranchMap.append(['PFJet30Count','njet_WMuNu'])
RivetBranchMap.append(['MT_muon1METR','mt_mumet'])
RivetBranchMap.append(['Pt_MET','ptmet'])

# This maps the LQAnalyzer branch names to the Rivet branch names due to my total lack of foresight.
GenBranchMap=[  ]
GenBranchMap.append(['Eta_pfjet','Eta_genjet'])
GenBranchMap.append(['Pt_pfjet','Pt_genjet'])
GenBranchMap.append(['PFJet40Count','GenJet40Count'])
GenBranchMap.append(['MT_muon1METR','MT_genmuon1genMET'])
GenBranchMap.append(['Pt_MET','Pt_genMET'])

RivetGenBranchMap = []
RivetGenBranchMap.append(['HT_genjets','htjets'])
RivetGenBranchMap.append(['MT_genmuon1genMET','mt_mumet'])
RivetGenBranchMap.append(['GenJet30Count_preexc','njet_WMuNu'])
RivetGenBranchMap.append(['GenJet30Count','njet_WMuNu'])
RivetGenBranchMap.append(['Pt_genMET','ptmet'])
RivetGenBranchMap.append(['Eta_','eta'])
RivetGenBranchMap.append(['Pt_','pt'])
RivetGenBranchMap.append(['DeltaPhi_','dphi'])
RivetGenBranchMap.append(['Phi_','phi'])
RivetGenBranchMap.append(['genjet','jet'])
RivetGenBranchMap.append(['genmuon','muon'])
RivetGenBranchMap.append(['muon1','muon'])
RivetGenBranchMap.append(['weight_pu_central*4955','evweight'])



RivetGenBareBranchMap = []
RivetGenBareBranchMap.append(['HT_genjets','htjets'])
RivetGenBareBranchMap.append(['MT_genmuon1genMET_bare','mt_mumet'])
RivetGenBareBranchMap.append(['Pt_genjet1_bare','ptjet1'])
RivetGenBareBranchMap.append(['Pt_genjet2_bare','ptjet2'])
RivetGenBareBranchMap.append(['Pt_genjet3_bare','ptjet3'])
RivetGenBareBranchMap.append(['Pt_genjet4_bare','ptjet4'])
RivetGenBareBranchMap.append(['Eta_genjet1_bare','etajet1'])
RivetGenBareBranchMap.append(['Eta_genjet2_bare','etajet2'])
RivetGenBareBranchMap.append(['Eta_genjet3_bare','etajet3'])
RivetGenBareBranchMap.append(['Eta_genjet4_bare','etajet4'])
RivetGenBareBranchMap.append(['DeltaPhi_genjet1genmuon1_bare','dphijet1muon1'])
RivetGenBareBranchMap.append(['DeltaPhi_genjet2genmuon1_bare','dphijet2muon1'])
RivetGenBareBranchMap.append(['DeltaPhi_genjet3genmuon1_bare','dphijet3muon1'])
RivetGenBareBranchMap.append(['DeltaPhi_genjet4genmuon1_bare','dphijet4muon1'])
RivetGenBareBranchMap.append(['Pt_genMET','ptmet'])
RivetGenBareBranchMap.append(['weight_pu_central*4955','evweight'])
RivetGenBareBranchMap.append(['Pt_genmuon1_bare','ptmuon'])
RivetGenBareBranchMap.append(['Eta_genmuon1_bare','etamuon'])



# Handy shortcuts for the tree name and common cuts used in selections
TreeName = "PhysicalVariables"

IsoMuCond = '*(IsoMu24Pass>0.5)'


#################################################################################
#############      DEFINE SELECTIONS FOR PLOTS and RESPONSE        ##############
#################################################################################

# Basic event filters
filters = '*(pass_HBHENoiseFilter*pass_passBeamHaloFilterTight)*(N_GoodVertices>0.5)'
# filters = '*(pass_HBHENoiseFilter)*(N_GoodVertices>0.5)'
# filters = '*(pass_passBeamHaloFilterTight)*(N_GoodVertices>0.5)'

# filters = '*(N_GoodVertices>0.5)'


# Placeholder to require additional jet
j1="*(Pt_pfjet1>30.0)*(abs(Eta_pfjet1)<2.4)"
j2="*(Pt_pfjet2>30.0)*(abs(Eta_pfjet2)<2.4)"
j3="*(Pt_pfjet3>30.0)*(abs(Eta_pfjet3)<2.4)"
j4="*(Pt_pfjet4>30.0)*(abs(Eta_pfjet4)<2.4)"
j5="*(Pt_pfjet5>30.0)*(abs(Eta_pfjet5)<2.4)"
j6="*(Pt_pfjet6>30.0)*(abs(Eta_pfjet6)<2.4)"

# Placeholder to require additional barejet
gj1="*(Pt_genjet1_bare>30.0)*(abs(Eta_genjet1_bare)<2.4)"
gj2="*(Pt_genjet2_bare>30.0)*(abs(Eta_genjet2_bare)<2.4)"
gj3="*(Pt_genjet3_bare>30.0)*(abs(Eta_genjet3_bare)<2.4)"
gj4="*(Pt_genjet4_bare>30.0)*(abs(Eta_genjet4_bare)<2.4)"
gj5="*(Pt_genjet5_bare>30.0)*(abs(Eta_genjet5_bare)<2.4)"
gj6="*(Pt_genjet6_bare>30.0)*(abs(Eta_genjet6_bare)<2.4)"

# QCD: Same as basic, but no isolation or MT cut. 
_qcd_selection = '(PFJet30TCHEMCountCentral<0.5)*(Pt_muon2<0.000001)*(Pt_muon1>25)*(abs(Eta_muon1)<2.1)'
# _qcd_selection+= '*(pass_HBHENoiseFilter*pass_passBeamHaloFilterTight)*(N_GoodVertices>0.5)'
_qcd_selection += filters
_qcd_selection += j1


# Basic selection for reco-level plots
basic_selection = '(Pt_muon1>25)*(RelIso_muon1<0.15)*(Pt_muon2<0.000001)*(abs(Eta_muon1)<2.1)*(IsoMu24Pass>0)'
basic_selection += '*(MT_muon1METR>50)*(PFJet30TCHEMCountCentral<0.5)'
basic_selection += filters
basic_selection += j1


# _ttbar_selection = '(Pt_muon1>25)*(RelIso_muon1<0.15)*(Pt_muon2<0.000001)*(abs(Eta_muon1)<2.1)*(IsoMu24Pass>0)'
# _ttbar_selection += '*(MT_muon1METR>50)*(PFJet30TCHEMCountCentral>1.5)'
# _ttbar_selection += filters
# _ttbar_selection += j1

# _z_selection = '(Pt_muon1>25)*(RelIso_muon1<0.15)*(Pt_muon2>25.0)*(abs(Eta_muon1)<2.1)*(IsoMu24Pass>0)'
# _z_selection += '*(PFJet30TCHEMCountCentral<0.5)'
# _z_selection += filters
# _z_selection += j1



# Minimal reco level selection (not currently needed!)
min_selection = '(Pt_muon1>0.1)*(Pt_pfjet1>0.1)'

# Gen selection for xini (bare) distribution. 
baregen_selection = '(MT_genmuon1genMET_bare>50)*(Eta_genmuon1_bare>-2.1)*(Eta_genmuon1_bare<2.1)*(Pt_genmuon1_bare>25)'
baregen_selection += gj1



_ttbar_selection = basic_selection.replace('(PFJet30TCHEMCountCentral<0.5)','(PFJet30TCHEMCountCentral>1.5)')
_z_selection = basic_selection.replace('(Pt_muon2<0.000001)','(Pt_muon2>25)')


###################
## DISTRIBUTIONS ##
###################

# Selections are as follows:
# Sels_*_reco = [ Full reco-level selection applies to data and MC, 
#                 Minimal reco-level selection (not yet used)]
# Sels_*_gen  = [ Full gen selection used in final distributions, 
#                 Minimal gen requirements for forming response matrix]


# Jet count - Normal Sel plus one reco jet. Gen level needs nothing extra!
Sels_PFJet30Count_reco = [basic_selection,min_selection]
Sels_PFJet30Count_gen = [baregen_selection, '(1)']

# MET - Same as jet count!
Sels_Pt_MET_reco = [basic_selection+j1,min_selection]
Sels_Pt_MET_gen = [baregen_selection, '(1)']


Sels_ZCont1_Pt_MET_reco = [_z_selection+j1,min_selection]
Sels_ZCont1_Pt_MET_gen = [baregen_selection, '(1)']

Sels_ZCont2_Pt_MET_reco = [_z_selection+j2,min_selection]
Sels_ZCont2_Pt_MET_gen = [baregen_selection, '(1)']

Sels_ZCont3_Pt_MET_reco = [_z_selection+j3,min_selection]
Sels_ZCont3_Pt_MET_gen = [baregen_selection, '(1)']

Sels_ZCont4_Pt_MET_reco = [_z_selection+j4,min_selection]
Sels_ZCont4_Pt_MET_gen = [baregen_selection, '(1)']

Sels_TCont1_Pt_MET_reco = [_ttbar_selection+j1,min_selection]
Sels_TCont1_Pt_MET_gen = [baregen_selection, '(1)']

Sels_TCont2_Pt_MET_reco = [_ttbar_selection+j2,min_selection]
Sels_TCont2_Pt_MET_gen = [baregen_selection, '(1)']

Sels_TCont3_Pt_MET_reco = [_ttbar_selection+j3,min_selection]
Sels_TCont3_Pt_MET_gen = [baregen_selection, '(1)']

Sels_TCont4_Pt_MET_reco = [_ttbar_selection+j4,min_selection]
Sels_TCont4_Pt_MET_gen = [baregen_selection, '(1)']


# Muon-related variables with no jet - gen level needs just that muon exists.
Sels_Pt_muon1_reco = [basic_selection,min_selection]
Sels_Pt_muon1_gen = [baregen_selection, '(Pt_genmuon1>0.1)']

Sels_Eta_muon1_reco = [basic_selection,min_selection]
Sels_Eta_muon1_gen = [baregen_selection, '(Pt_genmuon1>0.1)']

Sels_MT_genmuon1genMET_reco = [basic_selection,min_selection]
Sels_MT_genmuon1genMET_gen = [baregen_selection, '(Pt_genmuon1>0.1)']

# Variables with 1 jet
Sels_Pt_pfjet1_reco = [basic_selection,min_selection]
Sels_Pt_pfjet1_gen = [baregen_selection, '(Pt_genjet1>0.1)']

Sels_Eta_pfjet1_reco = [basic_selection,min_selection]
Sels_Eta_pfjet1_gen = [baregen_selection, '(Pt_genjet1>0.1)']

Sels_DeltaPhi_pfjet1muon1_reco = [basic_selection,min_selection]
Sels_DeltaPhi_pfjet1muon1_gen = [baregen_selection, '(Pt_genjet1>0.1)*(Pt_genmuon1>0.1)']


# Variables with 2 jet
Sels_Pt_pfjet2_reco = [basic_selection+j2,min_selection]
Sels_Pt_pfjet2_gen = [baregen_selection+gj2, '(Pt_genjet2>0.1)']

Sels_Eta_pfjet2_reco = [basic_selection+j2,min_selection]
Sels_Eta_pfjet2_gen = [baregen_selection+gj2, '(Pt_genjet2>0.1)']

Sels_DeltaPhi_pfjet2muon1_reco = [basic_selection+j2,min_selection]
Sels_DeltaPhi_pfjet2muon1_gen = [baregen_selection+gj2, '(Pt_genjet2>0.1)*(Pt_genmuon1>0.1)']


# Variables with 3 jet
Sels_Pt_pfjet3_reco = [basic_selection+j3,min_selection]
Sels_Pt_pfjet3_gen = [baregen_selection+gj3, '(Pt_genjet3>0.1)']

Sels_Eta_pfjet3_reco = [basic_selection+j3,min_selection]
Sels_Eta_pfjet3_gen = [baregen_selection+gj3, '(Pt_genjet3>0.1)']

Sels_DeltaPhi_pfjet3muon1_reco = [basic_selection+j3,min_selection]
Sels_DeltaPhi_pfjet3muon1_gen = [baregen_selection+gj3, '(Pt_genjet3>0.1)*(Pt_genmuon1>0.1)']


# Variables with 4 jet
Sels_Pt_pfjet4_reco = [basic_selection+j4,min_selection]
Sels_Pt_pfjet4_gen = [baregen_selection+gj4, '(Pt_genjet4>0.1)']

Sels_Eta_pfjet4_reco = [basic_selection+j4,min_selection]
Sels_Eta_pfjet4_gen = [baregen_selection+gj4, '(Pt_genjet4>0.1)']

Sels_DeltaPhi_pfjet4muon1_reco = [basic_selection+j4,min_selection]
Sels_DeltaPhi_pfjet4muon1_gen = [baregen_selection+gj4, '(Pt_genjet4>0.1)*(Pt_genmuon1>0.1)']


# Variables with inclusive jets

Sels_HT_pfjets_1_reco = [basic_selection+j1,min_selection]
Sels_HT_pfjets_1_gen = [baregen_selection+gj1, '(Pt_genjet1>0.1)']

Sels_HT_pfjets_2_reco = [basic_selection+j2,min_selection]
Sels_HT_pfjets_2_gen = [baregen_selection+gj2, '(Pt_genjet2>0.1)']

Sels_HT_pfjets_3_reco = [basic_selection+j3,min_selection]
Sels_HT_pfjets_3_gen = [baregen_selection+gj3, '(Pt_genjet3>0.1)']

Sels_HT_pfjets_4_reco = [basic_selection+j4,min_selection]
Sels_HT_pfjets_4_gen = [baregen_selection+gj4, '(Pt_genjet4>0.1)']



Sels_Pt_pfjet5_reco = [basic_selection+j4+'*(PFJet30Count>4.5)',min_selection]
Sels_Pt_pfjet6_reco = [basic_selection+j4+'*(PFJet30Count>5.5)',min_selection]


triggerweight = '*( (abs(Eta_muon1 +1.85)<0.25)*1.0344 + '
triggerweight += '(abs(Eta_muon1 +1.4)<0.2)*1.0550 + '
triggerweight += '(abs(Eta_muon1 +1.05)<0.15)*0.9858 + ' 
triggerweight += '(abs(Eta_muon1 +0.75)<0.15)*0.9876 + '
triggerweight += '(abs(Eta_muon1 +0.45)<0.15)*0.9837 + '
triggerweight += '(abs(Eta_muon1 +0.25)<0.05)*0.9597 + '
triggerweight += '(abs(Eta_muon1 -0)<0.2)*0.9815 + '
triggerweight += '(abs(Eta_muon1 -0.25)<0.05)*0.9630 + '
triggerweight += '(abs(Eta_muon1 -0.45)<0.15)*0.9847 + '
triggerweight += '(abs(Eta_muon1 -0.75)<0.15)*0.9932 + '
triggerweight += '(abs(Eta_muon1 -1.05)<0.15)*0.9776 + '
triggerweight += '(abs(Eta_muon1 -1.4)<0.2)*1.0402 + '
triggerweight += '(abs(Eta_muon1 -1.85)<0.25)*1.0623 )'


idisoweight = '*('
idisoweight += '(abs(Eta_muon1)<1.2)*('
idisoweight += '(abs(Pt_muon1-15)<5)*0.9400+'
idisoweight += '(abs(Pt_muon1-25)<5)*0.9754+'
idisoweight += '(abs(Pt_muon1-35)<5)*0.9897+'
idisoweight += '(abs(Pt_muon1-45)<5)*0.9928+'
idisoweight += '(abs(Pt_muon1-55)<5)*0.9922+'
idisoweight += '(abs(Pt_muon1-70)<10)*0.9843+'
idisoweight += '(abs(Pt_muon1-880)<800)*0.9903'
idisoweight += ')'
idisoweight += '+(abs(Eta_muon1)>=1.2)*('
idisoweight += '(abs(Pt_muon1-15)<5)*0.9963+'
idisoweight += '(abs(Pt_muon1-25)<5)*0.9883+'
idisoweight += '(abs(Pt_muon1-35)<5)*0.9899+'
idisoweight += '(abs(Pt_muon1-45)<5)*0.9910+'
idisoweight += '(abs(Pt_muon1-55)<5)*0.9862+'
idisoweight += '(abs(Pt_muon1-70)<10)*0.9886+'
idisoweight += '(abs(Pt_muon1-880)<800)*0.9720'
idisoweight += ')'
idisoweight += ')'


idisosysweight = '*('
idisosysweight += '(abs(Eta_muon1)<1.2)*('
idisosysweight += '(abs(Pt_muon1-15)<5)*0.9493+'
idisosysweight += '(abs(Pt_muon1-25)<5)*0.9775+'
idisosysweight += '(abs(Pt_muon1-35)<5)*0.9907+'
idisosysweight += '(abs(Pt_muon1-45)<5)*1.0109+'
idisosysweight += '(abs(Pt_muon1-55)<5)*0.9936+'
idisosysweight += '(abs(Pt_muon1-70)<10)*0.9872+'
idisosysweight += '(abs(Pt_muon1-880)<800)*0.9935'
idisosysweight += ')'
idisosysweight += '+(abs(Eta_muon1)>=1.2)*('
idisosysweight += '(abs(Pt_muon1-15)<5)*1.0028+'
idisosysweight += '(abs(Pt_muon1-25)<5)*0.9903+'
idisosysweight += '(abs(Pt_muon1-35)<5)*0.9910+'
idisosysweight += '(abs(Pt_muon1-45)<5)*0.9914+'
idisosysweight += '(abs(Pt_muon1-55)<5)*0.9888+'
idisosysweight += '(abs(Pt_muon1-70)<10)*0.9937+'
idisosysweight += '(abs(Pt_muon1-880)<800)*0.9778'
idisosysweight += ')'
idisosysweight += ')'


# This is the baseline selection - only one muon, fiducial region, MT in W window.

weight = '*weight_pu_central*4955'

weight += triggerweight + idisoweight

##########################################################################
########      Put all uses of the plotting funcs into main()      ########
##########################################################################

# The main function, called at the end of the script after all other function definitions. If just running analysis on a variable, modify only here.
def main():

	WRenorm = "(1.0)"
	# ParseTablesToFinalResults(WRenorm,basic_selection)	
	# ParseTablesToRecoHistograms()	
	# os.system("convert pyplots/*.png pyplots/AllPlots.pdf")
	# os.system("convert pyplots/*FINAL*Count.png pyplots/AllFinalCountPlots.pdf")
	# os.system("convert pyplots/*FINAL*XSec.png pyplots/AllFinalXSecPlots.pdf")
	# os.system("convert pyplots/*standard.png pyplots/StandardUnf.pdf")
	# os.system("convert pyplots/*altunf.png pyplots/SherpaUnf.pdf")
	# sys.exit()

	# selection = JetRescaleString+'*'+basic_selection

	htbinning = [30,60,90,120,150,195,240,285,330,390,450,510,570,660,750,840,990,1170,1500]
	htbinning = [30,60,90,120,150,180,210,240,270,300,360,420,480,540,600,720,840,960,1200,1700]
	htunfbinning1 = [114,15,1725]
	htunfbinning2 = [112,45,1725]
	htunfbinning3 = [110,75,1725]
	htunfbinning4 = [108,105,1725]
	htbinning = [30,60,90,120,150,180,210,240,270,300,360,420,480,540,600,660,720,780,840,900,1020,1140,1260,1500]
	htbinning = [30,60,90,120,150,195,240,285,330,390,450,510,570,660,750,840,990,1590]
	#mtbinning = [50,55,60,65,70,75,80,85,90,95,100,110,120,130,145,160,180,200,250]

	htunfbinningB1 = [58,0,1740]
	htunfbinningB2 = [57,30,1740]
	htunfbinningB3 = [56,60,1740]
	htunfbinningB4 = [55,90,1740]
	htbinningB = [30,60,90,120,150,180,240,300,360,420,510,600,720,870,1110,1590]


	_zmetbins = [0,2.5,5.0,7.5,10.0,12.5,15.0,17.5,20.0,22.5,25.0,30,35,40,45,50,60,70,80,100,135,200]
	_zmetbins = [0,2,4,6,8,10,12,14,16,18,20,23,27,33,43,61,95,161,300]
	_zuubins = [70,72.5,75,77.5,80,82.5,85,87.5,90,92.5,95,97.5,100,102.5,105,107.5,110]

	# F#ullAnalysisWithUncertainty(['M_muon1muon2','M_muon1muon2'],'M_muon1muon2',-1,["M_{#mu #mu} [GeV]","Z_j1"],[100,0,500],_zuubins,Sels_ZCont1_Pt_MET_reco,Sels_ZCont1_Pt_MET_gen,weight,'c',22)

	# F#ullAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]","Z_j1"],[100,0,500],_zmetbins,Sels_ZCont1_Pt_MET_reco,Sels_ZCont1_Pt_MET_gen,weight,'c',22)
	# F#ullAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]","TT_j1"],[100,0,500],[50,0,200],Sels_TCont1_Pt_MET_reco,Sels_TCont1_Pt_MET_gen,weight,'c',22)

	# F#ullAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]","Z_j2"],[100,0,500],_zmetbins,Sels_ZCont2_Pt_MET_reco,Sels_ZCont2_Pt_MET_gen,weight,'c',22)
	# F#ullAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]","Z_j3"],[100,0,500],_zmetbins,Sels_ZCont3_Pt_MET_reco,Sels_ZCont3_Pt_MET_gen,weight,'c',22)
	# F#ullAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]","Z_j4"],[100,0,500],_zmetbins,Sels_ZCont4_Pt_MET_reco,Sels_ZCont4_Pt_MET_gen,weight,'c',22)

	# F#ullAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]","TT_j2"],[100,0,500],[50,0,200],Sels_TCont2_Pt_MET_reco,Sels_TCont2_Pt_MET_gen,weight,'c',22)
	# F#ullAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]","TT_j3"],[100,0,500],[50,0,200],Sels_TCont3_Pt_MET_reco,Sels_TCont3_Pt_MET_gen,weight,'c',22)
	# F#llAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]","TT_j4"],[100,0,500],[50,0,200],Sels_TCont4_Pt_MET_reco,Sels_TCont4_Pt_MET_gen,weight,'c',22)

	# F#ullAnalysisWithUncertainty(['M_muon1muon2','M_muon1muon2'],'M_muon1muon2',-1,["M_{#mu #mu} [GeV]","Z_j2"],[100,0,500],_zuubins,Sels_ZCont2_Pt_MET_reco,Sels_ZCont2_Pt_MET_gen,weight,'c',22)
	# F#ullAnalysisWithUncertainty(['M_muon1muon2','M_muon1muon2'],'M_muon1muon2',-1,["M_{#mu #mu} [GeV]","Z_j3"],[100,0,500],_zuubins,Sels_ZCont3_Pt_MET_reco,Sels_ZCont3_Pt_MET_gen,weight,'c',22)
	# F#ullAnalysisWithUncertainty(['M_muon1muon2','M_muon1muon2'],'M_muon1muon2',-1,["M_{#mu #mu} [GeV]","Z_j4"],[100,0,500],_zuubins,Sels_ZCont4_Pt_MET_reco,Sels_ZCont4_Pt_MET_gen,weight,'c',22)









	# sys.exit()

	FullAnalysisWithUncertainty(['Pt_genjet1','Pt_genjet1_bare'],'Pt_pfjet1',0,["p_{T}(jet_{1}) [GeV]",""],[40,10,810],[30,50,70,90,110,150,190,250,310,400,750],Sels_Pt_pfjet1_reco, Sels_Pt_pfjet1_gen,weight,'c',12)
	FullAnalysisWithUncertainty(['Pt_genjet2','Pt_genjet2_bare'],'Pt_pfjet2',0,["p_{T}(jet_{2}) [GeV]",""],[30,10,610],[30,50,70,90,110,150,190,250,550],Sels_Pt_pfjet2_reco, Sels_Pt_pfjet2_gen,weight,'c',7)
	FullAnalysisWithUncertainty(['Pt_genjet3','Pt_genjet3_bare'],'Pt_pfjet3',0,["p_{T}(jet_{3}) [GeV]",""],[25,10,510],[30,50,70,90,110,150,210,450],Sels_Pt_pfjet3_reco, Sels_Pt_pfjet3_gen,weight,'c',4)
	FullAnalysisWithUncertainty(['Pt_genjet4','Pt_genjet4_bare'],'Pt_pfjet4',0,["p_{T}(jet_{4}) [GeV]",""],[20,10,410],[30,50,70,90,350],Sels_Pt_pfjet4_reco, Sels_Pt_pfjet4_gen,weight,'c',4)

	FullAnalysisWithUncertainty(['GenJet30Count','GenJet30Count'],'PFJet30Count',-1,["N_{Jet}",""],[11,-.5,10.5],[6 ,0.5,6.5],Sels_PFJet30Count_reco,Sels_PFJet30Count_gen,weight,'c',3)	
	FullAnalysisWithUncertainty(['GenJet30Count','GenJet30Count'],'PFJet30Count',-1,["N_{Jet}","_preexc"],[11,-.5,10.5],[8 ,0.5,8.5],Sels_PFJet30Count_reco,Sels_PFJet30Count_gen,weight,'c',4)	

	FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',25.,["H_{T}(jets) [GeV]","_inc1"],htunfbinningB1,htbinningB[0:],Sels_HT_pfjets_1_reco, Sels_HT_pfjets_1_gen,weight,'c',8)
	FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',55.,["H_{T}(jets) [GeV]","_inc2"],htunfbinningB2,htbinningB[1:],Sels_HT_pfjets_2_reco, Sels_HT_pfjets_2_gen,weight,'c',8)
	FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',85.,["H_{T}(jets) [GeV]","_inc3"],htunfbinningB3,htbinningB[2:],Sels_HT_pfjets_3_reco, Sels_HT_pfjets_3_gen,weight,'c',8)
	FullAnalysisWithUncertainty(['HT_genjets','HT_genjets'],'HT_pfjets',115.,["H_{T}(jets) [GeV]","_inc4"],htunfbinningB4,htbinningB[3:],Sels_HT_pfjets_4_reco, Sels_HT_pfjets_4_gen,weight,'c',8)


	FullAnalysisWithUncertainty(['Eta_genjet1','Eta_genjet1_bare'],'Eta_pfjet1',-2.5,["#eta(jet_{1}) ",""],[28,-2.8,2.8],[24,-2.4,2.4],Sels_Eta_pfjet1_reco, Sels_Eta_pfjet1_gen,weight,'c',6)
	FullAnalysisWithUncertainty(['Eta_genjet2','Eta_genjet2_bare'],'Eta_pfjet2',-2.5,["#eta(jet_{2}) ",""],[28,-2.8,2.8],[24,-2.4,2.4],Sels_Eta_pfjet2_reco, Sels_Eta_pfjet2_gen,weight,'c',6)
	FullAnalysisWithUncertainty(['Eta_genjet3','Eta_genjet3_bare'],'Eta_pfjet3',-2.5,["#eta(jet_{3}) ",""],[10,-3.0,3.0],[8,-2.4,2.4],Sels_Eta_pfjet3_reco, Sels_Eta_pfjet3_gen,weight,'c',3)
	FullAnalysisWithUncertainty(['Eta_genjet4','Eta_genjet4_bare'],'Eta_pfjet4',-2.5,["#eta(jet_{4}) ",""],[8,-3.2,3.2],[6,-2.4,2.4],Sels_Eta_pfjet4_reco, Sels_Eta_pfjet4_gen,weight,'c',3)

	FullAnalysisWithUncertainty(['DeltaPhi_genjet1genmuon1','DeltaPhi_genjet1genmuon1_bare'],'DeltaPhi_pfjet1muon1',-0.05,["#Delta#phi(jet_{1},#mu) [GeV]",""],[22,-.15707963,3.1415927+.15707963],[20,0,3.1415927],Sels_DeltaPhi_pfjet1muon1_reco,Sels_DeltaPhi_pfjet1muon1_gen,weight,'c',5)
	FullAnalysisWithUncertainty(['DeltaPhi_genjet2genmuon1','DeltaPhi_genjet2genmuon1_bare'],'DeltaPhi_pfjet2muon1',-0.05,["#Delta#phi(jet_{2},#mu) [GeV]",""],[17,-0.20943950,3.1415927+0.20943950],[15,0,3.1415927],Sels_DeltaPhi_pfjet2muon1_reco,Sels_DeltaPhi_pfjet2muon1_gen,weight,'c',5)
	FullAnalysisWithUncertainty(['DeltaPhi_genjet3genmuon1','DeltaPhi_genjet3genmuon1_bare'],'DeltaPhi_pfjet3muon1',-0.05,["#Delta#phi(jet_{3},#mu) [GeV]",""],[12,-0.31415926,3.1415927+0.31415926],[10,0,3.1415927],Sels_DeltaPhi_pfjet3muon1_reco,Sels_DeltaPhi_pfjet3muon1_gen,weight,'c',4)
	FullAnalysisWithUncertainty(['DeltaPhi_genjet4genmuon1','DeltaPhi_genjet4genmuon1_bare'],'DeltaPhi_pfjet4muon1',-0.05,["#Delta#phi(jet_{4},#mu) [GeV]",""],[8,-0.523598766,3.1415927+0.523598766],[6,0,3.1415927],Sels_DeltaPhi_pfjet4muon1_reco,Sels_DeltaPhi_pfjet4muon1_gen,weight,'c',4)

	FullAnalysisWithUncertainty(['Pt_genMET','Pt_genMET'],'Pt_MET',-1,["E_{T}^{miss} [GeV]",""],[100,0,500],[0,10,20,30,40,50,60,70,80,90,100,115,130,150,170,200,250,400],Sels_Pt_MET_reco,Sels_Pt_MET_gen,weight,'c',22)
	FullAnalysisWithUncertainty(['MT_genmuon1genMET','MT_genmuon1genMET_bare'],'MT_muon1METR',25,["M_{T}(#mu,E_{T}^{miss}) [GeV]",""],[50,0,250],[40,0,200],Sels_MT_genmuon1genMET_reco,Sels_MT_genmuon1genMET_gen,weight,'c',28)


	FullAnalysisWithUncertainty(['Pt_genmuon1','Pt_genmuon1_bare'],'Pt_muon1',0,["p_{T}(#mu_{1}) [GeV]",""],[80,15,415],[25,30,35,40,45,50,55,60,70,80,90,100,115,130,145,160,180,200,230,260,300],Sels_Pt_muon1_reco,Sels_Pt_muon1_gen,weight,'c',10)
	FullAnalysisWithUncertainty(['Eta_genmuon1','Eta_genmuon1_bare'],'Eta_muon1',0,["#eta (#mu_{1}) [GeV]",""],[92,-2.3,2.3],[42,-2.1,2.1],Sels_Eta_muon1_reco,Sels_Eta_muon1_gen,weight,'c',10)

	FullAnalysisWithUncertainty(['N_GoodVertices','N_GoodVertices'],'N_GoodVertices',0,["N_GoodVertices",""],[51,-1,50],[40,0,40],Sels_Eta_muon1_reco,Sels_Eta_muon1_gen,weight,'c',10)


	

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
gROOT.ProcessLine("gErrorIgnoreLevel = 3001;") # Suppress warnings
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
	# tmpfile = TFile.Open('tmp'+str(random.randint(0,100000000))+str(random.randint(0,100000000))+'.root',"RECREATE")
	# print 'Creating histo for ',name, legendname,
	binset=ConvertBinning(binning) # Assure variable binning
	n = len(binset)-1 # carry the 1
	# print '   ... bins created.'
	hout= TH1D(name,legendname,n,array('d',binset)) # Declar empty TH1D
	hout.Sumw2() # Store sum of squares
	# print '   ... histo initialized.'
	tree.Project(name,variable,selection) # Project from branch to histo
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


# Make basic TH1D for a branch. Projects branch to histo for given binning and selection. 
def NullHisto(name,legendname,binning,style,label):
	binset=ConvertBinning(binning) # Assure variable binning
	n = len(binset)-1 # carry the 1
	hout= TH1D(name,legendname,n,array('d',binset)) # Declar empty TH1D
	hout.Sumw2() # Store sum of squares
	
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

	hout.GetXaxis().SetTitleFont(42)
	hout.GetYaxis().SetTitleFont(42)
	hout.GetXaxis().SetLabelFont(42)
	hout.GetYaxis().SetLabelFont(42)

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
	
	
	return hout

def MakeInclusiveBinInfo(bininfo):

	outputinfo = []

	inputinfo = []
	_cont = []
	_err = []
	_bin = []
	for x in bininfo:
		_bin.append(x[0])
		hcont = x[1].split('+-')
		_cont.append(float(hcont[0]))
		_err.append(float(hcont[1]))

	def CumulativeSum(_alist,_flag_quadrature):
		if _flag_quadrature == 'linear':
			_do_quadrature = False
		elif _flag_quadrature == 'quadrature':
			_do_quadrature = True
		else:
			print 'Incorrect flag for quadrature!'
			sys.exit()
		_out_alist = []
		for _x in range(len(_alist)):
			x = _alist[_x]
			bintot = 0.0
			for _y in range(len(_alist)):
				y = _alist[_y]
				if _y >=_x:
					bintot_addon = 1.0*y
					if _do_quadrature:
						bintot_addon *= y
					bintot += bintot_addon
			if _do_quadrature:
				bintot = math.sqrt(bintot)
			_out_alist.append(bintot)
		return _out_alist

	_newcont = CumulativeSum(_cont,'linear')
	_newerr = CumulativeSum(_err,'quadrature')
	for _x in range(len(_bin)):
		_thisinfo = []
		_thisinfo.append(_bin[_x])
		_thisinfo.append(str(_newcont[_x]) + ' +- '+str(_newerr[_x]))
		outputinfo.append(_thisinfo)

	return outputinfo



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

		print 'Statcov Bin:Cont',i,data.GetBinError(i)*data.GetBinError(i)
	
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
	print 'TABULATING A BIN-BY-BIN RESCALING!!'
	num = Params[1].Clone()
	denom = Params[0].Clone()
	num.Divide(denom)
	unfres_mod = data_histo.Clone()
	unfres_mod.Multiply(num) 
	print 'bin-by-bin rescaling complete'
	# Get the distribution of the d to cross check the regularization
	# - choose kreg to be the point where |d_i| stop being statistically significantly >>1
	ddist = tsvdunf.GetD()
	ddist.SetTitle("Diagonal Values")
		
	# Get the distribution of the singular values
	svdist = tsvdunf.GetSV()
	svdist.SetTitle("Singular Values")
	print 'got D/SV dists'
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
	print 'Got covariances'
	# Errors on unfolding result.
	for i in range(unfres.GetNbinsX()):
		if OptTau != 123456:
			continue
		unfres.SetBinError(i, math.sqrt(utaucov.GetBinContent(i,i)))
	print 'errors set, returning...'
	if OptTau != 123456:
		return [unfres,ddist,svdist,OptTau,OptI]
	else:
		return [unfres_mod,ddist,svdist,OptTau,OptI]

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


def TestFit(flatarray):
	ft = TF1("ft","[1]*x + [0]", 0,len(flatarray)+1 )
	xaxis = [n for n in range(len(flatarray))]
	flatarray = array("d",flatarray) 
	xaxis = array("d",xaxis) 
	n = len(xaxis)
	hout = TGraph(n,xaxis,flatarray)
	hout.Fit('ft')
	slope = ft.GetParameter(1)
	slope_err = ft.GetParError(1)

	# print ' ---- ',slope, slope_err

	isinc = slope > 0.0
	isflat = ((abs(slope) - abs(slope_err)) < 0.0)

	result = isinc or isflat
	# print "Result:", result
	return result

def FindFlatPoint(inflatarray):
	flatresult = 99
	flatarray = []
	for x in inflatarray:
		if x>0.00001:
			flatarray.append(x)


	for n in range(len(flatarray)):
		if n < 2:
			continue
		isflat = TestFit(flatarray[n:])
		if isflat:
			flatresult = n
			break
	print 'FOUND FLAT AT  tau = ',n
	return flatresult


# This will test multiple values of tau with TestSVDTau, and find the best tau as the smallest difference of GEN wrt controlled unfoldings.
def FindOptimalTauWithDIVals(Params,hdata,binning):
	binset=ConvertBinning(binning)
	n = len(binset)-1


	hreco = Params[0]
	hgen = Params[1]
	hresp = Params[2]

	oldcont = -99.9;
	cont = -99.9;
	best_tau = -99.9;

	tau = 2
	[unfres,ddist,svdist] = GetSVD(hdata,[hreco,hgen,hresp],tau,binning)
	print 'Bin Ind', 'i value' ,'D_i Value' 
	distcont = []

	for x in range(ddist.GetNbinsX()+2):
		cont = ddist.GetBinContent(x)
		print x, ddist.GetBinCenter(x) - 0.5, cont
		distcont.append(cont)
	best_tau = FindFlatPoint(distcont)
	print "\n +++++++++++ Choosing tau value: ",best_tau,'\n'
	if best_tau < 2:
		best_tau = 2
	mid_tau = int(round(0.5*n))
	
	if best_tau > mid_tau:
		print 'defaulting to half distribution size.'
		best_tau = mid_tau
	if mid_tau>=40:
		best_tau = int(round(best_tau*0.5))
	return best_tau

# This will test multiple values of tau with TestSVDTau, and find the best tau as the smallest difference of GEN wrt controlled unfoldings.
def FindOptimalTauWithDIValsBasic(Params,hdata,binning,should_offset):
	binset=ConvertBinning(binning)
	n = len(binset)-1


	hreco = Params[0]
	hgen = Params[1]
	hresp = Params[2]

	oldcont = -99.9;
	cont = -99.9;
	best_tau = -99.9;

	tau = 2
	[unfres,ddist,svdist] = GetSVD(hdata,[hreco,hgen,hresp],tau,binning)
	print 'Bin Ind', 'i value' ,'D_i Value', 
	for x in range(ddist.GetNbinsX()+2):
		cont = ddist.GetBinContent(x)
		print x, ddist.GetBinCenter(x) - 0.5, cont
		# if ddist.GetBinCenter(x)<2:
		# 	continue
		if (oldcont >1.0 and cont<1.0 and best_tau < -99.0) or (oldcont < 2.0 and cont>2.0 and best_tau < -99.0):
			if ddist.GetBinCenter(x)>=2:
				best_tau = ddist.GetBinCenter(x)

		oldcont = cont

	best_tau = int(best_tau-0.5)
	print "\n +++++++++++ Choosing tau value: ",best_tau,'\n'
	if best_tau < 2:
		best_tau = 2
	return best_tau


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
	hs_rec_WJets_win=CreateHisto('hs_rec_WJets_win','W+Jets [Reco] (Win)',t_WJets_MG,variable,fullbinning,selection+weight+"*(MT_muon1METR>50)*(MT_muon1METR<300)",MCRecoStyle,Label)

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


	table = '\n\nJet Multiplicity | Muon PT | Global Scale Factor | Isolation Fake Rate (Data) | Isolation Fake Rate (QCD MC)| Total Rescaling \\\\ \\hline \n'

	globalreweightingvals = MakeBasicPlotQCD('Pt_MET',"E_{T}^{miss} [GeV]",[50,0,10],selection+'*(RelIso_muon1<0.15)*(MT_muon1METR>50)',gen_selection,weight,FileDirectory,'globalreweightbackground','(1.0)')

	globaldata = globalreweightingvals[6][0]
	globalmc = globalreweightingvals[5][0]+ globalreweightingvals[0][0]+globalreweightingvals[1][0]+globalreweightingvals[2][0]+globalreweightingvals[3][0]+globalreweightingvals[4][0]

	globalscale = str(round(globaldata/globalmc,3))

	selection += ('*(Pt_MET<10.0)')

	weight = weight+'*('+globalscale+')'

	jetreq = -1
	ptpoint = ''

	scalestring_qcd_central = '('
	scalestring_qcd_up = '('
	scalestring_qcd_down = '('

	for jetcut in ['*(PFJet30Count==0)','*(PFJet30Count==1)','*(PFJet30Count==2)','*(PFJet30Count==3)','*(PFJet30Count==4)','*(PFJet30Count==5)']:
	# for jetcut in ['*(PFJet30Count==0)','*(PFJet30Count==1)']:
		jetreq += 1

		for ptrange in ['*(Pt_muon1>25)*(Pt_muon1<40)','*(Pt_muon1>40)']:
			ptpoint = ((ptrange.split('>')[1]).split(')')[0]).replace(' ','')

			nonisovals = MakeBasicPlotQCD('Pt_MET',"E_{T}^{miss} [GeV] (Non-Iso, Non-Rescaled, Njet="+str(jetreq)+')',[50,0,10],selection+jetcut+ptrange,gen_selection,weight,FileDirectory,'qcdunscaled_noniso_'+str(jetreq)+'jet_mupt_'+ptpoint,'(1.0)')
			nonisodata = nonisovals[6][0]
			nonisoqcd = nonisovals[5][0]
			nonisobg = nonisovals[0][0]+nonisovals[1][0]+nonisovals[2][0]+nonisovals[3][0]+nonisovals[4][0]
			nonisodata_err = nonisovals[6][1]
			nonisoqcd_err = nonisovals[5][1] 
			nonisobg_err = math.sqrt(nonisovals[0][1]**2+nonisovals[1][1]**2+nonisovals[2][1]**2+nonisovals[3][1]**2+nonisovals[4][1]**2)

			isovals = MakeBasicPlotQCD('Pt_MET',"E_{T}^{miss} [GeV] (Isolated, Non-Rescaled, Njet="+str(jetreq)+')',[50,0,10],selection+jetcut+'*(RelIso_muon1<0.15)'+ptrange,gen_selection,weight,FileDirectory,'qcdunscaled_iso_'+str(jetreq)+'jet_mupt_'+ptpoint,'(1.0)')
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

			scalestring_qcd_central += ' ('+str(round(TotalNorm,4))+')' +jetcut+ptrange +' +'*(jetreq!=5) + ' )'*(jetreq ==5)
			scalestring_qcd_up += ' ('+str(round(TotalNorm + TotalNorm_err,4))+')' +jetcut+ptrange +' +'*(jetreq!=5)+ ' )'*(jetreq ==5)
			scalestring_qcd_down += ' ('+str(round(TotalNorm - TotalNorm_err,4))+')' +jetcut+ptrange +' +'*(jetreq!=5)+ ' )'*(jetreq ==5)

			table += '$N_{jet} =='+str(jetreq) + ' $  &  ' + 'Muon $p_T >$ ' +ptpoint+' & '
			table += str(round(ScaleFactor,3)) + '\\pm' + str(round(ScaleFactor_err,3)) + ' & '
			table += str(round(FakeRate,3)) + '\\pm' + str(round(FakeRate_err,3)) + ' & '
			table += str(round(MCFakeRate,3)) + '\\pm' + str(round(MCFakeRate_err,3)) + ' & '
			table += str(round(TotalNorm,3)) + '\\pm' + str(round(TotalNorm_err,3)) + ' \\\\ \\hline \n '


			null = MakeBasicPlotQCD('Pt_MET',"E_{T}^{miss} [GeV](Non-Isolated, Global QCD MC Rescaling = "+str(round(ScaleFactor,2))+" , Njet="+str(jetreq)+')',[50,0,10],selection+jetcut+ptrange,gen_selection,weight,FileDirectory,'qcdscaled_noniso_'+str(jetreq)+'jet_mupt_'+ptpoint,'('+str(ScaleFactor)+')' ) 

			ratednonisovals = MakeBasicPlotQCD('Pt_MET',"E_{T}^{miss} [GeV](Isolated, QCD FakeRate*Rescaling = "+str(round(TotalNorm,2))+", Njet="+str(jetreq)+')',[50,0,10],selection+jetcut+'*(RelIso_muon1<0.15)'+ptrange,gen_selection,weight,FileDirectory,'qcdrated_iso_'+str(jetreq)+'jet_mupt_'+ptpoint,'('+str(TotalNorm)+')' ) 
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
		qcdselection = qcdselection.replace('*(RelIso_muon1<0.15)','')

	### Make the plots without variable bins!
	hs_rec_WJets=CreateHisto('hs_rec_WJets','W+Jets [Reco]',t_WJets_MG,recovariable,presentationbinning,selection+weight,WStackStyle,Label)
	# print 'got wjets', hs_rec_WJets.Integral()
	hs_rec_Data=CreateHisto('hs_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recovariable,presentationbinning,selection+'*Mu24PassPrescale*(Mu24Pass>0.5)',DataRecoStyle,Label)
	print 'got data', hs_rec_Data.Integral()
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
# 	# starting_selection += '*(PFJet30Count>1.5)'#*(PFJet30TCHEMCount>0.5)'
# 	[w,tt,ot,dat] = MakeBasicPlot('PFJet30Count',"N_{Jet} (Inclusive) [GeV]",[7,-0.5,6.5],starting_selection,gen_selection,weight,FileDirectory,'_btageff')
# 	[w2,tt2,ot2,dat2] = MakeBasicPlot('PFJet30Count',"N_{Jet} (Inclusive) [GeV]",[7,-0.5,6.5],starting_selection+'*(PFJet30TCHEMCount>1.5)',gen_selection,weight,FileDirectory,'_btageff')

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
	hs_rec_Data=CreateHisto('hs_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recovariable,presentationbinning,selection+IsoMuCond,DataRecoStyle,Label)
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
# 	# starting_selection += '*(PFJet30Count>1.5)'#*(PFJet30TCHEMCount>0.5)'
# 	[w,tt,ot,dat] = MakeBasicPlot('PFJet30Count',"N_{Jet} (Inclusive) [GeV]",[7,-0.5,6.5],starting_selection,gen_selection,weight,FileDirectory,'_btageff')
# 	[w2,tt2,ot2,dat2] = MakeBasicPlot('PFJet30Count',"N_{Jet} (Inclusive) [GeV]",[7,-0.5,6.5],starting_selection+'*(PFJet30TCHEMCount>1.5)',gen_selection,weight,FileDirectory,'_btageff')

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





def GetSFIntegrated(histolist,_d,_m,_o):

	_c = [[__h.GetBinContent(1),__h.GetBinError(1)] for __h in histolist]

	_D = _c[_d]
	_M = _c[_m]
	_OList = [_c[x] for x in _o]
	_O = []
	_O.append(sum([x[0] for x in _OList]))
	_O.append(math.sqrt(sum([x[1]*x[1] for x in _OList])))

	num = _D[0] - _O[0]
	num_err = math.sqrt(_D[1]*_D[1] + _O[1]*_O[1])
	denom = _M[0]
	denom_err = _M[1]

	sf = num/denom
	sf_err = sf*(  (num_err/num)**2.0 + (denom_err/denom)**2 )

	_SF = str(round(sf,4)) + ' +- '+str(round(sf_err,4))

	return [[sf,sf_err],_SF]



def GetSF(histolist,_d,_m,_o):

	_c = [[__h.GetBinContent(1),__h.GetBinError(1)] for __h in histolist]

	_D = _c[_d]
	_M = _c[_m]
	_OList = [_c[x] for x in _o]
	_O = []
	_O.append(sum([x[0] for x in _OList]))
	_O.append(math.sqrt(sum([x[1]*x[1] for x in _OList])))

	num = _D[0] - _O[0]
	num_err = math.sqrt(_D[1]*_D[1] + _O[1]*_O[1])
	denom = _M[0]
	denom_err = _M[1]

	sf = num/denom
	sf_err = sf*(  (num_err/num)**2.0 + (denom_err/denom)**2 )

	_SF = str(round(sf,4)) + ' +- '+str(round(sf_err,4))

	return [[sf,sf_err],_SF]

def GetScaleFactors(recoselections,weight,FileDirectory):

	##############################################################################
	#######     Basic setup - Get the files and trees, designate styles    #######
	##############################################################################

	# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
	allfiles = [x.replace('\n','') for x in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines()]
	if 'SingleMuData.root' not in allfiles:
		allfiles.append('SingleMuData.root')
	for f in allfiles:
		if 'Scale' in f or 'Match' in f or 'out' in f:
			continue
		fin = f.replace('\n','')

		if 'WJets_MG' in fin:
			exec("t_MG = TFile.Open(\""+FileDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")	

		if 'Data' not in fin:
			exec('t_'+f.replace(".root","")+" = TFile.Open(\""+FileDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")
		if 'Data' in fin:
			exec('t_'+f.replace(".root","")+" = TFile.Open(\""+NormalDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")


	##############################################################################
	#######   Define selections and weights for normal, qcd, and unfolding #######
	##############################################################################


	[selection, selection_minimal] = recoselections
	recomodvariable = '1'
	binning = [1,0,2]

	# Get optimal variable binning binning
	varbinning=GetConstBinStructure(binning)

	##############################################################################
	#######   Preparation and stylistic modifications below                #######
	##############################################################################

	tmpname = "tmp"+str(random.randint(0,1000000))+".root"
	tmpfile = TFile(tmpname,"RECREATE") # temporary root file. Named with random number so you can run several versions of this script at once if needed.

	# These are the style parameters for certain plots - [FillStyle,MarkerStyle,MarkerSize,LineWidth,Color]
	MCGenStyle=[0,20,.00001,1,2]
	MCGenSmearStyle=[0,20,.00001,1,9]

	MCRecoStyle=[0,21,.00001,1,4]
	DataRecoStyle=[0,20,1.0,1,1]
	DataCompStyle=[0,21,0.5,1,6]
	BlankRecoStyle=[0,21,.00001,1,0]
	DataUnfoldedStyle=[0,21,0.5,1,1]
	DataUnfoldedStyle_pseudo=[0,20,0.5,1,9]
	DataUnfoldedStyle_pseudo2=[0,20,0.5,1,2]

	# X and Y axis labels for plot
	Label=["X","Events/Bin"]

	WStackStyle=[3007,20,.00001,2,6]
	TTStackStyle=[3005,20,.00001,2,4]
	ZStackStyle=[3004,20,.00001,2,2]
	DiBosonStackStyle=[3006,20,.00001,2,3]
	StopStackStyle=[3008,20,.00001,2,9]
	QCDStackStyle=[3013,20,.00001,2,15]

	# Convert to variable binning.
	presentationbinning = [1,0,2]
	presentationbinning=ConvertBinning(presentationbinning)


	##############################################################################
	#######   Get Data-Driven Scale Factors                                #######
	##############################################################################


	ttbar_selection = selection.replace('(PFJet30TCHEMCountCentral<0.5)','(PFJet30TCHEMCountCentral>1.5)')
	ttbar_selection1 = selection.replace('(PFJet30TCHEMCountCentral<0.5)','(PFJet30TCHEMCountEffUp>1.5)')
	ttbar_selection2 = selection.replace('(PFJet30TCHEMCountCentral<0.5)','(PFJet30TCHEMCountEffDown>1.5)')
	ttbar_selection3 = selection.replace('(PFJet30TCHEMCountCentral<0.5)','(PFJet30TCHEMCountMisUp>1.5)')
	ttbar_selection4 = selection.replace('(PFJet30TCHEMCountCentral<0.5)','(PFJet30TCHEMCountMisDown>1.5)')
	w_selection = selection

	z_selection = selection.replace('(Pt_muon2<25)','(Pt_muon2>25)')

	__Z_h_rec_Data=CreateHisto('__Z_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,varbinning,z_selection+IsoMuCond,DataRecoStyle,Label)
	__Z_h_rec_WJetsMG=CreateHisto('__Z_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_MG,recomodvariable,varbinning,z_selection+weight,MCRecoStyle,Label)
	__Z_h_rec_DiBoson=CreateHisto('__Z_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,varbinning,z_selection+weight,DiBosonStackStyle,Label)
	__Z_h_rec_ZJets=CreateHisto('__Z_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,varbinning,z_selection+weight,ZStackStyle,Label)
	__Z_h_rec_TTBar=CreateHisto('__Z_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,varbinning,z_selection+weight,TTStackStyle,Label)
	__Z_h_rec_SingleTop=CreateHisto('__Z_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,varbinning,z_selection+weight,StopStackStyle,Label)

	__W_h_rec_Data=CreateHisto('__W_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,varbinning,w_selection+IsoMuCond,DataRecoStyle,Label)
	__W_h_rec_WJetsMG=CreateHisto('__W_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_MG,recomodvariable,varbinning,w_selection+weight,MCRecoStyle,Label)
	__W_h_rec_DiBoson=CreateHisto('__W_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,varbinning,w_selection+weight,DiBosonStackStyle,Label)
	__W_h_rec_ZJets=CreateHisto('__W_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,varbinning,w_selection+weight,ZStackStyle,Label)
	__W_h_rec_TTBar=CreateHisto('__W_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,varbinning,w_selection+weight,TTStackStyle,Label)
	__W_h_rec_SingleTop=CreateHisto('__W_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,varbinning,w_selection+weight,StopStackStyle,Label)

	__T_h_rec_Data=CreateHisto('__T_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,varbinning,ttbar_selection+IsoMuCond,DataRecoStyle,Label)
	__T_h_rec_WJetsMG=CreateHisto('__T_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_MG,recomodvariable,varbinning,ttbar_selection+weight,MCRecoStyle,Label)
	__T_h_rec_DiBoson=CreateHisto('__T_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,varbinning,ttbar_selection+weight,DiBosonStackStyle,Label)
	__T_h_rec_ZJets=CreateHisto('__T_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,varbinning,ttbar_selection+weight,ZStackStyle,Label)
	__T_h_rec_TTBar=CreateHisto('__T_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,varbinning,ttbar_selection+weight,TTStackStyle,Label)
	__T_h_rec_SingleTop=CreateHisto('__T_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,varbinning,ttbar_selection+weight,StopStackStyle,Label)

	__T1_h_rec_Data=CreateHisto('__T1_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,varbinning,ttbar_selection1+IsoMuCond,DataRecoStyle,Label)
	__T1_h_rec_WJetsMG=CreateHisto('__T1_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_MG,recomodvariable,varbinning,ttbar_selection1+weight,MCRecoStyle,Label)
	__T1_h_rec_DiBoson=CreateHisto('__T1_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,varbinning,ttbar_selection1+weight,DiBosonStackStyle,Label)
	__T1_h_rec_ZJets=CreateHisto('__T1_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,varbinning,ttbar_selection1+weight,ZStackStyle,Label)
	__T1_h_rec_TTBar=CreateHisto('__T1_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,varbinning,ttbar_selection1+weight,TTStackStyle,Label)
	__T1_h_rec_SingleTop=CreateHisto('__T1_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,varbinning,ttbar_selection1+weight,StopStackStyle,Label)

	__T2_h_rec_Data=CreateHisto('__T2_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,varbinning,ttbar_selection2+IsoMuCond,DataRecoStyle,Label)
	__T2_h_rec_WJetsMG=CreateHisto('__T2_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_MG,recomodvariable,varbinning,ttbar_selection2+weight,MCRecoStyle,Label)
	__T2_h_rec_DiBoson=CreateHisto('__T2_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,varbinning,ttbar_selection2+weight,DiBosonStackStyle,Label)
	__T2_h_rec_ZJets=CreateHisto('__T2_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,varbinning,ttbar_selection2+weight,ZStackStyle,Label)
	__T2_h_rec_TTBar=CreateHisto('__T2_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,varbinning,ttbar_selection2+weight,TTStackStyle,Label)
	__T2_h_rec_SingleTop=CreateHisto('__T2_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,varbinning,ttbar_selection2+weight,StopStackStyle,Label)

	__T3_h_rec_Data=CreateHisto('__T_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,varbinning,ttbar_selection3+IsoMuCond,DataRecoStyle,Label)
	__T3_h_rec_WJetsMG=CreateHisto('__T3_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_MG,recomodvariable,varbinning,ttbar_selection3+weight,MCRecoStyle,Label)
	__T3_h_rec_DiBoson=CreateHisto('__T3_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,varbinning,ttbar_selection3+weight,DiBosonStackStyle,Label)
	__T3_h_rec_ZJets=CreateHisto('__T3_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,varbinning,ttbar_selection+weight,ZStackStyle,Label)
	__T3_h_rec_TTBar=CreateHisto('__T3_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,varbinning,ttbar_selection+weight,TTStackStyle,Label)
	__T3_h_rec_SingleTop=CreateHisto('__T3_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,varbinning,ttbar_selection3+weight,StopStackStyle,Label)

	__T4_h_rec_Data=CreateHisto('__T4_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,varbinning,ttbar_selection4+IsoMuCond,DataRecoStyle,Label)
	__T4_h_rec_WJetsMG=CreateHisto('__T4_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_MG,recomodvariable,varbinning,ttbar_selection4+weight,MCRecoStyle,Label)
	__T4_h_rec_DiBoson=CreateHisto('__T4_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,varbinning,ttbar_selection4+weight,DiBosonStackStyle,Label)
	__T4_h_rec_ZJets=CreateHisto('__T4_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,varbinning,ttbar_selection4+weight,ZStackStyle,Label)
	__T4_h_rec_TTBar=CreateHisto('__T4_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,varbinning,ttbar_selection4+weight,TTStackStyle,Label)
	__T4_h_rec_SingleTop=CreateHisto('__T4_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,varbinning,ttbar_selection4+weight,StopStackStyle,Label)		

	__Z_histos = [__Z_h_rec_Data,	__Z_h_rec_WJetsMG,	__Z_h_rec_DiBoson,	__Z_h_rec_ZJets,	__Z_h_rec_TTBar,	__Z_h_rec_SingleTop]
	__W_histos = [__W_h_rec_Data,	__W_h_rec_WJetsMG,	__W_h_rec_DiBoson,	__W_h_rec_ZJets,	__W_h_rec_TTBar,	__W_h_rec_SingleTop]

	__T_histos = [__T_h_rec_Data,	__T_h_rec_WJetsMG,	__T_h_rec_DiBoson,	__T_h_rec_ZJets,	__T_h_rec_TTBar,	__T_h_rec_SingleTop]
	__T1_histos = [__T1_h_rec_Data,	__T1_h_rec_WJetsMG,	__T1_h_rec_DiBoson,	__T1_h_rec_ZJets,	__T1_h_rec_TTBar,	__T1_h_rec_SingleTop]
	__T2_histos = [__T2_h_rec_Data,	__T2_h_rec_WJetsMG,	__T2_h_rec_DiBoson,	__T2_h_rec_ZJets,	__T2_h_rec_TTBar,	__T2_h_rec_SingleTop]
	__T3_histos = [__T3_h_rec_Data,	__T3_h_rec_WJetsMG,	__T3_h_rec_DiBoson,	__T3_h_rec_ZJets,	__T3_h_rec_TTBar,	__T3_h_rec_SingleTop]
	__T4_histos = [__T4_h_rec_Data,	__T4_h_rec_WJetsMG,	__T4_h_rec_DiBoson,	__T4_h_rec_ZJets,	__T4_h_rec_TTBar,	__T4_h_rec_SingleTop]

	[_zz,zz] = GetSF(__Z_histos,0,3,[1,2,4,5])
	[_ww,ww] = GetSF(__W_histos,0,1,[2,3,4,5])
	[_tt,tt] = GetSF(__T_histos,0,4,[1,2,3,5])
	tt1 = GetSF(__T1_histos,0,4,[1,2,3,5])
	tt2 = GetSF(__T2_histos,0,4,[1,2,3,5])
	tt3 = GetSF(__T3_histos,0,4,[1,2,3,5])
	tt4 = GetSF(__T4_histos,0,4,[1,2,3,5])

	print ' ----------- DATA DRIVEN INFORMATION ------------- '
	print ' '
	print selection
	print ' '
	print 'SF_Z: ',zz
	print ' '
	print 'SF_W: ',ww
	print ' '
	print 'SF_T:   ',tt
	print 'SF_T EU:   ',tt1
	print 'SF_T ED:   ',tt2	
	print 'SF_T MU:   ',tt3
	print 'SF_T MD:   ',tt4
	print ' '
	print ' ----------- END DRIVEN INFORMATION ------------- '

	return [_ww,_zz,_tt]




def MakeUnfoldedPlots(genvariables,recovariable, default_value, labelmods, binning,presentationbinning,recoselections,genselections,weight,optvar,FileDirectory,file_override,tau_override,tagname):

	##############################################################################
	#######     Basic setup - Get the files and trees, designate styles    #######
	##############################################################################

	JESTag = 'JetScale' in FileDirectory
	# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
	allfiles = [x.replace('\n','') for x in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines()]
	if 'SingleMuData.root' not in allfiles:
		allfiles.append('SingleMuData.root')
	for f in allfiles:
		if 'Scale' in f or 'Match' in f or 'out' in f:
			continue
		fin = f.replace('\n','')
		fin_orig = f.replace('\n','')
		if 'altunf' in tagname:
			print '-'*35+' SHERPA '+'-'*35
			if 'WJets_MG' in fin:
				fin = fin.replace('WJets_MG','WJets_Sherpa')

		if JESTag==True:

			if 'Data' not in fin :
				exec('t_'+f.replace(".root","")+" = TFile.Open(\""+NormalDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")

				if 'WJets_MG' in fin:
					exec("t_MG = TFile.Open(\""+NormalDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")	

			else:
				exec('t_'+f.replace(".root","")+" = TFile.Open(\""+FileDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")


		else:
			if 'Data' not in fin:
				exec('t_'+f.replace(".root","")+" = TFile.Open(\""+FileDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")

				if 'WJets_MG' in fin_orig:
					exec("t_MG = TFile.Open(\""+FileDirectory+"/"+fin_orig+"\")"+".Get(\""+TreeName+"\")")	

			else:
				exec('t_'+f.replace(".root","")+" = TFile.Open(\""+NormalDirectory+"/"+fin+"\")"+".Get(\""+TreeName+"\")")


	print 'Is the new modified JES being used (Data not unf Matrix?):', JESTag

	print 'Using BTagging Algorithm: TCHEM'

	##############################################################################
	#######   Define selections and weights for normal, qcd, and unfolding #######
	##############################################################################

	if 'hltidiso' in tagname:
		weight = weight.replace(idisoweight,idisosysweight)
		weight += '*1.002'

	[selection, selection_minimal] = recoselections
	[gen_selection, gen_selection_minimal] = genselections

	# QCDScale_Central = '(0)'
	qcdselection = selection.replace('IsoMu24Pass','1')
	qcdselection = qcdselection.replace('MT_muon1METR','99999')
	qcdselection = qcdselection.replace('RelIso_muon1','0.0')

	[genvariable,baregenvariable] = genvariables
	[xlabel,namelabel] = labelmods


	recomodvariable = recovariable	
	genmodvariable = genvariable

	if 'HT' in recovariable:
		# recomodvariable = '( ('+selection+')*('+recovariable+ ') + (1-'+selection+')*('+str(default_value)+') )'
		genmodvariable = '( ('+gen_selection+')*('+genvariable+ ') + (1-'+gen_selection+')*('+str(default_value)+') )'		
		baregenvariable = genmodvariable

	rivetselection = str(gen_selection).replace('_bare','')
	rivetmodvariable = str(genmodvariable.replace('_bare',''))

	# Get optimal variable binning binning
	varbinning=GetConstBinStructure(binning)
	if (optvar=="v" or optvar=="V"):
		varbinning=GetIdealBinStructure(CreateHisto('h_forrebin_WJets','temptest',t_WJets_MG,recomodvariable,[100000*len(presentationbinning),presentationbinning[0],presentationbinning[-1]],selection+weight,MCGenStyle,Label),binning)


	##############################################################################
	#######   Preparation and stylistic modifications below                #######
	##############################################################################

	tmpname = "tmp"+str(random.randint(0,1000000))+".root"
	tmpfile = TFile(tmpname,"RECREATE") # temporary root file. Named with random number so you can run several versions of this script at once if needed.
		
	# Create Canvas
	c0 = TCanvas("c1","",1200,900)
	gStyle.SetOptStat(0)

	# These are the style parameters for certain plots - [FillStyle,MarkerStyle,MarkerSize,LineWidth,Color]
	MCGenStyle=[0,20,.00001,1,2]
	MCGenSmearStyle=[0,20,.00001,1,9]

	MCRecoStyle=[0,21,.00001,1,4]
	DataRecoStyle=[0,20,1.0,1,1]
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
	#######   Get Data-Driven Scale Factors                                #######
	##############################################################################


	scalefactoron = 'BGSFOn' in 'pyplots'

	if scalefactoron == True:

		if 'Count' in recovariable or len(varbinning)<=6:
			_sfbinning = varbinning

		else:
			# _sfbinning = [6,varbinning[0], varbinning[-1]]
			_sfbinning = [varbinning[0]]+presentationbinning[1:-1]+[varbinning[-1]]
			_sfbinning = ConvertBinning(_sfbinning)


		ttbar_selection = selection.replace('(PFJet30TCHEMCountCentral<0.5)','(PFJet30TCHEMCountCentral>1.5)')
		w_selection = selection
		z_selection = selection.replace('(Pt_muon2<0.000001)','(Pt_muon2>25)')

		LabelDD=[xlabel,"Data-Driven SF"]


		__Z_h_rec_Data=CreateHisto('__Z_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,_sfbinning,z_selection+IsoMuCond,DataRecoStyle,LabelDD)
		__Z_h_rec_WJetsMG=CreateHisto('__Z_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_WJets_MG,recomodvariable,_sfbinning,z_selection+weight,MCRecoStyle,LabelDD)
		__Z_h_rec_DiBoson=CreateHisto('__Z_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,_sfbinning,z_selection+weight,DiBosonStackStyle,LabelDD)
		__Z_h_rec_ZJets=CreateHisto('__Z_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,_sfbinning,z_selection+weight,ZStackStyle,LabelDD)
		__Z_h_rec_TTBar=CreateHisto('__Z_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,_sfbinning,z_selection+weight,TTStackStyle,LabelDD)
		__Z_h_rec_SingleTop=CreateHisto('__Z_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,_sfbinning,z_selection+weight,StopStackStyle,LabelDD)

		__W_h_rec_Data=CreateHisto('__W_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,_sfbinning,w_selection+IsoMuCond,DataRecoStyle,LabelDD)
		__W_h_rec_WJetsMG=CreateHisto('__W_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_WJets_MG,recomodvariable,_sfbinning,w_selection+weight,MCRecoStyle,LabelDD)
		__W_h_rec_DiBoson=CreateHisto('__W_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,_sfbinning,w_selection+weight,DiBosonStackStyle,LabelDD)
		__W_h_rec_ZJets=CreateHisto('__W_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,_sfbinning,w_selection+weight,ZStackStyle,LabelDD)
		__W_h_rec_TTBar=CreateHisto('__W_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,_sfbinning,w_selection+weight,TTStackStyle,LabelDD)
		__W_h_rec_SingleTop=CreateHisto('__W_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,_sfbinning,w_selection+weight,StopStackStyle,LabelDD)

		__T_h_rec_Data=CreateHisto('__T_h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,_sfbinning,ttbar_selection+IsoMuCond,DataRecoStyle,LabelDD)
		__T_h_rec_WJetsMG=CreateHisto('__T_h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_WJets_MG,recomodvariable,_sfbinning,ttbar_selection+weight,MCRecoStyle,LabelDD)
		__T_h_rec_DiBoson=CreateHisto('__T_h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,_sfbinning,ttbar_selection+weight,DiBosonStackStyle,LabelDD)
		__T_h_rec_ZJets=CreateHisto('__T_h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,_sfbinning,ttbar_selection+weight,ZStackStyle,LabelDD)
		__T_h_rec_TTBar=CreateHisto('__T_h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,_sfbinning,ttbar_selection+weight,TTStackStyle,LabelDD)
		__T_h_rec_SingleTop=CreateHisto('__T_h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,_sfbinning,ttbar_selection+weight,StopStackStyle,LabelDD)

		__Z_histos = [__Z_h_rec_Data,	__Z_h_rec_WJetsMG,	__Z_h_rec_DiBoson,	__Z_h_rec_ZJets,	__Z_h_rec_TTBar,	__Z_h_rec_SingleTop]
		__W_histos = [__W_h_rec_Data,	__W_h_rec_WJetsMG,	__W_h_rec_DiBoson,	__W_h_rec_ZJets,	__W_h_rec_TTBar,	__W_h_rec_SingleTop]
		__T_histos = [__T_h_rec_Data,	__T_h_rec_WJetsMG,	__T_h_rec_DiBoson,	__T_h_rec_ZJets,	__T_h_rec_TTBar,	__T_h_rec_SingleTop]

		# [_zz,zz] = GetSF(__Z_histos,0,3,[1,2,4,5])
		# [_ww,ww] = GetSF(__W_histos,0,1,[2,3,4,5])
		# [_tt,tt] = GetSF(__T_histos,0,4,[1,2,3,5])
		# tt1 = GetSF(__T1_histos,0,4,[1,2,3,5])


		print " --------  Z REGION TABLE INFO -----------"
		_z_b = 'Bin '
		_z_d = 'Data '
		_z_z = 'Z '
		_z_tt = '$t \overline{t}$ '
		_z_w = 'W '
		_z_o = 'Other '


		_ra = range(__Z_h_rec_Data.GetNbinsX())
		if 'Count' in recovariable:
			_ra = [1,2,3,4,5,6] 
		for _nn in _ra:
			_nn += 1
			_z_b+= ' & '+str((round(__Z_h_rec_Data.GetBinCenter(_nn) ,4)))
			_z_d+= ' & '+str(int(round(__Z_h_rec_Data.GetBinContent(_nn) ,0)))
			_z_w+= ' & '+str(int(round(__Z_h_rec_WJetsMG.GetBinContent(_nn) ,0)))
			_z_z+= ' & '+str(int(round(__Z_h_rec_ZJets.GetBinContent(_nn) ,0)))
			_z_tt+= ' & '+str(int(round(__Z_h_rec_TTBar.GetBinContent(_nn) ,0)))
			_z_o+= ' & '+str(int(round(__Z_h_rec_SingleTop.GetBinContent(_nn) +__Z_h_rec_DiBoson.GetBinContent(_nn) ,0)))

		print _z_b
		print _z_d
		print _z_w
		print _z_z
		print _z_tt
		print _z_o

		print " -------- TT REGION TABLE INFO -----------"
		_t_b = 'Bin '
		_t_d = 'Data '
		_t_z = 'Z '
		_t_tt = '$t \overline{t}$ '
		_t_w = 'W '
		_t_o = 'Other '

		for _nn in _ra:
			_nn += 1
			_t_b+= ' & '+str((round(__T_h_rec_Data.GetBinCenter(_nn) ,4)))
			_t_d+= ' & '+str(int(round(__T_h_rec_Data.GetBinContent(_nn) ,0)))
			_t_w+= ' & '+str(int(round(__T_h_rec_WJetsMG.GetBinContent(_nn) ,0)))
			_t_z+= ' & '+str(int(round(__T_h_rec_ZJets.GetBinContent(_nn) ,0)))
			_t_tt+= ' & '+str(int(round(__T_h_rec_TTBar.GetBinContent(_nn) ,0)))						
			_t_o+= ' & '+str(int(round(__T_h_rec_SingleTop.GetBinContent(_nn) +__T_h_rec_DiBoson.GetBinContent(_nn) ,0)))

		print _t_b
		print _t_d
		print _t_w
		print _t_z
		print _t_tt
		print _t_o



		# Data Minus BG
		__Z_h_rec_Data.Add(__Z_h_rec_WJetsMG,-1)
		__Z_h_rec_Data.Add(__Z_h_rec_DiBoson,-1)
		__Z_h_rec_Data.Add(__Z_h_rec_TTBar,-1)
		__Z_h_rec_Data.Add(__Z_h_rec_SingleTop,-1)

		# Data Minus BG
		__W_h_rec_Data.Add(__W_h_rec_ZJets,-1)
		__W_h_rec_Data.Add(__W_h_rec_DiBoson,-1)
		__W_h_rec_Data.Add(__W_h_rec_TTBar,-1)
		__W_h_rec_Data.Add(__W_h_rec_SingleTop,-1)

		# Data Minus BG
		__T_h_rec_Data.Add(__T_h_rec_WJetsMG,-1)
		__T_h_rec_Data.Add(__T_h_rec_DiBoson,-1)
		__T_h_rec_Data.Add(__T_h_rec_ZJets,-1)
		__T_h_rec_Data.Add(__T_h_rec_SingleTop,-1)

		# Data / MC
		__Z_h_rec_Data.Divide(__Z_h_rec_ZJets)
		__W_h_rec_Data.Divide(__W_h_rec_WJetsMG)
		__T_h_rec_Data.Divide(__T_h_rec_TTBar)


		# Sum MC For Purity
		__Z_h_rec_WJetsMG.Add(__Z_h_rec_DiBoson)
		__Z_h_rec_WJetsMG.Add(__Z_h_rec_TTBar)
		__Z_h_rec_WJetsMG.Add(__Z_h_rec_SingleTop)
		__Z_h_rec_WJetsMG.Add(__Z_h_rec_ZJets)


		# Sum MC For Purity
		__T_h_rec_WJetsMG.Add(__T_h_rec_DiBoson)
		__T_h_rec_WJetsMG.Add(__T_h_rec_TTBar)
		__T_h_rec_WJetsMG.Add(__T_h_rec_SingleTop)
		__T_h_rec_WJetsMG.Add(__T_h_rec_ZJets)
			
		# Sum MC For Purity
		__W_h_rec_TTBar.Add(__W_h_rec_DiBoson)
		__W_h_rec_TTBar.Add(__W_h_rec_ZJets)
		__W_h_rec_TTBar.Add(__W_h_rec_SingleTop)
		__W_h_rec_TTBar.Add(__W_h_rec_WJetsMG)



		# Divide MC by BG for Purity	
		__Z_h_rec_ZJets.Divide(__Z_h_rec_WJetsMG)
		__T_h_rec_TTBar.Divide(__T_h_rec_WJetsMG)
		__W_h_rec_WJetsMG.Divide(__W_h_rec_TTBar)

		# Fill Style Fix
		__Z_h_rec_Data.SetFillStyle(0)
		__W_h_rec_Data.SetFillStyle(0)
		__T_h_rec_Data.SetFillStyle(0)

		__Z_h_rec_ZJets.SetFillStyle(0)
		__T_h_rec_TTBar.SetFillStyle(0)
		__W_h_rec_WJetsMG.SetFillStyle(0)

		# Color Fix
		__Z_h_rec_Data.SetMarkerStyle(22)
		__W_h_rec_Data.SetMarkerStyle(21)
		__T_h_rec_Data.SetMarkerStyle(23)	
		__Z_h_rec_Data.SetMarkerSize(2)
		__W_h_rec_Data.SetMarkerSize(2)
		__T_h_rec_Data.SetMarkerSize(2)	
		__Z_h_rec_Data.SetMarkerColor(2)
		__W_h_rec_Data.SetMarkerColor(6)
		__T_h_rec_Data.SetMarkerColor(4)
		__Z_h_rec_Data.SetFillColor(2)
		__W_h_rec_Data.SetFillColor(6)
		__T_h_rec_Data.SetFillColor(4)
		__Z_h_rec_Data.SetLineColor(2)
		__W_h_rec_Data.SetLineColor(6)
		__T_h_rec_Data.SetLineColor(4)


		__Z_h_rec_ZJets.SetLineColor(2)
		__Z_h_rec_ZJets.SetLineStyle(2)
		__Z_h_rec_ZJets.SetMarkerColor(2)
		__Z_h_rec_ZJets.SetFillColor(2)



		__T_h_rec_TTBar.SetLineStyle(3)
		__T_h_rec_TTBar.SetLineColor(4)
		__T_h_rec_TTBar.SetMarkerColor(4)
		__T_h_rec_TTBar.SetFillColor(4)


		__W_h_rec_WJetsMG.SetLineStyle(6)
		__W_h_rec_WJetsMG.SetLineColor(6)
		__W_h_rec_WJetsMG.SetMarkerColor(6)
		__W_h_rec_WJetsMG.SetFillColor(6)


		__Z_h_rec_Data.SetMaximum(2.0)
		__Z_h_rec_Data.SetMinimum(0.0)

		__Z_h_rec_Data.Draw("EP")
		__Z_h_rec_ZJets.Draw("EHISTSAME")

		# __W_h_rec_Data.Draw("EPSAME")
		# __W_h_rec_WJetsMG.Draw("EHISTSAME")

		__T_h_rec_Data.Draw("EPSAME")
		__T_h_rec_TTBar.Draw("EHISTSAME")

		leg = TLegend(0.19,0.76,0.35,0.93,"","brNDC")
		leg.SetTextFont(42)
		leg.SetFillColor(0)
		leg.SetBorderSize(0)
		leg.SetTextSize(.03)
		leg.AddEntry(__Z_h_rec_Data,"Z+Jets SF")
		leg.AddEntry(__T_h_rec_Data,"TTBar SF")
		# leg.AddEntry(__W_h_rec_Data,"W+Jets SF")
		leg.Draw()

		leg2 = TLegend(0.36,0.76,0.52,0.93,"","brNDC")
		leg2.SetTextFont(42)
		leg2.SetFillColor(0)
		leg2.SetBorderSize(0)
		leg2.SetTextSize(.03)
		leg2.AddEntry(__Z_h_rec_ZJets,"Z+Jets Pur")
		leg2.AddEntry(__T_h_rec_TTBar,"TTBar Pur")
		# leg2.AddEntry(__W_h_rec_WJetsMG,"W+Jets Pur")
		leg2.Draw()


		_zres = '*('
		_zres_unc = '*('


		print " -------- SF VALUES TABLE INFO -----------"
		_s_b = ' Bin '
		_s_z = ' Z SF '
		_s_t = ' $t \overline{t} $ '


		for xx in range(__Z_h_rec_Data.GetNbinsX()):
			_n = xx+1
			_halfwidth = 0.5*__Z_h_rec_Data.GetBinWidth(_n)
			_center = __Z_h_rec_Data.GetBinCenter(_n)
			_lhs = _center - _halfwidth
			_rhs = _center + _halfwidth
			_cont = __Z_h_rec_Data.GetBinContent(_n)
			_err = __Z_h_rec_Data.GetBinError(_n)
			_cut = '('+recomodvariable+'>='+str(round(_lhs,3))+')*('+recomodvariable+'<'+str(round(_rhs,3))+')'
			_vsf = '*'+str(round(_cont,3))
			_ver = '*'+str(round(_err,3))
			_zres += _cut+_vsf	
			_zres_unc += _cut+_ver

			if 'Count' not in recovariable or (_center > 0.7 and _center < 6.8):
				_s_b += str(round(_center,4))
				_s_z += ' & '+ str(round(_cont,3)) + '$ \\pm $ '+str(round(_err,3))

			if xx != range(__Z_h_rec_Data.GetNbinsX())[-1]:
				_zres += ' + '
				_zres_unc += ' + '		
		_zres += ')'
		_zres_unc += ')'


		_tres = '*('
		_tres_unc = '*('

		for xx in range(__T_h_rec_Data.GetNbinsX()):
			_n = xx+1
			_halfwidth = 0.5*__T_h_rec_Data.GetBinWidth(_n)
			_center = __T_h_rec_Data.GetBinCenter(_n)
			_lhs = _center - _halfwidth
			_rhs = _center + _halfwidth
			_cont = __T_h_rec_Data.GetBinContent(_n)
			_err = __T_h_rec_Data.GetBinError(_n)
			_cut = '('+recomodvariable+'>='+str(round(_lhs,3))+')*('+recomodvariable+'<'+str(round(_rhs,3))+')'
			_vsf = '*'+str(round(_cont,3))
			_ver = '*'+str(round(_err,3))
			_tres += _cut+_vsf	
			_tres_unc += _cut+_ver

			if 'Count' not in recovariable or (_center > 0.7 and _center < 6.8):

				_s_t += ' & '+ str(round(_cont,3)) + '$ \\pm $ '+str(round(_err,3))

			if xx != range(__T_h_rec_Data.GetNbinsX())[-1]:
				_tres += ' + '
				_tres_unc += ' + '		
		_tres += ')'
		_tres_unc += ')'

		print _s_b
		print _s_z
		print _s_t

		print " -------- CONTORL REGION TABLES COMPLETE -----------"


		sfunity=TLine(__T_h_rec_Data.GetXaxis().GetXmin(), 1.0 , __T_h_rec_Data.GetXaxis().GetXmax(),1.0)
		sfunity.Draw("SAME")
		c0.Print('pyplots/'+recovariable+'_'+tagname+namelabel+'_sfhisto.png')
		c0.Print('pyplots/'+recovariable+'_'+tagname+namelabel+'_sfhisto.pdf')

		# sys.exit()

	fW = '*(1.0)'
	fZ = '*(1.0)'
	fT = '*(1.0)'
	fsT = '*(1.0)'
	fV = '*(1.0)'



	if scalefactoron == True:
		fZ = _zres
		fT = _tres

	print 'Z SF:',fZ
	print 'TTBar SF:',fT

	print 'Scale factor derivation complete!'


	if 'bgnorm_plus' in tagname:
		print 'REASSIGNING BACKGROUD NORMALIZATION - POSITIVE MODIFICATIONS'
		fZ += '*(1.04331)'
		fT += '*(1.06061)' 
		fsT += '*(1.06)'
		fV += '*(1.04)'



	if 'bgnorm_minus' in tagname:
		print 'REASSIGNING BACKGROUD NORMALIZATION - NEGATIVE MODIFICATIONS'
		fZ += '*(0.95669)'
		fT += '*(0.93939)' 
		fsT += '*(0.94)'
		fV += '*(0.96)'


	# sys.exit()





	##############################################################################
	#######     Top Right - Background Subtracted Distributions            #######
	##############################################################################


	tmpname = "tmp"+str(random.randint(0,1000000))+".root"
	tmpfile = TFile(tmpname,"RECREATE") # temporary root file. Named with random number so you can run several versions of this script at once if needed.
		
	# Create Canvas
	c1 = TCanvas("c1","",1200,900)
	c1.Divide(2,2)
	gStyle.SetOptStat(0)


	c1.cd(2)

	# The selection for the reco variable, constrained to the range the final distribution will be shown.
	# selection+='*('+recovariable+'<'+str(presentationbinning[-1])+')*('+recovariable+'>'+str(presentationbinning[0])+')'
	# The selection for the gen variable. Larger range for the underflow/overflow. '(Pt_genmuon1>1.0)' also demands that a gen-muon is present. 
	# The trees should otherwise be skimmed for a reco muon to be present.

	# print rivetselection
	for x in RivetGenBranchMap:
		if x[0] in rivetselection:
			rivetselection = rivetselection.replace(x[0],x[1])
		if x[0] in rivetmodvariable:
			rivetmodvariable = rivetmodvariable.replace(x[0],x[1])

	
	nrivet = (RIVETMadGraph.split('_')[-1]).replace('.root','')+'.0'
	rivetselection = 'evweight*(31314*4955.0/'+nrivet+')*'+rivetselection
	t_rivet = TFile.Open(RIVETMadGraph,'READ').Get('RivetTree')


	nvbin = len(varbinning)
	vbinmin = 1
	vbinmax = nvbin-1

	npbin = len(presentationbinning)
	pbinmin = 1
	pbinmax = npbin-1

	gtag = 'MadGraph'
	if 'altunf' in tagname:
		gtag = 'Sherpa'



	selection_norm = selection+"*(MT_muon1METR>50.0)"
	gen_selection_norm = gen_selection+"*(MT_muon1METR>50.0)"

	h_normgen_WJets=CreateHisto('h_normgen_WJets','W+Jets MG [Truth]',t_WJets_MG,baregenvariable,varbinning,gen_selection_norm+'*weight_gen*4955',MCGenStyle,Label)
	h_normrec_WJets=CreateHisto('h_normrec_WJets','W+Jets '+gtag+' [Reco]',t_WJets_MG,recomodvariable,varbinning,selection_norm+weight+fW,MCRecoStyle,Label)
	h_normrec_WJetsMG=CreateHisto('h_normrec_WJetsMG','W+Jets MadGraph [Reco]',t_MG,recomodvariable,varbinning,selection_norm+weight+fW,MCRecoStyle,Label)

	# Data
	h_normrec_Data=CreateHisto('h_normrec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,varbinning,selection_norm+IsoMuCond,DataRecoStyle,Label)
	# Other Backgrounds
	h_normrec_DiBoson=CreateHisto('h_normrec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,varbinning,selection_norm+weight+fV,DiBosonStackStyle,Label)
	h_normrec_ZJets=CreateHisto('h_normrec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,varbinning,selection_norm+weight+fZ,ZStackStyle,Label)
	h_normrec_TTBar=CreateHisto('h_normrec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,varbinning,selection_norm+weight+fT,TTStackStyle,Label)
	h_normrec_SingleTop=CreateHisto('h_normrec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,varbinning,selection_norm+weight+fsT,StopStackStyle,Label)

	print 'D:',h_normrec_Data.Integral()
	print 'Z:',h_normrec_ZJets.Integral()
	print 'T:',h_normrec_TTBar.Integral()
	print 'V:',h_normrec_DiBoson.Integral()
	print 'S:',h_normrec_SingleTop.Integral()
	print 'W:',h_normrec_WJets.Integral() 


	_wsf   = 	( h_normrec_Data.Integral() - h_normrec_ZJets.Integral() - h_normrec_TTBar.Integral() - h_normrec_DiBoson.Integral() - h_normrec_SingleTop.Integral() ) / (	h_normrec_WJets.Integral() )
	_wsfMG = 	( h_normrec_Data.Integral() - h_normrec_ZJets.Integral() - h_normrec_TTBar.Integral() - h_normrec_DiBoson.Integral() - h_normrec_SingleTop.Integral() ) / (	h_normrec_WJetsMG.Integral() )

	# print "USING W SCALE FACTOR:", _wsf
	# h_normrec_WJets.Scale(_wsf)
	# h_normrec_WJetsMG.Scale(_wsf)

	wsfoff = 'WSFOFF' in 'pyplots'

	if wsfoff == True:
		_wsf   = 1.0
		_wsfMG = 1.0


	print "USING W SCALE FACTOR:", _wsf


	fW = '*('+str(round(_wsf,4))+')'
	fWMG = '*('+str(round(_wsfMG,4))+')'



	# _wsf = 1.0
	# print "USING W SCALE FACTOR:", _wsf




	# W + Jets Contributions (Normalized for display)
	# h_gen_WJets=CreateHisto('h_gen_WJets_aod','W+Jets '+gtag+' [Truth]',t_WJets_MG,baregenvariable,varbinning,gen_selection+'*weight_gen*4955',MCGenStyle,Label)
	h_gen_WJets=CreateHisto('h_gen_WJets','W+Jets MG [Truth]',t_WJets_MG,baregenvariable,varbinning,gen_selection+'*weight_gen*4955'+fW,MCGenStyle,Label)

	print '-'*50+'\n'+rivetmodvariable+'\n'+rivetselection+'\n'+'-'*50+'\n'	
	# h_gen_WJets=CreateHisto('h_gen_WJets','W+Jets [Truth Rivet]',t_rivet,rivetmodvariable,varbinning,rivetselection,MCGenStyle,Label)
	# print '-'*50+'\n'+recomodvariable+'\n'+selection+weight+'\n'+'-'*50+'\n'	
	h_rec_WJets=CreateHisto('h_rec_WJets','W+Jets '+gtag+' [Reco]',t_WJets_MG,recomodvariable,varbinning,selection+weight+fW,MCRecoStyle,Label)
	h_rec_WJetsMG=CreateHisto('h_rec_WJetsMG','W+Jets MadGraph [Reco]',t_MG,recomodvariable,varbinning,selection+weight+fWMG,MCRecoStyle,Label)

	# Data
	h_rec_Data=CreateHisto('h_rec_Data','Data, 5/fb [Reco]',t_SingleMuData,recomodvariable,varbinning,selection+IsoMuCond,DataRecoStyle,Label)
	# Other Backgrounds
	h_rec_DiBoson=CreateHisto('h_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,varbinning,selection+weight+fV,DiBosonStackStyle,Label)
	h_rec_ZJets=CreateHisto('h_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,varbinning,selection+weight+fZ,ZStackStyle,Label)
	h_rec_TTBar=CreateHisto('h_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,varbinning,selection+weight+fT,TTStackStyle,Label)
	h_rec_SingleTop=CreateHisto('h_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,varbinning,selection+weight+fsT,StopStackStyle,Label)

	print ' W: ',h_rec_WJets.Integral()
	print ' Z: ',h_rec_ZJets.Integral()
	print ' TT:',h_rec_TTBar.Integral()
	print ' VV:',h_rec_DiBoson.Integral()
	print ' t: ',h_rec_SingleTop.Integral()
	print ' D: ',h_rec_Data.Integral()
	# sys.exit()

	# GETTING QCD 
	selection_nomt = selection.replace('MT_muon1METR','99999')
	nonisotrees = [t_TTBar,t_WJets_MG,t_SingleTop,t_DiBoson,t_ZJets_MG]
	nonisotreenames = ['t_TTBarNonIso','t_WJets_MGNonIso','t_SingleTopNonIso','t_DiBosonNonIso','t_ZJets_MGNonIso']
	treesf = [fT,fW,fsT,fV,fZ]
	

	regtrees = [t_TTBar,t_WJets_MG,t_SingleTop,t_DiBoson,t_ZJets_MG]
	regtreenames = ['t_TTBar','t_WJets_MG','t_SingleTop','t_DiBoson','t_ZJets_MG']
	__h_noniso_qcd=CreateHisto('__h_noniso_qcd','QCD',t_SingleMuData,recomodvariable,varbinning,qcdselection+'*(RelIso_muon1>0.15)*(Mu24Pass>0)*Mu24PassPrescale*(MT_muon1METR<50)',QCDStackStyle,Label)
	__h_iso_reg=CreateHisto('__h_iso_reg','__h_iso_reg',t_SingleMuData,recovariable,varbinning,selection_nomt+'*(MT_muon1METR<50)*(IsoMu24Pass>0.5)',WStackStyle,Label)


	tn = 0
	for tt in nonisotrees:
		__sf = treesf[tn]
		print nonisotreenames[tn], __sf
		tmpname = '__h_noniso_mc'+str(random.randint(0,1000000))
		__h_noniso_qcd.Add(CreateHisto(tmpname,tmpname,tt,recomodvariable,varbinning,qcdselection+weight+'*(RelIso_muon1>0.15)*(MT_muon1METR<50)*(-1)'+__sf,QCDStackStyle,Label))
		tmpname = '__h_iso_mc'+str(random.randint(0,1000000))
		__h_iso_reg.Add(CreateHisto(tmpname,tmpname,regtrees[tn],recovariable,varbinning,qcdselection+'*(RelIso_muon1<0.15)'+weight+'*(-1)*(IsoMu24Pass>0.5)*(MT_muon1METR<50)'+__sf,WStackStyle,Label))
		tn += 1

	if __h_noniso_qcd.GetEntries()>0:
		QCDSF = __h_iso_reg.Integral()/__h_noniso_qcd.Integral()
	else:
		QCDSF = 0.02

	h_rec_QCDMu=CreateHisto('h_rec_QCDMu','QCD',t_SingleMuData,recomodvariable,varbinning,qcdselection+'*(MT_muon1METR>50)*(RelIso_muon1>0.15)*(Mu24Pass>0)*Mu24PassPrescale*('+str(QCDSF)+')',QCDStackStyle,Label)
	tn = 0
	for tt in nonisotrees:
		__sf = treesf[tn]

		tmpname = 'h_noniso_mc'+str(random.randint(0,1000000))
		h_rec_QCDMu.Add(CreateHisto(tmpname,tmpname,tt,recomodvariable,varbinning,qcdselection+weight+'*(MT_muon1METR>50)*(RelIso_muon1>0.15)*(-1.0)*('+str(QCDSF)+')'+__sf,QCDStackStyle,Label))
		tn += 1


	if 'Pt_muon2>25' in selection:
		QCDSF = 0.0
		print 'Z SELECTION -- SETTING QCD SCALE TO ZERO'





	# Pseudo-Data for Unfolding (ALWAYS FROM MADGRAPH)
	h_rec_Data_pseudo=PseudoDataHisto(h_rec_WJetsMG,'h_rec_PseudoData',varbinning)

	## Draw W+Jets Gen and Reco
	h_gen_WJets.Draw("HIST")	
	h_rec_WJets.Draw("HISTSAME")

	# Create Legend
	FixDrawLegend(c1.cd(2).BuildLegend( 0.5,  0.6,  0.9,  0.88,'' ))
	
	##############################################################################
	#######      Independent Plot - Normal Stacked Distributions                #######
	##############################################################################

	# Canvas Setup
	c2 = TCanvas("c2","",700,1000)
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
	cpad1.SetLogy(1)
	cpad1.cd()


	
	### Make the plots without variable bins!
	hs_rec_WJets=CreateHisto('hs_rec_WJets','W+Jets',t_WJets_MG,recovariable,presentationbinning,selection+weight+fW,WStackStyle,Label)
	hs_rec_Data=CreateHisto('hs_rec_Data','Data, 5/fb',t_SingleMuData,recovariable,presentationbinning,selection+IsoMuCond,DataRecoStyle,Label)
	hs_rec_DiBoson=CreateHisto('hs_rec_DiBoson','DiBoson',t_DiBoson,recovariable,presentationbinning,selection+weight+fV,DiBosonStackStyle,Label)
	hs_rec_ZJets=CreateHisto('hs_rec_ZJets','Z+Jets',t_ZJets_MG,recovariable,presentationbinning,selection+weight+fZ,ZStackStyle,Label)
	hs_rec_TTBar=CreateHisto('hs_rec_TTBar','t#bar{t}',t_TTBar,recovariable,presentationbinning,selection+weight+fT,TTStackStyle,Label)
	hs_rec_SingleTop=CreateHisto('hs_rec_SingleTop','SingleTop',t_SingleTop,recovariable,presentationbinning,selection+weight+fsT,StopStackStyle,Label)

	hs_rec_QCDMu=CreateHisto('hs_rec_QCDMu','QCD',t_SingleMuData,recomodvariable,presentationbinning,qcdselection+'*(MT_muon1METR>50.0)*(RelIso_muon1>0.15)*(Mu24Pass>0)*Mu24PassPrescale*('+str(QCDSF)+')',QCDStackStyle,Label)
	
	print '-------- QCD TABLE ',recovariable,' ---------'
	print 'Inv Iso Data: ',hs_rec_QCDMu.Integral()
	_presub = hs_rec_QCDMu.Integral()

	tn = 0
	for tt in nonisotrees:
		__sf = treesf[tn]
		tmpname = 'hs_noniso_mc'+str(random.randint(0,1000000))
		hs_rec_QCDMu.Add(CreateHisto(tmpname,tmpname,tt,recomodvariable,presentationbinning,qcdselection+weight+'*(MT_muon1METR>50.0)*(RelIso_muon1>0.15)*(-1.0)*('+str(QCDSF)+')'+__sf,QCDStackStyle,Label))
		tn += 1

	_postsub = hs_rec_QCDMu.Integral()


	print 'Inv Iso Data After Sub: ',hs_rec_QCDMu.Integral()
	print 'Subtracted backround: ', _presub - _postsub

	# print 'Perc Subtracted Background: ',(_presub - _postsub)/_presub

	print ' -------------------------------------------------'
	# Search for a decent y axis minimum and maximum
	qcdmin = hs_rec_QCDMu.GetMinimum()
	stopmin = hs_rec_SingleTop.GetMinimum()
	plotmin = qcdmin
	if qcdmin < 0.001:
		plotmin =stopmin
	plotmin = 0.5*plotmin
	if plotmin < 0.1:
		plotmin = 0.1
	plotmax = 100*hs_rec_Data.GetMaximum()

	# Declare the MC Stack
	MCStack = THStack ("MCStack","")
	MCStack.SetMinimum(plotmin)
	MCStack.SetMaximum(plotmax)




	print " -------- SIGNAL REGION TABLE INFO -----------"
	_w_b = 'Bin '
	_w_d = 'Data '
	_w_z = 'Z '
	_w_tt = '$t \overline{t}$ '
	_w_w = 'W '
	_w_q = 'QCD '
	_w_o = 'Other '

	for _nn in range(hs_rec_Data.GetNbinsX()):
		_nn += 1
		_center = hs_rec_Data.GetBinCenter(_nn)
		if 'Count' not in recovariable or (_center > 0.7 and _center < 6.8):

			_w_b+= ' & '+str(round(hs_rec_Data.GetBinCenter(_nn) ,3))
			_w_d+= ' & '+str(int(round(hs_rec_Data.GetBinContent(_nn) ,0)))
			_w_w+= ' & '+str(int(round(hs_rec_WJets.GetBinContent(_nn) ,0)))
			_w_z+= ' & '+str(int(round(hs_rec_ZJets.GetBinContent(_nn) ,0)))
			_w_tt+= ' & '+str(int(round(hs_rec_TTBar.GetBinContent(_nn) ,0)))
			_w_o+= ' & '+str(int(round(hs_rec_SingleTop.GetBinContent(_nn) +hs_rec_DiBoson.GetBinContent(_nn) ,0)))
			_w_q+= ' & '+str(int(round(hs_rec_QCDMu.GetBinContent(_nn) ,0)))


	print _w_b
	print _w_d
	print _w_w
	print _w_z
	print _w_tt
	print _w_o
	print _w_q

	print " -------- SIGNAL REGION TABLE COMPLETE -----------"





	# List of MC Histos
	SM=[hs_rec_QCDMu,hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar,hs_rec_WJets]

	hlog = 'pyplots/'+recovariable+'_'+tagname+namelabel+'_simplehisto.hlog'
	_hlog = open(hlog,'w')
	print '\nBin','W','TTbar'

	for _nn in range(hs_rec_WJets.GetNbinsX()+1):
		nn = _nn+1
		logline = ''
		totsm = 0.0
		totsmerr = 0.0

		bincent = hs_rec_WJets.GetBinCenter(nn)
		binlhs = bincent - 0.5*hs_rec_WJets.GetBinWidth(nn)
		binrhs = bincent + 0.5*hs_rec_WJets.GetBinWidth(nn)
		logline += str(binlhs)+','+str(binrhs)+';'
		
		for ss in SM:
			totsm += ss.GetBinContent(nn)
			totsmerr += (ss.GetBinError(nn))**2
			logline += str(ss.GetBinContent(nn))+ ','+str(ss.GetBinError(nn))+';'
		totsmerr = math.sqrt(totsmerr)
		print hs_rec_WJets.GetBinCenter(nn),hs_rec_WJets.GetBinContent(nn), hs_rec_TTBar.GetBinContent(nn), totsm
		logline +=str(totsm)+','+str(totsmerr)+';' 
		logline +=str(hs_rec_Data.GetBinContent(nn))+'\n'
		_hlog.write(logline)
	_hlog.close()


	# sys.exit()
	# Set attributes
	for x in SM + [hs_rec_Data]:
		x.GetYaxis().SetTitleOffset(0.9)
		x.SetMaximum(plotmax)

	# Build stack
	for x in SM:
		MCStack.Add(x)
	
	# Draw the stack
	MCStack.Draw()
	MCStack.SetMinimum(plotmin)
	MCStack.SetMaximum(plotmax)
	MCStack.GetYaxis().SetTitleOffset(0.9)
	MCStack.Draw("HIST")
	cpad1.SetLogy()
	MCStack.SetMinimum(plotmin)
	MCStack.SetMaximum(plotmax)
	cpad1.Update()
	MCStack=BeautifyStack(MCStack,Label)

	# Draw the data.
	hs_rec_Data.Draw("EPSAME")
	
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
	cpad2.Draw()

	hs_rec_total=CreateHisto('hs_rec_total','total',t_WJets_MG,recovariable,presentationbinning,selection+weight+fW,WStackStyle,Label)
	hs_rec_total.Sumw2()
	for s in [hs_rec_QCDMu,hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar]:
		hs_rec_total.Add(s)

	hs_rec_ratio=CreateHisto('hs_rec_ratio','Data Ratio',t_SingleMuData,recovariable,presentationbinning,selection+IsoMuCond,DataRecoStyle,Label)
	hs_rec_ratio.Sumw2()

	hs_rec_ratio.Divide(hs_rec_total)


	hs_rec_pur_num=CreateHisto('hs_rec_pur_num','W Purity',t_SingleMuData,recovariable,presentationbinning,"(0)",WStackStyle,Label)
	hs_rec_pur_den=CreateHisto('hs_rec_pur_den','W Purity Den',t_SingleMuData,recovariable,presentationbinning,"(0)",WStackStyle,Label)
	hs_rec_pur_num.Sumw2()
	hs_rec_pur_den.Sumw2()



	hs_rec_pur_num.Add(hs_rec_WJets)
	hs_rec_pur_den.Add(hs_rec_WJets)
	for s in [hs_rec_QCDMu,hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar]:
		hs_rec_pur_den.Add(s)

	hs_rec_pur_num.Divide(hs_rec_pur_den)



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
	hs_rec_ratio.SetMaximum(1.5)
	hs_rec_ratio.SetMinimum(0.5)


	hs_rec_ratio.GetXaxis().SetTitle(Label[0])
	hs_rec_ratio.GetYaxis().SetTitle("Data / MC")
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

	hs_rec_pur_num.GetXaxis().SetTitle(Label[0])
	hs_rec_pur_num.GetXaxis().SetTitleOffset(.73);

	hs_rec_pur_num.GetYaxis().SetTitleFont(42);
	hs_rec_pur_num.GetXaxis().SetTitleSize(.12);
	hs_rec_pur_num.GetYaxis().SetTitleSize(.12);
	hs_rec_pur_num.GetXaxis().CenterTitle(0);
	hs_rec_pur_num.GetYaxis().CenterTitle(1);
	hs_rec_pur_num.GetXaxis().SetTitleOffset(0.88);
	hs_rec_pur_num.GetYaxis().SetTitleOffset(0.45);
	hs_rec_pur_num.GetYaxis().SetLabelSize(.1);
	hs_rec_pur_num.GetXaxis().SetLabelSize(.1);


	hs_rec_pur_num.SetFillStyle(0)
	hs_rec_pur_num.SetLineStyle(1)
	hs_rec_ratio.Draw("EP")
	# hs_rec_pur_num.GetYaxis().SetTitle("W Purity")

	# hs_rec_pur_num.Draw("EHIST")

	
	unity.Draw("SAME")



	c2.Print('pyplots/'+recovariable+'_'+tagname+namelabel+'_simplehisto.png')
	c2.Print('pyplots/'+recovariable+'_'+tagname+namelabel+'_simplehisto.pdf')

	if ('--quickplots' in sys.argv):
		return [0,0,0]

	# sys.exit()


	##############################################################################
	#######      Top Left Plot - Normal Stacked Distributions                #######
	##############################################################################
	c1.cd(1)

	mcdatascalepres = (1.0*(hs_rec_Data.Integral(pbinmin,pbinmax)))/(sum([k.Integral(pbinmin,pbinmax) for k in SM]))

	# Draw the stack
	MCStack.Draw("HIST")
	c1.cd(1).SetLogy()

	# Draw the data.
	hs_rec_Data.Draw("EPSAME")

	# Create Legend
	FixDrawLegend(c1.cd(1).BuildLegend(0.7,  0.6,  0.92,  0.88,''))
	gPad.RedrawAxis()


	##############################################################################
	#######      Bottom Left - Gen Versus Reco Response Matrix             #######
	##############################################################################	
	c1.cd(3)

	# unfgen_selection = gen_selection
	# unfgenmodvariable = genmodvariable

	# if 'jet' in genmodvariable and 'HT' not in genmodvariable:
	# 	for nn in [1,2,3,4,5]:
	# 		unfgen_selection = unfgen_selection.replace('jet'+str(nn),'jet'+str(nn)+'_bare')
	# 	unfgenmodvariable = unfgenmodvariable+'_bare'

	# thismingenselection = ''
	# for ll in mingenselection:
	# 	thismingenselection += ll

	# for nn in [1,2,3,4,5]:
	# 	if 'jet'+str(nn) in gen_selection: 
	# 		thismingenselection += '*(Pt_genjet'+str(nn)+'>0.1)'

	print 'Unfolding ',recomodvariable,namelabel,'using',gtag,' with selections:'
	print 'Gen Selection (for xini):', gen_selection+'*(weight_gen*4955)'
	print 'RecoSelection (for Adet/reco):',selection+'*'+gen_selection_minimal+'*(weight_gen*4955)'
	print 'Gen Variable: ',baregenvariable
	print 'Adet variables: ',recomodvariable, genvariable
	print '-'*50


	# W + Jets Contributions (Rivet and GEN)
	# h_gen_WJets_flat=CreateHisto('h_gen_WJets_flat','W+Jets [Truth Rivet]',t_rivet,rivetmodvariable,varbinning,rivetselection,MCGenStyle,Label)
	# h_gen_WJets_flat_bakMG=CreateHisto('h_gen_WJets_flat_bakMG','W+Jets MadGraph [Truth]',t_MG,unfgenmodvariable,varbinning,gen_selection+'*(weight_gen*4955)',MCGenStyle,Label)
	h_gen_WJets_flatRIVET=CreateHisto('h_gen_WJets_flatRIVET','W+Jets [Truth Rivet]',t_rivet,rivetmodvariable,varbinning,rivetselection,MCGenStyle,Label)
	# h_gen_WJets_flat=CreateHisto('h_gen_WJets_flat','W+Jets MadGraph [Truth]',t_MG,unfgenmodvariable,varbinning,gen_selection+'*'+gen_selection_minimal+'*(weight_gen*4955)',MCGenStyle,Label)
	# h_gen_WJets_flat=CreateHisto('h_gen_WJets_flat','W+Jets MadGraph [Truth]',t_MG,baregenvariable,varbinning,gen_selection+'*(weight_gen*4955)',MCGenStyle,Label)
	h_gen_WJets_flat=CreateHisto('h_gen_WJets_flat','W+Jets MadGraph [Truth]',t_WJets_MG,baregenvariable,varbinning,gen_selection+'*(weight_pu_central*4955)'+fW,MCGenStyle,Label)


	# Reco histograms (MadGraph and Other) 
	# h_rec_WJets_flat=CreateHisto('h_rec_WJets_flat','W+Jets '+gtag+' [Reco]',t_WJets_MG,recomodvariable,varbinning,selection+'*'+gen_selection_minimal+'*(weight_gen*4955)', MCRecoStyle,Label)
	# h_rec_WJets_flatMG=CreateHisto('h_rec_WJets_flatMG','W+Jets '+gtag+' MG [Reco]',t_MG,recomodvariable,varbinning,selection+'*'+gen_selection_minimal+'*(weight_gen*4955)', MCRecoStyle,Label)
	h_rec_WJets_flat=CreateHisto('h_rec_WJets_flat','W+Jets '+gtag+' [Reco]',t_WJets_MG,recomodvariable,varbinning,selection+'*(weight_pu_central*4955)'+fW, MCRecoStyle,Label)
	# h_rec_WJets_flatMG=CreateHisto('h_rec_WJets_flatMG','W+Jets '+gtag+' MG [Reco]',t_MG,recomodvariable,varbinning,selection+'*(weight_gen*4955)', MCRecoStyle,Label)
	h_rec_WJets_flatMG=CreateHisto('h_rec_WJets_flatMG','W+Jets '+gtag+' MG [Reco]',t_MG,recomodvariable,varbinning,selection+'*(weight_pu_central*4955)'+fWMG, MCRecoStyle,Label)


	# Reco histogram without gen minimal selection for normalization
	# h_rec_WJets_flat_nogen=CreateHisto('h_rec_WJets_flat_nogen','W+Jets '+gtag+' [Reco]',t_WJets_MG,recomodvariable,varbinning,selection+'*'+gen_selection_minimal+'*(weight_gen*4955)', MCRecoStyle,Label)
	# genscale = h_rec_WJets_flat_nogen.Integral()/h_rec_WJets_flat.Integral()

	# h_rec_WJets_flatMG_nogen=CreateHisto('h_rec_WJets_flatMG_nogen','W+Jets '+gtag+' MG [Reco]',t_MG,recomodvariable,varbinning,selection+'*'+gen_selection_minimal+'*(weight_gen*4955)', MCRecoStyle,Label)
	# genscaleMG = h_rec_WJets_flatMG_nogen.Integral()/h_rec_WJets_flatMG.Integral()

	# Response Matrix 
	h_response_WJets=Create2DHisto('h_response_WJets','ResponseMatrix',t_WJets_MG,genmodvariable,recomodvariable,varbinning,selection+'*'+gen_selection_minimal+'*(weight_pu_central*4955)'+fW,[xlabel+" Reco",xlabel+" Truth"])

	# Rescaling of Adet and bini for gen cuts:
	# h_rec_WJets_flat.Scale(genscale)
	# h_response_WJets.Scale(genscale)
	# h_rec_WJets_flatMG.Scale(genscaleMG)


	# mgscale = h_rec_WJets_flatMG_nogen.Integral()/h_rec_WJets_flat_nogen.Integral()
	mgscale = h_rec_WJets_flatMG.Integral()/h_rec_WJets_flat.Integral()

	# if 'altunf' in tagname:
	# 	h_rec_WJets_flat.Scale(mgscale)
	# 	h_response_WJets.Scale(mgscale)


	h_response_WJets.Draw("COLZ") # Draw it with color scheme
	l_bottom=TLine(binning[1], presentationbinning[0] ,binning[2],presentationbinning[0])
	l_top=TLine(binning[1], presentationbinning[-1] ,binning[2],presentationbinning[-1])
	l_left=TLine(presentationbinning[0], binning[1] ,presentationbinning[0],binning[2])
	l_right=TLine(presentationbinning[-1], binning[1] ,presentationbinning[-1],binning[2])
	bounds = [l_bottom,l_top,l_right,l_left]
	
	for x in bounds:
		x.SetLineStyle(2)
		x.Draw("SAME")
	# sys.exit()

	print 'Xini:',h_gen_WJets_flat.Integral()
	print 'Bini:',h_rec_WJets_flat.Integral()
	print 'Adet:',h_response_WJets.Integral()
	print 'Pseu:',h_rec_Data_pseudo.Integral()


	##############################################################################
	#######      Top Right Addition  - UnFolded Distribution               #######
	##############################################################################	
	c1.cd(2)
	# Subtract other backgrounds from Data using the BackgroundSubtractedHistogram function.
	h_rec_Data2= h_rec_Data.Clone()
	h_rec_Data2 = BackgroundSubtractedHistogram(h_rec_Data2,[ h_rec_DiBoson, h_rec_ZJets,h_rec_TTBar,h_rec_SingleTop,h_rec_QCDMu])
	h_rec_Data2 = BeautifyHisto(h_rec_Data2,DataCompStyle,Label,"Data, 5/fb [Reco]")

	print 'Data:', h_rec_Data2.Integral()

	# These are the paramters for the unfolding [reco, gen, response]
	Params = [ h_rec_WJets_flat, h_gen_WJets_flat, h_response_WJets]

	# Tau is calculated only for the real unfolding. Systematics use that tau. This allows an overridee of the tau value as an argument.
	if tau_override>0:
		tau=tau_override
	else:
		#tau=2  # For quick tests only!
		tau = FindOptimalTauWithDIVals(Params,h_rec_Data2,varbinning) # Get the optimal tau value.

	# Perform the unfolding. Returns unfolded data histo, some unfolding parameters not currently used
	[h_unf_Data,h_dd,h_sv,optimal_tau,optimal_i] = GetSmartSVD(h_rec_Data2,Params, varbinning,tau)

	# Samme as above, but using pseudo-data from the WJets MC - this is the closure test! Always using MadGraph!
	[h_unf_Data_pseudo,h_dd,h_sv_pseudo,optimal_tau_pseudo,optimal_i_pseudo] = GetSmartSVD(h_rec_Data_pseudo,Params, varbinning,tau)

	print 'Unfolded Data', h_unf_Data.Integral()
	print 'Unfolded PseudoData', h_unf_Data_pseudo.Integral()

	# How much would you have to scale the unfolded data to meet the reco data? Should be ~1.
	UnfScale=(h_rec_Data2.Integral(vbinmin,vbinmax)/h_unf_Data.Integral(vbinmin,vbinmax))
	UnfScale_pseudo=(h_rec_Data_pseudo.Integral(vbinmin,vbinmax)/h_unf_Data_pseudo.Integral(vbinmin,vbinmax))

	# Creates plots, with extra label giving the optimal tau and unfolding scale above.
	h_unf_Data = BeautifyHisto(h_unf_Data,DataUnfoldedStyle,Label,"Data, 5/fb [Unfolded, #tau = "+str(optimal_tau)+",R="+str(round(UnfScale,2))+"]")
	h_unf_Data_pseudo = BeautifyHisto(h_unf_Data_pseudo,DataUnfoldedStyle_pseudo,Label,"WJets Closure [Unfolded, #tau = "+str(optimal_tau)+",R="+str(round(UnfScale_pseudo,2))+"]")

	# Using the unfolded data and reeco data, get a rescaling string to convert between the two types of binning.
	[DataRescalingString,DataErrorString] = GetRescaling(h_unf_Data,h_rec_Data2,varbinning,recovariable)
	# Same as above, but for the closure test.
	[DataRescalingString_pseudo,DataErrorString_pseudo] = GetRescaling(h_unf_Data_pseudo,h_rec_Data_pseudo,varbinning,recovariable)

	print "DataRescaling:", DataRescalingString
	print "PseudoData Rscaling:" , DataRescalingString_pseudo

	print "Error DataRescaling:", DataErrorString
	print "Error PseudoData Rscaling:" , DataErrorString_pseudo

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
		CompMax = 500*CompMax
	
	leftborder =  TLine( presentationbinning[0],CompMin,presentationbinning[0],CompMax )
	rightborder =  TLine( presentationbinning[-1],CompMin,presentationbinning[-1],CompMax )
	leftborder.SetLineStyle(2)
	rightborder.SetLineStyle(2)
	h_gen_WJets.SetMaximum(CompMax)
	h_gen_WJets.SetMinimum(CompMin)
	leftborder.Draw("SAME")
	rightborder.Draw("SAME")	
	if (optvar=="v" or optvar=="V" or optvar=="c"):
		c1.cd(2).SetLogy()
	
	c1.cd(3).Update()


	##############################################################################
	#######      Bottom Right - More legible ratio plots                   #######
	##############################################################################	
	c1.cd(4)
	#c1.cd(4).SetLogy()

	# genpres_selection = gen_selection.replace(gj1,gpj1).replace(gj2,gpj2).replace(gj3,gpj3).replace(gj4,gpj4).replace(gj5,gpj5)
	genpres_selection = ''
	for ll in gen_selection:
		genpres_selection += ll
	# for ll in [[plj1,pj1],[plj2,pj2],[plj3,pj3],[plj4,pj4],[plj5,pj5]]:
	# 	if ll[0] in genpres_selection:
	# 		genpres_selection = genpres_selection.replace(ll[0],ll[1])

	# for ll in [[elj1,ej1],[elj2,ej2],[elj3,ej3],[elj4,ej4],[elj5,ej5]]:
	# 	if ll[0] in genpres_selection:
	# 		genpres_selection = genpres_selection.replace(ll[0],ll[1])

	# for ll in [[plm1,pm1],[elm1,em1]]:
	# 	if ll[0] in genpres_selection:
	# 		genpres_selection = genpres_selection.replace(ll[0],ll[1])

	unfgenpres_selection = genpres_selection

	# if 'jet' in genmodvariable:
	# 	for nn in [1,2,3,4,5]:
			# unfgenpres_selection = unfgen_selection.replace('jet'+str(nn),'jet'+str(nn)+'_bare')



	# WJets Gen + Reco
	h_pres_rec_WJets=CreateHisto('h_pres_rec_WJets','W+Jets '+ gtag+' [Truth/Reco]',t_WJets_MG,recomodvariable,presentationbinning,selection+weight+fW,MCRecoStyle,Label)
	h_pres_rec_WJetsMG=CreateHisto('h_pres_rec_WJets','W+Jets MADGRAPH [Truth/Reco]',t_MG,recomodvariable,presentationbinning,selection+weight+fWMG,MCRecoStyle,Label)
	# h_pres_gen_WJets=CreateHisto('h_pres_gen_WJets','W+Jets '+gtag+' [Truth/Reco]',t_WJets_MG,baregenvariable,presentationbinning,gen_selection+'*weight_pu_central*4955',MCRecoStyle,Label)
	h_pres_gen_WJets=CreateHisto('h_pres_gen_WJets','W+Jets '+gtag+' [Truth/Reco]',t_WJets_MG,baregenvariable,presentationbinning,gen_selection+'*weight_pu_central*4955'+fW,MCRecoStyle,Label)
	h_pres_gen_WJetsMG=CreateHisto('h_pres_gen_WJetsMG','W+Jets MadGraph [Truth/Reco]',t_MG,baregenvariable,presentationbinning,gen_selection+'*weight_pu_central*4955'+fWMG,MCRecoStyle,Label)
	# NOW FROM RIVET
	# h_pres_gen_WJets=CreateHisto('h_pres_gen_WJets','W+Jets [Truth Rivet]',t_rivet,rivetmodvariable,presentationbinning,rivetselection,MCRecoStyle,Label)
	# h_pres_gen_WJetsMG=CreateHisto('h_pres_gen_WJets','W+Jets [Truth Rivet]',t_rivet,rivetmodvariable,presentationbinning,rivetselection,MCRecoStyle,Label)


	# Data
	h_pres_rec_Data=CreateHisto('h_pres_rec_Data','Data, 5/fb [Unfolded/Reco]',t_SingleMuData,recomodvariable,presentationbinning,selection+IsoMuCond,DataCompStyle,Label)
	h_pres_rec_Data_err=CreateHisto('h_pres_rec_Data_err','Data, 5/fb [Unfolded/Reco]',t_SingleMuData,recomodvariable,presentationbinning,selection+IsoMuCond,DataCompStyle,Label)
	h_pres_unf_Data=CreateHisto('h_pres_unf_Data','Data, 5/fb [Unfolded/Reco]',t_SingleMuData,recomodvariable,presentationbinning,selection+'*'+DataRescalingString+IsoMuCond,DataUnfoldedStyle,Label)
	h_pres_unf_Data_err=CreateHisto('h_pres_unf_Data_err','Data, 5/fb [Unfolded/Reco]',t_SingleMuData,recomodvariable,presentationbinning,selection+'*'+DataErrorString+IsoMuCond,DataUnfoldedStyle,Label)

	# Closure
	h_pres_unf_Data_pseudo=CreateHisto('h_pres_unf_Data_pseudo','MC Closure [Unf. Reco/ Gen]',t_MG,recomodvariable,presentationbinning,selection+weight+fWMG+'*'+DataRescalingString_pseudo,DataUnfoldedStyle_pseudo,Label)
	h_pres_unf_Data_err_pseudo=CreateHisto('h_pres_unf_Data_err_pseudo','MC Closure [Unf. Reco/ Gen]',t_MG,recomodvariable,presentationbinning,selection+weight+fWMG+'*'+DataErrorString_pseudo,DataUnfoldedStyle_pseudo,Label)

	# Other Backgrounds Rescaled
	h_pres_rec_DiBoson_res=CreateHisto('h_pres_rec_DiBoson_res','DiBoson [MadGraph]',t_DiBoson,recomodvariable,presentationbinning,selection+weight+'*'+DataRescalingString+fV,DiBosonStackStyle,Label)
	h_pres_rec_ZJets_res=CreateHisto('h_pres_rec_ZJets_res','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,presentationbinning,selection+weight+'*'+DataRescalingString+fZ,ZStackStyle,Label)
	h_pres_rec_TTBar_res=CreateHisto('h_pres_rec_TTBar_res','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,presentationbinning,selection+weight+'*'+DataRescalingString+fT,TTStackStyle,Label)
	h_pres_rec_SingleTop_res=CreateHisto('h_pres_rec_SingleTop_res','SingleTop [MadGraph]',t_SingleTop,recomodvariable,presentationbinning,selection+weight+'*'+DataRescalingString+fsT,StopStackStyle,Label)	

	h_pres_rec_QCDMu_res=CreateHisto('h_pres_rec_QCDMu_res','QCD',t_SingleMuData,recomodvariable,presentationbinning,qcdselection+'*(MT_muon1METR>50)*(RelIso_muon1>0.15)*(Mu24Pass>0)*Mu24PassPrescale*('+str(QCDSF)+')*'+DataRescalingString,QCDStackStyle,Label)
	tn = 0
	for tt in nonisotrees:
		__sf = treesf[tn]
		h_pres_rec_QCDMu_res.Add(CreateHisto('h_pres_rec_QCDMu_res_add'+str(random.randint(0,1000000)),'mc',tt,recomodvariable,presentationbinning,qcdselection+weight+'*(MT_muon1METR>50)*(RelIso_muon1>0.15)*(-1.0)*('+str(QCDSF)+')*'+DataRescalingString+__sf,QCDStackStyle,Label))
		tn += 1

	# Other Backgrounds Unrescaled
	h_pres_rec_DiBoson=CreateHisto('h_pres_rec_DiBoson','DiBoson [MadGraph]',t_DiBoson,recomodvariable,presentationbinning,selection+weight+fV,DiBosonStackStyle,Label)
	h_pres_rec_ZJets=CreateHisto('h_pres_rec_ZJets','Z+Jets [MadGraph]',t_ZJets_MG,recomodvariable,presentationbinning,selection+weight+fZ,ZStackStyle,Label)
	h_pres_rec_TTBar=CreateHisto('h_pres_rec_TTBar','t#bar{t} [MadGraph]',t_TTBar,recomodvariable,presentationbinning,selection+weight+fT,TTStackStyle,Label)
	h_pres_rec_SingleTop=CreateHisto('h_pres_rec_SingleTop','SingleTop [MadGraph]',t_SingleTop,recomodvariable,presentationbinning,selection+weight+fsT,StopStackStyle,Label)	

	h_pres_rec_QCDMu=CreateHisto('h_pres_rec_QCDMu','QCD',t_SingleMuData,recomodvariable,presentationbinning,qcdselection+'*(MT_muon1METR>50)*(RelIso_muon1>0.15)*(Mu24Pass>0)*Mu24PassPrescale*('+str(QCDSF)+')',QCDStackStyle,Label)
	tn = 0 
	for tt in nonisotrees:
		__sf = treesf[tn]	
		h_pres_rec_QCDMu.Add(CreateHisto('h_pres_rec_QCDMu_add'+str(random.randint(0,1000000)),'mc',tt,recomodvariable,presentationbinning,qcdselection+weight+'*(MT_muon1METR>50)*(RelIso_muon1>0.15)*(-1.0)*('+str(QCDSF)+')'+__sf,QCDStackStyle,Label))
		tn += 1
	# Make background subtracted histos.
	# h_pres_rec_Data = BackgroundSubtractedHistogram(h_pres_rec_Data,[ h_pres_rec_DiBoson_res, h_pres_rec_ZJets_res,h_pres_rec_TTBar_res,h_pres_rec_SingleTop_res,h_pres_rec_QCDMu_res])
	# h_pres_unf_Data = BackgroundSubtractedHistogram(h_pres_unf_Data,[ h_pres_rec_DiBoson, h_pres_rec_ZJets,h_pres_rec_TTBar,h_pres_rec_SingleTop,h_pres_rec_QCDMu])

	h_pres_rec_Data = BackgroundSubtractedHistogram(h_pres_rec_Data,[ h_pres_rec_DiBoson, h_pres_rec_ZJets,h_pres_rec_TTBar,h_pres_rec_SingleTop,h_pres_rec_QCDMu])
	h_pres_unf_Data = BackgroundSubtractedHistogram(h_pres_unf_Data,[ h_pres_rec_DiBoson_res, h_pres_rec_ZJets_res,h_pres_rec_TTBar_res,h_pres_rec_SingleTop_res,h_pres_rec_QCDMu_res])

	DataBinInfo=[]
	MCBinInfo=[]

	# Loop to get the data and MC bin info as lists - need for tables and so forth.

	lumifactor = 1.0
	if 'lumi_plus' in tagname:
		lumifactor = lumifactor * 1.022
	if 'lumi_minus' in tagname:
		lumifactor = lumifactor / 1.022

	for x in range(h_pres_rec_Data.GetNbinsX()+1):
		if x==0:
			continue
		if h_pres_unf_Data.GetBinContent(x) != 0:
			h_pres_unf_Data.SetBinError(x,h_pres_unf_Data_err.GetBinContent(x)/h_pres_unf_Data.GetBinContent(x))
		else: 
			h_pres_unf_Data.SetBinError(x,0)

		lhs=h_pres_unf_Data.GetBinCenter(x)-0.5*(h_pres_unf_Data.GetBinWidth(x))
		rhs=h_pres_unf_Data.GetBinCenter(x)+0.5*(h_pres_unf_Data.GetBinWidth(x))
		content=lumifactor*h_pres_unf_Data.GetBinContent(x)
		error=lumifactor*h_pres_unf_Data_err.GetBinContent(x)
		lhs=str(lhs)
		rhs=str(rhs)
		content=str(round(content,2))
		error=str(round(error,2))
		DataBinInfo.append([lhs+' - '+str(rhs),content+' +- '+error])

		lhs=h_pres_gen_WJets.GetBinCenter(x)-0.5*(h_pres_gen_WJets.GetBinWidth(x))
		rhs=h_pres_gen_WJets.GetBinCenter(x)+0.5*(h_pres_gen_WJets.GetBinWidth(x))
		content=lumifactor*h_pres_gen_WJets.GetBinContent(x)
		error=lumifactor*h_pres_gen_WJets.GetBinError(x)
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
	h_pres_unf_Data_pseudo.Divide(h_pres_gen_WJetsMG)

	## Divide gen by reco for MC, and unfolded by reco for data.
	h_pres_gen_WJets.Divide(h_pres_rec_WJets)
	h_pres_unf_Data.Divide(h_pres_rec_Data)

	# Clean up style for closure test
	h_pres_unf_Data_pseudo = BeautifyHisto(h_pres_unf_Data_pseudo,DataUnfoldedStyle_pseudo2,Label,"MC Closure [Unf. Reco/ Gen]")

	# Dashed line at unity for closure test
	l_one=TLine(presentationbinning[0], 1 ,presentationbinning[-1],1)
	l_one.SetLineStyle(2)
	
	# Appropriate y axis ranges...
	# RelMax=0.0
	# RelMin=990.0
	# binset = ConvertBinning(binning)
	# for x in range(len(binset)):
	# 	if x == 0:
	# 		continue
	# 	M=max([h_pres_gen_WJets.GetBinContent(x),h_pres_unf_Data.GetBinContent(x)])
	# 	m=min([h_pres_gen_WJets.GetBinContent(x),h_pres_unf_Data.GetBinContent(x)])
	# 	if M>RelMax and M<10:
	# 		RelMax=M
	# 	if m<RelMin and m<10:
	# 		RelMin=m
	# RelMax*=2.0
	# RelMin*=0.75
	# if RelMin < 0.0:
	# 	RelMin = 0.0
	# if RelMax > 5.0:
	# 	RelMax = 5.0
	RelMin = 0.0
	RelMax = 3.0
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
	c1.Print('pyplots/'+recovariable+'_'+tagname+namelabel+'.pdf')
	c1.Print('pyplots/'+recovariable+'_'+tagname+namelabel+'.png')


	c3 = TCanvas("c3","",700,500)
	c3pad1 = TPad( 'c3pad1', 'c3pad1', 0.0, 0.0, 1.0, 1.0 )#divide canvas into pads
	c3pad1.Draw()
	c3pad1.SetLogy()
	c3pad1.cd()
	h_dd.GetXaxis().SetTitle('Bin of '+Label[0]+' dist.')
	h_dd.GetYaxis().SetTitle('d_{i}')
	h_dd.Draw("")
	l_oneB=TLine(0, 1 ,len(varbinning),1)

	l_oneB.Draw("SAME")

	l1B=TLatex()
	l1B.SetTextAlign(12)
	l1B.SetTextFont(42)
	l1B.SetNDC()
	l1B.SetTextSize(0.05)
	l1B.DrawLatex(0.22,0.85,recovariable+' '+namelabel)


	# clear tmp file
	os.system("rm "+tmpname)
	c3.Print('pyplots/DI_'+recovariable+'_'+tagname+namelabel+'.pdf')
	c3.Print('pyplots/DI_'+recovariable+'_'+tagname+namelabel+'.png')



	if 'preexc' in namelabel:
		DataBinInfo = MakeInclusiveBinInfo(DataBinInfo)
		MCBinInfo = MakeInclusiveBinInfo(MCBinInfo)

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
def FullAnalysisWithUncertainty(genvariable,recovariable,default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,prefab_tau):

	# prefab_tau = 123456
	# prefab_tau = -10

	if 'BinByBin' in 'pyplots':
		prefab_tau = 123456

	# This is the standard plot. here we get the optimal tau value. 
	_tau = -1
	if prefab_tau > -1:
		_tau = prefab_tau
	[tau,data_standard,mc_standard]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',_tau,'standard')

	if prefab_tau > -1:
		tau = prefab_tau

	if ('--quickplots') in sys.argv:
		return 0

	# Replacing with ScaleUp/ScaleDown samples. 
	# [null,data_scale_plus,mc_scale_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'ScaleUp',tau,'scaleup')
	# [null,data_scale_minus,mc_scale_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'ScaleDown',tau,'scaledown')
	# [null,data_match_plus,mc_match_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'MatchUp',tau,'matchup')
	# [null,data_match_minus,mc_match_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'MatchDown',tau,'matchdown')
	
	if (False):

		# Plleup variations
		[null,data_pileup_plus,mc_pileup_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('central','sysplus'),optvar,NormalDirectory,'',tau,'pileup_plus')
		[null,data_pileup_minus,mc_pileup_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('central','sysminus'),optvar,NormalDirectory,'',tau,'pileup_minus')

		[null,data_bgnorm_plus,mc_bgnorm_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'bgnorm_plus')
		[null,data_bgnorm_minus,mc_bgnorm_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'bgnorm_minus')


		# Integrated luminosity up/down
		# [null,data_lumi_plus,mc_lumi_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('4955','5064'),optvar,NormalDirectory,'',tau,'lumi_plus')
		# [null,data_lumi_minus,mc_lumi_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('4955','4848'),optvar,NormalDirectory,'',tau,'lumi_minus')

		[null,data_lumi_plus,mc_lumi_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'lumi_plus')
		[null,data_lumi_minus,mc_lumi_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'lumi_minus')


		# Jet energy scale up/down, and smeared
		[null,data_jetscale_plus,mc_jetscale_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,JetScaleUpDirectory,'',tau,'jetscale_plus')
		[null,data_jetscale_minus,mc_jetscale_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,JetScaleDownDirectory,'',tau,'jetscale_minus')
		[null,data_jetsmear,mc_jetsmear]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,JetSmearDirectory,'',tau,'jetsmear')

		# Muon energy scale up/down and smeared.
		[null,data_muscale_plus,mc_muscale_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,MuScaleUpDirectory,'',tau,'muscale_plus')
		[null,data_muscale_minus,mc_muscale_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,MuScaleDownDirectory,'',tau,'muscale_minus')
		[null,data_musmear,mc_musmear]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,MuSmearDirectory,'',tau,'musmear')	

		# BTag Efficiency Up/Down
		if 'UnCorr' not in selection[0]:
			[null,data_btag_plus,mc_btag_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,[selection[0].replace('CountCentral','CountEffUp'),selection[1]],gen_selection,weight,optvar,NormalDirectory,'',tau,'btag_plus')
			[null,data_btag_minus,mc_btag_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,[selection[0].replace('CountCentral','CountEffDown'),selection[1]],gen_selection,weight,optvar,NormalDirectory,'',tau,'btag_minus')

		else:
			[null,data_btag_plus,mc_btag_plus]=[tau,data_standard,mc_standard]
			[null,data_btag_minus,mc_btag_minus]=[tau,data_standard,mc_standard]
			
		# [null,data_altunf,mc_altunf]=[tau,data_standard,mc_standard]

		# [null,data_altunf,mc_altunf]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',-1,'altunf')
		[null,data_altunf,mc_altunf]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'altunf')

		[null,data_hltidiso,mc_hltidiso]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'hltidiso')



	if (False):  # JUST JES

		[null,data_pileup_plus,mc_pileup_plus]= [tau,data_standard,mc_standard]
		[null,data_pileup_minus,mc_pileup_minus]= [tau,data_standard,mc_standard]

		[null,data_bgnorm_plus,mc_bgnorm_plus]= [tau,data_standard,mc_standard]
		[null,data_bgnorm_minus,mc_bgnorm_minus]= [tau,data_standard,mc_standard]


		# Integrated luminosity up/down
		[null,data_lumi_plus,mc_lumi_plus]=[tau,data_standard,mc_standard]
		[null,data_lumi_minus,mc_lumi_minus]=[tau,data_standard,mc_standard]

		# Jet energy scale up/down, and smeared
		[null,data_jetscale_plus,mc_jetscale_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,JetScaleUpDirectory,'',tau,'jetscale_plus')
		[null,data_jetscale_minus,mc_jetscale_minus]=[tau,data_standard,mc_standard]
		[null,data_jetsmear,mc_jetsmear]=[tau,data_standard,mc_standard]

		# Muon energy scale up/down and smeared.
		[null,data_muscale_plus,mc_muscale_plus]=[tau,data_standard,mc_standard]
		[null,data_muscale_minus,mc_muscale_minus]=[tau,data_standard,mc_standard]
		[null,data_musmear,mc_musmear]=[tau,data_standard,mc_standard]

		# BTag Efficiency Up/Down
		[null,data_btag_plus,mc_btag_plus]=[tau,data_standard,mc_standard]
		[null,data_btag_minus,mc_btag_minus]=[tau,data_standard,mc_standard]

		[null,data_altunf,mc_altunf]=[tau,data_standard,mc_standard]
		# [null,data_altunf,mc_altunf]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'altunf')

		[null,data_hltidiso,mc_hltidiso]=[tau,data_standard,mc_standard]


	# QUICK FIX FOR NO SYSTEMATICS
	if (True):
		[null,data_pileup_plus,mc_pileup_plus]= [tau,data_standard,mc_standard]
		[null,data_pileup_minus,mc_pileup_minus]= [tau,data_standard,mc_standard]


		[null,data_bgnorm_plus,mc_bgnorm_plus]= [tau,data_standard,mc_standard]
		[null,data_bgnorm_minus,mc_bgnorm_minus]= [tau,data_standard,mc_standard]


		# Integrated luminosity up/down
		[null,data_lumi_plus,mc_lumi_plus]=[tau,data_standard,mc_standard]
		[null,data_lumi_minus,mc_lumi_minus]=[tau,data_standard,mc_standard]

		# Jet energy scale up/down, and smeared
		# [null,data_jetscale_plus,mc_jetscale_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,JetScaleUpDirectory,'',tau,'jetscale_plus')		
		[null,data_jetscale_plus,mc_jetscale_plus]=[tau,data_standard,mc_standard]
		[null,data_jetscale_minus,mc_jetscale_minus]=[tau,data_standard,mc_standard]
		[null,data_jetsmear,mc_jetsmear]=[tau,data_standard,mc_standard]

		# Muon energy scale up/down and smeared.
		[null,data_muscale_plus,mc_muscale_plus]=[tau,data_standard,mc_standard]
		[null,data_muscale_minus,mc_muscale_minus]=[tau,data_standard,mc_standard]
		[null,data_musmear,mc_musmear]=[tau,data_standard,mc_standard]

		# BTag Efficiency Up/Down
		[null,data_btag_plus,mc_btag_plus]=[tau,data_standard,mc_standard]
		[null,data_btag_minus,mc_btag_minus]=[tau,data_standard,mc_standard]

		# [null,data_altunf,mc_altunf]=[tau,data_standard,mc_standard]
		[null,data_altunf,mc_altunf]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight,optvar,NormalDirectory,'',tau,'altunf')

		[null,data_hltidiso,mc_hltidiso]=[tau,data_standard,mc_standard]


	# QUICK FIX FOR NO SYSTEMATICS
	if (False):
		[null,data_pileup_plus,mc_pileup_plus]= [tau,data_standard,mc_standard]
		[null,data_pileup_minus,mc_pileup_minus]= [tau,data_standard,mc_standard]

		[null,data_bgnorm_plus,mc_bgnorm_plus]= [tau,data_standard,mc_standard]
		[null,data_bgnorm_minus,mc_bgnorm_minus]= [tau,data_standard,mc_standard]

		# Integrated luminosity up/down
		[null,data_lumi_plus,mc_lumi_plus]=[tau,data_standard,mc_standard]
		[null,data_lumi_minus,mc_lumi_minus]=[tau,data_standard,mc_standard]

		# Jet energy scale up/down, and smeared
		[null,data_jetscale_plus,mc_jetscale_plus]=[tau,data_standard,mc_standard]
		[null,data_jetscale_minus,mc_jetscale_minus]=[tau,data_standard,mc_standard]
		[null,data_jetsmear,mc_jetsmear]=[tau,data_standard,mc_standard]

		# Muon energy scale up/down and smeared.
		[null,data_muscale_plus,mc_muscale_plus]=[tau,data_standard,mc_standard]
		[null,data_muscale_minus,mc_muscale_minus]=[tau,data_standard,mc_standard]
		[null,data_musmear,mc_musmear]=[tau,data_standard,mc_standard]

		# BTag Efficiency Up/Down
		[null,data_btag_plus,mc_btag_plus]=[tau,data_standard,mc_standard]
		[null,data_btag_minus,mc_btag_minus]=[tau,data_standard,mc_standard]

		[null,data_altunf,mc_altunf]=[tau,data_standard,mc_standard]

		[null,data_hltidiso,mc_hltidiso]=[tau,data_standard,mc_standard]





	# Here we make a vary verbose table.	
	data_table=[['|','Bin','|','Prediction','|','DataMean','|','PU(+)','PU(-)','|','BG(+)','BG(-)','|','Lumi(+)','Lumi(-)','|','BTag(+)','BTag(-)','|','JScale(+)','JScale(-)','JetSmear','|','MuScale(+)','MuScale(-)','MuSmear','|','Generator(+)','Generator(-)','|','HLTIDISO(+)','HLTIDISO(-)','|']]#,'|','Scale(+)','Scale(-)','Match(+)','Match(-)','|']]
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

		bg_up = (data_bgnorm_plus[x])[1]
		bg_down = (data_bgnorm_minus[x])[1]

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

		generator= data_altunf[x][1]
		centval = float(center.split("+-")[0])
		alt = float(generator.split("+-")[0])
		if alt>0 and centval:
			if alt>centval:
				gen_factor = alt/centval
			else:
				gen_factor = centval/alt
		else:
			gen_factor = 1.0
		gen_1 = centval*gen_factor
		gen_2 = centval/gen_factor

		gens = [gen_1,gen_2]
		gens.sort()
		gen_down = str(round(gens[0],2)) + '+-'+generator.split('+-')[-1]
		gen_up = str(round(gens[1],2)) + '+-'+generator.split('+-')[-1]


		muoneff= data_hltidiso[x][1]

		id_1 = float(muoneff.split("+-")[0])
		centval = float(center.split("+-")[0])
		id_2 = centval - (id_1-centval)

		ids = [id_1,id_2]
		ids.sort()
		id_down = str(round(ids[0],2)) + '+-'+muoneff.split('+-')[-1]
		id_up = str(round(ids[1],2)) + '+-'+muoneff.split('+-')[-1]


		# Strip out the +- statistical uncertainty for the various systematics. We will only consider statistical uncertainties on the central values. 
		for v in ['pu_up','pu_down','bg_up','bg_down','jet_up','jet_down','jet_smear','mu_up','mu_down','mu_smear','lumi_up','lumi_down','btag_up','btag_down','gen_down','gen_up','id_up','id_down']:
			exec(v+'='+v+'.split("+-")[0]')
		
		# Add a line to the data table.
		data_table.append(['|',thisbin,'|',prediction,'|',center,'|',pu_up,pu_down,'|',bg_up,bg_down,'|',lumi_up,lumi_down,'|',btag_up,btag_down,'|',jet_up,jet_down,jet_smear,'|',mu_up,mu_down,mu_smear,'|',gen_up,gen_down,'|',id_up,id_down,'|'])#,'|',scale_up,scale_down,match_up,match_down,'|'])
	
	# Here we print a cleaned-up table.
	f = open('table_tmp.txt','w')
	print ' GETTING READY TO PRINT TABLE!!!'
	for line in data_table:
		print 'OUTPUT TABLE PRINTING HERE...'
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
	os.system('cat table_tmp.txt | column -t -s"," > pyplots/'+recovariable+xlabel[-1]+'.txt')
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
# 	[null,data_lumi_plus,mc_lumi_plus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('4955','5090'),optvar,NormalDirectory,'',tau,'lumi_plus')
# 	[null,data_lumi_minus,mc_lumi_minus]=MakeUnfoldedPlots(genvariable,recovariable, default_value,xlabel, binning,presentationbinning,selection,gen_selection,weight.replace('4955','4870'),optvar,NormalDirectory,'',tau,'lumi_minus')

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
			if mean>0 and variations[v][n] > 0:
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
		BGerrors = filter_pair([errors[2],errors[3]])

		LUMIerrors=filter_pair([errors[4],errors[5]])
		BTAGerrors=filter_pair([errors[6],errors[7]])

		JESerrors=filter_pair([errors[8],errors[9]])
		JERerrors=[errors[10]]
		MESerrors=filter_pair([errors[11],errors[12]])
		MERerrors=[errors[13]]
		GENerrors = [errors[14],errors[15]]
		IDerrors = [errors[16],errors[17]]

		# SCALEerrors=filter_pair([errors[12],errors[13]])
		# MATCHerrors=filter_pair([errors[14],errors[15]])
		STATerrors=[rel_err, -rel_err]
		
		allerrors=PUerrors+BGerrors+LUMIerrors+BTAGerrors+JESerrors+JERerrors+MESerrors+MERerrors+STATerrors+GENerrors+IDerrors#SCALEerrors+MATCHerrors+STATerrors
		# Quick hack to ignore shape systematics
		# allerrors=PUerrors+LUMIerrors+JESerrors+JERerrors+MESerrors+MERerrors+STATerrors

		standard_errorset = [PUerrors,BGerrors,LUMIerrors,BTAGerrors,JESerrors,JERerrors,MESerrors,MERerrors,STATerrors,GENerrors,IDerrors]#SCALEerrors,MATCHerrors,STATerrors]

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
			if abs(x)>10*mean:
				continue
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
		
		# test fix
		if abs(center) < 0.0000001:
			center = 999999999

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
		hout.GetYaxis().SetTitleFont(42)
		hout.GetXaxis().SetTitleSize(.05)
		hout.GetYaxis().SetTitleSize(.05)
		hout.GetXaxis().CenterTitle()
		hout.GetYaxis().CenterTitle()
		hout.GetXaxis().SetTitleOffset(0.9)
		hout.GetYaxis().SetTitleOffset(1.15)
		hout.GetYaxis().SetLabelSize(.05)
		hout.GetXaxis().SetLabelSize(.05)
		hout.GetYaxis().SetNdivisions(508)


	if plottype=="SubPlot":
		hout.GetYaxis().SetNdivisions(308)
		hout.GetYaxis().SetTitleFont(42)
		hout.GetXaxis().SetTitleSize(.13)
		hout.GetYaxis().SetTitleSize(.13)
		hout.GetXaxis().CenterTitle()
		hout.GetYaxis().CenterTitle()
		hout.GetXaxis().SetTitleOffset(.33)
		hout.GetYaxis().SetTitleOffset(.33)
		hout.GetYaxis().SetLabelSize(.09)
		hout.GetXaxis().SetLabelSize(.09)

	return [hout,[mean,up,down,binset]]


def CreateWindowFromVerbse(_verbs,Name,label,style,norm,plottype,symmetrize):
	meansets = []
	for L in _verbs:
		meansets.append(L[0])
	_mins = []
	_maxs = []
	_centers = []
	_ups = []
	_downs = []
	binrange = range(len(meansets[0]))
	for m in binrange:
		entries = [_means[m] for _means in meansets]
		_mins.append(min(entries))
		_maxs.append(max(entries))
		_centers.append(  meansets[0][m] )
		_iup = abs(_maxs[-1] - _centers[-1])
		_idown = abs(_mins[-1] - _centers[-1])

		if symmetrize: 
			_ierr = max([_iup,_idown])
			_iup = _ierr
			_idown = _ierr

		_ups.append(_iup)
		_downs.append(_idown )



	binning = _verbs[0][-1]

	# print 'Binning:',binning
	# print 'Name:',Name
	# print 'Label:',label
	# print 'Centers:',_centers
	# print 'Ups:',_ups
	# print 'Downs:',_downs
	# print 'Style:',style
	# print 'PlotType:',plottype
	OutputHisto = CreateHistoFromLists(binning, Name,label, _centers, _ups,_downs, style,norm,plottype)

	return OutputHisto




def MergeErrorsFromVerbse(_verbs,Name,label,style,norm,plottype,symmetrize):
	meansets = []
	upsets = []
	downsets = []
	for L in _verbs:
		meansets.append(L[0])
		upsets.append(L[1])
		downsets.append(L[2])

	_mins = []
	_maxs = []
	_centers = []
	_ups = []
	_downs = []
	binrange = range(len(meansets[0]))
	for m in binrange:
		meanentries = [contents[m] for contents in meansets]
		upentries = [contents[m] for contents in upsets]
		downentries = [contents[m] for contents in downsets]


		_centers.append(  meansets[0][m] )

		_iup = 0.0
		_idown = 0.0

		for xx in upentries:
			_iup += xx*xx		
		for xx in downentries:
			_idown += xx*xx		
		_iup = math.sqrt(_iup)
		_idown = math.sqrt(_idown)


		if symmetrize: 
			_ierr = max([_iup,_idown])
			_iup = _ierr
			_idown = _ierr

		_ups.append(_iup)
		_downs.append(_idown )



	binning = _verbs[0][-1]

	# print 'Binning:',binning
	# print 'Name:',Name
	# print 'Label:',label
	# print 'Centers:',_centers
	# print 'Ups:',_ups
	# print 'Downs:',_downs
	# print 'Style:',style
	# print 'PlotType:',plottype
	OutputHisto = CreateHistoFromLists(binning, Name,label, _centers, _ups,_downs, style,norm,plottype)

	return OutputHisto


# Take a given binning, and means with errors, and create a TGraphAsymErrors output.
def CreateBandHistoFromLists(binning, name, label, mean, up, down, style,normalization,plottype):

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
	# print X
	# print Xplus
	# print Xminus
	# hout.GetXaxis().SetRangeUser(X[0],X[-1])
	# hout.GetXaxis().SetLimits(X[0],X[-1])

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
		hout.GetYaxis().SetTitleFont(42)
		hout.GetXaxis().SetTitleSize(.05)
		hout.GetYaxis().SetTitleSize(.05)
		hout.GetXaxis().CenterTitle()
		hout.GetYaxis().CenterTitle()
		hout.GetXaxis().SetTitleOffset(0.9)
		hout.GetYaxis().SetTitleOffset(1.15)
		hout.GetYaxis().SetLabelSize(.05)
		hout.GetXaxis().SetLabelSize(.05)


	if plottype=="SubPlot":
		hout.GetYaxis().SetNdivisions(508)
		hout.GetYaxis().SetTitleFont(42)
		hout.GetXaxis().SetTitleSize(.13)
		hout.GetYaxis().SetTitleSize(.13)
		hout.GetXaxis().CenterTitle()
		hout.GetYaxis().CenterTitle()
		hout.GetXaxis().SetTitleOffset(.33)
		hout.GetYaxis().SetTitleOffset(.33)
		hout.GetYaxis().SetLabelSize(.09)
		hout.GetXaxis().SetLabelSize(.09)

	return [hout,[mean,up,down,binset]]

# Use CreateHistoFromLists to quickly cast a Rivet NTuple into a tGraph for overlay with other plots. 
def RivetHisto(rivetfile, rivetvariable, binning,selection, label, style,original_events,normalization, ncompare, quantity, WRenormalizationForRivet):

	# print ' ------> ',rivetvariable
	frivet = TFile.Open(rivetfile)
	if 'SummaryFile' not in rivetfile:
		trivet = frivet.Get("RivetTree")
	else:
		trivet = frivet.Get("PhysicalVariables")

	Name = "MadGraph"*("Madgraph" in rivetfile)+"MadGraphAOD"*("MG.root" in rivetfile) + "Pythia"*("Pythia" in rivetfile)  + "Sherpa"*("Sherpa" in rivetfile) + ("PROBLEM")*(("Madgraph" not in rivetfile)*("Pythia" not in rivetfile)*("Sherpa" not in rivetfile))
	hrivet = CreateHisto(Name,Name,trivet,rivetvariable,binning,selection+'*'+WRenormalizationForRivet,style,label)
	hrivet.Scale(4955.0*31314.0/(1.0*original_events))



	if 'njet_WMuNu' in rivetvariable and len(binning) > 7:
	
		print 'Converting',rivetfile,':',rivetvariable,' to integrated histo.'

		for _n in range(hrivet.GetNbinsX()):
			__cont = 0.0
			__err = 0.0
			for __n in range(hrivet.GetNbinsX()):
				if __n >= _n:
					__cont += hrivet.GetBinContent(__n) 
					__err += hrivet.GetBinError(__n) **2.0
				__err = math.sqrt(__err)
			hrivet.SetBinContent(_n,__cont)
			hrivet.SetBinError(_n,__err)

		binning = ConvertBinning([6 ,0.5,6.5])

	# print 'RIVETSELECTION: ',selection+'*'+WRenormalizationForRivet
	# print 'RIvet histo: ',rivetfile, rivetvariable, binning
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


	# print ' ***',means

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

# Use CreateHistoFromLists to quickly cast a Rivet NTuple into a tGraph for overlay with other plots. 
def BlackHatHisto(rivetvariable, binning, standard_name, label, style, quantity, ncompare, normalization,hadhisto,nonhadhisto,dohadrenorm,bhdir):

	# bhdir = 'hists5/hists_CT10/'
	bhdir += '/'
	Name = 'BlackHat'	
	bhfile = bhdir+'W1j_all.root'
	bhfiles = [bhdir+'W'+str(nn)+'j_all.root' for nn in [0,1,2,3,4]]


	if 'njet_WMuNu' in rivetvariable and len(binning) > 6:
		binning = ConvertBinning([4 ,0.5,4.5])

	if 'jet1' in standard_name:
		bhfile = bhfiles[1]
	if 'jet2' in standard_name:
		bhfile = bhfiles[2]
	if 'jet3' in standard_name:
		bhfile = bhfiles[3]
	if 'jet4' in standard_name:
		bhfile = bhfiles[4]			

	# print 'For - ',rivetvariable, ' -- using: ',bhfile
	# print "  BH ------->  ",rivetvariable, " --> ",rivetvariable.replace('htjets','ht')
	hblackhat = TFile.Open(bhfile).Get(rivetvariable.replace('htjets','ht'))
	# print "    --- > int ---> ",hblackhat.GetEntries(),hblackhat.Integral()
	# print 'Blackhat histo for ',rivetvariable, 'with binning',binning

	# for nn in range((hblackhat.GetNbinsX())+2):
	# 	print hblackhat.GetBinCenter(nn) - hblackhat.GetBinWidth(nn)*0.5

	means=[]
	errs=[]
	scalefactor = 1.0
	# for x in range(len(binning)-1):
	# 	means.append(scalefactor*(hblackhat.GetBinContent(x+1)))
	# 	errs.append(scalefactor*(hblackhat.GetBinError(x+1)))


	if 'Count' in standard_name:
		# hblackhat = TH1D('hblackhat','hblackhat',6,array('d',[0.5,1.5,2.5,3.5,4.5,5.5,6.5]))
		for nn in [1,2,3,4]:
			bhindex = 0
			newbhfile = bhfiles[nn]
			lhs = 99
			for nb in range(hblackhat.GetNbinsX()+2):	
				lhs = hblackhat.GetBinCenter(nb) - hblackhat.GetBinWidth(nb)*0.5
				lhs = int(lhs)
				if lhs == nn:
					bhindex = nb

			bhsource = TFile.Open(newbhfile).Get(rivetvariable)
			bhsourceindex = 0
			for nb in range(bhsource.GetNbinsX()+2):	
				lhs = bhsource.GetBinCenter(nb) - bhsource.GetBinWidth(nb)*0.5
				lhs = int(lhs)
				if lhs == nn:
					bhsourceindex = nb

			binloc = bhsource.GetBinCenter(bhsourceindex) - 0.5					
			binloc2 = hblackhat.GetBinCenter(bhindex) - 0.5					

			newcont = bhsource.GetBinContent(bhsourceindex)			
			newerr = bhsource.GetBinError(bhsourceindex)

			if ('preexc' in standard_name) and (nn <4):
				newcont += bhsource.GetBinContent(bhsourceindex+1)
				newerr *= newerr
				newerr += (bhsource.GetBinError(bhsourceindex+1))**2.0
				newerr = math.sqrt(newerr)

			bhindex = bhindex -1 
			hblackhat.SetBinContent(bhindex,newcont)
			hblackhat.SetBinError(bhindex,newerr)


	bhscale = (4955.0/1000.0)
	hblackhat.Scale(bhscale)

	# print binning
	bhbinning = []
	rhs = 0.0
	hadsfs = []
	for x in range(len(binning)-1):

		_x = x

		if 'ht_jet1' in standard_name:
			_x += 0
		if 'ht_jet2' in standard_name:
			_x += 1
		if 'ht_jet3' in standard_name:
			_x += 2
		if 'ht_jet4' in standard_name:
			_x += 3

		hadsf = 1.0
		if (hadhisto[0][x] > 0.0) and  (nonhadhisto[0][x]> 0.0):
			hadsf = hadhisto[0][x]/nonhadhisto[0][x]

		# hadsf = 1.0 # QUICK FIX!	
		hadsfs.append(hadsf)

		meanval = scalefactor*(hblackhat.GetBinContent(_x+1))*(hblackhat.GetBinWidth(_x+1))
		# print ' *** ',hadsf,' *** ', meanval,' --> ',meanval*hadsf

		means.append( meanval*hadsf )
		bhbinning.append( hblackhat.GetBinCenter(_x+1) - 0.5*hblackhat.GetBinWidth(_x+1) )
		rhs = (hblackhat.GetBinCenter(_x+1) + 0.5*hblackhat.GetBinWidth(_x+1))
		# errs.append(means[-1]*0.05)
		errs.append(hadsf*scalefactor*(hblackhat.GetBinError(_x+1))*(hblackhat.GetBinWidth(_x+1)) )		

	bhbinning.append(rhs)

	if 'Count' in standard_name:
		for iii in range(2):
			binning.append(binning[-1]+1.0)
			means.append(0.0)
			errs.append(0.0)

	# print standard_name,label
	# print ' -- ',binning
	# if 'ht' in standard_name:
	# 	# print 'Abridging blackhat to have correct bins.'
	# 	nabridge = -1
	# 	if 'inc1' in standard_name:
	# 		nabridge += 0
	# 	if 'inc2' in standard_name:
	# 		nabridge += 1
	# 	if 'inc3' in standard_name:
	# 		nabridge += 2
	# 	if 'inc4' in standard_name:
	# 		nabridge += 3
	# 	print 'Abridging from index',nabridge						
	# 	if nabridge>-1:
	# 		binning = binning[nabridge:]
	# 		means = means[nabridge:]
	# 		errs = errs[nabridge:]
	# print ' ---- ', binning

	# if 'ht' in standard_name:
	# 	print 'INSERTING MISSING BINS'
	# 	for yy in [30.0,60.0,90.0,120.0]:
	# 		print binning
	# 		if yy not in binning:
	# 			print 'mod:',binning
	#  			binning = [yy] + binning
	#  			means = [0.0]+means
	#  			errs = [0.0]+errs


	# print 'BH:',binning 

	if normalization==0:
		label = [label, 'Events/Bin']
	else:
		label = [label, '#sigma [pb]']

	blackhatscale = ncompare/(hblackhat.Integral())

	BlackHatOutputHisto = CreateHistoFromLists(binning, Name,label, means, errs, errs, style,normalization,"SubPlot")

	BlackHatOutputHisto[0].GetXaxis().SetTitle(label[0])
	BlackHatOutputHisto[0].GetYaxis().SetTitle(label[1])
	BlackHatOutputHisto[0].GetXaxis().SetTitleFont(42)
	BlackHatOutputHisto[0].GetYaxis().SetTitleFont(42)
	BlackHatOutputHisto[0].GetXaxis().SetLabelFont(42)
	BlackHatOutputHisto[0].GetYaxis().SetLabelFont(42)

	BlackHatOutputHisto[0].GetYaxis().SetTitleFont(42);
	BlackHatOutputHisto[0].GetXaxis().SetTitleSize(.1);
	BlackHatOutputHisto[0].GetYaxis().SetTitleSize(.1);
	BlackHatOutputHisto[0].GetXaxis().CenterTitle();
	BlackHatOutputHisto[0].GetYaxis().CenterTitle();
	BlackHatOutputHisto[0].GetXaxis().SetTitleOffset(1.1);
	BlackHatOutputHisto[0].GetYaxis().SetTitleOffset(1.1);
	BlackHatOutputHisto[0].GetYaxis().SetLabelSize(.1);
	BlackHatOutputHisto[0].GetXaxis().SetLabelSize(.1);
	return [BlackHatOutputHisto,blackhatscale]


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

	return CreateHistoFromLists(binset, "example",["","Data / MC"], ratmean,raterr,raterr,style,1.0,"SubPlot")[0]

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
	return [CreateHistoFromLists(binset, "example",["","Data / MC"], ratmean,raterr_up,raterr_down,style,1.0,"SubPlot")[0] ,[yup,ydown]]



# Using basic asymmetric errors.
def HadRatioPlot(gv1, gv2,XName,binning,fname):

	binset = ConvertBinning(binning)
	style = [0,20,.7,1,1]

	[mean1,up1,down1,binset]=gv1
	[mean2,up2,down2,binset]=gv2

	ratmean = []
	raterr_up = []
	raterr_down = []

	yvalues = []
	print '1'
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
			rat = 1.0
		ratmean.append(rat)

		raterr = math.sqrt(abs(u1 - m1)**2.0 + abs(u2-m2)**2.0)


		raterr_up.append(raterr)
		raterr_down.append(raterr)
		
	print '2'
	[res,[null,null2,null3,null4]] = CreateHistoFromLists(binset, "example",[XName,"Ratio"], ratmean,raterr_up,raterr_down,style,1.0,"SubPlot")
	print '3'
	cp = TCanvas("cp","",500,800)
	print '4a'
	pad1a = TPad( 'pad1a', 'pad1a', 0.0, 0.0, 1.0, 1.0 )#divide canvas into pads
	print '4b'
	res.Draw("EP")
	outname = ('HadronizationPlots/'+fname+'_HadComp').replace('.','_')
	print '4c', outname
	cp.Print(outname+'.png')
	print 5
	cp.Print(outname+'.pdf')
	print 6

# Using basic asymmetric errors.
def DivideTGraphsFlatRel(gv1, gv2,style):

	# Inverted to flip ratios!
	[mean1,up1,down1,binset1]=gv2
	[mean2,up2,down2,binset2]=gv1


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
			# print m2,d2
			rat = m1/m2
			ratup = m1/(m2 + u2)
			if m2 != d2:
				ratdown = m1/(m2 - d2)
			else:
				ratdown = 99

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

		# print binset[x],m1,u1,d1

		uval = 0.0
		dval = 0.0
		if m1 > 0:
			uval = u1/m1
			dval = d1/m1
		ratmean.append(1.0)
		raterr_down.append(dval)
		raterr_up.append(uval)
		# print uval,dval
		# yvalues+= [1.0-uval,1.0+dval]
		yvalues+= [1.0-dval,1.0+uval] # Mod for inverted ratios


	yup = round((1.0*max(yvalues)),2)
	ydown = round((1.0*min(yvalues)),2)



	return [CreateHistoFromLists(binset, "example",["","Data / MC"], ratmean,raterr_up,raterr_down,style,1.0,"SubPlot")[0] ,[yup,ydown]]

def AbridgeHistoList(h,nbins):
	[a,b,c,d] = h
	_a = []
	_b = []
	_c = []
	_d = []
	for x in range(nbins):
		_a.append(a[x])
		_b.append(b[x])
		_c.append(c[x])
		_d.append(d[x])
	_d.append(d[range(nbins)[-1]+1])
	return [_a,_b,_c,_d]

# This creates the final "results"-style plot!
def FinalHisto(binning, label, quantity, filename ,expectation_means, expectation_errors, expectation_names, measurement, measurement_error_up, measurement_error_down, normalization,WRenormalization,sel):

	c1 = TCanvas("c1","",700,800)

	pad1 = TPad( 'pad1', 'pad1', 0.0, 0.45, 1.0, 1.0 )#divide canvas into pads
	pad2 = TPad( 'pad2', 'pad2', 0.0, 0.3, 1.0, 0.55 )
	pad3 = TPad( 'pad3', 'pad3', 0.0, 0.15, 1.0, 0.40 )
	pad4 = TPad( 'pad4', 'pad4', 0.0, 0.0, 1.0, 0.25 )

	pad1.SetBottomMargin(0.19)
	pad1.SetTopMargin(0.13)
	pad1.SetLeftMargin(0.12)
	pad1.SetRightMargin(0.1)

	pad2.SetBottomMargin(0.4)
	pad2.SetTopMargin(0.0)
	pad2.SetLeftMargin(0.12)
	pad2.SetRightMargin(0.1)

	pad3.SetBottomMargin(0.4)
	pad3.SetTopMargin(0.0)
	pad3.SetLeftMargin(0.12)
	pad3.SetRightMargin(0.1)


	pad4.SetBottomMargin(0.4)
	pad4.SetTopMargin(0.0)
	pad4.SetLeftMargin(0.12)
	pad4.SetRightMargin(0.1)


	# pad1.SetTopMargin(0)

	# pad2.SetBottomMargin(0)
	# pad2.SetTopMargin(0)


	pad1.Draw()
	pad2.Draw()
	pad3.Draw()
	pad4.Draw()


	# pad1.SetGrid()
	pad1.SetLogy()
	pad1.cd()

	gStyle.SetOptStat(0)
	MadGraphStyle=[3254,21,.5,1,4]
	MadGraphSubStyle=[3254,21,.5,1,4]

	SherpaStyle=[3254+1001,20,.0000005,1,28]

	SherpaRivetStyle=[3254,20,.0000005,1,28]
	# SherpaRivetSubStyle=[3254,22,.9,1,2]
	SherpaRivetSubStyle=[0,32,1.0,1,28]
	BlackHatSubStyle=[0,26,1.0,1,2]


	# MadGraphRivetSubStyle=[3245,21,.9,1,4]
	MadGraphRivetSubStyle=[0,25,1.0,1,4]

	MadGraphAODSubStyle=[0,27,1.0,1,6]

	MadGraphRivetStyle=[3245,21,.5,1,4]

	DataRecoStyle=[0,20,1.0,1,1]	

	# CentralBandStyle = [3001,20,1,1,8]
	# CentralBandStyle = [3001,20,1,1,33]
	CentralBandStyle = [1001,20,1,1,kGreen -9]

	
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
	
	nzm = []
	for __m in measurement:
		if __m > 0.000001:
			# print len(nzm)
			if 'preexc' in filename and len(nzm) >= 6:
				continue
			nzm.append(__m) 
			# print nzm

	Max = max(nzm)*2.5
	Min = min(nzm)*.7
	# print Min

	if normalization==0:
		label = [label, 'Events/Bin']
	else:
		label = [label, '#sigma [pb]']
		Max=Max/normalization
		Min=Min/normalization

	# print "MIN", Min	


	# MadGraph AOD Quick
	name = expectation_names[0]
	mean_value = expectation_means[0]
	plus_errors = expectation_errors[0]
	minus_errors = expectation_errors[0]
	style=MadGraphAODSubStyle
	[Exp,Exp_verbose] = CreateHistoFromLists(binning, name,label, mean_value, plus_errors, minus_errors, style,normalization,"TopPlot")



	for nn in range(6):
		nn+=2
		if 'pfjet'+str(nn) in standardname:
			sel+='j'+str(nn-1)
	
	# Get Measured Histo
	name="Measured"
	mean_value = measurement
	plus_errors=measurement_error_up
	minus_errors=measurement_error_down
	style=DataRecoStyle
	[Meas,Meas_verbose] = CreateHistoFromLists(binning, name,label, mean_value, plus_errors, minus_errors, CentralBandStyle,normalization,"TopPlot")
	ndataunf = sum(Meas_verbose[0])

	if 'preexc' in filename:
		# print "ABRIDGING LISTS"
		Meas_verbose = AbridgeHistoList(Meas_verbose,6)
		Exp_verbose = AbridgeHistoList(Exp_verbose,6)
		# Get Measured Histo
		name="Measured"
		mean_value = measurement
		plus_errors=measurement_error_up
		minus_errors=measurement_error_down
		[Meas,Meas_verbose_null] = CreateHistoFromLists([6 ,0.5,6.5], name,label, mean_value, plus_errors, minus_errors, CentralBandStyle,normalization,"TopPlot")
		# Min = 0.1*min(mean_value)
		# MadGraph AOD Quick
		name = expectation_names[0]
		mean_value = expectation_means[0]
		plus_errors = expectation_errors[0]
		minus_errors = expectation_errors[0]
		[Exp,Exp_verbose_null] = CreateHistoFromLists([6 ,0.5,6.5], name,label, mean_value, plus_errors, minus_errors, style,normalization,"TopPlot")



	Exp.SetMaximum(Max)
	Exp.SetMinimum(Min)


	rivetsel = '(evweight)*(mt_mumet>50)*(ptmuon>25)*(abs(etamuon)<2.1)*(ptjet1>30)'

	if 'jet1' in standardname or 'inc1' in standardname:
		rivetsel += '*(ptjet1>30)'
	if 'jet2' in standardname or 'inc2' in standardname:
		rivetsel += '*(ptjet2>30)'
	if 'jet3' in standardname or 'inc3' in standardname:
		rivetsel += '*(ptjet3>30)'
	if 'jet4' in standardname or 'inc4' in standardname:
		rivetsel += '*(ptjet4>30)'

	if 'inc' in rivetname:
		standardname = 'ht_jet'+rivetname.split('_inc')[1]
		rivetname = rivetname.split('_inc')[0]

	# print 'ME:',Meas_verbose, [len(aa) for aa in Meas_verbose]

	print rivetsel

	aodsel = str(rivetsel)
	aodname = str(rivetname)
	for x in RivetGenBareBranchMap:
		aodsel = aodsel.replace(x[1],x[0])
		aodname = aodname.replace(x[1],x[0])

	print aodsel
	print aodname



	# AOD Histo
	# [[AOD_MadGraph_Result,AOD_MadGraph_Result_verbose], aodrescale] = RivetHisto(NormalDirectory+'/WJets_MG.root',aodname,binning,aodsel,rivetlabel,MadGraphAODSubStyle,4955.0*31314.0,normalization,1.0,quantity,WRenormalization)

	# sys.exit()
	# Get Rivet Histos
	[[Rivet_MadGraph_Result,Rivet_MadGraph_Result_verbose], rivetrescale] = RivetHisto(RIVETMadGraph,rivetname,binning,rivetsel,rivetlabel,MadGraphRivetSubStyle,madgraph_NOriginal,normalization,ndataunf,quantity,WRenormalization)
	[[Rivet_MadGraphNonHad_Result,Rivet_MadGraphNonHad_Result_verbose], rivetrescalenonhad] = RivetHisto(RIVETMadGraphNonHad,rivetname,binning,rivetsel,rivetlabel,MadGraphRivetSubStyle,madgraph_NOriginal,normalization,ndataunf,quantity,WRenormalization)

	# HadRatioPlot(Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,rivetlabel,binning,filename)
	[[Rivet_Sherpa_Result,Rivet_Sherpa_Result_verbose], sherparescale]    = RivetHisto(RIVETSherpa,  rivetname,binning,rivetsel,rivetlabel,  SherpaRivetSubStyle,sherpa_NOriginal  ,normalization,ndataunf,quantity,WRenormalization)

	[[Blackhat_Result,Blackhat_Result_verbose], blackhatrescale]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,'BlackHatAll/hists_CT10_r1.0_f1.0')
	[[Blackhat_Result_nocorr,Blackhat_Result_verbose_nocorr], blackhatrescale_nocorr]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraph_Result_verbose,True,'BlackHatAll/hists_CT10_r1.0_f1.0')
	[Blackhat_Result_hadwindow,Blackhat_Result_verbose_hadwindow] = CreateWindowFromVerbse([Blackhat_Result_verbose, Blackhat_Result_verbose_nocorr],"BlackhatHadCorr",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",True)	


	[[Blackhat_Result_sup,Blackhat_Result_verbose_sup], blackhatrescale_sup]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,'BlackHatAll/hists_CT10_r2.0_f2.0')
	[[Blackhat_Result_sdown,Blackhat_Result_verbose_sdown], blackhatrescale_sdown]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,'BlackHatAll/hists_CT10_r0.5_f0.5')

	[[Blackhat_Result_mstw,Blackhat_Result_verbose_mstw], blackhatrescale_mstw]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,'BlackHatAll/hists_MSTW2008nlo68cl_r1.0_f1.0')
	[[Blackhat_Result_nnpdf,Blackhat_Result_verbose_nnpdf], blackhatrescale_nnpdf]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,'BlackHatAll/hists_NNPDF21_100_r1.0_f1.0')

	[[Blackhat_Result_cteq6,Blackhat_Result_verbose_cteq6], blackhatrescale_cteq6]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,'BlackHatAll/hists_cteq6m_r1.0_f1.0')

	[Blackhat_Result_scalewindow,Blackhat_Result_verbose_scalewindow] = CreateWindowFromVerbse([Blackhat_Result_verbose, Blackhat_Result_verbose_sup,Blackhat_Result_verbose_sdown],"BlackhatScale",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",False)	
	[Blackhat_Result_pdf,Blackhat_Result_verbose_pdf] = CreateWindowFromVerbse([Blackhat_Result_verbose, Blackhat_Result_verbose_mstw,Blackhat_Result_verbose_cteq6, Blackhat_Result_verbose_nnpdf],"BlackhatPDF",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",True)	

	[Blackhat_Result_basic,Blackhat_Result_verbose_basic] = MergeErrorsFromVerbse([Blackhat_Result_verbose, Blackhat_Result_verbose_pdf, Blackhat_Result_verbose_hadwindow],"BlackhatBasic",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",False)	
	[Blackhat_Result_basicplusscale,Blackhat_Result_verbose_basicplusscale] = MergeErrorsFromVerbse([Blackhat_Result_verbose_basic, Blackhat_Result_verbose_scalewindow],"BlackhatBasicplusscale",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",False)	

	# print 'BH:',Blackhat_Result_verbose_basicplusscale, [len(aa) for aa in Blackhat_Result_verbose_basicplusscale]

	# print "MADGRAPH   INT:",Rivet_MadGraph_Result.Integral()
	# print "SHERPA     INT:",Rivet_Sherpa_Result.Integral()
	# print "BLACKHAT   INT:",Blackhat_Result.Integral()
	# print Blackhat_Result_verbose

	# Storing stuff...
	fplot = TFile.Open(filename+'root',"RECREATE")

	# Meas.GetYaxis().SetTitleFont(42);
	Meas.GetXaxis().SetTitleSize(.18);
	Meas.GetXaxis().SetTitleOffset(.12);

	# Meas.GetYaxis().SetTitleSize(.14);
	# Meas.GetXaxis().CenterTitle(0);
	# Meas.GetYaxis().CenterTitle(1);
	# Meas.GetYaxis().SetTitle("")
	Meas.GetXaxis().SetTitle("")

	Meas.Write("Meas")
	# Exp.Write("Exp")
	fplot.Close()

	flog = open(filename+'_TGraphContent.txt','w')
	flog.write('\n,Meas_verbose = '+str(Meas_verbose)+'\n')
	# flog.write('\n,Exp_verbose = '+str(Exp_verbose)+'\n')
	flog.close()

	# print '----  TABLE: ',rivetname
	# print Rivet_MadGraph_Result_verbose
	# print Meas_verbose
	# print ' ------ '
	# Draw Two Rivet Histos and one Measured Histo
	Meas.SetMaximum(Max)
	Meas.SetMinimum(Min)
	Rivet_MadGraph_Result.SetMaximum(Max)
	Rivet_MadGraph_Result.SetMinimum(Min)
	
	# AOD_MadGraph_Result.SetMaximum(Max)
	# AOD_MadGraph_Result.SetMinimum(Min)	

	Rivet_Sherpa_Result.SetMaximum(Max)
	Rivet_Sherpa_Result.SetMinimum(Min)		
	# print 'USING MIN',Min
	Blackhat_Result_basicplusscale.SetMinimum(Min)		
	Blackhat_Result_basicplusscale.SetMaximum(Max)		


	print ' --------------------------------------- '
	print label[0]
	print ' '
	print 'Measured:',Meas_verbose
	print 'Blackhat:',Blackhat_Result_verbose_basicplusscale
	print 'Sherpa:',Rivet_Sherpa_Result_verbose
	print 'Madgraph:',Rivet_MadGraph_Result_verbose
	print ' '
	print filename+'_papertable.tex'
	print ' '
	def verbose_to_string(_verbose):
		_output = []
		for v in range(len(_verbose[0])):
			if '30Count' not in filename:
				_bin = str(round(float(_verbose[-1][v]),2)) +' $-$ ' +str(round(float(_verbose[-1][v+1]),2) )
			else:
				if 'pre' not in filename:
					_bin = str( int(  round( 0.5*float(_verbose[-1][v]) + 0.5*float(_verbose[-1][v+1])  )) )			
				else:
					_bin = ' $\\geq$'+str( int(round( 0.5*float(_verbose[-1][v]) + 0.5*float(_verbose[-1][v+1])  )) )			
			_mean = str(round(_verbose[0][v],2))
			_errp = str(round(_verbose[1][v],2))
			_errm = str(round(_verbose[2][v],2))
			_output.append([_bin,_mean,_errp,_errm])
		return _output
	def check_compatibility(_verbose_sets):
		_binsets = []
		for v in _verbose_sets:
			_binsets.append(v[-1])
		for _b in range(len(_binsets)-1):
			if _binsets[_b] != _binsets[_b+1]:
				print 'Compatibility error!'
				print _binsets[_b]
				print _binsets[_b+1]
				sys.exit()

	check_compatibility([Meas_verbose,Blackhat_Result_verbose_basicplusscale,Rivet_Sherpa_Result_verbose,Rivet_MadGraph_Result_verbose])

	__D = verbose_to_string(Meas_verbose)
	__B = verbose_to_string(Blackhat_Result_verbose_basicplusscale)
	__S = verbose_to_string(Rivet_Sherpa_Result_verbose)
	__M = verbose_to_string(Rivet_MadGraph_Result_verbose)



	vmap = []
	vmap.append(["DeltaPhi_pfjet1muon1","$\\Delta \\phi (jet_1, \mu)$"])
	vmap.append(["DeltaPhi_pfjet2muon1","$\\Delta \\phi (jet_2, \mu)$"])
	vmap.append(["DeltaPhi_pfjet3muon1","$\\Delta \\phi (jet_3, \mu)$"])
	vmap.append(["DeltaPhi_pfjet4muon1","$\\Delta \\phi (jet_4, \mu)$"])
	vmap.append(["Eta_pfjet1","$\\eta(jet_1)$"])
	vmap.append(["Eta_pfjet2","$\\eta(jet_2)$"])
	vmap.append(["Eta_pfjet3","$\\eta(jet_3)$"])
	vmap.append(["Eta_pfjet4","$\\eta(jet_4)$"])
	vmap.append(["MT_muon1MET","$M_T(\\mu,E_T^{miss})$"])
	vmap.append(["PFJet30Count","Exc Jet Mult"])
	vmap.append(["PFJet30Count_preexc","Inc Jet Mult"])
	vmap.append(["Pt_MET","$E_T^{miss}$"])
	vmap.append(["Pt_pfjet1","$p_T(jet_1)$"])
	vmap.append(["Pt_pfjet2","$p_T(jet_2)$"])
	vmap.append(["Pt_pfjet3","$p_T(jet_3)$"])
	vmap.append(["Pt_pfjet4","$p_T(jet_4)$"])
	vmap.append(["Pt_muon1","$p_T(\\mu)$"])
	vmap.append(["Eta_muon1","$\eta(\\mu)$"])
	vmap.append(["HT_pfjets_inc1","$H_T(\\geq 1 jet)$"])
	vmap.append(["HT_pfjets_inc2","$H_T(\\geq 2 jet)$"])
	vmap.append(["HT_pfjets_inc3","$H_T(\\geq 3 jet)$"])
	vmap.append(["HT_pfjets_inc4","$H_T(\\geq 4 jet)$"])

	var = 'Bin'
	for v in vmap:
		if v[0] in str(filename):
			var = v[1]



	_table = ['\\begin{table}[htb]']
	_table.append('\\caption{Bin-by-bin data and uncertainties for the final '+var+' distribution.}')
	_table.append('\\begin{center}')
	_table.append('\\begin{tabular}{|l|l|lll|}\\hline')

	_table.append(var +' & Measurement & Blackhat+Sherpa & Sherpa & MadGraph \\\\ \\hline')

	for x in range(len(__D)):
		__d = __D[x]
		__b = __B[x]
		__s = __S[x]
		__m = __M[x]
		aline = __d[0]
		aline += ' & '+__d[1] +'$^{+'+__d[2]+'}_{-'+__d[3]+'}$ '
		aline += ' & '+__b[1] +'$^{+'+__b[2]+'}_{-'+__b[3]+'}$ '		
		aline += ' & '+__s[1] 
		aline += ' & '+__m[1] 
		aline += ' \\\\ '
		_table.append(aline)
	_table.append('\\hline')
	_table.append('\\end{tabular}')
	_table.append('\\end{center}')
	_table.append( ('\\label{tab:'+filename+'}').replace('.','').replace('/','__') )	
	_table.append('\\end{table}')
	_table.append('')
	__tab = open(filename+'_papertable.tex','w')
	for tline in _table:
		print tline
		__tab.write(tline+'\n')
	__tab.close()

	print ' '
	print ' --------------------------------------- '
	# sys.exit()


	# Meas.SetMarkerSize(0.0001)
	# Meas.SetLineColor(1)

	Meas.SetMarkerColor(1)
	Meas.Draw("A2")
	Meas.Draw("PX")

	Rivet_MadGraph_Result.Draw("P")

	# AOD_MadGraph_Result.Draw("P")
	Rivet_Sherpa_Result.Draw("P")
	Blackhat_Result_basicplusscale.Draw("P")

	# print 'MEAS:',Meas_verbose[-1]
	# print 'MG:', Rivet_MadGraph_Result_verbose[-1]
	# print 'Sherpa', Rivet_Sherpa_Result_verbose[-1]
	# print 'BH:', Blackhat_Result_verbose_basicplusscale[-1]
	# Blackhat_Result_basicplusscale.Draw("2")

	# Blackhat_Result_basic.Draw("||")

	# gPad.Update()
	Blackhat_Result_mstw.SetLineStyle(2)
	Blackhat_Result_cteq6.SetLineStyle(2)

	# Blackhat_Result_mstw.Draw("L")
	# Blackhat_Result_cteq6.Draw("L")
	# Exp.Draw("P")

	leg = TLegend(0.5,0.64,0.84,0.84,"","brNDC")
	leg.SetTextFont(42)
	leg.SetFillColor(0)
	leg.SetBorderSize(0)
	leg.SetTextSize(.05)
	leg.AddEntry(Meas,"Data");
	leg.AddEntry(Rivet_MadGraph_Result,"MadGraph")
	# leg.AddEntry(AOD_MadGraph_Result,"MadGraph AOD")
	# leg.AddEntry(Exp,"MadGraph AOD");
	leg.AddEntry(Rivet_Sherpa_Result,"Sherpa")
	leg.AddEntry(Blackhat_Result,"BlackHat+Sherpa")
	leg.Draw()




	# Stamp on top
	sqrts = "#sqrt{s} = 7 TeV";
	l1=TLatex()
	l1.SetTextAlign(12)
	l1.SetTextFont(42)
	l1.SetNDC()
	l1.SetTextSize(0.05)
	l1.DrawLatex(0.15,0.92,"CMS Preliminary     "+sqrts+"      #int L = 5.0 fb^{-1}")
	# l1.DrawLatex(0.19,0.87,"CMS Preliminary ")
	# l1.DrawLatex(0.19,0.81,sqrts+"  #int L = 5.0 fb^{-1}")

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
	pad2.SetGridy()
	pad2.Draw()

	[cent1,[cent2up,cent2down]] = CentralRatioBand(Meas_verbose, CentralBandStyle)

	# print Meas_verbose
	# print Rivet_Sherpa_Result_verbose
	# print 'Dividing Meas/Sherpa'
	# print Meas_verbose
	# print Rivet_Sherpa_Result_verbose
	[grat2,[grat2up,grat2down]] = DivideTGraphsFlatRel(Meas_verbose,Rivet_Sherpa_Result_verbose,SherpaRivetSubStyle)
	unity=TLine(grat2.GetXaxis().GetXmin(), 1.0 , grat2.GetXaxis().GetXmax(),1.0)

	# print 'Dividing Meas/MG RIVET'
	[grat3,[grat3up,grat3down]] = DivideTGraphsFlatRel(Meas_verbose,Rivet_MadGraph_Result_verbose,MadGraphRivetSubStyle)
	# [grat3aod,[grat3upaod,grat3downaod]] = DivideTGraphsFlatRel(Meas_verbose,AOD_MadGraph_Result_verbose,MadGraphAODSubStyle)

	# print 'Dividing Meas/BH'
	# print Meas_verbose
	# print Blackhat_Result_verbose
	[grat4,[grat4up,grat4down]] = DivideTGraphsFlatRel(Meas_verbose,Blackhat_Result_verbose_basicplusscale,BlackHatSubStyle)
	# print 'Dividing Meas/BHBasic'
	[grat4b,[grat4bup,grat4bdown]] = DivideTGraphsFlatRel(Meas_verbose,Blackhat_Result_verbose_basic,BlackHatSubStyle)

	[grat5,[grat5up,grat5down]] = DivideTGraphsFlatRel(Meas_verbose,Exp_verbose,MadGraphAODSubStyle)

	[grat6,[grat6up,grat6down]] = DivideTGraphsFlatRel(Meas_verbose,Blackhat_Result_verbose_mstw,BlackHatSubStyle)
	[grat6b,[grat6bup,grat6bdown]] = DivideTGraphsFlatRel(Meas_verbose,Blackhat_Result_verbose_cteq6,BlackHatSubStyle)
	grat6.SetLineStyle(2)
	grat6b.SetLineStyle(2)


	if grat3up > grat2up: grat2up = grat3up
	if grat3down < grat2down: grat2down = grat3down

	grat2up *= 1.3
	grat2down *= 0.7
	if grat2down < 0 : grat2down = 0
	if grat2up > 5: grat2up = 5

	grat2down = 0.501
	grat2up = 1.499

	# print 'CENTRAL VALUES:', cent2up,cent2down
	if cent2up > 1.5 or cent2down < 0.5:
		grat2down = 0.001
		grat2up = 1.999		
	
	cent1.SetMaximum(grat2up)
	cent1.SetMinimum(grat2down)
	cent1.GetXaxis().SetTitle(label[0])
	cent1.GetYaxis().SetTitle("MC/Data")
	cent1.GetXaxis().SetTitleOffset(.73);

	cent1.GetYaxis().SetTitleFont(42);
	cent1.GetXaxis().SetTitleSize(.07);
	cent1.GetYaxis().SetTitleSize(.07);
	# cent1.GetXaxis().CenterTitle(1);
	# cent1.GetYaxis().CenterTitle(1);
	# cent1.GetXaxis().SetTitleOffset(0.7);
	# cent1.GetYaxis().SetTitleOffset(0.3);
	# cent1.GetYaxis().SetLabelSize(.1);
	# cent1.GetXaxis().SetLabelSize(.1);

	grat2.SetMinimum(grat2down)
	grat2.SetMaximum(grat2up)
	grat3.SetMinimum(grat2down)
	grat3.SetMaximum(grat2up)
	# grat3aod.SetMinimum(grat2down)
	# grat3aod.SetMaximum(grat2up)
	
	
	cent1.Draw("A2")
	unity.Draw("SAME")
	grat3.Draw("p")
	# grat3aod.Draw("p")

	lb2=TLatex()
	lb2.SetTextAlign(12)
	lb2.SetTextFont(42)
	lb2.SetNDC()
	lb2.SetTextSize(0.1)
	lb2.DrawLatex(0.18,0.5,"Madgraph")







	pad3.SetGridy()
	pad4.SetGridy()

	pad2.RedrawAxis()
	pad3.cd()
	cent1.Draw("A2")
	unity.Draw("SAME")
	grat2.Draw("p")
	pad3.RedrawAxis()

	lb3=TLatex()
	lb3.SetTextAlign(12)
	lb3.SetTextFont(42)
	lb3.SetNDC()
	lb3.SetTextSize(0.1)
	lb3.DrawLatex(0.18,0.5,"Sherpa")


	pad4.cd()
	cent1.Draw("A2")
	unity.Draw("SAME")	
	grat4.Draw("p")
	# grat4b.Draw("||")
	# grat6.Draw("L")
	# grat6b.Draw("L")

	# grat5.Draw("p")
	lb4=TLatex()
	lb4.SetTextAlign(12)
	lb4.SetTextFont(42)
	lb4.SetNDC()
	lb4.SetTextSize(0.1)
	lb4.DrawLatex(0.18,0.5,"Blackhat+Sherpa")

	cent1.GetXaxis().SetTitleSize(.14);
	cent1.GetYaxis().SetTitleSize(.14);

	pad4.RedrawAxis()


	c1.Print(filename+'pdf')
	c1.Print(filename+'png')



# This creates the final "results"-style plot!
def FinalHistoOLD(binning, label, quantity, filename ,expectation_means, expectation_errors, expectation_names, measurement, measurement_error_up, measurement_error_down, normalization,WRenormalization,sel):

	c1 = TCanvas("c1","",700,800)

	pad1 = TPad( 'pad1', 'pad1', 0.0, 0.31, 1.0, 1.0 )#divide canvas into pads
	pad2 = TPad( 'pad2', 'pad2', 0.0, 0.02, 1.0, 0.31 )

	pad1.SetBottomMargin(0.0)
	pad1.SetTopMargin(0.13)
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
	MadGraphStyle=[3254,21,.5,1,4]
	MadGraphSubStyle=[3254,21,.5,1,4]

	SherpaStyle=[3254+1001,20,.0000005,1,28]

	SherpaRivetStyle=[3254,20,.0000005,1,28]
	# SherpaRivetSubStyle=[3254,22,.9,1,2]
	SherpaRivetSubStyle=[0,32,1.0,1,28]
	BlackHatSubStyle=[0,26,1.0,1,2]


	# MadGraphRivetSubStyle=[3245,21,.9,1,4]
	MadGraphRivetSubStyle=[0,25,1.0,1,4]

	MadGraphAODSubStyle=[0,21,1.0,1,28]

	MadGraphRivetStyle=[3245,21,.5,1,4]

	DataRecoStyle=[0,20,1.0,1,1]	

	# CentralBandStyle = [3001,20,1,1,8]
	# CentralBandStyle = [3001,20,1,1,33]
	CentralBandStyle = [1001,20,1,1,5]

	
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
	
	nzm = []
	for __m in measurement:
		if __m > 0.000001:
			# print len(nzm)
			if 'preexc' in filename and len(nzm) >= 6:
				continue
			nzm.append(__m) 
			# print nzm

	Max = max(nzm)*5.5
	Min = min(nzm)*.4
	# print Min

	if normalization==0:
		label = [label, 'Events/Bin']
	else:
		label = [label, '#sigma [pb]']
		Max=Max/normalization
		Min=Min/normalization

	# print "MIN", Min	


	# MadGraph AOD Quick
	name = expectation_names[0]
	mean_value = expectation_means[0]
	plus_errors = expectation_errors[0]
	minus_errors = expectation_errors[0]
	style=MadGraphAODSubStyle
	[Exp,Exp_verbose] = CreateHistoFromLists(binning, name,label, mean_value, plus_errors, minus_errors, style,normalization,"TopPlot")



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

	if 'preexc' in filename:
		# print "ABRIDGING LISTS"
		Meas_verbose = AbridgeHistoList(Meas_verbose,6)
		Exp_verbose = AbridgeHistoList(Exp_verbose,6)
		# Get Measured Histo
		name="Measured"
		mean_value = measurement
		plus_errors=measurement_error_up
		minus_errors=measurement_error_down
		[Meas,Meas_verbose_null] = CreateHistoFromLists([6 ,0.5,6.5], name,label, mean_value, plus_errors, minus_errors, CentralBandStyle,normalization,"TopPlot")
		# Min = 0.1*min(mean_value)
		# MadGraph AOD Quick
		name = expectation_names[0]
		mean_value = expectation_means[0]
		plus_errors = expectation_errors[0]
		minus_errors = expectation_errors[0]
		[Exp,Exp_verbose_null] = CreateHistoFromLists([6 ,0.5,6.5], name,label, mean_value, plus_errors, minus_errors, style,normalization,"TopPlot")



	Exp.SetMaximum(Max)
	Exp.SetMinimum(Min)


	rivetsel = '(evweight)*(mt_mumet>50)*(ptmuon>25)*(abs(etamuon)<2.1)*(ptjet1>30)'

	if 'jet1' in standardname or 'inc1' in standardname:
		rivetsel += '*(ptjet1>30)'
	if 'jet2' in standardname or 'inc2' in standardname:
		rivetsel += '*(ptjet2>30)'
	if 'jet3' in standardname or 'inc3' in standardname:
		rivetsel += '*(ptjet3>30)'
	if 'jet4' in standardname or 'inc4' in standardname:
		rivetsel += '*(ptjet4>30)'

	if 'inc' in rivetname:
		standardname = 'ht_jet'+rivetname.split('_inc')[1]
		rivetname = rivetname.split('_inc')[0]

	# print 'ME:',Meas_verbose, [len(aa) for aa in Meas_verbose]

	# Get Rivet Histos
	[[Rivet_MadGraph_Result,Rivet_MadGraph_Result_verbose], rivetrescale] = RivetHisto(RIVETMadGraph,rivetname,binning,rivetsel,rivetlabel,MadGraphRivetSubStyle,madgraph_NOriginal,normalization,ndataunf,quantity,WRenormalization)
	[[Rivet_MadGraphNonHad_Result,Rivet_MadGraphNonHad_Result_verbose], rivetrescalenonhad] = RivetHisto(RIVETMadGraphNonHad,rivetname,binning,rivetsel,rivetlabel,MadGraphRivetSubStyle,madgraph_NOriginal,normalization,ndataunf,quantity,WRenormalization)

	# HadRatioPlot(Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,rivetlabel,binning,filename)
	[[Rivet_Sherpa_Result,Rivet_Sherpa_Result_verbose], sherparescale]    = RivetHisto(RIVETSherpa,  rivetname,binning,rivetsel,rivetlabel,  SherpaRivetSubStyle,sherpa_NOriginal  ,normalization,ndataunf,quantity,WRenormalization)

	[[Blackhat_Result,Blackhat_Result_verbose], blackhatrescale]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,'BlackHatAll/hists_CT10_r1.0_f1.0')
	[[Blackhat_Result_nocorr,Blackhat_Result_verbose_nocorr], blackhatrescale_nocorr]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraph_Result_verbose,True,'BlackHatAll/hists_CT10_r1.0_f1.0')
	[Blackhat_Result_hadwindow,Blackhat_Result_verbose_hadwindow] = CreateWindowFromVerbse([Blackhat_Result_verbose, Blackhat_Result_verbose_nocorr],"BlackhatHadCorr",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",True)	


	[[Blackhat_Result_sup,Blackhat_Result_verbose_sup], blackhatrescale_sup]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,'BlackHatAll/hists_CT10_r2.0_f2.0')
	[[Blackhat_Result_sdown,Blackhat_Result_verbose_sdown], blackhatrescale_sdown]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,'BlackHatAll/hists_CT10_r0.5_f0.5')

	[[Blackhat_Result_mstw,Blackhat_Result_verbose_mstw], blackhatrescale_mstw]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,'BlackHatAll/hists_MSTW2008nlo68cl_r1.0_f1.0')
	[[Blackhat_Result_cteq6,Blackhat_Result_verbose_cteq6], blackhatrescale_cteq6]    = BlackHatHisto( rivetname,binning,standardname, rivetlabel, BlackHatSubStyle,quantity,ndataunf,normalization,Rivet_MadGraph_Result_verbose,Rivet_MadGraphNonHad_Result_verbose,True,'BlackHatAll/hists_cteq6m_r1.0_f1.0')

	[Blackhat_Result_scalewindow,Blackhat_Result_verbose_scalewindow] = CreateWindowFromVerbse([Blackhat_Result_verbose, Blackhat_Result_verbose_sup,Blackhat_Result_verbose_sdown],"BlackhatScale",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",False)	
	[Blackhat_Result_pdf,Blackhat_Result_verbose_pdf] = CreateWindowFromVerbse([Blackhat_Result_verbose, Blackhat_Result_verbose_mstw,Blackhat_Result_verbose_cteq6],"BlackhatPDF",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",True)	

	[Blackhat_Result_basic,Blackhat_Result_verbose_basic] = MergeErrorsFromVerbse([Blackhat_Result_verbose, Blackhat_Result_verbose_pdf, Blackhat_Result_verbose_hadwindow],"BlackhatBasic",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",False)	
	[Blackhat_Result_basicplusscale,Blackhat_Result_verbose_basicplusscale] = MergeErrorsFromVerbse([Blackhat_Result_verbose_basic, Blackhat_Result_verbose_scalewindow],"BlackhatBasicplusscale",rivetlabel,BlackHatSubStyle,normalization,"TopPlot",False)	

	# print 'BH:',Blackhat_Result_verbose_basicplusscale, [len(aa) for aa in Blackhat_Result_verbose_basicplusscale]

	# print "MADGRAPH   INT:",Rivet_MadGraph_Result.Integral()
	# print "SHERPA     INT:",Rivet_Sherpa_Result.Integral()
	# print "BLACKHAT   INT:",Blackhat_Result.Integral()
	# print Blackhat_Result_verbose

	# Storing stuff...
	fplot = TFile.Open(filename+'root',"RECREATE")

	Meas.Write("Meas")
	# Exp.Write("Exp")
	fplot.Close()

	flog = open(filename+'_TGraphContent.txt','w')
	flog.write('\n,Meas_verbose = '+str(Meas_verbose)+'\n')
	# flog.write('\n,Exp_verbose = '+str(Exp_verbose)+'\n')
	flog.close()

	# print '----  TABLE: ',rivetname
	# print Rivet_MadGraph_Result_verbose
	# print Meas_verbose
	# print ' ------ '
	# Draw Two Rivet Histos and one Measured Histo
	Meas.SetMaximum(Max)
	Meas.SetMinimum(Min)
	Rivet_MadGraph_Result.SetMaximum(Max)
	Rivet_MadGraph_Result.SetMinimum(Min)
	Rivet_Sherpa_Result.SetMaximum(Max)
	Rivet_Sherpa_Result.SetMinimum(Min)		
	# print 'USING MIN',Min
	Blackhat_Result_basicplusscale.SetMinimum(Min)		
	Blackhat_Result_basicplusscale.SetMaximum(Max)		


	# Meas.SetMarkerSize(0.0001)
	# Meas.SetLineColor(1)

	Meas.SetMarkerColor(1)
	Meas.Draw("A2")
	Meas.Draw("PX")

	Rivet_MadGraph_Result.Draw("P")
	Rivet_Sherpa_Result.Draw("P")
	Blackhat_Result_basicplusscale.Draw("P")

	# print 'MEAS:',Meas_verbose[-1]
	# print 'MG:', Rivet_MadGraph_Result_verbose[-1]
	# print 'Sherpa', Rivet_Sherpa_Result_verbose[-1]
	# print 'BH:', Blackhat_Result_verbose_basicplusscale[-1]
	# Blackhat_Result_basicplusscale.Draw("2")

	# Blackhat_Result_basic.Draw("||")

	# gPad.Update()
	Blackhat_Result_mstw.SetLineStyle(2)
	Blackhat_Result_cteq6.SetLineStyle(2)

	# Blackhat_Result_mstw.Draw("L")
	# Blackhat_Result_cteq6.Draw("L")
	# Exp.Draw("P")

	leg = TLegend(0.5,0.68,0.84,0.84,"","brNDC")
	leg.SetTextFont(42)
	leg.SetFillColor(0)
	leg.SetBorderSize(0)
	leg.SetTextSize(.04)
	leg.AddEntry(Meas,"Data");
	leg.AddEntry(Rivet_MadGraph_Result,"MadGraph")
	# leg.AddEntry(Exp,"MadGraph AOD");
	leg.AddEntry(Rivet_Sherpa_Result,"Sherpa")
	leg.AddEntry(Blackhat_Result,"BlackHat+Sherpa")

	leg.Draw()

	# Stamp on top
	sqrts = "#sqrt{s} = 7 TeV";
	l1=TLatex()
	l1.SetTextAlign(12)
	l1.SetTextFont(42)
	l1.SetNDC()
	l1.SetTextSize(0.05)
	l1.DrawLatex(0.15,0.92,"CMS Preliminary     "+sqrts+"      #int L = 5.0 fb^{-1}")
	# l1.DrawLatex(0.19,0.87,"CMS Preliminary ")
	# l1.DrawLatex(0.19,0.81,sqrts+"  #int L = 5.0 fb^{-1}")

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
	pad2.SetGridy()
	pad2.Draw()

	[cent1,[cent2up,cent2down]] = CentralRatioBand(Meas_verbose, CentralBandStyle)

	# print Meas_verbose
	# print Rivet_Sherpa_Result_verbose
	# print 'Dividing Meas/Sherpa'
	# print Meas_verbose
	# print Rivet_Sherpa_Result_verbose
	[grat2,[grat2up,grat2down]] = DivideTGraphsFlatRel(Meas_verbose,Rivet_Sherpa_Result_verbose,SherpaRivetSubStyle)
	unity=TLine(grat2.GetXaxis().GetXmin(), 1.0 , grat2.GetXaxis().GetXmax(),1.0)

	# print 'Dividing Meas/MG RIVET'
	[grat3,[grat3up,grat3down]] = DivideTGraphsFlatRel(Meas_verbose,Rivet_MadGraph_Result_verbose,MadGraphRivetSubStyle)
	# print 'Dividing Meas/BH'
	# print Meas_verbose
	# print Blackhat_Result_verbose
	[grat4,[grat4up,grat4down]] = DivideTGraphsFlatRel(Meas_verbose,Blackhat_Result_verbose_basicplusscale,BlackHatSubStyle)
	# print 'Dividing Meas/BHBasic'
	[grat4b,[grat4bup,grat4bdown]] = DivideTGraphsFlatRel(Meas_verbose,Blackhat_Result_verbose_basic,BlackHatSubStyle)

	[grat5,[grat5up,grat5down]] = DivideTGraphsFlatRel(Meas_verbose,Exp_verbose,MadGraphAODSubStyle)

	[grat6,[grat6up,grat6down]] = DivideTGraphsFlatRel(Meas_verbose,Blackhat_Result_verbose_mstw,BlackHatSubStyle)
	[grat6b,[grat6bup,grat6bdown]] = DivideTGraphsFlatRel(Meas_verbose,Blackhat_Result_verbose_cteq6,BlackHatSubStyle)
	grat6.SetLineStyle(2)
	grat6b.SetLineStyle(2)


	if grat3up > grat2up: grat2up = grat3up
	if grat3down < grat2down: grat2down = grat3down

	grat2up *= 1.3
	grat2down *= 0.7
	if grat2down < 0 : grat2down = 0
	if grat2up > 5: grat2up = 5

	grat2down = 0.501
	grat2up = 1.499

	# print 'CENTRAL VALUES:', cent2up,cent2down
	if cent2up > 1.5 or cent2down < 0.5:
		grat2down = 0.001
		grat2up = 1.999		
	
	cent1.SetMaximum(grat2up)
	cent1.SetMinimum(grat2down)
	cent1.GetXaxis().SetTitle(label[0])
	cent1.GetYaxis().SetTitle("Data/MC")
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
	unity.Draw("SAME")
	grat2.Draw("p")
	grat3.Draw("p")
	grat4.Draw("p")
	# grat4b.Draw("||")
	# grat6.Draw("L")
	# grat6b.Draw("L")

	# grat5.Draw("p")
	pad2.RedrawAxis()

	c1.Print(filename+'pdf')
	c1.Print(filename+'png')





def HArrayFromHlog(hlog):
	harray = []
	for line in open(hlog,'r'):
		line = line.replace(';',',')
		line = line.split(',')
		for x in range(len(line)):
			if 'ROOT' in line[x]:
				line[x] = '100'
		fline = [float(x) for x in line]
		harray.append(fline)
	harray = harray[0:-1]
	return harray

def quadsum(_list):
	ss = 0.0
	for a in _list:
		ss += a*a
	ss = math.sqrt(ss)
	return ss

def ParseTablesToRecoHistograms():

	WStackStyle=[3007,20,.00001,2,6]
	TTStackStyle=[3005,20,.00001,2,4]
	ZStackStyle=[3004,20,.00001,2,2]
	DiBosonStackStyle=[3006,20,.00001,2,3]
	StopStackStyle=[3008,20,.00001,2,9]
	QCDStackStyle=[3013,20,.00001,2,15]
	MCGenStyle=[0,20,.00001,1,2]
	MCGenSmearStyle=[0,20,.00001,1,9]
	MCRecoStyle=[0,21,.00001,1,4]
	DataRecoStyle=[0,20,1.0,1,1]
	DataCompStyle=[0,21,1.0,1,6]
	BlankRecoStyle=[0,21,.00001,1,0]
	DataUnfoldedStyle=[0,21,0.5,1,1]
	DataUnfoldedStyle_pseudo=[0,20,0.5,1,9]
	DataUnfoldedStyle_pseudo2=[0,20,0.5,1,2]

	bgbandstyle=[3253,20,.00001,0,14]
	bgbandstyle=[3002,20,.00001,0,14]

	relabels = []
	relabels.append(['Pt_pfjet1','Leading Jet p_{T} [GeV]','p_{T}'])
	relabels.append(['Pt_muon1','Muon p_{T} [GeV]','p_{T}'])
	relabels.append(['N_GoodVertices','N_{Vertices}','N_{Vertices}'])
	relabels.append(['Pt_pfjet2','Second Leading Jet p_{T} [GeV]','p_{T}'])
	relabels.append(['Pt_pfjet3','Third Leading Jet p_{T} [GeV]','p_{T}'])
	relabels.append(['Pt_pfjet4','Fourth Leading Jet p_{T} [GeV]','p_{T}'])
	relabels.append(['Pt_pfjet5','Fifth Leading Jet p_{T} [GeV]','p_{T}'])
	relabels.append(['Eta_pfjet1','Leading Jet #eta','#eta'])
	relabels.append(['Eta_pfjet2','Second Leading Jet #eta','#eta'])
	relabels.append(['Eta_pfjet3','Third Leading Jet #eta','#eta'])
	relabels.append(['Eta_pfjet4','Fourth Leading Jet #eta','#eta'])
	relabels.append(['Eta_pfjet5','Fifth Leading Jet #eta','#eta'])
	relabels.append(['preexc','Jet Count (Inclusive)','N_{Jet}'])
	relabels.append(['PFJet30Count','Jet Count (Exclusive)','N_{Jet}'])
	relabels.append(['MT_muon1METR','M_{T}(#mu,E_{T}^{miss}) [GeV]','M_{T}'])
	relabels.append(['Pt_MET','E_{T}^{miss} [GeV]','E_{T}^{miss}'])
	relabels.append(['DeltaPhi_pfjet1muon1','#Delta #phi(jet_{1},#mu)'	,'#Delta #phi(jet_{1},#mu)'])
	relabels.append(['DeltaPhi_pfjet2muon1','#Delta #phi(jet_{2},#mu)'	,'#Delta #phi(jet_{2},#mu)'])
	relabels.append(['DeltaPhi_pfjet3muon1','#Delta #phi(jet_{3},#mu)'	,'#Delta #phi(jet_{3},#mu)'])
	relabels.append(['DeltaPhi_pfjet4muon1','#Delta #phi(jet_{4},#mu)'	,'#Delta #phi(jet_{4},#mu)'])
	relabels.append(['DeltaPhi_pfjet5muon1','#Delta #phi(jet_{5},#mu)'	,'#Delta #phi(jet_{5},#mu)'])

	filesets = []

	allfiles = glob('pyplots/*hlog')
	usedfiles = []
	# print allfiles
	for rl in relabels:
		fset = []
		for a in allfiles:
			if rl[0] in a and 'standard' in a and a not in usedfiles:
				fset.append(a)
		for a in allfiles:
			if rl[0] in a and 'standard' not in a and a not in usedfiles:
				fset.append(a)
		if len(fset)>0:
			fset.append([rl[1],"Events/Bin"])
			filesets.append(fset)
		usedfiles = []
		for x in filesets:
			for y in x:
				usedfiles.append(y)

	for f in filesets:
		print ' '
		c1 = TCanvas("c1","",800,600)
		cpad1 = TPad( 'cpad1', 'cpad1', 0.0, 0.0, 1.0, 1.0 )#divide canvas into pads
		cpad1.SetRightMargin(0.1)
		cpad1.SetTopMargin(0.13)

		dolinear = False
		if 'MT' in str(f):
			dolinear=True
		dolinear = False
		if (dolinear == False):
			cpad1.SetLogy()

		cpad1.Draw()
		cpad1.cd()

		harray = HArrayFromHlog(f[0])
		# print harray
		_binning = []

		entries = []
		plotmin = 99999.9
		plotmax = 0.1
		for entry in harray:
			# print entry
			[lhs,rhs,q,eq,s,es,v,ev,z,ez,t,et,w,ew,T,eT,D] = entry
			print lhs, rhs
			_plotpoints = [q,s,v,z,t,w,T,D]
			plotpoints = []
			for p in _plotpoints:
				if p>0.0001:
					plotpoints.append(p)
			entries.append(entry)
			_binning.append(lhs)
			if len(plotpoints)==0:
				continue
			_plotmin = 10.9*min(plotpoints)
			_plotmax = 4.0*max(plotpoints)
			if _plotmin < plotmin: plotmin = _plotmin
			if _plotmax > plotmax: plotmax = _plotmax


		if plotmin <0.1: plotmin = 0.1
		if dolinear:
			plotmin = 0
			plotmax = 0.25*plotmax*1.2
		_binning.append(rhs)
		# print _binning
		presentationbinning= _binning
		Label = f[-1]
		hs_rec_WJets=NullHisto('hs_rec_WJets','W+Jets',presentationbinning,WStackStyle,Label)
		hs_rec_Data=NullHisto('hs_rec_Data','Data, 5/fb',presentationbinning,DataRecoStyle,Label)
		hs_rec_DiBoson=NullHisto('hs_rec_DiBoson','DiBoson',presentationbinning,DiBosonStackStyle,Label)
		hs_rec_ZJets=NullHisto('hs_rec_ZJets','Z+Jets',presentationbinning,ZStackStyle,Label)
		hs_rec_TTBar=NullHisto('hs_rec_TTBar','t#bar{t}',presentationbinning,TTStackStyle,Label)
		hs_rec_SingleTop=NullHisto('hs_rec_SingleTop','SingleTop',presentationbinning,StopStackStyle,Label)
		hs_rec_QCDMu=NullHisto('hs_rec_QCDMu','QCD',presentationbinning,QCDStackStyle,Label)

		# Declare the MC Stack
		MCStack = THStack ("MCStack","")

		MCStack.SetMinimum(plotmin)
		MCStack.SetMaximum(plotmax)

		# List of MC Histos
		SM=[hs_rec_QCDMu,hs_rec_SingleTop,hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar,hs_rec_WJets]
		xoffset = 1.1
		_nbin = 0
		for entry in entries:
			_nbin += 1
			[lhs,rhs,q,eq,s,es,v,ev,z,ez,t,et,w,ew,T,eT,D] = entry			
			# print hs_rec_WJets.GetBinCenter(_nbin) - 0.5*hs_rec_WJets.GetBinWidth(_nbin)

			hs_rec_WJets.SetBinContent(_nbin,w)
			hs_rec_Data.SetBinContent(_nbin,D)
			hs_rec_DiBoson.SetBinContent(_nbin,v)
			hs_rec_ZJets.SetBinContent(_nbin,z)
			hs_rec_TTBar.SetBinContent(_nbin,t)
			hs_rec_SingleTop.SetBinContent(_nbin,s)
			hs_rec_QCDMu.SetBinContent(_nbin,q)

		# Build stack
		for x in SM:
			# print x.Integral()
			# x.GetXaxis().SetRangeUser(_binning[0],_binning[-1])
			# x.GetXaxis().SetLimits(_binning[0],_binning[-1])
			x.SetMaximum(plotmax)
			x.SetMaximum(plotmin)
			x.GetXaxis().SetTitleOffset(xoffset)

			MCStack.Add(x)
		# MCStack.GetHistogram().GetXaxis().SetRangeUser(_binning[0],_binning[-1])		
		# hs_rec_Data.GetXaxis().SetRangeUser(_binning[0],_binning[-1])
		# hs_rec_Data.GetXaxis().SetLimits(_binning[0],_binning[-1])






		centlog = f[0]
		syslogs = (f[1:-1])

		_centralvals = []
		_staterrs = []
		_syserrsup = []
		_syserrsdown = []

		_variations = []

		for entry in HArrayFromHlog(centlog):
			[lhs,rhs,q,eq,s,es,v,ev,z,ez,t,et,w,ew,T,eT,D] = entry
			_centralvals.append(T)
			_staterrs.append(eT)

		for syslog in syslogs:
			_sysvals = []
			for entry in HArrayFromHlog(syslog):
				[lhs,rhs,q,eq,s,es,v,ev,z,ez,t,et,w,ew,T,eT,D] = entry
				_sysvals.append(T)
			_variations.append(_sysvals)

		# print f
		for _c in range(len(_centralvals)):
			c = _centralvals[_c]
			_staterr = _staterrs[_c]
			_upvars = []
			_downvars = []
			for _v in _variations:
				_val = _v[_c]
				if _val > c:
					_upvars.append(_val - c)
				if _val < c:
					_downvars.append(c-_val)
			_upvars.append(_staterr)
			_downvars.append(_staterr)
			# print c, _upvars,_downvars				
			__sup = quadsum(_upvars)
			__sdown = quadsum(_downvars)
			_syserrsup.append(__sup)
			_syserrsdown.append(__sdown)

		# print _centralvals
		# print _staterrs
		# print _syserrsup
		# print _syserrsdown


		# print 'WINDOW', presentationbinning, plotmin
		[ErrorWindow,null] = CreateBandHistoFromLists(presentationbinning, "",Label, _centralvals, _syserrsup, _syserrsdown, bgbandstyle,1.0,"TopPlot")
		print presentationbinning
		print _centralvals
		# [ErrorWindow,null] = CreateHistoFromLists([100.0,110.0,120.0,130.0], "",Label, [10000.0,10000.0,10000.0], [1000.0,1000.0,1000.0], [10000.0,10000.0,10000.0] , bgbandstyle,1.0,"TopPlot")
		# print null

		ErrorWindow.SetMaximum(plotmax)
		ErrorWindow.SetMinimum(plotmin)

		ErrorWindow.Draw("a2")
		# ErrorWindow.GetXaxis().SetMinimum(presentationbinning[0])
		# ErrorWindow.GetXaxis().SetMaximum(presentationbinning[-1])
		# ErrorWindow.GetXaxis().SetRangeUser(_binning[0],_binning[-1])
		# ErrorWindow.GetXaxis().SetLimits(_binning[0],_binning[-1])

		ErrorWindow.SetMaximum(plotmax)
		ErrorWindow.SetMinimum(plotmin)
		ErrorWindow.GetXaxis().SetTitleOffset(xoffset)

		ErrorWindow.Draw("a2")
		# cpad1.Update()


		MCStack.Draw("SAME")
		MCStack.SetMinimum(plotmin)
		MCStack.SetMaximum(plotmax)
		MCStack.GetXaxis().SetTitleOffset(xoffset)
		MCStack.GetYaxis().SetTitleOffset(0.9)
		MCStack.Draw("HISTSAME")

		MCStack.SetMinimum(plotmin)
		MCStack.SetMaximum(plotmax)
		cpad1.Update()
		MCStack=BeautifyStack(MCStack,Label)

		# Draw the data.
		hs_rec_Data.Draw("EPSAME")		
		# ErrorWindow.Draw("2")

		leg = TLegend(0.69,0.58,0.9,0.82,"","brNDC");
		leg.SetTextFont(42);
		leg.SetFillColor(0);
		leg.SetBorderSize(0);
		leg.SetTextSize(.03)
		leg.AddEntry(hs_rec_Data)
		ind = -1
		for s in SM:
			ind += 1
			leg.AddEntry(SM[ind])

		leg.Draw()

		# Stamp on top
		sqrts = "#sqrt{s} = 7 TeV";
		l1=TLatex()
		l1.SetTextAlign(12)
		l1.SetTextFont(42)
		l1.SetNDC()
		l1.SetTextSize(0.05)
		l1.DrawLatex(0.18,0.92,"CMS Preliminary     "+sqrts+"      #int L = 5.0 fb^{-1}")



		gPad.RedrawAxis()
		fname = f[0].replace('.hlog','_reco.')
		print fname
		c1.Print(fname+'png')
		c1.Print(fname+'pdf')




def ParseTablesToFinalResults(WRenorm,sel):
	allfiles = glob('pyplots/*txt')
	for f in allfiles:

		if 'FINAL' in f:
			continue
		# if 'MET' in f and ('phi' in f or 'Phi' in f):
		# 	continue
		# if 'Eta_mu' not in f:
		# 	continue
		# if "Delta" not in f or 'et1' not in f:
		# 	continue
		# if 'HT' not in f : 
		# 	continue
		# if 'Count' not in f or 'pre' not in f:
		# 	continue	
		# if 'Pt_pfjet1' not in f:
		# 	continue
		print f
		# if ('Pt_pf' not in f and 'Count' not in f) and 'pre' not in f:
		# 	continue
		if 'Vert' in f:
			continue
		print '\n\nAnalyzing table: ',f
		# continue
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
		StringToFile(NormalizeTexTable(output+'TexCount.txt',4955.0), output+'TexXSec.txt',',')

		prediction_means = [pred_mean]
		prediction_errors = [pred_err]
		prediction_names = ['MADGRAPH']
		
		label = f.split('/')[-1]
		label = label.split('.')[0]
		
		quantity = ' BLANK '
		
		if label=='Pt_pfjet1':
			label = 'Leading Jet p_{T} [GeV]'
			quantity = 'p_{T}'

		if label=='Pt_muon1':
			label = 'Muon p_{T} [GeV]'
			quantity = 'p_{T}'

		if label=='Eta_muon1':
			label = 'Muon #eta '
			quantity = '#eta'

		if label=='HT_pfjets_inc1':
			label = 'H_{T} (#geq 1 jet) [GeV]'
			quantity = 'H_{T}'

		if label=='HT_pfjets_inc2':
			label = 'H_{T} (#geq 2 jet) [GeV]'
			quantity = 'H_{T}'

		if label=='HT_pfjets_inc3':
			label = 'H_{T} (#geq 3 jet) [GeV]'
			quantity = 'H_{T}'

		if label=='HT_pfjets_inc4':
			label = 'H_{T} (#geq 4 jet) [GeV]'
			quantity = 'H_{T}'						

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

		if label=='PFJet30Count_preexc':
			label = 'Jet Count (Inclusive)'
			quantity = 'N_{Jet}'

		if label=='MT_muon1METR':
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
		FinalHisto(rootbinning,label,quantity, output+'PlotXSec.', prediction_means, prediction_errors, prediction_names, meas_mean, meas_err_plus, meas_err_minus,4955.0,WRenorm,sel)
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

setTDRStyle()


main()





