

# JUST RUN THESE COMMANDS. Make sure to cmsenv before you run anything!

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_withsys_EOS.csv --autorun   -t WJetsAnalysis_5fb_Feb20  
cp -r *Feb20* ~/neuhome/LQAnalyzerOutput/ && rm -r *Feb20*

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_Feb20_JetScaleUp --jetscale 1.04
cp -r *Feb20* ~/neuhome/LQAnalyzerOutput/ && rm -r *Feb20*

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_Feb20_JetScaleDown --jetscale 0.96
cp -r *Feb20* ~/neuhome/LQAnalyzerOutput/ && rm -r *Feb20*

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_Feb20_MuScaleUp --muscale 1.01
cp -r *Feb20* ~/neuhome/LQAnalyzerOutput/ && rm -r *Feb20*

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_Feb20_MuScaleDown --muscale 0.99
cp -r *Feb20* ~/neuhome/LQAnalyzerOutput/ && rm -r *Feb20*

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_Feb20_JetSmear --jetres 1.0
cp -r *Feb20* ~/neuhome/LQAnalyzerOutput/ && rm -r *Feb20*

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun   -t WJetsAnalysis_5fb_Feb20_MuSmear --mures 0.04
cp -r *Feb20* ~/neuhome/LQAnalyzerOutput/ && rm -r *Feb20*

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets_NonIso.C -h NTupleAnalyzer_V00_02_06_WPlusJets_NonIso.h -i NTupleInfo2011_V00_02_06_WPlusJets_NonIso_EOS.csv --autorun   -t WJetsAnalysis_5fb_Feb20_NonIso 
cp -r *Feb20* ~/neuhome/LQAnalyzerOutput/ && rm -r *Feb20*

