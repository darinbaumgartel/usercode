{

TFile *f__CurrentData = TFile::Open = TFile::Open("rfio:/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_VBTFTight_2011_06_10_12_28_30/SummaryFiles/SingleMuData.root");
//TFile f__lq(" rfio:/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_VBTFTight_2011_06_10_12_28_30/SummaryFiles/LQToCMu_MuNuJJFilter_M_300.root");
//TFile f__lqmumu(" rfio:/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_VBTFTight_2011_06_10_12_28_30/SummaryFiles/LQToCMu_M_400.root");
TFile *f__WJets = TFile::Open("rfio:/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_VBTFTight_2011_06_10_12_28_30/SummaryFiles/WJetsMG.root");
TFile *f__TTbarJets = TFile::Open("rfio:/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_VBTFTight_2011_06_10_12_28_30/SummaryFiles/TTBar.root");
TFile *f__ZJets = TFile::Open("rfio:/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_VBTFTight_2011_06_10_12_28_30/SummaryFiles/ZJetsMG.root");
TFile *f__VVJets = TFile::Open("rfio:/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_VBTFTight_2011_06_10_12_28_30/SummaryFiles/DiBoson.root");
TFile *f__SingleTop = TFile::Open("rfio:/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_VBTFTight_2011_06_10_12_28_30/SummaryFiles/SingleTop.root");
TFile *f__QCDMu = TFile::Open("rfio:/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_04_VBTFTight_2011_06_10_12_28_30/SummaryFiles/QCDMu.root");


TTree* wjets = (TTree* )f__WJets->Get("PhysicalVariables");
TTree* ttbar = (TTree* )f__TTbarJets->Get("PhysicalVariables");
TTree* zjets = (TTree* )f__ZJets->Get("PhysicalVariables");
TTree* vvjets = (TTree* )f__VVJets->Get("PhysicalVariables");
TTree* singtop = (TTree* )f__SingleTop->Get("PhysicalVariables");
TTree* qcd = (TTree* )f__QCDMu->Get("PhysicalVariables");
TTree* data = (TTree* )f__CurrentData->Get("PhysicalVariables");

//TTree* lq = (TTree* )f__lq->Get("PhysicalVariables");
//TTree* lqmumu = (TTree* )f__lqmumu->Get("PhysicalVariables");

}
