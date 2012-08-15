#!/bin/sh

python AnalyzerMakerFast.py -c ExampleAnalyzers/NTupleAnalyzer_V00_02_06_Default.C -h ExampleAnalyzers/NTupleAnalyzer_V00_02_06_Default.h -i NTupleInfo2011_V00_02_06_Basic.csv --autorun --stager_check  -t StandardSelections_4p7fb_Mar13  
rm /tmp/darinb/NT*/*root

python AnalyzerMakerFast.py -c ExampleAnalyzers/NTupleAnalyzer_V00_02_06_Default.C -h ExampleAnalyzers/NTupleAnalyzer_V00_02_06_Default.h -i NTupleInfo2011_V00_02_06_Basic.csv --autorun --stager_check  -t StandardSelections_4p7fb_Mar13_JetScaleUp --jetscale 1.04
rm /tmp/darinb/NT*/*root

python AnalyzerMakerFast.py -c ExampleAnalyzers/NTupleAnalyzer_V00_02_06_Default.C -h ExampleAnalyzers/NTupleAnalyzer_V00_02_06_Default.h -i NTupleInfo2011_V00_02_06_Basic.csv --autorun --stager_check  -t StandardSelections_4p7fb_Mar13_JetScaleDown --jetscale 0.96
rm /tmp/darinb/NT*/*root

python AnalyzerMakerFast.py -c ExampleAnalyzers/NTupleAnalyzer_V00_02_06_Default.C -h ExampleAnalyzers/NTupleAnalyzer_V00_02_06_Default.h -i NTupleInfo2011_V00_02_06_Basic.csv --autorun --stager_check  -t StandardSelections_4p7fb_Mar13_MuScaleUp --muscale 1.01
rm /tmp/darinb/NT*/*root

python AnalyzerMakerFast.py -c ExampleAnalyzers/NTupleAnalyzer_V00_02_06_Default.C -h ExampleAnalyzers/NTupleAnalyzer_V00_02_06_Default.h -i NTupleInfo2011_V00_02_06_Basic.csv --autorun --stager_check  -t StandardSelections_4p7fb_Mar13_MuScaleDown --muscale 0.99
rm /tmp/darinb/NT*/*root

python AnalyzerMakerFast.py -c ExampleAnalyzers/NTupleAnalyzer_V00_02_06_Default.C -h ExampleAnalyzers/NTupleAnalyzer_V00_02_06_Default.h -i NTupleInfo2011_V00_02_06_Basic.csv --autorun --stager_check  -t StandardSelections_4p7fb_Mar13_JetSmear --jetres 1.0
rm /tmp/darinb/NT*/*root

python AnalyzerMakerFast.py -c ExampleAnalyzers/NTupleAnalyzer_V00_02_06_Default.C -h ExampleAnalyzers/NTupleAnalyzer_V00_02_06_Default.h -i NTupleInfo2011_V00_02_06_Basic.csv --autorun --stager_check  -t StandardSelections_4p7fb_Mar13_MuSmear --mures 0.04
rm /tmp/darinb/NT*/*root




