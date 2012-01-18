#define placeholder_cxx
#include "placeholder.h"
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
#include "TRandom3.h"
#include "JSONFilterFunction.h"
#include "ResidualModifier.h"

#define BRANCH(bname) Double_t bname = -99999.12345; tree->Branch(#bname,& bname," bname /D ");
#define VRESET(vname) vname = -99999.12345;

TRandom3* rr = new TRandom3();


Double_t JetRescaleFactor = 1.00;
Double_t MuonRescaleFactor = 1.00;
Double_t JetSmearFactor = 0.0;
Double_t MuonSmearFactor = 0.0;

Double_t TMass(Double_t Pt1, Double_t Pt2, Double_t DPhi12)
{
	return sqrt( 2*Pt2*Pt1*(1-cos(DPhi12)) );
}

Double_t ScaleObject(Double_t PT, Double_t fraction)
{
	return (PT*(fraction));
}

Double_t SmearObject(Double_t PT, Double_t fraction)
{
	return (rr->Gaus(PT,fraction*PT));
}

Double_t GetRecoGenJetScaleFactor(Double_t RecoPT,Double_t GenPT, Double_t SmearFactor)
{
	Double_t deltaPT = ((RecoPT-GenPT)*SmearFactor);
	return (RecoPT+deltaPT)/RecoPT;
}


TLorentzVector PropagatePTChangeToMET(Double_t MET, Double_t METPhi, Double_t PTCorr, Double_t PTOrig, Double_t Phi)
{
	Double_t yMET = MET*sin(METPhi) - ( (PTCorr - PTOrig)*sin(Phi)  );
	Double_t xMET = MET*cos(METPhi) - ( (PTCorr - PTOrig)*cos(Phi)  );
	Double_t metCorr =  sqrt(xMET*xMET + yMET*yMET);
	Double_t metPhiCorr = acos (xMET/metCorr);
	if (yMET<0) metPhiCorr *= -1;
	TLorentzVector vmetcorr;
	vmetcorr.SetPtEtaPhiM( metCorr,0,metPhiCorr,0 );
	return vmetcorr;
}


// Recoil Correction Function for U1
Double_t F_U1Prime(Double_t P)
{
	Double_t newU1 =+(0.444896)/(0.860121)*(0.766883)+(-0.808669)/(-0.834743)*(-0.789876)*(P)+(-0.00219386)/(-0.00292147)*(-0.00311338)*(pow(P,2.0));
	Double_t newsU1 =+(5.8243)/(4.67677)*(4.39298)+(0.0542917)/(0.0868557)*(0.0919195)*(P)+(0.000606564)/(0.000149318)*(0.000734456)*(pow(P,2.0));
	return gRandom->Gaus(newU1,newsU1);
}


// Recoil Correction Function for U1
Double_t F_U2Prime(Double_t P)
{
	Double_t newU2 =+(-0.257587)/(-0.0294369)*(-0.0447997)+(0.0318125)/(0.00367515)*(0.00493626)*(P)+(-0.00054509)/(-5.08201e-05)*(-0.000106641)*(pow(P,2.0));
	Double_t newsU2 =+(5.94468)/(4.80093)*(4.45511)+(0.00960053)/(0.0373637)*(0.063819)*(P)+(0.000780935)/(0.000569114)*(0.00042653)*(pow(P,2.0));
	return gRandom->Gaus(newU2,newsU2);
}

int CustomHeepID(double e_pt, double e_pt_real, double e_eta, bool e_ecaldriven , double e_dphi_sc, double e_deta_sc, double e_hoe, double e_sigmann, double e_e1x5_over_5x5, double e_e2x5_over_5x5, double e_em_had1iso , double e_had2iso, double e_trkiso, double e_losthits )
{
	int isgood = 1;

	if (e_pt_real<35.0) isgood = 0; // OK
	if (e_pt<35.0) isgood = 0; // OK
	//if (fabs(e_eta) > 1.442 && fabs(e_eta) < 1.560) isgood = 0;
	if (fabs(e_eta) > 2.50) isgood = 0; //OK
	if (!e_ecaldriven) isgood = 0; //OK
	if (fabs(e_dphi_sc) > 0.06) isgood = 0; //OK
	if (e_hoe > 0.05) isgood = 0; //OK
	if (e_losthits != 0) isgood = 0;
	//bool barrel = (fabs(e_eta) < 1.442);
	bool barrel = (fabs(e_eta) < 1.560); //OK
	bool endcap = (fabs(e_eta) > 1.560 && fabs(e_eta) < 2.5); //OK
	
	if (barrel)
	{
		if (fabs(e_deta_sc) > 0.005) isgood = 0; // OK
		if (( e_e1x5_over_5x5 > 0.83)&&( e_e2x5_over_5x5 > 0.94 )) isgood = 0; // OK
		if ( e_em_had1iso > ( 2.0 + 0.03*e_pt )) isgood = 0; //OK
		if (e_trkiso > 5) isgood = 0; //OK
	}
	
	if (endcap)
	{
		if (fabs(e_deta_sc)> 0.007) isgood = 0; //OK
		if (fabs(e_sigmann) > 0.03) isgood = 0; //OK
		if ((e_pt < 50.0) && ( e_em_had1iso >  2.5 )) isgood = 0; //OK
		if ((e_pt >= 50.0) && ( e_em_had1iso > ( 2.5 + 0.03*(e_pt-50.0) ))) isgood = 0; // OK
		//if ( e_had2iso > 0.5 ) isgood = 0;
		if (e_trkiso > 5.0) 	isgood = 0; // OK
	}
	
	
	return isgood;
	
	
}
			

// Boolean switches for Recoil and Smearing corrections, False by default.
bool DoRecoilCorrections = false;

void placeholder::Loop()
{

	//===================================================================================================
	//      MAKE TREE FOR PLACEHOLDER SIGNAL/BG TYPE AND DECLARE VARIABLES
	//===================================================================================================

	// Update output file
	TFile * file1 = new TFile("placeholder.root","RECREATE");
	// create tree for the signal or background type
	TTree *tree=new TTree("PhysicalVariables","PhysicalVariables");

	//*****************************************************************
	//         MUON AND CALOJET/CALOMET VARIABLES BELOW
	//*****************************************************************

	// Particle Counts
	BRANCH(MuonCount); BRANCH(EleCount); BRANCH(HEEPEleCount); BRANCH(PFJetCount); BRANCH(BpfJetCount);
	BRANCH(GlobalMuonCount); BRANCH(TrackerMuonCount);
	BRANCH(PFJetRawCount);   BRANCH(CaloJetRawCount);

	// Leading muon 1
	BRANCH(TrkD0_muon1);     BRANCH(NHits_muon1);   BRANCH(TrkDZ_muon1);   BRANCH(ChiSq_muon1);
	BRANCH(TrkIso_muon1); BRANCH(EcalIso_muon1); BRANCH(HcalIso_muon1); BRANCH(RelIso_muon1);
	BRANCH(Phi_muon1);    BRANCH(Eta_muon1);     BRANCH(Pt_muon1);      BRANCH(Charge_muon1);
	BRANCH(QOverPError_muon1); BRANCH(PhiError_muon1);    BRANCH(EtaError_muon1);     BRANCH(PtError_muon1); 
	BRANCH(TrackerIsoSumPT_muon1);

	// Leading muon 2
	BRANCH(TrkD0_muon2);     BRANCH(NHits_muon2);   BRANCH(TrkDZ_muon2);   BRANCH(ChiSq_muon2);
	BRANCH(TrkIso_muon2); BRANCH(EcalIso_muon2); BRANCH(HcalIso_muon2); BRANCH(RelIso_muon2);
	BRANCH(Phi_muon2);    BRANCH(Eta_muon2);     BRANCH(Pt_muon2);      BRANCH(Charge_muon2);
	BRANCH(QOverPError_muon2); BRANCH(PhiError_muon2);    BRANCH(EtaError_muon2);     BRANCH(PtError_muon2); 
	BRANCH(TrackerIsoSumPT_muon2);


	// PFJet 1
	BRANCH(Phi_pfjet1); BRANCH(Eta_pfjet1); BRANCH(Pt_pfjet1); BRANCH(BDisc_pfjet1);
	BRANCH(PFJetNeutralMultiplicity_pfjet1);         BRANCH(PFJetNeutralHadronEnergyFraction_pfjet1);
	BRANCH(PFJetNeutralEmEnergyFraction_pfjet1);     BRANCH(PFJetChargedMultiplicity_pfjet1);
	BRANCH(PFJetChargedHadronEnergyFraction_pfjet1); BRANCH(PFJetChargedEmEnergyFraction_pfjet1);
	BRANCH(PFJetTrackAssociatedVertex_pfjet1);

	// PFJet 2
	BRANCH(Phi_pfjet2); BRANCH(Eta_pfjet2); BRANCH(Pt_pfjet2); BRANCH(BDisc_pfjet2);
	BRANCH(PFJetNeutralMultiplicity_pfjet2);         BRANCH(PFJetNeutralHadronEnergyFraction_pfjet2);
	BRANCH(PFJetNeutralEmEnergyFraction_pfjet2);     BRANCH(PFJetChargedMultiplicity_pfjet2);
	BRANCH(PFJetChargedHadronEnergyFraction_pfjet2); BRANCH(PFJetChargedEmEnergyFraction_pfjet2);
	BRANCH(PFJetTrackAssociatedVertex_pfjet2);

	// Electron (If any)
	BRANCH(Pt_ele1);
	BRANCH(Eta_ele1);
	BRANCH(Phi_ele1);
	BRANCH(Pt_HEEPele1);
	BRANCH(Eta_HEEPele1);
	BRANCH(Phi_HEEPele1);


	// Event Information
	UInt_t run_number,event_number,ls_number;
	tree->Branch("event_number",&event_number,"event_number/i");
	tree->Branch("run_number",&run_number,"run_number/i");
	tree->Branch("ls_number",&ls_number,"ls_number/i");
	BRANCH(bx);	BRANCH(xsection);   BRANCH(weight);
	BRANCH(Events_AfterLJ); BRANCH(Events_Orig);
	BRANCH(N_Vertices);
	BRANCH(N_GoodVertices);
	BRANCH(weight_964pileup_gen); BRANCH(weight_pileup2fb); BRANCH(weight_pileup4p7fb); BRANCH(weight_pileup2011B); BRANCH(weight_pileup2011A); BRANCH(weight_pileup4p7fb_higgs);
	
	BRANCH(pass_HBHENoiseFilter); BRANCH(pass_isBPTX0); BRANCH(pass_EcalMaskedCellDRFilter); BRANCH(pass_passBeamHaloFilterLoose); 
	BRANCH(pass_passBeamHaloFilterTight); BRANCH(pass_CaloBoundaryDRFilter);


	// PFMET
	BRANCH(MET_pf); BRANCH(Phi_MET_pf);
	BRANCH(MET_lq); BRANCH(METRatio_pfcalo); BRANCH(METRatio_lqpf); BRANCH(METRatio_lqcalo);
	BRANCH(MET_pfsig);

	// Event Flags
	BRANCH(FailIDCaloThreshold); BRANCH(FailIDPFThreshold);

	// Delta Phi Variables
	BRANCH(deltaPhi_muon1muon2);  BRANCH(deltaPhi_pfjet1pfjet2);
	BRANCH(deltaPhi_muon1pfMET);  BRANCH(deltaPhi_muon2pfMET);
	BRANCH(deltaPhi_pfjet1pfMET); BRANCH(deltaPhi_pfjet2pfMET);
	BRANCH(deltaPhi_muon1pfjet1); BRANCH(deltaPhi_muon1pfjet2);
	BRANCH(deltaPhi_muon2pfjet1); BRANCH(deltaPhi_muon2pfjet2);
	BRANCH(deltaPhi_METClosestCaloJet);
	BRANCH(deltaPhi_METClosestPFJet);
	BRANCH(deltaPhi_METFurthestCaloJet);
	BRANCH(deltaPhi_METFurthestPFJet);
	BRANCH(deltaPhi_METClosestPT10CaloJet);
	BRANCH(deltaPhi_METClosestPT10PFJet);
	BRANCH(deltaPhi_METFurthestPT10CaloJet);
	BRANCH(deltaPhi_METFurthestPT10PFJet);

	// Delta R Variables
	BRANCH(deltaR_muon1muon2);  BRANCH(deltaR_pfjet1pfjet2);
	BRANCH(deltaR_muon1pfjet1); BRANCH(deltaR_muon1pfjet2);
	BRANCH(deltaR_muon2pfjet1); BRANCH(deltaR_muon2pfjet2);
	BRANCH(deltaR_muon1closestPFJet);
	BRANCH(deltaR_muon1HEEPele1);


	// Mass Combinations
	BRANCH(M_muon1muon2);  BRANCH(M_pfjet1pfjet2);
	BRANCH(M_muon1pfjet1); BRANCH(M_muon1pfjet2);
	BRANCH(M_muon2pfjet1); BRANCH(M_muon2pfjet2);
	BRANCH(M_muon1muon2pfjet1pfjet2);
	BRANCH(M_muon1pfjet1pfjet2); BRANCH(M_muon1muon2pfjet1);

	BRANCH(M_bestmupfjet1_mumu); BRANCH(M_bestmupfjet2_mumu);
	BRANCH(M_bestmupfjet_munu);
	BRANCH(M_muon1HEEPele1);
	BRANCH(M_mujetjet);
	BRANCH(M_AllCaloJet);	BRANCH(M_AllPFJet);
	BRANCH(Pt_AllCaloJet);	BRANCH(Pt_AllPFJet);
	BRANCH(MetDirComp_AllCaloJet);	BRANCH(MetDirComp_AllPFJet);
	BRANCH(MetDirCompOverMET_AllCaloJet);	BRANCH(MetDirCompOverMET_AllPFJet);
	BRANCH(JetMatchMuon1); BRANCH(JetMatchMuon2);
 
	// Transverse Mass Combinations
	BRANCH(MT_muon1pfMET);
	BRANCH(MT_pfjet1pfMET); BRANCH(MT_pfjet2pfMET);
	BRANCH(MT_muon1pfjet1); BRANCH(MT_muon1pfjet2);
	BRANCH(MT_muon2pfjet1); BRANCH(MT_muon2pfjet2);

	// ST Variables
	BRANCH(ST_pf_mumu); BRANCH(ST_pf_munu);
	BRANCH(ST_pf_hadronic); BRANCH(ST_calo_hadronic);
	BRANCH(ST_pf_emu);
	
	// Other Variables
	BRANCH(minval_muon1pfMET);
	BRANCH(Pt_Z);  BRANCH(Pt_W);
	BRANCH(Phi_Z); BRANCH(Phi_W);
	BRANCH(N_PileUpInteractions);
	BRANCH(N_WeightedPileUpInteractions);

	// Generator Level Variables
	BRANCH(Pt_genjet1);     BRANCH(Pt_genjet2);
	BRANCH(Pt_genmuon1);    BRANCH(Pt_genmuon2);
	BRANCH(Phi_genmuon1);   BRANCH(Phi_genmuon2);
	BRANCH(Eta_genmuon1);   BRANCH(Eta_genmuon2);
	BRANCH(Pt_genMET);      BRANCH(Phi_genMET);    BRANCH(Eta_genMET);
	BRANCH(Pt_genneutrino); BRANCH(Phi_genneutrino); BRANCH(Eta_genneutrino);
	BRANCH(MT_genmuon1genMET);
	BRANCH(Pt_Z_gen);       BRANCH(Pt_W_gen);
	BRANCH(Phi_Z_gen);      BRANCH(Phi_W_gen);
	BRANCH(deltaPhi_genmuon1genMET);  
	BRANCH(deltaPhi_genjet1genMET); BRANCH(deltaPhi_genjet2genMET);
	BRANCH(ST_gen_mumu); BRANCH(ST_gen_munu);


	// Recoil variables
	BRANCH(U1_Z_gen); BRANCH(U2_Z_gen);
	BRANCH(U1_W_gen); BRANCH(U2_W_gen);
	BRANCH(U1_Z);     BRANCH(U2_Z);
	BRANCH(U1_W);     BRANCH(U2_W);
	BRANCH(UdotMu);   BRANCH(UdotMu_overmu);
	
	// Extra Discriminating Variables
	BRANCH(RangeMass_BestLQCombo);
	BRANCH(RangeTransverseMass_BestLQCombo);
	BRANCH(CenterMass_BestLQCombo);
	BRANCH(CenterTransverseMass_BestLQCombo);
	BRANCH(RangeCenterMassRatio_BestLQCombo);
	BRANCH(RangeCenterTransverseMassRatio_BestLQCombo);
	BRANCH(LowestMass_BestLQCombo);
	BRANCH(AverageMass_BestLQCombo);

	// Additions for E-Mu Selection

	BRANCH(LowestMass_BestLQCombo_emuselection);
	BRANCH(AverageMass_BestLQCombo_emuselection);
	

	BRANCH(M_HEEPele1pfjet1_emuselection); BRANCH(M_HEEPele1pfjet2_emuselection);
	BRANCH(M_bestmuORelepfjet1_mumu_emuselection); BRANCH(M_bestmuORelepfjet2_mumu_emuselection);

	
	
	// Trigger
	BRANCH(LowestUnprescaledTrigger); BRANCH(Closest40UnprescaledTrigger);
	BRANCH(LowestUnprescaledTriggerPass); BRANCH(Closest40UnprescaledTriggerPass);
	BRANCH(HLTIsoMu24Pass);
	BRANCH(HLTMu40TriggerPass);

	//===================================================================================================
	//===================================================================================================

	//===================================================================================================
	//        SETUP WITH SOME TEMPLATE INPUTS AND THRESHOLDS
	//===================================================================================================

	// "desired_luminosity" is a PlaceHolder that gets replaced from the python template replicator
	Double_t lumi=desired_luminosity;

	// PlaceHolder, values stored in bookkeeping/NTupleInfo.csv
	Events_Orig = Numberofevents;

	// Another placeHolder. Needed because recoil corrections only get applied to W MC.
	bool IsW = IsItWMC;

	xsection = crosssection;	 // Another PlaceHolder for the cross sections in bookkeeping/NTupleInfo.csv

	//===================================================================================================
	//===================================================================================================

	//===================================================================================================
	//           LOOP OVER ENTRIES AND MAKE MAIN CALCULATIONS
	//===================================================================================================

	if (fChain == 0) return;	 //check for correctly assigned chain from h file

	Long64_t nentries = fChain->GetEntriesFast();
	Long64_t nbytes = 0, nb = 0;

	//nentries=10000;  /// TEST>>>>>> COMMENT THIS ALWAYS
	for (Long64_t jentry=0; jentry<nentries;jentry++)
	{
		Long64_t ientry = LoadTree(jentry);
		if (ientry < 0) break;
		nb = fChain->GetEntry(jentry);   nbytes += nb;

		//if (jentry>5) break;  // comment this!!! testing only !

		// Important Event Informations
		run_number = run;
		event_number = event;
		ls_number = ls;
		bx = bunch;
		float extraweight = 1.0;
		if (!isData) extraweight = Weight;
		
		weight = extraweight*lumi*xsection/Events_Orig;

		//========================     JSON   Conditions   ================================//

		if (isData)
		{
			bool KeepEvent = PassFilter(run, ls);
			if (!KeepEvent) continue;
		}
		//========================     Vertex Conditions   ================================//

		if ( isBeamScraping ) continue;

		bool vtxFound = false;
		N_GoodVertices = 0.0;
		for(unsigned int ivtx = 0; ivtx != VertexZ->size(); ++ivtx)
		{
			if ( VertexIsFake->at(ivtx) == true ) continue;
			if ( VertexNDF->at(ivtx) <= 4.0 ) continue;
			if ( TMath::Abs(VertexZ->at(ivtx)) > 24.0 ) continue;
			if ( TMath::Abs(VertexRho->at(ivtx)) >= 2.0 ) continue;
			vtxFound = true;
			N_GoodVertices = N_GoodVertices + 1.0;
		}
		if ( !vtxFound ) continue;

		N_Vertices = 1.0*(VertexZ->size());
		
		pass_HBHENoiseFilter =1.0*passHBHENoiseFilter;
		pass_isBPTX0 = 1.0*isBPTX0 ; 
		pass_EcalMaskedCellDRFilter = 1.0*passEcalMaskedCellDRFilter ; 
		pass_CaloBoundaryDRFilter = 1.0*passCaloBoundaryDRFilter ; 
		pass_passBeamHaloFilterLoose = 1.0*passBeamHaloFilterLoose ; 
		pass_passBeamHaloFilterTight = 1.0*passBeamHaloFilterTight ;

		
		
		//========================     PileUp Methodology   ================================//
		
		
		N_PileUpInteractions = 0.0;
		N_WeightedPileUpInteractions = 0.0;

		if (!isData)
		{
			for(unsigned int iPU = 0; iPU != PileUpInteractions->size(); ++iPU)
			{
				if (TMath::Abs(PileUpOriginBX->at(iPU)) <= 1) N_WeightedPileUpInteractions += (1.0*(PileUpInteractions->at(iPU)))/3.0;
				if (TMath::Abs(PileUpOriginBX->at(iPU)) == 0) N_PileUpInteractions += (1.0*(PileUpInteractions->at(iPU)));
			}	
		}
		
		
		weight_pileup2fb = weight;
		
		weight_pileup4p7fb = weight;
		weight_pileup4p7fb_higgs = weight;

		weight_pileup2011A = weight;
		
		weight_pileup2011B = weight;

		if ((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5))    weight_pileup2fb *=  (0.0752233034121);
		if ((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5))     weight_pileup2fb *=  (0.361994702942);
		if ((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5))     weight_pileup2fb *=  (0.787119271271);
		if ((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5))     weight_pileup2fb *=  (1.31779962348);
		if ((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5))     weight_pileup2fb *=  (1.76293927848);
		if ((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5))     weight_pileup2fb *=  (1.99059826007);
		if ((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5))     weight_pileup2fb *=  (2.00731349758);
		if ((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5))     weight_pileup2fb *=  (1.82730847106);
		if ((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5))     weight_pileup2fb *=  (1.56802352509);
		if ((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5))     weight_pileup2fb *=  (1.26852456276);
		if ((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5))    weight_pileup2fb *=  (0.993808726427);
		if ((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5))   weight_pileup2fb *=  (0.760786688881);
		if ((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5))   weight_pileup2fb *=  (0.566015549542);
		if ((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5))   weight_pileup2fb *=  (0.41722578577);
		if ((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5))   weight_pileup2fb *=  (0.303388545407);
		if ((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5))   weight_pileup2fb *=  (0.220634364549);
		if ((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5))   weight_pileup2fb *=  (0.155308189438);
		if ((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5))   weight_pileup2fb *=  (0.110585960196);
		if ((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5))   weight_pileup2fb *=  (0.0776646451932);
		if ((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5))   weight_pileup2fb *=  (0.0543492223545);
		if ((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5))   weight_pileup2fb *=  (0.037244740125);
		if ((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5))   weight_pileup2fb *=  (0.0259826507587);
		if ((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5))   weight_pileup2fb *=  (0.0175412449088);
		if ((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5))   weight_pileup2fb *=  (0.0118325534711);
		if (N_PileUpInteractions > 23.5)                                   weight_pileup2fb *=  (0.00);

		
		if ((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)) weight_pileup4p7fb *=(0.0196731565572);
		if ((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)) weight_pileup4p7fb *=(0.195399330292);
		if ((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)) weight_pileup4p7fb *=(0.430966978677);
		if ((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)) weight_pileup4p7fb *=(0.73646462398);
		if ((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)) weight_pileup4p7fb *=(1.02418311439);
		if ((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)) weight_pileup4p7fb *=(1.2377627943);
		if ((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)) weight_pileup4p7fb *=(1.36607528129);
		if ((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)) weight_pileup4p7fb *=(1.42406461192);
		if ((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)) weight_pileup4p7fb *=(1.44293126093);
		if ((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)) weight_pileup4p7fb *=(1.44522180871);
		if ((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)) weight_pileup4p7fb *=(1.44680390895);
		if ((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)) weight_pileup4p7fb *=(1.45540561707);
		if ((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)) weight_pileup4p7fb *=(1.47236035231);
		if ((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)) weight_pileup4p7fb *=(1.49354734691);
		if ((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)) weight_pileup4p7fb *=(1.52226051225);
		if ((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)) weight_pileup4p7fb *=(1.54763397975);
		if ((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)) weight_pileup4p7fb *=(1.56834698994);
		if ((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)) weight_pileup4p7fb *=(1.58085292349);
		if ((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)) weight_pileup4p7fb *=(1.58087980016);
		if ((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)) weight_pileup4p7fb *=(1.57063876111);
		if ((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)) weight_pileup4p7fb *=(1.54770541788);
		if ((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)) weight_pileup4p7fb *=(1.50322376245);
		if ((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)) weight_pileup4p7fb *=(1.45081762123);
		if ((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)) weight_pileup4p7fb *=(1.39085977185);
		if ((N_PileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)) weight_pileup4p7fb *=(1.32050731802);
		if ((N_PileUpInteractions > 24.5)*(N_PileUpInteractions < 25.5)) weight_pileup4p7fb *=(1.24011037359);
		if ((N_PileUpInteractions > 25.5)*(N_PileUpInteractions < 26.5)) weight_pileup4p7fb *=(1.15924512432);
		if ((N_PileUpInteractions > 26.5)*(N_PileUpInteractions < 27.5)) weight_pileup4p7fb *=(1.06193569458);
		if ((N_PileUpInteractions > 27.5)*(N_PileUpInteractions < 28.5)) weight_pileup4p7fb *=(0.978045170078);
		if ((N_PileUpInteractions > 28.5)*(N_PileUpInteractions < 29.5)) weight_pileup4p7fb *=(0.905247484036);
		if ((N_PileUpInteractions > 29.5)*(N_PileUpInteractions < 30.5)) weight_pileup4p7fb *=(0.815564522288);
		if ((N_PileUpInteractions > 30.5)*(N_PileUpInteractions < 31.5)) weight_pileup4p7fb *=(0.721687664425);
		if ((N_PileUpInteractions > 31.5)*(N_PileUpInteractions < 32.5)) weight_pileup4p7fb *=(0.641765904129);
		if ((N_PileUpInteractions > 32.5)*(N_PileUpInteractions < 33.5)) weight_pileup4p7fb *=(0.598173871387);
		if ((N_PileUpInteractions > 33.5)*(N_PileUpInteractions < 34.5)) weight_pileup4p7fb *=(1.02679374255);
		if (N_PileUpInteractions > 34.5) weight_pileup4p7fb *= 0.0;

		if ((N_PileUpInteractions>-0.5)*(N_PileUpInteractions<0.5)) weight_pileup4p7fb_higgs *= (0.014303450 );
		if ((N_PileUpInteractions>0.5)*(N_PileUpInteractions<1.5)) weight_pileup4p7fb_higgs *= (0.148914600 );
		if ((N_PileUpInteractions>1.5)*(N_PileUpInteractions<2.5)) weight_pileup4p7fb_higgs *= (0.342742300 );
		if ((N_PileUpInteractions>2.5)*(N_PileUpInteractions<3.5)) weight_pileup4p7fb_higgs *= (0.610077800 );
		if ((N_PileUpInteractions>3.5)*(N_PileUpInteractions<4.5)) weight_pileup4p7fb_higgs *= (0.881386800 );
		if ((N_PileUpInteractions>4.5)*(N_PileUpInteractions<5.5)) weight_pileup4p7fb_higgs *= (1.102893000 );
		if ((N_PileUpInteractions>5.5)*(N_PileUpInteractions<6.5)) weight_pileup4p7fb_higgs *= (1.255616000 );
		if ((N_PileUpInteractions>6.5)*(N_PileUpInteractions<7.5)) weight_pileup4p7fb_higgs *= (1.345269000 );
		if ((N_PileUpInteractions>7.5)*(N_PileUpInteractions<8.5)) weight_pileup4p7fb_higgs *= (1.396842000 );
		if ((N_PileUpInteractions>8.5)*(N_PileUpInteractions<9.5)) weight_pileup4p7fb_higgs *= (1.431426000 );
		if ((N_PileUpInteractions>9.5)*(N_PileUpInteractions<10.5)) weight_pileup4p7fb_higgs *= (1.466321000 );
		if ((N_PileUpInteractions>10.5)*(N_PileUpInteractions<11.5)) weight_pileup4p7fb_higgs *= (1.511987000 );
		if ((N_PileUpInteractions>11.5)*(N_PileUpInteractions<12.5)) weight_pileup4p7fb_higgs *= (1.572500000 );
		if ((N_PileUpInteractions>12.5)*(N_PileUpInteractions<13.5)) weight_pileup4p7fb_higgs *= (1.645584000 );
		if ((N_PileUpInteractions>13.5)*(N_PileUpInteractions<14.5)) weight_pileup4p7fb_higgs *= (1.736351000 );
		if ((N_PileUpInteractions>14.5)*(N_PileUpInteractions<15.5)) weight_pileup4p7fb_higgs *= (1.833339000 );
		if ((N_PileUpInteractions>15.5)*(N_PileUpInteractions<16.5)) weight_pileup4p7fb_higgs *= (1.934649000 );
		if ((N_PileUpInteractions>16.5)*(N_PileUpInteractions<17.5)) weight_pileup4p7fb_higgs *= (2.034955000 );
		if ((N_PileUpInteractions>17.5)*(N_PileUpInteractions<18.5)) weight_pileup4p7fb_higgs *= (2.127016000 );
		if ((N_PileUpInteractions>18.5)*(N_PileUpInteractions<19.5)) weight_pileup4p7fb_higgs *= (2.211426000 );
		if ((N_PileUpInteractions>19.5)*(N_PileUpInteractions<20.5)) weight_pileup4p7fb_higgs *= (2.282289000 );
		if ((N_PileUpInteractions>20.5)*(N_PileUpInteractions<21.5)) weight_pileup4p7fb_higgs *= (2.322883000 );
		if ((N_PileUpInteractions>21.5)*(N_PileUpInteractions<22.5)) weight_pileup4p7fb_higgs *= (2.350057000 );
		if ((N_PileUpInteractions>22.5)*(N_PileUpInteractions<23.5)) weight_pileup4p7fb_higgs *= (2.361952000 );
		if ((N_PileUpInteractions>23.5)*(N_PileUpInteractions<24.5)) weight_pileup4p7fb_higgs *= (2.350979000 );
		if ((N_PileUpInteractions>24.5)*(N_PileUpInteractions<25.5)) weight_pileup4p7fb_higgs *= (2.314393000 );
		if ((N_PileUpInteractions>25.5)*(N_PileUpInteractions<26.5)) weight_pileup4p7fb_higgs *= (2.267422000 );
		if ((N_PileUpInteractions>26.5)*(N_PileUpInteractions<27.5)) weight_pileup4p7fb_higgs *= (2.176294000 );
		if ((N_PileUpInteractions>27.5)*(N_PileUpInteractions<28.5)) weight_pileup4p7fb_higgs *= (2.099417000 );
		if ((N_PileUpInteractions>28.5)*(N_PileUpInteractions<29.5)) weight_pileup4p7fb_higgs *= (2.034581000 );
		if ((N_PileUpInteractions>29.5)*(N_PileUpInteractions<30.5)) weight_pileup4p7fb_higgs *= (1.918498000 );
		if ((N_PileUpInteractions>30.5)*(N_PileUpInteractions<31.5)) weight_pileup4p7fb_higgs *= (1.776173000 );
		if ((N_PileUpInteractions>31.5)*(N_PileUpInteractions<32.5)) weight_pileup4p7fb_higgs *= (1.651888000 );
		if ((N_PileUpInteractions>32.5)*(N_PileUpInteractions<33.5)) weight_pileup4p7fb_higgs *= (1.609676000 );
		if ((N_PileUpInteractions>33.5)*(N_PileUpInteractions<34.5)) weight_pileup4p7fb_higgs *= (1.470914000 );
		if (N_PileUpInteractions>34.5) weight_pileup4p7fb_higgs *= 0.000000000 ;

		if ((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)) weight_pileup2011B *=(0.00131573357575);
		if ((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)) weight_pileup2011B *=(0.0198727041317);
		if ((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)) weight_pileup2011B *=(0.0661623409037);
		if ((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)) weight_pileup2011B *=(0.166388520711);
		if ((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)) weight_pileup2011B *=(0.330422419256);
		if ((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)) weight_pileup2011B *=(0.551853005828);
		if ((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)) weight_pileup2011B *=(0.812401387851);
		if ((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)) weight_pileup2011B *=(1.0876898499);
		if ((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)) weight_pileup2011B *=(1.36112666526);
		if ((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)) weight_pileup2011B *=(1.61986239723);
		if ((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)) weight_pileup2011B *=(1.85857471348);
		if ((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)) weight_pileup2011B *=(2.07583022795);
		if ((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)) weight_pileup2011B *=(2.27073458079);
		if ((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)) weight_pileup2011B *=(2.43879630527);
		if ((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)) weight_pileup2011B *=(2.58972279802);
		if ((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)) weight_pileup2011B *=(2.7104762223);
		if ((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)) weight_pileup2011B *=(2.80323038109);
		if ((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)) weight_pileup2011B *=(2.86580045174);
		if ((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)) weight_pileup2011B *=(2.89395216121);
		if ((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)) weight_pileup2011B *=(2.8945268421);
		if ((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)) weight_pileup2011B *=(2.86535465266);
		if ((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)) weight_pileup2011B *=(2.79167002202);
		if ((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)) weight_pileup2011B *=(2.70003386131);
		if ((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)) weight_pileup2011B *=(2.59214839811);
		if ((N_PileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)) weight_pileup2011B *=(2.46339776265);
		if ((N_PileUpInteractions > 24.5)*(N_PileUpInteractions < 25.5)) weight_pileup2011B *=(2.31490544385);
		if ((N_PileUpInteractions > 25.5)*(N_PileUpInteractions < 26.5)) weight_pileup2011B *=(2.1648847143);
		if ((N_PileUpInteractions > 26.5)*(N_PileUpInteractions < 27.5)) weight_pileup2011B *=(1.9837396241);
		if ((N_PileUpInteractions > 27.5)*(N_PileUpInteractions < 28.5)) weight_pileup2011B *=(1.82737557193);
		if ((N_PileUpInteractions > 28.5)*(N_PileUpInteractions < 29.5)) weight_pileup2011B *=(1.69157837089);
		if ((N_PileUpInteractions > 29.5)*(N_PileUpInteractions < 30.5)) weight_pileup2011B *=(1.52412087763);
		if ((N_PileUpInteractions > 30.5)*(N_PileUpInteractions < 31.5)) weight_pileup2011B *=(1.34875616702);
		if ((N_PileUpInteractions > 31.5)*(N_PileUpInteractions < 32.5)) weight_pileup2011B *=(1.19943409544);
		if ((N_PileUpInteractions > 32.5)*(N_PileUpInteractions < 33.5)) weight_pileup2011B *=(1.11798841681);
		if ((N_PileUpInteractions > 33.5)*(N_PileUpInteractions < 34.5)) weight_pileup2011B *=(1.91912739641);
		if (N_PileUpInteractions > 34.5) weight_pileup2011B *= 0.0;

		if ((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)) weight_pileup2011A *=(0.0462294709045);
		if ((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)) weight_pileup2011A *=(0.449017084862);
		if ((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)) weight_pileup2011A *=(0.95496408116);
		if ((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)) weight_pileup2011A *=(1.54742236648);
		if ((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)) weight_pileup2011A *=(1.99350537074);
		if ((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)) weight_pileup2011A *=(2.16591787484);
		if ((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)) weight_pileup2011A *=(2.07253064588);
		if ((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)) weight_pileup2011A *=(1.79716874247);
		if ((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)) weight_pileup2011A *=(1.44879640373);
		if ((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)) weight_pileup2011A *=(1.10390353315);
		if ((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)) weight_pileup2011A *=(0.805940525344);
		if ((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)) weight_pileup2011A *=(0.56963353603);
		if ((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)) weight_pileup2011A *=(0.392561321337);
		if ((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)) weight_pileup2011A *=(0.264739490683);
		if ((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)) weight_pileup2011A *=(0.176134312968);
		if ((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)) weight_pileup2011A *=(0.115357340197);
		if ((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)) weight_pileup2011A *=(0.074618085727);
		if ((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)) weight_pileup2011A *=(0.047710687865);
		if ((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)) weight_pileup2011A *=(0.0301416687552);
		if ((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)) weight_pileup2011A *=(0.0188683583314);
		if ((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)) weight_pileup2011A *=(0.011694470133);
		if ((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)) weight_pileup2011A *=(0.00713547685162);
		if ((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)) weight_pileup2011A *=(0.00432221446709);
		if ((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)) weight_pileup2011A *=(0.00259823843652);
		if ((N_PileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)) weight_pileup2011A *=(0.00154531071684);
		if ((N_PileUpInteractions > 24.5)*(N_PileUpInteractions < 25.5)) weight_pileup2011A *=(0.00090805400071);
		if ((N_PileUpInteractions > 25.5)*(N_PileUpInteractions < 26.5)) weight_pileup2011A *=(0.0005303976563);
		if ((N_PileUpInteractions > 26.5)*(N_PileUpInteractions < 27.5)) weight_pileup2011A *=(0.000303095137964);
		if ((N_PileUpInteractions > 27.5)*(N_PileUpInteractions < 28.5)) weight_pileup2011A *=(0.00017379704299);
		if ((N_PileUpInteractions > 28.5)*(N_PileUpInteractions < 29.5)) weight_pileup2011A *=(9.99256986151e-05);
		if ((N_PileUpInteractions > 29.5)*(N_PileUpInteractions < 30.5)) weight_pileup2011A *=(5.57817765096e-05);
		if ((N_PileUpInteractions > 30.5)*(N_PileUpInteractions < 31.5)) weight_pileup2011A *=(3.04991209629e-05);
		if ((N_PileUpInteractions > 31.5)*(N_PileUpInteractions < 32.5)) weight_pileup2011A *=(1.67068817976e-05);
		if ((N_PileUpInteractions > 32.5)*(N_PileUpInteractions < 33.5)) weight_pileup2011A *=(9.56164451078e-06);
		if ((N_PileUpInteractions > 33.5)*(N_PileUpInteractions < 34.5)) weight_pileup2011A *=(7.31897654042e-06);
		if (N_PileUpInteractions > 34.5) weight_pileup2011A *= 0.0;



		//========================     Trigger Scanning  ================================//

		string hltmu ("HLT_Mu");
		string hltisomu ("HLT_IsoMu24");
		string eta2p1 ("eta2p1");
		string hltmu40 ("HLT_Mu40_v");
		string hltmu40eta2p1 ("HLT_Mu40_eta2p1_v");

		LowestUnprescaledTrigger = -1.;
		LowestUnprescaledTriggerPass = -1.;
		Closest40UnprescaledTrigger = -1.;
		Closest40UnprescaledTrigger = -1.;
		HLTMu40TriggerPass = -1.;
		
		
		vector <double> SingleMuThresholds;
		vector <int> SingleMuPrescales;
		vector <int> SingleMuPasses;

		HLTIsoMu24Pass = 0;
		for(unsigned int iHLT = 0; iHLT != HLTInsideDatasetTriggerNames->size(); ++iHLT)
		{
			string thishlt = HLTInsideDatasetTriggerNames->at(iHLT);
			
			bool isSingleMuTrigger = (thishlt.compare(0,11,hltisomu)==0) && (thishlt.length()>7) && (thishlt.length()<19);
			if (!isSingleMuTrigger) continue;			
			//std::cout<<thishlt<<"   "<<HLTInsideDatasetTriggerPrescales->at(iHLT)<<std::endl;
			HLTIsoMu24Pass = HLTInsideDatasetTriggerDecisions->at(iHLT);

		}
		for(unsigned int iHLT = 0; iHLT != HLTInsideDatasetTriggerNames->size(); ++iHLT)
		{
			string thishlt = HLTInsideDatasetTriggerNames->at(iHLT);
			bool isSingleMuTrigger = (thishlt.compare(0,6,hltmu)==0) && (thishlt.length()>7) && (thishlt.length()<20);
			if (!isSingleMuTrigger) continue;

			string onesplace,tensplace;	
			onesplace = thishlt[7];
			tensplace = thishlt[6];
			bool notrigger = (onesplace=="_" || tensplace=="_");
			if (notrigger) continue;
			
			std::string thresh = tensplace+onesplace+".0";
			double triggervalue  = ::atof(thresh.c_str());
			SingleMuThresholds.push_back(triggervalue);
			SingleMuPrescales.push_back(HLTInsideDatasetTriggerPrescales->at(iHLT));
			SingleMuPasses.push_back(HLTInsideDatasetTriggerDecisions->at(iHLT));
			
			if ((!(thishlt.compare(0,10,hltmu40)==0))&&(!(thishlt.compare(0,17,hltmu40eta2p1)==0))) continue;
			
			if (( HLTInsideDatasetTriggerPrescales->at(iHLT) == 1) && HLTMu40TriggerPass < 1.0) HLTMu40TriggerPass = HLTInsideDatasetTriggerDecisions->at(iHLT);
			
		}
		
		for(unsigned int iHLTmu = 0; iHLTmu !=SingleMuThresholds.size(); ++iHLTmu)
		{
			
			if (LowestUnprescaledTrigger < 0 && SingleMuPrescales[iHLTmu] ==1) 
			{
				LowestUnprescaledTriggerPass = 1.0*SingleMuPasses[iHLTmu];
				LowestUnprescaledTrigger = 1.0*SingleMuThresholds[iHLTmu];
			}
			if (SingleMuPrescales[iHLTmu] ==1 && SingleMuThresholds[iHLTmu] < 40.01)
			{
				Closest40UnprescaledTrigger = 1.0*SingleMuThresholds[iHLTmu];
				Closest40UnprescaledTriggerPass = 1.0*SingleMuPasses[iHLTmu];
			}
		}
		//std::cout<<LowestUnprescaledTriggerPass<<"  "<<LowestUnprescaledTrigger<<"              "<<Closest40UnprescaledTrigger<<"  "<<Closest40UnprescaledTriggerPass<<std::endl;
		
		
		//========================     Jet Rescaling / Smearing Sequence   ================================//

		TLorentzVector JetAdjustedMET;
		JetAdjustedMET.SetPtEtaPhiM(PFMET->at(0),0.0,PFMETPhi->at(0),0);
		//std::cout<<PFMET->at(0)<<"  "<<(*PFMET)[0]<<"      "<<PFMETPhi->at(0)<<"  "<<(*PFMETPhi)[0]<<std::endl;
		//std::cout<<(*PFJetPt)[0]<<"  "<<(*PFJetPtRaw)[0]<<std::endl;
		if (!isData)
		{
			for(unsigned int ijet = 0; ijet < PFJetPt->size(); ++ijet)
			{
			(*PFJetPt)[ijet]  = (*PFJetPt)[ijet];// * PFJetL1OffsetJEC->at(ijet)/PFJetL1FastJetJEC->at(ijet);
			}
		}

		
		if (!isData)
		{
			for(unsigned int ijet = 0; ijet < PFJetPt->size(); ++ijet)
			{
				if (PFJetPt->at(ijet) < 25.0) continue;
				if (PFJetPassLooseID->at(ijet) != 1) continue;		
				if ( fabs(PFJetEta->at(ijet)) > 3.0 ) continue;
	
				bool consider = true;
				TLorentzVector ThisPFJet;
				Double_t JetLepDR;
				ThisPFJet.SetPtEtaPhiM((*PFJetPt)[ijet],(*PFJetEta)[ijet],(*PFJetPhi)[ijet],0);

				for(unsigned int imuon = 0; imuon < MuonPt->size(); ++imuon)
				{
					TLorentzVector ThisLepton;	
					ThisLepton.SetPtEtaPhiM(MuonPt->at(imuon),MuonEta->at(imuon), MuonPhi->at(imuon),0.0);
					JetLepDR = ThisLepton.DeltaR(ThisPFJet);
					if (JetLepDR < .2) consider = false;
				}
				for(unsigned int iele = 0; iele < ElectronPt->size(); ++iele)
				{
					TLorentzVector ThisLepton;	
					ThisLepton.SetPtEtaPhiM(ElectronPt->at(iele),ElectronEta->at(iele),ElectronPhi->at(iele),0.0);
					JetLepDR = ThisLepton.DeltaR(ThisPFJet);
					if (JetLepDR < .2) consider = false;
				}
				
				if (!consider) continue;
				double NewJetRescalingFactor = 1.0+NewJesUncertainty((JetRescaleFactor - 1.0), (*PFJetPtRaw)[ijet], (*PFJetEta)[ijet]);
				if (JetRescaleFactor < 1.0) NewJetRescalingFactor = 2.0 - NewJetRescalingFactor;
				
				
				double NewJetPT = (*PFJetPt)[ijet];
				double NewJetETA = (*PFJetEta)[ijet];

				if (JetRescaleFactor != 1.00) NewJetPT = NewJetPT + ((ScaleObject((*PFJetPtRaw)[ijet],NewJetRescalingFactor)) - ((*PFJetPtRaw)[ijet])) ; 
				
			
				int closestgenjet = -1;
				Double_t SmallestDeltaR = 9999.9999;
				Double_t ClosestGenJetPT = 99999.9999;
				for(unsigned int igenjet = 0; igenjet != GenJetPt->size(); ++igenjet)
				{
					TLorentzVector thisGenJet;
					thisGenJet.SetPtEtaPhiM(GenJetPt->at(igenjet),GenJetEta->at(igenjet),GenJetPhi->at(igenjet),0);
					Double_t ThisGenJetDR = fabs((thisGenJet).DeltaR(ThisPFJet));
					if (ThisGenJetDR<SmallestDeltaR) 
					{
						SmallestDeltaR = ThisGenJetDR;
						closestgenjet = igenjet;
						ClosestGenJetPT = GenJetPt->at(igenjet);
					}
				}
			
				Double_t Standard_rescale = 0.0;
				if (SmallestDeltaR<0.5) Standard_rescale = 0.1;
				//if ((SmallestDeltaR<0.5)&&(ijet==0)) std::cout<<ClosestGenJetPT<<std::endl;
				//if ((SmallestDeltaR<0.5)&&(ijet==0)) difreg += ((ClosestGenJetPT - (PFJetPt->at(ijet)))*(ClosestGenJetPT - (PFJetPt->at(ijet))));
				//if ((SmallestDeltaR<0.5)&&(ijet==0)) difraw += ((ClosestGenJetPT - (PFJetPtRaw->at(ijet)))*(ClosestGenJetPT - (PFJetPtRaw->at(ijet))));

				//if ((SmallestDeltaR<0.5)&&(ijet==0)) std::cout<<difreg<<"  "<<difraw<<std::endl;
				Double_t JetAdjustmentFactor = GetRecoGenJetScaleFactor(PFJetPt->at(ijet),ClosestGenJetPT,Standard_rescale);
				NewJetPT *=JetAdjustmentFactor;

				JetAdjustedMET = PropagatePTChangeToMET(JetAdjustedMET.Pt(),  JetAdjustedMET.Phi(), NewJetPT, (*PFJetPt)[ijet], PFJetPhi->at(ijet));

				//std::cout<<SmallestDeltaR<<"   "<<ClosestGenJetPT<<"   "<<(*PFJetPt)[ijet]<<"   "<<NewJetPT<<"        "<<(*PFMET)[0]<<"   "<<JetAdjustedMET.Pt()<<std::endl;
		
				if (JetSmearFactor > 0.0){

					Double_t JetEta = fabs(PFJetEta->at(ijet));
					Double_t Systematic_rescale = 0.2;
					
					if ((JetEta >1.5) && (JetEta<2.0)) Systematic_rescale = 0.25;
					if (JetEta >2.0) Systematic_rescale = 0.3;
					
					Double_t JetAdjustmentFactorSys = GetRecoGenJetScaleFactor(PFJetPt->at(ijet),ClosestGenJetPT,Systematic_rescale);
					NewJetPT *=JetAdjustmentFactorSys;
				
				}
				
				JetAdjustedMET = PropagatePTChangeToMET(JetAdjustedMET.Pt(),  JetAdjustedMET.Phi(), NewJetPT, (*PFJetPt)[ijet], PFJetPhi->at(ijet));
				
				//std::cout<<SmallestDeltaR<<"   "<<ClosestGenJetPT<<"   "<<(*PFJetPt)[ijet]<<"   "<<NewJetPT<<"        "<<(*PFMET)[0]<<"   "<<JetAdjustedMET.Pt()<<std::endl;

				(*PFJetPt)[ijet] = NewJetPT ;	
				//(*PFJetEta)[ijet] = NewJetETA ;	
				
				
			}
		}
		//std::cout<<(*PFJetPt)[0]<<"  "<<(*PFJetPtRaw)[0]<<std::endl;

		(*PFMET)[0] = JetAdjustedMET.Pt();
		(*PFMETPhi)[0] = JetAdjustedMET.Phi();
		//std::cout<<PFMET->at(0)<<"  "<<(*PFMET)[0]<<"      "<<PFMETPhi->at(0)<<"  "<<(*PFMETPhi)[0]<<std::endl;

		//std::cout<<" ------------------------------------------------ " <<std::endl;
		//========================     Muon Rescaling / Smearing Sequence   ================================//

		TLorentzVector MuAdjustedMET;
		MuAdjustedMET.SetPtEtaPhiM(PFMET->at(0),0.0,PFMETPhi->at(0),0);
		
		if (!isData)
		{
			for(unsigned int imuon = 0; imuon < MuonPt->size(); ++imuon)
			{
				double NewMuonPT =  ScaleObject((*MuonPt)[imuon],MuonRescaleFactor); 
				NewMuonPT =  SmearObject(NewMuonPT,MuonSmearFactor); 
				MuAdjustedMET = PropagatePTChangeToMET(MuAdjustedMET.Pt(),  MuAdjustedMET.Phi(), NewMuonPT, (*MuonPt)[imuon], MuonPhi->at(imuon));
				(*MuonPt)[imuon] = NewMuonPT ;	
			}
		}
		(*PFMET)[0] = MuAdjustedMET.Pt();
		(*PFMETPhi)[0] = MuAdjustedMET.Phi();
		//std::cout<<MuonPt->size()<<std::endl;
		//std::cout<<PFMET->at(0)<<"  "<<(*PFMET)[0]<<"      "<<PFMETPhi->at(0)<<"  "<<(*PFMETPhi)[0]<<std::endl;
		//std::cout<<" ---------------------------------------------------"<<std::endl;

		//========================     Electron Conditions   ================================//

		vector<int> v_idx_ele_final;
		for(unsigned int iele = 0; iele < ElectronPt->size(); ++iele)
		{
			double e_pt_real = ElectronPt->at(iele);
			double e_pt = ElectronPtHeep->at(iele);
			double e_eta = ElectronSCEta->at(iele);
			bool e_ecaldriven = ElectronHasEcalDrivenSeed->at(iele);
			double e_dphi_sc = ElectronDeltaPhiTrkSC->at(iele);
			double e_deta_sc = ElectronDeltaEtaTrkSC->at(iele);
			double e_hoe = ElectronHoE->at(iele);

			double e_sigmann = ElectronSigmaEtaEta->at(iele);
			double e_e1x5_over_5x5 = ElectronE1x5OverE5x5->at(iele);
			double e_e2x5_over_5x5 = ElectronE2x5OverE5x5->at(iele);
			double e_em_had1iso = ElectronHcalIsoD1DR03->at(iele);
			double e_had2iso = ElectronHcalIsoD2DR03->at(iele);
			double e_trkiso = ElectronTrkIsoPAT->at(iele);
			int e_missinghits = ElectronMissingHits->at(iele);

						
			//std::cout<<CustomHeepID(e_pt, e_eta, e_ecaldriven , e_dphi_sc, e_deta_sc, e_hoe, e_sigmann, e_e1x5_over_5x5, e_e2x5_over_5x5, e_em_had1iso , e_had2iso, e_trkiso )<<std::endl;

			//			if ( ElectronPt->at(iele) < 15.0 ) continue;
			if  (CustomHeepID(e_pt,e_pt_real, e_eta, e_ecaldriven , e_dphi_sc, e_deta_sc, e_hoe, e_sigmann, e_e1x5_over_5x5, e_e2x5_over_5x5, e_em_had1iso , e_had2iso, e_trkiso, e_missinghits ) && ElectronOverlaps->at(iele) == 0 )
			{
				v_idx_ele_final.push_back(iele);
			}
		}

		EleCount = 1.0*v_idx_ele_final.size();
		

		//========================     Stricter Electron Conditions   =============================//
		
		vector<int> v_idx_ele_good_final;


		//===  NOTE: Currently not implementing a cut on ElectronPt, this would be the cut if we wanted to:   double ele_PtCut = 35;

		for(unsigned int iele = 0; iele < ElectronPt->size(); ++iele)
		{
			double e_pt_real = ElectronPt->at(iele);			
			double e_pt = ElectronPtHeep->at(iele);
			double e_eta = ElectronSCEta->at(iele);
			bool e_ecaldriven = ElectronHasEcalDrivenSeed->at(iele);
			double e_dphi_sc = ElectronDeltaPhiTrkSC->at(iele);
			double e_deta_sc = ElectronDeltaEtaTrkSC->at(iele);
			double e_hoe = ElectronHoE->at(iele);

			double e_sigmann = ElectronSigmaEtaEta->at(iele);
			double e_e1x5_over_5x5 = ElectronE1x5OverE5x5->at(iele);
			double e_e2x5_over_5x5 = ElectronE2x5OverE5x5->at(iele);
			double e_em_had1iso = ElectronHcalIsoD1DR03->at(iele);
			double e_had2iso = ElectronHcalIsoD2DR03->at(iele);
			double e_trkiso = ElectronTrkIsoPAT->at(iele);
			int e_missinghits = ElectronMissingHits->at(iele);

		  
		  if ( CustomHeepID(e_pt,e_pt_real, e_eta, e_ecaldriven , e_dphi_sc, e_deta_sc, e_hoe, e_sigmann, e_e1x5_over_5x5, e_e2x5_over_5x5, e_em_had1iso , e_had2iso, e_trkiso, e_missinghits )  && ElectronOverlaps->at(iele) == 0 )  
		    {		      
		      v_idx_ele_good_final.push_back(iele);  
		    }
		}
		HEEPEleCount = 1.0*v_idx_ele_good_final.size();

		//========================      Muon Conditions   ================================//

		vector<int> v_idx_muon_final;
		vector<TLorentzVector> muons;
		int iMUON = -1;
		bool checkPT = true;	 // Pt requirement only on first muon at this stage
		
		// SubRoutine for Muon Counts
		GlobalMuonCount = 0.0;
		TrackerMuonCount = 0.0;
		
		for(unsigned int imuon = 0; imuon < MuonPt->size(); ++imuon)
		{
			if (MuonIsGlobal  ->at(imuon) == 1) GlobalMuonCount += 1.0;
			if (MuonIsTracker ->at(imuon) == 1) TrackerMuonCount += 1.0;
			
			Double_t muonPt = MuonPt->at(imuon);
			Double_t muonEta = MuonEta->at(imuon);

			if (checkPT && (muonPt < 20.0) ) continue;
			if  ( fabs(muonEta) > 2.4 )      continue;

			bool PassGlobalTightPrompt =
				MuonIsGlobal ->at(imuon) == 1 &&
				MuonIsTracker ->at(imuon) == 1 &&
				MuonTrackerIsoSumPT->at(imuon) < 3.0 &&                             // Disable for EWK
				//((MuonHcalIso->at(imuon) + MuonTrkIso->at(imuon))/muonPt) < 0.15;  // Enable for EWK
				MuonTrkHitsTrackerOnly ->at(imuon) >= 11   ;                         

			bool PassPOGTight =
				MuonStationMatches->at(imuon) > 1 && 
				fabs(MuonPrimaryVertexDXY ->at(imuon)) < 0.2  &&
				MuonGlobalChi2 ->at(imuon) < 10.0 &&                         /// Disable for EWK
				MuonPixelHitCount ->at(imuon) >=1 &&
				MuonGlobalTrkValidHits->at(imuon)>=1 ;

			if ( ! (PassGlobalTightPrompt && PassPOGTight) ) continue;
			iMUON = imuon;
			TLorentzVector muon;
			muon.SetPtEtaPhiM( MuonPt -> at(imuon), MuonEta-> at(imuon),    MuonPhi-> at(imuon),    0);

			muons.push_back(muon);
			checkPT=false;

			v_idx_muon_final.push_back(imuon);
		}						 // loop over muons

		MuonCount = 1.0*v_idx_muon_final.size();

		if ( MuonCount < 1 ) continue;
		TLorentzVector muon = muons[0];

		//========================    CaloJet Flags Conditions   ================================//
	
		FailIDCaloThreshold = -1.0;

		for(int ijet=0;ijet<(*CaloJetPt).size();ijet++)
		{

			bool IsBadCaloJet = false;
			
			if (fabs((*CaloJetEta)[ijet])<2.6)
			{
				if ((*CaloJetEMF)[ijet]<.01) IsBadCaloJet = true;
			}
			if ((*CaloJetn90Hits)[ijet]<=1) IsBadCaloJet = true;

			if ((*CaloJetfHPD)[ijet]>.98) IsBadCaloJet = true;

			if (!IsBadCaloJet) continue;
			
			if (CaloJetPt->at(ijet) > FailIDCaloThreshold) FailIDCaloThreshold = CaloJetPt->at(ijet);

		}			

		//========================     PFJet Conditions   ================================//
		// Get Good Jets in general

		deltaR_muon1closestPFJet = 999.9;
		Double_t deltaR_thisjet = 9999.9;
		vector<TLorentzVector> jets;
		vector<int> v_idx_pfjet_prefinal;
		vector<int> v_idx_pfjet_final_unseparated;
		vector<int> v_idx_pfjet_final;
		BpfJetCount = 0.0;
		FailIDPFThreshold = -1.0;
		TLorentzVector CurrentLepton,CurrentPFJet;


		// Initial Jet Quality Selection
		for(unsigned int ijet = 0; ijet < PFJetPt->size(); ++ijet)
		{
			//std::cout<<PFJetL2L3ResJEC->at(ijet)<<std::endl;
			//std::cout<<PFJetPt -> at(ijet)<<"   "<<PFJetPtRaw-> at(ijet) * PFJetL1OffsetJEC-> at(ijet) * PFJetL2RelJEC-> at(ijet) * PFJetL3AbsJEC-> at(ijet)<<std::endl;

			double jetPt = PFJetPt -> at(ijet);
			double jetEta = PFJetEta -> at(ijet);
			CurrentPFJet.SetPtEtaPhiM((*PFJetPt)[ijet],(*PFJetEta)[ijet],(*PFJetPhi)[ijet],0);

			bool IsLepton = false;
			for(unsigned int imuon = 0; imuon < MuonPt->size(); ++imuon)
			{
				CurrentLepton.SetPtEtaPhiM(MuonPt->at(imuon),MuonEta->at(imuon), MuonPhi->at(imuon),0.0);
				if (CurrentLepton.DeltaR(CurrentPFJet) < .5) IsLepton = true;
			}

			if (PFJetMuonEnergyFraction->at(ijet) > .8) IsLepton = true;

			if ((PFJetPassLooseID->at(ijet) != 1)&&(PFJetPt->at(ijet) > FailIDPFThreshold)&&(!IsLepton)) FailIDPFThreshold = PFJetPt->at(ijet);

			if ( jetPt < 25.0 ) continue;			

			if ( fabs(jetEta) > 3.0 ) continue;

			if (PFJetPassLooseID->at(ijet) != 1) continue;        // Disable for EWK
			//if (PFJetPassTightID->at(ijet) != 1) continue;

			v_idx_pfjet_prefinal.push_back(ijet);
		}
		
		/// Filter out jets that are actually muons
		TLorentzVector thisjet, thismu;
		vector<int> jetstoremove;

		Double_t thisdeltar = 0.0;
		Double_t mindeltar = 99999;
		int minjet = 0;
		int muindex = 99;
		int jetindex = 99;
		// Get list of jets to throw out
		//		for(unsigned int imu=0; imu<v_idx_muon_final.size(); imu++)
		//		{
		//			mindeltar = 999999;
		//			muindex = v_idx_muon_final[imu];
		//			thismu.SetPtEtaPhiM(MuonPt->at(muindex),MuonEta->at(muindex),MuonPhi->at(muindex),0);

		//			for(unsigned int ijet=0; ijet<v_idx_pfjet_prefinal.size(); ijet++)
		//			{
		//				jetindex = v_idx_pfjet_prefinal[ijet];
		//				thisjet.SetPtEtaPhiM((*PFJetPt)[jetindex],(*PFJetEta)[jetindex],(*PFJetPhi)[jetindex],0);

		//				thisdeltar = thismu.DeltaR(thisjet);

		//				if (thisdeltar < mindeltar)
		//				{
		//					mindeltar = thisdeltar;
		//					minjet = ijet;
		//				}
		//			}

		//			if (mindeltar<0.3) jetstoremove.push_back(minjet)       ;

		//		}

		for(unsigned int ijet=0; ijet<v_idx_pfjet_prefinal.size(); ijet++)
		{
			jetindex = v_idx_pfjet_prefinal[ijet];
			thisjet.SetPtEtaPhiM((*PFJetPt)[jetindex],(*PFJetEta)[jetindex],(*PFJetPhi)[jetindex],0);

			for(unsigned int imu=0; imu<v_idx_muon_final.size(); imu++)
			{
				muindex = v_idx_muon_final[imu];
				thismu.SetPtEtaPhiM(MuonPt->at(muindex),MuonEta->at(muindex),MuonPhi->at(muindex),0);

				thisdeltar = thismu.DeltaR(thisjet);

				if (thisdeltar < 0.5)		jetstoremove.push_back(jetindex);
			}
		}

		jetindex = 99;
		int remjetindex = 99;
		// Eliminate bad jets from prefinal jet vector, save as final
		for(unsigned int ijet=0; ijet<v_idx_pfjet_prefinal.size(); ijet++)
		{
			int jetgood = 1;
			jetindex = v_idx_pfjet_prefinal[ijet];
			for(unsigned int kjet=0; kjet<jetstoremove.size(); kjet++)
			{
				remjetindex = jetstoremove[kjet];
				if (jetindex == remjetindex) jetgood=0;

			}

			if (jetgood ==1) v_idx_pfjet_final_unseparated.push_back(jetindex);
		}

		// Take filtered jets and eliminate those too close to the muon. save b variables

		jetindex = 99;

		for(unsigned int ijet=0; ijet<v_idx_pfjet_final_unseparated.size(); ijet++)
		{
			jetindex = v_idx_pfjet_final_unseparated[ijet];
			double jetPt = PFJetPt -> at(jetindex);
			double jetEta = PFJetEta -> at(jetindex);

			TLorentzVector newjet;
			newjet.SetPtEtaPhiM(jetPt,  jetEta, PFJetPhi->at(jetindex),     0);
			// require a separation between a muon and a jet

			//deltaR_thisjet =  newjet.DeltaR(muon);
			//if ( deltaR_thisjet < deltaR_muon1closestPFJet)  deltaR_muon1closestPFJet = deltaR_thisjet ;

			//			if ( deltaR_thisjet < 0.5 ) continue;

			if ( PFJetTrackCountingHighEffBTag->at(jetindex) > 2.0 )
			{
				BpfJetCount = BpfJetCount + 1.0;
			}

			// if we are here, the jet is good
			v_idx_pfjet_final.push_back(jetindex);
		}
		PFJetCount = 1.0*v_idx_pfjet_final.size();

		//if (PFJetCount <2) continue;

		//========================     Generator Level Module  ================================//

		Double_t piover2 = 3.1415926/2.0;
		TLorentzVector V_MetAddition;
		V_MetAddition.SetPtEtaPhiM(0.0,0.0,0.0,0.0);

		TLorentzVector UW_gen , BW_gen, v_GenNu, muon1test;

		BW_gen.SetPtEtaPhiM(0,0,0,0); UW_gen.SetPtEtaPhiM(0,0,0,0); v_GenNu.SetPtEtaPhiM(0,0,0,0), muon1test.SetPtEtaPhiM(0,0,0,0) ;

		// Generator Level Variables
		VRESET(Pt_genjet1);     VRESET(Pt_genjet2);
		VRESET(Pt_genmuon1);    VRESET(Pt_genmuon2);
		VRESET(Phi_genmuon1);   VRESET(Phi_genmuon2);
		VRESET(Eta_genmuon1);   VRESET(Eta_genmuon2);
		VRESET(Pt_genMET);      VRESET(Phi_genMET);    VRESET(Eta_genMET);
		VRESET(Pt_genneutrino); VRESET(Phi_genneutrino); VRESET(Eta_genneutrino);
		VRESET(Pt_Z_gen);       VRESET(Pt_W_gen);
		VRESET(Phi_Z_gen);      VRESET(Phi_W_gen);
		VRESET(JetMatchMuon1);  VRESET(JetMatchMuon2);


		// Recoil variables
		VRESET(U1_Z_gen); VRESET(U2_Z_gen);
		VRESET(U1_W_gen); VRESET(U2_W_gen);

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
			
			int LQIndex1 = -1;
			int LQIndex2 = -1;

			int LQIndex1_jet, LQIndex1_lepton, LQIndex2_jet, LQIndex2_lepton;
			TLorentzVector v_LQIndex1_jet, v_LQIndex1_lepton, v_LQIndex2_jet, v_LQIndex2_lepton;


			for(unsigned int ip = 0; ip != GenParticlePdgId->size(); ++ip)
			{
				int pdgId = GenParticlePdgId->at(ip);
				int motherIndex = GenParticleMotherIndex->at(ip);
				if ( TMath::Abs(pdgId) == 42 ) {
					if ((LQIndex1 != -1)&&(LQIndex2 == -1)) LQIndex2 = ip;
					if (LQIndex1 == -1) LQIndex1 = ip;
				}	
			}

			int Lepton1_ismuon = 0;
			int Lepton2_ismuon = 0;
			for(unsigned int ip = 0; ip != GenParticlePdgId->size(); ++ip)
			{
				int pdgId = GenParticlePdgId->at(ip);
				int motherIndex = GenParticleMotherIndex->at(ip);
				if ( motherIndex == LQIndex1 ) {
					if (( TMath::Abs(pdgId) == 13 ) || ( TMath::Abs(pdgId) == 14 )) {
						LQIndex1_lepton = ip;
						v_LQIndex1_lepton.SetPtEtaPhiM(GenParticlePt->at(ip),GenParticleEta->at(ip),GenParticlePhi->at(ip),0);
						if ( TMath::Abs(pdgId) == 13 ) Lepton1_ismuon = 1 ; 
					}
					else{
						LQIndex1_jet = ip;
						v_LQIndex1_jet.SetPtEtaPhiM(GenParticlePt->at(ip),GenParticleEta->at(ip),GenParticlePhi->at(ip),0);
					}
				}	

				if ( motherIndex == LQIndex2 ) {
					if (( TMath::Abs(pdgId) == 13 ) || ( TMath::Abs(pdgId) == 14 )) {
						LQIndex2_lepton = ip;
						v_LQIndex2_lepton.SetPtEtaPhiM(GenParticlePt->at(ip),GenParticleEta->at(ip),GenParticlePhi->at(ip),0);
						if ( TMath::Abs(pdgId) == 13 ) Lepton2_ismuon = 1 ; 
						
					}
					else{
						LQIndex2_jet = ip;
						v_LQIndex2_jet.SetPtEtaPhiM(GenParticlePt->at(ip),GenParticleEta->at(ip),GenParticlePhi->at(ip),0);
					}
				}	
			}

			
			int RecoJet1MatchedToJet1 = 0;
			int RecoJet2MatchedToJet1 = 0;
			int RecoMu1MatchedToLepton1 = 0;
			int RecoMu2MatchedToLepton1 = 0;

			int RecoJet1MatchedToJet2 = 0;
			int RecoJet2MatchedToJet2 = 0;
			int RecoMu1MatchedToLepton2 = 0;
			int RecoMu2MatchedToLepton2 = 0;
			
			TLorentzVector reco_muon1, reco_muon2, reco_jet1, reco_jet2;
			
			if (MuonCount>=1) reco_muon1.SetPtEtaPhiM(MuonPt->at(v_idx_muon_final[0]),MuonEta->at(v_idx_muon_final[0]),MuonPhi->at(v_idx_muon_final[0]),0);
			if (MuonCount>=2) reco_muon2.SetPtEtaPhiM(MuonPt->at(v_idx_muon_final[1]),MuonEta->at(v_idx_muon_final[1]),MuonPhi->at(v_idx_muon_final[1]),0);
			if (PFJetCount>=1) reco_jet1.SetPtEtaPhiM(PFJetPt->at(v_idx_pfjet_final[0]),PFJetEta->at(v_idx_pfjet_final[0]),PFJetPhi->at(v_idx_pfjet_final[0]),0);
			if (PFJetCount>=2) reco_jet2.SetPtEtaPhiM(PFJetPt->at(v_idx_pfjet_final[1]),PFJetEta->at(v_idx_pfjet_final[1]),PFJetPhi->at(v_idx_pfjet_final[1]),0);

			float dR_l1_rl1 = 19 ; float  dR_l1_rl2 = 29 ; float  dR_l2_rl1 = 39 ; float  dR_l2_rl2 = 49 ; float  dR_j1_rj1 = 59 ; float  dR_j1_rj2 = 69 ; float  dR_j2_rj1 = 79 ; float  dR_j2_rj2 = 89; 

			if ( (v_LQIndex1_lepton.Pt()>1) && (v_LQIndex1_jet.Pt()>1) && (v_LQIndex2_lepton.Pt()>1) && (v_LQIndex2_jet.Pt()>1) ){
				if (MuonCount>=1 ) { 
					dR_l1_rl1 = reco_muon1.DeltaR(v_LQIndex1_lepton);
					dR_l2_rl1 = reco_muon1.DeltaR(v_LQIndex2_lepton);
				}	
				if (MuonCount>=2 ) { 
					dR_l1_rl2 = reco_muon2.DeltaR(v_LQIndex1_lepton);
					dR_l2_rl2 = reco_muon2.DeltaR(v_LQIndex2_lepton);
				}	
				if (PFJetCount>=1 ) { 
					dR_j1_rj1 = reco_jet1.DeltaR(v_LQIndex1_jet);
					dR_j2_rj1 = reco_jet1.DeltaR(v_LQIndex2_jet);
				}	
				if (PFJetCount>=2 ) { 
					dR_j1_rj2 = reco_jet2.DeltaR(v_LQIndex1_jet);
					dR_j2_rj2 = reco_jet2.DeltaR(v_LQIndex2_jet);
				}	
			}


			if ( ( dR_l1_rl1 < dR_l1_rl2 ) &&  (dR_l1_rl1 < 0.5 ) ) RecoMu1MatchedToLepton1 = 1;
			if ( ( dR_l1_rl1 > dR_l1_rl2 ) &&  (dR_l1_rl2 < 0.5 ) ) RecoMu2MatchedToLepton1 = 1;
			
			if ( ( dR_l2_rl1 < dR_l2_rl2 ) &&  (dR_l2_rl1 < 0.5 ) ) RecoMu1MatchedToLepton2 = 1;
			if ( ( dR_l2_rl1 > dR_l2_rl2 ) &&  (dR_l2_rl2 < 0.5 ) ) RecoMu2MatchedToLepton2 = 1;			

			if ( ( dR_j1_rj1 < dR_j1_rj2 ) &&  (dR_j1_rj1 < 0.5 ) ) RecoJet1MatchedToJet1 = 1;
			if ( ( dR_j1_rj1 > dR_j1_rj2 ) &&  (dR_j1_rj2 < 0.5 ) ) RecoJet2MatchedToJet1 = 1;
			
			if ( ( dR_j2_rj1 < dR_j2_rj2 ) &&  (dR_j2_rj1 < 0.5 ) ) RecoJet1MatchedToJet2 = 1;
			if ( ( dR_j2_rj1 > dR_j2_rj2 ) &&  (dR_j2_rj2 < 0.5 ) ) RecoJet2MatchedToJet2 = 1;	
			
			int JetMatchedToRecoMuon1, JetMatchedToRecoMuon2;
			
			int LQPair1Muon, LQPair2Muon, LQPair1Jet, LQPair2Jet;


			LQPair1Muon = ( 1*RecoMu1MatchedToLepton1 + 2*RecoMu2MatchedToLepton1  ); 
			LQPair2Muon = ( 1*RecoMu1MatchedToLepton2 + 2*RecoMu2MatchedToLepton2  ); 
			
			LQPair1Jet = ( 1*RecoJet1MatchedToJet1 + 2*RecoJet2MatchedToJet1  ); 
			LQPair2Jet = ( 1*RecoJet1MatchedToJet2 + 2*RecoJet2MatchedToJet2  ); 

			
			if ( LQPair1Muon == 1 ) JetMatchedToRecoMuon1 = LQPair1Jet;
			if ( LQPair2Muon == 1 ) JetMatchedToRecoMuon1 = LQPair2Jet;

			if ( LQPair1Muon == 2 ) JetMatchedToRecoMuon2 = LQPair1Jet;
			if ( LQPair2Muon == 2 ) JetMatchedToRecoMuon2 = LQPair2Jet;

			//if ((LQPair1Muon == 3)||(LQPair2Muon == 3)||(LQPair1Jet == 3)||(LQPair2Jet == 3)) std::cout<<"ALERT"<<std::endl;
			
			JetMatchMuon1 = JetMatchedToRecoMuon1;
			JetMatchMuon2 = JetMatchedToRecoMuon2;
			
			//std::cout<<LQIndex1<<":"<<GenParticlePdgId->at(LQIndex1)<<"   "<<LQIndex1_lepton<<":"<<GenParticlePdgId->at(LQIndex1_lepton)<<"   "<<LQIndex1_jet<<":"<<GenParticlePdgId->at(LQIndex1_jet)<<std::endl;
			//std::cout<<LQIndex2<<":"<<GenParticlePdgId->at(LQIndex2)<<"   "<<LQIndex2_lepton<<":"<<GenParticlePdgId->at(LQIndex2_lepton)<<"   "<<LQIndex2_jet<<":"<<GenParticlePdgId->at(LQIndex2_jet)<<std::endl;
			//std::cout<<JetMatchedToRecoMuon1<<std::endl;

			//std::cout<<JetMatchedToRecoMuon2<<std::endl;
			//std::cout<<dR_l1_rl1<<" "<<dR_l1_rl2<<" "<<dR_l2_rl1<<" "<<dR_l2_rl2<<" "<<dR_j1_rj1<<" "<<dR_j1_rj2<<" "<<dR_j2_rj1<<" "<<dR_j2_rj2<<std::endl;
			//std::cout<<" -----------------------------------------------------------------" <<std::endl;			

			for(unsigned int ijet = 0; ijet < GenJetPt->size(); ++ijet)
			{
				if (ijet ==0) Pt_genjet1 = GenJetPt->at(ijet);
				if (ijet ==1) Pt_genjet2 = GenJetPt->at(ijet);
			}

			for(unsigned int ip = 0; ip != GenParticlePdgId->size(); ++ip)
			{

				int pdgId = GenParticlePdgId->at(ip);
				int motherIndex = GenParticleMotherIndex->at(ip);
				
								 // ISR
				if ( motherIndex == -1 ) continue;
				//std::cout<<"a"<<"  "<<motherIndex<<std::endl;
				//int pdgIdMother = GenParticlePdgId->at(motherIndex);
				//std::cout<<"b"<<"  "<<pdgIdMother<<std::endl;

				//muon
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
			
			
			Pt_genjet1 = -1.0;
			Pt_genjet2 = -1.0;
			TLorentzVector genjet1, genjet2;
			for(unsigned int ijet = 0; ijet != GenJetPt->size(); ++ijet)
			{
				if (GenJetEta->at(ijet)>3.0) continue;
				if (Pt_genjet1 > 0.0 && Pt_genjet2 < 0.0 ) {
					Pt_genjet2 = GenJetPt->at(ijet);
					genjet2.SetPtEtaPhiM(Pt_genjet2,GenJetEta->at(ijet),GenJetPhi->at(ijet),0);
				}
				
				if (Pt_genjet1 < 0.0) {
					Pt_genjet1 = GenJetPt->at(ijet);
					genjet1.SetPtEtaPhiM(Pt_genjet1,GenJetEta->at(ijet),GenJetPhi->at(ijet),0);					
				}
			}


				
			Pt_genMET = GenMETTrue->at(0);
			Phi_genMET = GenMETPhiTrue->at(0);
			MT_genmuon1genMET =  TMass(Pt_genmuon1,Pt_genMET, fabs(Phi_genmuon1 - Phi_genMET) );

			TLorentzVector v_GenMuon1, v_GenMuon2, v_GenMet;

			v_GenMuon1.SetPtEtaPhiM(Pt_genmuon1,Eta_genmuon1,Phi_genmuon1,0);
			v_GenMuon2.SetPtEtaPhiM(Pt_genmuon2,Eta_genmuon2,Phi_genmuon2,0);
			v_GenNu.SetPtEtaPhiM( Pt_genneutrino ,Eta_genneutrino,Phi_genneutrino ,0);
			v_GenMet.SetPtEtaPhiM ( Pt_genMET, 0, Phi_genMET,0 );

			v_GenMuon1.SetPtEtaPhiM(Pt_genmuon1,Eta_genmuon1,Phi_genmuon1,0);
			v_GenMuon2.SetPtEtaPhiM(Pt_genmuon2,Eta_genmuon2,Phi_genmuon2,0);

			deltaPhi_genmuon1genMET = v_GenMuon1.DeltaPhi(v_GenMet);
			deltaPhi_genjet1genMET = genjet1.DeltaPhi(v_GenMet);
			deltaPhi_genjet2genMET = genjet2.DeltaPhi(v_GenMet);
			
			ST_gen_mumu = Pt_genjet1 + Pt_genjet2 + Pt_genmuon1 + Pt_genmuon2;
			ST_gen_munu = Pt_genjet1 + Pt_genjet2 + Pt_genmuon1 + Pt_genMET;

			

			


			
			//std::cout<<Pt_genmuon1<<"  "<<Pt_genmuon2<<std::endl;
			//std::cout<<Pt_genjet1<<"  "<<Pt_genjet2<<std::endl;
			//std::cout<<Pt_genMET<<"  "<<MT_genmuon1genMET<<std::endl;
			//std::cout<<ST_gen_mumu<<"  "<<ST_gen_munu<<std::endl;
			//std::cout<<deltaPhi_genmuon1genMET<<"  "<<deltaPhi_genjet1genMET<<"  "<<deltaPhi_genjet2genMET<<std::endl;
			//std::cout<<" -----------------------------------------------"<<std::endl;

			Pt_Z_gen = (v_GenMuon1 + v_GenMuon2).Pt();
			Phi_Z_gen = (v_GenMuon1 + v_GenMuon2).Phi();

			// Set the recoil variables

			U1_Z_gen = 990.0;
			U2_Z_gen = 990.0;
			U1_W_gen = 990.0;
			U2_W_gen = 990.0;

			TLorentzVector UZ_gen = -(v_GenMet + v_GenMuon1 + v_GenMuon2);
			TLorentzVector BZ_gen = (v_GenMuon1+v_GenMuon2 );
			U1_Z_gen = (UZ_gen.Pt()) * (cos(UZ_gen.DeltaPhi(BZ_gen))) ;
			U2_Z_gen = (UZ_gen.Pt()) * (sin(UZ_gen.DeltaPhi(BZ_gen))) ;
			
			TLorentzVector pfMETtest;
			pfMETtest.SetPtEtaPhiM(PFMET->at(0),0.0,PFMETPhi->at(0),0.0);
			muon1test.SetPtEtaPhiM(MuonPt->at(v_idx_muon_final[0]),MuonEta->at(v_idx_muon_final[0]),MuonPhi->at(v_idx_muon_final[0]),0.0);

			Pt_W_gen = (muon1test + v_GenNu).Pt();
			Phi_W_gen = (muon1test + v_GenNu).Phi();

			UW_gen = -(pfMETtest + muon1test );
			BW_gen = (muon1test +v_GenNu);
			U1_W_gen = (UW_gen.Pt()) * (cos(UW_gen.DeltaPhi(BW_gen))) ;
			U2_W_gen = (UW_gen.Pt()) * (sin(UW_gen.DeltaPhi(BW_gen))) ;

			if (IsW && DoRecoilCorrections)
			{
				Double_t U1Phi = - BW_gen.Phi();
				Double_t U2Phi = BW_gen.Phi() + piover2;

				if ((BW_gen.DeltaPhi(UW_gen)) < 0)   U2Phi = BW_gen.Phi() - piover2;

				Double_t U1Prime = F_U1Prime(Pt_W_gen);
				Double_t U2Prime = F_U2Prime(Pt_W_gen);

				TLorentzVector V_UPrime, V_U1Prime, V_U2Prime, V_MetPrime;

				V_U1Prime.SetPtEtaPhiM(U1Prime,0,U1Phi,0);
				V_U2Prime.SetPtEtaPhiM(U2Prime,0,U2Phi,0);
				V_UPrime = V_U1Prime + V_U2Prime;
				V_MetPrime = -(v_GenMuon1+ V_UPrime);

				V_MetAddition.SetPtEtaPhiM(V_MetPrime.Pt(),0,V_MetPrime.Phi(),0);
				V_MetAddition = V_MetAddition - v_GenMet;

			}
		}

		//========================     Set variables to zero  ================================//

		// Leading muon 1
		VRESET(TrkD0_muon1);     VRESET(NHits_muon1);   VRESET(TrkDZ_muon1);   VRESET(ChiSq_muon1);
		VRESET(TrkIso_muon1); VRESET(EcalIso_muon1); VRESET(HcalIso_muon1); VRESET(RelIso_muon1);
		VRESET(Phi_muon1);    VRESET(Eta_muon1);     VRESET(Pt_muon1);      VRESET(Charge_muon1);
		VRESET(QOverPError_muon1); VRESET(PhiError_muon1);    VRESET(EtaError_muon1);     VRESET(PtError_muon1); 
		VRESET(TrackerIsoSumPT_muon1);


		// Leading muon 2
		VRESET(TrkD0_muon2);     VRESET(NHits_muon2);   VRESET(TrkDZ_muon2);   VRESET(ChiSq_muon2);
		VRESET(TrkIso_muon2); VRESET(EcalIso_muon2); VRESET(HcalIso_muon2); VRESET(RelIso_muon2);
		VRESET(Phi_muon2);    VRESET(Eta_muon2);     VRESET(Pt_muon2);      VRESET(Charge_muon2);
		VRESET(QOverPError_muon2); VRESET(PhiError_muon2);    VRESET(EtaError_muon2);     VRESET(PtError_muon2); 
		VRESET(TrackerIsoSumPT_muon2);


		// PFJet 1
		VRESET(Phi_pfjet1); VRESET(Eta_pfjet1); VRESET(Pt_pfjet1); VRESET(BDisc_pfjet1);
		VRESET(PFJetNeutralMultiplicity_pfjet1);         VRESET(PFJetNeutralHadronEnergyFraction_pfjet1);
		VRESET(PFJetNeutralEmEnergyFraction_pfjet1);     VRESET(PFJetChargedMultiplicity_pfjet1);
		VRESET(PFJetChargedHadronEnergyFraction_pfjet1); VRESET(PFJetChargedEmEnergyFraction_pfjet1);

		// PFJet 2
		VRESET(Phi_pfjet2); VRESET(Eta_pfjet2); VRESET(Pt_pfjet2); VRESET(BDisc_pfjet2);
		VRESET(PFJetNeutralMultiplicity_pfjet2);         VRESET(PFJetNeutralHadronEnergyFraction_pfjet2);
		VRESET(PFJetNeutralEmEnergyFraction_pfjet2);     VRESET(PFJetChargedMultiplicity_pfjet2);
		VRESET(PFJetChargedHadronEnergyFraction_pfjet2); VRESET(PFJetChargedEmEnergyFraction_pfjet2);

		// Electron (If any)
		VRESET(Pt_ele1);
		VRESET(Eta_ele1);
		VRESET(Phi_ele1);
		VRESET(Pt_HEEPele1);
		VRESET(Eta_HEEPele1);
		VRESET(Phi_HEEPele1);
	
		// PFMET
		VRESET(MET_pf); VRESET(Phi_MET_pf);
		VRESET(MET_lq); VRESET(METRatio_pfcalo); VRESET(METRatio_lqpf); VRESET(METRatio_lqcalo);


		// Delta Phi Variables
		VRESET(deltaPhi_muon1muon2);  VRESET(deltaPhi_pfjet1pfjet2);
		VRESET(deltaPhi_muon1pfMET);  VRESET(deltaPhi_muon2pfMET);
		VRESET(deltaPhi_pfjet1pfMET); VRESET(deltaPhi_pfjet2pfMET);
		VRESET(deltaPhi_muon1pfjet1); VRESET(deltaPhi_muon1pfjet2);
		VRESET(deltaPhi_muon2pfjet1); VRESET(deltaPhi_muon2pfjet2);
		VRESET(deltaPhi_METClosestCaloJet);
		VRESET(deltaPhi_METClosestPFJet);
		VRESET(deltaPhi_METFurthestCaloJet);
		VRESET(deltaPhi_METFurthestPFJet);
		VRESET(deltaPhi_METClosestPT10CaloJet);
		VRESET(deltaPhi_METClosestPT10PFJet);
		VRESET(deltaPhi_METFurthestPT10CaloJet);
		VRESET(deltaPhi_METFurthestPT10PFJet);

		// Delta R Variables
		VRESET(deltaR_muon1muon2);  VRESET(deltaR_pfjet1pfjet2);
		VRESET(deltaR_muon1pfjet1); VRESET(deltaR_muon1pfjet2);
		VRESET(deltaR_muon2pfjet1); VRESET(deltaR_muon2pfjet2);
		VRESET(deltaR_muon1closestPFJet);
		VRESET(deltaR_muon1HEEPele1);


		// Mass Combinations
		VRESET(M_muon1muon2);  VRESET(M_pfjet1pfjet2);
		VRESET(M_muon1pfjet1); VRESET(M_muon1pfjet2);
		VRESET(M_muon2pfjet1); VRESET(M_muon2pfjet2);
		VRESET(M_muon1muon2pfjet1pfjet2);
		VRESET(M_muon1pfjet1pfjet2); VRESET(M_muon1muon2pfjet1);

		VRESET(M_bestmupfjet1_mumu); VRESET(M_bestmupfjet2_mumu);
		VRESET(M_bestmupfjet_munu);
		VRESET(M_muon1HEEPele1);
		VRESET(M_mujetjet);
		VRESET(M_AllCaloJet);	VRESET(M_AllPFJet);
		VRESET(Pt_AllCaloJet);	VRESET(Pt_AllPFJet);
		VRESET(MetDirComp_AllCaloJet);	VRESET(MetDirComp_AllPFJet);
		VRESET(MetDirCompOverMET_AllCaloJet);	VRESET(MetDirCompOverMET_AllPFJet);



		// Transverse Mass Combinations
		VRESET(MT_muon1pfMET);
		VRESET(MT_pfjet1pfMET); VRESET(MT_pfjet2pfMET);
		VRESET(MT_muon1pfjet1); VRESET(MT_muon1pfjet2);
		VRESET(MT_muon1pfjet2); VRESET(MT_muon2pfjet2);

		// ST Variables
		VRESET(ST_pf_mumu); VRESET(ST_pf_munu);

		// Other Variables
		VRESET(minval_muon1pfMET);
		VRESET(Pt_Z);  VRESET(Pt_W);
		VRESET(Phi_Z); VRESET(Phi_W);

		// Extra Discriminating Variables

		VRESET(RangeMass_BestLQCombo);
		VRESET(RangeTransverseMass_BestLQCombo);
		VRESET(CenterMass_BestLQCombo);
		VRESET(CenterTransverseMass_BestLQCombo);
		VRESET(RangeCenterMassRatio_BestLQCombo);
		VRESET(RangeCenterTransverseMassRatio_BestLQCombo);
		VRESET(LowestMass_BestLQCombo);
		VRESET(AverageMass_BestLQCombo);
	
		// Additions for E-Mu Selection
	
		VRESET(LowestMass_BestLQCombo_emuselection);
		VRESET(AverageMass_BestLQCombo_emuselection);
		
	
		VRESET(M_HEEPele1pfjet1_emuselection); VRESET(M_HEEPele1pfjet2_emuselection);
		VRESET(M_bestmuORelepfjet1_mumu_emuselection); VRESET(M_bestmuORelepfjet2_mumu_emuselection);
	

		// Recoil variables
		VRESET(U1_Z);     VRESET(U2_Z);
		VRESET(U1_W);     VRESET(U2_W);
		VRESET(UdotMu);   VRESET(UdotMu_overmu);
		VRESET(MET_pfsig);
		
		// Additional Counts
		PFJetRawCount = 0.0;   CaloJetRawCount=0.0;
		ST_pf_hadronic = 0.0;  ST_calo_hadronic = 0.0;
		

		//===================================================================================================
		//      Run the Calculations of physical variables using selected particles.
		//===================================================================================================

		// 4-Vectors for Particles
		TLorentzVector jet1, jet2, pfjet1, pfjet2, muon1,muon3, caloMET,muon2,pfMET,tcMET,heepele1;

		//========================     MET Basics  ================================//

		MET_pf = PFMET->at(0);
		MET_pfsig = PFMETSig->at(0);
		pfMET.SetPtEtaPhiM(MET_pf,0.0,PFMETPhi->at(0),0.0);
		caloMET.SetPtEtaPhiM(CaloMET->at(0),0.0,CaloMETPhi->at(0),0.0);
		double MET_calo = CaloMET->at(0);
		
		METRatio_pfcalo = MET_pf/MET_calo; 
		
		TLorentzVector ThisPFJet;
		TLorentzVector ThisCaloJet;
		TLorentzVector ThisLepton;
		Double_t MetJetDphi;
		Double_t JetLepDR;

				// Find Closest and furthest of any jet w.r.t. MET 
		deltaPhi_METClosestCaloJet = 99999.12345;
		deltaPhi_METClosestPFJet = 99999.12345;
		deltaPhi_METFurthestCaloJet=-99999.12345;
		deltaPhi_METFurthestPFJet = -99999.12345;
				
		for(unsigned int ijet = 0; ijet < PFJetPt->size(); ++ijet)
		{
			ThisPFJet.SetPtEtaPhiM((*PFJetPt)[ijet],(*PFJetEta)[ijet],(*PFJetPhi)[ijet],0);
			MetJetDphi = TMath::Abs(ThisPFJet.DeltaPhi(pfMET));
			bool consider = true;
			
			for(unsigned int imuon = 0; imuon < MuonPt->size(); ++imuon)
			{
				ThisLepton.SetPtEtaPhiM(MuonPt->at(imuon),MuonEta->at(imuon), MuonPhi->at(imuon),0.0);
				JetLepDR = ThisLepton.DeltaR(ThisPFJet);
				if (JetLepDR < .2) consider = false;
			}
			for(unsigned int iele = 0; iele < ElectronPt->size(); ++iele)
			{
				ThisLepton.SetPtEtaPhiM(ElectronPt->at(iele),ElectronEta->at(iele),ElectronPhi->at(iele),0.0);
				JetLepDR = ThisLepton.DeltaR(ThisPFJet);
				if (JetLepDR < .2) consider = false;
			}
			if (consider)
			{
				PFJetRawCount += 1.0;
				ST_pf_hadronic +=(*PFJetPt)[ijet]; 
				if (MetJetDphi < deltaPhi_METClosestPFJet) deltaPhi_METClosestPFJet = MetJetDphi;
				if (MetJetDphi > deltaPhi_METFurthestPFJet) deltaPhi_METFurthestPFJet = MetJetDphi;	
			}
		}
		
		for(unsigned int ijet = 0; ijet < CaloJetPt->size(); ++ijet)
		{
			CaloJetRawCount += 1.0;
			ST_calo_hadronic += (*CaloJetPt)[ijet];
			ThisCaloJet.SetPtEtaPhiM((*CaloJetPt)[ijet],(*CaloJetEta)[ijet],(*CaloJetPhi)[ijet],0);
			MetJetDphi = TMath::Abs(ThisCaloJet.DeltaPhi(caloMET));
			if (MetJetDphi < deltaPhi_METClosestCaloJet) deltaPhi_METClosestCaloJet = MetJetDphi;
			if (MetJetDphi > deltaPhi_METFurthestCaloJet) deltaPhi_METFurthestCaloJet = MetJetDphi;	
		}
		
		
				// Find Closest and furthest of any jet with PT>10 w.r.t. MET 

		deltaPhi_METClosestPT10CaloJet = 99999.12345;
		deltaPhi_METClosestPT10PFJet = 99999.12345;
		deltaPhi_METFurthestPT10CaloJet=-99999.12345;
		deltaPhi_METFurthestPT10PFJet = -99999.12345;
				
		for(unsigned int ijet = 0; ijet < PFJetPt->size(); ++ijet)
		{
			ThisPFJet.SetPtEtaPhiM((*PFJetPt)[ijet],(*PFJetEta)[ijet],(*PFJetPhi)[ijet],0);
			if (ThisPFJet.Pt()<10.0) continue;
			MetJetDphi = TMath::Abs(ThisPFJet.DeltaPhi(pfMET));
			bool consider = true;
			
			for(unsigned int imuon = 0; imuon < MuonPt->size(); ++imuon)
			{
				ThisLepton.SetPtEtaPhiM(MuonPt->at(imuon),MuonEta->at(imuon), MuonPhi->at(imuon),0.0);
				JetLepDR = ThisLepton.DeltaR(ThisPFJet);
				if (JetLepDR < .2) consider = false;
			}
			for(unsigned int iele = 0; iele < ElectronPt->size(); ++iele)
			{
				ThisLepton.SetPtEtaPhiM(ElectronPt->at(iele),ElectronEta->at(iele),ElectronPhi->at(iele),0.0);
				JetLepDR = ThisLepton.DeltaR(ThisPFJet);
				if (JetLepDR < .2) consider = false;
			}
			if (consider)
			{
				if (MetJetDphi < deltaPhi_METClosestPT10PFJet) deltaPhi_METClosestPT10PFJet = MetJetDphi;
				if (MetJetDphi > deltaPhi_METFurthestPT10PFJet) deltaPhi_METFurthestPT10PFJet = MetJetDphi;	
			}
		}
		
		for(unsigned int ijet = 0; ijet < CaloJetPt->size(); ++ijet)
		{
			ThisCaloJet.SetPtEtaPhiM((*CaloJetPt)[ijet],(*CaloJetEta)[ijet],(*CaloJetPhi)[ijet],0);
			if (ThisCaloJet.Pt()<10.0) continue;

			MetJetDphi = TMath::Abs(ThisCaloJet.DeltaPhi(caloMET));

			if (MetJetDphi < deltaPhi_METClosestPT10CaloJet) deltaPhi_METClosestPT10CaloJet = MetJetDphi;
			if (MetJetDphi > deltaPhi_METFurthestPT10CaloJet) deltaPhi_METFurthestPT10CaloJet = MetJetDphi;	

		}

		//========================     MET Recoil Correction  ================================//

		// Recoil Corrections
		if (IsW && DoRecoilCorrections && true)
		{

			// Very careful calculation of the geometry of the recoil vectors.
			Double_t U1Phi =  BW_gen.Phi() + 2*piover2;
			if (U1Phi> (2*piover2)) U1Phi = U1Phi - 4*piover2;

			Double_t check_phi_u1 = U1Phi; if (check_phi_u1<0) check_phi_u1 = check_phi_u1 + 4*piover2;
			Double_t check_phi_w = BW_gen.Phi(); if (check_phi_w<0) check_phi_w = check_phi_w +  4*piover2;
			Double_t check_phi_u = UW_gen.Phi(); if (check_phi_u<0) check_phi_u = check_phi_u +  4*piover2;

			Double_t check_phi_u2 = 99;
			if ((check_phi_w<2*piover2)&&(check_phi_u>check_phi_w)) check_phi_u2 = check_phi_w + piover2;
			if ((check_phi_w<2*piover2)&&(check_phi_u<check_phi_w)) check_phi_u2 = check_phi_w - piover2;
			if ((check_phi_w>2*piover2)&&(check_phi_u>check_phi_w)) check_phi_u2 = check_phi_w + piover2;
			if ((check_phi_w>2*piover2)&&(check_phi_u<check_phi_w)&&(check_phi_u>(check_phi_w - 2*piover2))) check_phi_u2 = check_phi_w - piover2;
			if ((check_phi_w>2*piover2)&&(check_phi_u<check_phi_w)&&(check_phi_u<(check_phi_w - 2*piover2))) check_phi_u2 = check_phi_w + piover2;
			if (check_phi_u2 > 4*piover2) check_phi_u2 = check_phi_u2 - 4*piover2;

			// Get the new recoil vectors
			Double_t U2Phi = check_phi_u2;
			Double_t reco_Pt_W = (muon1test + v_GenNu).Pt();
			Double_t U1Prime = F_U1Prime(reco_Pt_W);
			Double_t U2Prime = F_U2Prime(reco_Pt_W);

			// Change the MET vector based on the new recoil vectors
			TLorentzVector V_UPrime, V_U1Prime, V_U2Prime, V_MetPrime;

			V_U1Prime.SetPtEtaPhiM(U1Prime,0,U1Phi,0);
			V_U2Prime.SetPtEtaPhiM(U2Prime,0,U2Phi,0);

			V_UPrime = V_U1Prime + V_U2Prime;
			V_MetPrime = -(muon1test+ V_UPrime);

			pfMET.SetPtEtaPhiM(V_MetPrime.Pt(),0,V_MetPrime.Phi(),0);
			MET_pf = pfMET.Pt();

		}

		//========================    Electrons?  ================================//

		if (EleCount>=1)
		{
			Pt_ele1 = ElectronPt->at(v_idx_ele_final[0]);
			Eta_ele1 = ElectronEta->at(v_idx_ele_final[0]);
			Phi_ele1 = ElectronPhi->at(v_idx_ele_final[0]);
		}
		

		if (HEEPEleCount>=1)
		{
			Pt_HEEPele1 = ElectronPt->at(v_idx_ele_good_final[0]);
			Eta_HEEPele1 = ElectronEta->at(v_idx_ele_good_final[0]);
			Phi_HEEPele1 = ElectronPhi->at(v_idx_ele_good_final[0]);
			heepele1.SetPtEtaPhiM(Pt_HEEPele1,Eta_HEEPele1,Phi_HEEPele1,0.0);
		}
	

		//========================   At least 1 muon  ================================//

		if (MuonCount>=1)
		{
			// Quality Variables
			TrkD0_muon1 = MuonTrkD0->at(v_idx_muon_final[0]);
			NHits_muon1 = MuonTrkHits ->at(v_idx_muon_final[0]);
			Charge_muon1 = MuonCharge->at(v_idx_muon_final[0]);
			RelIso_muon1 = MuonRelIso->at(v_idx_muon_final[0]);
			TrkDZ_muon1 = MuonTrkDz->at(v_idx_muon_final[0]);
			TrkIso_muon1 = MuonTrkIso->at(v_idx_muon_final[0]);
			EcalIso_muon1 = MuonEcalIso->at(v_idx_muon_final[0]);
			HcalIso_muon1 = MuonHcalIso->at(v_idx_muon_final[0]);
			TrackerIsoSumPT_muon1 = MuonTrackerIsoSumPT->at(v_idx_muon_final[0]);
			ChiSq_muon1 = MuonGlobalChi2->at(v_idx_muon_final[0]);
            QOverPError_muon1 = MuonQOverPError->at(v_idx_muon_final[0]);
            PhiError_muon1  = MuonPhiError->at(v_idx_muon_final[0]);
            EtaError_muon1  = MuonEtaError->at(v_idx_muon_final[0]);
            PtError_muon1 = MuonPtError->at(v_idx_muon_final[0]);



			// muon Pt/Eta/Phi
			Pt_muon1 = MuonPt->at(v_idx_muon_final[0]);
			Phi_muon1 = MuonPhi->at(v_idx_muon_final[0]);
			Eta_muon1 = MuonEta->at(v_idx_muon_final[0]);

			// Other Variables
			muon1.SetPtEtaPhiM(Pt_muon1,Eta_muon1,Phi_muon1,0);

			deltaPhi_muon1pfMET = (pfMET.DeltaPhi(muon1));
			MT_muon1pfMET = TMass(Pt_muon1,MET_pf,deltaPhi_muon1pfMET);

			minval_muon1pfMET = Pt_muon1;
			if (MET_pf < Pt_muon1) minval_muon1pfMET = MET_pf;

			// Recoil Stuff
			Pt_W = (muon1 + pfMET).Pt();
			Phi_W = (muon1 + pfMET).Phi();

			TLorentzVector UW = -(pfMET + muon1);
			TLorentzVector BW = (muon1+pfMET);

			U1_W = (UW.Pt()) * (cos(UW.DeltaPhi(BW))) ;
			U2_W = (UW.Pt()) * (sin(UW.DeltaPhi(BW))) ;

			UdotMu = Pt_muon1*UW.Pt()*cos(UW.DeltaPhi(muon1));
			UdotMu_overmu = UW.Pt()*cos(UW.DeltaPhi(muon1));

		}

		//========================   At least 2 muon  ================================//

		if (MuonCount>=2)
		{
			// Quality Variables
			TrkD0_muon2 = MuonTrkD0->at(v_idx_muon_final[1]);
			NHits_muon2 = MuonTrkHits ->at(v_idx_muon_final[1]);
			Charge_muon2 = MuonCharge->at(v_idx_muon_final[1]);
			RelIso_muon2 = MuonRelIso->at(v_idx_muon_final[1]);
			TrkDZ_muon2 = MuonTrkDz->at(v_idx_muon_final[1]);
			TrkIso_muon2 = MuonTrkIso->at(v_idx_muon_final[1]);
			EcalIso_muon2 = MuonEcalIso->at(v_idx_muon_final[1]);
			HcalIso_muon2 = MuonHcalIso->at(v_idx_muon_final[1]);
			TrackerIsoSumPT_muon2 = MuonTrackerIsoSumPT->at(v_idx_muon_final[1]);
			ChiSq_muon2 = MuonGlobalChi2->at(v_idx_muon_final[1]);
            QOverPError_muon2 = MuonQOverPError->at(v_idx_muon_final[1]);
            PhiError_muon2  = MuonPhiError->at(v_idx_muon_final[1]);
            EtaError_muon2  = MuonEtaError->at(v_idx_muon_final[1]);
            PtError_muon2 = MuonPtError->at(v_idx_muon_final[1]);
			
			

			// muon Pt/Eta/Phi
			Pt_muon2 = MuonPt->at(v_idx_muon_final[1]);
			Phi_muon2 = MuonPhi->at(v_idx_muon_final[1]);
			Eta_muon2 = MuonEta->at(v_idx_muon_final[1]);

			// Other Variables
			muon2.SetPtEtaPhiM(Pt_muon2,Eta_muon2,Phi_muon2,0);

			deltaPhi_muon1pfMET = (pfMET.DeltaPhi(muon1));

			deltaPhi_muon1muon2 = (muon1.DeltaPhi(muon2));
			deltaR_muon1muon2 = muon1.DeltaR(muon2);
			M_muon1muon2 = (muon1+muon2).M();

			// Boson PT
			TLorentzVector UZ = -(pfMET + muon1 + muon2);
			TLorentzVector BZ = (muon1+muon2);

			U1_Z = (UZ.Pt()) * (cos(UZ.DeltaPhi(BZ))) ;
			U2_Z = (UZ.Pt()) * (sin(UZ.DeltaPhi(BZ))) ;

			Pt_Z = (muon1 + muon2).Pt();
			Phi_Z = (muon1 + muon2).Phi();

		}

		//========================   At least 1 PFJET  ================================//

		if (PFJetCount>=1)
		{

			// Jet Quality
			PFJetNeutralMultiplicity_pfjet1= PFJetNeutralMultiplicity->at(v_idx_pfjet_final[0]);
			PFJetNeutralHadronEnergyFraction_pfjet1= PFJetNeutralHadronEnergyFraction->at(v_idx_pfjet_final[0]);
			PFJetNeutralEmEnergyFraction_pfjet1= PFJetNeutralEmEnergyFraction->at(v_idx_pfjet_final[0]);
			PFJetChargedMultiplicity_pfjet1= PFJetChargedMultiplicity->at(v_idx_pfjet_final[0]);
			PFJetChargedHadronEnergyFraction_pfjet1= PFJetChargedHadronEnergyFraction->at(v_idx_pfjet_final[0]);
			PFJetChargedEmEnergyFraction_pfjet1= PFJetChargedEmEnergyFraction->at(v_idx_pfjet_final[0]);
			PFJetTrackAssociatedVertex_pfjet1 = PFJetBestVertexTrackAssociationIndex->at(v_idx_pfjet_final[0]);


			// Pt/Eta/Phi
			Pt_pfjet1 = PFJetPt->at(v_idx_pfjet_final[0]);
			Phi_pfjet1 = PFJetPhi->at(v_idx_pfjet_final[0]);
			Eta_pfjet1 = PFJetEta->at(v_idx_pfjet_final[0]);

			// Other Variables
			pfjet1.SetPtEtaPhiM(Pt_pfjet1,Eta_pfjet1,Phi_pfjet1,0);

			deltaPhi_pfjet1pfMET = (pfMET.DeltaPhi(pfjet1));
			MT_pfjet1pfMET = TMass(Pt_pfjet1,MET_pf,deltaPhi_pfjet1pfMET);
			BDisc_pfjet1 = PFJetTrackCountingHighEffBTag->at(v_idx_pfjet_final[0]);

		}

		//========================   At least 2 PFJET  ================================//

		if (PFJetCount>=2)
		{
			// Pt/Eta/Phi
			Pt_pfjet2 = PFJetPt->at(v_idx_pfjet_final[1]);
			Phi_pfjet2 = PFJetPhi->at(v_idx_pfjet_final[1]);
			Eta_pfjet2 = PFJetEta->at(v_idx_pfjet_final[1]);

			// Jet Quality
			PFJetNeutralMultiplicity_pfjet2= PFJetNeutralMultiplicity->at(v_idx_pfjet_final[1]);
			PFJetNeutralHadronEnergyFraction_pfjet2= PFJetNeutralHadronEnergyFraction->at(v_idx_pfjet_final[1]);
			PFJetNeutralEmEnergyFraction_pfjet2= PFJetNeutralEmEnergyFraction->at(v_idx_pfjet_final[1]);
			PFJetChargedMultiplicity_pfjet2= PFJetChargedMultiplicity->at(v_idx_pfjet_final[1]);
			PFJetChargedHadronEnergyFraction_pfjet2= PFJetChargedHadronEnergyFraction->at(v_idx_pfjet_final[1]);
			PFJetChargedEmEnergyFraction_pfjet2= PFJetChargedEmEnergyFraction->at(v_idx_pfjet_final[1]);
			PFJetTrackAssociatedVertex_pfjet2 = PFJetBestVertexTrackAssociationIndex->at(v_idx_pfjet_final[1]);

			// Other Variables
			pfjet2.SetPtEtaPhiM(Pt_pfjet2,Eta_pfjet2,Phi_pfjet2,0);

			BDisc_pfjet2 = PFJetTrackCountingHighEffBTag->at(v_idx_pfjet_final[1]);

			deltaPhi_pfjet2pfMET = (pfMET.DeltaPhi(pfjet2));
			MT_pfjet2pfMET = TMass(Pt_pfjet2,MET_pf,deltaPhi_pfjet2pfMET);

			deltaR_pfjet1pfjet2 = pfjet1.DeltaR(pfjet2);
			deltaPhi_pfjet1pfjet2 = (pfjet1.DeltaPhi(pfjet2));
			M_pfjet1pfjet2 = (pfjet1 + pfjet2).M();
		}

		//========================   1 Muon 1 Jet ================================//

		if ((MuonCount>0) && (PFJetCount> 0))
		{
			deltaPhi_muon1pfjet1 = (muon1.DeltaPhi(pfjet1));
			deltaR_muon1pfjet1 = (muon1.DeltaR(pfjet1));
			M_muon1pfjet1 = (pfjet1 + muon1).M();
			MT_muon1pfjet1 = TMass(Pt_pfjet1,Pt_muon1,deltaPhi_muon1pfjet1);
		}

		//========================   1 Muon 2 Jet ================================//

		if ((MuonCount>0) && (PFJetCount> 1))
		{
			deltaPhi_muon1pfjet2 = (muon1.DeltaPhi(pfjet2));
			deltaR_muon1pfjet2 = (muon1.DeltaR(pfjet2));
			M_muon1pfjet2 = (pfjet2 + muon1).M();
			MT_muon1pfjet2 = TMass(Pt_pfjet2,Pt_muon1,deltaPhi_muon1pfjet2);
			ST_pf_munu= Pt_muon1 + MET_pf + Pt_pfjet1 + Pt_pfjet2;
			M_mujetjet = (muon1 + pfjet1 +pfjet2).M();
			
			MET_lq = (-muon1 -pfjet1 -pfjet2).Pt();
			METRatio_lqpf = MET_lq/MET_pf;
			METRatio_lqcalo = MET_lq/MET_calo;
			
			M_muon1pfjet1pfjet2 = (muon1+pfjet1+pfjet2).M();
			
		}

		//========================   2 Muon 1 Jet ================================//

		if ((MuonCount>1) && (PFJetCount> 0))
		{
			deltaPhi_muon2pfjet1 = (muon2.DeltaPhi(pfjet1));
			deltaR_muon2pfjet1 = (muon2.DeltaR(pfjet1));
			M_muon2pfjet1 = (pfjet1+muon2).M();
			MT_muon2pfjet1 = TMass(Pt_pfjet1,Pt_muon2,deltaPhi_muon2pfjet1);
			M_muon1muon2pfjet1 = (muon1 + muon2 + pfjet1).M();

		}

		//========================   2 Muon 2 Jet ================================//

		if ((MuonCount>1) && (PFJetCount> 1))
		{
			deltaPhi_muon2pfjet2 = (muon2.DeltaPhi(pfjet2));
			deltaR_muon2pfjet2 = (muon2.DeltaR(pfjet2));
			ST_pf_mumu= Pt_muon1 + Pt_muon2 + Pt_pfjet1 + Pt_pfjet2;
			M_muon2pfjet2 = (pfjet2 + muon2).M();
			MT_muon2pfjet2 = TMass(Pt_pfjet2,Pt_muon2,deltaPhi_muon2pfjet2);

			M_muon1muon2pfjet1pfjet2 = (muon1+muon2+pfjet1+pfjet2).M();
		}
		
		//=========================   1 Electron 1 Muon 2 Jet ====================//

		if ((MuonCount>=1) && (PFJetCount>1) && (HEEPEleCount>=1))
		{
   		        ST_pf_emu = Pt_muon1 + Pt_pfjet1 + Pt_pfjet2 + Pt_HEEPele1;
				M_muon1HEEPele1 = (muon1 + heepele1).M();
				deltaR_muon1HEEPele1 = (heepele1).DeltaR(muon1);
				M_HEEPele1pfjet1_emuselection = (heepele1 + pfjet1).M();
				M_HEEPele1pfjet2_emuselection = (heepele1 + pfjet2).M();
		}

		//========================   LQ Mass Concepts ================================//

		// DiMuon, minimizing differene between mu-jet masses
		if ((MuonCount>1) && (PFJetCount> 1))
		{
			if (TMath::Abs(M_muon1pfjet1 - M_muon2pfjet2) < TMath::Abs(M_muon1pfjet2 - M_muon2pfjet1) )
			{
				M_bestmupfjet1_mumu = M_muon1pfjet1;
				M_bestmupfjet2_mumu = M_muon2pfjet2;
				RangeMass_BestLQCombo = TMath::Abs(M_muon1pfjet1 - M_muon2pfjet2);
				CenterMass_BestLQCombo = TMath::Abs(M_muon1pfjet1 + M_muon2pfjet2)/2.0;
				RangeCenterMassRatio_BestLQCombo = RangeMass_BestLQCombo/CenterMass_BestLQCombo;
			}

			if (TMath::Abs(M_muon1pfjet1 - M_muon2pfjet2) > TMath::Abs(M_muon1pfjet2 - M_muon2pfjet1) )
			{
				M_bestmupfjet1_mumu = M_muon2pfjet1;
				M_bestmupfjet2_mumu = M_muon1pfjet2;
				RangeMass_BestLQCombo = TMath::Abs(M_muon2pfjet1 - M_muon1pfjet2);
				CenterMass_BestLQCombo = TMath::Abs(M_muon2pfjet1 + M_muon1pfjet2)/2.0;
				RangeCenterMassRatio_BestLQCombo = RangeMass_BestLQCombo/CenterMass_BestLQCombo;
			}
		}
		
		LowestMass_BestLQCombo = M_bestmupfjet1_mumu;
		if (M_bestmupfjet1_mumu > M_bestmupfjet2_mumu) LowestMass_BestLQCombo = M_bestmupfjet2_mumu;

		AverageMass_BestLQCombo = 0.5*(M_bestmupfjet1_mumu + M_bestmupfjet2_mumu);

		// e-mu selection for Data-Driven ttbar
		if ((MuonCount>=1) && (PFJetCount>1) && (HEEPEleCount>=1))
		{
			if (TMath::Abs(M_HEEPele1pfjet1_emuselection - M_muon1pfjet2) < TMath::Abs(M_HEEPele1pfjet2_emuselection - M_muon1pfjet1) )
			{
				M_bestmuORelepfjet1_mumu_emuselection = M_HEEPele1pfjet1_emuselection;
				M_bestmuORelepfjet2_mumu_emuselection = M_muon1pfjet2;
			}

			if (TMath::Abs(M_HEEPele1pfjet1_emuselection - M_muon1pfjet2) > TMath::Abs(M_HEEPele1pfjet2_emuselection - M_muon1pfjet1) )
			{
				M_bestmuORelepfjet1_mumu_emuselection = M_HEEPele1pfjet2_emuselection;
				M_bestmuORelepfjet2_mumu_emuselection = M_muon1pfjet1;
			}
		}
		
		LowestMass_BestLQCombo_emuselection = M_bestmuORelepfjet1_mumu_emuselection;
		if (M_bestmuORelepfjet1_mumu_emuselection > M_bestmuORelepfjet2_mumu_emuselection) LowestMass_BestLQCombo_emuselection = M_bestmuORelepfjet2_mumu_emuselection;

		AverageMass_BestLQCombo = 0.5*( M_bestmuORelepfjet1_mumu_emuselection + M_bestmuORelepfjet2_mumu_emuselection);
	

		// Beta - Half production - minimize difference of transverse masses
		if ((MuonCount>0) && (PFJetCount> 1))
		{
			if (TMath::Abs(MT_muon1pfjet1 - MT_pfjet2pfMET) < TMath::Abs(MT_muon1pfjet2 - MT_pfjet1pfMET) )
			{
				M_bestmupfjet_munu= M_muon1pfjet1;
				RangeTransverseMass_BestLQCombo = TMath::Abs(MT_muon1pfjet1 - MT_pfjet2pfMET);
				CenterTransverseMass_BestLQCombo = TMath::Abs(MT_muon1pfjet1 + MT_pfjet2pfMET) / 2.0 ;
				RangeCenterTransverseMassRatio_BestLQCombo = RangeTransverseMass_BestLQCombo/CenterTransverseMass_BestLQCombo;
			}

			if (TMath::Abs(MT_muon1pfjet1 - MT_pfjet2pfMET) > TMath::Abs(MT_muon1pfjet2 - MT_pfjet1pfMET) )
			{
				M_bestmupfjet_munu= M_muon1pfjet2;
				RangeTransverseMass_BestLQCombo = TMath::Abs(MT_muon1pfjet2 - MT_pfjet1pfMET);
				CenterTransverseMass_BestLQCombo = TMath::Abs(MT_muon1pfjet2 + MT_pfjet1pfMET) / 2.0 ;
				RangeCenterTransverseMassRatio_BestLQCombo = RangeTransverseMass_BestLQCombo/CenterTransverseMass_BestLQCombo;
			}
		}
		
		// Nonsense for testing - test of jet masses
		
		TLorentzVector AllCaloJets,AllPFJets;
		
		for(unsigned int ijet = 0; ijet < PFJetPt->size(); ++ijet)
		{
			ThisPFJet.SetPtEtaPhiM((*PFJetPt)[ijet],(*PFJetEta)[ijet],(*PFJetPhi)[ijet],0);
			bool consider = true;
			
			for(unsigned int imuon = 0; imuon < MuonPt->size(); ++imuon)
			{
				ThisLepton.SetPtEtaPhiM(MuonPt->at(imuon),MuonEta->at(imuon), MuonPhi->at(imuon),0.0);
				JetLepDR = ThisLepton.DeltaR(ThisPFJet);
				if (JetLepDR < .2) consider = false;
			}
			for(unsigned int iele = 0; iele < ElectronPt->size(); ++iele)
			{
				ThisLepton.SetPtEtaPhiM(ElectronPt->at(iele),ElectronEta->at(iele),ElectronPhi->at(iele),0.0);
				JetLepDR = ThisLepton.DeltaR(ThisPFJet);
				if (JetLepDR < .2) consider = false;
			}
			if (consider)
			{
				AllPFJets = AllPFJets + ThisPFJet;
			}
		}
		
		for(unsigned int ijet = 0; ijet < CaloJetPt->size(); ++ijet)
		{
			ThisCaloJet.SetPtEtaPhiM((*CaloJetPt)[ijet],(*CaloJetEta)[ijet],(*CaloJetPhi)[ijet],0);
			AllCaloJets = AllCaloJets + ThisCaloJet;
		}

		M_AllCaloJet = AllCaloJets.M();
		M_AllPFJet = AllPFJets.M();
		Pt_AllCaloJet = AllCaloJets.Pt();	
		Pt_AllPFJet = AllPFJets.Pt();
		MetDirComp_AllCaloJet = Pt_AllCaloJet*cos(AllCaloJets.DeltaPhi(caloMET));
		MetDirComp_AllPFJet = Pt_AllPFJet*cos(AllPFJets.DeltaPhi(pfMET));
		MetDirCompOverMET_AllCaloJet = MetDirComp_AllCaloJet/(caloMET.Pt());
		MetDirCompOverMET_AllPFJet = MetDirComp_AllPFJet/(pfMET.Pt());

		
		//std::cout<<M_AllCaloJet<<"   "<<M_AllPFJet<<std::endl;
		if ((Pt_muon2 < 40.0 ) && (Pt_HEEPele1<40) && ( MET_pf < 45.0) ) continue;
		if ( Pt_pfjet2 < 30.0  ) continue;
		if (ST_pf_mumu < 250.0 && ST_pf_munu < 250.0 && ST_pf_emu < 250.0) continue;
	//	if (Pt_muon2 < 30.0 && Pt_genmuon2 < 30.0 && Pt_genMET < 40.0 && MET_pf < 40.0) continue; 

		tree->Fill();			 // FILL FINAL TREE

	}

	tree->Write();
	file1->Close();
}
