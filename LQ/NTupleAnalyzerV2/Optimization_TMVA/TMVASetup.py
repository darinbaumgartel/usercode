directory = '/afs/cern.ch/user/d/darinb/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_StandardSelections_PostLP_2fb_2011_08_24_05_33_55/SummaryFiles'

signaltags = ['LQToCMu_M',
'LQToCMu_BetaHalf_M']

backgroundtags = ['TTBar','WJets','ZJets','SingleTop']

discriminatingvariables = [['Pt_muon1','Pt_pfjet1','Pt_muon2','Pt_pfjet2','M_muon1muon2'],['Pt_muon1','Pt_pfjet1','Pt_pfjet2','MET_pf']]

tagname = 'test'

treename = 'PhysicalVariables'

weightexpression = '2000.0*weight'

preselectionmumu ='((Pt_muon1>40)*(Pt_muon2>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_mumu>250)*(deltaR_muon1muon2>0.3)*(M_muon1muon2>50)*((abs(Eta_muon1)<2.1)||(abs(Eta_muon2)<2.1)))'
preselectionmunu = '(((Pt_muon1>40)*(Pt_muon2<15.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5)*(FailIDPFThreshold<25.0)*(MT_muon1pfMET>50.0))'
preselectionenu = '(Pt_muon1>40)*(Pt_HEEPele1>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_emu>250)*(M_muon1HEEPele1>50)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.1)||(abs(Eta_HEEPele1)<2.1))';

preselections = [preselectionmumu,preselectionmunu]

methods = [ 'Fisher', 'KNN', 'LikelihoodD']
