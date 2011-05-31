# Variables for cutting, starting points, interval, number of points to test
#CutVariables=['ST_pf_munu','MET_pf'] # Which variables do you want to cut on
CutVariables=['ST_pf_munu'] # Which variables do you want to cut on


#VariableStartingPoint = [140,80,50] # Where to start cutting on the variable 
#VariableInterval = [10,10,10] # Intervals in which you will test cuts
#VariablePointsToTest = [50,12,10] # Number of cutting points to test at the given interval

#VariableInterval = [10,10] # Intervals in which you will test cuts
#VariableStartingPoint = [250,50] # Where to start cutting on the variable 
#VariablePointsToTest = [60,8] # Number of cutting points to test at the given interval

VariableInterval = [10] # Intervals in which you will test cuts
VariableStartingPoint = [170] # Where to start cutting on the variable 
VariablePointsToTest = [75] # Number of cutting points to test at the given interval


# Other variable to precut on as they appear in the root file (these are not variable cuts, they are single static cuts):
#PrecutVariables=['Pt_muon1','-Pt_muon2','Pt_pfjet1','Pt_pfjet2','-1.0*deltaPhi_muon1pfMET','deltaPhi_muon1pfMET','precut_HLT','MT_muon1pfMET']
#PrecutMinValues = [30,-.001,30,30,-2.9415,.2,.5,125,]

PrecutVariables=['-Pt_muon2','-Pt_ele1','Pt_pfjet1','Pt_pfjet2','Pt_muon1','1.0*deltaPhi_muon1pfMET','deltaPhi_pfjet1pfMET','MT_muon1pfMET','MET_pf' , 'ST_pf_munu'  ]
PrecutMinValues = [-30,        -.1,      30,          30,         85,             0.8,                  .5,                        125     ,85.0  ,  250 ]

#===============================================================================================

#NonOptCutLevels=['(precut_HLT>.5)*(Pt_muon2==0.0)*(abs(deltaPhi_muon1caloMET)<2.9415)*(abs(deltaPhi_muon1caloMET)>0.2)*(Pt_muon1>30.0)*(Pt_pfjet1>30.0)*(Pt_pfjet2>30.0)','(MT_muon1pfMET>125)']
NonOptCutLevels=[
                  '(Pt_muon1>35.0)*(MET_pf>45)*(Pt_muon2<30)*(abs(deltaPhi_muon1pfMET)>0.8)*(abs(deltaPhi_pfjet1pfMET)>0.2)*(Pt_pfjet1>30.0)*(Pt_pfjet2>30.0)*(Eta_muon1<2.1)*(Eta_pfjet1<3.0)*(Eta_pfjet2<3.0)*(ST_pf_munu>250)*(Pt_ele1==0.0)',
                  '(MT_muon1pfMET>125)',
                  '((Pt_muon1>85)&&(MET_pf>85))',
                 ]
BackgroundTypes=['ZJets','WJets','VVJets','QCD','TTbarJets','SingleTop']
