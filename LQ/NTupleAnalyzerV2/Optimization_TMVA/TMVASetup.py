# Directory where root files are kept
#directory = '/afs/cern.ch/user/d/darinb/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Dec14_2011_12_14_22_39_56/SummaryFiles'
#directory = '/tmp/darinb/NTupleAnalyzer_V00_02_06_Default_StandardSelections_Dec21_4p7fb_2011_12_21_14_59_05/SummaryFiles'
#directory = '/afs/cern.ch/user/d/darinb/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_Dec27_4p7fb_2011_12_27_20_16_37/SummaryFiles'
directory = '/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan17_TEST_2012_01_17_18_23_52/SummaryFiles'
# Background root files without the .root
backgroundtags = ['TTBar','WJets_MG','ZJets_MG','SingleTop','DiBoson']

# Data root file starts with:
datatag = 'SingleMuData'

# Variables you will optimize with
#discriminatingvariables = [['M_muon1muon2','ST_pf_mumu','LowestMass_BestLQCombo','((M_bestmupfjet1_mumu > M_bestmupfjet2_mumu)*M_bestmupfjet1_mumu + (M_bestmupfjet1_mumu < M_bestmupfjet2_mumu)*M_bestmupfjet2_mumu)'],['MT_muon1pfMET','MET_pf','Pt_muon1','ST_pf_munu','M_bestmupfjet_munu','(abs(deltaPhi_muon1pfMET))','(abs(deltaPhi_pfjet1pfMET))','(abs(deltaPhi_pfjet2pfMET))']]
discriminatingvariables = [['M_muon1muon2','LowestMass_BestLQCombo','ST_pf_mumu'],['MET_pf','Pt_muon1','ST_pf_munu','M_bestmupfjet_munu']]

# Naming convention for output files
tagname = 'test'

# Tree name where variables in root file are stored
treename = 'PhysicalVariables'

# Weight for MC events
weightexpression = '4700*weight_pileup4p7fb'

# Preselections. One for each channels. Cuts out many events to speed up process. Highly recommended to have a good preselection.
preselectionmumu ='((Pt_muon1>40)*(Pt_muon2>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_mumu>250)*(deltaR_muon1muon2>0.3)*(M_muon1muon2>50)*((abs(Eta_muon1)<2.1)||(abs(Eta_muon2)<2.1)))*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5)'
#preselectionmunu = '(((Pt_muon1>40)*(Pt_muon2<15.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(FailIDPFThreshold<25.0)*(MT_muon1pfMET>50.0)*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5))'
preselectionmunu = '(((Pt_muon1>40)*(Pt_muon2<15.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(FailIDPFThreshold<25.0)*(MT_muon1pfMET>50.0))'

#preselectionenu = '(Pt_muon1>40)*(Pt_HEEPele1>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_emu>250)*(M_muon1HEEPele1>50)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.1)||(abs(Eta_HEEPele1)<2.1))';

# Signal root files will begin with the following. Can be multiple, like  LQToCMu_M_350.root and LQToCMu_M_550.root 
signaltags = ['LQToCMu_M','LQToCMu_BetaHalf_M']

# preselections correspond to above signal types
preselections = [preselectionmumu,preselectionmunu]

# MVA Methods to employ
#methods = ['CutsGA']
methods = ['Likelihood']
#methods = ['BDT','CutsGA','Likelihood','Fisher','KNN','Fisher']
#methods = ['BDT']
