

# JUST RUN THESE COMMANDS. Make sure to cmsenv before you run anything!

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_withsys_EOS.csv --autorun   -t WJetsAnalysis_5fb_May20  

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_May20_JetScaleUp --jetscale 1.04

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_May20_JetScaleDown --jetscale 0.96

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_May20_MuScaleUp --muscale 1.01

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_May20_MuScaleDown --muscale 0.99

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_May20_JetSmear --jetres 1.0

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_May20_MuSmear --mures 0.04




python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_withsys_EOS_Sherpa.csv --autorun   -t WJetsAnalysis_5fb_May20Sherpa  


python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets_NonIso.C -h NTupleAnalyzer_V00_02_06_WPlusJets_NonIso.h -i NTupleInfo2011_V00_02_06_WPlusJets_NonIso_EOS.csv --autorun   -t WJetsAnalysis_5fb_May20_NonIso 






python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_NonIso_EOS_powheg.csv --autorun   -t WJetsAnalysis_5fb_May20_powfix  

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets_NonIso.C -h NTupleAnalyzer_V00_02_06_WPlusJets_NonIso.h -i NTupleInfo2011_V00_02_06_WPlusJets_NonIso_EOS_powheg.csv --autorun   -t WJetsAnalysis_5fb_May20_NonIso_powfix

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_May20_JetSmear --jetres 1.0



python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_ForRecoil_EOS.csv --autorun   -t WJetsAnalysis_5fb_Apr1Recoil  
