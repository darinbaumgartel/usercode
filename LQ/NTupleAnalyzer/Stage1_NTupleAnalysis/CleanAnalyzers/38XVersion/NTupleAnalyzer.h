//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Wed May 19 14:33:42 2010 by ROOT version 5.22/00d
// from TChain rootTupleTree/tree/
//////////////////////////////////////////////////////////

#ifndef NTupleAnalyzer_placeholder_h
#define NTupleAnalyzer_placeholder_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <iostream>
#include <TH1F.h>
class NTupleAnalyzer_placeholder {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   Bool_t          isData;
   Bool_t          isBPTX0;
   Bool_t          isBSCBeamHalo;
   Bool_t          isBSCMinBias;
   Bool_t          isBeamScraping;
   Bool_t          isPhysDeclared;
   Bool_t          isPrimaryVertex;
   Bool_t          passHighLevelNoiseFilter;
   Bool_t          passLooseNoiseFilter;
   Bool_t          passTightNoiseFilter;
   Double_t        time;
   Double_t        PtHat;
   vector<double>  *CaloJetBProbabilityBTag;
   vector<double>  *CaloJetEMF;
   vector<double>  *CaloJetEnergy;
   vector<double>  *CaloJetEnergyRaw;
   vector<double>  *CaloJetEta;
   vector<double>  *CaloJetHADF;
   vector<double>  *CaloJetPhi;
   vector<double>  *CaloJetPt;
   vector<double>  *CaloJetPtRaw;
   vector<double>  *CaloJetSigmaEta;
   vector<double>  *CaloJetSigmaPhi;
   vector<double>  *CaloJetSimpleSecondaryVertexBTag;
   vector<double>  *CaloJetSoftMuonByPtBTag;
   vector<double>  *CaloJetTrackCountingHighEffBTag;
   vector<double>  *CaloJetfHPD;
   vector<double>  *CaloJetfRBX;
   vector<double>  *CaloJetresEMF;
   vector<double>  *CaloMET;
   vector<double>  *CaloMETPhi;
   vector<double>  *CaloSumET;
   vector<double>  *ElectronCaloEnergy;
   vector<double>  *ElectronDeltaEtaTrkSC;
   vector<double>  *ElectronDeltaPhiTrkSC;
   vector<double>  *ElectronE1x5OverE5x5;
   vector<double>  *ElectronE2x5OverE5x5;
   vector<double>  *ElectronEcalIso;
   vector<double>  *ElectronEcalIsoHeep;
   vector<double>  *ElectronEnergy;
   vector<double>  *ElectronEta;
   vector<double>  *ElectronHcalIso;
   vector<double>  *ElectronHcalIsoD1Heep;
   vector<double>  *ElectronHcalIsoD2Heep;
   vector<double>  *ElectronHoE;
   vector<double>  *ElectronPhi;
   vector<double>  *ElectronPt;
   vector<double>  *ElectronRelIso;
   vector<double>  *ElectronSCEta;
   vector<double>  *ElectronSCPhi;
   vector<double>  *ElectronSCPt;
   vector<double>  *ElectronSCRawEnergy;
   vector<double>  *ElectronSigmaEtaEta;
   vector<double>  *ElectronSigmaIEtaIEta;
   vector<double>  *ElectronTrackPt;
   vector<double>  *ElectronTrkIso;
   vector<double>  *ElectronTrkIsoHeep;
   vector<double>  *PDFWeights;
   vector<double>  *GenJetEMF;
   vector<double>  *GenJetEnergy;
   vector<double>  *GenJetEta;
   vector<double>  *GenJetHADF;
   vector<double>  *GenJetP;
   vector<double>  *GenJetPhi;
   vector<double>  *GenJetPt;
   vector<double>  *GenParticleEnergy;
   vector<double>  *GenParticleEta;
   vector<double>  *GenParticleP;
   vector<double>  *GenParticlePhi;
   vector<double>  *GenParticlePt;
   vector<double>  *GenParticlePx;
   vector<double>  *GenParticlePy;
   vector<double>  *GenParticlePz;
   vector<double>  *GenParticleVX;
   vector<double>  *GenParticleVY;
   vector<double>  *GenParticleVZ;
   vector<double>  *MuonEcalIso;
   vector<double>  *MuonEnergy;
   vector<double>  *MuonEta;
   vector<double>  *MuonGlobalChi2;
   vector<double>  *MuonHOIso;
   vector<double>  *MuonHcalIso;
   vector<double>  *MuonP;
   vector<double>  *MuonPhi;
   vector<double>  *MuonPt;
   vector<double>  *MuonRelIso;
   vector<double>  *MuonTrkD0;
   vector<double>  *MuonTrkD0Error;
   vector<double>  *MuonTrkDz;
   vector<double>  *MuonTrkDzError;
   vector<double>  *MuonTrkIso;
   vector<double>  *PFJetChargedEmEnergyFraction;
   vector<double>  *PFJetChargedHadronEnergyFraction;
   vector<double>  *PFJetChargedMuEnergyFraction;
   vector<double>  *PFJetChargedMultiplicity;
   vector<double>  *PFJetEnergy;
   vector<double>  *PFJetEnergyRaw;
   vector<double>  *PFJetEta;
   vector<double>  *PFJetMuonMultiplicity;
   vector<double>  *PFJetNeutralEmEnergyFraction;
   vector<double>  *PFJetNeutralHadronEnergyFraction;
   vector<double>  *PFJetNeutralMultiplicity;
   vector<double>  *PFJetPhi;
   vector<double>  *PFJetPt;
   vector<double>  *PFJetPtRaw;
   vector<double>  *PFMET;
   vector<double>  *PFMETPhi;
   vector<double>  *PFSumET;
   vector<double>  *ElectronSCE1E9;
   vector<double>  *ElectronSCEcalIso;
   vector<double>  *ElectronSCHEEPEcalIso;
   vector<double>  *ElectronSCHEEPTrkIso;
   vector<double>  *ElectronSCS4S1;
   vector<double>  *SuperClusterDrTrack1;
   vector<double>  *SuperClusterDrTrack2;
   vector<double>  *SuperClusterE1E9;
   vector<double>  *SuperClusterEcalIso;
   vector<double>  *SuperClusterEta;
   vector<double>  *SuperClusterHEEPEcalIso;
   vector<double>  *SuperClusterHEEPTrkIso;
   vector<double>  *SuperClusterHoE;
   vector<double>  *SuperClusterPhi;
   vector<double>  *SuperClusterPt;
   vector<double>  *SuperClusterRawEnergy;
   vector<double>  *SuperClusterS4S1;
   vector<double>  *SuperClusterSigmaIEtaIEta;
   vector<double>  *SuperClusterTrack1Eta;
   vector<double>  *SuperClusterTrack1Phi;
   vector<double>  *SuperClusterTrack1Pt;
   vector<double>  *SuperClusterTrack2Eta;
   vector<double>  *SuperClusterTrack2Phi;
   vector<double>  *SuperClusterTrack2Pt;
   vector<double>  *TCMET;
   vector<double>  *TCMETPhi;
   vector<double>  *TCSumET;
   vector<int>     *CaloJetOverlaps;
   vector<int>     *CaloJetPartonFlavour;
   vector<int>     *CaloJetn90Hits;
   vector<int>     *ElectronCharge;
   vector<int>     *ElectronClassif;
   vector<int>     *ElectronHeepID;
   vector<int>     *ElectronOverlaps;
   vector<int>     *ElectronPassID;
   vector<int>     *ElectronPassIso;
   vector<int>     *GenParticleMotherIndex;
   vector<int>     *GenParticleNumDaught;
   vector<int>     *GenParticlePdgId;
   vector<int>     *GenParticleStatus;
   vector<int>     *MuonCharge;
   vector<int>     *MuonPassID;
   vector<int>     *MuonPassIso;
   vector<int>     *MuonTrkHits;
   vector<int>     *PFJetPartonFlavour;
   vector<int>     *SuperClusterClustersSize;
   vector<int>     *SuperClusterTrackMatch;
   vector<int>     *HLTBits;
   vector<int>     *HLTResults;
   vector<int>     *L1PhysBits;
   vector<int>     *L1TechBits;
   UInt_t          bunch;
   UInt_t          event;
   UInt_t          ls;
   UInt_t          orbit;
   UInt_t          run;
   UInt_t          ProcessID;

   // List of branches
   TBranch        *b_isData;   //!
   TBranch        *b_isBPTX0;   //!
   TBranch        *b_isBSCBeamHalo;   //!
   TBranch        *b_isBSCMinBias;   //!
   TBranch        *b_isBeamScraping;   //!
   TBranch        *b_isPhysDeclared;   //!
   TBranch        *b_isPrimaryVertex;   //!
   TBranch        *b_passHighLevelNoiseFilter;   //!
   TBranch        *b_passLooseNoiseFilter;   //!
   TBranch        *b_passTightNoiseFilter;   //!
   TBranch        *b_time;   //!
   TBranch        *b_PtHat;   //!
   TBranch        *b_CaloJetBProbabilityBTag;   //!
   TBranch        *b_CaloJetEMF;   //!
   TBranch        *b_CaloJetEnergy;   //!
   TBranch        *b_CaloJetEnergyRaw;   //!
   TBranch        *b_CaloJetEta;   //!
   TBranch        *b_CaloJetHADF;   //!
   TBranch        *b_CaloJetPhi;   //!
   TBranch        *b_CaloJetPt;   //!
   TBranch        *b_CaloJetPtRaw;   //!
   TBranch        *b_CaloJetSigmaEta;   //!
   TBranch        *b_CaloJetSigmaPhi;   //!
   TBranch        *b_CaloJetSimpleSecondaryVertexBTag;   //!
   TBranch        *b_CaloJetSoftMuonByPtBTag;   //!
   TBranch        *b_CaloJetTrackCountingHighEffBTag;   //!
   TBranch        *b_CaloJetfHPD;   //!
   TBranch        *b_CaloJetfRBX;   //!
   TBranch        *b_CaloJetresEMF;   //!
   TBranch        *b_CaloMET;   //!
   TBranch        *b_CaloMETPhi;   //!
   TBranch        *b_CaloSumET;   //!
   TBranch        *b_ElectronCaloEnergy;   //!
   TBranch        *b_ElectronDeltaEtaTrkSC;   //!
   TBranch        *b_ElectronDeltaPhiTrkSC;   //!
   TBranch        *b_ElectronE1x5OverE5x5;   //!
   TBranch        *b_ElectronE2x5OverE5x5;   //!
   TBranch        *b_ElectronEcalIso;   //!
   TBranch        *b_ElectronEcalIsoHeep;   //!
   TBranch        *b_ElectronEnergy;   //!
   TBranch        *b_ElectronEta;   //!
   TBranch        *b_ElectronHcalIso;   //!
   TBranch        *b_ElectronHcalIsoD1Heep;   //!
   TBranch        *b_ElectronHcalIsoD2Heep;   //!
   TBranch        *b_ElectronHoE;   //!
   TBranch        *b_ElectronPhi;   //!
   TBranch        *b_ElectronPt;   //!
   TBranch        *b_ElectronRelIso;   //!
   TBranch        *b_ElectronSCEta;   //!
   TBranch        *b_ElectronSCPhi;   //!
   TBranch        *b_ElectronSCPt;   //!
   TBranch        *b_ElectronSCRawEnergy;   //!
   TBranch        *b_ElectronSigmaEtaEta;   //!
   TBranch        *b_ElectronSigmaIEtaIEta;   //!
   TBranch        *b_ElectronTrackPt;   //!
   TBranch        *b_ElectronTrkIso;   //!
   TBranch        *b_ElectronTrkIsoHeep;   //!
   TBranch        *b_PDFWeights;   //!
   TBranch        *b_GenJetEMF;   //!
   TBranch        *b_GenJetEnergy;   //!
   TBranch        *b_GenJetEta;   //!
   TBranch        *b_GenJetHADF;   //!
   TBranch        *b_GenJetP;   //!
   TBranch        *b_GenJetPhi;   //!
   TBranch        *b_GenJetPt;   //!
   TBranch        *b_GenParticleEnergy;   //!
   TBranch        *b_GenParticleEta;   //!
   TBranch        *b_GenParticleP;   //!
   TBranch        *b_GenParticlePhi;   //!
   TBranch        *b_GenParticlePt;   //!
   TBranch        *b_GenParticlePx;   //!
   TBranch        *b_GenParticlePy;   //!
   TBranch        *b_GenParticlePz;   //!
   TBranch        *b_GenParticleVX;   //!
   TBranch        *b_GenParticleVY;   //!
   TBranch        *b_GenParticleVZ;   //!
   TBranch        *b_MuonEcalIso;   //!
   TBranch        *b_MuonEnergy;   //!
   TBranch        *b_MuonEta;   //!
   TBranch        *b_MuonGlobalChi2;   //!
   TBranch        *b_MuonHOIso;   //!
   TBranch        *b_MuonHcalIso;   //!
   TBranch        *b_MuonP;   //!
   TBranch        *b_MuonPhi;   //!
   TBranch        *b_MuonPt;   //!
   TBranch        *b_MuonRelIso;   //!
   TBranch        *b_MuonTrkD0;   //!
   TBranch        *b_MuonTrkD0Error;   //!
   TBranch        *b_MuonTrkDz;   //!
   TBranch        *b_MuonTrkDzError;   //!
   TBranch        *b_MuonTrkIso;   //!
   TBranch        *b_PFJetChargedEmEnergyFraction;   //!
   TBranch        *b_PFJetChargedHadronEnergyFraction;   //!
   TBranch        *b_PFJetChargedMuEnergyFraction;   //!
   TBranch        *b_PFJetChargedMultiplicity;   //!
   TBranch        *b_PFJetEnergy;   //!
   TBranch        *b_PFJetEnergyRaw;   //!
   TBranch        *b_PFJetEta;   //!
   TBranch        *b_PFJetMuonMultiplicity;   //!
   TBranch        *b_PFJetNeutralEmEnergyFraction;   //!
   TBranch        *b_PFJetNeutralHadronEnergyFraction;   //!
   TBranch        *b_PFJetNeutralMultiplicity;   //!
   TBranch        *b_PFJetPhi;   //!
   TBranch        *b_PFJetPt;   //!
   TBranch        *b_PFJetPtRaw;   //!
   TBranch        *b_PFMET;   //!
   TBranch        *b_PFMETPhi;   //!
   TBranch        *b_PFSumET;   //!
   TBranch        *b_ElectronSCE1E9;   //!
   TBranch        *b_ElectronSCEcalIso;   //!
   TBranch        *b_ElectronSCHEEPEcalIso;   //!
   TBranch        *b_ElectronSCHEEPTrkIso;   //!
   TBranch        *b_ElectronSCS4S1;   //!
   TBranch        *b_SuperClusterDrTrack1;   //!
   TBranch        *b_SuperClusterDrTrack2;   //!
   TBranch        *b_SuperClusterE1E9;   //!
   TBranch        *b_SuperClusterEcalIso;   //!
   TBranch        *b_SuperClusterEta;   //!
   TBranch        *b_SuperClusterHEEPEcalIso;   //!
   TBranch        *b_SuperClusterHEEPTrkIso;   //!
   TBranch        *b_SuperClusterHoE;   //!
   TBranch        *b_SuperClusterPhi;   //!
   TBranch        *b_SuperClusterPt;   //!
   TBranch        *b_SuperClusterRawEnergy;   //!
   TBranch        *b_SuperClusterS4S1;   //!
   TBranch        *b_SuperClusterSigmaIEtaIEta;   //!
   TBranch        *b_SuperClusterTrack1Eta;   //!
   TBranch        *b_SuperClusterTrack1Phi;   //!
   TBranch        *b_SuperClusterTrack1Pt;   //!
   TBranch        *b_SuperClusterTrack2Eta;   //!
   TBranch        *b_SuperClusterTrack2Phi;   //!
   TBranch        *b_SuperClusterTrack2Pt;   //!
   TBranch        *b_TCMET;   //!
   TBranch        *b_TCMETPhi;   //!
   TBranch        *b_TCSumET;   //!
   TBranch        *b_CaloJetOverlaps;   //!
   TBranch        *b_CaloJetPartonFlavour;   //!
   TBranch        *b_CaloJetn90Hits;   //!
   TBranch        *b_ElectronCharge;   //!
   TBranch        *b_ElectronClassif;   //!
   TBranch        *b_ElectronHeepID;   //!
   TBranch        *b_ElectronOverlaps;   //!
   TBranch        *b_ElectronPassID;   //!
   TBranch        *b_ElectronPassIso;   //!
   TBranch        *b_GenParticleMotherIndex;   //!
   TBranch        *b_GenParticleNumDaught;   //!
   TBranch        *b_GenParticlePdgId;   //!
   TBranch        *b_GenParticleStatus;   //!
   TBranch        *b_MuonCharge;   //!
   TBranch        *b_MuonPassID;   //!
   TBranch        *b_MuonPassIso;   //!
   TBranch        *b_MuonTrkHits;   //!
   TBranch        *b_PFJetPartonFlavour;   //!
   TBranch        *b_SuperClusterClustersSize;   //!
   TBranch        *b_SuperClusterTrackMatch;   //!
   TBranch        *b_HLTBits;   //!
   TBranch        *b_HLTResults;   //!
   TBranch        *b_L1PhysBits;   //!
   TBranch        *b_L1TechBits;   //!
   TBranch        *b_bunch;   //!
   TBranch        *b_event;   //!
   TBranch        *b_ls;   //!
   TBranch        *b_orbit;   //!
   TBranch        *b_run;   //!
   TBranch        *b_ProcessID;   //!

   NTupleAnalyzer_placeholder(TTree *tree=0);
   virtual ~NTupleAnalyzer_placeholder();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef NTupleAnalyzer_placeholder_cxx
NTupleAnalyzer_placeholder::NTupleAnalyzer_placeholder(TTree *tree)

{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {

#ifdef SINGLE_TREE
      // The following code should be used if you want this class to access
      // a single tree instead of a chain
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("Memory Directory");
      if (!f) {
         f = new TFile("Memory Directory");
         f->cd("Rint:/");
      }
      tree = (TTree*)gDirectory->Get("rootTupleTree/tree");

#else // SINGLE_TREE

// DO NOT REMOVE THE COMMENT BELOW:::::
// REGISTER YOUR RELEVANT FILE CHAINS BELOW:: filetracermark000
    
//    TChain * chain_ZmumuJet_Pt300toInf = new TChain("treeCreator/RootTupleMakerPAT","");
//      chain_ZmumuJet_Pt300toInf->Add("/home/darinb/scratch0/data_7TeV/ZmumuJet_Pt300toInf_Summer09-MC_31X_V3_7TeV-v1_GEN-SIM-RECO_count_1.root");
      
//      TChain * chain = new TChain("treeCreator/RootTupleMakerPAT","");
//      chain=chain_placeholder;
      
      tree = chain;

#endif // SINGLE_TREE

   }
   Init(tree);
}

NTupleAnalyzer_placeholder::~NTupleAnalyzer_placeholder()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t NTupleAnalyzer_placeholder::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t NTupleAnalyzer_placeholder::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (!fChain->InheritsFrom(TChain::Class()))  return centry;
   TChain *chain = (TChain*)fChain;
   if (chain->GetTreeNumber() != fCurrent) {
      fCurrent = chain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void NTupleAnalyzer_placeholder::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   CaloJetBProbabilityBTag = 0;
   CaloJetEMF = 0;
   CaloJetEnergy = 0;
   CaloJetEnergyRaw = 0;
   CaloJetEta = 0;
   CaloJetHADF = 0;
   CaloJetPhi = 0;
   CaloJetPt = 0;
   CaloJetPtRaw = 0;
   CaloJetSigmaEta = 0;
   CaloJetSigmaPhi = 0;
   CaloJetSimpleSecondaryVertexBTag = 0;
   CaloJetSoftMuonByPtBTag = 0;
   CaloJetTrackCountingHighEffBTag = 0;
   CaloJetfHPD = 0;
   CaloJetfRBX = 0;
   CaloJetresEMF = 0;
   CaloMET = 0;
   CaloMETPhi = 0;
   CaloSumET = 0;
   ElectronCaloEnergy = 0;
   ElectronDeltaEtaTrkSC = 0;
   ElectronDeltaPhiTrkSC = 0;
   ElectronE1x5OverE5x5 = 0;
   ElectronE2x5OverE5x5 = 0;
   ElectronEcalIso = 0;
   ElectronEcalIsoHeep = 0;
   ElectronEnergy = 0;
   ElectronEta = 0;
   ElectronHcalIso = 0;
   ElectronHcalIsoD1Heep = 0;
   ElectronHcalIsoD2Heep = 0;
   ElectronHoE = 0;
   ElectronPhi = 0;
   ElectronPt = 0;
   ElectronRelIso = 0;
   ElectronSCEta = 0;
   ElectronSCPhi = 0;
   ElectronSCPt = 0;
   ElectronSCRawEnergy = 0;
   ElectronSigmaEtaEta = 0;
   ElectronSigmaIEtaIEta = 0;
   ElectronTrackPt = 0;
   ElectronTrkIso = 0;
   ElectronTrkIsoHeep = 0;
   PDFWeights = 0;
   GenJetEMF = 0;
   GenJetEnergy = 0;
   GenJetEta = 0;
   GenJetHADF = 0;
   GenJetP = 0;
   GenJetPhi = 0;
   GenJetPt = 0;
   GenParticleEnergy = 0;
   GenParticleEta = 0;
   GenParticleP = 0;
   GenParticlePhi = 0;
   GenParticlePt = 0;
   GenParticlePx = 0;
   GenParticlePy = 0;
   GenParticlePz = 0;
   GenParticleVX = 0;
   GenParticleVY = 0;
   GenParticleVZ = 0;
   MuonEcalIso = 0;
   MuonEnergy = 0;
   MuonEta = 0;
   MuonGlobalChi2 = 0;
   MuonHOIso = 0;
   MuonHcalIso = 0;
   MuonP = 0;
   MuonPhi = 0;
   MuonPt = 0;
   MuonRelIso = 0;
   MuonTrkD0 = 0;
   MuonTrkD0Error = 0;
   MuonTrkDz = 0;
   MuonTrkDzError = 0;
   MuonTrkIso = 0;
   PFJetChargedEmEnergyFraction = 0;
   PFJetChargedHadronEnergyFraction = 0;
   PFJetChargedMuEnergyFraction = 0;
   PFJetChargedMultiplicity = 0;
   PFJetEnergy = 0;
   PFJetEnergyRaw = 0;
   PFJetEta = 0;
   PFJetMuonMultiplicity = 0;
   PFJetNeutralEmEnergyFraction = 0;
   PFJetNeutralHadronEnergyFraction = 0;
   PFJetNeutralMultiplicity = 0;
   PFJetPhi = 0;
   PFJetPt = 0;
   PFJetPtRaw = 0;
   PFMET = 0;
   PFMETPhi = 0;
   PFSumET = 0;
   ElectronSCE1E9 = 0;
   ElectronSCEcalIso = 0;
   ElectronSCHEEPEcalIso = 0;
   ElectronSCHEEPTrkIso = 0;
   ElectronSCS4S1 = 0;
   SuperClusterDrTrack1 = 0;
   SuperClusterDrTrack2 = 0;
   SuperClusterE1E9 = 0;
   SuperClusterEcalIso = 0;
   SuperClusterEta = 0;
   SuperClusterHEEPEcalIso = 0;
   SuperClusterHEEPTrkIso = 0;
   SuperClusterHoE = 0;
   SuperClusterPhi = 0;
   SuperClusterPt = 0;
   SuperClusterRawEnergy = 0;
   SuperClusterS4S1 = 0;
   SuperClusterSigmaIEtaIEta = 0;
   SuperClusterTrack1Eta = 0;
   SuperClusterTrack1Phi = 0;
   SuperClusterTrack1Pt = 0;
   SuperClusterTrack2Eta = 0;
   SuperClusterTrack2Phi = 0;
   SuperClusterTrack2Pt = 0;
   TCMET = 0;
   TCMETPhi = 0;
   TCSumET = 0;
   CaloJetOverlaps = 0;
   CaloJetPartonFlavour = 0;
   CaloJetn90Hits = 0;
   ElectronCharge = 0;
   ElectronClassif = 0;
   ElectronHeepID = 0;
   ElectronOverlaps = 0;
   ElectronPassID = 0;
   ElectronPassIso = 0;
   GenParticleMotherIndex = 0;
   GenParticleNumDaught = 0;
   GenParticlePdgId = 0;
   GenParticleStatus = 0;
   MuonCharge = 0;
   MuonPassID = 0;
   MuonPassIso = 0;
   MuonTrkHits = 0;
   PFJetPartonFlavour = 0;
   SuperClusterClustersSize = 0;
   SuperClusterTrackMatch = 0;
   HLTBits = 0;
   HLTResults = 0;
   L1PhysBits = 0;
   L1TechBits = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("isData", &isData, &b_isData);
   fChain->SetBranchAddress("isBPTX0", &isBPTX0, &b_isBPTX0);
   fChain->SetBranchAddress("isBSCBeamHalo", &isBSCBeamHalo, &b_isBSCBeamHalo);
   fChain->SetBranchAddress("isBSCMinBias", &isBSCMinBias, &b_isBSCMinBias);
   fChain->SetBranchAddress("isBeamScraping", &isBeamScraping, &b_isBeamScraping);
   fChain->SetBranchAddress("isPhysDeclared", &isPhysDeclared, &b_isPhysDeclared);
   fChain->SetBranchAddress("isPrimaryVertex", &isPrimaryVertex, &b_isPrimaryVertex);
   fChain->SetBranchAddress("passHighLevelNoiseFilter", &passHighLevelNoiseFilter, &b_passHighLevelNoiseFilter);
   fChain->SetBranchAddress("passLooseNoiseFilter", &passLooseNoiseFilter, &b_passLooseNoiseFilter);
   fChain->SetBranchAddress("passTightNoiseFilter", &passTightNoiseFilter, &b_passTightNoiseFilter);
   fChain->SetBranchAddress("time", &time, &b_time);
   fChain->SetBranchAddress("PtHat", &PtHat, &b_PtHat);
   fChain->SetBranchAddress("CaloJetBProbabilityBTag", &CaloJetBProbabilityBTag, &b_CaloJetBProbabilityBTag);
   fChain->SetBranchAddress("CaloJetEMF", &CaloJetEMF, &b_CaloJetEMF);
   fChain->SetBranchAddress("CaloJetEnergy", &CaloJetEnergy, &b_CaloJetEnergy);
   fChain->SetBranchAddress("CaloJetEnergyRaw", &CaloJetEnergyRaw, &b_CaloJetEnergyRaw);
   fChain->SetBranchAddress("CaloJetEta", &CaloJetEta, &b_CaloJetEta);
   fChain->SetBranchAddress("CaloJetHADF", &CaloJetHADF, &b_CaloJetHADF);
   fChain->SetBranchAddress("CaloJetPhi", &CaloJetPhi, &b_CaloJetPhi);
   fChain->SetBranchAddress("CaloJetPt", &CaloJetPt, &b_CaloJetPt);
   fChain->SetBranchAddress("CaloJetPtRaw", &CaloJetPtRaw, &b_CaloJetPtRaw);
   fChain->SetBranchAddress("CaloJetSigmaEta", &CaloJetSigmaEta, &b_CaloJetSigmaEta);
   fChain->SetBranchAddress("CaloJetSigmaPhi", &CaloJetSigmaPhi, &b_CaloJetSigmaPhi);
   fChain->SetBranchAddress("CaloJetSimpleSecondaryVertexBTag", &CaloJetSimpleSecondaryVertexBTag, &b_CaloJetSimpleSecondaryVertexBTag);
   fChain->SetBranchAddress("CaloJetSoftMuonByPtBTag", &CaloJetSoftMuonByPtBTag, &b_CaloJetSoftMuonByPtBTag);
   fChain->SetBranchAddress("CaloJetTrackCountingHighEffBTag", &CaloJetTrackCountingHighEffBTag, &b_CaloJetTrackCountingHighEffBTag);
   fChain->SetBranchAddress("CaloJetfHPD", &CaloJetfHPD, &b_CaloJetfHPD);
   fChain->SetBranchAddress("CaloJetfRBX", &CaloJetfRBX, &b_CaloJetfRBX);
   fChain->SetBranchAddress("CaloJetresEMF", &CaloJetresEMF, &b_CaloJetresEMF);
   fChain->SetBranchAddress("CaloMET", &CaloMET, &b_CaloMET);
   fChain->SetBranchAddress("CaloMETPhi", &CaloMETPhi, &b_CaloMETPhi);
   fChain->SetBranchAddress("CaloSumET", &CaloSumET, &b_CaloSumET);
   fChain->SetBranchAddress("ElectronCaloEnergy", &ElectronCaloEnergy, &b_ElectronCaloEnergy);
   fChain->SetBranchAddress("ElectronDeltaEtaTrkSC", &ElectronDeltaEtaTrkSC, &b_ElectronDeltaEtaTrkSC);
   fChain->SetBranchAddress("ElectronDeltaPhiTrkSC", &ElectronDeltaPhiTrkSC, &b_ElectronDeltaPhiTrkSC);
   fChain->SetBranchAddress("ElectronE1x5OverE5x5", &ElectronE1x5OverE5x5, &b_ElectronE1x5OverE5x5);
   fChain->SetBranchAddress("ElectronE2x5OverE5x5", &ElectronE2x5OverE5x5, &b_ElectronE2x5OverE5x5);
   fChain->SetBranchAddress("ElectronEcalIso", &ElectronEcalIso, &b_ElectronEcalIso);
   fChain->SetBranchAddress("ElectronEcalIsoHeep", &ElectronEcalIsoHeep, &b_ElectronEcalIsoHeep);
   fChain->SetBranchAddress("ElectronEnergy", &ElectronEnergy, &b_ElectronEnergy);
   fChain->SetBranchAddress("ElectronEta", &ElectronEta, &b_ElectronEta);
   fChain->SetBranchAddress("ElectronHcalIso", &ElectronHcalIso, &b_ElectronHcalIso);
   fChain->SetBranchAddress("ElectronHcalIsoD1Heep", &ElectronHcalIsoD1Heep, &b_ElectronHcalIsoD1Heep);
   fChain->SetBranchAddress("ElectronHcalIsoD2Heep", &ElectronHcalIsoD2Heep, &b_ElectronHcalIsoD2Heep);
   fChain->SetBranchAddress("ElectronHoE", &ElectronHoE, &b_ElectronHoE);
   fChain->SetBranchAddress("ElectronPhi", &ElectronPhi, &b_ElectronPhi);
   fChain->SetBranchAddress("ElectronPt", &ElectronPt, &b_ElectronPt);
   fChain->SetBranchAddress("ElectronRelIso", &ElectronRelIso, &b_ElectronRelIso);
   fChain->SetBranchAddress("ElectronSCEta", &ElectronSCEta, &b_ElectronSCEta);
   fChain->SetBranchAddress("ElectronSCPhi", &ElectronSCPhi, &b_ElectronSCPhi);
   fChain->SetBranchAddress("ElectronSCPt", &ElectronSCPt, &b_ElectronSCPt);
   fChain->SetBranchAddress("ElectronSCRawEnergy", &ElectronSCRawEnergy, &b_ElectronSCRawEnergy);
   fChain->SetBranchAddress("ElectronSigmaEtaEta", &ElectronSigmaEtaEta, &b_ElectronSigmaEtaEta);
   fChain->SetBranchAddress("ElectronSigmaIEtaIEta", &ElectronSigmaIEtaIEta, &b_ElectronSigmaIEtaIEta);
   fChain->SetBranchAddress("ElectronTrackPt", &ElectronTrackPt, &b_ElectronTrackPt);
   fChain->SetBranchAddress("ElectronTrkIso", &ElectronTrkIso, &b_ElectronTrkIso);
   fChain->SetBranchAddress("ElectronTrkIsoHeep", &ElectronTrkIsoHeep, &b_ElectronTrkIsoHeep);
   fChain->SetBranchAddress("PDFWeights", &PDFWeights, &b_PDFWeights);
   fChain->SetBranchAddress("GenJetEMF", &GenJetEMF, &b_GenJetEMF);
   fChain->SetBranchAddress("GenJetEnergy", &GenJetEnergy, &b_GenJetEnergy);
   fChain->SetBranchAddress("GenJetEta", &GenJetEta, &b_GenJetEta);
   fChain->SetBranchAddress("GenJetHADF", &GenJetHADF, &b_GenJetHADF);
   fChain->SetBranchAddress("GenJetP", &GenJetP, &b_GenJetP);
   fChain->SetBranchAddress("GenJetPhi", &GenJetPhi, &b_GenJetPhi);
   fChain->SetBranchAddress("GenJetPt", &GenJetPt, &b_GenJetPt);
   fChain->SetBranchAddress("GenParticleEnergy", &GenParticleEnergy, &b_GenParticleEnergy);
   fChain->SetBranchAddress("GenParticleEta", &GenParticleEta, &b_GenParticleEta);
   fChain->SetBranchAddress("GenParticleP", &GenParticleP, &b_GenParticleP);
   fChain->SetBranchAddress("GenParticlePhi", &GenParticlePhi, &b_GenParticlePhi);
   fChain->SetBranchAddress("GenParticlePt", &GenParticlePt, &b_GenParticlePt);
   fChain->SetBranchAddress("GenParticlePx", &GenParticlePx, &b_GenParticlePx);
   fChain->SetBranchAddress("GenParticlePy", &GenParticlePy, &b_GenParticlePy);
   fChain->SetBranchAddress("GenParticlePz", &GenParticlePz, &b_GenParticlePz);
   fChain->SetBranchAddress("GenParticleVX", &GenParticleVX, &b_GenParticleVX);
   fChain->SetBranchAddress("GenParticleVY", &GenParticleVY, &b_GenParticleVY);
   fChain->SetBranchAddress("GenParticleVZ", &GenParticleVZ, &b_GenParticleVZ);
   fChain->SetBranchAddress("MuonEcalIso", &MuonEcalIso, &b_MuonEcalIso);
   fChain->SetBranchAddress("MuonEnergy", &MuonEnergy, &b_MuonEnergy);
   fChain->SetBranchAddress("MuonEta", &MuonEta, &b_MuonEta);
   fChain->SetBranchAddress("MuonGlobalChi2", &MuonGlobalChi2, &b_MuonGlobalChi2);
   fChain->SetBranchAddress("MuonHOIso", &MuonHOIso, &b_MuonHOIso);
   fChain->SetBranchAddress("MuonHcalIso", &MuonHcalIso, &b_MuonHcalIso);
   fChain->SetBranchAddress("MuonP", &MuonP, &b_MuonP);
   fChain->SetBranchAddress("MuonPhi", &MuonPhi, &b_MuonPhi);
   fChain->SetBranchAddress("MuonPt", &MuonPt, &b_MuonPt);
   fChain->SetBranchAddress("MuonRelIso", &MuonRelIso, &b_MuonRelIso);
   fChain->SetBranchAddress("MuonTrkD0", &MuonTrkD0, &b_MuonTrkD0);
   fChain->SetBranchAddress("MuonTrkD0Error", &MuonTrkD0Error, &b_MuonTrkD0Error);
   fChain->SetBranchAddress("MuonTrkDz", &MuonTrkDz, &b_MuonTrkDz);
   fChain->SetBranchAddress("MuonTrkDzError", &MuonTrkDzError, &b_MuonTrkDzError);
   fChain->SetBranchAddress("MuonTrkIso", &MuonTrkIso, &b_MuonTrkIso);
   fChain->SetBranchAddress("PFJetChargedEmEnergyFraction", &PFJetChargedEmEnergyFraction, &b_PFJetChargedEmEnergyFraction);
   fChain->SetBranchAddress("PFJetChargedHadronEnergyFraction", &PFJetChargedHadronEnergyFraction, &b_PFJetChargedHadronEnergyFraction);
   fChain->SetBranchAddress("PFJetChargedMuEnergyFraction", &PFJetChargedMuEnergyFraction, &b_PFJetChargedMuEnergyFraction);
   fChain->SetBranchAddress("PFJetChargedMultiplicity", &PFJetChargedMultiplicity, &b_PFJetChargedMultiplicity);
   fChain->SetBranchAddress("PFJetEnergy", &PFJetEnergy, &b_PFJetEnergy);
   fChain->SetBranchAddress("PFJetEnergyRaw", &PFJetEnergyRaw, &b_PFJetEnergyRaw);
   fChain->SetBranchAddress("PFJetEta", &PFJetEta, &b_PFJetEta);
   fChain->SetBranchAddress("PFJetMuonMultiplicity", &PFJetMuonMultiplicity, &b_PFJetMuonMultiplicity);
   fChain->SetBranchAddress("PFJetNeutralEmEnergyFraction", &PFJetNeutralEmEnergyFraction, &b_PFJetNeutralEmEnergyFraction);
   fChain->SetBranchAddress("PFJetNeutralHadronEnergyFraction", &PFJetNeutralHadronEnergyFraction, &b_PFJetNeutralHadronEnergyFraction);
   fChain->SetBranchAddress("PFJetNeutralMultiplicity", &PFJetNeutralMultiplicity, &b_PFJetNeutralMultiplicity);
   fChain->SetBranchAddress("PFJetPhi", &PFJetPhi, &b_PFJetPhi);
   fChain->SetBranchAddress("PFJetPt", &PFJetPt, &b_PFJetPt);
   fChain->SetBranchAddress("PFJetPtRaw", &PFJetPtRaw, &b_PFJetPtRaw);
   fChain->SetBranchAddress("PFMET", &PFMET, &b_PFMET);
   fChain->SetBranchAddress("PFMETPhi", &PFMETPhi, &b_PFMETPhi);
   fChain->SetBranchAddress("PFSumET", &PFSumET, &b_PFSumET);
   fChain->SetBranchAddress("ElectronSCE1E9", &ElectronSCE1E9, &b_ElectronSCE1E9);
   fChain->SetBranchAddress("ElectronSCEcalIso", &ElectronSCEcalIso, &b_ElectronSCEcalIso);
   fChain->SetBranchAddress("ElectronSCHEEPEcalIso", &ElectronSCHEEPEcalIso, &b_ElectronSCHEEPEcalIso);
   fChain->SetBranchAddress("ElectronSCHEEPTrkIso", &ElectronSCHEEPTrkIso, &b_ElectronSCHEEPTrkIso);
   fChain->SetBranchAddress("ElectronSCS4S1", &ElectronSCS4S1, &b_ElectronSCS4S1);
   fChain->SetBranchAddress("SuperClusterDrTrack1", &SuperClusterDrTrack1, &b_SuperClusterDrTrack1);
   fChain->SetBranchAddress("SuperClusterDrTrack2", &SuperClusterDrTrack2, &b_SuperClusterDrTrack2);
   fChain->SetBranchAddress("SuperClusterE1E9", &SuperClusterE1E9, &b_SuperClusterE1E9);
   fChain->SetBranchAddress("SuperClusterEcalIso", &SuperClusterEcalIso, &b_SuperClusterEcalIso);
   fChain->SetBranchAddress("SuperClusterEta", &SuperClusterEta, &b_SuperClusterEta);
   fChain->SetBranchAddress("SuperClusterHEEPEcalIso", &SuperClusterHEEPEcalIso, &b_SuperClusterHEEPEcalIso);
   fChain->SetBranchAddress("SuperClusterHEEPTrkIso", &SuperClusterHEEPTrkIso, &b_SuperClusterHEEPTrkIso);
   fChain->SetBranchAddress("SuperClusterHoE", &SuperClusterHoE, &b_SuperClusterHoE);
   fChain->SetBranchAddress("SuperClusterPhi", &SuperClusterPhi, &b_SuperClusterPhi);
   fChain->SetBranchAddress("SuperClusterPt", &SuperClusterPt, &b_SuperClusterPt);
   fChain->SetBranchAddress("SuperClusterRawEnergy", &SuperClusterRawEnergy, &b_SuperClusterRawEnergy);
   fChain->SetBranchAddress("SuperClusterS4S1", &SuperClusterS4S1, &b_SuperClusterS4S1);
   fChain->SetBranchAddress("SuperClusterSigmaIEtaIEta", &SuperClusterSigmaIEtaIEta, &b_SuperClusterSigmaIEtaIEta);
   fChain->SetBranchAddress("SuperClusterTrack1Eta", &SuperClusterTrack1Eta, &b_SuperClusterTrack1Eta);
   fChain->SetBranchAddress("SuperClusterTrack1Phi", &SuperClusterTrack1Phi, &b_SuperClusterTrack1Phi);
   fChain->SetBranchAddress("SuperClusterTrack1Pt", &SuperClusterTrack1Pt, &b_SuperClusterTrack1Pt);
   fChain->SetBranchAddress("SuperClusterTrack2Eta", &SuperClusterTrack2Eta, &b_SuperClusterTrack2Eta);
   fChain->SetBranchAddress("SuperClusterTrack2Phi", &SuperClusterTrack2Phi, &b_SuperClusterTrack2Phi);
   fChain->SetBranchAddress("SuperClusterTrack2Pt", &SuperClusterTrack2Pt, &b_SuperClusterTrack2Pt);
   fChain->SetBranchAddress("TCMET", &TCMET, &b_TCMET);
   fChain->SetBranchAddress("TCMETPhi", &TCMETPhi, &b_TCMETPhi);
   fChain->SetBranchAddress("TCSumET", &TCSumET, &b_TCSumET);
   fChain->SetBranchAddress("CaloJetOverlaps", &CaloJetOverlaps, &b_CaloJetOverlaps);
   fChain->SetBranchAddress("CaloJetPartonFlavour", &CaloJetPartonFlavour, &b_CaloJetPartonFlavour);
   fChain->SetBranchAddress("CaloJetn90Hits", &CaloJetn90Hits, &b_CaloJetn90Hits);
   fChain->SetBranchAddress("ElectronCharge", &ElectronCharge, &b_ElectronCharge);
   fChain->SetBranchAddress("ElectronClassif", &ElectronClassif, &b_ElectronClassif);
   fChain->SetBranchAddress("ElectronHeepID", &ElectronHeepID, &b_ElectronHeepID);
   fChain->SetBranchAddress("ElectronOverlaps", &ElectronOverlaps, &b_ElectronOverlaps);
   fChain->SetBranchAddress("ElectronPassID", &ElectronPassID, &b_ElectronPassID);
   fChain->SetBranchAddress("ElectronPassIso", &ElectronPassIso, &b_ElectronPassIso);
   fChain->SetBranchAddress("GenParticleMotherIndex", &GenParticleMotherIndex, &b_GenParticleMotherIndex);
   fChain->SetBranchAddress("GenParticleNumDaught", &GenParticleNumDaught, &b_GenParticleNumDaught);
   fChain->SetBranchAddress("GenParticlePdgId", &GenParticlePdgId, &b_GenParticlePdgId);
   fChain->SetBranchAddress("GenParticleStatus", &GenParticleStatus, &b_GenParticleStatus);
   fChain->SetBranchAddress("MuonCharge", &MuonCharge, &b_MuonCharge);
   fChain->SetBranchAddress("MuonPassID", &MuonPassID, &b_MuonPassID);
   fChain->SetBranchAddress("MuonPassIso", &MuonPassIso, &b_MuonPassIso);
   fChain->SetBranchAddress("MuonTrkHits", &MuonTrkHits, &b_MuonTrkHits);
   fChain->SetBranchAddress("PFJetPartonFlavour", &PFJetPartonFlavour, &b_PFJetPartonFlavour);
   fChain->SetBranchAddress("SuperClusterClustersSize", &SuperClusterClustersSize, &b_SuperClusterClustersSize);
   fChain->SetBranchAddress("SuperClusterTrackMatch", &SuperClusterTrackMatch, &b_SuperClusterTrackMatch);
   fChain->SetBranchAddress("HLTBits", &HLTBits, &b_HLTBits);
   fChain->SetBranchAddress("HLTResults", &HLTResults, &b_HLTResults);
   fChain->SetBranchAddress("L1PhysBits", &L1PhysBits, &b_L1PhysBits);
   fChain->SetBranchAddress("L1TechBits", &L1TechBits, &b_L1TechBits);
   fChain->SetBranchAddress("bunch", &bunch, &b_bunch);
   fChain->SetBranchAddress("event", &event, &b_event);
   fChain->SetBranchAddress("ls", &ls, &b_ls);
   fChain->SetBranchAddress("orbit", &orbit, &b_orbit);
   fChain->SetBranchAddress("run", &run, &b_run);
   fChain->SetBranchAddress("ProcessID", &ProcessID, &b_ProcessID);
   Notify();

}

Bool_t NTupleAnalyzer_placeholder::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void NTupleAnalyzer_placeholder::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t NTupleAnalyzer_placeholder::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
float WHY=entry;
WHY=0;
   return 1;
}
#endif // #ifdef NTupleAnalyzer_placeholder_cxx
