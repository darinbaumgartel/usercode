#define NTupleAnalyzer_W0Jets_Pt0to100_cxx
#include "NTupleAnalyzer_W0Jets_Pt0to100.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TVector2.h>
#include "TVector3.h"
#include "TLorentzVector.h"
#include <vector>
#include <cmath>
#include <TMath.h>
#include "TRandom2.h"

float TMass(float Pt1, float Pt2, float DPhi12)
{
	return sqrt( 2*Pt2*Pt1*(1-cos(DPhi12)) );
}

// Recoil Function Definitions
float F_U1Prime(float P)
{
float newU1 =+(0.794254)/(1.09126)*(1.29887)+(-0.883448)/(-0.91393)*(-0.905936)*(P);

float newsU1 =+(5.83895)/(4.6548)*(4.41959)+(0.0668703)/(0.0797865)*(0.0928476)*(P)+(0.000447746)/(0.000908574)*(0.00049701)*(pow(P,2.0));


return gRandom->Gaus(newU1,newsU1);
}


float F_U2Prime(float P)
{
float newU2 =+(0.00486499)/(-0.00367621)*(-0.0225686)+(-0.00211337)/(0.00064751)*(0.000600862)*(P);

float newsU2 =+(5.7388)/(4.67223)*(4.41606)+(0.0609486)/(0.0654114)*(0.080841)*(P)+(-2.46186e-05)/(-0.000202861)*(-0.000317848)*(pow(P,2.0));

return gRandom->Gaus(newU2,newsU2);
}


bool DoRecoilCorrections = true;

void NTupleAnalyzer_W0Jets_Pt0to100::Loop()
{

	//===================================================================================================
	//      MAKE TREE FOR PLACEHOLDER SIGNAL/BG TYPE AND DECLARE VARIABLES
	//===================================================================================================

	// Update output file
	TFile * file1 = new TFile("W0Jets_Pt0to100.root","RECREATE");
	// create tree for the signal or background type
	TTree *tree=new TTree("PhysicalVariables","PhysicalVariables");

	//*****************************************************************
	//         MUON AND CALOJET/CALOMET VARIABLES BELOW
	//*****************************************************************

	// Precut variables
	float precut_HLT=0.0;
	tree->Branch("precut_HLT",&precut_HLT,"precut_HLT");

	float precut_1muon=0.0;
	tree->Branch("precut_1muon",&precut_1muon,"precut_1muon");
	float precut_2muon=0.0;
	tree->Branch("precut_2muon",&precut_2muon,"precut_2muon");
	float precut_1jet=0.0;
	tree->Branch("precut_1jet",&precut_1jet,"precut_1jet");
	float precut_2jet=0.0;
	tree->Branch("precut_2jet",&precut_2jet,"precut_2jet");

	float precut_2muonexact_chargeproduct = 0.0;
	tree->Branch("precut_2muonexact_chargeproduct",&precut_2muonexact_chargeproduct,"precut_2muonexact_chargeproduct");

	float precut_muonDeltaR=0.0;
	tree->Branch("precut_muonDeltaR",&precut_muonDeltaR,"precut_muonDeltaR");

	float MuonCount = 0.0;
	tree->Branch("MuonCount",&MuonCount,"MuonCount");

	float EleCount = 0.0;
	tree->Branch("EleCount",&EleCount,"EleCount");

	float JetCount = 0.0;
	tree->Branch("JetCount",&JetCount,"JetCount");

	float D0_muon1 = 0.0;
	tree->Branch("D0_muon1",&D0_muon1,"D0_muon1");

	float NHits_muon1 = 0.0;
	tree->Branch("NHits_muon1",&NHits_muon1,"NHits_muon1");

	float D0_muon2 = 0.0;
	tree->Branch("D0_muon2",&D0_muon2,"D0_muon2");

	float NHits_muon2 = 0.0;
	tree->Branch("NHits_muon2",&NHits_muon2,"NHits_muon2");

	float D0_muon3 = 0.0;
	tree->Branch("D0_muon3",&D0_muon3,"D0_muon3");

	float NHits_muon3 = 0.0;
	tree->Branch("NHits_muon3",&NHits_muon3,"NHits_muon3");

	float CaloBTagCountPandT= 0.0;
	tree->Branch("CaloBTagCountPandT",&CaloBTagCountPandT,"CaloBTagCountPandT");

	float CaloBTagCountPorT= 0.0;
	tree->Branch("CaloBTagCountPorT",&CaloBTagCountPorT,"CaloBTagCountPorT");

	// Leptoquark Mass
	float LQMass = 0.0;
	tree->Branch("LQMass",&LQMass,"LQMass");

	// Angular Variables
	float Phi_muon1=0.0;
	tree->Branch("Phi_muon1",&Phi_muon1,"Phi_muon1");
	float Phi_muon2=0.0;
	tree->Branch("Phi_muon2",&Phi_muon2,"Phi_muon2");
	float Phi_muon3=0.0;
	tree->Branch("Phi_muon3",&Phi_muon3,"Phi_muon3");

	float Eta_muon1=0.0;
	tree->Branch("Eta_muon1",&Eta_muon1,"Eta_muon1");
	float Eta_muon2=0.0;
	tree->Branch("Eta_muon2",&Eta_muon2,"Eta_muon2");
	float Eta_muon3=0.0;
	tree->Branch("Eta_muon3",&Eta_muon3,"Eta_muon3");

	float Phi_jet1=0.0;
	tree->Branch("Phi_jet1",&Phi_jet1,"Phi_jet1");
	float Phi_jet2=0.0;
	tree->Branch("Phi_jet2",&Phi_jet2,"Phi_jet2");

	float Eta_jet1=0.0;
	tree->Branch("Eta_jet1",&Eta_jet1,"Eta_jet1");
	float Eta_jet2=0.0;
	tree->Branch("Eta_jet2",&Eta_jet2,"Eta_jet2");

	//MET
	float MET_calo=0.0;
	tree->Branch("MET_calo",&MET_calo,"MET_calo");

	// PT Variables
	float Pt_muon1=0.0;
	tree->Branch("Pt_muon1",&Pt_muon1,"Pt_muon1");

	float Charge_muon1=0.0;
	tree->Branch("Charge_muon1",&Charge_muon1,"Charge_muon1");
	float Charge_muon2=0.0;
	tree->Branch("Charge_muon2",&Charge_muon2,"Charge_muon2");
	float Charge_muon3=0.0;
	tree->Branch("Charge_muon3",&Charge_muon3,"Charge_muon3");

	float RelIso_muon1=0.0;
	tree->Branch("RelIso_muon1",&RelIso_muon1,"RelIso_muon1");
	float RelIso_muon2;
	tree->Branch("RelIso_muon2",&RelIso_muon2,"RelIso_muon2");
	float RelIso_muon3=0.0;
	tree->Branch("RelIso_muon3",&RelIso_muon3,"RelIso_muon3");

	float ChiSq_muon1=0.0;
	tree->Branch("ChiSq_muon1",&ChiSq_muon1,"ChiSq_muon1");
	float TrkDZ_muon1=0.0;
	tree->Branch("TrkDZ_muon1",&TrkDZ_muon1,"TrkDZ_muon1");

	float ChiSq_muon2=0.0;
	tree->Branch("ChiSq_muon2",&ChiSq_muon2,"ChiSq_muon2");
	float TrkDZ_muon2=0.0;
	tree->Branch("TrkDZ_muon2",&TrkDZ_muon2,"TrkDZ_muon2");

	float ChiSq_muon3=0.0;
	tree->Branch("ChiSq_muon3",&ChiSq_muon3,"ChiSq_muon3");
	float TrkDZ_muon3=0.0;
	tree->Branch("TrkDZ_muon3",&TrkDZ_muon3,"TrkDZ_muon3");

	float Pt_muon2=0.0;
	tree->Branch("Pt_muon2",&Pt_muon2,"Pt_muon2");
	float Pt_muon3=0.0;
	tree->Branch("Pt_muon3",&Pt_muon3,"Pt_muon3");
	float Pt_jet1=0.0;
	tree->Branch("Pt_jet1",&Pt_jet1,"Pt_jet1");
	float Pt_jet2=0.0;
	tree->Branch("Pt_jet2",&Pt_jet2,"Pt_jet2");

	float Pt_ele1=0.0;
	tree->Branch("Pt_ele1",&Pt_ele1,"Pt_ele1");

	//Delta Phi Variables
	float deltaPhi_muon1caloMET=0.0;
	tree->Branch("deltaPhi_muon1caloMET",&deltaPhi_muon1caloMET,"deltaPhi_muon1caloMET");
	float deltaPhi_caloMETmuon2=0.0;
	tree->Branch("deltaPhi_caloMETmuon2",&deltaPhi_caloMETmuon2,"deltaPhi_caloMETmuon2");
	float deltaPhi_jet1caloMET=0.0;
	tree->Branch("deltaPhi_jet1caloMET",&deltaPhi_jet1caloMET,"deltaPhi_jet1caloMET");
	float deltaPhi_jet2caloMET=0.0;
	tree->Branch("deltaPhi_jet2caloMET",&deltaPhi_jet2caloMET,"deltaPhi_jet2caloMET");
	float deltaPhi_muon1jet1=0.0;
	tree->Branch("deltaPhi_muon1jet1",&deltaPhi_muon1jet1,"deltaPhi_muon1jet1");
	float deltaPhi_muon1jet2=0.0;
	tree->Branch("deltaPhi_muon1jet2",&deltaPhi_muon1jet2,"deltaPhi_muon1jet2");
	float deltaPhi_muon2jet1=0.0;
	tree->Branch("deltaPhi_muon2jet1",&deltaPhi_muon2jet1,"deltaPhi_muon2jet1");
	float deltaPhi_muon2jet2=0.0;
	tree->Branch("deltaPhi_muon2jet2",&deltaPhi_muon2jet2,"deltaPhi_muon2jet2");
	float deltaPhi_jet1jet2=0.0;
	tree->Branch("deltaPhi_jet1jet2",&deltaPhi_jet1jet2,"deltaPhi_jet1jet2");

	float deltaPhi_muon1muon2=0.0;
	tree->Branch("deltaPhi_muon1muon2",&deltaPhi_muon1muon2,"deltaPhi_muon1muon2");

	// Delta R Variables
	float deltaR_muon1muon2=0.0;
	tree->Branch("deltaR_muon1muon2",&deltaR_muon1muon2,"deltaR_muon1muon2");
	float deltaR_jet1jet2=0.0;
	tree->Branch("deltaR_jet1jet2",&deltaR_jet1jet2,"deltaR_jet1jet2");

	// Invariant and transverse masses
	float M_muon1jet1=0.0;
	tree->Branch("M_muon1jet1",&M_muon1jet1,"M_muon1jet1");
	float M_muon1muon2=0.0;
	tree->Branch("M_muon1muon2",&M_muon1muon2,"M_muon1muon2");
	float M_muon1muon3=0.0;
	tree->Branch("M_muon1muon3",&M_muon1muon3,"M_muon1muon3");
	float M_muon2muon3=0.0;
	tree->Branch("M_muon2muon3",&M_muon2muon3,"M_muon2muon3");
	float M_muon1jet2=0.0;
	tree->Branch("M_muon1jet2",&M_muon1jet2,"M_muon1jet2");
	float M_muon2jet1=0.0;
	tree->Branch("M_muon2jet1",&M_muon2jet1,"M_muon2jet1");
	float M_muon2jet2=0.0;
	tree->Branch("M_muon2jet2",&M_muon2jet2,"M_muon2jet2");
	float M_jet1jet2=0.0;
	tree->Branch("M_jet1jet2",&M_jet1jet2,"M_jet1jet2");
	float M_AllParticles=0.0;
	tree->Branch("M_AllParticles",&M_AllParticles,"M_AllParticles");

	float MT_muon1caloMET=0.0;
	tree->Branch("MT_muon1caloMET",&MT_muon1caloMET,"MT_muon1caloMET");
	float MT_jet1caloMET=0.0;
	tree->Branch("MT_jet1caloMET",&MT_jet1caloMET,"MT_jet1caloMET");
	float MT_jet2caloMET=0.0;
	tree->Branch("MT_jet2caloMET",&MT_jet2caloMET,"MT_jet2caloMET");

	//ST
	float ST_calo=0.0;
	tree->Branch("ST_calo",&ST_calo,"ST_calo");
	float ST_calo_munu=0.0;
	tree->Branch("ST_calo_munu",&ST_calo_munu,"ST_calo_munu");

	// Min Met and muon 1

	float minval_muon1caloMET = 0.0;
	tree->Branch("minval_muon1caloMET",&minval_muon1caloMET,"minval_muon1caloMET");

	//*****************************************************************
	//             PARTICLE FLOW MET/JET VARIABLES BELOW
	//*****************************************************************

	float precut_1pfjet=0.0;
	tree->Branch("precut_1pfjet",&precut_1pfjet,"precut_1pfjet");
	float precut_2pfjet=0.0;
	tree->Branch("precut_2pfjet",&precut_2pfjet,"precut_2pfjet");

	float PFJetCount = 0.0;
	tree->Branch("PFJetCount",&PFJetCount,"PFJetCount");

	// Angular Variables

	float Phi_pfjet1=0.0;
	tree->Branch("Phi_pfjet1",&Phi_pfjet1,"Phi_pfjet1");
	float Phi_pfjet2=0.0;
	tree->Branch("Phi_pfjet2",&Phi_pfjet2,"Phi_pfjet2");

	float Eta_pfjet1=0.0;
	tree->Branch("Eta_pfjet1",&Eta_pfjet1,"Eta_pfjet1");
	float Eta_pfjet2=0.0;
	tree->Branch("Eta_pfjet2",&Eta_pfjet2,"Eta_pfjet2");

	//MET
	float MET_pf=0.0;
	float MET_tc=0.0;
	tree->Branch("MET_pf",&MET_pf,"MET_pf");
	tree->Branch("MET_tc",&MET_tc,"MET_tc");

	float MET_pf_prime=0.0;
	tree->Branch("MET_pf_prime",&MET_pf_prime,"MET_pf_prime");

	float MT_muon1pfMET_prime=0.0;
	tree->Branch("MT_muon1pfMET_prime",&MT_muon1pfMET_prime,"MT_muon1pfMET_prime");

	float MT_muon1pfMET_prime_angle=0.0;
	tree->Branch("MT_muon1pfMET_prime_angle",&MT_muon1pfMET_prime_angle,"MT_muon1pfMET_prime_angle");

	float MET_calo_prime=0.0;
	tree->Branch("MET_calo_prime",&MET_calo_prime,"MET_calo_prime");

	float MT_muon1caloMET_prime=0.0;
	tree->Branch("MT_muon1caloMET_prime",&MT_muon1caloMET_prime,"MT_muon1caloMET_prime");

	float MT_muon1caloMET_prime_angle=0.0;

	// PT Variables
	float Pt_pfjet1=0.0;
	tree->Branch("Pt_pfjet1",&Pt_pfjet1,"Pt_pfjet1");
	float Pt_pfjet2=0.0;
	tree->Branch("Pt_pfjet2",&Pt_pfjet2,"Pt_pfjet2");

	//Delta Phi Variables
	float deltaPhi_muon1pfMET=0.0;
	float deltaPhi_muon1tcMET=0.0;
	tree->Branch("deltaPhi_muon1pfMET",&deltaPhi_muon1pfMET,"deltaPhi_muon1pfMET");
	tree->Branch("deltaPhi_muon1tcMET",&deltaPhi_muon1tcMET,"deltaPhi_muon1tcMET");
	float deltaPhi_pfMETmuon2=0.0;
	float deltaPhi_tcMETmuon2=0.0;
	tree->Branch("deltaPhi_pfMETmuon2",&deltaPhi_pfMETmuon2,"deltaPhi_pfMETmuon2");
	tree->Branch("deltaPhi_tcMETmuon2",&deltaPhi_tcMETmuon2,"deltaPhi_tcMETmuon2");
	float deltaPhi_pfjet1pfMET=0.0;
	float deltaPhi_pfjet1tcMET=0.0;
	tree->Branch("deltaPhi_pfjet1pfMET",&deltaPhi_pfjet1pfMET,"deltaPhi_pfjet1pfMET");
	tree->Branch("deltaPhi_pfjet1tcMET",&deltaPhi_pfjet1tcMET,"deltaPhi_pfjet1tcMET");
	float deltaPhi_pfjet2pfMET=0.0;
	float deltaPhi_pfjet2tcMET=0.0;
	tree->Branch("deltaPhi_pfjet2pfMET",&deltaPhi_pfjet2pfMET,"deltaPhi_pfjet2pfMET");
	tree->Branch("deltaPhi_pfjet2tcMET",&deltaPhi_pfjet2tcMET,"deltaPhi_pfjet2tcMET");
	float deltaPhi_muon1pfjet1=0.0;
	tree->Branch("deltaPhi_muon1pfjet1",&deltaPhi_muon1pfjet1,"deltaPhi_muon1pfjet1");
	float deltaPhi_muon1pfjet2=0.0;
	tree->Branch("deltaPhi_muon1pfjet2",&deltaPhi_muon1pfjet2,"deltaPhi_muon1pfjet2");
	float deltaPhi_muon2pfjet1=0.0;
	tree->Branch("deltaPhi_muon2pfjet1",&deltaPhi_muon2pfjet1,"deltaPhi_muon2pfjet1");
	float deltaPhi_muon2pfjet2=0.0;
	tree->Branch("deltaPhi_muon2pfjet2",&deltaPhi_muon2pfjet2,"deltaPhi_muon2pfjet2");
	float deltaPhi_pfjet1pfjet2=0.0;
	tree->Branch("deltaPhi_pfjet1pfjet2",&deltaPhi_pfjet1pfjet2,"deltaPhi_pfjet1pfjet2");

	// Delta R Variables
	float deltaR_pfjet1pfjet2=0.0;
	tree->Branch("deltaR_pfjet1pfjet2",&deltaR_pfjet1pfjet2,"deltaR_pfjet1pfjet2");

	// Invariant and transverse masses
	float M_muon1pfjet1=0.0;
	tree->Branch("M_muon1pfjet1",&M_muon1pfjet1,"M_muon1pfjet1");
	float M_muon1pfjet2=0.0;
	tree->Branch("M_muon1pfjet2",&M_muon1pfjet2,"M_muon1pfjet2");
	float M_muon2pfjet1=0.0;
	tree->Branch("M_muon2pfjet1",&M_muon2pfjet1,"M_muon2pfjet1");
	float M_muon2pfjet2=0.0;
	tree->Branch("M_muon2pfjet2",&M_muon2pfjet2,"M_muon2pfjet2");
	float M_pfjet1pfjet2=0.0;
	tree->Branch("M_pfjet1pfjet2",&M_pfjet1pfjet2,"M_pfjet1pfjet2");
	float M_AllpfParticles=0.0;
	tree->Branch("M_AllpfParticles",&M_AllpfParticles,"M_AllpfParticles");

	float MT_muon1pfMET=0.0;
	float MT_muon1tcMET=0.0;
	tree->Branch("MT_muon1pfMET",&MT_muon1pfMET,"MT_muon1pfMET");
	tree->Branch("MT_muon1tcMET",&MT_muon1tcMET,"MT_muon1tcMET");
	float MT_pfjet1pfMET=0.0;
	float MT_pfjet1tcMET=0.0;
	tree->Branch("MT_pfjet1pfMET",&MT_pfjet1pfMET,"MT_pfjet1pfMET");
	tree->Branch("MT_pfjet1tcMET",&MT_pfjet1tcMET,"MT_pfjet1tcMET");
	float MT_pfjet2pfMET=0.0;
	float MT_pfjet2tcMET=0.0;
	tree->Branch("MT_pfjet2pfMET",&MT_pfjet2pfMET,"MT_pfjet2pfMET");
	tree->Branch("MT_pfjet2tcMET",&MT_pfjet2tcMET,"MT_pfjet2tcMET");
	float MT_pfjet1muon1=0.0;
	tree->Branch("MT_pfjet1muon1",&MT_pfjet1muon1,"MT_pfjet1muon1");
	float MT_pfjet2muon1=0.0;
	tree->Branch("MT_pfjet2muon1",&MT_pfjet2muon1,"MT_pfjet2muon1");
	//ST
	float ST_pf=0.0;
	float ST_tc=0.0;
	tree->Branch("ST_pf",&ST_pf,"ST_pf");
	tree->Branch("ST_tc",&ST_tc,"ST_tc");
	float ST_pf_munu=0.0;
	float ST_tc_munu=0.0;
	tree->Branch("ST_pf_munu",&ST_pf_munu,"ST_pf_munu");
	tree->Branch("ST_tc_munu",&ST_tc_munu,"ST_tc_munu");

	// Min Met and muon 1

	float minval_muon1pfMET = 0.0;
	float minval_muon1tcMET = 0.0;
	tree->Branch("minval_muon1pfMET",&minval_muon1pfMET,"minval_muon1pfMET");
	tree->Branch("minval_muon1tcMET",&minval_muon1tcMET,"minval_muon1tcMET");

	float BJetCount = 0.0;
	tree->Branch("BJetCount",&BJetCount,"BJetCount");

	float BDisc_jet1 = 0.0;
	tree->Branch("BDisc_jet1",&BDisc_jet1,"BDisc_jet1");
	float BDisc_jet2 = 0.0;
	tree->Branch("BDisc_jet2",&BDisc_jet2,"BDisc_jet2");

	float BpfJetCount = 0.0;
	tree->Branch("BpfJetCount",&BpfJetCount,"BpfJetCount");

	float BDisc_pfjet1 = 0.0;
	tree->Branch("BDisc_pfjet1",&BDisc_pfjet1,"BDisc_pfjet1");
	float BDisc_pfjet2 = 0.0;
	tree->Branch("BDisc_pfjet2",&BDisc_pfjet2,"BDisc_pfjet2");

	// Extra Checks

	float deltaR_muon1closestPFJet = 999.9;
	tree->Branch("deltaR_muon1closestPFJet",&deltaR_muon1closestPFJet,"deltaR_muon1closestPFJet");

	float M_pfjet1 = 0.0;
	tree->Branch("M_pfjet1",&M_pfjet1,"M_pfjet1");

	float M_pfjet2 = 0.0;
	tree->Branch("M_pfjet2",&M_pfjet2,"M_pfjet2");

	float PFJetNeutralMultiplicity_pfjet1= 0.0;
	tree->Branch("PFJetNeutralMultiplicity_pfjet1",&PFJetNeutralMultiplicity_pfjet1,"PFJetNeutralMultiplicity_pfjet1");
	float PFJetNeutralHadronEnergyFraction_pfjet1= 0.0;
	tree->Branch("PFJetNeutralHadronEnergyFraction_pfjet1",&PFJetNeutralHadronEnergyFraction_pfjet1,"PFJetNeutralHadronEnergyFraction_pfjet1");
	float PFJetNeutralEmEnergyFraction_pfjet1= 0.0;
	tree->Branch("PFJetNeutralEmEnergyFraction_pfjet1",&PFJetNeutralEmEnergyFraction_pfjet1,"PFJetNeutralEmEnergyFraction_pfjet1");
	float PFJetChargedMultiplicity_pfjet1= 0.0;
	tree->Branch("PFJetChargedMultiplicity_pfjet1",&PFJetChargedMultiplicity_pfjet1,"PFJetChargedMultiplicity_pfjet1");
	float PFJetChargedHadronEnergyFraction_pfjet1= 0.0;
	tree->Branch("PFJetChargedHadronEnergyFraction_pfjet1",&PFJetChargedHadronEnergyFraction_pfjet1,"PFJetChargedHadronEnergyFraction_pfjet1");
	float PFJetChargedEmEnergyFraction_pfjet1= 0.0;
	tree->Branch("PFJetChargedEmEnergyFraction_pfjet1",&PFJetChargedEmEnergyFraction_pfjet1,"PFJetChargedEmEnergyFraction_pfjet1");
	float PFJetNeutralMultiplicity_pfjet2= 0.0;
	tree->Branch("PFJetNeutralMultiplicity_pfjet2",&PFJetNeutralMultiplicity_pfjet2,"PFJetNeutralMultiplicity_pfjet2");
	float PFJetNeutralHadronEnergyFraction_pfjet2= 0.0;
	tree->Branch("PFJetNeutralHadronEnergyFraction_pfjet2",&PFJetNeutralHadronEnergyFraction_pfjet2,"PFJetNeutralHadronEnergyFraction_pfjet2");
	float PFJetNeutralEmEnergyFraction_pfjet2= 0.0;
	tree->Branch("PFJetNeutralEmEnergyFraction_pfjet2",&PFJetNeutralEmEnergyFraction_pfjet2,"PFJetNeutralEmEnergyFraction_pfjet2");
	float PFJetChargedMultiplicity_pfjet2= 0.0;
	tree->Branch("PFJetChargedMultiplicity_pfjet2",&PFJetChargedMultiplicity_pfjet2,"PFJetChargedMultiplicity_pfjet2");
	float PFJetChargedHadronEnergyFraction_pfjet2= 0.0;
	tree->Branch("PFJetChargedHadronEnergyFraction_pfjet2",&PFJetChargedHadronEnergyFraction_pfjet2,"PFJetChargedHadronEnergyFraction_pfjet2");
	float PFJetChargedEmEnergyFraction_pfjet2= 0.0;
	tree->Branch("PFJetChargedEmEnergyFraction_pfjet2",&PFJetChargedEmEnergyFraction_pfjet2,"PFJetChargedEmEnergyFraction_pfjet2");

	// Generator Addon

	// Generator Addon

	float Pt_genjet1 = 0;
	float Pt_genjet2 = 0;
	tree->Branch("Pt_genjet1",&Pt_genjet1,"Pt_genjet1");
	tree->Branch("Pt_genjet2",&Pt_genjet2,"Pt_genjet2");

	float Pt_genmuon1 = 0;
	float Pt_genmuon2 = 0;
	tree->Branch("Pt_genmuon1",&Pt_genmuon1,"Pt_genmuon1");
	tree->Branch("Pt_genmuon2",&Pt_genmuon2,"Pt_genmuon2");

	float Phi_genmuon1 = 0;
	float Phi_genmuon2 = 0;
	tree->Branch("Phi_genmuon1",&Phi_genmuon1,"Phi_genmuon1");
	tree->Branch("Phi_genmuon2",&Phi_genmuon2,"Phi_genmuon2");

	float Eta_genmuon1 = 0;
	float Eta_genmuon2 = 0;
	tree->Branch("Eta_genmuon1",&Eta_genmuon1,"Eta_genmuon1");
	tree->Branch("Eta_genmuon2",&Eta_genmuon2,"Eta_genmuon2");

	float Pt_genMET = 0;
	tree->Branch("Pt_genMET",&Pt_genMET,"Pt_genMET");

	float Phi_genMET = 0;
	tree->Branch("Phi_genMET",&Phi_genMET,"Phi_genMET");

	float genWTM = 0;
	tree->Branch("genWTM",&genWTM,"genWTM");

	float Eta_genMET = 0;
	tree->Branch("Eta_genMET",&Eta_genMET,"Eta_genMET");

	float Pt_genneutrino = 0;
	tree->Branch("Pt_genneutrino",&Pt_genneutrino,"Pt_genneutrino");

	float Phi_genneutrino = 0;
	tree->Branch("Phi_genneutrino",&Phi_genneutrino,"Phi_genneutrino");

	float Eta_genneutrino = 0;
	tree->Branch("Eta_genneutrino",&Eta_genneutrino,"Eta_genneutrino");

	// Recoil

	float Pt_Z_gen = 0.0;
	tree->Branch("Pt_Z_gen",&Pt_Z_gen,"Pt_Z_gen");
	float Pt_W_gen = 0.0;
	tree->Branch("Pt_W_gen",&Pt_W_gen,"Pt_W_gen");

	float Phi_Z_gen = 0.0;
	tree->Branch("Phi_Z_gen",&Phi_Z_gen,"Phi_Z_gen");
	float Phi_W_gen = 0.0;
	tree->Branch("Phi_W_gen",&Phi_W_gen,"Phi_W_gen");

	float U1_Z_gen = 990.0;
	tree->Branch("U1_Z_gen",&U1_Z_gen,"U1_Z_gen");
	float U2_Z_gen = 990.0;
	tree->Branch("U2_Z_gen",&U2_Z_gen,"U2_Z_gen");

	float U1_W_gen = 990.0;
	tree->Branch("U1_W_gen",&U1_W_gen,"U1_W_gen");
	float U2_W_gen = 990.0;
	tree->Branch("U2_W_gen",&U2_W_gen,"U2_W_gen");

	float Pt_Z = 0.0;
	tree->Branch("Pt_Z",&Pt_Z,"Pt_Z");
	float Pt_W = 0.0;
	tree->Branch("Pt_W",&Pt_W,"Pt_W");

	float Phi_Z = 0.0;
	tree->Branch("Phi_Z",&Phi_Z,"Phi_Z");
	float Phi_W = 0.0;
	tree->Branch("Phi_W",&Phi_W,"Phi_w");

	float U1_Z = 0.0;
	tree->Branch("U1_Z",&U1_Z,"U1_Z");
	float U2_Z = 0.0;
	tree->Branch("U2_Z",&U2_Z,"U2_Z");

	float U1_W = 0.0;
	tree->Branch("U1_W",&U1_W,"U1_W");
	float U2_W = 0.0;
	tree->Branch("U2_W",&U2_W,"U2_W");

	//	vector<float>  *BDisc = new vector<float>(100);
	//  t->Branch("BDisc", &BDisc,"BDisc");

	//*****************************************************************
	//             BookKeeping Variables
	//*****************************************************************

	// BookKeeping Variables
	Double_t run_number = 0.0;
	tree->Branch("run_number",&run_number,"run_number/D");
	Double_t event_number = 0.0;
	tree->Branch("event_number",&event_number,"event_number/D");
	float bx = 0.0;
	tree->Branch("bx",&bx,"bx");
	Double_t xsection = 0.0;
	tree->Branch("xsection",&xsection,"xsection/D");

	// Original event number for double checking
	Double_t Events_AfterLJ=0;
	tree->Branch("Events_AfterLJ",&Events_AfterLJ,"Events_AfterLJ/D");

	Double_t Events_Orig=0;
	tree->Branch("Events_Orig",&Events_Orig,"Events_Orig/D");

	// Store weight value for reference in root file
	Double_t weight=0.0;
	tree->Branch("weight",&weight,"weight/D");

	//===================================================================================================
	//===================================================================================================

	//===================================================================================================
	//        SETUP WITH SOME TEMPLATE INPUTS AND THRESHOLDS
	//===================================================================================================

	// "1.0" is a W0Jets_Pt0to100 that gets replaced from the python template replicator
	Double_t lumi=1.0;

	Events_AfterLJ = 1.0*(fChain->GetEntries());

	Events_Orig = 3541971.0;// placekeeperr

	bool IsW = true;

	Double_t N = Events_AfterLJ;
	xsection = 25060.799999999999;	 // "25060.799999999999" is a W0Jets_Pt0to100 that gets replaced from the python template replicator
	Double_t eff = 1.0;	 // Another W0Jets_Pt0to100, for filter 1.0 or what have you. Multiply by sigma for "effective cross section"

	//calculate the event weighting
	weight = eff*lumi*xsection/Events_Orig;
	int xx=0;					 //dummy variable for state of loop calculation
	//PT THRESHOLDS -- need to define here
	//	double cut_pT_lep = 35.;
	//	double cut_pT_jet = 30.;
	// Display status to screen
	std::cout<<"            "<<std::endl;
	std::cout<<" Evaluating for: W0Jets_Pt0to100 \n MC events: "<<N<< " \n Actual Events: "<<weight*Events_Orig<<" \n Integrated Luminosity: "<<lumi<<" pb^(-1) \n Cross Section: "<<xsection<<" pb "<<std::endl;
	std::cout<<"            "<<std::endl;

	//===================================================================================================
	//===================================================================================================

	//===================================================================================================
	//           LOOP OVER ENTRIES AND MAKE MAIN CALCULATIONS
	//===================================================================================================

	if (fChain == 0) return;	 //check for correctly assigned chain from h file

	//Long64_t nentries = fChain->GetEntriesFast();
	Long64_t nbytes = 0, nb = 0;

	//N=1000;  /// TEST>>>>>> COMMENT THIS ALWAYS

	for (Long64_t jentry=0; jentry<N;jentry++)
	{
		//-------------------------------------------------------
		// Show progress so you know the program hasn't failed...
		//-------------------------------------------------------
		for (xx=0; xx<100; xx=xx+10)
		{
			if ((100*jentry/(N)>xx)&&(100*(jentry-1)/(N)<xx))
			{
				std::cout<<xx<<" % complete"<<std::endl;
			}
		}
		//-------------------------------------------------------
		//-------------------------------------------------------

		Long64_t ientry = LoadTree(jentry);
		if (ientry < 0) break;
		nb = fChain->GetEntry(jentry);   nbytes += nb;

		// HLT Requirement Enforcement

		run_number = run;
		event_number = event;
		bx = bunch;

		if (run_number<1000)
		{
			if ( ((*HLTResults)[60] ==1) ||((*HLTResults)[0] ==1) ) precut_HLT=1.0;
			else continue;
		}

		if ((run_number>1000)&&(run_number<146000))
		{
			if ((*HLTResults)[60] ==1) precut_HLT=1.0;
			else continue;
		}

		if ((run_number>146000)&&(run_number<147455))
		{
			if ((*HLTResults)[61] ==1) precut_HLT=1.0;
			else continue;
		}

		if (run_number>=147455)
		{
			if ((*HLTResults)[66] ==1) precut_HLT=1.0;
			else continue;
		}

		//===========================================================================================//
		//===========================================================================================//

		///////////////////////////////////////////////////////////////////////////////////
		//////////////////////////////  VERTEX CONDITIONS      ////////////////////////////
		///////////////////////////////////////////////////////////////////////////////////
		//					std::cout<<isBeamScraping<<std::endl;

		if ( isBeamScraping ) continue;

		bool vtxFound = false;
		for(int ivtx = 0; ivtx != VertexZ->size(); ++ivtx)
		{
			if ( VertexIsFake->at(ivtx) == true ) continue;
			if ( VertexNDF->at(ivtx) <= 4.0 ) continue;
			if ( TMath::Abs(VertexZ->at(ivtx)) > 24.0 ) continue;
			if ( TMath::Abs(VertexRho->at(ivtx)) >= 2.0 ) continue;
			vtxFound = true;
			break;
		}
		if ( !vtxFound ) continue;

		///////////////////////////////////////////////////////////////////////////////////
		//////////////////////////////ELECTRONS DISAMBIGUATIONS////////////////////////////
		///////////////////////////////////////////////////////////////////////////////////
		vector<int> v_idx_ele_final;
		// check if there are electrons
		int nelectrons = 0;
		for(int iele = 0; iele < ElectronPt->size(); ++iele)
		{
			if ( ElectronPt->at(iele) < 15.0 ) continue;
			if ( (ElectronPassID->at(iele) & 1 << 5 ) && ElectronOverlaps->at(iele) == 0 )
			{
				++nelectrons;

				v_idx_ele_final.push_back(iele);
			}
		}
		//		if ( nelectrons != 0 ) continue;

		///////////////////////////////////////////////////////////////////////////////////
		//////////////////////////////MUONS DISAMBIGUATIONS////////////////////////////////
		///////////////////////////////////////////////////////////////////////////////////

		vector<int> v_idx_muon_final;
		// container for muons
		vector<TLorentzVector> muons;
		int iMUON = -1;
		// select muons

		bool checkPT = true;

		for(int imuon = 0; imuon < MuonPt->size(); ++imuon)
		{

			float muonPt = MuonPt->at(imuon);
			float muonEta = MuonEta->at(imuon);

			//       if ( muonPt < 35.0 ) continue;
			if (checkPT && (muonPt < 30.0) ) continue;

			bool quality =
				fabs(muonEta) < 2.1  &&
								 // pass isolation requirements
				MuonPassIso ->at(imuon) == 1    &&
								 // pass muon ID
				MuonPassID  ->at(imuon) == 1    &&
								 // at least 11 muon track hits
				MuonTrkHits ->at(imuon) >= 11   &&
								 // track d0 < 0.2 cm
				fabs(MuonTrkD0   ->at(imuon)) < 0.2;

			if ( ! quality ) continue;
			iMUON = imuon;

			TLorentzVector muon;
			muon.SetPtEtaPhiM( MuonPt -> at(imuon),
				MuonEta-> at(imuon),
				MuonPhi-> at(imuon),
				0);

			//			bool same = false;
			//			for(unsigned j = 0; j != muons.size(); ++j)
			//				if ( muon.DeltaR(muons[j]) < 0.3 ) same = true;
			//			if ( same ) continue;
			muons.push_back(muon);
			checkPT=false;

			v_idx_muon_final.push_back(imuon);
		}						 // loop over muons

		if ( muons.size() <1 ) continue;

		D0_muon1 = MuonTrkD0->at(v_idx_muon_final[0]);
		NHits_muon1 = MuonTrkHits ->at(v_idx_muon_final[0]);
		Charge_muon1 = MuonCharge->at(v_idx_muon_final[0]);
		RelIso_muon1 = MuonRelIso->at(v_idx_muon_final[0]);
		TrkDZ_muon1 = MuonTrkDz->at(v_idx_muon_final[0]);
		ChiSq_muon1 = MuonGlobalChi2->at(v_idx_muon_final[0]);
		TLorentzVector muon = muons[0];

		if ( muons.size() >1 )
		{

			D0_muon2 = MuonTrkD0->at(v_idx_muon_final[1]);
			NHits_muon2 = MuonTrkHits ->at(v_idx_muon_final[1]);
			Charge_muon2 = MuonCharge->at(v_idx_muon_final[1]);
			RelIso_muon2 = MuonRelIso->at(v_idx_muon_final[1]);
			TrkDZ_muon2 = MuonTrkDz->at(v_idx_muon_final[1]);
			ChiSq_muon2 = MuonGlobalChi2->at(v_idx_muon_final[1]);
		}

		if ( muons.size() >2 )
		{

			D0_muon3 = MuonTrkD0->at(v_idx_muon_final[2]);
			NHits_muon3 = MuonTrkHits ->at(v_idx_muon_final[2]);
			Charge_muon3 = MuonCharge->at(v_idx_muon_final[2]);
			RelIso_muon3 = MuonRelIso->at(v_idx_muon_final[2]);
			TrkDZ_muon3 = MuonTrkDz->at(v_idx_muon_final[2]);
		}
		///////////////////////////////////////////////////////////////////////////////////
		//////////////////////////////pfjetS DISAMBIGUATIONS/////////////////////////////////
		///////////////////////////////////////////////////////////////////////////////////

		// Get Good Jets in general

		deltaR_muon1closestPFJet = 999.9;
		float deltaR_thisjet = 9999.9;
		vector<TLorentzVector> jets;
		vector<int> v_idx_pfjet_prefinal;
		vector<int> v_idx_pfjet_final_unseparated;
		vector<int> v_idx_pfjet_final;
		BpfJetCount = 0.0;
		// select jets
		for(int ijet = 0; ijet < PFJetPt->size(); ++ijet)
		{
			double jetPt = PFJetPt -> at(ijet);
			double jetEta = PFJetEta -> at(ijet);

								 // require jets with pT > 25
			if ( jetPt < 30.0 ) continue;
								 // require jets in acceptance
			if ( fabs(jetEta) > 3.0 ) continue;

			if ( PFJetNeutralHadronEnergyFraction->at(ijet) >= 0.99) continue;
			if ( PFJetNeutralEmEnergyFraction    ->at(ijet) >= 0.99) continue;
			if ( PFJetChargedMultiplicity -> at(ijet) +
				PFJetNeutralMultiplicity -> at(ijet) <= 1 ) continue;
			if ( TMath::Abs(jetEta) < 2.4 )
			{
				if ( PFJetChargedHadronEnergyFraction->at(ijet) <= 0 ) continue;
				if ( PFJetChargedMultiplicity        ->at(ijet) <= 0 ) continue;
				if ( PFJetChargedEmEnergyFraction    ->at(ijet) >= 0.99) continue;
			}

			v_idx_pfjet_prefinal.push_back(ijet);
		}

		/// Filter out jets that are actuall muons
		TLorentzVector thisjet, thismu;
		vector<int> jetstoremove;

		float thisdeltar = 0.0;
		float mindeltar = 99999;
		int minjet = 0;
		int muindex = 99;
		int jetindex = 99;
		// Get list of jets to throw out
		for(int imu=0; imu<v_idx_muon_final.size(); imu++)
		{
			mindeltar = 999999;
			muindex = v_idx_muon_final[imu];
			thismu.SetPtEtaPhiM(MuonPt->at(muindex),MuonEta->at(muindex),MuonPhi->at(muindex),0);

			for(int ijet=0; ijet<v_idx_pfjet_prefinal.size(); ijet++)
			{
				jetindex = v_idx_pfjet_prefinal[ijet];
				thisjet.SetPtEtaPhiM((*PFJetPt)[jetindex],(*PFJetEta)[jetindex],(*PFJetPhi)[jetindex],0);

				thisdeltar = thismu.DeltaR(thisjet);

				if (thisdeltar < mindeltar)
				{
					mindeltar = thisdeltar;
					minjet = ijet;
				}
			}

			if (mindeltar<0.3) jetstoremove.push_back(minjet)       ;

		}

		jetindex = 99;
		int remjetindex = 99;
		// Eliminate bad jets from prefinal jet vector, save as final
		for(int ijet=0; ijet<v_idx_pfjet_prefinal.size(); ijet++)
		{
			int jetgood = 1;
			jetindex = v_idx_pfjet_prefinal[ijet];
			for(int kjet=0; kjet<jetstoremove.size(); kjet++)
			{
				remjetindex = jetstoremove[kjet];
				if (jetindex == remjetindex) jetgood=0;

			}

			if (jetgood ==1) v_idx_pfjet_final_unseparated.push_back(jetindex);
		}

		// Take filtered jets and eliminate those too close to the muon. save b variables

		jetindex = 99;

		for(int ijet=0; ijet<v_idx_pfjet_final_unseparated.size(); ijet++)
		{
			jetindex = v_idx_pfjet_final_unseparated[ijet];
			double jetPt = PFJetPt -> at(jetindex);
			double jetEta = PFJetEta -> at(jetindex);

			TLorentzVector newjet;
			newjet.SetPtEtaPhiM(jetPt,  jetEta, PFJetPhi->at(jetindex),     0);
			// require a separation between a muon and a jet

			deltaR_thisjet =  newjet.DeltaR(muon);
			if ( deltaR_thisjet < deltaR_muon1closestPFJet)  deltaR_muon1closestPFJet = deltaR_thisjet ;

			if ( deltaR_thisjet < 0.5 ) continue;

			if ( PFJetTrackCountingHighEffBTag->at(jetindex) > 1.7 )
			{
				BpfJetCount = BpfJetCount + 1.0;
			}

			// if we are here, the jet is good
			v_idx_pfjet_final.push_back(jetindex);
		}

		///////////////////////////////////////////////////////////////////////////////////
		///////////////////////// CALOJETS DISAMBIGUATIONS/////////////////////////////////
		///////////////////////////////////////////////////////////////////////////////////
		vector<int> v_idx_jet_final;
		for(int ijet=0;ijet<(*CaloJetPt).size();ijet++)
		{

			//pT pre-cut on reco jets (no disambiguation)
			if ((*CaloJetPt)[ijet] < 30.0) continue;

			// strict jet eta requirement
			if (fabs((*CaloJetEta)[ijet])>3.0) continue;
			//Loose Jet conditions
			if (fabs((*CaloJetEta)[ijet])<2.6)
			{
				if ((*CaloJetEMF)[ijet]<.01) continue;
			}
			if ((*CaloJetn90Hits)[ijet]<=1) continue;

			if ((*CaloJetfHPD)[ijet]>.98) continue;

			TLorentzVector currentjet;
			currentjet.SetPtEtaPhiM(  (*CaloJetPt)[ijet] , (*CaloJetEta)[ijet]  , (*CaloJetPhi)[ijet] , 0  );

			if( (currentjet.DeltaR(muon)) <.5 ) continue;

			//			if (muonfinalcount>=2){
			//				if( (currentjet.DeltaR(mu2)) <.5 ) continue;
			//			}

			//if((((*CaloJetOverlaps)[ijet] & 1 << 6)==0)

			v_idx_jet_final.push_back(ijet);
			//      BDisc -> push_back(CaloJetTrackCountingHighEffBTag->at(ijet));

			if ( CaloJetTrackCountingHighEffBTag->at(ijet) > 1.7 ) BJetCount = BJetCount + 1.0;

		}						 //end loop over original jets

		vector<int> v_idx_Jet_calofinal = v_idx_jet_final;


		//###########################################################################################//
		//#######  GENERATOR ADD-ON INFORMATION                                           ###########//
		//###########################################################################################//

				float piover2 = 3.1415926/2.0;
     TLorentzVector V_MetAddition;
			V_MetAddition.SetPtEtaPhiM(0.0,0.0,0.0,0.0);

TLorentzVector UW_gen , BW_gen, v_GenNu, muon1test;

BW_gen.SetPtEtaPhiM(0,0,0,0); UW_gen.SetPtEtaPhiM(0,0,0,0); v_GenNu.SetPtEtaPhiM(0,0,0,0), muon1test.SetPtEtaPhiM(0,0,0,0) ;

		/// Generator Addon
		if (!isData)
		{

			Pt_genjet1 = 0;
			Pt_genjet2 = 0;
			Pt_genmuon1 = 0;
			Pt_genmuon2 = 0;
			Phi_genmuon1 = 0;
			Eta_genmuon1 = 0;
			Phi_genmuon2 = 0;
			Eta_genmuon2 = 0;
			Pt_genMET = 0;
			Pt_genneutrino = 0;
			Eta_genneutrino = 0;
			Phi_genneutrino = 0;
			Phi_genMET = 0;
			Eta_genMET = 0;

			float genmetPX = 0.0;
			float genmetPY = 0.0;

			float tmu = 0;

			for(int ijet = 0; ijet < GenJetPt->size(); ++ijet)
			{
				if (ijet ==0) Pt_genjet1 = GenJetPt->at(ijet);
				if (ijet ==1) Pt_genjet2 = GenJetPt->at(ijet);
			}

			for(int ip = 0; ip != GenParticlePdgId->size(); ++ip)
			{

				int pdgId = GenParticlePdgId->at(ip);
				int motherIndex = GenParticleMotherIndex->at(ip);
								 // ISR
				if ( motherIndex == -1 ) continue;
				int pdgIdMother = GenParticlePdgId->at(motherIndex);

				//muon
								 // && TMath::Abs(pdgIdMother) == 23 ) {
								 // Muon
				if ( TMath::Abs(pdgId) == 13 )
				{
//				std::cout<<GenParticlePt -> at (ip)<<"   "<<GenParticlePhi-> at (ip)<<std::endl;

					if (Pt_genmuon1==0)
					{
						Pt_genmuon1 = GenParticlePt -> at (ip);
						Phi_genmuon1 = GenParticlePhi-> at (ip);
						Eta_genmuon1 = GenParticleEta-> at (ip);
					}

					if (Pt_genmuon1>0)
					{
						Pt_genmuon2 = GenParticlePt -> at (ip);
						Phi_genmuon2 = GenParticlePhi-> at (ip);
						Eta_genmuon2 = GenParticleEta-> at (ip);
					}

				}

								 // Muon Neutrino
				if ( TMath::Abs(pdgId) == 14 )
				{

					if (GenParticlePt->at(ip) > Pt_genneutrino)
					{
						Pt_genneutrino = GenParticlePt -> at (ip);
						Phi_genneutrino = GenParticlePhi-> at (ip);
						Eta_genneutrino = GenParticleEta-> at (ip);
					}
				}

			}

//			std::cout<<"---------------"<<std::endl;
//			std::cout<<Pt_genmuon1<<"   "<<Phi_genmuon1<<std::endl;
//			std::cout<<Pt_genmuon2<<"   "<<Phi_genmuon2<<std::endl;
//			std::cout<<"==============="<<std::endl;
//						std::cout<<Pt_genneutrino<<"    "<<Pt_genmuon1<<std::endl;

			Pt_genMET = GenMETTrue->at(0);
			Phi_genMET = GenMETPhiTrue->at(0);
			genWTM = 0.0;
			genWTM =  TMass(Pt_genmuon1,Pt_genMET, fabs(Phi_genmuon1 - Phi_genMET) );

			// Set the recoil variables

			U1_Z_gen = 990.0;
			U2_Z_gen = 990.0;
			U1_W_gen = 990.0;
			U2_W_gen = 990.0;

			TLorentzVector v_GenMuon1, v_GenMuon2, v_GenMet;

			v_GenMuon1.SetPtEtaPhiM(Pt_genmuon1,Eta_genmuon1,Phi_genmuon1,0);
			v_GenMuon2.SetPtEtaPhiM(Pt_genmuon2,Eta_genmuon2,Phi_genmuon2,0);
			v_GenNu.SetPtEtaPhiM( Pt_genneutrino ,Eta_genneutrino,Phi_genneutrino ,0);
			v_GenMet.SetPtEtaPhiM ( Pt_genMET, 0, Phi_genMET,0 );



			Pt_W_gen = (v_GenMuon1 + v_GenNu).Pt();
			Phi_W_gen = (v_GenMuon1 + v_GenNu).Phi();

			UW_gen = -(v_GenMet + v_GenMuon1 );
			BW_gen = (v_GenMuon1+v_GenNu);
			U1_W_gen = (UW_gen.Pt()) * (cos(UW_gen.DeltaPhi(BW_gen))) ;
			U2_W_gen = (UW_gen.Pt()) * (sin(UW_gen.DeltaPhi(BW_gen))) ;

			Pt_Z_gen = (v_GenMuon1 + v_GenMuon2).Pt();
			Phi_Z_gen = (v_GenMuon1 + v_GenMuon2).Phi();

			TLorentzVector UZ_gen = -(v_GenMet + v_GenMuon1 + v_GenMuon2);
			TLorentzVector BZ_gen = (v_GenMuon1+v_GenMuon2 );
			U1_Z_gen = (UZ_gen.Pt()) * (cos(UZ_gen.DeltaPhi(BZ_gen))) ;
			U2_Z_gen = (UZ_gen.Pt()) * (sin(UZ_gen.DeltaPhi(BZ_gen))) ;


//**********************************************************************************
     // TEST TEST Using only gen neutrino

			TLorentzVector pfMETtest;
		  pfMETtest.SetPtEtaPhiM(PFMET->at(0),0.0,PFMETPhi->at(0),0.0);
			muon1test.SetPtEtaPhiM(MuonPt->at(v_idx_muon_final[0]),MuonEta->at(v_idx_muon_final[0]),MuonPhi->at(v_idx_muon_final[0]),0.0);

			Pt_W_gen = (muon1test + v_GenNu).Pt();

			UW_gen = -(pfMETtest + muon1test );
			BW_gen = (muon1test +v_GenNu);
			U1_W_gen = (UW_gen.Pt()) * (cos(UW_gen.DeltaPhi(BW_gen))) ;
			U2_W_gen = (UW_gen.Pt()) * (sin(UW_gen.DeltaPhi(BW_gen))) ;

     // END  TEST TEST Using only gen neutrino
//**********************************************************************************


//			std::cout<<(v_GenMuon1.DeltaPhi(v_GenNu))<<std::endl;
//			std::cout<<(v_GenMuon1.DeltaPhi(v_GenMuon2))<<std::endl;
//			std::cout<<"-----------------------"<<std::endl;

//      if (Pt_W_gen> 10 && Pt_W_gen< 11) std::cout<<U1_W_gen<<std::endl;
//      if (Pt_W_gen> 10 && Pt_W_gen< 11) std::cout<<U2_W_gen<<std::endl;
//      if (Pt_W_gen> 10 && Pt_W_gen< 11) 			std::cout<<"-----------------------"<<std::endl;
      // Recoil Corrections
//      if (Pt_Z_gen> 10 && Pt_Z_gen< 11) std::cout<<U1_Z_gen<<std::endl;
//      if (Pt_Z_gen> 10 && Pt_Z_gen< 11) std::cout<<U2_Z_gen<<std::endl;
//      if (Pt_Z_gen> 10 && Pt_Z_gen< 11) 			std::cout<<"-----------------------"<<std::endl;

			

			if (IsW && DoRecoilCorrections)
			{



				float U1Phi = - BW_gen.Phi();

				float U2Phi = BW_gen.Phi() + piover2;

				if ((BW_gen.DeltaPhi(UW_gen)) < 0)	 U2Phi = BW_gen.Phi() - piover2;


//				if (cos(abs( U2Phi-UW_gen.Phi())) <0.0) U2Phi = BW_gen.Phi() - piover2;


//				std::cout<<BW_gen.Phi() - U2Phi<<std::endl;

				float U1Prime = F_U1Prime(Pt_W_gen);
				float U2Prime = F_U2Prime(Pt_W_gen);

				TLorentzVector V_UPrime, V_U1Prime, V_U2Prime, V_MetPrime;

				V_U1Prime.SetPtEtaPhiM(U1Prime,0,U1Phi,0);
				V_U2Prime.SetPtEtaPhiM(U2Prime,0,U2Phi,0);

				V_UPrime = V_U1Prime + V_U2Prime;

				V_MetPrime = -(v_GenMuon1+ V_UPrime);

				V_MetAddition.SetPtEtaPhiM(V_MetPrime.Pt(),0,V_MetPrime.Phi(),0);
		
				V_MetAddition = V_MetAddition - v_GenMet;

			}

		}

		//###########################################################################################//
		//#######    BEGIN PRECUT ANALYSIS AND TMVA/LQMuMuAnalysis VARIABLE CALCULATION     ###########//
		//###########################################################################################//

		//*******************************************************//
		//***************** ZERO THE VARIABLES ******************//
		//*******************************************************//

		// Basic precut variables

		precut_1muon=0.0;
		precut_2muon=0.0;
		precut_1jet=0.0;
		precut_2jet=0.0;

		precut_1pfjet=0.0;
		precut_2pfjet=0.0;

		precut_2muonexact_chargeproduct=0.0;
		precut_muonDeltaR = 0.0;

		// Extra PT variables for computational purposes
		Pt_muon1 = 0.0 ;
		Pt_muon2=0.0;
		Pt_muon3=0.0;
		Pt_jet1 = 0.0 ;
		Pt_jet2 = 0.0 ;
		Pt_ele1 = 0.0;
		MET_calo=0.0;
		MET_pf=0.0;
		MET_tc=0.0;

		Pt_pfjet1 = 0.0 ;
		Pt_pfjet2 = 0.0 ;

		// delta phi's for transverse masses
		deltaPhi_muon1caloMET=99.0;
		deltaPhi_jet1caloMET=99.0;
		deltaPhi_jet2caloMET=99.0;

		deltaPhi_muon1pfMET=99.0;
		deltaPhi_muon1tcMET=99.0;
		deltaPhi_pfjet1pfMET=99.0;
		deltaPhi_pfjet1tcMET=99.0;
		deltaPhi_pfjet2pfMET=99.0;
		deltaPhi_pfjet2tcMET=99.0;

		deltaPhi_muon1jet1=99.0;
		deltaPhi_muon1jet2=99.0;
		deltaPhi_muon2jet1=99.0;
		deltaPhi_muon2jet2=99.0;

		deltaPhi_muon1pfjet1=99.0;
		deltaPhi_muon1pfjet2=99.0;
		deltaPhi_muon2pfjet1=99.0;
		deltaPhi_muon2pfjet2=99.0;

		deltaPhi_jet1jet2=99.0;

		deltaPhi_pfjet1pfjet2=99.0;

		deltaPhi_muon1muon2=99.0;

		// mass variables and S_T
		M_muon1muon2 = 0.0;
		M_muon1muon3 = 0.0;
		M_muon2muon3 = 0.0;

		M_muon1jet1 = 0.0;
		M_muon1jet2 = 0.0;
		M_muon2jet1 = 0.0;
		M_muon2jet2 = 0.0;
		M_jet1jet2 = 0.0;
		M_AllParticles = 0.0;

		M_muon1pfjet1 = 0.0;
		M_muon1pfjet2 = 0.0;
		M_muon2pfjet1 = 0.0;
		M_muon2pfjet2 = 0.0;
		M_pfjet1pfjet2 = 0.0;
		M_AllpfParticles = 0.0;

		MT_muon1caloMET = 0.0;
		MT_jet1caloMET = 0.0;
		MT_jet2caloMET = 0.0;

		MT_muon1pfMET = 0.0;
		MT_muon1tcMET = 0.0;
		MT_pfjet1pfMET = 0.0;
		MT_pfjet1tcMET = 0.0;
		MT_pfjet2pfMET = 0.0;
		MT_pfjet2tcMET = 0.0;

		ST_calo= 0.0;
		ST_calo_munu=0.0;

		ST_pf= 0.0;
		ST_tc= 0.0;
		ST_pf_munu=0.0;
		ST_tc_munu=0.0;
		Charge_muon1=0.0;
		Phi_muon1=99.0;
		Phi_muon2=99.0;
		Phi_muon3=99.0;
		Eta_muon1=99.0;
		Eta_muon2=99.0;
		Eta_muon3=99.0;

		Phi_jet1=99.0;
		Phi_jet2=99.0;
		Eta_jet1=99.0;
		Eta_jet2=99.0;

		Phi_pfjet1=99.0;
		Phi_pfjet2=99.0;
		Eta_pfjet1=99.0;
		Eta_pfjet2=99.0;

		deltaR_muon1muon2=99.0;
		deltaR_jet1jet2=99.0;
		deltaR_pfjet1pfjet2=99.0;

		minval_muon1pfMET = 0.0;
		minval_muon1tcMET = 0.0;
		minval_muon1caloMET = 0.0;

		MT_pfjet1pfMET=0.0;
		MT_pfjet1tcMET=0.0;
		MT_pfjet2pfMET=0.0;
		MT_pfjet2tcMET=0.0;
		MT_pfjet1muon1=0.0;
		MT_pfjet2muon1=0.0;

		MET_pf_prime = 0;
		MT_muon1caloMET_prime = 0;
		MT_muon1caloMET_prime_angle = 0;

		MET_pf_prime = 0;
		MT_muon1pfMET_prime = 0;
		MT_muon1pfMET_prime_angle = 0;

		M_pfjet1 = 0.0;
		M_pfjet2 = 0.0;

		Pt_Z = 0.0;
		Pt_W = 0.0;

		Phi_Z = 0.0;
		Phi_W = 0.0;

		PFJetNeutralMultiplicity_pfjet1= 0.0;
		PFJetNeutralHadronEnergyFraction_pfjet1= 0.0;
		PFJetNeutralEmEnergyFraction_pfjet1= 0.0;
		PFJetChargedMultiplicity_pfjet1= 0.0;
		PFJetChargedHadronEnergyFraction_pfjet1= 0.0;
		PFJetChargedEmEnergyFraction_pfjet1= 0.0;
		PFJetNeutralMultiplicity_pfjet2= 0.0;
		PFJetNeutralHadronEnergyFraction_pfjet2= 0.0;
		PFJetNeutralEmEnergyFraction_pfjet2= 0.0;
		PFJetChargedMultiplicity_pfjet2= 0.0;
		PFJetChargedHadronEnergyFraction_pfjet2= 0.0;
		PFJetChargedEmEnergyFraction_pfjet2= 0.0;

		U1_Z = 990.0;
		U2_Z = 990.0;
		U1_W = 990.0;
		U2_W = 990.0;

								 // 4-Vectors for Particles
		TLorentzVector jet1, jet2, pfjet1, pfjet2, muon1,muon3, caloMET,muon2,pfMET,tcMET;

		MuonCount = 1.0*v_idx_muon_final.size();
		EleCount = 1.0*v_idx_ele_final.size();
		JetCount = 1.0*v_idx_jet_final.size();
		PFJetCount = 1.0*v_idx_pfjet_final.size();

		//*******************************************************//

		//*******************************************************//
		//*****************    MET (or Nu)     ******************//
		//*******************************************************//

		MET_calo = CaloMET->at(0);
		caloMET.SetPtEtaPhiM(MET_calo,0.0,CaloMETPhi->at(0),0.0);

		MET_pf = PFMET->at(0);

		MET_tc = TCMET->at(0);
		pfMET.SetPtEtaPhiM(MET_pf,0.0,PFMETPhi->at(0),0.0);

		tcMET.SetPtEtaPhiM(MET_tc,0.0,TCMETPhi->at(0),0.0);

		if (IsW && DoRecoilCorrections && false)
		{
			caloMET = caloMET + V_MetAddition; MET_calo = caloMET.Pt();
			pfMET = pfMET + V_MetAddition; MET_pf = pfMET.Pt();
			tcMET = tcMET + V_MetAddition; MET_tc = tcMET.Pt();
		}

//std::cout<<MET_pf<<std::endl;
    // Secondary Recoil Test 

		//*******************************************************//
		//***************   Recoil Corrections    ***************//
		//*******************************************************//
      // Recoil Corrections
			if (IsW && DoRecoilCorrections && true)
			{

				float rho = BW_gen.DeltaPhi(UW_gen);

				float U1Phi =  BW_gen.Phi() + 2*piover2;
				if (U1Phi> (2*piover2)) U1Phi = U1Phi - 4*piover2;

//				std::cout<<U1Phi<<"  "<<BW_gen.Phi()<<std::endl;

				float check_phi_u1 = U1Phi; if (check_phi_u1<0) check_phi_u1 = check_phi_u1 + 4*piover2;
				float check_phi_w = BW_gen.Phi(); if (check_phi_w<0) check_phi_w = check_phi_w +  4*piover2;
				float check_phi_u = UW_gen.Phi(); if (check_phi_u<0) check_phi_u = check_phi_u +  4*piover2;

				float check_phi_u2 = 99;
				if ((check_phi_w<2*piover2)&&(check_phi_u>check_phi_w)) check_phi_u2 = check_phi_w + piover2;
				if ((check_phi_w<2*piover2)&&(check_phi_u<check_phi_w)) check_phi_u2 = check_phi_w - piover2;
				if ((check_phi_w>2*piover2)&&(check_phi_u>check_phi_w)) check_phi_u2 = check_phi_w + piover2;
				if ((check_phi_w>2*piover2)&&(check_phi_u<check_phi_w)&&(check_phi_u>(check_phi_w - 2*piover2))) check_phi_u2 = check_phi_w - piover2;
				if ((check_phi_w>2*piover2)&&(check_phi_u<check_phi_w)&&(check_phi_u<(check_phi_w - 2*piover2))) check_phi_u2 = check_phi_w + piover2;

        if (check_phi_u2 > 4*piover2) check_phi_u2 = check_phi_u2 - 4*piover2;

//				std::cout<<check_phi_w<<"   "<<check_phi_u<<"   "<<check_phi_u2<<std::endl;
				float U2Phi = check_phi_u2;


//				float U2Phi = BW_gen.Phi() + piover2;

//				if (cos(abs( U2Phi-UW_gen.Phi())) <0.0) U2Phi = BW_gen.Phi() - piover2;


			  float reco_Pt_W = (muon1test + v_GenNu).Pt();
			  float reco_Phi_W = (muon1test + v_GenNu).Phi();

				

//				std::cout<<reco_Pt_W <<std::endl;
				float U1Prime = F_U1Prime(reco_Pt_W);
				float U2Prime = F_U2Prime(reco_Pt_W);

				TLorentzVector V_UPrime, V_U1Prime, V_U2Prime, V_MetPrime;

				V_U1Prime.SetPtEtaPhiM(U1Prime,0,U1Phi,0);
				V_U2Prime.SetPtEtaPhiM(U2Prime,0,U2Phi,0);

				V_UPrime = V_U1Prime + V_U2Prime;

				V_MetPrime = -(muon1test+ V_UPrime);

				pfMET.SetPtEtaPhiM(V_MetPrime.Pt(),0,V_MetPrime.Phi(),0);
		
				MET_pf = pfMET.Pt();

			}
//std::cout<<MET_pf<<std::endl;
//std::cout<<"------"<<std::endl;
		//===========================================================================================//

		//*******************************************************//
		//***************   In case of Electron   ***************//
		//*******************************************************//

		if (EleCount>=1)
		{
			Pt_ele1 = ElectronPt->at(v_idx_ele_final[0]);

		}


//		std::cout<<MET_pf<<"    "<<pfMET.Phi()<<std::endl;
//		std::cout<<"---------"<<std::endl;
		//*******************************************************//

		//===========================================================================================//

		//*******************************************************//
		//*****************    At least 1 Mu   ******************//
		//*******************************************************//

		if (MuonCount>=1)
		{
			Pt_muon1 = MuonPt->at(v_idx_muon_final[0]);
			Phi_muon1 = MuonPhi->at(v_idx_muon_final[0]);
			Eta_muon1 = MuonEta->at(v_idx_muon_final[0]);
			precut_1muon = 1.0;

			muon1.SetPtEtaPhiM(Pt_muon1,Eta_muon1,Phi_muon1,0);

			deltaPhi_muon1caloMET = abs(caloMET.DeltaPhi(muon1));

			MT_muon1caloMET = TMass(Pt_muon1,MET_calo,deltaPhi_muon1caloMET);

			Charge_muon1 = 1.0*(MuonCharge->at(v_idx_muon_final[0]));

			minval_muon1caloMET = Pt_muon1;

			if (MET_calo < Pt_muon1) minval_muon1caloMET = MET_calo;

			MET_calo_prime = MET_calo;

			MT_muon1caloMET_prime_angle = TMass(Pt_muon1,MET_calo_prime,deltaPhi_muon1caloMET);

			if (deltaPhi_muon1caloMET < 3.1415926/2.0)
			{
				MET_calo_prime = MET_calo*sin(deltaPhi_muon1caloMET);
				MT_muon1caloMET_prime_angle = TMass(Pt_muon1,MET_calo_prime,3.1415926/2.0);
			}

			MT_muon1caloMET_prime = TMass(Pt_muon1,MET_calo_prime,deltaPhi_muon1caloMET);

			Pt_W = (muon1 + pfMET).Pt();
			Phi_W = (muon1 + pfMET).Phi();

			TLorentzVector UW = -(pfMET + muon1);
			TLorentzVector BW = (muon1+pfMET);

			U1_W = (UW.Pt()) * (cos(UW.DeltaPhi(BW))) ;
			U2_W = (UW.Pt()) * (sin(UW.DeltaPhi(BW))) ;
//			U1_W = (UW.Pt()) * (sin(UW.Phi() - BW.Phi())) ;
//			U2_W = (UW.Pt()) * (cos(UW.Phi() - BW.Phi())) ;

		}

		//			std::cout<<Pt_W<<std::endl;
		//			std::cout<<"---------------"<<std::endl;

		//*******************************************************//

		//===========================================================================================//

		//*******************************************************//
		//*****************    At least 2 Mu   ******************//
		//*******************************************************//

		if (MuonCount>=2)
		{
			Pt_muon2 = MuonPt->at(v_idx_muon_final[1]);
			Phi_muon2 = MuonPhi->at(v_idx_muon_final[1]);
			Eta_muon2 = MuonEta->at(v_idx_muon_final[1]);
			precut_2muon = 1.0;

			muon2.SetPtEtaPhiM(Pt_muon2,Eta_muon2,Phi_muon2,0);

			deltaPhi_caloMETmuon2 = abs(caloMET.DeltaPhi(muon2));

			deltaPhi_muon1muon2 = abs(muon1.DeltaPhi(muon2));

			M_muon1muon2 = (muon1+muon2).M();

			deltaR_muon1muon2 = muon1.DeltaR(muon2);

			if (deltaR_muon1muon2 >.3) precut_muonDeltaR = 1.0;

			if (MuonCount==2)
			{
				precut_2muonexact_chargeproduct = (1.0 * (MuonCharge->at(v_idx_muon_final[0])) * (MuonCharge->at(v_idx_muon_final[1]) ));
			}

			TLorentzVector UZ = -(pfMET + muon1 + muon2);
			TLorentzVector BZ = (muon1+muon2);
//			U1_Z = (UZ.Pt()) * (sin(UZ.Phi() - BZ.Phi())) ;
//			U2_Z = (UZ.Pt()) * (cos(UZ.Phi() - BZ.Phi())) ;

			U1_Z = (UZ.Pt()) * (cos(UZ.DeltaPhi(BZ))) ;
			U2_Z = (UZ.Pt()) * (sin(UZ.DeltaPhi(BZ))) ;

			Pt_Z = (muon1 + muon2).Pt();
			Phi_Z = (muon1 + muon2).Phi();

		}

		if (MuonCount>=3)
		{
			Pt_muon3 = MuonPt->at(v_idx_muon_final[2]);
			//			Phi_muon3 = MuonPhi->at(v_idx_muon_final[2]);
			Eta_muon3 = MuonEta->at(v_idx_muon_final[2]);
			//			precut_2muon = 1.0;

			muon3.SetPtEtaPhiM(Pt_muon3,Eta_muon3,Phi_muon3,0);

			//			deltaPhi_caloMETmuon2 = abs(caloMET.DeltaPhi(muon2));

			//			deltaPhi_muon1muon2 = abs(muon1.DeltaPhi(muon2));

			M_muon1muon2 = (muon1+muon2).M();
			M_muon1muon3 = (muon1+muon3).M();
			M_muon2muon3 = (muon2+muon3).M();

			//			deltaR_muon1muon2 = muon1.DeltaR(muon2);

		}

		//*******************************************************//

		//===========================================================================================//

		//*******************************************************//
		//*****************    At least 1 Jet  ******************//
		//*******************************************************//

		if (JetCount>=1)
		{
			Pt_jet1 = CaloJetPt->at(v_idx_jet_final[0]);
			//			std::cout<<Pt_jet1<<std::endl;
			precut_1jet = 1.0;
			Phi_jet1 = CaloJetPhi->at(v_idx_jet_final[0]);
			Eta_jet1 = CaloJetEta->at(v_idx_jet_final[0]);

			jet1.SetPtEtaPhiM(Pt_jet1,Eta_jet1,Phi_jet1,0);

			deltaPhi_jet1caloMET = abs(caloMET.DeltaPhi(jet1));

			MT_jet1caloMET = TMass(Pt_jet1,MET_calo,deltaPhi_jet1caloMET);

			BDisc_jet1 = CaloJetTrackCountingHighEffBTag->at(v_idx_jet_final[0]);

		}

		//*******************************************************//

		//===========================================================================================//

		//*******************************************************//
		//*****************    At least 2 Jet  ******************//
		//*******************************************************//

		if (JetCount>=2)
		{
			Pt_jet2 = CaloJetPt->at(v_idx_jet_final[1]);
			precut_2jet = 1.0;
			Phi_jet2 = CaloJetPhi->at(v_idx_jet_final[1]);
			Eta_jet2 = CaloJetEta->at(v_idx_jet_final[1]);

			jet2.SetPtEtaPhiM(Pt_jet2,Eta_jet2,Phi_jet2,0);

			deltaPhi_jet2caloMET = abs(caloMET.DeltaPhi(jet2));

			deltaPhi_jet1jet2 = abs(jet1.DeltaPhi(jet2));

			MT_jet2caloMET = TMass(Pt_jet2,MET_calo,deltaPhi_jet1caloMET);

			M_jet1jet2 = (jet1 + jet2).M();

			deltaR_jet1jet2 = jet1.DeltaR(jet2);

			BDisc_jet2 = CaloJetTrackCountingHighEffBTag->at(v_idx_jet_final[1]);
		}

		//*******************************************************//

		//===========================================================================================//

		//*******************************************************//
		//*****************    1 Muon 1 Jet    ******************//
		//*******************************************************//

		if ((precut_1muon> .5) && (precut_1jet> .5))
		{
			deltaPhi_muon1jet1 = abs(muon1.DeltaPhi(jet1));
			M_muon1jet1 = (jet1 + muon1).M();
		}

		//*******************************************************//

		//===========================================================================================//

		//*******************************************************//
		//*****************    1 Muon 2 Jet    ******************//
		//*******************************************************//

		if ((precut_1muon> .5) && (precut_2jet> .5))
		{
			deltaPhi_muon1jet2 = abs(muon1.DeltaPhi(jet2));
			M_muon1jet2 = (jet2 + muon1).M();
			ST_calo_munu= Pt_muon1 + MET_calo + Pt_jet1 + Pt_jet2;
		}

		//*******************************************************//

		//===========================================================================================//

		//*******************************************************//
		//*****************    2 Muon 1 Jet    ******************//
		//*******************************************************//

		if ((precut_2muon> .5) && (precut_1jet> .5))
		{
			deltaPhi_muon2jet1 = abs(muon2.DeltaPhi(jet1));
			M_muon2jet1 = (jet1+muon2).M();
		}

		//*******************************************************//

		//===========================================================================================//

		//*******************************************************//
		//*****************    2 Muon 2 Jet    ******************//
		//*******************************************************//

		if ((precut_2muon> .5) && (precut_2jet> .5))
		{
			deltaPhi_muon2jet2 = abs(muon2.DeltaPhi(jet2));
			ST_calo= Pt_muon1 + Pt_muon2 + Pt_jet1 + Pt_jet2;
			M_muon2jet2 = (jet2 + muon2).M();

			M_AllParticles = (muon1+muon2+jet1+jet2).M();
		}

		//*******************************************************//

		//===========================================================================================//

		//		*******************************************************//
		//		*****************    At least 1 Mu   ******************//
		//		*******************************************************//

		if (MuonCount>=1)
		{
			deltaPhi_muon1pfMET = abs(pfMET.DeltaPhi(muon1));
			deltaPhi_muon1tcMET = abs(tcMET.DeltaPhi(muon1));
			MT_muon1pfMET = TMass(Pt_muon1,MET_pf,deltaPhi_muon1pfMET);
			MT_muon1tcMET = TMass(Pt_muon1,MET_tc,deltaPhi_muon1tcMET);

			minval_muon1pfMET = Pt_muon1;
			minval_muon1tcMET = Pt_muon1;

			if (MET_pf < Pt_muon1) minval_muon1caloMET = MET_pf;
			if (MET_tc < Pt_muon1) minval_muon1caloMET = MET_tc;

			MET_pf_prime = MET_pf;

			MT_muon1pfMET_prime_angle = TMass(Pt_muon1,MET_pf_prime,deltaPhi_muon1pfMET);

			if (deltaPhi_muon1pfMET < 3.1415926/2.0)
			{
				MET_pf_prime = MET_pf*sin(deltaPhi_muon1pfMET);
				MT_muon1pfMET_prime_angle = TMass(Pt_muon1,MET_pf_prime,3.1415926/2.0);
			}

			MT_muon1pfMET_prime = TMass(Pt_muon1,MET_pf_prime,deltaPhi_muon1pfMET);

		}

		//*******************************************************//

		//*******************************************************//
		//*****************    At least 1 PFJET  ****************//
		//*******************************************************//

		if (PFJetCount>=1)
		{
			Pt_pfjet1 = PFJetPt->at(v_idx_pfjet_final[0]);
			precut_1pfjet = 1.0;
			Phi_pfjet1 = PFJetPhi->at(v_idx_pfjet_final[0]);
			Eta_pfjet1 = PFJetEta->at(v_idx_pfjet_final[0]);

			pfjet1.SetPtEtaPhiM(Pt_pfjet1,Eta_pfjet1,Phi_pfjet1,0);

			deltaPhi_pfjet1pfMET = abs(pfMET.DeltaPhi(pfjet1));
			deltaPhi_pfjet1tcMET = abs(tcMET.DeltaPhi(pfjet1));

			MT_pfjet1pfMET = TMass(Pt_pfjet1,MET_pf,deltaPhi_pfjet1pfMET);
			MT_pfjet1tcMET = TMass(Pt_pfjet1,MET_tc,deltaPhi_pfjet1tcMET);

			BDisc_pfjet1 = PFJetTrackCountingHighEffBTag->at(v_idx_pfjet_final[0]);

			TLorentzVector pfjet1e;
			pfjet1e.SetPtEtaPhiM(Pt_pfjet1,Eta_pfjet1,Phi_pfjet1,PFJetEnergy->at(v_idx_pfjet_final[0]));
			M_pfjet1 = pfjet1e.Mag();
			PFJetNeutralMultiplicity_pfjet1= PFJetNeutralMultiplicity->at(v_idx_pfjet_final[0]);
			PFJetNeutralHadronEnergyFraction_pfjet1= PFJetNeutralHadronEnergyFraction->at(v_idx_pfjet_final[0]);
			PFJetNeutralEmEnergyFraction_pfjet1= PFJetNeutralEmEnergyFraction->at(v_idx_pfjet_final[0]);
			PFJetChargedMultiplicity_pfjet1= PFJetChargedMultiplicity->at(v_idx_pfjet_final[0]);
			PFJetChargedHadronEnergyFraction_pfjet1= PFJetChargedHadronEnergyFraction->at(v_idx_pfjet_final[0]);
			PFJetChargedEmEnergyFraction_pfjet1= PFJetChargedEmEnergyFraction->at(v_idx_pfjet_final[0]);

		}

		//*******************************************************//

		//===========================================================================================//

		//*******************************************************//
		//*****************    At least 2 PFJET  ****************//
		//*******************************************************//

		if (PFJetCount>=2)
		{
			Pt_pfjet2 = PFJetPt->at(v_idx_pfjet_final[1]);
			precut_2pfjet = 1.0;
			Phi_pfjet2 = PFJetPhi->at(v_idx_pfjet_final[1]);
			Eta_pfjet2 = PFJetEta->at(v_idx_pfjet_final[1]);

			pfjet2.SetPtEtaPhiM(Pt_pfjet2,Eta_pfjet2,Phi_pfjet2,0);

			deltaPhi_pfjet2pfMET = abs(pfMET.DeltaPhi(pfjet2));
			deltaPhi_pfjet2tcMET = abs(tcMET.DeltaPhi(pfjet2));

			deltaPhi_pfjet1pfjet2 = abs(pfjet1.DeltaPhi(pfjet2));

			MT_pfjet2pfMET = TMass(Pt_pfjet2,MET_pf,deltaPhi_pfjet2pfMET);
			MT_pfjet2tcMET = TMass(Pt_pfjet2,MET_tc,deltaPhi_pfjet2tcMET);

			M_pfjet1pfjet2 = (pfjet1 + pfjet2).M();

			deltaR_pfjet1pfjet2 = pfjet1.DeltaR(pfjet2);
			BDisc_pfjet2 = PFJetTrackCountingHighEffBTag->at(v_idx_pfjet_final[1]);

			TLorentzVector pfjet2e;
			pfjet2e.SetPtEtaPhiM(Pt_pfjet2,Eta_pfjet2,Phi_pfjet2,PFJetEnergy->at(v_idx_pfjet_final[1]));
			M_pfjet2 = pfjet2e.Mag();
			PFJetNeutralMultiplicity_pfjet2= PFJetNeutralMultiplicity->at(v_idx_pfjet_final[1]);
			PFJetNeutralHadronEnergyFraction_pfjet2= PFJetNeutralHadronEnergyFraction->at(v_idx_pfjet_final[1]);
			PFJetNeutralEmEnergyFraction_pfjet2= PFJetNeutralEmEnergyFraction->at(v_idx_pfjet_final[1]);
			PFJetChargedMultiplicity_pfjet2= PFJetChargedMultiplicity->at(v_idx_pfjet_final[1]);
			PFJetChargedHadronEnergyFraction_pfjet2= PFJetChargedHadronEnergyFraction->at(v_idx_pfjet_final[1]);
			PFJetChargedEmEnergyFraction_pfjet2= PFJetChargedEmEnergyFraction->at(v_idx_pfjet_final[1]);
		}

		//*******************************************************//

		//===========================================================================================//

		//*******************************************************//
		//*****************    1 Muon 1 Jet    ******************//
		//*******************************************************//

		if ((precut_1muon> .5) && (precut_1pfjet> .5))
		{
			deltaPhi_muon1pfjet1 = abs(muon1.DeltaPhi(pfjet1));
			M_muon1pfjet1 = (pfjet1 + muon1).M();
			MT_pfjet1muon1 = TMass(Pt_pfjet1,Pt_muon1,deltaPhi_muon1pfjet1);
		}

		//*******************************************************//

		//===========================================================================================//

		//*******************************************************//
		//*****************    1 Muon 2 Jet    ******************//
		//*******************************************************//

		if ((precut_1muon> .5) && (precut_2pfjet> .5))
		{
			deltaPhi_muon1pfjet2 = abs(muon1.DeltaPhi(pfjet2));
			M_muon1pfjet2 = (pfjet2 + muon1).M();
			ST_pf_munu= Pt_muon1 + MET_pf + Pt_pfjet1 + Pt_pfjet2;
			ST_tc_munu= Pt_muon1 + MET_tc + Pt_pfjet1 + Pt_pfjet2;
			MT_pfjet2muon1 = TMass(Pt_pfjet2,Pt_muon1,deltaPhi_muon1pfjet2);
		}

		//*******************************************************//

		//===========================================================================================//

		//*******************************************************//
		//*****************    2 Muon 1 Jet    ******************//
		//*******************************************************//

		if ((precut_2muon> .5) && (precut_1pfjet> .5))
		{
			deltaPhi_muon2pfjet1 = abs(muon2.DeltaPhi(pfjet1));
			M_muon2pfjet1 = (pfjet1+muon2).M();
		}

		//*******************************************************//

		//===========================================================================================//

		//*******************************************************//
		//*****************    2 Muon 2 Jet    ******************//
		//*******************************************************//

		if ((precut_2muon> .5) && (precut_2pfjet> .5))
		{
			deltaPhi_muon2pfjet2 = abs(muon2.DeltaPhi(pfjet2));
			ST_pf= Pt_muon1 + Pt_muon2 + Pt_pfjet1 + Pt_pfjet2;
			ST_tc= Pt_muon1 + Pt_muon2 + Pt_pfjet1 + Pt_pfjet2;
			M_muon2pfjet2 = (pfjet2 + muon2).M();

			M_AllpfParticles = (muon1+muon2+pfjet1+pfjet2).M();
		}

		//*******************************************************//


		tree->Fill();			 // FILL FINAL TREE

	}

	tree->Write();
	file1->Close();
}
