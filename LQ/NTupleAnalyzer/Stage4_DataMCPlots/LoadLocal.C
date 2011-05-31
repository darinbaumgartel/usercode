{

//TFile f__CurrentData("/home/darinb/scratch0/LQ/Summer2011/Stage1_NTupleAnalysis/CurrentRootFiles/CurrentData_Certified_2011A_SingleMuV1V2_152_8pb.root");
TFile f__CurrentData("/home/darinb/scratch0/LQ/Summer2011/Stage1_NTupleAnalysis/CurrentRootFiles/CurrentData_Certified_April21ReReco_May2011Processing.root");
TFile f__lq("/home/darinb/scratch0/LQ/Summer2011/Stage1_NTupleAnalysis/CurrentRootFiles/LQToCMu_MuNuJJFilter_M_300.root");
TFile f__lqmumu("/home/darinb/scratch0/LQ/Summer2011/Stage1_NTupleAnalysis/CurrentRootFiles/LQToCMu_M_400.root");
TFile f__WJets("/home/darinb/scratch0/LQ/Summer2011/Stage1_NTupleAnalysis/CurrentRootFiles/Fall10PU_WJets.root");
TFile f__TTbarJets("/home/darinb/scratch0/LQ/Summer2011/Stage1_NTupleAnalysis/CurrentRootFiles/Fall10PU_TTbarJets.root");
TFile f__ZJets("/home/darinb/scratch0/LQ/Summer2011/Stage1_NTupleAnalysis/CurrentRootFiles/ZJets.root");
TFile f__VVJets("/home/darinb/scratch0/LQ/Summer2011/Stage1_NTupleAnalysis/CurrentRootFiles/VVJets.root");
TFile f__SingleTop("/home/darinb/scratch0/LQ/Summer2011/Stage1_NTupleAnalysis/CurrentRootFiles/SingleTop.root");

//TFile f__LQ250("/home/darinb/scratch0/LQ/Summer2011/Stage1_NTupleAnalysis/CurrentRootFiles/LQToCMu_MuNuJJFilter_M_250.root");

//TTree* LQToCMu_MuNuJJFilter_M_250 = (TTree* )f__LQ250->Get("PhysicalVariables");

TTree* wjets = (TTree* )f__WJets->Get("PhysicalVariables");
TTree* ttbar = (TTree* )f__TTbarJets->Get("PhysicalVariables");
TTree* zjets = (TTree* )f__ZJets->Get("PhysicalVariables");
TTree* vvjets = (TTree* )f__VVJets->Get("PhysicalVariables");
TTree* singtop = (TTree* )f__SingleTop->Get("PhysicalVariables");
TTree* data = (TTree* )f__CurrentData->Get("PhysicalVariables");
TTree* lq = (TTree* )f__lq->Get("PhysicalVariables");
TTree* lqmumu = (TTree* )f__lqmumu->Get("PhysicalVariables");


}
