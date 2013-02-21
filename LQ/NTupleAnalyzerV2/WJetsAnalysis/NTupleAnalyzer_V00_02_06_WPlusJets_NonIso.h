//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Sat Mar  5 14:33:03 2011 by ROOT version 5.26/00
// from TTree tree/
// found on file: RootNtuple2011Feb10_Run2010A_Nov4ReReco_ALL_20110211_172658.root
//////////////////////////////////////////////////////////

#ifndef placeholder_h
#define placeholder_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <iostream>
#include <TH1F.h>
class placeholder {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   string          *HLTKey;
   vector<string>  *HLTInsideDatasetTriggerNames;
   vector<string>  *HLTOutsideDatasetTriggerNames;
   Bool_t          isData;
   Bool_t          isBPTX0;
   Bool_t          isBSCBeamHalo;
   Bool_t          isBSCMinBias;
   Bool_t          isBeamScraping;
   Bool_t          isPhysDeclared;
   Bool_t          isPrimaryVertex;
   Bool_t          isTrackingFailure;
   Bool_t          passBeamHaloFilterLoose;
   Bool_t          passBeamHaloFilterTight;
   Bool_t          passCaloBoundaryDRFilter;
   Bool_t          passEcalMaskedCellDRFilter;
   Bool_t          passHBHENoiseFilter;
   vector<bool>    *ElectronHasEcalDrivenSeed;
   vector<bool>    *ElectronHasMatchedConvPhot;
   vector<bool>    *PhotonHasMatchedConvPhot;
   vector<bool>    *PhotonHasMatchedPromptEle;
   vector<bool>    *PhotonHasPixelSeed;
   vector<bool>    *PhotonIsEBEEGap;
   vector<bool>    *PhotonIsEBGap;
   vector<bool>    *PhotonIsEEGap;
   vector<bool>    *HLTInsideDatasetTriggerDecisions;
   vector<bool>    *HLTOutsideDatasetTriggerDecisions;
   vector<bool>    *VertexIsFake;
   Double_t        rhoIso;
   Double_t        rhoJets;
   Double_t        time;
   Double_t        PtHat;
   Double_t        Weight;
   vector<double>  *CaloJetEMF;
   vector<double>  *CaloJetEnergy;
   vector<double>  *CaloJetEnergyRaw;
   vector<double>  *CaloJetEta;
   vector<double>  *CaloJetHADF;
   vector<double>  *CaloJetJECUnc;
   vector<double>  *CaloJetJetBProbabilityBTag;
   vector<double>  *CaloJetJetProbabilityBTag;
   vector<double>  *CaloJetL1FastJetJEC;
   vector<double>  *CaloJetL1OffsetJEC;
   vector<double>  *CaloJetL2L3ResJEC;
   vector<double>  *CaloJetL2RelJEC;
   vector<double>  *CaloJetL3AbsJEC;
   vector<double>  *CaloJetPhi;
   vector<double>  *CaloJetPt;
   vector<double>  *CaloJetPtRaw;
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
   vector<double>  *ElectronBeamSpotDXY;
   vector<double>  *ElectronBeamSpotDXYError;
   vector<double>  *ElectronCaloEnergy;
   vector<double>  *ElectronDCotTheta;
   vector<double>  *ElectronDeltaEtaTrkSC;
   vector<double>  *ElectronDeltaPhiTrkSC;
   vector<double>  *ElectronDist;
   vector<double>  *ElectronE1x5OverE5x5;
   vector<double>  *ElectronE2x5OverE5x5;
   vector<double>  *ElectronESuperClusterOverP;
   vector<double>  *ElectronEcalIsoDR03;
   vector<double>  *ElectronEcalIsoPAT;
   vector<double>  *ElectronEnergy;
   vector<double>  *ElectronEta;
   vector<double>  *ElectronFbrem;
   vector<double>  *ElectronHcalIsoD1DR03;
   vector<double>  *ElectronHcalIsoD2DR03;
   vector<double>  *ElectronHcalIsoDR03;
   vector<double>  *ElectronHcalIsoDR03FullCone;
   vector<double>  *ElectronHcalIsoPAT;
   vector<double>  *ElectronHoE;
   vector<double>  *ElectronLikelihood;
   vector<double>  *ElectronPhi;
   vector<double>  *ElectronPrimaryVertexDXY;
   vector<double>  *ElectronPrimaryVertexDXYError;
   vector<double>  *ElectronPt;
   vector<double>  *ElectronPtHeep;
   vector<double>  *ElectronRelIsoPAT;
   vector<double>  *ElectronSCEta;
   vector<double>  *ElectronSCPhi;
   vector<double>  *ElectronSCPt;
   vector<double>  *ElectronSCRawEnergy;
   vector<double>  *ElectronSigmaEtaEta;
   vector<double>  *ElectronSigmaIEtaIEta;
   vector<double>  *ElectronTrackPt;
   vector<double>  *ElectronTrackValidFractionOfHits;
   vector<double>  *ElectronTrackVx;
   vector<double>  *ElectronTrackVy;
   vector<double>  *ElectronTrackVz;
   vector<double>  *ElectronTrkIsoDR03;
   vector<double>  *ElectronTrkIsoPAT;
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
   vector<double>  *GenMETCalo;
   vector<double>  *GenMETPhiCalo;
   vector<double>  *GenSumETCalo;
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
   vector<double>  *MuonBackToBackCompatibility;
   vector<double>  *MuonBeamSpotDXY;
   vector<double>  *MuonBeamSpotDXYError;
   vector<double>  *MuonCocktailEta;
   vector<double>  *MuonCocktailEtaError;
   vector<double>  *MuonCocktailGlobalChi2;
   vector<double>  *MuonCocktailP;
   vector<double>  *MuonCocktailPhi;
   vector<double>  *MuonCocktailPhiError;
   vector<double>  *MuonCocktailPt;
   vector<double>  *MuonCocktailPtError;
   vector<double>  *MuonCocktailQOverPError;
   vector<double>  *MuonCocktailRelIso;
   vector<double>  *MuonCocktailTrkD0;
   vector<double>  *MuonCocktailTrkD0Error;
   vector<double>  *MuonCocktailTrkDz;
   vector<double>  *MuonCocktailTrkDzError;
   vector<double>  *MuonCocktailTrkValidFractionOfHits;
   vector<double>  *MuonCosmicCompatibility;
   vector<double>  *MuonEcalIso;
   vector<double>  *MuonEnergy;
   vector<double>  *MuonEta;
   vector<double>  *MuonEtaError;
   vector<double>  *MuonGlobalChi2;
   vector<double>  *MuonHOIso;
   vector<double>  *MuonHcalIso;
   vector<double>  *MuonOverlapCompatibility;
   vector<double>  *MuonP;
   vector<double>  *MuonPhi;
   vector<double>  *MuonPhiError;
   vector<double>  *MuonPrimaryVertexDXY;
   vector<double>  *MuonPrimaryVertexDXYError;
   vector<double>  *MuonPt;
   vector<double>  *MuonPtError;
   vector<double>  *MuonQOverPError;
   vector<double>  *MuonRelIso;
   vector<double>  *MuonTimeCompatibility;
   vector<double>  *MuonTrackChi2;
   vector<double>  *MuonTrackerIsoSumPT;
   vector<double>  *MuonTrkD0;
   vector<double>  *MuonTrkD0Error;
   vector<double>  *MuonTrkDz;
   vector<double>  *MuonTrkDzError;
   vector<double>  *MuonTrkEta;
   vector<double>  *MuonTrkEtaError;
   vector<double>  *MuonTrkIso;
   vector<double>  *MuonTrkPhi;
   vector<double>  *MuonTrkPhiError;
   vector<double>  *MuonTrkPt;
   vector<double>  *MuonTrkPtError;
   vector<double>  *MuonTrkValidFractionOfHits;
   vector<double>  *MuonTrkVx;
   vector<double>  *MuonTrkVy;
   vector<double>  *MuonTrkVz;
   vector<double>  *MuonVtxDistXY;
   vector<double>  *MuonVtxDistZ;
   vector<double>  *PFCandEnergyLeptLink;
   vector<double>  *PFCandEtaLeptLink;
   vector<double>  *PFCandPhiLeptLink;
   vector<double>  *PFCandPtLeptLink;
   vector<double>  *PFMETCharged;
   vector<double>  *PFMETPhiCharged;
   vector<double>  *PFSumETCharged;
   vector<double>  *PFJetBestVertexTrackAssociationFactor;
   vector<double>  *PFJetChargedEmEnergyFraction;
   vector<double>  *PFJetChargedHadronEnergyFraction;
   vector<double>  *PFJetChargedMuEnergyFraction;
   vector<double>  *PFJetClosestVertexWeighted3DSeparation;
   vector<double>  *PFJetClosestVertexWeightedXYSeparation;
   vector<double>  *PFJetClosestVertexWeightedZSeparation;
   vector<double>  *PFJetElectronEnergyFraction;
   vector<double>  *PFJetEnergy;
   vector<double>  *PFJetEnergyRaw;
   vector<double>  *PFJetEta;
   vector<double>  *PFJetHFEMEnergyFraction;
   vector<double>  *PFJetHFHadronEnergyFraction;
   vector<double>  *PFJetJECUnc;
   vector<double>  *PFJetJetBProbabilityBTag;
   vector<double>  *PFJetJetProbabilityBTag;
   vector<double>  *PFJetL1FastJetJEC;
   vector<double>  *PFJetL1OffsetJEC;
   vector<double>  *PFJetL2L3ResJEC;
   vector<double>  *PFJetL2RelJEC;
   vector<double>  *PFJetL3AbsJEC;
   vector<double>  *PFJetMuonEnergyFraction;
   vector<double>  *PFJetNeutralEmEnergyFraction;
   vector<double>  *PFJetNeutralHadronEnergyFraction;
   vector<double>  *PFJetPhi;
   vector<double>  *PFJetPhotonEnergyFraction;
   vector<double>  *PFJetPt;
   vector<double>  *PFJetPtRaw;
   vector<double>  *PFJetSimpleSecondaryVertexHighEffBTag;
   vector<double>  *PFJetSimpleSecondaryVertexHighPurBTag;
   vector<double>  *PFJetTrackCountingHighEffBTag;
   vector<double>  *PFJetTrackCountingHighPurBTag;
   vector<double>  *PFMET;
   vector<double>  *PFMETPhi;
   vector<double>  *PFMETSig;
   vector<double>  *PFMETSigMatrixDXX;
   vector<double>  *PFMETSigMatrixDXY;
   vector<double>  *PFMETSigMatrixDYX;
   vector<double>  *PFMETSigMatrixDYY;
   vector<double>  *PFSumET;
   vector<double>  *PFMETPhiType1Cor;
   vector<double>  *PFMETType1Cor;
   vector<double>  *PFSumETType1Cor;
   vector<double>  *PhotonAlpha;
   vector<double>  *PhotonChi2ConvPhot;
   vector<double>  *PhotonDPhiTracksAtVtxConvPhot;
   vector<double>  *PhotonDistOfMinApproachConvPhot;
   vector<double>  *PhotonE2OverE9;
   vector<double>  *PhotonE3x3;
   vector<double>  *PhotonE4SwissCross;
   vector<double>  *PhotonE5x5;
   vector<double>  *PhotonEOverPConvPhot;
   vector<double>  *PhotonEcalIsoDR03;
   vector<double>  *PhotonEcalIsoDR04;
   vector<double>  *PhotonEnergy;
   vector<double>  *PhotonEta;
   vector<double>  *PhotonHcalIsoDR03;
   vector<double>  *PhotonHcalIsoDR03FullCone;
   vector<double>  *PhotonHcalIsoDR04;
   vector<double>  *PhotonHcalIsoDR04FullCone;
   vector<double>  *PhotonHoE;
   vector<double>  *PhotonNDofConvPhot;
   vector<double>  *PhotonPairCotThetaSeparationConvPhot;
   vector<double>  *PhotonPairInvariantMassConvPhot;
   vector<double>  *PhotonPairMomentumxConvPhot;
   vector<double>  *PhotonPairMomentumyConvPhot;
   vector<double>  *PhotonPairMomentumzConvPhot;
   vector<double>  *PhotonPhi;
   vector<double>  *PhotonPt;
   vector<double>  *PhotonSCenergy;
   vector<double>  *PhotonSCeta;
   vector<double>  *PhotonSCphi;
   vector<double>  *PhotonSCseedEnergy;
   vector<double>  *PhotonSEtaEta;
   vector<double>  *PhotonSEtaPhi;
   vector<double>  *PhotonSMajMaj;
   vector<double>  *PhotonSMinMin;
   vector<double>  *PhotonSPhiPhi;
   vector<double>  *PhotonSigmaIEtaIEta;
   vector<double>  *PhotonTimeSeed;
   vector<double>  *PhotonTrkIsoHollowDR03;
   vector<double>  *PhotonTrkIsoHollowDR04;
   vector<double>  *PhotonTrkIsoSolidDR03;
   vector<double>  *PhotonTrkIsoSolidDR04;
   vector<double>  *PhotonXVtxConvPhot;
   vector<double>  *PhotonYVtxConvPhot;
   vector<double>  *PhotonZVtxConvPhot;
   vector<double>  *TCMET;
   vector<double>  *TCMETPhi;
   vector<double>  *TCSumET;
   vector<double>  *TauEmFraction;
   vector<double>  *TauEt;
   vector<double>  *TauEta;
   vector<double>  *TauEtaLeadCharged;
   vector<double>  *TauHcal3x3OverPLead;
   vector<double>  *TauHcalMaxOverPLead;
   vector<double>  *TauHcalTotOverPLead;
   vector<double>  *TauIsolationPFChargedHadrCandsPtSum;
   vector<double>  *TauIsolationPFGammaCandsEtSum;
   vector<double>  *TauLeadPFChargedHadrCandsignedSipt;
   vector<double>  *TauPhi;
   vector<double>  *TauPhiLeadCharged;
   vector<double>  *TauPt;
   vector<double>  *TauPtLeadCharged;
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
   vector<int>     *ElectronMissingHits;
   vector<int>     *ElectronNumberOfBrems;
   vector<int>     *ElectronOverlaps;
   vector<int>     *ElectronPassIDPAT;
   vector<int>     *ElectronPassIsoPAT;
   vector<int>     *ElectronVtxIndex;
   vector<int>     *PileUpInteractions;
   vector<int>     *PileUpOriginBX;
   vector<int>     *GenParticleMotherIndex;
   vector<int>     *GenParticleNumDaught;
   vector<int>     *GenParticlePdgId;
   vector<int>     *GenParticleStatus;
   vector<int>     *MuonCharge;
   vector<int>     *MuonCocktailCharge;
   vector<int>     *MuonCocktailPassIso;
   vector<int>     *MuonCocktailRefitID;
   vector<int>     *MuonCocktailTrkHits;
   vector<int>     *MuonGlobalTrkValidHits;
   vector<int>     *MuonIsGlobal;
   vector<int>     *MuonIsTracker;
   vector<int>     *MuonPassID;
   vector<int>     *MuonPassIso;
   vector<int>     *MuonPixelHitCount;
   vector<int>     *MuonSegmentMatches;
   vector<int>     *MuonStationMatches;
   vector<int>     *MuonTrkHits;
   vector<int>     *MuonTrkHitsTrackerOnly;
   vector<int>     *MuonTrkPixelHitCount;
   vector<int>     *MuonVtxIndex;
   vector<int>     *PFCandChargeLeptLink;
   vector<int>     *PFJetBestVertexTrackAssociationIndex;
   vector<int>     *PFJetChargedHadronMultiplicity;
   vector<int>     *PFJetChargedMultiplicity;
   vector<int>     *PFJetClosestVertex3DIndex;
   vector<int>     *PFJetClosestVertexXYIndex;
   vector<int>     *PFJetClosestVertexZIndex;
   vector<int>     *PFJetElectronMultiplicity;
   vector<int>     *PFJetHFEMMultiplicity;
   vector<int>     *PFJetHFHadronMultiplicity;
   vector<int>     *PFJetMuonMultiplicity;
   vector<int>     *PFJetNConstituents;
   vector<int>     *PFJetNeutralHadronMultiplicity;
   vector<int>     *PFJetNeutralMultiplicity;
   vector<int>     *PFJetPartonFlavour;
   vector<int>     *PFJetPassLooseID;
   vector<int>     *PFJetPassTightID;
   vector<int>     *PFJetPhotonMultiplicity;
   vector<int>     *PhotonNTracksConvPhot;
   vector<int>     *TauAgainstElectronDiscr;
   vector<int>     *TauAgainstMuonDiscr;
   vector<int>     *TauByIsolationDiscr;
   vector<int>     *TauByIsolationUsingLeadingPionDiscr;
   vector<int>     *TauCharge;
   vector<int>     *TauDecayMode;
   vector<int>     *TauEcalIsolationDiscr;
   vector<int>     *TauEcalIsolationUsingLeadingPionDiscr;
   vector<int>     *TauIsCaloTau;
   vector<int>     *TauIsPFTau;
   vector<int>     *TauLeadingPionPtCutDiscr;
   vector<int>     *TauLeadingTrackFindingDiscr;
   vector<int>     *TauLeadingTrackPtCutDiscr;
   vector<int>     *TauTrackIsolationDiscr;
   vector<int>     *TauTrackIsolationUsingLeadingPionDiscr;
   vector<int>     *HLTInsideDatasetTriggerPrescales;
   vector<int>     *HLTOutsideDatasetTriggerPrescales;
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
   TBranch        *b_HLTKey;   //!
   TBranch        *b_HLTInsideDatasetTriggerNames;   //!
   TBranch        *b_HLTOutsideDatasetTriggerNames;   //!
   TBranch        *b_isData;   //!
   TBranch        *b_isBPTX0;   //!
   TBranch        *b_isBSCBeamHalo;   //!
   TBranch        *b_isBSCMinBias;   //!
   TBranch        *b_isBeamScraping;   //!
   TBranch        *b_isPhysDeclared;   //!
   TBranch        *b_isPrimaryVertex;   //!
   TBranch        *b_isTrackingFailure;   //!
   TBranch        *b_passBeamHaloFilterLoose;   //!
   TBranch        *b_passBeamHaloFilterTight;   //!
   TBranch        *b_passCaloBoundaryDRFilter;   //!
   TBranch        *b_passEcalMaskedCellDRFilter;   //!
   TBranch        *b_passHBHENoiseFilter;   //!
   TBranch        *b_ElectronHasEcalDrivenSeed;   //!
   TBranch        *b_ElectronHasMatchedConvPhot;   //!
   TBranch        *b_PhotonHasMatchedConvPhot;   //!
   TBranch        *b_PhotonHasMatchedPromptEle;   //!
   TBranch        *b_PhotonHasPixelSeed;   //!
   TBranch        *b_PhotonIsEBEEGap;   //!
   TBranch        *b_PhotonIsEBGap;   //!
   TBranch        *b_PhotonIsEEGap;   //!
   TBranch        *b_HLTInsideDatasetTriggerDecisions;   //!
   TBranch        *b_HLTOutsideDatasetTriggerDecisions;   //!
   TBranch        *b_VertexIsFake;   //!
   TBranch        *b_rhoIso;   //!
   TBranch        *b_rhoJets;   //!
   TBranch        *b_time;   //!
   TBranch        *b_PtHat;   //!
   TBranch        *b_Weight;   //!
   TBranch        *b_CaloJetEMF;   //!
   TBranch        *b_CaloJetEnergy;   //!
   TBranch        *b_CaloJetEnergyRaw;   //!
   TBranch        *b_CaloJetEta;   //!
   TBranch        *b_CaloJetHADF;   //!
   TBranch        *b_CaloJetJECUnc;   //!
   TBranch        *b_CaloJetJetBProbabilityBTag;   //!
   TBranch        *b_CaloJetJetProbabilityBTag;   //!
   TBranch        *b_CaloJetL1FastJetJEC;   //!
   TBranch        *b_CaloJetL1OffsetJEC;   //!
   TBranch        *b_CaloJetL2L3ResJEC;   //!
   TBranch        *b_CaloJetL2RelJEC;   //!
   TBranch        *b_CaloJetL3AbsJEC;   //!
   TBranch        *b_CaloJetPhi;   //!
   TBranch        *b_CaloJetPt;   //!
   TBranch        *b_CaloJetPtRaw;   //!
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
   TBranch        *b_ElectronBeamSpotDXY;   //!
   TBranch        *b_ElectronBeamSpotDXYError;   //!
   TBranch        *b_ElectronCaloEnergy;   //!
   TBranch        *b_ElectronDCotTheta;   //!
   TBranch        *b_ElectronDeltaEtaTrkSC;   //!
   TBranch        *b_ElectronDeltaPhiTrkSC;   //!
   TBranch        *b_ElectronDist;   //!
   TBranch        *b_ElectronE1x5OverE5x5;   //!
   TBranch        *b_ElectronE2x5OverE5x5;   //!
   TBranch        *b_ElectronESuperClusterOverP;   //!
   TBranch        *b_ElectronEcalIsoDR03;   //!
   TBranch        *b_ElectronEcalIsoPAT;   //!
   TBranch        *b_ElectronEnergy;   //!
   TBranch        *b_ElectronEta;   //!
   TBranch        *b_ElectronFbrem;   //!
   TBranch        *b_ElectronHcalIsoD1DR03;   //!
   TBranch        *b_ElectronHcalIsoD2DR03;   //!
   TBranch        *b_ElectronHcalIsoDR03;   //!
   TBranch        *b_ElectronHcalIsoDR03FullCone;   //!
   TBranch        *b_ElectronHcalIsoPAT;   //!
   TBranch        *b_ElectronHoE;   //!
   TBranch        *b_ElectronLikelihood;   //!
   TBranch        *b_ElectronPhi;   //!
   TBranch        *b_ElectronPrimaryVertexDXY;   //!
   TBranch        *b_ElectronPrimaryVertexDXYError;   //!
   TBranch        *b_ElectronPt;   //!
   TBranch        *b_ElectronPtHeep;   //!
   TBranch        *b_ElectronRelIsoPAT;   //!
   TBranch        *b_ElectronSCEta;   //!
   TBranch        *b_ElectronSCPhi;   //!
   TBranch        *b_ElectronSCPt;   //!
   TBranch        *b_ElectronSCRawEnergy;   //!
   TBranch        *b_ElectronSigmaEtaEta;   //!
   TBranch        *b_ElectronSigmaIEtaIEta;   //!
   TBranch        *b_ElectronTrackPt;   //!
   TBranch        *b_ElectronTrackValidFractionOfHits;   //!
   TBranch        *b_ElectronTrackVx;   //!
   TBranch        *b_ElectronTrackVy;   //!
   TBranch        *b_ElectronTrackVz;   //!
   TBranch        *b_ElectronTrkIsoDR03;   //!
   TBranch        *b_ElectronTrkIsoPAT;   //!
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
   TBranch        *b_GenMETCalo;   //!
   TBranch        *b_GenMETPhiCalo;   //!
   TBranch        *b_GenSumETCalo;   //!
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
   TBranch        *b_MuonBackToBackCompatibility;   //!
   TBranch        *b_MuonBeamSpotDXY;   //!
   TBranch        *b_MuonBeamSpotDXYError;   //!
   TBranch        *b_MuonCocktailEta;   //!
   TBranch        *b_MuonCocktailEtaError;   //!
   TBranch        *b_MuonCocktailGlobalChi2;   //!
   TBranch        *b_MuonCocktailP;   //!
   TBranch        *b_MuonCocktailPhi;   //!
   TBranch        *b_MuonCocktailPhiError;   //!
   TBranch        *b_MuonCocktailPt;   //!
   TBranch        *b_MuonCocktailPtError;   //!
   TBranch        *b_MuonCocktailQOverPError;   //!
   TBranch        *b_MuonCocktailRelIso;   //!
   TBranch        *b_MuonCocktailTrkD0;   //!
   TBranch        *b_MuonCocktailTrkD0Error;   //!
   TBranch        *b_MuonCocktailTrkDz;   //!
   TBranch        *b_MuonCocktailTrkDzError;   //!
   TBranch        *b_MuonCocktailTrkValidFractionOfHits;   //!
   TBranch        *b_MuonCosmicCompatibility;   //!
   TBranch        *b_MuonEcalIso;   //!
   TBranch        *b_MuonEnergy;   //!
   TBranch        *b_MuonEta;   //!
   TBranch        *b_MuonEtaError;   //!
   TBranch        *b_MuonGlobalChi2;   //!
   TBranch        *b_MuonHOIso;   //!
   TBranch        *b_MuonHcalIso;   //!
   TBranch        *b_MuonOverlapCompatibility;   //!
   TBranch        *b_MuonP;   //!
   TBranch        *b_MuonPhi;   //!
   TBranch        *b_MuonPhiError;   //!
   TBranch        *b_MuonPrimaryVertexDXY;   //!
   TBranch        *b_MuonPrimaryVertexDXYError;   //!
   TBranch        *b_MuonPt;   //!
   TBranch        *b_MuonPtError;   //!
   TBranch        *b_MuonQOverPError;   //!
   TBranch        *b_MuonRelIso;   //!
   TBranch        *b_MuonTimeCompatibility;   //!
   TBranch        *b_MuonTrackChi2;   //!
   TBranch        *b_MuonTrackerIsoSumPT;   //!
   TBranch        *b_MuonTrkD0;   //!
   TBranch        *b_MuonTrkD0Error;   //!
   TBranch        *b_MuonTrkDz;   //!
   TBranch        *b_MuonTrkDzError;   //!
   TBranch        *b_MuonTrkEta;   //!
   TBranch        *b_MuonTrkEtaError;   //!
   TBranch        *b_MuonTrkIso;   //!
   TBranch        *b_MuonTrkPhi;   //!
   TBranch        *b_MuonTrkPhiError;   //!
   TBranch        *b_MuonTrkPt;   //!
   TBranch        *b_MuonTrkPtError;   //!
   TBranch        *b_MuonTrkValidFractionOfHits;   //!
   TBranch        *b_MuonTrkVx;   //!
   TBranch        *b_MuonTrkVy;   //!
   TBranch        *b_MuonTrkVz;   //!
   TBranch        *b_MuonVtxDistXY;   //!
   TBranch        *b_MuonVtxDistZ;   //!
   TBranch        *b_PFCandEnergyLeptLink;   //!
   TBranch        *b_PFCandEtaLeptLink;   //!
   TBranch        *b_PFCandPhiLeptLink;   //!
   TBranch        *b_PFCandPtLeptLink;   //!
   TBranch        *b_PFMETCharged;   //!
   TBranch        *b_PFMETPhiCharged;   //!
   TBranch        *b_PFSumETCharged;   //!
   TBranch        *b_PFJetBestVertexTrackAssociationFactor;   //!
   TBranch        *b_PFJetChargedEmEnergyFraction;   //!
   TBranch        *b_PFJetChargedHadronEnergyFraction;   //!
   TBranch        *b_PFJetChargedMuEnergyFraction;   //!
   TBranch        *b_PFJetClosestVertexWeighted3DSeparation;   //!
   TBranch        *b_PFJetClosestVertexWeightedXYSeparation;   //!
   TBranch        *b_PFJetClosestVertexWeightedZSeparation;   //!
   TBranch        *b_PFJetElectronEnergyFraction;   //!
   TBranch        *b_PFJetEnergy;   //!
   TBranch        *b_PFJetEnergyRaw;   //!
   TBranch        *b_PFJetEta;   //!
   TBranch        *b_PFJetHFEMEnergyFraction;   //!
   TBranch        *b_PFJetHFHadronEnergyFraction;   //!
   TBranch        *b_PFJetJECUnc;   //!
   TBranch        *b_PFJetJetBProbabilityBTag;   //!
   TBranch        *b_PFJetJetProbabilityBTag;   //!
   TBranch        *b_PFJetL1FastJetJEC;   //!
   TBranch        *b_PFJetL1OffsetJEC;   //!
   TBranch        *b_PFJetL2L3ResJEC;   //!
   TBranch        *b_PFJetL2RelJEC;   //!
   TBranch        *b_PFJetL3AbsJEC;   //!
   TBranch        *b_PFJetMuonEnergyFraction;   //!
   TBranch        *b_PFJetNeutralEmEnergyFraction;   //!
   TBranch        *b_PFJetNeutralHadronEnergyFraction;   //!
   TBranch        *b_PFJetPhi;   //!
   TBranch        *b_PFJetPhotonEnergyFraction;   //!
   TBranch        *b_PFJetPt;   //!
   TBranch        *b_PFJetPtRaw;   //!
   TBranch        *b_PFJetSimpleSecondaryVertexHighEffBTag;   //!
   TBranch        *b_PFJetSimpleSecondaryVertexHighPurBTag;   //!
   TBranch        *b_PFJetTrackCountingHighEffBTag;   //!
   TBranch        *b_PFJetTrackCountingHighPurBTag;   //!
   TBranch        *b_PFMET;   //!
   TBranch        *b_PFMETPhi;   //!
   TBranch        *b_PFMETSig;   //!
   TBranch        *b_PFMETSigMatrixDXX;   //!
   TBranch        *b_PFMETSigMatrixDXY;   //!
   TBranch        *b_PFMETSigMatrixDYX;   //!
   TBranch        *b_PFMETSigMatrixDYY;   //!
   TBranch        *b_PFSumET;   //!
   TBranch        *b_PFMETPhiType1Cor;   //!
   TBranch        *b_PFMETType1Cor;   //!
   TBranch        *b_PFSumETType1Cor;   //!
   TBranch        *b_PhotonAlpha;   //!
   TBranch        *b_PhotonChi2ConvPhot;   //!
   TBranch        *b_PhotonDPhiTracksAtVtxConvPhot;   //!
   TBranch        *b_PhotonDistOfMinApproachConvPhot;   //!
   TBranch        *b_PhotonE2OverE9;   //!
   TBranch        *b_PhotonE3x3;   //!
   TBranch        *b_PhotonE4SwissCross;   //!
   TBranch        *b_PhotonE5x5;   //!
   TBranch        *b_PhotonEOverPConvPhot;   //!
   TBranch        *b_PhotonEcalIsoDR03;   //!
   TBranch        *b_PhotonEcalIsoDR04;   //!
   TBranch        *b_PhotonEnergy;   //!
   TBranch        *b_PhotonEta;   //!
   TBranch        *b_PhotonHcalIsoDR03;   //!
   TBranch        *b_PhotonHcalIsoDR03FullCone;   //!
   TBranch        *b_PhotonHcalIsoDR04;   //!
   TBranch        *b_PhotonHcalIsoDR04FullCone;   //!
   TBranch        *b_PhotonHoE;   //!
   TBranch        *b_PhotonNDofConvPhot;   //!
   TBranch        *b_PhotonPairCotThetaSeparationConvPhot;   //!
   TBranch        *b_PhotonPairInvariantMassConvPhot;   //!
   TBranch        *b_PhotonPairMomentumxConvPhot;   //!
   TBranch        *b_PhotonPairMomentumyConvPhot;   //!
   TBranch        *b_PhotonPairMomentumzConvPhot;   //!
   TBranch        *b_PhotonPhi;   //!
   TBranch        *b_PhotonPt;   //!
   TBranch        *b_PhotonSCenergy;   //!
   TBranch        *b_PhotonSCeta;   //!
   TBranch        *b_PhotonSCphi;   //!
   TBranch        *b_PhotonSCseedEnergy;   //!
   TBranch        *b_PhotonSEtaEta;   //!
   TBranch        *b_PhotonSEtaPhi;   //!
   TBranch        *b_PhotonSMajMaj;   //!
   TBranch        *b_PhotonSMinMin;   //!
   TBranch        *b_PhotonSPhiPhi;   //!
   TBranch        *b_PhotonSigmaIEtaIEta;   //!
   TBranch        *b_PhotonTimeSeed;   //!
   TBranch        *b_PhotonTrkIsoHollowDR03;   //!
   TBranch        *b_PhotonTrkIsoHollowDR04;   //!
   TBranch        *b_PhotonTrkIsoSolidDR03;   //!
   TBranch        *b_PhotonTrkIsoSolidDR04;   //!
   TBranch        *b_PhotonXVtxConvPhot;   //!
   TBranch        *b_PhotonYVtxConvPhot;   //!
   TBranch        *b_PhotonZVtxConvPhot;   //!
   TBranch        *b_TCMET;   //!
   TBranch        *b_TCMETPhi;   //!
   TBranch        *b_TCSumET;   //!
   TBranch        *b_TauEmFraction;   //!
   TBranch        *b_TauEt;   //!
   TBranch        *b_TauEta;   //!
   TBranch        *b_TauEtaLeadCharged;   //!
   TBranch        *b_TauHcal3x3OverPLead;   //!
   TBranch        *b_TauHcalMaxOverPLead;   //!
   TBranch        *b_TauHcalTotOverPLead;   //!
   TBranch        *b_TauIsolationPFChargedHadrCandsPtSum;   //!
   TBranch        *b_TauIsolationPFGammaCandsEtSum;   //!
   TBranch        *b_TauLeadPFChargedHadrCandsignedSipt;   //!
   TBranch        *b_TauPhi;   //!
   TBranch        *b_TauPhiLeadCharged;   //!
   TBranch        *b_TauPt;   //!
   TBranch        *b_TauPtLeadCharged;   //!
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
   TBranch        *b_ElectronMissingHits;   //!
   TBranch        *b_ElectronNumberOfBrems;   //!
   TBranch        *b_ElectronOverlaps;   //!
   TBranch        *b_ElectronPassIDPAT;   //!
   TBranch        *b_ElectronPassIsoPAT;   //!
   TBranch        *b_ElectronVtxIndex;   //!
   TBranch        *b_PileUpInteractions;   //!
   TBranch        *b_PileUpOriginBX;   //!
   TBranch        *b_GenParticleMotherIndex;   //!
   TBranch        *b_GenParticleNumDaught;   //!
   TBranch        *b_GenParticlePdgId;   //!
   TBranch        *b_GenParticleStatus;   //!
   TBranch        *b_MuonCharge;   //!
   TBranch        *b_MuonCocktailCharge;   //!
   TBranch        *b_MuonCocktailPassIso;   //!
   TBranch        *b_MuonCocktailRefitID;   //!
   TBranch        *b_MuonCocktailTrkHits;   //!
   TBranch        *b_MuonGlobalTrkValidHits;   //!
   TBranch        *b_MuonIsGlobal;   //!
   TBranch        *b_MuonIsTracker;   //!
   TBranch        *b_MuonPassID;   //!
   TBranch        *b_MuonPassIso;   //!
   TBranch        *b_MuonPixelHitCount;   //!
   TBranch        *b_MuonSegmentMatches;   //!
   TBranch        *b_MuonStationMatches;   //!
   TBranch        *b_MuonTrkHits;   //!
   TBranch        *b_MuonTrkHitsTrackerOnly;   //!
   TBranch        *b_MuonTrkPixelHitCount;   //!
   TBranch        *b_MuonVtxIndex;   //!
   TBranch        *b_PFCandChargeLeptLink;   //!
   TBranch        *b_PFJetBestVertexTrackAssociationIndex;   //!
   TBranch        *b_PFJetChargedHadronMultiplicity;   //!
   TBranch        *b_PFJetChargedMultiplicity;   //!
   TBranch        *b_PFJetClosestVertex3DIndex;   //!
   TBranch        *b_PFJetClosestVertexXYIndex;   //!
   TBranch        *b_PFJetClosestVertexZIndex;   //!
   TBranch        *b_PFJetElectronMultiplicity;   //!
   TBranch        *b_PFJetHFEMMultiplicity;   //!
   TBranch        *b_PFJetHFHadronMultiplicity;   //!
   TBranch        *b_PFJetMuonMultiplicity;   //!
   TBranch        *b_PFJetNConstituents;   //!
   TBranch        *b_PFJetNeutralHadronMultiplicity;   //!
   TBranch        *b_PFJetNeutralMultiplicity;   //!
   TBranch        *b_PFJetPartonFlavour;   //!
   TBranch        *b_PFJetPassLooseID;   //!
   TBranch        *b_PFJetPassTightID;   //!
   TBranch        *b_PFJetPhotonMultiplicity;   //!
   TBranch        *b_PhotonNTracksConvPhot;   //!
   TBranch        *b_TauAgainstElectronDiscr;   //!
   TBranch        *b_TauAgainstMuonDiscr;   //!
   TBranch        *b_TauByIsolationDiscr;   //!
   TBranch        *b_TauByIsolationUsingLeadingPionDiscr;   //!
   TBranch        *b_TauCharge;   //!
   TBranch        *b_TauDecayMode;   //!
   TBranch        *b_TauEcalIsolationDiscr;   //!
   TBranch        *b_TauEcalIsolationUsingLeadingPionDiscr;   //!
   TBranch        *b_TauIsCaloTau;   //!
   TBranch        *b_TauIsPFTau;   //!
   TBranch        *b_TauLeadingPionPtCutDiscr;   //!
   TBranch        *b_TauLeadingTrackFindingDiscr;   //!
   TBranch        *b_TauLeadingTrackPtCutDiscr;   //!
   TBranch        *b_TauTrackIsolationDiscr;   //!
   TBranch        *b_TauTrackIsolationUsingLeadingPionDiscr;   //!
   TBranch        *b_HLTInsideDatasetTriggerPrescales;   //!
   TBranch        *b_HLTOutsideDatasetTriggerPrescales;   //!
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



   placeholder(TTree *tree=0);
   virtual ~placeholder();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef placeholder_cxx
placeholder::placeholder(TTree *tree)

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

placeholder::~placeholder()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t placeholder::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t placeholder::LoadTree(Long64_t entry)
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

void placeholder::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   HLTKey = 0;
   HLTInsideDatasetTriggerNames = 0;
   HLTOutsideDatasetTriggerNames = 0;
   ElectronHasEcalDrivenSeed = 0;
   ElectronHasMatchedConvPhot = 0;
   PhotonHasMatchedConvPhot = 0;
   PhotonHasMatchedPromptEle = 0;
   PhotonHasPixelSeed = 0;
   PhotonIsEBEEGap = 0;
   PhotonIsEBGap = 0;
   PhotonIsEEGap = 0;
   HLTInsideDatasetTriggerDecisions = 0;
   HLTOutsideDatasetTriggerDecisions = 0;
   VertexIsFake = 0;
   CaloJetEMF = 0;
   CaloJetEnergy = 0;
   CaloJetEnergyRaw = 0;
   CaloJetEta = 0;
   CaloJetHADF = 0;
   CaloJetJECUnc = 0;
   CaloJetJetBProbabilityBTag = 0;
   CaloJetJetProbabilityBTag = 0;
   CaloJetL1FastJetJEC = 0;
   CaloJetL1OffsetJEC = 0;
   CaloJetL2L3ResJEC = 0;
   CaloJetL2RelJEC = 0;
   CaloJetL3AbsJEC = 0;
   CaloJetPhi = 0;
   CaloJetPt = 0;
   CaloJetPtRaw = 0;
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
   ElectronBeamSpotDXY = 0;
   ElectronBeamSpotDXYError = 0;
   ElectronCaloEnergy = 0;
   ElectronDCotTheta = 0;
   ElectronDeltaEtaTrkSC = 0;
   ElectronDeltaPhiTrkSC = 0;
   ElectronDist = 0;
   ElectronE1x5OverE5x5 = 0;
   ElectronE2x5OverE5x5 = 0;
   ElectronESuperClusterOverP = 0;
   ElectronEcalIsoDR03 = 0;
   ElectronEcalIsoPAT = 0;
   ElectronEnergy = 0;
   ElectronEta = 0;
   ElectronFbrem = 0;
   ElectronHcalIsoD1DR03 = 0;
   ElectronHcalIsoD2DR03 = 0;
   ElectronHcalIsoDR03 = 0;
   ElectronHcalIsoDR03FullCone = 0;
   ElectronHcalIsoPAT = 0;
   ElectronHoE = 0;
   ElectronLikelihood = 0;
   ElectronPhi = 0;
   ElectronPrimaryVertexDXY = 0;
   ElectronPrimaryVertexDXYError = 0;
   ElectronPt = 0;
   ElectronPtHeep = 0;
   ElectronRelIsoPAT = 0;
   ElectronSCEta = 0;
   ElectronSCPhi = 0;
   ElectronSCPt = 0;
   ElectronSCRawEnergy = 0;
   ElectronSigmaEtaEta = 0;
   ElectronSigmaIEtaIEta = 0;
   ElectronTrackPt = 0;
   ElectronTrackValidFractionOfHits = 0;
   ElectronTrackVx = 0;
   ElectronTrackVy = 0;
   ElectronTrackVz = 0;
   ElectronTrkIsoDR03 = 0;
   ElectronTrkIsoPAT = 0;
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
   GenMETCalo = 0;
   GenMETPhiCalo = 0;
   GenSumETCalo = 0;
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
   MuonBackToBackCompatibility = 0;
   MuonBeamSpotDXY = 0;
   MuonBeamSpotDXYError = 0;
   MuonCocktailEta = 0;
   MuonCocktailEtaError = 0;
   MuonCocktailGlobalChi2 = 0;
   MuonCocktailP = 0;
   MuonCocktailPhi = 0;
   MuonCocktailPhiError = 0;
   MuonCocktailPt = 0;
   MuonCocktailPtError = 0;
   MuonCocktailQOverPError = 0;
   MuonCocktailRelIso = 0;
   MuonCocktailTrkD0 = 0;
   MuonCocktailTrkD0Error = 0;
   MuonCocktailTrkDz = 0;
   MuonCocktailTrkDzError = 0;
   MuonCocktailTrkValidFractionOfHits = 0;
   MuonCosmicCompatibility = 0;
   MuonEcalIso = 0;
   MuonEnergy = 0;
   MuonEta = 0;
   MuonEtaError = 0;
   MuonGlobalChi2 = 0;
   MuonHOIso = 0;
   MuonHcalIso = 0;
   MuonOverlapCompatibility = 0;
   MuonP = 0;
   MuonPhi = 0;
   MuonPhiError = 0;
   MuonPrimaryVertexDXY = 0;
   MuonPrimaryVertexDXYError = 0;
   MuonPt = 0;
   MuonPtError = 0;
   MuonQOverPError = 0;
   MuonRelIso = 0;
   MuonTimeCompatibility = 0;
   MuonTrackChi2 = 0;
   MuonTrackerIsoSumPT = 0;
   MuonTrkD0 = 0;
   MuonTrkD0Error = 0;
   MuonTrkDz = 0;
   MuonTrkDzError = 0;
   MuonTrkEta = 0;
   MuonTrkEtaError = 0;
   MuonTrkIso = 0;
   MuonTrkPhi = 0;
   MuonTrkPhiError = 0;
   MuonTrkPt = 0;
   MuonTrkPtError = 0;
   MuonTrkValidFractionOfHits = 0;
   MuonTrkVx = 0;
   MuonTrkVy = 0;
   MuonTrkVz = 0;
   MuonVtxDistXY = 0;
   MuonVtxDistZ = 0;
   PFCandEnergyLeptLink = 0;
   PFCandEtaLeptLink = 0;
   PFCandPhiLeptLink = 0;
   PFCandPtLeptLink = 0;
   PFMETCharged = 0;
   PFMETPhiCharged = 0;
   PFSumETCharged = 0;
   PFJetBestVertexTrackAssociationFactor = 0;
   PFJetChargedEmEnergyFraction = 0;
   PFJetChargedHadronEnergyFraction = 0;
   PFJetChargedMuEnergyFraction = 0;
   PFJetClosestVertexWeighted3DSeparation = 0;
   PFJetClosestVertexWeightedXYSeparation = 0;
   PFJetClosestVertexWeightedZSeparation = 0;
   PFJetElectronEnergyFraction = 0;
   PFJetEnergy = 0;
   PFJetEnergyRaw = 0;
   PFJetEta = 0;
   PFJetHFEMEnergyFraction = 0;
   PFJetHFHadronEnergyFraction = 0;
   PFJetJECUnc = 0;
   PFJetJetBProbabilityBTag = 0;
   PFJetJetProbabilityBTag = 0;
   PFJetL1FastJetJEC = 0;
   PFJetL1OffsetJEC = 0;
   PFJetL2L3ResJEC = 0;
   PFJetL2RelJEC = 0;
   PFJetL3AbsJEC = 0;
   PFJetMuonEnergyFraction = 0;
   PFJetNeutralEmEnergyFraction = 0;
   PFJetNeutralHadronEnergyFraction = 0;
   PFJetPhi = 0;
   PFJetPhotonEnergyFraction = 0;
   PFJetPt = 0;
   PFJetPtRaw = 0;
   PFJetSimpleSecondaryVertexHighEffBTag = 0;
   PFJetSimpleSecondaryVertexHighPurBTag = 0;
   PFJetTrackCountingHighEffBTag = 0;
   PFJetTrackCountingHighPurBTag = 0;
   PFMET = 0;
   PFMETPhi = 0;
   PFMETSig = 0;
   PFMETSigMatrixDXX = 0;
   PFMETSigMatrixDXY = 0;
   PFMETSigMatrixDYX = 0;
   PFMETSigMatrixDYY = 0;
   PFSumET = 0;
   PFMETPhiType1Cor = 0;
   PFMETType1Cor = 0;
   PFSumETType1Cor = 0;
   PhotonAlpha = 0;
   PhotonChi2ConvPhot = 0;
   PhotonDPhiTracksAtVtxConvPhot = 0;
   PhotonDistOfMinApproachConvPhot = 0;
   PhotonE2OverE9 = 0;
   PhotonE3x3 = 0;
   PhotonE4SwissCross = 0;
   PhotonE5x5 = 0;
   PhotonEOverPConvPhot = 0;
   PhotonEcalIsoDR03 = 0;
   PhotonEcalIsoDR04 = 0;
   PhotonEnergy = 0;
   PhotonEta = 0;
   PhotonHcalIsoDR03 = 0;
   PhotonHcalIsoDR03FullCone = 0;
   PhotonHcalIsoDR04 = 0;
   PhotonHcalIsoDR04FullCone = 0;
   PhotonHoE = 0;
   PhotonNDofConvPhot = 0;
   PhotonPairCotThetaSeparationConvPhot = 0;
   PhotonPairInvariantMassConvPhot = 0;
   PhotonPairMomentumxConvPhot = 0;
   PhotonPairMomentumyConvPhot = 0;
   PhotonPairMomentumzConvPhot = 0;
   PhotonPhi = 0;
   PhotonPt = 0;
   PhotonSCenergy = 0;
   PhotonSCeta = 0;
   PhotonSCphi = 0;
   PhotonSCseedEnergy = 0;
   PhotonSEtaEta = 0;
   PhotonSEtaPhi = 0;
   PhotonSMajMaj = 0;
   PhotonSMinMin = 0;
   PhotonSPhiPhi = 0;
   PhotonSigmaIEtaIEta = 0;
   PhotonTimeSeed = 0;
   PhotonTrkIsoHollowDR03 = 0;
   PhotonTrkIsoHollowDR04 = 0;
   PhotonTrkIsoSolidDR03 = 0;
   PhotonTrkIsoSolidDR04 = 0;
   PhotonXVtxConvPhot = 0;
   PhotonYVtxConvPhot = 0;
   PhotonZVtxConvPhot = 0;
   TCMET = 0;
   TCMETPhi = 0;
   TCSumET = 0;
   TauEmFraction = 0;
   TauEt = 0;
   TauEta = 0;
   TauEtaLeadCharged = 0;
   TauHcal3x3OverPLead = 0;
   TauHcalMaxOverPLead = 0;
   TauHcalTotOverPLead = 0;
   TauIsolationPFChargedHadrCandsPtSum = 0;
   TauIsolationPFGammaCandsEtSum = 0;
   TauLeadPFChargedHadrCandsignedSipt = 0;
   TauPhi = 0;
   TauPhiLeadCharged = 0;
   TauPt = 0;
   TauPtLeadCharged = 0;
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
   ElectronMissingHits = 0;
   ElectronNumberOfBrems = 0;
   ElectronOverlaps = 0;
   ElectronPassIDPAT = 0;
   ElectronPassIsoPAT = 0;
   ElectronVtxIndex = 0;
   PileUpInteractions = 0;
   PileUpOriginBX = 0;
   GenParticleMotherIndex = 0;
   GenParticleNumDaught = 0;
   GenParticlePdgId = 0;
   GenParticleStatus = 0;
   MuonCharge = 0;
   MuonCocktailCharge = 0;
   MuonCocktailPassIso = 0;
   MuonCocktailRefitID = 0;
   MuonCocktailTrkHits = 0;
   MuonGlobalTrkValidHits = 0;
   MuonIsGlobal = 0;
   MuonIsTracker = 0;
   MuonPassID = 0;
   MuonPassIso = 0;
   MuonPixelHitCount = 0;
   MuonSegmentMatches = 0;
   MuonStationMatches = 0;
   MuonTrkHits = 0;
   MuonTrkHitsTrackerOnly = 0;
   MuonTrkPixelHitCount = 0;
   MuonVtxIndex = 0;
   PFCandChargeLeptLink = 0;
   PFJetBestVertexTrackAssociationIndex = 0;
   PFJetChargedHadronMultiplicity = 0;
   PFJetChargedMultiplicity = 0;
   PFJetClosestVertex3DIndex = 0;
   PFJetClosestVertexXYIndex = 0;
   PFJetClosestVertexZIndex = 0;
   PFJetElectronMultiplicity = 0;
   PFJetHFEMMultiplicity = 0;
   PFJetHFHadronMultiplicity = 0;
   PFJetMuonMultiplicity = 0;
   PFJetNConstituents = 0;
   PFJetNeutralHadronMultiplicity = 0;
   PFJetNeutralMultiplicity = 0;
   PFJetPartonFlavour = 0;
   PFJetPassLooseID = 0;
   PFJetPassTightID = 0;
   PFJetPhotonMultiplicity = 0;
   PhotonNTracksConvPhot = 0;
   TauAgainstElectronDiscr = 0;
   TauAgainstMuonDiscr = 0;
   TauByIsolationDiscr = 0;
   TauByIsolationUsingLeadingPionDiscr = 0;
   TauCharge = 0;
   TauDecayMode = 0;
   TauEcalIsolationDiscr = 0;
   TauEcalIsolationUsingLeadingPionDiscr = 0;
   TauIsCaloTau = 0;
   TauIsPFTau = 0;
   TauLeadingPionPtCutDiscr = 0;
   TauLeadingTrackFindingDiscr = 0;
   TauLeadingTrackPtCutDiscr = 0;
   TauTrackIsolationDiscr = 0;
   TauTrackIsolationUsingLeadingPionDiscr = 0;
   HLTInsideDatasetTriggerPrescales = 0;
   HLTOutsideDatasetTriggerPrescales = 0;
   L1PhysBits = 0;
   L1TechBits = 0;
   VertexNTracks = 0;
   VertexNTracksW05 = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("HLTKey", &HLTKey, &b_HLTKey);
   fChain->SetBranchAddress("HLTInsideDatasetTriggerNames", &HLTInsideDatasetTriggerNames, &b_HLTInsideDatasetTriggerNames);
   fChain->SetBranchAddress("HLTOutsideDatasetTriggerNames", &HLTOutsideDatasetTriggerNames, &b_HLTOutsideDatasetTriggerNames);
   fChain->SetBranchAddress("isData", &isData, &b_isData);
   fChain->SetBranchAddress("isBPTX0", &isBPTX0, &b_isBPTX0);
   fChain->SetBranchAddress("isBSCBeamHalo", &isBSCBeamHalo, &b_isBSCBeamHalo);
   fChain->SetBranchAddress("isBSCMinBias", &isBSCMinBias, &b_isBSCMinBias);
   fChain->SetBranchAddress("isBeamScraping", &isBeamScraping, &b_isBeamScraping);
   fChain->SetBranchAddress("isPhysDeclared", &isPhysDeclared, &b_isPhysDeclared);
   fChain->SetBranchAddress("isPrimaryVertex", &isPrimaryVertex, &b_isPrimaryVertex);
   fChain->SetBranchAddress("isTrackingFailure", &isTrackingFailure, &b_isTrackingFailure);
   fChain->SetBranchAddress("passBeamHaloFilterLoose", &passBeamHaloFilterLoose, &b_passBeamHaloFilterLoose);
   fChain->SetBranchAddress("passBeamHaloFilterTight", &passBeamHaloFilterTight, &b_passBeamHaloFilterTight);
   fChain->SetBranchAddress("passCaloBoundaryDRFilter", &passCaloBoundaryDRFilter, &b_passCaloBoundaryDRFilter);
   fChain->SetBranchAddress("passEcalMaskedCellDRFilter", &passEcalMaskedCellDRFilter, &b_passEcalMaskedCellDRFilter);
   fChain->SetBranchAddress("passHBHENoiseFilter", &passHBHENoiseFilter, &b_passHBHENoiseFilter);
   fChain->SetBranchAddress("ElectronHasEcalDrivenSeed", &ElectronHasEcalDrivenSeed, &b_ElectronHasEcalDrivenSeed);
   fChain->SetBranchAddress("ElectronHasMatchedConvPhot", &ElectronHasMatchedConvPhot, &b_ElectronHasMatchedConvPhot);
   fChain->SetBranchAddress("PhotonHasMatchedConvPhot", &PhotonHasMatchedConvPhot, &b_PhotonHasMatchedConvPhot);
   fChain->SetBranchAddress("PhotonHasMatchedPromptEle", &PhotonHasMatchedPromptEle, &b_PhotonHasMatchedPromptEle);
   fChain->SetBranchAddress("PhotonHasPixelSeed", &PhotonHasPixelSeed, &b_PhotonHasPixelSeed);
   fChain->SetBranchAddress("PhotonIsEBEEGap", &PhotonIsEBEEGap, &b_PhotonIsEBEEGap);
   fChain->SetBranchAddress("PhotonIsEBGap", &PhotonIsEBGap, &b_PhotonIsEBGap);
   fChain->SetBranchAddress("PhotonIsEEGap", &PhotonIsEEGap, &b_PhotonIsEEGap);
   fChain->SetBranchAddress("HLTInsideDatasetTriggerDecisions", &HLTInsideDatasetTriggerDecisions, &b_HLTInsideDatasetTriggerDecisions);
   fChain->SetBranchAddress("HLTOutsideDatasetTriggerDecisions", &HLTOutsideDatasetTriggerDecisions, &b_HLTOutsideDatasetTriggerDecisions);
   fChain->SetBranchAddress("VertexIsFake", &VertexIsFake, &b_VertexIsFake);
   fChain->SetBranchAddress("rhoIso", &rhoIso, &b_rhoIso);
   fChain->SetBranchAddress("rhoJets", &rhoJets, &b_rhoJets);
   fChain->SetBranchAddress("time", &time, &b_time);
   fChain->SetBranchAddress("PtHat", &PtHat, &b_PtHat);
   fChain->SetBranchAddress("Weight", &Weight, &b_Weight);
   fChain->SetBranchAddress("CaloJetEMF", &CaloJetEMF, &b_CaloJetEMF);
   fChain->SetBranchAddress("CaloJetEnergy", &CaloJetEnergy, &b_CaloJetEnergy);
   fChain->SetBranchAddress("CaloJetEnergyRaw", &CaloJetEnergyRaw, &b_CaloJetEnergyRaw);
   fChain->SetBranchAddress("CaloJetEta", &CaloJetEta, &b_CaloJetEta);
   fChain->SetBranchAddress("CaloJetHADF", &CaloJetHADF, &b_CaloJetHADF);
   fChain->SetBranchAddress("CaloJetJECUnc", &CaloJetJECUnc, &b_CaloJetJECUnc);
   fChain->SetBranchAddress("CaloJetJetBProbabilityBTag", &CaloJetJetBProbabilityBTag, &b_CaloJetJetBProbabilityBTag);
   fChain->SetBranchAddress("CaloJetJetProbabilityBTag", &CaloJetJetProbabilityBTag, &b_CaloJetJetProbabilityBTag);
   fChain->SetBranchAddress("CaloJetL1FastJetJEC", &CaloJetL1FastJetJEC, &b_CaloJetL1FastJetJEC);
   fChain->SetBranchAddress("CaloJetL1OffsetJEC", &CaloJetL1OffsetJEC, &b_CaloJetL1OffsetJEC);
   fChain->SetBranchAddress("CaloJetL2L3ResJEC", &CaloJetL2L3ResJEC, &b_CaloJetL2L3ResJEC);
   fChain->SetBranchAddress("CaloJetL2RelJEC", &CaloJetL2RelJEC, &b_CaloJetL2RelJEC);
   fChain->SetBranchAddress("CaloJetL3AbsJEC", &CaloJetL3AbsJEC, &b_CaloJetL3AbsJEC);
   fChain->SetBranchAddress("CaloJetPhi", &CaloJetPhi, &b_CaloJetPhi);
   fChain->SetBranchAddress("CaloJetPt", &CaloJetPt, &b_CaloJetPt);
   fChain->SetBranchAddress("CaloJetPtRaw", &CaloJetPtRaw, &b_CaloJetPtRaw);
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
   fChain->SetBranchAddress("ElectronBeamSpotDXY", &ElectronBeamSpotDXY, &b_ElectronBeamSpotDXY);
   fChain->SetBranchAddress("ElectronBeamSpotDXYError", &ElectronBeamSpotDXYError, &b_ElectronBeamSpotDXYError);
   fChain->SetBranchAddress("ElectronCaloEnergy", &ElectronCaloEnergy, &b_ElectronCaloEnergy);
   fChain->SetBranchAddress("ElectronDCotTheta", &ElectronDCotTheta, &b_ElectronDCotTheta);
   fChain->SetBranchAddress("ElectronDeltaEtaTrkSC", &ElectronDeltaEtaTrkSC, &b_ElectronDeltaEtaTrkSC);
   fChain->SetBranchAddress("ElectronDeltaPhiTrkSC", &ElectronDeltaPhiTrkSC, &b_ElectronDeltaPhiTrkSC);
   fChain->SetBranchAddress("ElectronDist", &ElectronDist, &b_ElectronDist);
   fChain->SetBranchAddress("ElectronE1x5OverE5x5", &ElectronE1x5OverE5x5, &b_ElectronE1x5OverE5x5);
   fChain->SetBranchAddress("ElectronE2x5OverE5x5", &ElectronE2x5OverE5x5, &b_ElectronE2x5OverE5x5);
   fChain->SetBranchAddress("ElectronESuperClusterOverP", &ElectronESuperClusterOverP, &b_ElectronESuperClusterOverP);
   fChain->SetBranchAddress("ElectronEcalIsoDR03", &ElectronEcalIsoDR03, &b_ElectronEcalIsoDR03);
   fChain->SetBranchAddress("ElectronEcalIsoPAT", &ElectronEcalIsoPAT, &b_ElectronEcalIsoPAT);
   fChain->SetBranchAddress("ElectronEnergy", &ElectronEnergy, &b_ElectronEnergy);
   fChain->SetBranchAddress("ElectronEta", &ElectronEta, &b_ElectronEta);
   fChain->SetBranchAddress("ElectronFbrem", &ElectronFbrem, &b_ElectronFbrem);
   fChain->SetBranchAddress("ElectronHcalIsoD1DR03", &ElectronHcalIsoD1DR03, &b_ElectronHcalIsoD1DR03);
   fChain->SetBranchAddress("ElectronHcalIsoD2DR03", &ElectronHcalIsoD2DR03, &b_ElectronHcalIsoD2DR03);
   fChain->SetBranchAddress("ElectronHcalIsoDR03", &ElectronHcalIsoDR03, &b_ElectronHcalIsoDR03);
   fChain->SetBranchAddress("ElectronHcalIsoDR03FullCone", &ElectronHcalIsoDR03FullCone, &b_ElectronHcalIsoDR03FullCone);
   fChain->SetBranchAddress("ElectronHcalIsoPAT", &ElectronHcalIsoPAT, &b_ElectronHcalIsoPAT);
   fChain->SetBranchAddress("ElectronHoE", &ElectronHoE, &b_ElectronHoE);
   fChain->SetBranchAddress("ElectronLikelihood", &ElectronLikelihood, &b_ElectronLikelihood);
   fChain->SetBranchAddress("ElectronPhi", &ElectronPhi, &b_ElectronPhi);
   fChain->SetBranchAddress("ElectronPrimaryVertexDXY", &ElectronPrimaryVertexDXY, &b_ElectronPrimaryVertexDXY);
   fChain->SetBranchAddress("ElectronPrimaryVertexDXYError", &ElectronPrimaryVertexDXYError, &b_ElectronPrimaryVertexDXYError);
   fChain->SetBranchAddress("ElectronPt", &ElectronPt, &b_ElectronPt);
   fChain->SetBranchAddress("ElectronPtHeep", &ElectronPtHeep, &b_ElectronPtHeep);
   fChain->SetBranchAddress("ElectronRelIsoPAT", &ElectronRelIsoPAT, &b_ElectronRelIsoPAT);
   fChain->SetBranchAddress("ElectronSCEta", &ElectronSCEta, &b_ElectronSCEta);
   fChain->SetBranchAddress("ElectronSCPhi", &ElectronSCPhi, &b_ElectronSCPhi);
   fChain->SetBranchAddress("ElectronSCPt", &ElectronSCPt, &b_ElectronSCPt);
   fChain->SetBranchAddress("ElectronSCRawEnergy", &ElectronSCRawEnergy, &b_ElectronSCRawEnergy);
   fChain->SetBranchAddress("ElectronSigmaEtaEta", &ElectronSigmaEtaEta, &b_ElectronSigmaEtaEta);
   fChain->SetBranchAddress("ElectronSigmaIEtaIEta", &ElectronSigmaIEtaIEta, &b_ElectronSigmaIEtaIEta);
   fChain->SetBranchAddress("ElectronTrackPt", &ElectronTrackPt, &b_ElectronTrackPt);
   fChain->SetBranchAddress("ElectronTrackValidFractionOfHits", &ElectronTrackValidFractionOfHits, &b_ElectronTrackValidFractionOfHits);
   fChain->SetBranchAddress("ElectronTrackVx", &ElectronTrackVx, &b_ElectronTrackVx);
   fChain->SetBranchAddress("ElectronTrackVy", &ElectronTrackVy, &b_ElectronTrackVy);
   fChain->SetBranchAddress("ElectronTrackVz", &ElectronTrackVz, &b_ElectronTrackVz);
   fChain->SetBranchAddress("ElectronTrkIsoDR03", &ElectronTrkIsoDR03, &b_ElectronTrkIsoDR03);
   fChain->SetBranchAddress("ElectronTrkIsoPAT", &ElectronTrkIsoPAT, &b_ElectronTrkIsoPAT);
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
   fChain->SetBranchAddress("GenMETCalo", &GenMETCalo, &b_GenMETCalo);
   fChain->SetBranchAddress("GenMETPhiCalo", &GenMETPhiCalo, &b_GenMETPhiCalo);
   fChain->SetBranchAddress("GenSumETCalo", &GenSumETCalo, &b_GenSumETCalo);
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
   fChain->SetBranchAddress("MuonBackToBackCompatibility", &MuonBackToBackCompatibility, &b_MuonBackToBackCompatibility);
   fChain->SetBranchAddress("MuonBeamSpotDXY", &MuonBeamSpotDXY, &b_MuonBeamSpotDXY);
   fChain->SetBranchAddress("MuonBeamSpotDXYError", &MuonBeamSpotDXYError, &b_MuonBeamSpotDXYError);
   fChain->SetBranchAddress("MuonCocktailEta", &MuonCocktailEta, &b_MuonCocktailEta);
   fChain->SetBranchAddress("MuonCocktailEtaError", &MuonCocktailEtaError, &b_MuonCocktailEtaError);
   fChain->SetBranchAddress("MuonCocktailGlobalChi2", &MuonCocktailGlobalChi2, &b_MuonCocktailGlobalChi2);
   fChain->SetBranchAddress("MuonCocktailP", &MuonCocktailP, &b_MuonCocktailP);
   fChain->SetBranchAddress("MuonCocktailPhi", &MuonCocktailPhi, &b_MuonCocktailPhi);
   fChain->SetBranchAddress("MuonCocktailPhiError", &MuonCocktailPhiError, &b_MuonCocktailPhiError);
   fChain->SetBranchAddress("MuonCocktailPt", &MuonCocktailPt, &b_MuonCocktailPt);
   fChain->SetBranchAddress("MuonCocktailPtError", &MuonCocktailPtError, &b_MuonCocktailPtError);
   fChain->SetBranchAddress("MuonCocktailQOverPError", &MuonCocktailQOverPError, &b_MuonCocktailQOverPError);
   fChain->SetBranchAddress("MuonCocktailRelIso", &MuonCocktailRelIso, &b_MuonCocktailRelIso);
   fChain->SetBranchAddress("MuonCocktailTrkD0", &MuonCocktailTrkD0, &b_MuonCocktailTrkD0);
   fChain->SetBranchAddress("MuonCocktailTrkD0Error", &MuonCocktailTrkD0Error, &b_MuonCocktailTrkD0Error);
   fChain->SetBranchAddress("MuonCocktailTrkDz", &MuonCocktailTrkDz, &b_MuonCocktailTrkDz);
   fChain->SetBranchAddress("MuonCocktailTrkDzError", &MuonCocktailTrkDzError, &b_MuonCocktailTrkDzError);
   fChain->SetBranchAddress("MuonCocktailTrkValidFractionOfHits", &MuonCocktailTrkValidFractionOfHits, &b_MuonCocktailTrkValidFractionOfHits);
   fChain->SetBranchAddress("MuonCosmicCompatibility", &MuonCosmicCompatibility, &b_MuonCosmicCompatibility);
   fChain->SetBranchAddress("MuonEcalIso", &MuonEcalIso, &b_MuonEcalIso);
   fChain->SetBranchAddress("MuonEnergy", &MuonEnergy, &b_MuonEnergy);
   fChain->SetBranchAddress("MuonEta", &MuonEta, &b_MuonEta);
   fChain->SetBranchAddress("MuonEtaError", &MuonEtaError, &b_MuonEtaError);
   fChain->SetBranchAddress("MuonGlobalChi2", &MuonGlobalChi2, &b_MuonGlobalChi2);
   fChain->SetBranchAddress("MuonHOIso", &MuonHOIso, &b_MuonHOIso);
   fChain->SetBranchAddress("MuonHcalIso", &MuonHcalIso, &b_MuonHcalIso);
   fChain->SetBranchAddress("MuonOverlapCompatibility", &MuonOverlapCompatibility, &b_MuonOverlapCompatibility);
   fChain->SetBranchAddress("MuonP", &MuonP, &b_MuonP);
   fChain->SetBranchAddress("MuonPhi", &MuonPhi, &b_MuonPhi);
   fChain->SetBranchAddress("MuonPhiError", &MuonPhiError, &b_MuonPhiError);
   fChain->SetBranchAddress("MuonPrimaryVertexDXY", &MuonPrimaryVertexDXY, &b_MuonPrimaryVertexDXY);
   fChain->SetBranchAddress("MuonPrimaryVertexDXYError", &MuonPrimaryVertexDXYError, &b_MuonPrimaryVertexDXYError);
   fChain->SetBranchAddress("MuonPt", &MuonPt, &b_MuonPt);
   fChain->SetBranchAddress("MuonPtError", &MuonPtError, &b_MuonPtError);
   fChain->SetBranchAddress("MuonQOverPError", &MuonQOverPError, &b_MuonQOverPError);
   fChain->SetBranchAddress("MuonRelIso", &MuonRelIso, &b_MuonRelIso);
   fChain->SetBranchAddress("MuonTimeCompatibility", &MuonTimeCompatibility, &b_MuonTimeCompatibility);
   fChain->SetBranchAddress("MuonTrackChi2", &MuonTrackChi2, &b_MuonTrackChi2);
   fChain->SetBranchAddress("MuonTrackerIsoSumPT", &MuonTrackerIsoSumPT, &b_MuonTrackerIsoSumPT);
   fChain->SetBranchAddress("MuonTrkD0", &MuonTrkD0, &b_MuonTrkD0);
   fChain->SetBranchAddress("MuonTrkD0Error", &MuonTrkD0Error, &b_MuonTrkD0Error);
   fChain->SetBranchAddress("MuonTrkDz", &MuonTrkDz, &b_MuonTrkDz);
   fChain->SetBranchAddress("MuonTrkDzError", &MuonTrkDzError, &b_MuonTrkDzError);
   fChain->SetBranchAddress("MuonTrkEta", &MuonTrkEta, &b_MuonTrkEta);
   fChain->SetBranchAddress("MuonTrkEtaError", &MuonTrkEtaError, &b_MuonTrkEtaError);
   fChain->SetBranchAddress("MuonTrkIso", &MuonTrkIso, &b_MuonTrkIso);
   fChain->SetBranchAddress("MuonTrkPhi", &MuonTrkPhi, &b_MuonTrkPhi);
   fChain->SetBranchAddress("MuonTrkPhiError", &MuonTrkPhiError, &b_MuonTrkPhiError);
   fChain->SetBranchAddress("MuonTrkPt", &MuonTrkPt, &b_MuonTrkPt);
   fChain->SetBranchAddress("MuonTrkPtError", &MuonTrkPtError, &b_MuonTrkPtError);
   fChain->SetBranchAddress("MuonTrkValidFractionOfHits", &MuonTrkValidFractionOfHits, &b_MuonTrkValidFractionOfHits);
   fChain->SetBranchAddress("MuonTrkVx", &MuonTrkVx, &b_MuonTrkVx);
   fChain->SetBranchAddress("MuonTrkVy", &MuonTrkVy, &b_MuonTrkVy);
   fChain->SetBranchAddress("MuonTrkVz", &MuonTrkVz, &b_MuonTrkVz);
   fChain->SetBranchAddress("MuonVtxDistXY", &MuonVtxDistXY, &b_MuonVtxDistXY);
   fChain->SetBranchAddress("MuonVtxDistZ", &MuonVtxDistZ, &b_MuonVtxDistZ);
   fChain->SetBranchAddress("PFCandEnergyLeptLink", &PFCandEnergyLeptLink, &b_PFCandEnergyLeptLink);
   fChain->SetBranchAddress("PFCandEtaLeptLink", &PFCandEtaLeptLink, &b_PFCandEtaLeptLink);
   fChain->SetBranchAddress("PFCandPhiLeptLink", &PFCandPhiLeptLink, &b_PFCandPhiLeptLink);
   fChain->SetBranchAddress("PFCandPtLeptLink", &PFCandPtLeptLink, &b_PFCandPtLeptLink);
   fChain->SetBranchAddress("PFMETCharged", &PFMETCharged, &b_PFMETCharged);
   fChain->SetBranchAddress("PFMETPhiCharged", &PFMETPhiCharged, &b_PFMETPhiCharged);
   fChain->SetBranchAddress("PFSumETCharged", &PFSumETCharged, &b_PFSumETCharged);
   fChain->SetBranchAddress("PFJetBestVertexTrackAssociationFactor", &PFJetBestVertexTrackAssociationFactor, &b_PFJetBestVertexTrackAssociationFactor);
   fChain->SetBranchAddress("PFJetChargedEmEnergyFraction", &PFJetChargedEmEnergyFraction, &b_PFJetChargedEmEnergyFraction);
   fChain->SetBranchAddress("PFJetChargedHadronEnergyFraction", &PFJetChargedHadronEnergyFraction, &b_PFJetChargedHadronEnergyFraction);
   fChain->SetBranchAddress("PFJetChargedMuEnergyFraction", &PFJetChargedMuEnergyFraction, &b_PFJetChargedMuEnergyFraction);
   fChain->SetBranchAddress("PFJetClosestVertexWeighted3DSeparation", &PFJetClosestVertexWeighted3DSeparation, &b_PFJetClosestVertexWeighted3DSeparation);
   fChain->SetBranchAddress("PFJetClosestVertexWeightedXYSeparation", &PFJetClosestVertexWeightedXYSeparation, &b_PFJetClosestVertexWeightedXYSeparation);
   fChain->SetBranchAddress("PFJetClosestVertexWeightedZSeparation", &PFJetClosestVertexWeightedZSeparation, &b_PFJetClosestVertexWeightedZSeparation);
   fChain->SetBranchAddress("PFJetElectronEnergyFraction", &PFJetElectronEnergyFraction, &b_PFJetElectronEnergyFraction);
   fChain->SetBranchAddress("PFJetEnergy", &PFJetEnergy, &b_PFJetEnergy);
   fChain->SetBranchAddress("PFJetEnergyRaw", &PFJetEnergyRaw, &b_PFJetEnergyRaw);
   fChain->SetBranchAddress("PFJetEta", &PFJetEta, &b_PFJetEta);
   fChain->SetBranchAddress("PFJetHFEMEnergyFraction", &PFJetHFEMEnergyFraction, &b_PFJetHFEMEnergyFraction);
   fChain->SetBranchAddress("PFJetHFHadronEnergyFraction", &PFJetHFHadronEnergyFraction, &b_PFJetHFHadronEnergyFraction);
   fChain->SetBranchAddress("PFJetJECUnc", &PFJetJECUnc, &b_PFJetJECUnc);
   fChain->SetBranchAddress("PFJetJetBProbabilityBTag", &PFJetJetBProbabilityBTag, &b_PFJetJetBProbabilityBTag);
   fChain->SetBranchAddress("PFJetJetProbabilityBTag", &PFJetJetProbabilityBTag, &b_PFJetJetProbabilityBTag);
   fChain->SetBranchAddress("PFJetL1FastJetJEC", &PFJetL1FastJetJEC, &b_PFJetL1FastJetJEC);
   fChain->SetBranchAddress("PFJetL1OffsetJEC", &PFJetL1OffsetJEC, &b_PFJetL1OffsetJEC);
   fChain->SetBranchAddress("PFJetL2L3ResJEC", &PFJetL2L3ResJEC, &b_PFJetL2L3ResJEC);
   fChain->SetBranchAddress("PFJetL2RelJEC", &PFJetL2RelJEC, &b_PFJetL2RelJEC);
   fChain->SetBranchAddress("PFJetL3AbsJEC", &PFJetL3AbsJEC, &b_PFJetL3AbsJEC);
   fChain->SetBranchAddress("PFJetMuonEnergyFraction", &PFJetMuonEnergyFraction, &b_PFJetMuonEnergyFraction);
   fChain->SetBranchAddress("PFJetNeutralEmEnergyFraction", &PFJetNeutralEmEnergyFraction, &b_PFJetNeutralEmEnergyFraction);
   fChain->SetBranchAddress("PFJetNeutralHadronEnergyFraction", &PFJetNeutralHadronEnergyFraction, &b_PFJetNeutralHadronEnergyFraction);
   fChain->SetBranchAddress("PFJetPhi", &PFJetPhi, &b_PFJetPhi);
   fChain->SetBranchAddress("PFJetPhotonEnergyFraction", &PFJetPhotonEnergyFraction, &b_PFJetPhotonEnergyFraction);
   fChain->SetBranchAddress("PFJetPt", &PFJetPt, &b_PFJetPt);
   fChain->SetBranchAddress("PFJetPtRaw", &PFJetPtRaw, &b_PFJetPtRaw);
   fChain->SetBranchAddress("PFJetSimpleSecondaryVertexHighEffBTag", &PFJetSimpleSecondaryVertexHighEffBTag, &b_PFJetSimpleSecondaryVertexHighEffBTag);
   fChain->SetBranchAddress("PFJetSimpleSecondaryVertexHighPurBTag", &PFJetSimpleSecondaryVertexHighPurBTag, &b_PFJetSimpleSecondaryVertexHighPurBTag);
   fChain->SetBranchAddress("PFJetTrackCountingHighEffBTag", &PFJetTrackCountingHighEffBTag, &b_PFJetTrackCountingHighEffBTag);
   fChain->SetBranchAddress("PFJetTrackCountingHighPurBTag", &PFJetTrackCountingHighPurBTag, &b_PFJetTrackCountingHighPurBTag);
   fChain->SetBranchAddress("PFMET", &PFMET, &b_PFMET);
   fChain->SetBranchAddress("PFMETPhi", &PFMETPhi, &b_PFMETPhi);
   fChain->SetBranchAddress("PFMETSig", &PFMETSig, &b_PFMETSig);
   fChain->SetBranchAddress("PFMETSigMatrixDXX", &PFMETSigMatrixDXX, &b_PFMETSigMatrixDXX);
   fChain->SetBranchAddress("PFMETSigMatrixDXY", &PFMETSigMatrixDXY, &b_PFMETSigMatrixDXY);
   fChain->SetBranchAddress("PFMETSigMatrixDYX", &PFMETSigMatrixDYX, &b_PFMETSigMatrixDYX);
   fChain->SetBranchAddress("PFMETSigMatrixDYY", &PFMETSigMatrixDYY, &b_PFMETSigMatrixDYY);
   fChain->SetBranchAddress("PFSumET", &PFSumET, &b_PFSumET);
   fChain->SetBranchAddress("PFMETPhiType1Cor", &PFMETPhiType1Cor, &b_PFMETPhiType1Cor);
   fChain->SetBranchAddress("PFMETType1Cor", &PFMETType1Cor, &b_PFMETType1Cor);
   fChain->SetBranchAddress("PFSumETType1Cor", &PFSumETType1Cor, &b_PFSumETType1Cor);
   fChain->SetBranchAddress("PhotonAlpha", &PhotonAlpha, &b_PhotonAlpha);
   fChain->SetBranchAddress("PhotonChi2ConvPhot", &PhotonChi2ConvPhot, &b_PhotonChi2ConvPhot);
   fChain->SetBranchAddress("PhotonDPhiTracksAtVtxConvPhot", &PhotonDPhiTracksAtVtxConvPhot, &b_PhotonDPhiTracksAtVtxConvPhot);
   fChain->SetBranchAddress("PhotonDistOfMinApproachConvPhot", &PhotonDistOfMinApproachConvPhot, &b_PhotonDistOfMinApproachConvPhot);
   fChain->SetBranchAddress("PhotonE2OverE9", &PhotonE2OverE9, &b_PhotonE2OverE9);
   fChain->SetBranchAddress("PhotonE3x3", &PhotonE3x3, &b_PhotonE3x3);
   fChain->SetBranchAddress("PhotonE4SwissCross", &PhotonE4SwissCross, &b_PhotonE4SwissCross);
   fChain->SetBranchAddress("PhotonE5x5", &PhotonE5x5, &b_PhotonE5x5);
   fChain->SetBranchAddress("PhotonEOverPConvPhot", &PhotonEOverPConvPhot, &b_PhotonEOverPConvPhot);
   fChain->SetBranchAddress("PhotonEcalIsoDR03", &PhotonEcalIsoDR03, &b_PhotonEcalIsoDR03);
   fChain->SetBranchAddress("PhotonEcalIsoDR04", &PhotonEcalIsoDR04, &b_PhotonEcalIsoDR04);
   fChain->SetBranchAddress("PhotonEnergy", &PhotonEnergy, &b_PhotonEnergy);
   fChain->SetBranchAddress("PhotonEta", &PhotonEta, &b_PhotonEta);
   fChain->SetBranchAddress("PhotonHcalIsoDR03", &PhotonHcalIsoDR03, &b_PhotonHcalIsoDR03);
   fChain->SetBranchAddress("PhotonHcalIsoDR03FullCone", &PhotonHcalIsoDR03FullCone, &b_PhotonHcalIsoDR03FullCone);
   fChain->SetBranchAddress("PhotonHcalIsoDR04", &PhotonHcalIsoDR04, &b_PhotonHcalIsoDR04);
   fChain->SetBranchAddress("PhotonHcalIsoDR04FullCone", &PhotonHcalIsoDR04FullCone, &b_PhotonHcalIsoDR04FullCone);
   fChain->SetBranchAddress("PhotonHoE", &PhotonHoE, &b_PhotonHoE);
   fChain->SetBranchAddress("PhotonNDofConvPhot", &PhotonNDofConvPhot, &b_PhotonNDofConvPhot);
   fChain->SetBranchAddress("PhotonPairCotThetaSeparationConvPhot", &PhotonPairCotThetaSeparationConvPhot, &b_PhotonPairCotThetaSeparationConvPhot);
   fChain->SetBranchAddress("PhotonPairInvariantMassConvPhot", &PhotonPairInvariantMassConvPhot, &b_PhotonPairInvariantMassConvPhot);
   fChain->SetBranchAddress("PhotonPairMomentumxConvPhot", &PhotonPairMomentumxConvPhot, &b_PhotonPairMomentumxConvPhot);
   fChain->SetBranchAddress("PhotonPairMomentumyConvPhot", &PhotonPairMomentumyConvPhot, &b_PhotonPairMomentumyConvPhot);
   fChain->SetBranchAddress("PhotonPairMomentumzConvPhot", &PhotonPairMomentumzConvPhot, &b_PhotonPairMomentumzConvPhot);
   fChain->SetBranchAddress("PhotonPhi", &PhotonPhi, &b_PhotonPhi);
   fChain->SetBranchAddress("PhotonPt", &PhotonPt, &b_PhotonPt);
   fChain->SetBranchAddress("PhotonSCenergy", &PhotonSCenergy, &b_PhotonSCenergy);
   fChain->SetBranchAddress("PhotonSCeta", &PhotonSCeta, &b_PhotonSCeta);
   fChain->SetBranchAddress("PhotonSCphi", &PhotonSCphi, &b_PhotonSCphi);
   fChain->SetBranchAddress("PhotonSCseedEnergy", &PhotonSCseedEnergy, &b_PhotonSCseedEnergy);
   fChain->SetBranchAddress("PhotonSEtaEta", &PhotonSEtaEta, &b_PhotonSEtaEta);
   fChain->SetBranchAddress("PhotonSEtaPhi", &PhotonSEtaPhi, &b_PhotonSEtaPhi);
   fChain->SetBranchAddress("PhotonSMajMaj", &PhotonSMajMaj, &b_PhotonSMajMaj);
   fChain->SetBranchAddress("PhotonSMinMin", &PhotonSMinMin, &b_PhotonSMinMin);
   fChain->SetBranchAddress("PhotonSPhiPhi", &PhotonSPhiPhi, &b_PhotonSPhiPhi);
   fChain->SetBranchAddress("PhotonSigmaIEtaIEta", &PhotonSigmaIEtaIEta, &b_PhotonSigmaIEtaIEta);
   fChain->SetBranchAddress("PhotonTimeSeed", &PhotonTimeSeed, &b_PhotonTimeSeed);
   fChain->SetBranchAddress("PhotonTrkIsoHollowDR03", &PhotonTrkIsoHollowDR03, &b_PhotonTrkIsoHollowDR03);
   fChain->SetBranchAddress("PhotonTrkIsoHollowDR04", &PhotonTrkIsoHollowDR04, &b_PhotonTrkIsoHollowDR04);
   fChain->SetBranchAddress("PhotonTrkIsoSolidDR03", &PhotonTrkIsoSolidDR03, &b_PhotonTrkIsoSolidDR03);
   fChain->SetBranchAddress("PhotonTrkIsoSolidDR04", &PhotonTrkIsoSolidDR04, &b_PhotonTrkIsoSolidDR04);
   fChain->SetBranchAddress("PhotonXVtxConvPhot", &PhotonXVtxConvPhot, &b_PhotonXVtxConvPhot);
   fChain->SetBranchAddress("PhotonYVtxConvPhot", &PhotonYVtxConvPhot, &b_PhotonYVtxConvPhot);
   fChain->SetBranchAddress("PhotonZVtxConvPhot", &PhotonZVtxConvPhot, &b_PhotonZVtxConvPhot);
   fChain->SetBranchAddress("TCMET", &TCMET, &b_TCMET);
   fChain->SetBranchAddress("TCMETPhi", &TCMETPhi, &b_TCMETPhi);
   fChain->SetBranchAddress("TCSumET", &TCSumET, &b_TCSumET);
   fChain->SetBranchAddress("TauEmFraction", &TauEmFraction, &b_TauEmFraction);
   fChain->SetBranchAddress("TauEt", &TauEt, &b_TauEt);
   fChain->SetBranchAddress("TauEta", &TauEta, &b_TauEta);
   fChain->SetBranchAddress("TauEtaLeadCharged", &TauEtaLeadCharged, &b_TauEtaLeadCharged);
   fChain->SetBranchAddress("TauHcal3x3OverPLead", &TauHcal3x3OverPLead, &b_TauHcal3x3OverPLead);
   fChain->SetBranchAddress("TauHcalMaxOverPLead", &TauHcalMaxOverPLead, &b_TauHcalMaxOverPLead);
   fChain->SetBranchAddress("TauHcalTotOverPLead", &TauHcalTotOverPLead, &b_TauHcalTotOverPLead);
   fChain->SetBranchAddress("TauIsolationPFChargedHadrCandsPtSum", &TauIsolationPFChargedHadrCandsPtSum, &b_TauIsolationPFChargedHadrCandsPtSum);
   fChain->SetBranchAddress("TauIsolationPFGammaCandsEtSum", &TauIsolationPFGammaCandsEtSum, &b_TauIsolationPFGammaCandsEtSum);
   fChain->SetBranchAddress("TauLeadPFChargedHadrCandsignedSipt", &TauLeadPFChargedHadrCandsignedSipt, &b_TauLeadPFChargedHadrCandsignedSipt);
   fChain->SetBranchAddress("TauPhi", &TauPhi, &b_TauPhi);
   fChain->SetBranchAddress("TauPhiLeadCharged", &TauPhiLeadCharged, &b_TauPhiLeadCharged);
   fChain->SetBranchAddress("TauPt", &TauPt, &b_TauPt);
   fChain->SetBranchAddress("TauPtLeadCharged", &TauPtLeadCharged, &b_TauPtLeadCharged);
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
   fChain->SetBranchAddress("ElectronMissingHits", &ElectronMissingHits, &b_ElectronMissingHits);
   fChain->SetBranchAddress("ElectronNumberOfBrems", &ElectronNumberOfBrems, &b_ElectronNumberOfBrems);
   fChain->SetBranchAddress("ElectronOverlaps", &ElectronOverlaps, &b_ElectronOverlaps);
   fChain->SetBranchAddress("ElectronPassIDPAT", &ElectronPassIDPAT, &b_ElectronPassIDPAT);
   fChain->SetBranchAddress("ElectronPassIsoPAT", &ElectronPassIsoPAT, &b_ElectronPassIsoPAT);
   fChain->SetBranchAddress("ElectronVtxIndex", &ElectronVtxIndex, &b_ElectronVtxIndex);
   fChain->SetBranchAddress("PileUpInteractions", &PileUpInteractions, &b_PileUpInteractions);
   fChain->SetBranchAddress("PileUpOriginBX", &PileUpOriginBX, &b_PileUpOriginBX);
   fChain->SetBranchAddress("GenParticleMotherIndex", &GenParticleMotherIndex, &b_GenParticleMotherIndex);
   fChain->SetBranchAddress("GenParticleNumDaught", &GenParticleNumDaught, &b_GenParticleNumDaught);
   fChain->SetBranchAddress("GenParticlePdgId", &GenParticlePdgId, &b_GenParticlePdgId);
   fChain->SetBranchAddress("GenParticleStatus", &GenParticleStatus, &b_GenParticleStatus);
   fChain->SetBranchAddress("MuonCharge", &MuonCharge, &b_MuonCharge);
   fChain->SetBranchAddress("MuonCocktailCharge", &MuonCocktailCharge, &b_MuonCocktailCharge);
   fChain->SetBranchAddress("MuonCocktailPassIso", &MuonCocktailPassIso, &b_MuonCocktailPassIso);
   fChain->SetBranchAddress("MuonCocktailRefitID", &MuonCocktailRefitID, &b_MuonCocktailRefitID);
   fChain->SetBranchAddress("MuonCocktailTrkHits", &MuonCocktailTrkHits, &b_MuonCocktailTrkHits);
   fChain->SetBranchAddress("MuonGlobalTrkValidHits", &MuonGlobalTrkValidHits, &b_MuonGlobalTrkValidHits);
   fChain->SetBranchAddress("MuonIsGlobal", &MuonIsGlobal, &b_MuonIsGlobal);
   fChain->SetBranchAddress("MuonIsTracker", &MuonIsTracker, &b_MuonIsTracker);
   fChain->SetBranchAddress("MuonPassID", &MuonPassID, &b_MuonPassID);
   fChain->SetBranchAddress("MuonPassIso", &MuonPassIso, &b_MuonPassIso);
   fChain->SetBranchAddress("MuonPixelHitCount", &MuonPixelHitCount, &b_MuonPixelHitCount);
   fChain->SetBranchAddress("MuonSegmentMatches", &MuonSegmentMatches, &b_MuonSegmentMatches);
   fChain->SetBranchAddress("MuonStationMatches", &MuonStationMatches, &b_MuonStationMatches);
   fChain->SetBranchAddress("MuonTrkHits", &MuonTrkHits, &b_MuonTrkHits);
   fChain->SetBranchAddress("MuonTrkHitsTrackerOnly", &MuonTrkHitsTrackerOnly, &b_MuonTrkHitsTrackerOnly);
   fChain->SetBranchAddress("MuonTrkPixelHitCount", &MuonTrkPixelHitCount, &b_MuonTrkPixelHitCount);
   fChain->SetBranchAddress("MuonVtxIndex", &MuonVtxIndex, &b_MuonVtxIndex);
   fChain->SetBranchAddress("PFCandChargeLeptLink", &PFCandChargeLeptLink, &b_PFCandChargeLeptLink);
   fChain->SetBranchAddress("PFJetBestVertexTrackAssociationIndex", &PFJetBestVertexTrackAssociationIndex, &b_PFJetBestVertexTrackAssociationIndex);
   fChain->SetBranchAddress("PFJetChargedHadronMultiplicity", &PFJetChargedHadronMultiplicity, &b_PFJetChargedHadronMultiplicity);
   fChain->SetBranchAddress("PFJetChargedMultiplicity", &PFJetChargedMultiplicity, &b_PFJetChargedMultiplicity);
   fChain->SetBranchAddress("PFJetClosestVertex3DIndex", &PFJetClosestVertex3DIndex, &b_PFJetClosestVertex3DIndex);
   fChain->SetBranchAddress("PFJetClosestVertexXYIndex", &PFJetClosestVertexXYIndex, &b_PFJetClosestVertexXYIndex);
   fChain->SetBranchAddress("PFJetClosestVertexZIndex", &PFJetClosestVertexZIndex, &b_PFJetClosestVertexZIndex);
   fChain->SetBranchAddress("PFJetElectronMultiplicity", &PFJetElectronMultiplicity, &b_PFJetElectronMultiplicity);
   fChain->SetBranchAddress("PFJetHFEMMultiplicity", &PFJetHFEMMultiplicity, &b_PFJetHFEMMultiplicity);
   fChain->SetBranchAddress("PFJetHFHadronMultiplicity", &PFJetHFHadronMultiplicity, &b_PFJetHFHadronMultiplicity);
   fChain->SetBranchAddress("PFJetMuonMultiplicity", &PFJetMuonMultiplicity, &b_PFJetMuonMultiplicity);
   fChain->SetBranchAddress("PFJetNConstituents", &PFJetNConstituents, &b_PFJetNConstituents);
   fChain->SetBranchAddress("PFJetNeutralHadronMultiplicity", &PFJetNeutralHadronMultiplicity, &b_PFJetNeutralHadronMultiplicity);
   fChain->SetBranchAddress("PFJetNeutralMultiplicity", &PFJetNeutralMultiplicity, &b_PFJetNeutralMultiplicity);
   fChain->SetBranchAddress("PFJetPartonFlavour", &PFJetPartonFlavour, &b_PFJetPartonFlavour);
   fChain->SetBranchAddress("PFJetPassLooseID", &PFJetPassLooseID, &b_PFJetPassLooseID);
   fChain->SetBranchAddress("PFJetPassTightID", &PFJetPassTightID, &b_PFJetPassTightID);
   fChain->SetBranchAddress("PFJetPhotonMultiplicity", &PFJetPhotonMultiplicity, &b_PFJetPhotonMultiplicity);
   fChain->SetBranchAddress("PhotonNTracksConvPhot", &PhotonNTracksConvPhot, &b_PhotonNTracksConvPhot);
   fChain->SetBranchAddress("TauAgainstElectronDiscr", &TauAgainstElectronDiscr, &b_TauAgainstElectronDiscr);
   fChain->SetBranchAddress("TauAgainstMuonDiscr", &TauAgainstMuonDiscr, &b_TauAgainstMuonDiscr);
   fChain->SetBranchAddress("TauByIsolationDiscr", &TauByIsolationDiscr, &b_TauByIsolationDiscr);
   fChain->SetBranchAddress("TauByIsolationUsingLeadingPionDiscr", &TauByIsolationUsingLeadingPionDiscr, &b_TauByIsolationUsingLeadingPionDiscr);
   fChain->SetBranchAddress("TauCharge", &TauCharge, &b_TauCharge);
   fChain->SetBranchAddress("TauDecayMode", &TauDecayMode, &b_TauDecayMode);
   fChain->SetBranchAddress("TauEcalIsolationDiscr", &TauEcalIsolationDiscr, &b_TauEcalIsolationDiscr);
   fChain->SetBranchAddress("TauEcalIsolationUsingLeadingPionDiscr", &TauEcalIsolationUsingLeadingPionDiscr, &b_TauEcalIsolationUsingLeadingPionDiscr);
   fChain->SetBranchAddress("TauIsCaloTau", &TauIsCaloTau, &b_TauIsCaloTau);
   fChain->SetBranchAddress("TauIsPFTau", &TauIsPFTau, &b_TauIsPFTau);
   fChain->SetBranchAddress("TauLeadingPionPtCutDiscr", &TauLeadingPionPtCutDiscr, &b_TauLeadingPionPtCutDiscr);
   fChain->SetBranchAddress("TauLeadingTrackFindingDiscr", &TauLeadingTrackFindingDiscr, &b_TauLeadingTrackFindingDiscr);
   fChain->SetBranchAddress("TauLeadingTrackPtCutDiscr", &TauLeadingTrackPtCutDiscr, &b_TauLeadingTrackPtCutDiscr);
   fChain->SetBranchAddress("TauTrackIsolationDiscr", &TauTrackIsolationDiscr, &b_TauTrackIsolationDiscr);
   fChain->SetBranchAddress("TauTrackIsolationUsingLeadingPionDiscr", &TauTrackIsolationUsingLeadingPionDiscr, &b_TauTrackIsolationUsingLeadingPionDiscr);
   fChain->SetBranchAddress("HLTInsideDatasetTriggerPrescales", &HLTInsideDatasetTriggerPrescales, &b_HLTInsideDatasetTriggerPrescales);
   fChain->SetBranchAddress("HLTOutsideDatasetTriggerPrescales", &HLTOutsideDatasetTriggerPrescales, &b_HLTOutsideDatasetTriggerPrescales);
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
   //filetracermarkstatus
}

Bool_t placeholder::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void placeholder::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t placeholder::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
float WHY=entry;
WHY=0;
   return 1;
}
#endif // #ifdef placeholder_cxx
