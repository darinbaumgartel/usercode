import os
import sys

import math
import random
from glob import glob

# Directory where root files are kept and the tree you want to get root files from
EMuDirectory = 'NTupleAnalyzer_Jan15FullEMuSwitch_2013_01_15_15_49_18'
NormalDirectory = 'NTupleAnalyzer_JBinfirstRun_2012_12_02_20_35_32/SummaryFiles'
NormalDirectory = 'NTupleAnalyzer_MetCorrPlusSys_2012_12_19_23_03_19/SummaryFiles'
NormalDirectory = 'NTupleAnalyzer_Dec20_2012_12_20_21_44_21/SummaryFiles'
NormalDirectory = 'NTupleAnalyzer_Dec27_2012_12_28_04_31_00/SummaryFiles'
NormalDirectory = 'NTupleAnalyzer_Jan6_2013_01_08_00_09_55/SummaryFiles'
NormalDirectory = 'NTupleAnalyzer_Jan11_2013_01_11_23_03_26/SummaryFiles'
NormalDirectory = 'NTupleAnalyzer_Jan14_2013_01_14_04_55_43/SummaryFiles'
NormalDirectory = 'NTupleAnalyzer_Jan14Full_2013_01_14_21_23_01/SummaryFiles'

TreeName = "PhysicalVariables"


lumi = 19600.0


singlemuHLT =  '*( 0.94*(abs(Eta_muon1)<=0.9) + 0.84*(abs(Eta_muon1)>0.9)*(abs(Eta_muon1)<=1.2) + 0.82*(abs(Eta_muon1)>1.2)*(abs(Eta_muon1)<=2.1) )'
doublemuHLT =  '*(1.0-(( 1.0 - 0.94*(abs(Eta_muon1)<=0.9) - 0.84*(abs(Eta_muon1)>0.9)*(abs(Eta_muon1)<=1.2) - 0.82*(abs(Eta_muon1)>1.2)*(abs(Eta_muon1)<=2.1) )'
doublemuHLT += '*( 1.0 - 0.94*(abs(Eta_muon2)<=0.9) - 0.84*(abs(Eta_muon2)>0.9)*(abs(Eta_muon2)<=1.2) - 0.82*(abs(Eta_muon2)>1.2)*(abs(Eta_muon2)<=2.1) )))'


NormalWeightMuMu = str(lumi)+'*weight_central'+doublemuHLT
NormalWeightMuNu = str(lumi)+'*weight_central'+singlemuHLT
# NormalWeightMuNu += '*( 0.0  + 1.036*(Phi_miss>-3.142)*(Phi_miss<=-2.9) + 1.055*(Phi_miss>-2.9)*(Phi_miss<=-2.658) + 1.061*(Phi_miss>-2.658)*(Phi_miss<=-2.417) + 0.998*(Phi_miss>-2.417)*(Phi_miss<=-2.175) + 1.017*(Phi_miss>-2.175)*(Phi_miss<=-1.933) + 1.016*(Phi_miss>-1.933)*(Phi_miss<=-1.692) + 0.971*(Phi_miss>-1.692)*(Phi_miss<=-1.45) + 1.044*(Phi_miss>-1.45)*(Phi_miss<=-1.208) + 1.009*(Phi_miss>-1.208)*(Phi_miss<=-0.967) + 1.079*(Phi_miss>-0.967)*(Phi_miss<=-0.725) + 1.03*(Phi_miss>-0.725)*(Phi_miss<=-0.483) + 0.961*(Phi_miss>-0.483)*(Phi_miss<=-0.242) + 1.019*(Phi_miss>-0.242)*(Phi_miss<=0.0) + 1.011*(Phi_miss>0.0)*(Phi_miss<=0.242) + 0.968*(Phi_miss>0.242)*(Phi_miss<=0.483) + 0.976*(Phi_miss>0.483)*(Phi_miss<=0.725) + 0.953*(Phi_miss>0.725)*(Phi_miss<=0.967) + 0.996*(Phi_miss>0.967)*(Phi_miss<=1.208) + 0.965*(Phi_miss>1.208)*(Phi_miss<=1.45) + 0.973*(Phi_miss>1.45)*(Phi_miss<=1.692) + 0.958*(Phi_miss>1.692)*(Phi_miss<=1.933) + 1.048*(Phi_miss>1.933)*(Phi_miss<=2.175) + 0.975*(Phi_miss>2.175)*(Phi_miss<=2.417) + 0.932*(Phi_miss>2.417)*(Phi_miss<=2.658) + 0.967*(Phi_miss>2.658)*(Phi_miss<=2.9) + 1.003*(Phi_miss>2.9)*(Phi_miss<=3.142))'
NormalWeightEMu = str(lumi)+'*weight_central'+singlemuHLT

dataHLT = '*(pass_HLTMu40_eta2p1)'

passfilter =  '*(passDataCert*passPrimaryVertex)'
passfilter += '*(passBeamScraping*passPhysDeclared*passBeamHalo*passHBHENoiseFilter*passTrackingFailure)'
# passfilter += '*(passEcalDeadCellBE*passEcalDeadCellTP*passBadEESuperCrystal*passEcalLaserCorr*passHcalLaserEvent)'
passfilter += '*(passEcalDeadCellBE*passEcalDeadCellTP*passBadEESuperCrystal*passHcalLaserEvent)'
# passEcalLaserCorr is bad in data
preselectionmumu = '((Pt_muon1>45)*(Pt_muon2>45)*(Pt_jet1>125)*(Pt_jet2>45)*(St_uujj>300)*(M_uu>50)*(DR_muon1muon2>0.3))'
# preselectionmunu = '((Pt_muon1>45)*(Pt_muon2<45.0)*(Pt_miss>55)*(Pt_jet1>125)*(Pt_jet2>45)*(Pt_ele1<45.0)*(St_uvjj>300)*(DPhi_muon1met>0.8)*(DPhi_jet1met>0.3)*(DPhi_jet2met>0.3)*(MT_uv>50.0))'
preselectionmunu = '((Pt_muon1>45)*(Pt_muon2<45.0)*(Pt_miss>55)*(Pt_jet1>125)*(Pt_jet2>45)*(Pt_ele1<45.0)*(St_uvjj>300)*(DPhi_muon1met>0.8)*(DPhi_jet1met>0.5)*(MT_uv>50.0))'

preselectionmumu+=passfilter
preselectionmunu+=passfilter

##########################################################################
########      Put all uses of the plotting funcs into main()      ########
##########################################################################



def main():


	ptbinning = [40,60]
	ptbinning2 = [40,60]
	metbinning2 = [0,5]

	stbinning = [250,275]
	bosonbinning = [50,60,70,80,90,100,110,120]
	bosonzoombinning_uujj_Z = [30,75,105]
	bosonzoombinning_uujj_TT = [95,100]
	metzoombinning_uujj_TT = [95,100]
	metzoombinning_uujj_Z = [0,5,10,15,22,30,40,55,75,100]

	bosonzoombinning_uvjj = [50,65,115]


	lqbinning = [50,60]
	etabinning = [26,-2.6,2.6]
	drbinning = [35,0,7]
	phibinning = [26,-3.1416,3.1416]
	dphibinning = [64,0,3.2]

	for x in range(40):
		if ptbinning[-1] < 1500:
			ptbinning.append(ptbinning[-1]+(ptbinning[-1] - ptbinning[-2])*1.2)
		if ptbinning2[-1] < 700:
			ptbinning2.append(ptbinning2[-1]+(ptbinning2[-1] - ptbinning2[-2])*1.2)
		if metbinning2[-1] < 700:
			metbinning2.append(metbinning2[-1]+(metbinning2[-1] - metbinning2[-2])*1.2)		
		if stbinning[-1] < 3200:
			stbinning.append(stbinning[-1]+(stbinning[-1] - stbinning[-2])*1.2)
		if bosonbinning[-1]<1000:
			bosonbinning.append(bosonbinning[-1]+ (bosonbinning[-1] - bosonbinning[-2])*1.2 )
		if lqbinning[-1]<2000:
			lqbinning.append(lqbinning[-1]+(lqbinning[-1] - lqbinning[-2])*1.1)
		if bosonzoombinning_uujj_TT[-1] < 900:
			bosonzoombinning_uujj_TT.append(bosonzoombinning_uujj_TT[-1] + (bosonzoombinning_uujj_TT[-1] - bosonzoombinning_uujj_TT[-2])*1.25)			
		if metzoombinning_uujj_TT[-1] < 900:
			metzoombinning_uujj_TT.append(metzoombinning_uujj_TT[-1] + (metzoombinning_uujj_TT[-1] - metzoombinning_uujj_TT[-2])*1.4)		
	# 	if metzoombinning_uujj_Z[-1] < 110:
	# 		metzoombinning_uujj_Z.append(metzoombinning_uujj_Z[-1]+4*(x+1))

	# print metzoombinning_uujj_Z
	# sys.exit()
	# print bosonbinning
	# ptbinning = [50,0,1000]
	# stbinning = [50,0,2500]
	# bosonbinning = [50,50,550]
	# lqbinning = [50,150,1650]
	vbinning = [60,0,60]
	nbinning = [10,0,10]


	# [tpscale,tperror] = MuonTPStudy()

	# sys.exit()

	# UpdateFilesWithMVA(NormalDirectory,['Pt_jet1','Pt_jet2','M_muon1muon2','Pt_muon1','Pt_muon2'])
	# exit()

	# PrintRuns()
	# exit()

	# quickplottest(version_name)
	# sys.exit()

	# version_name = 'Testing_highpt'
	# os.system('mkdir Results_'+version_name)

	# [[Rz_uujj,Rz_uujj_err],[Rtt_uujj,Rtt_uujj_err]] = GetMuMuScaleFactors( NormalWeightMuMu+'*'+preselectionmumu, NormalDirectory, '(M_uu>80)*(M_uu<100)', '(M_uu>100)*(Pt_miss>60)')
	# [[Rw_uvjj,Rw_uvjj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( NormalWeightMuNu+'*'+preselectionmunu, NormalDirectory, '(MT_uv>60)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>60)*(MT_uv<110)*(JetCount>3.5)')


	# MuMuOptCutFile = OptimizeCuts3D(['St_uujj:250:10:1900','M_uujj2:100:10:1900','M_uu:120:10:330'],preselectionmumu,NormalWeightMuMu,version_name,[Rz_uujj,Rtt_uujj,Rw_uvjj],'','uujj')
	# MuNuOptCutFile = OptimizeCuts3D(['St_uvjj:250:10:1900','M_uvjj:100:10:1900','MT_uv:120:10:330'],preselectionmunu,NormalWeightMuNu,version_name,[Rz_uujj,Rtt_uvjj,Rw_uvjj],'','uvjj')


	# version_name = 'Testing_lowpt'
	# os.system('mkdir Results_'+version_name)

	# [[Rz_uujj,Rz_uujj_err],[Rtt_uujj,Rtt_uujj_err]] = GetMuMuScaleFactors( NormalWeightMuMu+'*'+preselectionmumu_lightjet, NormalDirectory, '(M_uu>80)*(M_uu<100)', '(M_uu>100)*(Pt_miss>60)')
	# [[Rw_uvjj,Rw_uvjj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( NormalWeightMuNu+'*'+preselectionmunu_lightjet, NormalDirectory, '(MT_uv>60)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>60)*(MT_uv<110)*(JetCount>3.5)')

	# # MuMuOptCutFile = OptimizeCuts3D(['St_uujj:250:10:1900','M_uujj2:100:10:1900','M_uu:120:10:330'],preselectionmumu_lightjet,NormalWeightMuMu,version_name,[Rz_uujj,Rtt_uujj,Rw_uvjj],'','uujj')
	# MuNuOptCutFile = OptimizeCuts3D(['St_uvjj:250:10:1900','M_uvjj:100:10:1900','MT_uv:120:10:330'],preselectionmunu_lightjet,NormalWeightMuNu,version_name,[Rz_uujj,Rtt_uvjj,Rw_uvjj],'','uvjj')


	# sys.exit()


	# WITH PRE-EXISTING LOGS

	# version_name = 'Testing_highpt'
	# os.system('mkdir Results_'+version_name)

	# ReDoOptFits('Results_Testing_highpt/Opt_uujjCuts.txt')
	# ReDoOptFits('Results_Testing_highpt/Opt_uvjjCuts.txt')
	# ReDoOptFits('Results_Testing_lowpt/Opt_uujjCuts.txt')
	# ReDoOptFits('Results_Testing_lowpt/Opt_uvjjCuts.txt')


	# [[Rz_uujj,Rz_uujj_err],[Rtt_uujj,Rtt_uujj_err]] = GetMuMuScaleFactors( NormalWeightMuMu+'*'+preselectionmumu, NormalDirectory, '(M_uu>80)*(M_uu<100)', '(M_uu>100)*(Pt_miss>60)')
	# [[Rw_uvjj,Rw_uvjj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( NormalWeightMuNu+'*'+preselectionmunu, NormalDirectory, '(MT_uv>60)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>60)*(MT_uv<110)*(JetCount>3.5)')


	# MuMuOptCutFile = OptimizeCuts3D(['St_uujj:250:10:1900','M_uujj2:100:10:1900','M_uu:120:10:330'],preselectionmumu,NormalWeightMuMu,version_name,[Rz_uujj,Rtt_uujj,Rw_uvjj],'Results_Testing_highpt/Log_uujjCuts.txt','uujj')
	# MuNuOptCutFile = OptimizeCuts3D(['St_uvjj:250:10:1900','M_uvjj:100:10:1900','MT_uv:120:10:330'],preselectionmunu,NormalWeightMuNu,version_name,[Rz_uujj,Rtt_uvjj,Rw_uvjj],'Results_Testing_highpt/Log_uvjjCuts.txt','uvjj')


	# version_name = 'Testing_lowpt'
	# os.system('mkdir Results_'+version_name)

	# [[Rz_uujj,Rz_uujj_err],[Rtt_uujj,Rtt_uujj_err]] = GetMuMuScaleFactors( NormalWeightMuMu+'*'+preselectionmumu_lightjet, NormalDirectory, '(M_uu>80)*(M_uu<100)', '(M_uu>100)*(Pt_miss>60)')
	# [[Rw_uvjj,Rw_uvjj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( NormalWeightMuNu+'*'+preselectionmunu_lightjet, NormalDirectory, '(MT_uv>60)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>60)*(MT_uv<110)*(JetCount>3.5)')

	# MuMuOptCutFile = OptimizeCuts3D(['St_uujj:250:10:1900','M_uujj2:100:10:1900','M_uu:120:10:330'],preselectionmumu_lightjet,NormalWeightMuMu,version_name,[Rz_uujj,Rtt_uujj,Rw_uvjj],'Results_Testing_lowpt/Log_uujjCuts.txt','uujj')
	# MuNuOptCutFile = OptimizeCuts3D(['St_uvjj:250:10:1900','M_uvjj:100:10:1900','MT_uv:120:10:330'],preselectionmunu_lightjet,NormalWeightMuNu,version_name,[Rz_uujj,Rtt_uvjj,Rw_uvjj],'Results_Testing_lowpt/Log_uvjjCuts.txt','uvjj')


	# sys.exit()




	# [[Rw_uvjj,Rw_uvjj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( NormalWeightMuNu+'*'+preselectionmunu, NormalDirectory, '(MT_uv>60)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>60)*(MT_uv<110)*(JetCount>3.5)')
	# CreateMuMuBDTs(['Pt_jet1','Pt_jet2','M_muon1muon2','Pt_muon1','Pt_muon2'],preselectionmumu,NormalWeightMuMu,NormalDirectory,Rz_uujj, Rw_uvjj,Rtt_uujj)

	# MuMuOptCutFile = 'cuttest.txt'
	# QuickTable(MuMuOptCutFile, preselectionmumu,NormalWeightMuMu,1.0,1.0,1.0)

	# GetMuMuScaleFactors( NormalWeightMuMu+'*'+preselectionmumu_lightjet, NormalDirectory, '(M_uu>80)*(M_uu<100)', '(M_uu>100)*(Pt_miss>60)')
	# GetMuNuScaleFactors( NormalWeightMuNu+'*'+preselectionmunu_lightjet, NormalDirectory, '(MT_uv>60)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>60)*(MT_uv<110)*(JetCount>3.5)')

	# print ' ------------ '

	# version_name = 'Testing_Dec27'
	# os.system('mkdir Results_'+version_name)

	# [[Rz_uujj,Rz_uujj_err],[Rtt_uujj,Rtt_uujj_err]] = GetMuMuScaleFactors( NormalWeightMuMu+'*'+preselectionmumu, NormalDirectory, '(M_uu>70)*(M_uu<110)*(Pt_miss<100)', '(M_uu>100)*(Pt_miss>=100)')
	# [[Rw_uvjj,Rw_uvjj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( NormalWeightMuNu+'*'+preselectionmunu, NormalDirectory, '(MT_uv>70)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>70)*(MT_uv<110)*(JetCount>3.5)')

	# MuMuOptCutFile = 'Results_Testing_highpt/Opt_uujjCuts_Smoothed_pol2cutoff.txt'
	# MuNuOptCutFile = 'Results_Testing_highpt/Opt_uvjjCuts_Smoothed_pol2cutoff.txt'



	# [[Rz_uujj,Rz_uujj_err],[Rtt_uujj,Rtt_uujj_err]] = GetMuMuScaleFactors( NormalWeightMuMu+'*'+preselectionmumu_lightjet, NormalDirectory, '(M_uu>80)*(M_uu<100)', '(M_uu>100)*(Pt_miss>60)')
	# [[Rw_uvjj,Rw_uvjj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( NormalWeightMuNu+'*'+preselectionmunu_lightjet, NormalDirectory, '(MT_uv>60)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>60)*(MT_uv<110)*(JetCount>3.5)')
	
	# uujjcards = ParseFinalCards('Results_Testing_Dec27/Opt_uujjCuts_Smoothed_pol2cutoff_systable*.txt')
	# uvjjcards = ParseFinalCards('Results_Testing_Dec27/Opt_uvjjCuts_Smoothed_pol2cutoff_systable*.txt')

	# print uujjcards
	# print uvjjcards
	# finalcards = FixFinalCards([uujjcards,uvjjcards])
	# print finalcards

	# sys.exit()

	# QuickTable('Results_Testing_lowpt/Opt_uujjCuts_Smoothed_pol2cutoff.txt', preselectionmumu_lightjet,NormalWeightMuMu,Rz_uujj, Rw_uvjj,Rtt_uujj)
	# QuickTable('Results_Testing_lowpt/Opt_uvjjCuts_Smoothed_pol2cutoff.txt', preselectionmunu_lightjet,NormalWeightMuNu,Rz_uujj, Rw_uvjj,Rtt_uvjj)

	# SysTable('Results_Testing_Dec27/Opt_uvjjCuts_Smoothed_pol2cutoff.txt', preselectionmunu,NormalWeightMuNu,0.85, 0.85,0.85,'')
	# FullAnalysis('Results_Testing_Dec27/Opt_uujjCuts_Smoothed_pol2cutoff.txt', preselectionmumu,preselectionmunu,NormalDirectory,NormalWeightMuMu)
	# FullAnalysis('Results_Testing_Dec27/Opt_uvjjCuts_Smoothed_pol2cutoff.txt', preselectionmumu,preselectionmunu,NormalDirectory,NormalWeightMuNu)




	############################################################
    ##############     STANDARD PLOT ROUTINES    ###############
	############################################################

	version_name = 'Testing_Jan14Full' # scriptflag
	os.system('mkdir Results_'+version_name) 

	MuMuOptCutFile = 'Results_Testing_Jan14Full/Opt_uujjCuts_Smoothed_pol2cutoff.txt' # scriptflag
	MuNuOptCutFile = 'Results_Testing_Jan14Full/Opt_uvjjCuts_Smoothed_pol2cutoff.txt' # scriptflag

	if (False):
		scalefacs = []
		minselectionmumu = '((Pt_muon1>45)*(Pt_muon2>45)*(M_uu>50)*(DR_muon1muon2>0.3))'
		minselectionmunu = '((Pt_muon1>45)*(Pt_muon2<45.0)*(Pt_miss>55)*(Pt_ele1<45.0)*(DPhi_muon1met>0.8)*(MT_uv>50.0))'
		minselectionmumu+=passfilter
		minselectionmunu+=passfilter		

		scalefacs.append('Selection & $R_Z$ & $R_{t \\bar{t}} & R_W & $R_{t \\bar{t}} \\\hline')
		[[Rz_uujj,Rz_uujj_err],[Rtt_uujj,Rtt_uujj_err]] = GetMuMuScaleFactors( NormalWeightMuMu+'*'+minselectionmumu, NormalDirectory, '(M_uu>80)*(M_uu<100)*(Pt_miss<100)', '(M_uu>100)*(Pt_miss>=100)')
		[[Rw_uvjj,Rw_uvjj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( NormalWeightMuNu+'*'+minselectionmunu, NormalDirectory, '(MT_uv>70)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>70)*(MT_uv<110)*(JetCount>3.5)')
		Rz_uujj = str(round(Rz_uujj,3)) + ' $\\pm$ ' + str(round(Rz_uujj_err,3))	
		Rtt_uujj = str(round(Rtt_uujj,3)) + ' $\\pm$ ' + str(round(Rtt_uujj_err,3))	
		Rw_uvjj = str(round(Rw_uvjj,3)) + ' $\\pm$ ' + str(round(Rw_uvjj_err,3))	
		Rtt_uvjj = str(round(Rtt_uvjj,3)) + ' $\\pm$ ' + str(round(Rtt_uvjj_err,3))	
		scalefacs.append('No Jet Req & ' + str(Rz_uujj)+' & '+str(Rtt_uujj)+' & '+str(Rw_uvjj)+' & '+str(Rtt_uvjj)+' \\\\')

		minselectionmumu += '*(Pt_jet1>45.0)'
		minselectionmunu += '*(Pt_jet1>45.0)*(DPhi_jet1met>0.5)'
		[[Rz_uujj,Rz_uujj_err],[Rtt_uujj,Rtt_uujj_err]] = GetMuMuScaleFactors( NormalWeightMuMu+'*'+minselectionmumu, NormalDirectory, '(M_uu>80)*(M_uu<100)*(Pt_miss<100)', '(M_uu>100)*(Pt_miss>=100)')
		[[Rw_uvjj,Rw_uvjj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( NormalWeightMuNu+'*'+minselectionmunu, NormalDirectory, '(MT_uv>70)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>70)*(MT_uv<110)*(JetCount>3.5)')		
		Rz_uujj = str(round(Rz_uujj,3)) + ' $\\pm$ ' + str(round(Rz_uujj_err,3))	
		Rtt_uujj = str(round(Rtt_uujj,3)) + ' $\\pm$ ' + str(round(Rtt_uujj_err,3))	
		Rw_uvjj = str(round(Rw_uvjj,3)) + ' $\\pm$ ' + str(round(Rw_uvjj_err,3))	
		Rtt_uvjj = str(round(Rtt_uvjj,3)) + ' $\\pm$ ' + str(round(Rtt_uvjj_err,3))	
		scalefacs.append('$1^{st}$ Jet $>$ 45 GeV & ' + str(Rz_uujj)+' & '+str(Rtt_uujj)+' & '+str(Rw_uvjj)+' & '+str(Rtt_uvjj)+' \\\\')

		minselectionmumu += '*(Pt_jet2>45.0)'
		minselectionmunu += '*(Pt_jet2>45.0)'
		[[Rz_uujj,Rz_uujj_err],[Rtt_uujj,Rtt_uujj_err]] = GetMuMuScaleFactors( NormalWeightMuMu+'*'+minselectionmumu, NormalDirectory, '(M_uu>80)*(M_uu<100)*(Pt_miss<100)', '(M_uu>100)*(Pt_miss>=100)')
		[[Rw_uvjj,Rw_uvjj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( NormalWeightMuNu+'*'+minselectionmunu, NormalDirectory, '(MT_uv>70)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>70)*(MT_uv<110)*(JetCount>3.5)')		
		Rz_uujj = str(round(Rz_uujj,3)) + ' $\\pm$ ' + str(round(Rz_uujj_err,3))	
		Rtt_uujj = str(round(Rtt_uujj,3)) + ' $\\pm$ ' + str(round(Rtt_uujj_err,3))	
		Rw_uvjj = str(round(Rw_uvjj,3)) + ' $\\pm$ ' + str(round(Rw_uvjj_err,3))	
		Rtt_uvjj = str(round(Rtt_uvjj,3)) + ' $\\pm$ ' + str(round(Rtt_uvjj_err,3))	
		scalefacs.append('$2^{nd}$ Jet $>$ 45 GeV & ' + str(Rz_uujj)+' & '+str(Rtt_uujj)+' & '+str(Rw_uvjj)+' & '+str(Rtt_uvjj)+' \\\\')

		minselectionmumu += '*(Pt_jet1>125.0)'
		minselectionmunu += '*(Pt_jet1>125.0)'
		[[Rz_uujj,Rz_uujj_err],[Rtt_uujj,Rtt_uujj_err]] = GetMuMuScaleFactors( NormalWeightMuMu+'*'+minselectionmumu, NormalDirectory, '(M_uu>80)*(M_uu<100)*(Pt_miss<100)', '(M_uu>100)*(Pt_miss>=100)')
		[[Rw_uvjj,Rw_uvjj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( NormalWeightMuNu+'*'+minselectionmunu, NormalDirectory, '(MT_uv>70)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>70)*(MT_uv<110)*(JetCount>3.5)')		
		Rz_uujj = str(round(Rz_uujj,3)) + ' $\\pm$ ' + str(round(Rz_uujj_err,3))	
		Rtt_uujj = str(round(Rtt_uujj,3)) + ' $\\pm$ ' + str(round(Rtt_uujj_err,3))	
		Rw_uvjj = str(round(Rw_uvjj,3)) + ' $\\pm$ ' + str(round(Rw_uvjj_err,3))	
		Rtt_uvjj = str(round(Rtt_uvjj,3)) + ' $\\pm$ ' + str(round(Rtt_uvjj_err,3))	
		scalefacs.append('$1^{st}$ Jet $>$ 125 GeV & ' + str(Rz_uujj)+' & '+str(Rtt_uujj)+' & '+str(Rw_uvjj)+' & '+str(Rtt_uvjj)+' \\\\')


		minselectionmumu += '*(St_uujj>300.0)'
		minselectionmunu += '*(St_uvjj>300.0)'
		[[Rz_uujj,Rz_uujj_err],[Rtt_uujj,Rtt_uujj_err]] = GetMuMuScaleFactors( NormalWeightMuMu+'*'+minselectionmumu, NormalDirectory, '(M_uu>80)*(M_uu<100)*(Pt_miss<100)', '(M_uu>100)*(Pt_miss>=100)')
		[[Rw_uvjj,Rw_uvjj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( NormalWeightMuNu+'*'+minselectionmunu, NormalDirectory, '(MT_uv>70)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>70)*(MT_uv<110)*(JetCount>3.5)')		
		Rz_uujj = str(round(Rz_uujj,3)) + ' $\\pm$ ' + str(round(Rz_uujj_err,3))	
		Rtt_uujj = str(round(Rtt_uujj,3)) + ' $\\pm$ ' + str(round(Rtt_uujj_err,3))	
		Rw_uvjj = str(round(Rw_uvjj,3)) + ' $\\pm$ ' + str(round(Rw_uvjj_err,3))	
		Rtt_uvjj = str(round(Rtt_uvjj,3)) + ' $\\pm$ ' + str(round(Rtt_uvjj_err,3))	
		scalefacs.append('$S_T>300$ GeV & ' + str(Rz_uujj)+' & '+str(Rtt_uujj)+' & '+str(Rw_uvjj)+' & '+str(Rtt_uvjj)+' \\\\')

		f = open('Results_'+version_name+'/ScaleFactorStudy.txt','w')
		for s in scalefacs:
			f.write(s+'\n')
		f.close()


	if (True):
		# Get Scale Factors
		[[Rz_uujj,Rz_uujj_err],[Rtt_uujj,Rtt_uujj_err]] = GetMuMuScaleFactors( NormalWeightMuMu+'*'+preselectionmumu, NormalDirectory, '(M_uu>80)*(M_uu<100)*(Pt_miss<100)', '(M_uu>100)*(Pt_miss>=100)')
		[[Rw_uvjj,Rw_uvjj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( NormalWeightMuNu+'*'+preselectionmunu, NormalDirectory, '(MT_uv>70)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>70)*(MT_uv<110)*(JetCount>3.5)')


		# Control Region Plots
		MakeBasicPlot("M_uu","M^{#mu #mu} [GeV]",bosonzoombinning_uujj_Z,preselectionmumu+'*(M_uu>80)*(M_uu<100)*(Pt_miss<100)',NormalWeightMuMu,NormalDirectory,'controlzoom_ZRegion','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Pt_miss","E_{T}^{miss} [GeV]",metzoombinning_uujj_Z,preselectionmumu+'*(M_uu>80)*(M_uu<100)*(Pt_miss<100)',NormalWeightMuMu,NormalDirectory,'controlzoomZRegion','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("M_uu","M^{#mu #mu} [GeV]",bosonzoombinning_uujj_TT,preselectionmumu+'*(M_uu>100)*(Pt_miss>=100)',NormalWeightMuMu,NormalDirectory,'controlzoom_TTRegion','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Pt_miss","E_{T}^{miss} [GeV]",metzoombinning_uujj_TT,preselectionmumu+'*(M_uu>100)*(Pt_miss>=100)',NormalWeightMuMu,NormalDirectory,'controlzoomTTRegion','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)

		MakeBasicPlot("MT_uv","M_{T}^{#mu #nu} [GeV]",bosonzoombinning_uvjj,preselectionmunu+'*(MT_uv>70)*(MT_uv<110)*(JetCount<3.5)',NormalWeightMuNu,NormalDirectory,'controlzoom_WRegion','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("MT_uv","M_{T}^{#mu #nu} [GeV]",bosonzoombinning_uvjj,preselectionmunu+'*(MT_uv>70)*(MT_uv<110)*(JetCount>3.5)',NormalWeightMuNu,NormalDirectory,'controlzoom_TTRegion','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)


		# # PreSelection Plots
		MakeBasicPlot("Pt_jet1","p_{T}(jet_{1}) [GeV]",ptbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Pt_jet2","p_{T}(jet_{2}) [GeV]",ptbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Pt_muon1","p_{T}(#mu_{1}) [GeV]",ptbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Pt_muon2","p_{T}(#mu_{2}) [GeV]",ptbinning2,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Pt_miss","E_{T}^{miss} [GeV]",metbinning2,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Eta_jet1","#eta(jet_{1}) [GeV]",etabinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Eta_jet2","#eta(jet_{2}) [GeV]",etabinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Eta_muon1","#eta(#mu_{1}) [GeV]",etabinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Eta_muon2","#eta(#mu_{2}) [GeV]",etabinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)	
		MakeBasicPlot("Phi_jet1","#phi(jet_{1}) [GeV]",phibinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Phi_jet2","#phi(jet_{2}) [GeV]",phibinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Phi_muon1","#phi(#mu_{1}) [GeV]",phibinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Phi_muon2","#phi(#mu_{2}) [GeV]",phibinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)	
		MakeBasicPlot("St_uujj","S_{T}^{#mu #mu j j} [GeV]",stbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("M_uu","M^{#mu #mu} [GeV]",bosonbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("MH_uujj","M^{#mu j} (lead jet combo) [GeV]",lqbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("M_uujj1","M^{#mu j}_{1} [GeV]",lqbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("M_uujj2","M^{#mu j}_{2} [GeV]",lqbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("GoodVertexCount","N_{Vertices}",vbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("JetCount","N_{jet}",nbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("MuonCount","N_{#mu}",nbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("ElectronCount","N_{e}",nbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DR_muon1muon2","#DeltaR(#mu_{1},#mu_{2})",drbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DR_muon1jet1","#DeltaR(#mu_{1},j_{1})",drbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DR_muon1jet2","#DeltaR(#mu_{1},j_{2})",drbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DR_muon2jet1","#DeltaR(#mu_{2},j_{1})",drbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DR_muon2jet2","#DeltaR(#mu_{2},j_{2})",drbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DPhi_muon1met","#Delta #phi (#mu_{1},E_{T}^{miss})",dphibinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DPhi_jet1met","#Delta #phi(j_{1},E_{T}^{miss})",dphibinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DPhi_jet2met","#Delta #phi(j_{2},E_{T}^{miss})",dphibinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'standard','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)


		MakeBasicPlot("Pt_jet1","p_{T}(jet_{1}) [GeV]",ptbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Pt_jet2","p_{T}(jet_{2}) [GeV]",ptbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Pt_muon1","p_{T}(#mu_{1}) [GeV]",ptbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Pt_miss","E_{T}^{miss} [GeV]",ptbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Eta_jet1","#eta(jet_{1}) [GeV]",etabinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Eta_jet2","#eta(jet_{2}) [GeV]",etabinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Eta_muon1","#eta(#mu_{1}) [GeV]",etabinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Phi_jet1","#phi(jet_{1}) [GeV]",phibinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Phi_jet2","#phi(jet_{2}) [GeV]",phibinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Phi_muon1","#phi(#mu_{1}) [GeV]",phibinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Phi_miss","#phi^{miss} [GeV]",phibinning,preselectionmunu+'',NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("St_uvjj","S_{T}^{#mu #nu j j} [GeV]",stbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("MT_uv","M_{T}^{#mu #nu} [GeV]",bosonbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("MT_uvjj","M_{T}^{#mu j} [GeV]",lqbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("M_uvjj","M^{#mu j} [GeV]",lqbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("MH_uvjj","M^{#mu j} (lead jet only) [GeV]",lqbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("GoodVertexCount","N_{Vertices}",vbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("JetCount","N_{jet}",nbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("MuonCount","N_{#mu}",nbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("ElectronCount","N_{e}",nbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("DPhi_muon1met","#Delta #phi (#mu_{1},E_{T}^{miss})",dphibinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("DPhi_jet1met","#Delta #phi(j_{1},E_{T}^{miss})",dphibinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("DPhi_jet2met","#Delta #phi(j_{2},E_{T}^{miss})",dphibinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("DR_muon1jet1","#DeltaR(#mu_{1},j_{1})",drbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("DR_muon1jet2","#DeltaR(#mu_{1},j_{2})",drbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'standard','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)


		# Full Selection Plots
		for lqmass in [300,400,450,500,600,700,900]:

			MakeBasicPlot("St_uujj","S_{T}^{#mu #mu j j} [GeV]",stbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'final','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,MuMuOptCutFile,version_name,lqmass)
			MakeBasicPlot("M_uu","M^{#mu #mu} [GeV]",bosonbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'final','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,MuMuOptCutFile,version_name,lqmass)
			MakeBasicPlot("M_uujj2","M^{#mu j}_{2} [GeV]",lqbinning,preselectionmumu,NormalWeightMuMu,NormalDirectory,'final','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,MuMuOptCutFile,version_name,lqmass)
			MakeBasicPlot("St_uvjj","S_{T}^{#mu #nu j j} [GeV]",stbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'final','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,MuNuOptCutFile,version_name,lqmass)
			MakeBasicPlot("MT_uv","M_{T}^{#mu #nu} [GeV]",bosonbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'final','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,MuNuOptCutFile,version_name,lqmass)
			MakeBasicPlot("M_uvjj","M^{#mu j} [GeV]",lqbinning,preselectionmunu,NormalWeightMuNu,NormalDirectory,'final','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,MuNuOptCutFile,version_name,lqmass)


		# PreSelection + boson cut Plots

		highstselectionmumu = preselectionmumu+ '*(M_uu>100.0)'
		highstselectionmunu = preselectionmunu+ '*(MT_uv>110.0)'

		MakeBasicPlot("Pt_jet1","p_{T}(jet_{1}) [GeV]",ptbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Pt_jet2","p_{T}(jet_{2}) [GeV]",ptbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Pt_muon1","p_{T}(#mu_{1}) [GeV]",ptbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Pt_muon2","p_{T}(#mu_{2}) [GeV]",ptbinning2,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Pt_miss","E_{T}^{miss} [GeV]",metbinning2,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Eta_jet1","#eta(jet_{1}) [GeV]",etabinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Eta_jet2","#eta(jet_{2}) [GeV]",etabinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Eta_muon1","#eta(#mu_{1}) [GeV]",etabinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Eta_muon2","#eta(#mu_{2}) [GeV]",etabinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)	
		MakeBasicPlot("Phi_jet1","#phi(jet_{1}) [GeV]",phibinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Phi_jet2","#phi(jet_{2}) [GeV]",phibinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Phi_muon1","#phi(#mu_{1}) [GeV]",phibinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Phi_muon2","#phi(#mu_{2}) [GeV]",phibinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)	
		MakeBasicPlot("St_uujj","S_{T}^{#mu #mu j j} [GeV]",stbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("M_uu","M^{#mu #mu} [GeV]",bosonbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("MH_uujj","M^{#mu j} (lead jet combo) [GeV]",lqbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("M_uujj1","M^{#mu j}_{1} [GeV]",lqbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("M_uujj2","M^{#mu j}_{2} [GeV]",lqbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("GoodVertexCount","N_{Vertices}",vbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("JetCount","N_{jet}",nbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("MuonCount","N_{#mu}",nbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("ElectronCount","N_{e}",nbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DR_muon1muon2","#DeltaR(#mu_1,#mu_2)",drbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DR_muon1jet1","#DeltaR(#mu_1,j_1)",drbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DR_muon1jet2","#DeltaR(#mu_1,j_2)",drbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DR_muon2jet1","#DeltaR(#mu_2,j_1)",drbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DR_muon2jet2","#DeltaR(#mu_2,j_2)",drbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'bosoncut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)

		MakeBasicPlot("Pt_jet1","p_{T}(jet_{1}) [GeV]",ptbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Pt_jet2","p_{T}(jet_{2}) [GeV]",ptbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Pt_muon1","p_{T}(#mu_{1}) [GeV]",ptbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Pt_miss","E_{T}^{miss} [GeV]",ptbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Eta_jet1","#eta(jet_{1}) [GeV]",etabinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Eta_jet2","#eta(jet_{2}) [GeV]",etabinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Eta_muon1","#eta(#mu_{1}) [GeV]",etabinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Phi_jet1","#phi(jet_{1}) [GeV]",phibinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Phi_jet2","#phi(jet_{2}) [GeV]",phibinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Phi_muon1","#phi(#mu_{1}) [GeV]",phibinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Phi_miss","#phi^{miss} [GeV]",phibinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("St_uvjj","S_{T}^{#mu #nu j j} [GeV]",stbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("MT_uv","M_{T}^{#mu #nu} [GeV]",bosonbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("MT_uvjj","M_{T}^{#mu j} [GeV]",lqbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("M_uvjj","M^{#mu j} [GeV]",lqbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("MH_uvjj","M^{#mu j} (lead jet only) [GeV]",lqbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("GoodVertexCount","N_{Vertices}",vbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("JetCount","N_{jet}",nbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("MuonCount","N_{#mu}",nbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("ElectronCount","N_{e}",nbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("DPhi_muon1met","#Delta #phi (#mu_{1},E_{T}^{miss})",dphibinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("DPhi_jet1met","#Delta #phi(j_{1},E_{T}^{miss})",dphibinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("DPhi_jet2met","#Delta #phi(j_{2},E_{T}^{miss})",dphibinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("DR_muon1jet1","#DeltaR(#mu_1,j_1)",drbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("DR_muon1jet2","#DeltaR(#mu_1,j_2)",drbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'bosoncut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)




		# PreSelection + boson cut Plots

		highstselectionmumu = preselectionmumu+ '*(M_uu>100.0)*(St_uujj>500.0)'
		highstselectionmunu = preselectionmunu+ '*(MT_uv>110.0)*(St_uvjj>500.0)'

		MakeBasicPlot("Pt_jet1","p_{T}(jet_{1}) [GeV]",ptbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Pt_jet2","p_{T}(jet_{2}) [GeV]",ptbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Pt_muon1","p_{T}(#mu_{1}) [GeV]",ptbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Pt_muon2","p_{T}(#mu_{2}) [GeV]",ptbinning2,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Pt_miss","E_{T}^{miss} [GeV]",metbinning2,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Eta_jet1","#eta(jet_{1}) [GeV]",etabinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Eta_jet2","#eta(jet_{2}) [GeV]",etabinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Eta_muon1","#eta(#mu_{1}) [GeV]",etabinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Eta_muon2","#eta(#mu_{2}) [GeV]",etabinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)	
		MakeBasicPlot("Phi_jet1","#phi(jet_{1}) [GeV]",phibinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Phi_jet2","#phi(jet_{2}) [GeV]",phibinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Phi_muon1","#phi(#mu_{1}) [GeV]",phibinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("Phi_muon2","#phi(#mu_{2}) [GeV]",phibinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)	
		MakeBasicPlot("St_uujj","S_{T}^{#mu #mu j j} [GeV]",stbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("M_uu","M^{#mu #mu} [GeV]",bosonbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("MH_uujj","M^{#mu j} (lead jet combo) [GeV]",lqbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("M_uujj1","M^{#mu j}_{1} [GeV]",lqbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("M_uujj2","M^{#mu j}_{2} [GeV]",lqbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("GoodVertexCount","N_{Vertices}",vbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("JetCount","N_{jet}",nbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("MuonCount","N_{#mu}",nbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("ElectronCount","N_{e}",nbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DR_muon1muon2","#DeltaR(#mu_1,#mu_2)",drbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DR_muon1jet1","#DeltaR(#mu_1,j_1)",drbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DR_muon1jet2","#DeltaR(#mu_1,j_2)",drbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DR_muon2jet1","#DeltaR(#mu_2,j_1)",drbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)
		MakeBasicPlot("DR_muon2jet2","#DeltaR(#mu_2,j_2)",drbinning,highstselectionmumu,NormalWeightMuMu,NormalDirectory,'stcut','uujj',Rz_uujj, Rw_uvjj,Rtt_uujj,'',version_name,500)

		MakeBasicPlot("Pt_jet1","p_{T}(jet_{1}) [GeV]",ptbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Pt_jet2","p_{T}(jet_{2}) [GeV]",ptbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Pt_muon1","p_{T}(#mu_{1}) [GeV]",ptbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Pt_miss","E_{T}^{miss} [GeV]",ptbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Eta_jet1","#eta(jet_{1}) [GeV]",etabinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Eta_jet2","#eta(jet_{2}) [GeV]",etabinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Eta_muon1","#eta(#mu_{1}) [GeV]",etabinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Phi_jet1","#phi(jet_{1}) [GeV]",phibinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Phi_jet2","#phi(jet_{2}) [GeV]",phibinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Phi_muon1","#phi(#mu_{1}) [GeV]",phibinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("Phi_miss","#phi^{miss} [GeV]",phibinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("St_uvjj","S_{T}^{#mu #nu j j} [GeV]",stbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("MT_uv","M_{T}^{#mu #nu} [GeV]",bosonbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("MT_uvjj","M_{T}^{#mu j} [GeV]",lqbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("M_uvjj","M^{#mu j} [GeV]",lqbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("MH_uvjj","M^{#mu j} (lead jet only) [GeV]",lqbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("GoodVertexCount","N_{Vertices}",vbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("JetCount","N_{jet}",nbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("MuonCount","N_{#mu}",nbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("ElectronCount","N_{e}",nbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("DPhi_muon1met","#Delta #phi (#mu_{1},E_{T}^{miss})",dphibinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("DPhi_jet1met","#Delta #phi(j_{1},E_{T}^{miss})",dphibinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("DPhi_jet2met","#Delta #phi(j_{2},E_{T}^{miss})",dphibinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("DR_muon1jet1","#DeltaR(#mu_1,j_1)",drbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)
		MakeBasicPlot("DR_muon1jet2","#DeltaR(#mu_1,j_2)",drbinning,highstselectionmunu,NormalWeightMuNu,NormalDirectory,'stcut','uvjj',Rz_uujj, Rw_uvjj,Rtt_uvjj,'',version_name,500)


		os.system('echo Combining Figures; convert -density 800 Results_'+version_name+'/*png Results_'+version_name+'/AllPlots.pdf')


		# Full Tables
		QuickTable(MuMuOptCutFile, preselectionmumu,NormalWeightMuMu,Rz_uujj, Rw_uvjj,Rtt_uujj)
		QuickTable(MuNuOptCutFile, preselectionmunu,NormalWeightMuNu,Rz_uujj, Rw_uvjj,Rtt_uvjj)

	if (False):
		# FullAnalysis(MuMuOptCutFile, preselectionmumu,preselectionmunu,NormalDirectory,NormalWeightMuMu)  # scriptflag
		# FullAnalysis(MuNuOptCutFile, preselectionmumu,preselectionmunu,NormalDirectory,NormalWeightMuNu)  # scriptflag

		uujjcardfiles = MuMuOptCutFile.replace('.txt','_systable*.txt')
		uvjjcardfiles = MuNuOptCutFile.replace('.txt','_systable*.txt')

		uujjcards = ParseFinalCards(uujjcardfiles)
		uvjjcards = ParseFinalCards(uvjjcardfiles)
		finalcards = FixFinalCards([uujjcards,uvjjcards])

		print 'Final Cards Available in ',finalcards


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
person = (os.popen('whoami').readlines()[0]).replace("\n",'')

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

for f in os.popen('ls '+EMuDirectory+"| grep \".root\"").readlines():
	exec('te_'+f.replace(".root\n","")+" = TFile.Open(\""+EMuDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")



def EMuStudy():
	for f in os.popen('ls '+EMuDirectory+"| grep \".root\"").readlines():
		exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+EMuDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")


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

def QuickSysIntegral(tree,selection,scalefac):

	h = TH1D('h','h',1,-1,3)
	h.Sumw2()
	tree.Project('h','1.0',selection+'*'+str(scalefac))
	I = h.Integral()
	E = h.GetEntries()
	return str([I,int(E)])

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

def QuickSysEntries(tree,selection,scalefac):

	h = TH1D('h','h',1,-1,3)
	h.Sumw2()
	tree.Project('h','1.0',selection)
	I = h.GetEntries()
	return str([int(1.0*I*scalefac),int(1.0*I*scalefac)]) 


def texentry(measurement):
	return '$ '+str(round(measurement[0],2))+' \\pm '+str(round(measurement[1],2))+' $'

def csventry(measurement):
	return str(round(measurement[0],2))+' +- '+str(round(measurement[1],2))

def QuickTableLine(treestruc,selection,scalefacs,ftex,fcsv):
	[_stree,_btrees,_dtree] = treestruc
	_s = QuickIntegral(_stree,selection,scalefacs[0])
	_bs = [QuickIntegral(_btrees[b],selection,scalefacs[1][b]) for b in range(len(_btrees))]
	_bt = QuickMultiIntegral(_btrees,selection,scalefacs[1])
	_d = QuickEntries (_dtree,selection+dataHLT,scalefacs[2])

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

	print selection
	print texline 

	f = open(ftex,'a')
	f.write(texline+'\n')
	f.close()

	f = open(fcsv,'a')
	f.write(csvline+'\n')
	f.close()

def QuickTable(optimlog, selection, weight,rz,rw,rt):
	selection = selection+'*'+weight
	texfile = optimlog.replace('.txt','_table.tex')
	csvfile = optimlog.replace('.txt','_table.csv')

	headers = ['TTBar','Z+Jets','W+Jets','sTop','VV','Tot BG','Data','Signal']


	f = open(texfile,'w')
	header = '  '
	for h in headers:
		header += h + '&'
	header = header[:-1]
	header += '\\\\'
	f.write(header+'\n')
	f.close()

	f = open(csvfile,'w')
	header = ' '
	for h in headers:
		header += h + ','
	header = header[:-1]	
	f.write(header+'\n')
	f.close()

	nline = 0
	for line in open(optimlog,'r'):

		if nline==0:

			print '  ..processing table line for optimization:  ', line
			fsel = line.replace('\n','')
			masschan = fsel.split('=')[0]
			masschan = masschan.replace('\n','')
			masschan = masschan.replace(' ','')
			mass = masschan.split('jj')[-1]
			chan = 't_'+masschan.split('_')[-1]
			fsel = (fsel.split("="))[-1]
			fsel = '*'+fsel.replace(" ","")
			this_sel = '('+selection+')'

			exec('treefeed = ['+chan+']')
			treefeed.append([t_TTBarDBin,t_ZJetsJBin,t_WJetsJBin,t_SingleTop,t_DiBoson])
			treefeed.append(t_SingleMuData)
			scalefacs = [1,[rt,rz,rw,1,1],1]
			QuickTableLine(treefeed,this_sel,scalefacs,texfile,csvfile)

		print '  ..processing table line for optimization:  ', line
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
		scalefacs = [1,[rt,rz,rw,1,1],1]
		QuickTableLine(treefeed,this_sel,scalefacs,texfile,csvfile)

		nline += 1

def QuickSysTableLine(treestruc,selection,scalefacs,fsys,chan):
	[_stree,_dtree,_btrees] = treestruc
	_s = QuickSysIntegral(_stree,selection,scalefacs[0])
	_bs = [QuickSysIntegral(_btrees[b],selection,scalefacs[1][b]) for b in range(len(_btrees))]
	_d = QuickSysEntries (_dtree,selection+dataHLT,scalefacs[2])

	sysline = 'L_'+chan + ' = ['
	sysline += (_s)+' , '
	sysline += (_d)+' , '
	for x in _bs:
		sysline += ' '+(x)
		sysline += ' , '
	sysline = sysline[0:-2]+' ]'

	print selection.replace('\n','')
	print ' '

	f = open(fsys,'a')
	f.write(sysline+'\n')
	f.close()

def ModSelection(selection,sysmethod,channel_log):
	_kinematicvariables = ['Pt_muon1','Pt_muon2','Pt_ele1','Pt_ele2','Pt_jet1','Pt_jet2','Pt_miss']
	_kinematicvariables += ['Eta_muon1','Eta_muon2','Eta_ele1','Eta_ele2','Eta_jet1','Eta_jet2','Eta_miss']
	_kinematicvariables += ['Phi_muon1','Phi_muon2','Phi_ele1','Phi_ele2','Phi_jet1','Phi_jet2','Phi_miss']
	_kinematicvariables += ['St_uujj','St_uvjj']
	_kinematicvariables += ['St_eejj','St_evjj']
	_kinematicvariables += ['M_uujj1','M_uujj2','M_uujjavg','MT_uvjj1','MT_uvjj2','M_uvjj','MT_uvjj']
	_kinematicvariables += ['M_uu','MT_uv']
	_kinematicvariables += ['DR_muon1muon2','DPhi_muon1met','DPhi_jet1met']
	# _kinematicvariables += ['M_eejj1','M_eejj2','MT_evjj1','MT_evjj2','M_evjj','MT_evjj']
	# _kinematicvariables += ['JetCount','MuonCount','ElectronCount','GenJetCount']
	_weights = ['weight_nopu','weight_central', 'weight_pu_up', 'weight_pu_down']
	_variations = ['','JESup','JESdown','MESup','MESdown','JERup','JERdown','MER']	
	selsplit = []
	selchars = ''
	alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
	for s in selection:
		if s not in alphabet:
			selsplit.append(selchars)
			selchars = s
			selsplit.append(selchars)
			selchars = ''
		else:
			selchars += s
	selsplit.append(selchars)
	outsel = ''
	for v in _variations:
		if sysmethod == v:
			for sobj in selsplit:
				for k in _kinematicvariables:
					if sobj == k:
						sobj = k+sysmethod
				outsel += sobj
	if outsel != '':
		selection=outsel

	if sysmethod == 'LUMIup':
		selection = '(1.044)*'+selection
	if sysmethod == 'LUMIdown':
		selection = '(0.956)*'+selection

	if sysmethod == 'MUONIDISO':
		if 'uujj' in channel_log: 
			selection = '(1.02)*'+selection
		if 'uvjj' in channel_log: 
			selection = '(1.01)*'+selection

	if sysmethod == 'MUONHLT':
		if 'uvjj' in channel_log: 
			selection = '(1.01)*'+selection

	if sysmethod == 'PUup':
		selection = selection.replace('weight_central','weight_pu_up')
	if sysmethod == 'PUdown':
		selection = selection.replace('weight_central','weight_pu_down')

	return selection


def SysTable(optimlog, selection_uujj,selection_uvjj,NormalDirectory, weight,sysmethod):
	selection_uujj = selection_uujj+'*'+weight
	selection_uvjj = selection_uvjj+'*'+weight
	selection_uujj = ModSelection(selection_uujj,sysmethod,optimlog)
	selection_uvjj = ModSelection(selection_uvjj,sysmethod,optimlog)

	[[Rz_uujj,Rz_uujj_err],[Rtt_uujj,Rtt_uujj_err]] = GetMuMuScaleFactors( selection_uujj, NormalDirectory, '(M_uu>80)*(M_uu<100)*(Pt_miss<100)', '(M_uu>100)*(Pt_miss>=100)')
	[[Rw_uvjj,Rw_uvjj_err],[Rtt_uvjj,Rtt_uvjj_err]] = GetMuNuScaleFactors( selection_uvjj, NormalDirectory, '(MT_uv>70)*(MT_uv<110)*(JetCount<3.5)', '(MT_uv>70)*(MT_uv<110)*(JetCount>3.5)')

	Rz_uujj_print = str(round(Rz_uujj,3)) + ' $\\pm$ ' + str(round(Rz_uujj_err,3))	
	Rtt_uujj_print = str(round(Rtt_uujj,3)) + ' $\\pm$ ' + str(round(Rtt_uujj_err,3))	
	Rw_uvjj_print = str(round(Rw_uvjj,3)) + ' $\\pm$ ' + str(round(Rw_uvjj_err,3))	
	Rtt_uvjj_print = str(round(Rtt_uvjj,3)) + ' $\\pm$ ' + str(round(Rtt_uvjj_err,3))	
	print sysmethod+' & ' + Rz_uujj_print+' & '+Rtt_uujj_print+' & '+Rw_uvjj_print+' & '+Rtt_uvjj_print+' \\\\'

	if 'uujj' in optimlog:
		[rz,rw,rt] = [Rz_uujj,Rw_uvjj,Rtt_uujj]
		[_e_rz,_e_rw,_e_rt] = [Rz_uujj_err,Rw_uvjj_err,Rtt_uujj_err]

		selection = selection_uujj
	if 'uvjj' in optimlog:
		[rz,rw,rt] = [Rz_uujj,Rw_uvjj,Rtt_uvjj]
		[_e_rz,_e_rw,_e_rt] = [Rz_uujj_err,Rw_uvjj_err,Rtt_uvjj_err]	
		selection = selection_uvjj

	rglobal = 1.0

	if sysmethod == 'ZNORMup':     rz += _e_rz 
	if sysmethod == 'ZNORMdown':   rz += -_e_rz 
	if sysmethod == 'WNORMup': 	   rw += _e_rw
	if sysmethod == 'WNORMdown':   rw += -_e_rw 
	if sysmethod == 'TTNORMup':    rt += _e_rt
	if sysmethod == 'TTNORMdown':  rt += -_e_rt 	

	if sysmethod == 'SHAPETT' : 
		if 'uujj' in optimlog: 
			rt = 1.077*rt
		if 'uvjj' in optimlog: 
			rt = 1.199*rt

	if sysmethod == 'SHAPEZ'  : rz = 1.033*rz
	if sysmethod == 'SHAPEW'  : rw = 1.091*rw

	sysfile = optimlog.replace('.txt','_systable_'+sysmethod+'.txt')

	headers = ['Signal','Data','TTBar','ZJets','WJets','sTop','VV']


	f = open(sysfile,'w')
	header = 'headers = '+str(headers)
	f.write(header+'\n')
	f.close()


	for line in open(optimlog,'r'):
		line = line.replace('\n','')
		print 'processing table line for optimization:  ', line
		fsel = line.replace('\n','')
		fsel = ModSelection(fsel,sysmethod,optimlog)
		masschan = fsel.split('=')[0]
		masschan = masschan.replace('\n','')
		masschan = masschan.replace(' ','')
		mass = masschan.split('jj')[-1]
		chan = 't_'+masschan.split('_')[-1]
		fsel = (fsel.split("="))[-1]
		fsel = '*'+fsel.replace(" ","")
		this_sel = '('+selection+fsel+')'

		exec('treefeed = ['+chan+']')
		treefeed.append(t_SingleMuData)
		treefeed.append([t_TTBarDBin,t_ZJetsJBin,t_WJetsJBin,t_SingleTop,t_DiBoson])
		scalefacs = [1,[rt,rz,rw,1,1],1]
		QuickSysTableLine(treefeed,this_sel,scalefacs,sysfile,chan)
		# break

def FullAnalysis(optimlog,selection_uujj,selection_uvjj,NormalDirectory,weight):

	_Variations = ['','JESup','JESdown','MESup','MESdown','JERup','JERdown','MER','LUMIup','LUMIdown','PUup','PUdown','ZNORMup','ZNORMdown','WNORMup','WNORMdown','TTNORMup','TTNORMdown','SHAPETT','SHAPEZ','SHAPEW','MUONIDISO','MUONHLT']	
	for v in _Variations:
		print ' -'*50
		print 'Processing table for variation: ',v
		if (optimlog.replace('.txt','_systable_'+v+'.txt')) in str(os.popen('ls '+optimlog.replace('.txt','_systable_'+v+'.txt')).readlines()):
			print 'Already present ... skipping. '
			continue
		SysTable(optimlog, selection_uujj, selection_uvjj,NormalDirectory, weight,v)


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
	# print QuickEntries(t_SingleMuData,selection + '*' + controlregion_1,1.0)
	# print QuickIntegral(t_ZJetsJBin,selection + '*' + controlregion_1,1.0)
	# sys.exit()
	N1 = QuickEntries(t_SingleMuData,selection + '*' + controlregion_1+dataHLT,1.0)
	N2 = QuickEntries(t_SingleMuData,selection + '*' + controlregion_2+dataHLT,1.0)

	Z1 = QuickIntegral(t_ZJetsJBin,selection + '*' + controlregion_1,1.0)
	T1 = QuickIntegral(t_TTBarDBin,selection + '*' + controlregion_1,1.0)
	s1 = QuickIntegral(t_SingleTop,selection + '*' + controlregion_1,1.0)
	w1 = QuickIntegral(t_WJetsJBin,selection + '*' + controlregion_1,1.0)
	v1 = QuickIntegral(t_DiBoson,selection + '*' + controlregion_1,1.0)

	Z2 = QuickIntegral(t_ZJetsJBin,selection + '*' + controlregion_2,1.0)
	T2 = QuickIntegral(t_TTBarDBin,selection + '*' + controlregion_2,1.0)
	s2 = QuickIntegral(t_SingleTop,selection + '*' + controlregion_2,1.0)
	w2 = QuickIntegral(t_WJetsJBin,selection + '*' + controlregion_2,1.0)
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

	# ttbar force unity
	tout = [1.0,0.067,'1.000 +- 0.067']

	print 'MuMu: RZ  = ', zout[-1]
	print 'MuMu: Rtt = ', tout[-1]
	return [ [ zout[0], zout[1] ] , [ tout[0],tout[1] ] ]



def GetMuNuScaleFactors( selection, FileDirectory, controlregion_1, controlregion_2):
	# for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
	# 	exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")

	N1 = QuickEntries(t_SingleMuData,selection + '*' + controlregion_1+dataHLT,1.0)
	N2 = QuickEntries(t_SingleMuData,selection + '*' + controlregion_2+dataHLT,1.0)

	W1 = QuickIntegral(t_WJetsJBin,selection + '*' + controlregion_1,1.0)
	T1 = QuickIntegral(t_TTBarDBin,selection + '*' + controlregion_1,1.0)
	s1 = QuickIntegral(t_SingleTop,selection + '*' + controlregion_1,1.0)
	z1 = QuickIntegral(t_ZJetsJBin,selection + '*' + controlregion_1,1.0)
	v1 = QuickIntegral(t_DiBoson,selection + '*' + controlregion_1,1.0)

	W2 = QuickIntegral(t_WJetsJBin,selection + '*' + controlregion_2,1.0)
	T2 = QuickIntegral(t_TTBarDBin,selection + '*' + controlregion_2,1.0)
	s2 = QuickIntegral(t_SingleTop,selection + '*' + controlregion_2,1.0)
	z2 = QuickIntegral(t_ZJetsJBin,selection + '*' + controlregion_2,1.0)
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



def MakeBasicPlot(recovariable,xlabel,presentationbinning,selection,weight,FileDirectory,tagname,channel, zscale, wscale, ttscale,cutlog,version_name,plotmass):

	# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "t_DiBoson"
	# for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
	# 	exec('t_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
	tmpfile = TFile("tmpbin.root","RECREATE")
	print "  Preparing basic histo for "+channel+":"+recovariable+"...  "
	# Create Canvas
	c1 = TCanvas("c1","",800,800)
	gStyle.SetOptStat(0)

	pad1 = TPad( 'pad1', 'pad1', 0.0, 0.47, 1.0, 1.0 )#divide canvas into pads
	pad2 = TPad( 'pad2', 'pad2', 0.0, 0.25, 1.0, 0.44 )
	pad3 = TPad( 'pad3', 'pad3', 0.0, 0.03, 1.0, 0.22 )
	pad1.Draw()
	pad2.Draw()
	pad3.Draw()

	pad1.cd()
	pad1.SetGrid()
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
		# print 'cat '+cutlog+' | grep '+channel+str(plotmass)
		fsel = ((os.popen('cat '+cutlog+' | grep '+channel+str(plotmass)).readlines())[0]).replace('\n','')
		fsel = (fsel.split("="))[-1]
		fsel = '*'+fsel.replace(" ","")
		selection = '('+selection+fsel+')'
		# print selection

	##############################################################################
	#######      Top Left Plot - Normal Stacked Distributions              #######
	##############################################################################
	c1.cd(1)
	print 'Projecting trees...  ',
	### Make the plots without variable bins!
	hs_rec_WJets=CreateHisto('hs_rec_WJets','W+Jets',t_WJetsJBin,recovariable,presentationbinning,selection+'*('+str(wscale)+')*'+weight,WStackStyle,Label)
	hs_rec_Data=CreateHisto('hs_rec_Data','Data',t_SingleMuData,recovariable,presentationbinning,selection+dataHLT,DataRecoStyle,Label)
	hs_rec_DiBoson=CreateHisto('hs_rec_DiBoson','DiBoson',t_DiBoson,recovariable,presentationbinning,selection+'*'+weight,DiBosonStackStyle,Label)
	hs_rec_ZJets=CreateHisto('hs_rec_ZJets','Z+Jets',t_ZJetsJBin,recovariable,presentationbinning,selection+'*('+str(zscale)+')*'+weight,ZStackStyle,Label)
	hs_rec_TTBar=CreateHisto('hs_rec_TTBar','t#bar{t}',t_TTBarDBin,recovariable,presentationbinning,selection+'*('+str(ttscale)+')*'+weight,TTStackStyle,Label)
	hs_rec_SingleTop=CreateHisto('hs_rec_SingleTop','SingleTop',t_SingleTop,recovariable,presentationbinning,selection+'*'+weight,StopStackStyle,Label)

	# hs_rec_QCDMu=CreateHisto('hs_rec_QCDMu','QCD #mu-enriched [Pythia]',t_QCDMu,recovariable,presentationbinning,selection+'*'+weight,QCDStackStyle,Label)

	sig1name = ''
	sig2name = ''

	if channel == 'uujj':
		sig1name = 'LQ, M = 500 GeV'
		sig2name = 'LQ, M = 900 GeV'
		if tagname != 'final':
			hs_rec_Signal=CreateHisto('hs_rec_Signal',sig1name,t_LQuujj500,recovariable,presentationbinning,selection+'*'+weight,SignalStyle,Label)
			hs_rec_Signal2=CreateHisto('hs_rec_Signal2',sig2name,t_LQuujj900,recovariable,presentationbinning,selection+'*'+weight,SignalStyle2,Label)
		if tagname == 'final':
			exec ("_stree = t_LQ"+channel+str(plotmass))
			hs_rec_Signal=CreateHisto('hs_rec_Signal','LQ, M = '+str(plotmass)+' GeV',_stree,recovariable,presentationbinning,selection+'*'+weight,SignalStyle,Label)

		hs_rec_DiBoson.SetTitle("Other Backgrounds")
		hs_rec_DiBoson.Add(hs_rec_WJets)
		hs_rec_DiBoson.Add(hs_rec_SingleTop)
		SM=[hs_rec_DiBoson,hs_rec_TTBar,hs_rec_ZJets]

	if channel == 'uvjj':
		if tagname != 'final':	
			sig1name = 'LQ, M = 400 GeV'
			sig2name = 'LQ, M = 750 GeV'
			hs_rec_Signal=CreateHisto('hs_rec_Signal',sig1name,t_LQuvjj400,recovariable,presentationbinning,selection+'*'+weight,SignalStyle,Label)
			hs_rec_Signal2=CreateHisto('hs_rec_Signal2',sig2name,t_LQuvjj750,recovariable,presentationbinning,selection+'*'+weight,SignalStyle2,Label)
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
	print SMIntegral
	print hs_rec_Data.Integral(), hs_rec_Data.GetEntries()
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
	# FixDrawLegend(c1.cd(1).BuildLegend())
	leg = TLegend(0.63,0.62,0.89,0.88,"","brNDC");
	leg.SetTextFont(132);
	leg.SetFillColor(0);
	leg.SetBorderSize(0);
	leg.SetTextSize(.04)
	leg.AddEntry(hs_rec_Data,"Data");
	if channel=='uujj':
		leg.AddEntry(hs_rec_ZJets,'Z/#gamma^{*} + jets')
	if channel=='uujj':
		leg.AddEntry(hs_rec_WJets,'W + jets')
	leg.AddEntry(hs_rec_TTBar,'t #bar{t} + jets')
	leg.AddEntry(hs_rec_DiBoson,'Other Backgrounds')
	if tagname !='final':
		leg.AddEntry(hs_rec_Signal,sig1name)
		leg.AddEntry(hs_rec_Signal2,sig2name)
	else:
		leg.AddEntry(hs_rec_Signal,'LQ, M = '+str(plotmass)+' GeV')
	leg.Draw()

	sqrts = "#sqrt{s} = 8 TeV";
	l1=TLatex()
	l1.SetTextAlign(12)
	l1.SetTextFont(132)
	l1.SetNDC()
	l1.SetTextSize(0.06)
 
	l1.DrawLatex(0.37,0.94,"CMS 2012  "+sqrts+", 19.6 fb^{-1}")
	# l1.DrawLatex(0.13,0.76,sqrts)

	l2=TLatex()
	l2.SetTextAlign(12)
	l2.SetTextFont(132)
	l2.SetNDC()
	l2.SetTextSize(0.06)
	# l2.SetTextAngle(45);	
	l2.DrawLatex(0.15,0.83,"PRELIMINARY")

	gPad.RedrawAxis()

	MCStack.SetMinimum(.03333)
	MCStack.SetMaximum(100*hs_rec_Data.GetMaximum())

	pad2.cd()
	# pad2.SetLogy()
	pad2.SetGrid()

	RatHistDen =CreateHisto('RatHisDen','RatHistDen',t_SingleMuData,recovariable,presentationbinning,'0',DataRecoStyle,Label)



	RatHistDen.Sumw2()
	RatHistNum =CreateHisto('RatHisNum','RatHistNum',t_SingleMuData,recovariable,presentationbinning,'0',DataRecoStyle,Label)
	RatHistNum.Sumw2()
	for hmc in SM:
		RatHistDen.Add(hmc)

	RatHistNum.Add(hs_rec_Data)
	RatHistNum.Divide(RatHistDen)
	# for x in RatHistNum.GetNbinsX():
	# 	print RatHistNum.GetBinCenter(x), RatHistNum.GetBinContent(x)

	RatHistNum.SetMaximum(1.5)
	RatHistNum.SetMinimum(0.5)


	RatHistNum.GetYaxis().SetTitleFont(132);
	RatHistNum.GetXaxis().SetTitle('');
	RatHistNum.GetYaxis().SetTitle('Data/MC');


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


	pad3.cd()
	# pad2.SetLogy()
	pad3.SetGrid()

	chiplot =CreateHisto('chiplot','chiplot',t_SingleMuData,recovariable,presentationbinning,'0',DataRecoStyle,Label)
	chiplot.Sumw2()

	resstring = '( 0.0 '

	for n in range(chiplot.GetNbinsX()+1):
		lhs = chiplot.GetBinCenter(n) - 0.5*chiplot.GetBinWidth(n)
		rhs = chiplot.GetBinCenter(n) + 0.5*chiplot.GetBinWidth(n)
		lhs = str(round(lhs,3))
		rhs = str(round(rhs,3))

		bg = 0
		bgerr = 0
		dat = hs_rec_Data.GetBinContent(n)
		daterr = math.sqrt(1.0*dat)
		for hmc in SM:
			bg += hmc.GetBinContent(n)
			bgerr += hmc.GetBinError(n)*hmc.GetBinError(n)
		bgerr = math.sqrt(bgerr)
		total_err = math.sqrt(bgerr*bgerr+daterr*daterr)
		
		resfac = '1.0'

		if total_err>0: 
			chi = (dat - bg)/total_err
			chiplot.SetBinContent(n,chi)
			chiplot.SetBinError(n,0.0)
		if bg > 0 and dat > 0:
			resfac = str(round(dat/bg,3))
		if n != 0:
			resstring += ' + '+resfac+'*('+recovariable +'>'+lhs+')'+'*('+recovariable +'<='+rhs+')'

	resstring += ')'
	if recovariable =='Phi_miss':
		print resstring

	chiplot.SetMaximum(6)
	chiplot.SetMinimum(-6)


	chiplot.GetYaxis().SetTitleFont(132);
	chiplot.GetXaxis().SetTitle('');
	chiplot.GetYaxis().SetTitle('#chi (Data,MC)');


	chiplot.GetXaxis().SetTitleSize(.13);
	chiplot.GetYaxis().SetTitleSize(.13);
	chiplot.GetXaxis().CenterTitle();
	chiplot.GetYaxis().CenterTitle();		
	chiplot.GetXaxis().SetTitleOffset(.28);
	chiplot.GetYaxis().SetTitleOffset(.28);
	chiplot.GetYaxis().SetLabelSize(.09);
	chiplot.GetXaxis().SetLabelSize(.09);


	chiplot.Draw('EP')
	zero=TLine(RatHistNum.GetXaxis().GetXmin(), 0.0 , RatHistNum.GetXaxis().GetXmax(),0.0)
	plus2=TLine(RatHistNum.GetXaxis().GetXmin(), 2.0 , RatHistNum.GetXaxis().GetXmax(),2.0)
	minus2=TLine(RatHistNum.GetXaxis().GetXmin(), -2.0 , RatHistNum.GetXaxis().GetXmax(),-2.0)
	plus2.SetLineColor(2)
	minus2.SetLineColor(2)

	plus2.Draw("SAME")
	minus2.Draw("SAME")
	zero.Draw("SAME")	


	print 'Saving...  ',
	if 'final' not in tagname:
		c1.Print('Results_'+version_name+'/Basic_'+channel+'_'+recovariable+'_'+tagname+'.pdf')
		c1.Print('Results_'+version_name+'/Basic_'+channel+'_'+recovariable+'_'+tagname+'.png')
	else:
		c1.Print('Results_'+version_name+'/Basic_'+channel+'_'+recovariable+'_'+tagname+str(plotmass)+'.pdf')
		c1.Print('Results_'+version_name+'/Basic_'+channel+'_'+recovariable+'_'+tagname+str(plotmass)+'.png')		
	print 'Done.'



def MakeBasicPlotEMu(recovariable,xlabel,presentationbinning,selection,weight,FileDirectory,tagname,channel, zscale, wscale, ttscale,cutlog,version_name,plotmass):

	# Load all root files as trees - e.g. file "DiBoson.root" will give you tree called "te_DiBoson"
	# for f in os.popen('ls '+FileDirectory+"| grep \".root\"").readlines():
	# 	exec('te_'+f.replace(".root\n","")+" = TFile.Open(\""+FileDirectory+"/"+f.replace("\n","")+"\")"+".Get(\""+TreeName+"\")")
	tmpfile = TFile("tmpbin.root","RECREATE")
	print "  Preparing basic histo for "+channel+":"+recovariable+"...  "
	# Create Canvas
	c1 = TCanvas("c1","",800,800)
	gStyle.SetOptStat(0)

	pad1 = TPad( 'pad1', 'pad1', 0.0, 0.47, 1.0, 1.0 )#divide canvas into pads
	pad2 = TPad( 'pad2', 'pad2', 0.0, 0.25, 1.0, 0.44 )
	pad3 = TPad( 'pad3', 'pad3', 0.0, 0.03, 1.0, 0.22 )
	pad1.Draw()
	pad2.Draw()
	pad3.Draw()

	pad1.cd()
	pad1.SetGrid()
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
		# print 'cat '+cutlog+' | grep '+channel+str(plotmass)
		fsel = ((os.popen('cat '+cutlog+' | grep '+channel+str(plotmass)).readlines())[0]).replace('\n','')
		fsel = (fsel.split("="))[-1]
		fsel = '*'+fsel.replace(" ","")
		selection = '('+selection+fsel+')'
		# print selection

	##############################################################################
	#######      Top Left Plot - Normal Stacked Distributions              #######
	##############################################################################
	c1.cd(1)
	print 'Projecting trees...  ',
	### Make the plots without variable bins!
	hs_rec_WJets=CreateHisto('hs_rec_WJets','W+Jets',te_WJetsJBin,recovariable,presentationbinning,selection+'*('+str(wscale)+')*'+weight,WStackStyle,Label)
	hs_rec_Data=CreateHisto('hs_rec_Data','Data',te_SingleMuData,recovariable,presentationbinning,selection+dataHLT,DataRecoStyle,Label)
	hs_rec_DiBoson=CreateHisto('hs_rec_DiBoson','DiBoson',te_DiBoson,recovariable,presentationbinning,selection+'*'+weight,DiBosonStackStyle,Label)
	hs_rec_ZJets=CreateHisto('hs_rec_ZJets','Z+Jets',te_ZJetsJBin,recovariable,presentationbinning,selection+'*('+str(zscale)+')*'+weight,ZStackStyle,Label)
	hs_rec_TTBar=CreateHisto('hs_rec_TTBar','t#bar{t}',te_TTBarDBin,recovariable,presentationbinning,selection+'*('+str(ttscale)+')*'+weight,TTStackStyle,Label)
	hs_rec_SingleTop=CreateHisto('hs_rec_SingleTop','SingleTop',te_SingleTop,recovariable,presentationbinning,selection+'*'+weight,StopStackStyle,Label)

	# hs_rec_QCDMu=CreateHisto('hs_rec_QCDMu','QCD #mu-enriched [Pythia]',te_QCDMu,recovariable,presentationbinning,selection+'*'+weight,QCDStackStyle,Label)

	sig1name = ''
	sig2name = ''

	if channel == 'uujj':
		sig1name = 'LQ, M = 500 GeV'
		sig2name = 'LQ, M = 900 GeV'
		if tagname != 'final':
			hs_rec_Signal=CreateHisto('hs_rec_Signal',sig1name,te_LQuujj500,recovariable,presentationbinning,selection+'*'+weight,SignalStyle,Label)
			hs_rec_Signal2=CreateHisto('hs_rec_Signal2',sig2name,te_LQuujj900,recovariable,presentationbinning,selection+'*'+weight,SignalStyle2,Label)
		if tagname == 'final':
			exec ("_stree = te_LQ"+channel+str(plotmass))
			hs_rec_Signal=CreateHisto('hs_rec_Signal','LQ, M = '+str(plotmass)+' GeV',_stree,recovariable,presentationbinning,selection+'*'+weight,SignalStyle,Label)

		hs_rec_DiBoson.SetTitle("Other Backgrounds")
		hs_rec_DiBoson.Add(hs_rec_WJets)
		hs_rec_DiBoson.Add(hs_rec_SingleTop)
		SM=[hs_rec_DiBoson,hs_rec_ZJets,hs_rec_TTBar]

	if channel == 'uvjj':
		if tagname != 'final':	
			sig1name = 'LQ, M = 400 GeV'
			sig2name = 'LQ, M = 750 GeV'
			hs_rec_Signal=CreateHisto('hs_rec_Signal',sig1name,te_LQuvjj400,recovariable,presentationbinning,selection+'*'+weight,SignalStyle,Label)
			hs_rec_Signal2=CreateHisto('hs_rec_Signal2',sig2name,te_LQuvjj750,recovariable,presentationbinning,selection+'*'+weight,SignalStyle2,Label)
		if tagname == 'final':
			exec ("_stree = te_LQ"+channel+str(plotmass))
			hs_rec_Signal=CreateHisto('hs_rec_Signal','LQ, M = '+str(plotmass)+' GeV',_stree,recovariable,presentationbinning,selection+'*'+weight,SignalStyle,Label)
	
		hs_rec_DiBoson.SetTitle("Other Backgrounds")
		hs_rec_DiBoson.Add(hs_rec_ZJets)
		hs_rec_DiBoson.Add(hs_rec_SingleTop)		
		SM=[hs_rec_DiBoson,hs_rec_TTBar,hs_rec_WJets]
		

	# mcdatascalepres = (1.0*(hs_rec_Data.GetEntries()))/(sum(k.Integral() for k in SM))

	MCStack = THStack ("MCStack","")
	SMIntegral = sum(k.Integral() for k in SM)
	print SMIntegral
	print hs_rec_Data.Integral(), hs_rec_Data.GetEntries()
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
	# FixDrawLegend(c1.cd(1).BuildLegend())
	leg = TLegend(0.63,0.62,0.89,0.88,"","brNDC");
	leg.SetTextFont(132);
	leg.SetFillColor(0);
	leg.SetBorderSize(0);
	leg.SetTextSize(.04)
	leg.AddEntry(hs_rec_Data,"Data");
	if channel=='uujj':
		leg.AddEntry(hs_rec_ZJets,'Z/#gamma^{*} + jets')
	if channel=='uujj':
		leg.AddEntry(hs_rec_WJets,'W + jets')
	leg.AddEntry(hs_rec_TTBar,'t #bar{t} + jets')
	leg.AddEntry(hs_rec_DiBoson,'Other Backgrounds')
	if tagname !='final':
		leg.AddEntry(hs_rec_Signal,sig1name)
		leg.AddEntry(hs_rec_Signal2,sig2name)
	else:
		leg.AddEntry(hs_rec_Signal,'LQ, M = '+str(plotmass)+' GeV')
	leg.Draw()

	sqrts = "#sqrt{s} = 8 TeV";
	l1=TLatex()
	l1.SetTextAlign(12)
	l1.SetTextFont(132)
	l1.SetNDC()
	l1.SetTextSize(0.06)
 
	l1.DrawLatex(0.37,0.94,"CMS 2012  "+sqrts+", 19.6 fb^{-1}")
	# l1.DrawLatex(0.13,0.76,sqrts)

	l2=TLatex()
	l2.SetTextAlign(12)
	l2.SetTextFont(132)
	l2.SetNDC()
	l2.SetTextSize(0.06)
	# l2.SetTextAngle(45);	
	l2.DrawLatex(0.15,0.83,"PRELIMINARY")

	gPad.RedrawAxis()

	MCStack.SetMinimum(.03333)
	MCStack.SetMaximum(100*hs_rec_Data.GetMaximum())

	pad2.cd()
	# pad2.SetLogy()
	pad2.SetGrid()

	RatHistDen =CreateHisto('RatHisDen','RatHistDen',te_SingleMuData,recovariable,presentationbinning,'0',DataRecoStyle,Label)



	RatHistDen.Sumw2()
	RatHistNum =CreateHisto('RatHisNum','RatHistNum',te_SingleMuData,recovariable,presentationbinning,'0',DataRecoStyle,Label)
	RatHistNum.Sumw2()
	for hmc in SM:
		RatHistDen.Add(hmc)

	RatHistNum.Add(hs_rec_Data)
	RatHistNum.Divide(RatHistDen)
	# for x in RatHistNum.GetNbinsX():
	# 	print RatHistNum.GetBinCenter(x), RatHistNum.GetBinContent(x)

	RatHistNum.SetMaximum(1.5)
	RatHistNum.SetMinimum(0.5)


	RatHistNum.GetYaxis().SetTitleFont(132);
	RatHistNum.GetXaxis().SetTitle('');
	RatHistNum.GetYaxis().SetTitle('Data/MC');


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


	pad3.cd()
	# pad2.SetLogy()
	pad3.SetGrid()

	chiplot =CreateHisto('chiplot','chiplot',te_SingleMuData,recovariable,presentationbinning,'0',DataRecoStyle,Label)
	chiplot.Sumw2()

	resstring = '( 0.0 '

	for n in range(chiplot.GetNbinsX()+1):
		lhs = chiplot.GetBinCenter(n) - 0.5*chiplot.GetBinWidth(n)
		rhs = chiplot.GetBinCenter(n) + 0.5*chiplot.GetBinWidth(n)
		lhs = str(round(lhs,3))
		rhs = str(round(rhs,3))

		bg = 0
		bgerr = 0
		dat = hs_rec_Data.GetBinContent(n)
		daterr = math.sqrt(1.0*dat)
		for hmc in SM:
			bg += hmc.GetBinContent(n)
			bgerr += hmc.GetBinError(n)*hmc.GetBinError(n)
		bgerr = math.sqrt(bgerr)
		total_err = math.sqrt(bgerr*bgerr+daterr*daterr)
		
		resfac = '1.0'

		if total_err>0: 
			chi = (dat - bg)/total_err
			chiplot.SetBinContent(n,chi)
			chiplot.SetBinError(n,0.0)
		if bg > 0 and dat > 0:
			resfac = str(round(dat/bg,3))
		if n != 0:
			resstring += ' + '+resfac+'*('+recovariable +'>'+lhs+')'+'*('+recovariable +'<='+rhs+')'

	resstring += ')'
	if recovariable =='Phi_miss':
		print resstring

	chiplot.SetMaximum(6)
	chiplot.SetMinimum(-6)


	chiplot.GetYaxis().SetTitleFont(132);
	chiplot.GetXaxis().SetTitle('');
	chiplot.GetYaxis().SetTitle('#chi (Data,MC)');


	chiplot.GetXaxis().SetTitleSize(.13);
	chiplot.GetYaxis().SetTitleSize(.13);
	chiplot.GetXaxis().CenterTitle();
	chiplot.GetYaxis().CenterTitle();		
	chiplot.GetXaxis().SetTitleOffset(.28);
	chiplot.GetYaxis().SetTitleOffset(.28);
	chiplot.GetYaxis().SetLabelSize(.09);
	chiplot.GetXaxis().SetLabelSize(.09);


	chiplot.Draw('EP')
	zero=TLine(RatHistNum.GetXaxis().GetXmin(), 0.0 , RatHistNum.GetXaxis().GetXmax(),0.0)
	plus2=TLine(RatHistNum.GetXaxis().GetXmin(), 2.0 , RatHistNum.GetXaxis().GetXmax(),2.0)
	minus2=TLine(RatHistNum.GetXaxis().GetXmin(), -2.0 , RatHistNum.GetXaxis().GetXmax(),-2.0)
	plus2.SetLineColor(2)
	minus2.SetLineColor(2)

	plus2.Draw("SAME")
	minus2.Draw("SAME")
	zero.Draw("SAME")	


	print 'Saving...  ',
	if 'final' not in tagname:
		c1.Print('Results_'+version_name+'/Basic_'+channel+'_'+recovariable+'_'+tagname+'.pdf')
		c1.Print('Results_'+version_name+'/Basic_'+channel+'_'+recovariable+'_'+tagname+'.png')
	else:
		c1.Print('Results_'+version_name+'/Basic_'+channel+'_'+recovariable+'_'+tagname+str(plotmass)+'.pdf')
		c1.Print('Results_'+version_name+'/Basic_'+channel+'_'+recovariable+'_'+tagname+str(plotmass)+'.png')		
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
	hs_rec_WJets=CreateHisto('hs_rec_WJets','W+Jets',t_WJetsJBin,recovariable,presentationbinning,selection+'*('+str(wscale)+')*'+weight,WStackStyle,Label)
	hs_rec_Data=CreateHisto('hs_rec_Data','Data, 5/fb',t_SingleMuData,recovariable,presentationbinning,selection+dataHLT,DataRecoStyle,Label)
	hs_rec_DiBoson=CreateHisto('hs_rec_DiBoson','DiBoson',t_DiBoson,recovariable,presentationbinning,selection+'*'+weight,DiBosonStackStyle,Label)
	hs_rec_ZJets=CreateHisto('hs_rec_ZJets','Z+Jets',t_ZJetsJBin,recovariable,presentationbinning,selection+'*('+str(zscale)+')*'+weight,ZStackStyle,Label)
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
	
	print 'Getting log ... '
	# flog = open('loglog.txt','w')

	nf = os.popen('cat '+cutfile+' | wc -l').readlines()[0]
	nf = int(nf)
	nd = 0
	for c in open(cutfile):
		nd += 1
		if nd%100000==0:
			print str(round( (1.0*nd)/(1.0*nf),2 )), '% complete'
		# print '** ',c
		# flog.write('** '+c)
		exec(c)

	# flog.close()
	
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

	print 'Performing fits ...'
	cuts = MakeSmoothCuts(valuetable,[minvar[0],hvars[0][0], hvars[1][0]],tag,channel,'lin')
	cuts = MakeSmoothCuts(valuetable,[minvar[0],hvars[0][0], hvars[1][0]],tag,channel,'lintanh')
	cuts = MakeSmoothCuts(valuetable,[minvar[0],hvars[0][0], hvars[1][0]],tag,channel,'pol2')
	cuts = MakeSmoothCuts(valuetable,[minvar[0],hvars[0][0], hvars[1][0]],tag,channel,'pol2cutoff')
	cuts = MakeSmoothCuts(valuetable,[minvar[0],hvars[0][0], hvars[1][0]],tag,channel,'lincutoff')

	return cuts

def ReDoOptFits(OptFile):
	tag = OptFile.split('/')[0]
	tag = tag.replace('Results_','')
	valuetable = []
	for line in open(OptFile):
		valueline = []
		channel = line.split('jj')[0]
		channel = channel.split('LQ')[1]
		channel += 'jj'
		mass = float(line.split('jj')[1].split('=')[0].replace(' ',''))

		varnames = line.split('=')[-1]
		varnames = varnames.replace(')','')
		varnames = varnames.replace('(','')
		varnames = varnames.split('*')
		varwords = []
		varvals = []
		for v in varnames:
			v = v.split('>')
			varwords.append(v[0].replace(' ',''))
			varvals.append(float(v[1]))
		valueline = [mass]
		for v in varvals:
			valueline.append(v)
		valuetable.append(valueline)
	# print tag,channel, varwords
	# for v in valuetable:
	# 	print v

	# cuts = MakeSmoothCuts(valuetable,varwords,tag,channel,'lin')
	# cuts = MakeSmoothCuts(valuetable,varwords,tag,channel,'lintanh')
	# cuts = MakeSmoothCuts(valuetable,varwords,tag,channel,'pol2')
	cuts = MakeSmoothCuts(valuetable,varwords,tag,channel,'pol2cutoff')
	# cuts = MakeSmoothCuts(valuetable,varwords,tag,channel,'lincutoff')		

def MakeSmoothCuts(vals,vnames,versionname,chan,rawmethod):

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

	_allvals = sorted(vals,key=lambda vals: vals[0])


	if 'cutoff' in rawmethod:
		_vals = []
		for v in _allvals:
			if v[0] <= 1000:
				_vals.append(v)
	else:
		_vals=_allvals

	for v in _vals:
		print v

	yinds = []
	masses = []

	for v in range(len(_vals[0])):
		if v == 0: 
			for v in _vals:
				masses.append(v[0])
			continue
		yinds.append(v)

	allmasses = []

	for v in range(len(_allvals[0])):
		if v == 0: 
			for v in _allvals:
				allmasses.append(v[0])	

	n = len(masses)

	method = rawmethod.replace('cutoff','')
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

		print X
		print Y
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
		
		if method == 'lin':
			ft = TF1("ft","[1]*x + [0]", 250,1250 )  # linear
		if method == 'lintanh':
			ft = TF1("ft","[0] + [1]*[1]*tanh(x+[2]) + [3]*[3]*x",250,1250) 		#linear+tanh monotonic
		if method == 'pol2':
			ft = TF1("ft","[0] + [1]*x + [2]*(x*x)", 250, 1250); # second degree pol
		hout.Fit('ft')

		betterfits = []
		for m in allmasses:
			orig_val = ft.Eval(m)
			new_val = round_to(orig_val,5)
			betterfits.append(new_val)
		optim_res.append(betterfits)
		c1.Print('Results_'+versionname+'/Optimization_'+chan+'_'+vnames[y-1]+'_'+rawmethod+'.pdf')
		c1.Print('Results_'+versionname+'/Optimization_'+chan+'_'+vnames[y-1]+'_'+rawmethod+'.png')

	optimlog = open('Results_'+versionname+'/Opt_'+chan+'Cuts_Smoothed_'+rawmethod+'.txt','w')	

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


def CompareMeanSys(m,s1,s2):
	_m = []
	_s1 = []
	_s2 = []
	for x in range(len(m)):
		if x == 1:
			continue
		_m.append(m[x][0])
		_s1.append(s1[x][0])
		_s2.append(s2[x][0])

	systematics = []

	for x in range(len(_m)):
		syst = 1
		mavg = _m[x]
		sv1 = _s1[x]
		sv2 = _s2[x]
		d1 = abs(sv1-mavg)
		d2 = abs(sv2-mavg)
		diff = max([d1,d2])
		if diff > 0 and mavg > 0:
			syst = 1 + diff/mavg
		systematics.append(syst)
	outline = ' '
	for s in systematics:
		outline += str(s) + ' '
	return outline


def ParseFinalCards(cardcoll):
	chan = '' + 'uujj'*('uujj' in cardcoll)+ 'uvjj'*('uvjj' in cardcoll) 
	tables = glob(cardcoll)
	systypes = []
	for t in tables:
		_sys = (t.split('_')[-1]).replace('.txt','')
		systypes.append(_sys)
	variations = []
	for s in systypes:
		s = s.replace('up','')
		s = s.replace('down','')
		if s not in variations:
			variations.append(s)
	# for v in variations:
	# 	print v
	T = ''
	for n in range(len(systypes)):
		if systypes[n]=='':
			T = tables[n]
	print T
	cardnames = []
	for line in open(T,'r'):
		if 'L_' in line:
			cardname = line.split(' = ')[0]
			cardname = cardname.split('_')[-1] 
			cardnames.append(cardname)
		print ' * ',line
		exec(line)

	configlines = ['','imax 1','jmax '+str(len(headers)-2),'kmax '+str(len(headers)-1+len(variations)-1),'','bin 1','']

	nc = 0
	standardweights = []

	finalcards = cardcoll.replace('*','_ALL_')
	finalcards = finalcards.replace('systable','finalcards')
	fout = open(finalcards,'w')


	for card in cardnames:
		allcards = [line.replace('\n','') for line in os.popen('grep '+card+' '+cardcoll).readlines()]
		nc += 1
		mcard = ''
		scards = []
		for a in allcards:
			if T in a:
				mcard = a
			else:
				scards.append(a)
			
		statlines = []

		# print headers
		# print mcard
		exec ('minfo = '+mcard.split('=')[-1])
		# print minfo
		# print ' \n '
		weights = []
		nums = []
		rates = []
		for entry in minfo:
			if entry[1] > 0.001:
				weights.append((1.0*entry[0])/(1.0*entry[1]))
			else:
				weights.append(0)
			nums.append(int(entry[1]))
			rates.append(entry[0])
		if nc ==1:
			standardweights = weights
		statlines = []
		spacers = -1
		rateline = 'rate '
		for h in range(len(headers)):
			head = headers[h]
			if 'Data' in head:
				continue
			spacers += 1
			nmc = nums[h]
			w = weights[h]
			if w <0.0000000001:
				w = standardweights[h]
			nmc = str(int(nmc))
			w = str(w)
			r = str(rates[h])
			statline = 'stat_'+head+' gmN '+nmc + (' - ')*spacers +' ' + w +' '+(' - ')*(len(headers) -2 - spacers)
			if nmc > 0:
				statlines.append(statline)
			rateline += ' '+r


		obsline = 'observation '+str(minfo[1][1])
		binline = 'bin '+(' 1 ')*(len(headers)-1)
		procline1 = 'process  '+card
		for hh in headers:
			if 'Sig' in hh or 'Data' in hh:
				continue
			procline1 += ' '+hh
		procline2 = 'process  0 '+(' 1 ')*(len(headers)-2)

		syslines = []
		for v in variations:
			if v == '':
				continue
			sysline = v + '  lnN  '
			this_sysset = []
			for ss in scards:
				if v in ss:
					this_sysset.append(ss)
			if len(this_sysset) == 1:
				this_sysset.append(this_sysset[0])
			exec ('sys1 = '+this_sysset[0].split('=')[-1])
			exec ('sys2 = '+this_sysset[1].split('=')[-1])
			sysline += CompareMeanSys(minfo,sys1,sys2)
			syslines.append(sysline)


		fout.write( card + '.txt\n\n')
		for configline in configlines:
			fout.write( configline+'\n')
		fout.write( obsline+'\n')
		fout.write( ' '+'\n')
		fout.write( binline+'\n')
		fout.write( procline1+'\n')
		fout.write( procline2+'\n')
		fout.write( ' '+'\n')
		fout.write( rateline+'\n')
		fout.write( ' '+'\n')
		for sysline in syslines:
			fout.write( sysline+'\n')
		fout.write( ' '+'\n')
		for statline in statlines:
			fout.write( statline+'\n')
		fout.write( '\n'*3)

	fout.close()
	return finalcards

def FixFinalCards(cardsets):
	f = cardsets[0].split('/')[0]+'/FinalCards.txt'
	fout = open(f,'w')
	for c in cardsets:
		for line in open(c,'r'):
			line = line.replace('uujj','_M_')
			line = line.replace('uvjj','_BetaHalf_M_')
			fout.write(line)
	fout.close()
	return f

def MuonTPStudy():

	__m = TFile.Open('root://eoscms//eos/cms/store/group/phys_exotica/darinb/TP2012/tagprobe_mc.root')
	__d = TFile.Open('root://eoscms//eos/cms/store/group/phys_exotica/darinb/TP2012/tagprobe_data.root')

	print 'Fetching MC tree...'
	_m = __m.Get("tpTree/fitter_tree")
	print 'Fetching Data tree...'
	_d = __d.Get("tpTree/fitter_tree")

	n_d = _d.GetEntries()
	n_m = _m.GetEntries()
	print ' '
	print 'Data Events:',n_d
	print 'MC Events:', n_m
	print ' '

	# f = TFile.Open('/tmp/'+person+'/tagprobetmp.root','RECREATE')
	# print 'Skimming MC (this may take a few minutes).'
	# dtag = _d.CopyTree('(pt>45.0)*(abseta<2.1)*(pair_nJets30>2)')
	# print 'Skimming Data (this may take a few minutes).'
	# mtag = _m.CopyTree('(pt>45.0)*(abseta<2.1)*(pair_nJets30>2)')



	np_d = 0
	np_m = 0
	np_hlt_d = 0
	np_id_d = 0
	np_id_m = 0
	np_id_hlt_d = 0
	np_hlt_id_d = 0

	binLowE = [45,50,60,80,100,150,200,600]

	hprof1  = TProfile( 'TagProbe1', '', 7, array('d',binLowE),0,1 )
	hprof1.GetXaxis().SetTitle("Muon p_{T} (GeV)")
	hprof1.GetYaxis().SetTitle("Mu40_eta2p1 [Data]")
	hprof1.SetMinimum(0.6)
	hprof1.SetMaximum(1.2)

	hprof2  = TProfile( 'TagProbe2', 'MC', 7, array('d',binLowE),0,1 )
	hprof2.GetXaxis().SetTitle("Muon p_{T} (GeV)")
	hprof2.GetYaxis().SetTitle("Tight2012")
	hprof2.SetMinimum(0.6)
	hprof2.SetMaximum(1.2)

	hprof3  = TProfile( 'TagProbe3', 'Data', 7, array('d',binLowE),0,1 )
	hprof3.GetXaxis().SetTitle("Muon p_{T} (GeV)")
	hprof3.GetYaxis().SetTitle("Tight2012")
	hprof3.SetMinimum(0.6)
	hprof3.SetMaximum(1.2)	


	for n in range(n_d):
		if n%150000==0: 
			print round(((1.0*n)/(1.0*n_d)*100.0),1) ,'%'
		_d.GetEntry(n)
		if _d.pt<45.0:
			continue
		if _d.pair_nJets30<2:
			continue
		if _d.abseta>2.1:
			continue
		if (_d.tag_pt>45)*(_d.tag_eta>-2.1)*(_d.tag_eta<2.1)*(_d.tag_combRelIso<0.1) < 1:
			continue
		np_d += 1

		di = (_d.Tight2012)*(_d.tkIso/_d.pt < 0.1)
		dh = _d.Mu40_eta2p1

		np_id_d += di
		np_hlt_d += dh

		if dh>0:
			hprof3.Fill( _d.pt, di)
			np_hlt_id_d += 1

		if di>0:
			np_id_hlt_d += dh
			hprof1.Fill( _d.pt, dh)



	for n in range(n_m):
		if n%150000==0: 
			print round(((1.0*n)/(1.0*n_m)*100.0),1) ,'%'
		_m.GetEntry(n)
		if _m.pt<45.0:
			continue
		if _m.pair_nJets30<2:
			continue
		if _m.abseta>2.1:
			continue
		if (_m.tag_pt>45)*(_m.tag_eta>-2.1)*(_m.tag_eta<2.1)*(_m.tag_combRelIso<0.1) < 1:
			continue			
		np_m += 1
		mt = _m.Tight2012
		np_id_m += mt		
	 	hprof2.Fill( _m.pt, mt)

	c1 = TCanvas( 'c1', 'c1', 200, 10, 700, 500 )
	c1.SetFillColor( 0 )
	c1.SetLogx()

	hprof1.Draw()
	c1.Print("TagProbe_Trigger_Data.png")

	c2 = TCanvas( 'c2', 'c2', 200, 10, 700, 500 )
	c2.SetFillColor( 0 )
	c2.SetLogx()


	hprof3.SetMarkerColor(2)
	hprof3.SetLineColor(2)

	hprof2.Draw()
	hprof3.Draw("SAME")

	c2.Print("TagProbe_ID.png")

	print ' '
	print 'Data Probe Events:', np_d
	print 'MC   Probe Events:', np_m
	print 'Data Probe HLT Events:', np_hlt_d
	print 'Data Probe ID  Events:', np_id_d
	print 'Data ID  Probe HLT Events:', np_id_hlt_d
	print 'Data HLT Probe ID  Events:', np_hlt_id_d
	print 'MC   Probe ID  Events:', np_id_m
	print ' '


	return [0,0]

main()
