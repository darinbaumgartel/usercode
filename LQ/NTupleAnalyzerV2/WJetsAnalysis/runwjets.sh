#!/bin/sh

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_withsys_EOS.csv --autorun --stager_check  -t WJetsAnalysis_5fb_Oct04  
rm /tmp/darinb/NT*/*root

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun --stager_check  -t WJetsAnalysis_5fb_Oct04_JetScaleUp --jetscale 1.04
rm /tmp/darinb/NT*/*root

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun --stager_check  -t WJetsAnalysis_5fb_Oct04_JetScaleDown --jetscale 0.96
rm /tmp/darinb/NT*/*root

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun --stager_check  -t WJetsAnalysis_5fb_Oct04_MuScaleUp --muscale 1.01
rm /tmp/darinb/NT*/*root

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun --stager_check  -t WJetsAnalysis_5fb_Oct04_MuScaleDown --muscale 0.99
rm /tmp/darinb/NT*/*root

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun --stager_check  -t WJetsAnalysis_5fb_Oct04_JetSmear --jetres 1.0
rm /tmp/darinb/NT*/*root

python AnalyzerMakerFastLocal.py -c NTupleAnalyzer_V00_02_06_WPlusJets.C -h NTupleAnalyzer_V00_02_06_WPlusJets.h -i NTupleInfo2011_V00_02_06_WPlusJets_EOS.csv --autorun --stager_check  -t WJetsAnalysis_5fb_Oct04_MuSmear --mures 0.04
rm /tmp/darinb/NT*/*root


