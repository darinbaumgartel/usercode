//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Sat Mar  5 14:33:03 2011 by ROOT version 5.26/00
// from TTree tree/
// found on file: RootNtuple2011Feb10_Run2010A_Nov4ReReco_ALL_20110211_172658.root
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
   Bool_t          passHBHENoiseFilter;
   vector<bool>    *VertexIsFake;
   Double_t        time;
   Double_t        PtHat;
   vector<double>  *CaloJetEMF;
   vector<double>  *CaloJetEnergy;
   vector<double>  *CaloJetEnergyRaw;
   vector<double>  *CaloJetEta;
   vector<double>  *CaloJetHADF;
   vector<double>  *CaloJetJECUnc;
   vector<double>  *CaloJetJetBProbabilityBTag;
   vector<double>  *CaloJetJetProbabilityBTag;
   vector<double>  *CaloJetPhi;
   vector<double>  *CaloJetPt;
   vector<double>  *CaloJetPtRaw;
   vector<double>  *CaloJetResJEC;
   vector<double>  *CaloJetSigmaEta;
   vector<double>  *CaloJetSigmaPhi;
   vector<double>  *CaloJetSimpleSecondaryVertexHighEffBTag;
   vector<double>  *CaloJetSimpleSecondaryVertexHighPurBTag;
   vector<double>  *CaloJetTrackCountingHighEffBTag;
   vector<double>  *CaloJetTrackCountingHighPurBTag;
   vector<double>  *CaloJetfHPD;
   vector<double>  *CaloJetfRBX;
   vector<double>  *CaloJetresEMF;
   vector<double>  *CaloMET;
   vector<double>  *CaloMETPhi;
   vector<double>  *CaloMETPhiUncorr;
   vector<double>  *CaloMETUncorr;
   vector<double>  *CaloSumET;
   vector<double>  *CaloSumETUncorr;
   vector<double>  *ElectronCaloEnergy;
   vector<double>  *ElectronDCotTheta;
   vector<double>  *ElectronDeltaEtaTrkSC;
   vector<double>  *ElectronDeltaPhiTrkSC;
   vector<double>  *ElectronDist;
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
   vector<double>  *ElectronVtxDistXY;
   vector<double>  *ElectronVtxDistZ;
   vector<double>  *PDFWeights;
   vector<double>  *GenJetEMF;
   vector<double>  *GenJetEnergy;
   vector<double>  *GenJetEta;
   vector<double>  *GenJetHADF;
   vector<double>  *GenJetP;
   vector<double>  *GenJetPhi;
   vector<double>  *GenJetPt;
   vector<double>  *GenMETPhiTrue;
   vector<double>  *GenMETTrue;
   vector<double>  *GenSumETTrue;
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
   vector<double>  *MuonVtxDistXY;
   vector<double>  *MuonVtxDistZ;
   vector<double>  *PFJetChargedEmEnergyFraction;
   vector<double>  *PFJetChargedHadronEnergyFraction;
   vector<double>  *PFJetChargedMuEnergyFraction;
   vector<double>  *PFJetElectronEnergyFraction;
   vector<double>  *PFJetEnergy;
   vector<double>  *PFJetEnergyRaw;
   vector<double>  *PFJetEta;
   vector<double>  *PFJetJECUnc;
   vector<double>  *PFJetJetBProbabilityBTag;
   vector<double>  *PFJetJetProbabilityBTag;
   vector<double>  *PFJetMuonEnergyFraction;
   vector<double>  *PFJetNeutralEmEnergyFraction;
   vector<double>  *PFJetNeutralHadronEnergyFraction;
   vector<double>  *PFJetPhi;
   vector<double>  *PFJetPhotonEnergyFraction;
   vector<double>  *PFJetPt;
   vector<double>  *PFJetPtRaw;
   vector<double>  *PFJetResJEC;
   vector<double>  *PFJetSimpleSecondaryVertexHighEffBTag;
   vector<double>  *PFJetSimpleSecondaryVertexHighPurBTag;
   vector<double>  *PFJetTrackCountingHighEffBTag;
   vector<double>  *PFJetTrackCountingHighPurBTag;
   vector<double>  *PFMET;
   vector<double>  *PFMETPhi;
   vector<double>  *PFSumET;
   vector<double>  *PFMETPhiType1Cor;
   vector<double>  *PFMETType1Cor;
   vector<double>  *PFSumETType1Cor;
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
   vector<double>  *VertexChi2;
   vector<double>  *VertexNDF;
   vector<double>  *VertexRho;
   vector<double>  *VertexX;
   vector<double>  *VertexXErr;
   vector<double>  *VertexY;
   vector<double>  *VertexYErr;
   vector<double>  *VertexZ;
   vector<double>  *VertexZErr;
   vector<int>     *CaloJetOverlaps;
   vector<int>     *CaloJetPartonFlavour;
   vector<int>     *CaloJetPassLooseID;
   vector<int>     *CaloJetPassTightID;
   vector<int>     *CaloJetn90Hits;
   vector<int>     *ElectronCharge;
   vector<int>     *ElectronClassif;
   vector<int>     *ElectronHeepID;
   vector<int>     *ElectronMissingHits;
   vector<int>     *ElectronOverlaps;
   vector<int>     *ElectronPassID;
   vector<int>     *ElectronPassIso;
   vector<int>     *ElectronVtxIndex;
   vector<int>     *GenParticleMotherIndex;
   vector<int>     *GenParticleNumDaught;
   vector<int>     *GenParticlePdgId;
   vector<int>     *GenParticleStatus;
   vector<int>     *MuonCharge;
   vector<int>     *MuonPassID;
   vector<int>     *MuonPassIso;
   vector<int>     *MuonTrkHits;
   vector<int>     *MuonVtxIndex;
   vector<int>     *PFJetChargedHadronMultiplicity;
   vector<int>     *PFJetChargedMultiplicity;
   vector<int>     *PFJetElectronMultiplicity;
   vector<int>     *PFJetMuonMultiplicity;
   vector<int>     *PFJetNConstituents;
   vector<int>     *PFJetNeutralHadronMultiplicity;
   vector<int>     *PFJetNeutralMultiplicity;
   vector<int>     *PFJetPartonFlavour;
   vector<int>     *PFJetPassLooseID;
   vector<int>     *PFJetPassTightID;
   vector<int>     *PFJetPhotonMultiplicity;
   vector<int>     *ElectronSCkOutOfTime;
   vector<int>     *SuperClusterClustersSize;
   vector<int>     *SuperClusterTrackMatch;
   vector<int>     *SuperClusterkOutOfTime;
   vector<int>     *HLTBits;
   vector<int>     *HLTPrescales;
   vector<int>     *HLTResults;
   vector<int>     *L1PhysBits;
   vector<int>     *L1TechBits;
   vector<int>     *VertexNTracks;
   vector<int>     *VertexNTracksW05;
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
   TBranch        *b_passHBHENoiseFilter;   //!
   TBranch        *b_VertexIsFake;   //!
   TBranch        *b_time;   //!
   TBranch        *b_PtHat;   //!
   TBranch        *b_CaloJetEMF;   //!
   TBranch        *b_CaloJetEnergy;   //!
   TBranch        *b_CaloJetEnergyRaw;   //!
   TBranch        *b_CaloJetEta;   //!
   TBranch        *b_CaloJetHADF;   //!
   TBranch        *b_CaloJetJECUnc;   //!
   TBranch        *b_CaloJetJetBProbabilityBTag;   //!
   TBranch        *b_CaloJetJetProbabilityBTag;   //!
   TBranch        *b_CaloJetPhi;   //!
   TBranch        *b_CaloJetPt;   //!
   TBranch        *b_CaloJetPtRaw;   //!
   TBranch        *b_CaloJetResJEC;   //!
   TBranch        *b_CaloJetSigmaEta;   //!
   TBranch        *b_CaloJetSigmaPhi;   //!
   TBranch        *b_CaloJetSimpleSecondaryVertexHighEffBTag;   //!
   TBranch        *b_CaloJetSimpleSecondaryVertexHighPurBTag;   //!
   TBranch        *b_CaloJetTrackCountingHighEffBTag;   //!
   TBranch        *b_CaloJetTrackCountingHighPurBTag;   //!
   TBranch        *b_CaloJetfHPD;   //!
   TBranch        *b_CaloJetfRBX;   //!
   TBranch        *b_CaloJetresEMF;   //!
   TBranch        *b_CaloMET;   //!
   TBranch        *b_CaloMETPhi;   //!
   TBranch        *b_CaloMETPhiUncorr;   //!
   TBranch        *b_CaloMETUncorr;   //!
   TBranch        *b_CaloSumET;   //!
   TBranch        *b_CaloSumETUncorr;   //!
   TBranch        *b_ElectronCaloEnergy;   //!
   TBranch        *b_ElectronDCotTheta;   //!
   TBranch        *b_ElectronDeltaEtaTrkSC;   //!
   TBranch        *b_ElectronDeltaPhiTrkSC;   //!
   TBranch        *b_ElectronDist;   //!
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
   TBranch        *b_ElectronVtxDistXY;   //!
   TBranch        *b_ElectronVtxDistZ;   //!
   TBranch        *b_PDFWeights;   //!
   TBranch        *b_GenJetEMF;   //!
   TBranch        *b_GenJetEnergy;   //!
   TBranch        *b_GenJetEta;   //!
   TBranch        *b_GenJetHADF;   //!
   TBranch        *b_GenJetP;   //!
   TBranch        *b_GenJetPhi;   //!
   TBranch        *b_GenJetPt;   //!
   TBranch        *b_GenMETPhiTrue;   //!
   TBranch        *b_GenMETTrue;   //!
   TBranch        *b_GenSumETTrue;   //!
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
   TBranch        *b_MuonVtxDistXY;   //!
   TBranch        *b_MuonVtxDistZ;   //!
   TBranch        *b_PFJetChargedEmEnergyFraction;   //!
   TBranch        *b_PFJetChargedHadronEnergyFraction;   //!
   TBranch        *b_PFJetChargedMuEnergyFraction;   //!
   TBranch        *b_PFJetElectronEnergyFraction;   //!
   TBranch        *b_PFJetEnergy;   //!
   TBranch        *b_PFJetEnergyRaw;   //!
   TBranch        *b_PFJetEta;   //!
   TBranch        *b_PFJetJECUnc;   //!
   TBranch        *b_PFJetJetBProbabilityBTag;   //!
   TBranch        *b_PFJetJetProbabilityBTag;   //!
   TBranch        *b_PFJetMuonEnergyFraction;   //!
   TBranch        *b_PFJetNeutralEmEnergyFraction;   //!
   TBranch        *b_PFJetNeutralHadronEnergyFraction;   //!
   TBranch        *b_PFJetPhi;   //!
   TBranch        *b_PFJetPhotonEnergyFraction;   //!
   TBranch        *b_PFJetPt;   //!
   TBranch        *b_PFJetPtRaw;   //!
   TBranch        *b_PFJetResJEC;   //!
   TBranch        *b_PFJetSimpleSecondaryVertexHighEffBTag;   //!
   TBranch        *b_PFJetSimpleSecondaryVertexHighPurBTag;   //!
   TBranch        *b_PFJetTrackCountingHighEffBTag;   //!
   TBranch        *b_PFJetTrackCountingHighPurBTag;   //!
   TBranch        *b_PFMET;   //!
   TBranch        *b_PFMETPhi;   //!
   TBranch        *b_PFSumET;   //!
   TBranch        *b_PFMETPhiType1Cor;   //!
   TBranch        *b_PFMETType1Cor;   //!
   TBranch        *b_PFSumETType1Cor;   //!
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
   TBranch        *b_VertexChi2;   //!
   TBranch        *b_VertexNDF;   //!
   TBranch        *b_VertexRho;   //!
   TBranch        *b_VertexX;   //!
   TBranch        *b_VertexXErr;   //!
   TBranch        *b_VertexY;   //!
   TBranch        *b_VertexYErr;   //!
   TBranch        *b_VertexZ;   //!
   TBranch        *b_VertexZErr;   //!
   TBranch        *b_CaloJetOverlaps;   //!
   TBranch        *b_CaloJetPartonFlavour;   //!
   TBranch        *b_CaloJetPassLooseID;   //!
   TBranch        *b_CaloJetPassTightID;   //!
   TBranch        *b_CaloJetn90Hits;   //!
   TBranch        *b_ElectronCharge;   //!
   TBranch        *b_ElectronClassif;   //!
   TBranch        *b_ElectronHeepID;   //!
   TBranch        *b_ElectronMissingHits;   //!
   TBranch        *b_ElectronOverlaps;   //!
   TBranch        *b_ElectronPassID;   //!
   TBranch        *b_ElectronPassIso;   //!
   TBranch        *b_ElectronVtxIndex;   //!
   TBranch        *b_GenParticleMotherIndex;   //!
   TBranch        *b_GenParticleNumDaught;   //!
   TBranch        *b_GenParticlePdgId;   //!
   TBranch        *b_GenParticleStatus;   //!
   TBranch        *b_MuonCharge;   //!
   TBranch        *b_MuonPassID;   //!
   TBranch        *b_MuonPassIso;   //!
   TBranch        *b_MuonTrkHits;   //!
   TBranch        *b_MuonVtxIndex;   //!
   TBranch        *b_PFJetChargedHadronMultiplicity;   //!
   TBranch        *b_PFJetChargedMultiplicity;   //!
   TBranch        *b_PFJetElectronMultiplicity;   //!
   TBranch        *b_PFJetMuonMultiplicity;   //!
   TBranch        *b_PFJetNConstituents;   //!
   TBranch        *b_PFJetNeutralHadronMultiplicity;   //!
   TBranch        *b_PFJetNeutralMultiplicity;   //!
   TBranch        *b_PFJetPartonFlavour;   //!
   TBranch        *b_PFJetPassLooseID;   //!
   TBranch        *b_PFJetPassTightID;   //!
   TBranch        *b_PFJetPhotonMultiplicity;   //!
   TBranch        *b_ElectronSCkOutOfTime;   //!
   TBranch        *b_SuperClusterClustersSize;   //!
   TBranch        *b_SuperClusterTrackMatch;   //!
   TBranch        *b_SuperClusterkOutOfTime;   //!
   TBranch        *b_HLTBits;   //!
   TBranch        *b_HLTPrescales;   //!
   TBranch        *b_HLTResults;   //!
   TBranch        *b_L1PhysBits;   //!
   TBranch        *b_L1TechBits;   //!
   TBranch        *b_VertexNTracks;   //!
   TBranch        *b_VertexNTracksW05;   //!
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
   VertexIsFake = 0;
   CaloJetEMF = 0;
   CaloJetEnergy = 0;
   CaloJetEnergyRaw = 0;
   CaloJetEta = 0;
   CaloJetHADF = 0;
   CaloJetJECUnc = 0;
   CaloJetJetBProbabilityBTag = 0;
   CaloJetJetProbabilityBTag = 0;
   CaloJetPhi = 0;
   CaloJetPt = 0;
   CaloJetPtRaw = 0;
   CaloJetResJEC = 0;
   CaloJetSigmaEta = 0;
   CaloJetSigmaPhi = 0;
   CaloJetSimpleSecondaryVertexHighEffBTag = 0;
   CaloJetSimpleSecondaryVertexHighPurBTag = 0;
   CaloJetTrackCountingHighEffBTag = 0;
   CaloJetTrackCountingHighPurBTag = 0;
   CaloJetfHPD = 0;
   CaloJetfRBX = 0;
   CaloJetresEMF = 0;
   CaloMET = 0;
   CaloMETPhi = 0;
   CaloMETPhiUncorr = 0;
   CaloMETUncorr = 0;
   CaloSumET = 0;
   CaloSumETUncorr = 0;
   ElectronCaloEnergy = 0;
   ElectronDCotTheta = 0;
   ElectronDeltaEtaTrkSC = 0;
   ElectronDeltaPhiTrkSC = 0;
   ElectronDist = 0;
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
   ElectronVtxDistXY = 0;
   ElectronVtxDistZ = 0;
   PDFWeights = 0;
   GenJetEMF = 0;
   GenJetEnergy = 0;
   GenJetEta = 0;
   GenJetHADF = 0;
   GenJetP = 0;
   GenJetPhi = 0;
   GenJetPt = 0;
   GenMETPhiTrue = 0;
   GenMETTrue = 0;
   GenSumETTrue = 0;
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
   MuonVtxDistXY = 0;
   MuonVtxDistZ = 0;
   PFJetChargedEmEnergyFraction = 0;
   PFJetChargedHadronEnergyFraction = 0;
   PFJetChargedMuEnergyFraction = 0;
   PFJetElectronEnergyFraction = 0;
   PFJetEnergy = 0;
   PFJetEnergyRaw = 0;
   PFJetEta = 0;
   PFJetJECUnc = 0;
   PFJetJetBProbabilityBTag = 0;
   PFJetJetProbabilityBTag = 0;
   PFJetMuonEnergyFraction = 0;
   PFJetNeutralEmEnergyFraction = 0;
   PFJetNeutralHadronEnergyFraction = 0;
   PFJetPhi = 0;
   PFJetPhotonEnergyFraction = 0;
   PFJetPt = 0;
   PFJetPtRaw = 0;
   PFJetResJEC = 0;
   PFJetSimpleSecondaryVertexHighEffBTag = 0;
   PFJetSimpleSecondaryVertexHighPurBTag = 0;
   PFJetTrackCountingHighEffBTag = 0;
   PFJetTrackCountingHighPurBTag = 0;
   PFMET = 0;
   PFMETPhi = 0;
   PFSumET = 0;
   PFMETPhiType1Cor = 0;
   PFMETType1Cor = 0;
   PFSumETType1Cor = 0;
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
   VertexChi2 = 0;
   VertexNDF = 0;
   VertexRho = 0;
   VertexX = 0;
   VertexXErr = 0;
   VertexY = 0;
   VertexYErr = 0;
   VertexZ = 0;
   VertexZErr = 0;
   CaloJetOverlaps = 0;
   CaloJetPartonFlavour = 0;
   CaloJetPassLooseID = 0;
   CaloJetPassTightID = 0;
   CaloJetn90Hits = 0;
   ElectronCharge = 0;
   ElectronClassif = 0;
   ElectronHeepID = 0;
   ElectronMissingHits = 0;
   ElectronOverlaps = 0;
   ElectronPassID = 0;
   ElectronPassIso = 0;
   ElectronVtxIndex = 0;
   GenParticleMotherIndex = 0;
   GenParticleNumDaught = 0;
   GenParticlePdgId = 0;
   GenParticleStatus = 0;
   MuonCharge = 0;
   MuonPassID = 0;
   MuonPassIso = 0;
   MuonTrkHits = 0;
   MuonVtxIndex = 0;
   PFJetChargedHadronMultiplicity = 0;
   PFJetChargedMultiplicity = 0;
   PFJetElectronMultiplicity = 0;
   PFJetMuonMultiplicity = 0;
   PFJetNConstituents = 0;
   PFJetNeutralHadronMultiplicity = 0;
   PFJetNeutralMultiplicity = 0;
   PFJetPartonFlavour = 0;
   PFJetPassLooseID = 0;
   PFJetPassTightID = 0;
   PFJetPhotonMultiplicity = 0;
   ElectronSCkOutOfTime = 0;
   SuperClusterClustersSize = 0;
   SuperClusterTrackMatch = 0;
   SuperClusterkOutOfTime = 0;
   HLTBits = 0;
   HLTPrescales = 0;
   HLTResults = 0;
   L1PhysBits = 0;
   L1TechBits = 0;
   VertexNTracks = 0;
   VertexNTracksW05 = 0;
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
   fChain->SetBranchAddress("passHBHENoiseFilter", &passHBHENoiseFilter, &b_passHBHENoiseFilter);
   fChain->SetBranchAddress("VertexIsFake", &VertexIsFake, &b_VertexIsFake);
   fChain->SetBranchAddress("time", &time, &b_time);
   fChain->SetBranchAddress("PtHat", &PtHat, &b_PtHat);
   fChain->SetBranchAddress("CaloJetEMF", &CaloJetEMF, &b_CaloJetEMF);
   fChain->SetBranchAddress("CaloJetEnergy", &CaloJetEnergy, &b_CaloJetEnergy);
   fChain->SetBranchAddress("CaloJetEnergyRaw", &CaloJetEnergyRaw, &b_CaloJetEnergyRaw);
   fChain->SetBranchAddress("CaloJetEta", &CaloJetEta, &b_CaloJetEta);
   fChain->SetBranchAddress("CaloJetHADF", &CaloJetHADF, &b_CaloJetHADF);
   fChain->SetBranchAddress("CaloJetJECUnc", &CaloJetJECUnc, &b_CaloJetJECUnc);
   fChain->SetBranchAddress("CaloJetJetBProbabilityBTag", &CaloJetJetBProbabilityBTag, &b_CaloJetJetBProbabilityBTag);
   fChain->SetBranchAddress("CaloJetJetProbabilityBTag", &CaloJetJetProbabilityBTag, &b_CaloJetJetProbabilityBTag);
   fChain->SetBranchAddress("CaloJetPhi", &CaloJetPhi, &b_CaloJetPhi);
   fChain->SetBranchAddress("CaloJetPt", &CaloJetPt, &b_CaloJetPt);
   fChain->SetBranchAddress("CaloJetPtRaw", &CaloJetPtRaw, &b_CaloJetPtRaw);
   fChain->SetBranchAddress("CaloJetResJEC", &CaloJetResJEC, &b_CaloJetResJEC);
   fChain->SetBranchAddress("CaloJetSigmaEta", &CaloJetSigmaEta, &b_CaloJetSigmaEta);
   fChain->SetBranchAddress("CaloJetSigmaPhi", &CaloJetSigmaPhi, &b_CaloJetSigmaPhi);
   fChain->SetBranchAddress("CaloJetSimpleSecondaryVertexHighEffBTag", &CaloJetSimpleSecondaryVertexHighEffBTag, &b_CaloJetSimpleSecondaryVertexHighEffBTag);
   fChain->SetBranchAddress("CaloJetSimpleSecondaryVertexHighPurBTag", &CaloJetSimpleSecondaryVertexHighPurBTag, &b_CaloJetSimpleSecondaryVertexHighPurBTag);
   fChain->SetBranchAddress("CaloJetTrackCountingHighEffBTag", &CaloJetTrackCountingHighEffBTag, &b_CaloJetTrackCountingHighEffBTag);
   fChain->SetBranchAddress("CaloJetTrackCountingHighPurBTag", &CaloJetTrackCountingHighPurBTag, &b_CaloJetTrackCountingHighPurBTag);
   fChain->SetBranchAddress("CaloJetfHPD", &CaloJetfHPD, &b_CaloJetfHPD);
   fChain->SetBranchAddress("CaloJetfRBX", &CaloJetfRBX, &b_CaloJetfRBX);
   fChain->SetBranchAddress("CaloJetresEMF", &CaloJetresEMF, &b_CaloJetresEMF);
   fChain->SetBranchAddress("CaloMET", &CaloMET, &b_CaloMET);
   fChain->SetBranchAddress("CaloMETPhi", &CaloMETPhi, &b_CaloMETPhi);
   fChain->SetBranchAddress("CaloMETPhiUncorr", &CaloMETPhiUncorr, &b_CaloMETPhiUncorr);
   fChain->SetBranchAddress("CaloMETUncorr", &CaloMETUncorr, &b_CaloMETUncorr);
   fChain->SetBranchAddress("CaloSumET", &CaloSumET, &b_CaloSumET);
   fChain->SetBranchAddress("CaloSumETUncorr", &CaloSumETUncorr, &b_CaloSumETUncorr);
   fChain->SetBranchAddress("ElectronCaloEnergy", &ElectronCaloEnergy, &b_ElectronCaloEnergy);
   fChain->SetBranchAddress("ElectronDCotTheta", &ElectronDCotTheta, &b_ElectronDCotTheta);
   fChain->SetBranchAddress("ElectronDeltaEtaTrkSC", &ElectronDeltaEtaTrkSC, &b_ElectronDeltaEtaTrkSC);
   fChain->SetBranchAddress("ElectronDeltaPhiTrkSC", &ElectronDeltaPhiTrkSC, &b_ElectronDeltaPhiTrkSC);
   fChain->SetBranchAddress("ElectronDist", &ElectronDist, &b_ElectronDist);
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
   fChain->SetBranchAddress("ElectronVtxDistXY", &ElectronVtxDistXY, &b_ElectronVtxDistXY);
   fChain->SetBranchAddress("ElectronVtxDistZ", &ElectronVtxDistZ, &b_ElectronVtxDistZ);
   fChain->SetBranchAddress("PDFWeights", &PDFWeights, &b_PDFWeights);
   fChain->SetBranchAddress("GenJetEMF", &GenJetEMF, &b_GenJetEMF);
   fChain->SetBranchAddress("GenJetEnergy", &GenJetEnergy, &b_GenJetEnergy);
   fChain->SetBranchAddress("GenJetEta", &GenJetEta, &b_GenJetEta);
   fChain->SetBranchAddress("GenJetHADF", &GenJetHADF, &b_GenJetHADF);
   fChain->SetBranchAddress("GenJetP", &GenJetP, &b_GenJetP);
   fChain->SetBranchAddress("GenJetPhi", &GenJetPhi, &b_GenJetPhi);
   fChain->SetBranchAddress("GenJetPt", &GenJetPt, &b_GenJetPt);
   fChain->SetBranchAddress("GenMETPhiTrue", &GenMETPhiTrue, &b_GenMETPhiTrue);
   fChain->SetBranchAddress("GenMETTrue", &GenMETTrue, &b_GenMETTrue);
   fChain->SetBranchAddress("GenSumETTrue", &GenSumETTrue, &b_GenSumETTrue);
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
   fChain->SetBranchAddress("MuonVtxDistXY", &MuonVtxDistXY, &b_MuonVtxDistXY);
   fChain->SetBranchAddress("MuonVtxDistZ", &MuonVtxDistZ, &b_MuonVtxDistZ);
   fChain->SetBranchAddress("PFJetChargedEmEnergyFraction", &PFJetChargedEmEnergyFraction, &b_PFJetChargedEmEnergyFraction);
   fChain->SetBranchAddress("PFJetChargedHadronEnergyFraction", &PFJetChargedHadronEnergyFraction, &b_PFJetChargedHadronEnergyFraction);
   fChain->SetBranchAddress("PFJetChargedMuEnergyFraction", &PFJetChargedMuEnergyFraction, &b_PFJetChargedMuEnergyFraction);
   fChain->SetBranchAddress("PFJetElectronEnergyFraction", &PFJetElectronEnergyFraction, &b_PFJetElectronEnergyFraction);
   fChain->SetBranchAddress("PFJetEnergy", &PFJetEnergy, &b_PFJetEnergy);
   fChain->SetBranchAddress("PFJetEnergyRaw", &PFJetEnergyRaw, &b_PFJetEnergyRaw);
   fChain->SetBranchAddress("PFJetEta", &PFJetEta, &b_PFJetEta);
   fChain->SetBranchAddress("PFJetJECUnc", &PFJetJECUnc, &b_PFJetJECUnc);
   fChain->SetBranchAddress("PFJetJetBProbabilityBTag", &PFJetJetBProbabilityBTag, &b_PFJetJetBProbabilityBTag);
   fChain->SetBranchAddress("PFJetJetProbabilityBTag", &PFJetJetProbabilityBTag, &b_PFJetJetProbabilityBTag);
   fChain->SetBranchAddress("PFJetMuonEnergyFraction", &PFJetMuonEnergyFraction, &b_PFJetMuonEnergyFraction);
   fChain->SetBranchAddress("PFJetNeutralEmEnergyFraction", &PFJetNeutralEmEnergyFraction, &b_PFJetNeutralEmEnergyFraction);
   fChain->SetBranchAddress("PFJetNeutralHadronEnergyFraction", &PFJetNeutralHadronEnergyFraction, &b_PFJetNeutralHadronEnergyFraction);
   fChain->SetBranchAddress("PFJetPhi", &PFJetPhi, &b_PFJetPhi);
   fChain->SetBranchAddress("PFJetPhotonEnergyFraction", &PFJetPhotonEnergyFraction, &b_PFJetPhotonEnergyFraction);
   fChain->SetBranchAddress("PFJetPt", &PFJetPt, &b_PFJetPt);
   fChain->SetBranchAddress("PFJetPtRaw", &PFJetPtRaw, &b_PFJetPtRaw);
   fChain->SetBranchAddress("PFJetResJEC", &PFJetResJEC, &b_PFJetResJEC);
   fChain->SetBranchAddress("PFJetSimpleSecondaryVertexHighEffBTag", &PFJetSimpleSecondaryVertexHighEffBTag, &b_PFJetSimpleSecondaryVertexHighEffBTag);
   fChain->SetBranchAddress("PFJetSimpleSecondaryVertexHighPurBTag", &PFJetSimpleSecondaryVertexHighPurBTag, &b_PFJetSimpleSecondaryVertexHighPurBTag);
   fChain->SetBranchAddress("PFJetTrackCountingHighEffBTag", &PFJetTrackCountingHighEffBTag, &b_PFJetTrackCountingHighEffBTag);
   fChain->SetBranchAddress("PFJetTrackCountingHighPurBTag", &PFJetTrackCountingHighPurBTag, &b_PFJetTrackCountingHighPurBTag);
   fChain->SetBranchAddress("PFMET", &PFMET, &b_PFMET);
   fChain->SetBranchAddress("PFMETPhi", &PFMETPhi, &b_PFMETPhi);
   fChain->SetBranchAddress("PFSumET", &PFSumET, &b_PFSumET);
   fChain->SetBranchAddress("PFMETPhiType1Cor", &PFMETPhiType1Cor, &b_PFMETPhiType1Cor);
   fChain->SetBranchAddress("PFMETType1Cor", &PFMETType1Cor, &b_PFMETType1Cor);
   fChain->SetBranchAddress("PFSumETType1Cor", &PFSumETType1Cor, &b_PFSumETType1Cor);
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
   fChain->SetBranchAddress("VertexChi2", &VertexChi2, &b_VertexChi2);
   fChain->SetBranchAddress("VertexNDF", &VertexNDF, &b_VertexNDF);
   fChain->SetBranchAddress("VertexRho", &VertexRho, &b_VertexRho);
   fChain->SetBranchAddress("VertexX", &VertexX, &b_VertexX);
   fChain->SetBranchAddress("VertexXErr", &VertexXErr, &b_VertexXErr);
   fChain->SetBranchAddress("VertexY", &VertexY, &b_VertexY);
   fChain->SetBranchAddress("VertexYErr", &VertexYErr, &b_VertexYErr);
   fChain->SetBranchAddress("VertexZ", &VertexZ, &b_VertexZ);
   fChain->SetBranchAddress("VertexZErr", &VertexZErr, &b_VertexZErr);
   fChain->SetBranchAddress("CaloJetOverlaps", &CaloJetOverlaps, &b_CaloJetOverlaps);
   fChain->SetBranchAddress("CaloJetPartonFlavour", &CaloJetPartonFlavour, &b_CaloJetPartonFlavour);
   fChain->SetBranchAddress("CaloJetPassLooseID", &CaloJetPassLooseID, &b_CaloJetPassLooseID);
   fChain->SetBranchAddress("CaloJetPassTightID", &CaloJetPassTightID, &b_CaloJetPassTightID);
   fChain->SetBranchAddress("CaloJetn90Hits", &CaloJetn90Hits, &b_CaloJetn90Hits);
   fChain->SetBranchAddress("ElectronCharge", &ElectronCharge, &b_ElectronCharge);
   fChain->SetBranchAddress("ElectronClassif", &ElectronClassif, &b_ElectronClassif);
   fChain->SetBranchAddress("ElectronHeepID", &ElectronHeepID, &b_ElectronHeepID);
   fChain->SetBranchAddress("ElectronMissingHits", &ElectronMissingHits, &b_ElectronMissingHits);
   fChain->SetBranchAddress("ElectronOverlaps", &ElectronOverlaps, &b_ElectronOverlaps);
   fChain->SetBranchAddress("ElectronPassID", &ElectronPassID, &b_ElectronPassID);
   fChain->SetBranchAddress("ElectronPassIso", &ElectronPassIso, &b_ElectronPassIso);
   fChain->SetBranchAddress("ElectronVtxIndex", &ElectronVtxIndex, &b_ElectronVtxIndex);
   fChain->SetBranchAddress("GenParticleMotherIndex", &GenParticleMotherIndex, &b_GenParticleMotherIndex);
   fChain->SetBranchAddress("GenParticleNumDaught", &GenParticleNumDaught, &b_GenParticleNumDaught);
   fChain->SetBranchAddress("GenParticlePdgId", &GenParticlePdgId, &b_GenParticlePdgId);
   fChain->SetBranchAddress("GenParticleStatus", &GenParticleStatus, &b_GenParticleStatus);
   fChain->SetBranchAddress("MuonCharge", &MuonCharge, &b_MuonCharge);
   fChain->SetBranchAddress("MuonPassID", &MuonPassID, &b_MuonPassID);
   fChain->SetBranchAddress("MuonPassIso", &MuonPassIso, &b_MuonPassIso);
   fChain->SetBranchAddress("MuonTrkHits", &MuonTrkHits, &b_MuonTrkHits);
   fChain->SetBranchAddress("MuonVtxIndex", &MuonVtxIndex, &b_MuonVtxIndex);
   fChain->SetBranchAddress("PFJetChargedHadronMultiplicity", &PFJetChargedHadronMultiplicity, &b_PFJetChargedHadronMultiplicity);
   fChain->SetBranchAddress("PFJetChargedMultiplicity", &PFJetChargedMultiplicity, &b_PFJetChargedMultiplicity);
   fChain->SetBranchAddress("PFJetElectronMultiplicity", &PFJetElectronMultiplicity, &b_PFJetElectronMultiplicity);
   fChain->SetBranchAddress("PFJetMuonMultiplicity", &PFJetMuonMultiplicity, &b_PFJetMuonMultiplicity);
   fChain->SetBranchAddress("PFJetNConstituents", &PFJetNConstituents, &b_PFJetNConstituents);
   fChain->SetBranchAddress("PFJetNeutralHadronMultiplicity", &PFJetNeutralHadronMultiplicity, &b_PFJetNeutralHadronMultiplicity);
   fChain->SetBranchAddress("PFJetNeutralMultiplicity", &PFJetNeutralMultiplicity, &b_PFJetNeutralMultiplicity);
   fChain->SetBranchAddress("PFJetPartonFlavour", &PFJetPartonFlavour, &b_PFJetPartonFlavour);
   fChain->SetBranchAddress("PFJetPassLooseID", &PFJetPassLooseID, &b_PFJetPassLooseID);
   fChain->SetBranchAddress("PFJetPassTightID", &PFJetPassTightID, &b_PFJetPassTightID);
   fChain->SetBranchAddress("PFJetPhotonMultiplicity", &PFJetPhotonMultiplicity, &b_PFJetPhotonMultiplicity);
   fChain->SetBranchAddress("ElectronSCkOutOfTime", &ElectronSCkOutOfTime, &b_ElectronSCkOutOfTime);
   fChain->SetBranchAddress("SuperClusterClustersSize", &SuperClusterClustersSize, &b_SuperClusterClustersSize);
   fChain->SetBranchAddress("SuperClusterTrackMatch", &SuperClusterTrackMatch, &b_SuperClusterTrackMatch);
   fChain->SetBranchAddress("SuperClusterkOutOfTime", &SuperClusterkOutOfTime, &b_SuperClusterkOutOfTime);
   fChain->SetBranchAddress("HLTBits", &HLTBits, &b_HLTBits);
   fChain->SetBranchAddress("HLTPrescales", &HLTPrescales, &b_HLTPrescales);
   fChain->SetBranchAddress("HLTResults", &HLTResults, &b_HLTResults);
   fChain->SetBranchAddress("L1PhysBits", &L1PhysBits, &b_L1PhysBits);
   fChain->SetBranchAddress("L1TechBits", &L1TechBits, &b_L1TechBits);
   fChain->SetBranchAddress("VertexNTracks", &VertexNTracks, &b_VertexNTracks);
   fChain->SetBranchAddress("VertexNTracksW05", &VertexNTracksW05, &b_VertexNTracksW05);
   fChain->SetBranchAddress("bunch", &bunch, &b_bunch);
   fChain->SetBranchAddress("event", &event, &b_event);
   fChain->SetBranchAddress("ls", &ls, &b_ls);
   fChain->SetBranchAddress("orbit", &orbit, &b_orbit);
   fChain->SetBranchAddress("run", &run, &b_run);
   fChain->SetBranchAddress("ProcessID", &ProcessID, &b_ProcessID);
   Notify();

fChain->SetBranchStatus("isData",1);
fChain->SetBranchStatus("isBPTX0",0);
fChain->SetBranchStatus("isBSCBeamHalo",0);
fChain->SetBranchStatus("isBSCMinBias",0);
fChain->SetBranchStatus("isBeamScraping",1);
fChain->SetBranchStatus("isPhysDeclared",0);
fChain->SetBranchStatus("isPrimaryVertex",0);
fChain->SetBranchStatus("passHBHENoiseFilter",0);
fChain->SetBranchStatus("VertexIsFake",1);
fChain->SetBranchStatus("time",0);
fChain->SetBranchStatus("PtHat",0);
fChain->SetBranchStatus("CaloJetEMF",0);
fChain->SetBranchStatus("CaloJetEnergy",0);
fChain->SetBranchStatus("CaloJetEnergyRaw",0);
fChain->SetBranchStatus("CaloJetEta",1);
fChain->SetBranchStatus("CaloJetHADF",0);
fChain->SetBranchStatus("CaloJetJECUnc",0);
fChain->SetBranchStatus("CaloJetJetBProbabilityBTag",0);
fChain->SetBranchStatus("CaloJetJetProbabilityBTag",0);
fChain->SetBranchStatus("CaloJetPhi",1);
fChain->SetBranchStatus("CaloJetPt",1);
fChain->SetBranchStatus("CaloJetPtRaw",0);
fChain->SetBranchStatus("CaloJetResJEC",0);
fChain->SetBranchStatus("CaloJetSigmaEta",0);
fChain->SetBranchStatus("CaloJetSigmaPhi",0);
fChain->SetBranchStatus("CaloJetSimpleSecondaryVertexHighEffBTag",0);
fChain->SetBranchStatus("CaloJetSimpleSecondaryVertexHighPurBTag",0);
fChain->SetBranchStatus("CaloJetTrackCountingHighEffBTag",1);
fChain->SetBranchStatus("CaloJetTrackCountingHighPurBTag",0);
fChain->SetBranchStatus("CaloJetfHPD",0);
fChain->SetBranchStatus("CaloJetfRBX",0);
fChain->SetBranchStatus("CaloJetresEMF",0);
fChain->SetBranchStatus("CaloMET",0);
fChain->SetBranchStatus("CaloMETPhi",0);
fChain->SetBranchStatus("CaloMETPhiUncorr",0);
fChain->SetBranchStatus("CaloMETUncorr",0);
fChain->SetBranchStatus("CaloSumET",0);
fChain->SetBranchStatus("CaloSumETUncorr",0);
fChain->SetBranchStatus("ElectronCaloEnergy",0);
fChain->SetBranchStatus("ElectronDCotTheta",0);
fChain->SetBranchStatus("ElectronDeltaEtaTrkSC",0);
fChain->SetBranchStatus("ElectronDeltaPhiTrkSC",0);
fChain->SetBranchStatus("ElectronDist",0);
fChain->SetBranchStatus("ElectronE1x5OverE5x5",0);
fChain->SetBranchStatus("ElectronE2x5OverE5x5",0);
fChain->SetBranchStatus("ElectronEcalIso",0);
fChain->SetBranchStatus("ElectronEcalIsoHeep",0);
fChain->SetBranchStatus("ElectronEnergy",0);
fChain->SetBranchStatus("ElectronEta",0);
fChain->SetBranchStatus("ElectronHcalIso",0);
fChain->SetBranchStatus("ElectronHcalIsoD1Heep",0);
fChain->SetBranchStatus("ElectronHcalIsoD2Heep",0);
fChain->SetBranchStatus("ElectronHoE",0);
fChain->SetBranchStatus("ElectronPhi",0);
fChain->SetBranchStatus("ElectronPt",1);
fChain->SetBranchStatus("ElectronRelIso",0);
fChain->SetBranchStatus("ElectronSCEta",0);
fChain->SetBranchStatus("ElectronSCPhi",0);
fChain->SetBranchStatus("ElectronSCPt",0);
fChain->SetBranchStatus("ElectronSCRawEnergy",0);
fChain->SetBranchStatus("ElectronSigmaEtaEta",0);
fChain->SetBranchStatus("ElectronSigmaIEtaIEta",0);
fChain->SetBranchStatus("ElectronTrackPt",0);
fChain->SetBranchStatus("ElectronTrkIso",0);
fChain->SetBranchStatus("ElectronTrkIsoHeep",0);
fChain->SetBranchStatus("ElectronVtxDistXY",0);
fChain->SetBranchStatus("ElectronVtxDistZ",0);
fChain->SetBranchStatus("PDFWeights",0);
fChain->SetBranchStatus("GenJetEMF",0);
fChain->SetBranchStatus("GenJetEnergy",0);
fChain->SetBranchStatus("GenJetEta",0);
fChain->SetBranchStatus("GenJetHADF",0);
fChain->SetBranchStatus("GenJetP",1);
fChain->SetBranchStatus("GenJetPhi",0);
fChain->SetBranchStatus("GenJetPt",1);
fChain->SetBranchStatus("GenMETPhiTrue",1);
fChain->SetBranchStatus("GenMETTrue",1);
fChain->SetBranchStatus("GenSumETTrue",0);
fChain->SetBranchStatus("GenParticleEnergy",0);
fChain->SetBranchStatus("GenParticleEta",1);
fChain->SetBranchStatus("GenParticleP",1);
fChain->SetBranchStatus("GenParticlePhi",1);
fChain->SetBranchStatus("GenParticlePt",1);
fChain->SetBranchStatus("GenParticlePx",0);
fChain->SetBranchStatus("GenParticlePy",0);
fChain->SetBranchStatus("GenParticlePz",0);
fChain->SetBranchStatus("GenParticleVX",0);
fChain->SetBranchStatus("GenParticleVY",0);
fChain->SetBranchStatus("GenParticleVZ",0);
fChain->SetBranchStatus("MuonEcalIso",1);
fChain->SetBranchStatus("MuonEnergy",0);
fChain->SetBranchStatus("MuonEta",1);
fChain->SetBranchStatus("MuonGlobalChi2",1);
fChain->SetBranchStatus("MuonHOIso",0);
fChain->SetBranchStatus("MuonHcalIso",1);
fChain->SetBranchStatus("MuonP",1);
fChain->SetBranchStatus("MuonPhi",1);
fChain->SetBranchStatus("MuonPt",1);
fChain->SetBranchStatus("MuonRelIso",1);
fChain->SetBranchStatus("MuonTrkD0",1);
fChain->SetBranchStatus("MuonTrkD0Error",0);
fChain->SetBranchStatus("MuonTrkDz",1);
fChain->SetBranchStatus("MuonTrkDzError",0);
fChain->SetBranchStatus("MuonTrkIso",1);
fChain->SetBranchStatus("MuonVtxDistXY",0);
fChain->SetBranchStatus("MuonVtxDistZ",0);
fChain->SetBranchStatus("PFJetChargedEmEnergyFraction",0);
fChain->SetBranchStatus("PFJetChargedHadronEnergyFraction",0);
fChain->SetBranchStatus("PFJetChargedMuEnergyFraction",0);
fChain->SetBranchStatus("PFJetElectronEnergyFraction",0);
fChain->SetBranchStatus("PFJetEnergy",0);
fChain->SetBranchStatus("PFJetEnergyRaw",0);
fChain->SetBranchStatus("PFJetEta",0);
fChain->SetBranchStatus("PFJetJECUnc",0);
fChain->SetBranchStatus("PFJetJetBProbabilityBTag",0);
fChain->SetBranchStatus("PFJetJetProbabilityBTag",0);
fChain->SetBranchStatus("PFJetMuonEnergyFraction",0);
fChain->SetBranchStatus("PFJetNeutralEmEnergyFraction",0);
fChain->SetBranchStatus("PFJetNeutralHadronEnergyFraction",0);
fChain->SetBranchStatus("PFJetPhi",0);
fChain->SetBranchStatus("PFJetPhotonEnergyFraction",0);
fChain->SetBranchStatus("PFJetPt",0);
fChain->SetBranchStatus("PFJetPtRaw",0);
fChain->SetBranchStatus("PFJetResJEC",0);
fChain->SetBranchStatus("PFJetSimpleSecondaryVertexHighEffBTag",0);
fChain->SetBranchStatus("PFJetSimpleSecondaryVertexHighPurBTag",0);
fChain->SetBranchStatus("PFJetTrackCountingHighEffBTag",0);
fChain->SetBranchStatus("PFJetTrackCountingHighPurBTag",0);
fChain->SetBranchStatus("PFMET",1);
fChain->SetBranchStatus("PFMETPhi",1);
fChain->SetBranchStatus("PFSumET",0);
fChain->SetBranchStatus("PFMETPhiType1Cor",0);
fChain->SetBranchStatus("PFMETType1Cor",0);
fChain->SetBranchStatus("PFSumETType1Cor",0);
fChain->SetBranchStatus("ElectronSCE1E9",0);
fChain->SetBranchStatus("ElectronSCEcalIso",0);
fChain->SetBranchStatus("ElectronSCHEEPEcalIso",0);
fChain->SetBranchStatus("ElectronSCHEEPTrkIso",0);
fChain->SetBranchStatus("ElectronSCS4S1",0);
fChain->SetBranchStatus("SuperClusterDrTrack1",0);
fChain->SetBranchStatus("SuperClusterDrTrack2",0);
fChain->SetBranchStatus("SuperClusterE1E9",0);
fChain->SetBranchStatus("SuperClusterEcalIso",0);
fChain->SetBranchStatus("SuperClusterEta",0);
fChain->SetBranchStatus("SuperClusterHEEPEcalIso",0);
fChain->SetBranchStatus("SuperClusterHEEPTrkIso",0);
fChain->SetBranchStatus("SuperClusterHoE",0);
fChain->SetBranchStatus("SuperClusterPhi",0);
fChain->SetBranchStatus("SuperClusterPt",0);
fChain->SetBranchStatus("SuperClusterRawEnergy",0);
fChain->SetBranchStatus("SuperClusterS4S1",0);
fChain->SetBranchStatus("SuperClusterSigmaIEtaIEta",0);
fChain->SetBranchStatus("SuperClusterTrack1Eta",0);
fChain->SetBranchStatus("SuperClusterTrack1Phi",0);
fChain->SetBranchStatus("SuperClusterTrack1Pt",0);
fChain->SetBranchStatus("SuperClusterTrack2Eta",0);
fChain->SetBranchStatus("SuperClusterTrack2Phi",0);
fChain->SetBranchStatus("SuperClusterTrack2Pt",0);
fChain->SetBranchStatus("TCMET",0);
fChain->SetBranchStatus("TCMETPhi",0);
fChain->SetBranchStatus("TCSumET",0);
fChain->SetBranchStatus("VertexChi2",0);
fChain->SetBranchStatus("VertexNDF",1);
fChain->SetBranchStatus("VertexRho",1);
fChain->SetBranchStatus("VertexX",0);
fChain->SetBranchStatus("VertexXErr",0);
fChain->SetBranchStatus("VertexY",0);
fChain->SetBranchStatus("VertexYErr",0);
fChain->SetBranchStatus("VertexZ",1);
fChain->SetBranchStatus("VertexZErr",0);
fChain->SetBranchStatus("CaloJetOverlaps",0);
fChain->SetBranchStatus("CaloJetPartonFlavour",0);
fChain->SetBranchStatus("CaloJetPassLooseID",1);
fChain->SetBranchStatus("CaloJetPassTightID",1);
fChain->SetBranchStatus("CaloJetn90Hits",0);
fChain->SetBranchStatus("ElectronCharge",0);
fChain->SetBranchStatus("ElectronClassif",0);
fChain->SetBranchStatus("ElectronHeepID",0);
fChain->SetBranchStatus("ElectronMissingHits",0);
fChain->SetBranchStatus("ElectronOverlaps",1);
fChain->SetBranchStatus("ElectronPassID",1);
fChain->SetBranchStatus("ElectronPassIso",0);
fChain->SetBranchStatus("ElectronVtxIndex",0);
fChain->SetBranchStatus("GenParticleMotherIndex",1);
fChain->SetBranchStatus("GenParticleNumDaught",0);
fChain->SetBranchStatus("GenParticlePdgId",1);
fChain->SetBranchStatus("GenParticleStatus",0);
fChain->SetBranchStatus("MuonCharge",1);
fChain->SetBranchStatus("MuonPassID",1);
fChain->SetBranchStatus("MuonPassIso",1);
fChain->SetBranchStatus("MuonTrkHits",1);
fChain->SetBranchStatus("MuonVtxIndex",0);
fChain->SetBranchStatus("PFJetChargedHadronMultiplicity",0);
fChain->SetBranchStatus("PFJetChargedMultiplicity",0);
fChain->SetBranchStatus("PFJetElectronMultiplicity",0);
fChain->SetBranchStatus("PFJetMuonMultiplicity",0);
fChain->SetBranchStatus("PFJetNConstituents",0);
fChain->SetBranchStatus("PFJetNeutralHadronMultiplicity",0);
fChain->SetBranchStatus("PFJetNeutralMultiplicity",0);
fChain->SetBranchStatus("PFJetPartonFlavour",0);
fChain->SetBranchStatus("PFJetPassLooseID",0);
fChain->SetBranchStatus("PFJetPassTightID",0);
fChain->SetBranchStatus("PFJetPhotonMultiplicity",0);
fChain->SetBranchStatus("ElectronSCkOutOfTime",0);
fChain->SetBranchStatus("SuperClusterClustersSize",0);
fChain->SetBranchStatus("SuperClusterTrackMatch",0);
fChain->SetBranchStatus("SuperClusterkOutOfTime",0);
fChain->SetBranchStatus("HLTBits",0);
fChain->SetBranchStatus("HLTPrescales",0);
fChain->SetBranchStatus("HLTResults",1);
fChain->SetBranchStatus("L1PhysBits",0);
fChain->SetBranchStatus("L1TechBits",0);
fChain->SetBranchStatus("VertexNTracks",0);
fChain->SetBranchStatus("VertexNTracksW05",0);
fChain->SetBranchStatus("bunch",1);
fChain->SetBranchStatus("event",1);
fChain->SetBranchStatus("ls",1);
fChain->SetBranchStatus("orbit",0);
fChain->SetBranchStatus("run",1);
fChain->SetBranchStatus("ProcessID",0);


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
