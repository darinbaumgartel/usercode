{

TFile f__CurrentData("/home/darinb/scratch0/LQ/Summer2011_PostAnalysis/RootFiles_V2_VBTF/SingleMuData.root");
//TFile f__lq("/home/darinb/scratch0/LQ/Summer2011_PostAnalysis/RootFiles_V2_VBTF/LQToCMu_MuNuJJFilter_M_300.root");
//TFile f__lqmumu("/home/darinb/scratch0/LQ/Summer2011_PostAnalysis/RootFiles_V2_VBTF/LQToCMu_M_400.root");
TFile f__WJets("/home/darinb/scratch0/LQ/Summer2011_PostAnalysis/RootFiles_V2_VBTF/WJetsMG.root");
TFile f__TTbarJets("/home/darinb/scratch0/LQ/Summer2011_PostAnalysis/RootFiles_V2_VBTF/TTBar.root");
TFile f__ZJets("/home/darinb/scratch0/LQ/Summer2011_PostAnalysis/RootFiles_V2_VBTF/ZJetsALP.root");
TFile f__VVJets("/home/darinb/scratch0/LQ/Summer2011_PostAnalysis/RootFiles_V2_VBTF/DiBoson.root");
TFile f__SingleTop("/home/darinb/scratch0/LQ/Summer2011_PostAnalysis/RootFiles_V2_VBTF/SingleTop.root");
TFile f__QCDMu("/home/darinb/scratch0/LQ/Summer2011_PostAnalysis/RootFiles_V2_VBTF/QCDMu.root");


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
