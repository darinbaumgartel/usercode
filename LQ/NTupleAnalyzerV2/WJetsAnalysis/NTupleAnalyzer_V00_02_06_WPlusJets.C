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

	//===================================================================================================
	//        Initial Setup and Special Functions
	//===================================================================================================

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

Double_t JERFactor(Double_t J_ETA)
{
if ((abs(J_ETA)<0.5))                     return rr->Gaus(1.052,0.063);
if ((abs(J_ETA)>0.5)&&(abs(J_ETA)<1.1))   return rr->Gaus(1.057,0.057);
if ((abs(J_ETA)>1.1)&&(abs(J_ETA)<1.7))   return rr->Gaus(1.096,0.065);
if ((abs(J_ETA)>1.7)&&(abs(J_ETA)<2.3))   return rr->Gaus(1.134,0.094);
if ((abs(J_ETA)>2.3)&&(abs(J_ETA)<5.0))   return rr->Gaus(1.288,0.200);
return 1.0;
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

int CustomHeepID(double e_pt, double e_pt_real, double e_eta, bool e_ecaldriven , double e_dphi_sc, double e_deta_sc, double e_hoe, double e_sigmann, double e_e1x5_over_5x5, double e_e2x5_over_5x5, double e_em_had1iso , double e_had2iso, double e_trkiso, double e_losthits )
{
	int isgood = 1;

	if (e_pt_real<20.0) isgood = 0; // OK
	if (e_pt<20.0) isgood = 0; // OK
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

	Double_t weight=0.0;
	Double_t xsection=0.0;
	//Double_t Events_AfterLJ=0.0;
	Double_t Events_Orig=0.0;
	Double_t N_PileUpInteractions=0.0;
	Double_t Pt_HEEPele1=0.0;

	// Particle Counts
	BRANCH(MuonCount); BRANCH(EleCount); BRANCH(HEEPEleCount); BRANCH(PFJetCount); BRANCH(BpfJetCount);
	BRANCH(GlobalMuonCount); BRANCH(TrackerMuonCount);
	BRANCH(PFJetRawCount);  
	BRANCH(GlobalMuonCount10GeV);


	// Event Information
	UInt_t run_number,event_number,ls_number;
	tree->Branch("event_number",&event_number,"event_number/i");
	tree->Branch("run_number",&run_number,"run_number/i");
	tree->Branch("ls_number",&ls_number,"ls_number/i");
	BRANCH(bx);	
	BRANCH(N_Vertices);
	BRANCH(N_GoodVertices);
	BRANCH(weight_pu_central); BRANCH(weight_pu_sysplus8); BRANCH(weight_pu_sysminus8);
	BRANCH(pass_HBHENoiseFilter); BRANCH(pass_isBPTX0); BRANCH(pass_passBeamHaloFilterLoose); 
	BRANCH(pass_passBeamHaloFilterTight);
	BRANCH(pass_isTrackingFailure);

	// PFMET
	BRANCH(MET_pfsig);	BRANCH(MET_pf_charged);

	// Event Flags
	BRANCH(FailIDPFThreshold);

	// Generator Level Variables
	
	BRANCH(Pt_genjet1);  BRANCH(Phi_genjet1);  BRANCH(Eta_genjet1);  
	BRANCH(Pt_genjet2);  BRANCH(Phi_genjet2);  BRANCH(Eta_genjet2);  
	BRANCH(Pt_genjet3);  BRANCH(Phi_genjet3);  BRANCH(Eta_genjet3);  
	BRANCH(Pt_genjet4);  BRANCH(Phi_genjet4);  BRANCH(Eta_genjet4);  
	BRANCH(Pt_genjet5);  BRANCH(Phi_genjet5);  BRANCH(Eta_genjet5);  
	//BRANCH(Pt_genjet6);  BRANCH(Phi_genjet6);  BRANCH(Eta_genjet6);  
	
	BRANCH(Pt_genmuon1);  BRANCH(Phi_genmuon1);  BRANCH(Eta_genmuon1);  
	BRANCH(Pt_genmuon2);  BRANCH(Phi_genmuon2);  BRANCH(Eta_genmuon2);  
	
	BRANCH(Pt_genMET);  BRANCH(Phi_genMET);  

	BRANCH(MT_genmuon1genMET);
	BRANCH(Pt_W_gen);  BRANCH(Phi_W_gen);

	// Reco Level Variables
	
	BRANCH(Pt_pfjet1);  BRANCH(Phi_pfjet1);  BRANCH(Eta_pfjet1);  
	BRANCH(Pt_pfjet2);  BRANCH(Phi_pfjet2);  BRANCH(Eta_pfjet2);  
	BRANCH(Pt_pfjet3);  BRANCH(Phi_pfjet3);  BRANCH(Eta_pfjet3);  
	BRANCH(Pt_pfjet4);  BRANCH(Phi_pfjet4);  BRANCH(Eta_pfjet4);  
	BRANCH(Pt_pfjet5);  BRANCH(Phi_pfjet5);  BRANCH(Eta_pfjet5);  
	//BRANCH(Pt_pfjet6);  BRANCH(Phi_pfjet6);  BRANCH(Eta_pfjet6);  
	
	BRANCH(Pt_muon1);  BRANCH(Phi_muon1);  BRANCH(Eta_muon1);  
	BRANCH(Pt_muon2);  BRANCH(Phi_muon2);  BRANCH(Eta_muon2);  
	
	BRANCH(Pt_MET);  BRANCH(Phi_MET);  

	BRANCH(MT_muon1MET);
	BRANCH(Pt_W);  BRANCH(Phi_W);
	

	// Trigger and other
	BRANCH(LowestUnprescaledTriggerPass); 

	Double_t LowestUnprescaledTrigger=0.0;//BRANCH(LowestUnprescaledTrigger); 
	Double_t Closest40UnprescaledTrigger=0.0;//BRANCH(Closest40UnprescaledTrigger);
	Double_t Closest40UnprescaledTriggerPass=0.0;//BRANCH(Closest40UnprescaledTriggerPass);
	Double_t HLTIsoMu24Pass=0.0;//RANCH(HLTIsoMu24Pass);
	Double_t HLTMu40TriggerPass=0.0;//BRANCH(HLTMu40TriggerPass);
	Double_t HT_genMG=0.0;//BRANCH(HT_genMG);
	
	//===================================================================================================
	//===================================================================================================

	//===================================================================================================
	//        SETUP WITH SOME TEMPLATE INPUTS AND THRESHOLDS
	//===================================================================================================

	// "desired_luminosity" is a PlaceHolder that gets replaced from the python template replicator
	Double_t lumi=desired_luminosity;

	// PlaceHolder, values stored in bookkeeping/NTupleInfo.csv
	Events_Orig = Numberofevents;

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
		//========================     Vertex Conditions  And Flags  ================================//

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
		//pass_EcalMaskedCellDRFilter = 1.0*passEcalMaskedCellDRFilter ; 
		//pass_CaloBoundaryDRFilter = 1.0*passCaloBoundaryDRFilter ; 
		pass_passBeamHaloFilterLoose = 1.0*passBeamHaloFilterLoose ; 
		pass_passBeamHaloFilterTight = 1.0*passBeamHaloFilterTight ;
		pass_isTrackingFailure = 1.00*(1.0-1.0*isTrackingFailure);		
		
		//========================     PileUp Technology  ================================//
		
		
		N_PileUpInteractions = 0.0;

		if (!isData)
		{
			for(unsigned int iPU = 0; iPU != PileUpInteractions->size(); ++iPU)
			{
				if (TMath::Abs(PileUpOriginBX->at(iPU)) == 0) N_PileUpInteractions += (1.0*(PileUpInteractions->at(iPU)));
			}	
		}
		

		weight_pu_central = weight;
		if ((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)) weight_pu_central  *=(0.0136759963465);
		if ((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)) weight_pu_central  *=(0.145092627325);
		if ((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)) weight_pu_central  *=(0.337346053675);
		if ((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)) weight_pu_central  *=(0.603889700177);
		if ((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)) weight_pu_central  *=(0.875723164145);
		if ((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)) weight_pu_central  *=(1.09904167986);
		if ((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)) weight_pu_central  *=(1.25430629491);
		if ((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)) weight_pu_central  *=(1.34642557836);
		if ((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)) weight_pu_central  *=(1.39979322363);
		if ((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)) weight_pu_central  *=(1.43532953354);
		if ((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)) weight_pu_central  *=(1.47049703593);
		if ((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)) weight_pu_central  *=(1.51604545424);
		if ((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)) weight_pu_central  *=(1.57633567564);
		if ((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)) weight_pu_central  *=(1.64932013381);
		if ((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)) weight_pu_central  *=(1.74029438919);
		if ((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)) weight_pu_central  *=(1.83791180719);
		if ((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)) weight_pu_central  *=(1.94039579764);
		if ((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)) weight_pu_central  *=(2.04245281118);
		if ((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)) weight_pu_central  *=(2.13680461818);
		if ((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)) weight_pu_central  *=(2.22395017393);
		if ((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)) weight_pu_central  *=(2.29776136337);
		if ((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)) weight_pu_central  *=(2.34107958833);
		if ((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)) weight_pu_central  *=(2.37047306281);
		if ((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)) weight_pu_central  *=(2.38365361416);
		if ((N_PileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)) weight_pu_central  *=(2.37251953266);
		if ((N_PileUpInteractions > 24.5)*(N_PileUpInteractions < 25.5)) weight_pu_central  *=(2.33390734715);
		if ((N_PileUpInteractions > 25.5)*(N_PileUpInteractions < 26.5)) weight_pu_central  *=(2.28287109918);
		if ((N_PileUpInteractions > 26.5)*(N_PileUpInteractions < 27.5)) weight_pu_central  *=(2.18527775378);
		if ((N_PileUpInteractions > 27.5)*(N_PileUpInteractions < 28.5)) weight_pu_central  *=(2.09984989719);
		if ((N_PileUpInteractions > 28.5)*(N_PileUpInteractions < 29.5)) weight_pu_central  *=(2.02417217124);
		if ((N_PileUpInteractions > 29.5)*(N_PileUpInteractions < 30.5)) weight_pu_central  *=(1.89559469244);
		if ((N_PileUpInteractions > 30.5)*(N_PileUpInteractions < 31.5)) weight_pu_central  *=(1.73994553659);
		if ((N_PileUpInteractions > 31.5)*(N_PileUpInteractions < 32.5)) weight_pu_central  *=(1.60146781888);
		if ((N_PileUpInteractions > 32.5)*(N_PileUpInteractions < 33.5)) weight_pu_central  *=(1.5415176127);
		if ((N_PileUpInteractions > 33.5)*(N_PileUpInteractions < 34.5)) weight_pu_central  *=(1.38880554853);
		if (N_PileUpInteractions > 34.5) weight_pu_central *= 0.0;
		
		
		weight_pu_sysplus8 = weight;
		if ((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)) weight_pu_sysplus8 *=(0.00924647898767);
		if ((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)) weight_pu_sysplus8 *=(0.103765308587);
		if ((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)) weight_pu_sysplus8 *=(0.254901026276);
		if ((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)) weight_pu_sysplus8 *=(0.480371942144);
		if ((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)) weight_pu_sysplus8 *=(0.729944556297);
		if ((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)) weight_pu_sysplus8 *=(0.954968986548);
		if ((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)) weight_pu_sysplus8 *=(1.13004026908);
		if ((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)) weight_pu_sysplus8 *=(1.25116215302);
		if ((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)) weight_pu_sysplus8 *=(1.33545960398);
		if ((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)) weight_pu_sysplus8 *=(1.40112202125);
		if ((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)) weight_pu_sysplus8 *=(1.46629994308);
		if ((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)) weight_pu_sysplus8 *=(1.54467848996);
		if ((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)) weight_pu_sysplus8 *=(1.64461047702);
		if ((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)) weight_pu_sysplus8 *=(1.7680582782);
		if ((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)) weight_pu_sysplus8 *=(1.9248181748);
		if ((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)) weight_pu_sysplus8 *=(2.10637260323);
		if ((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)) weight_pu_sysplus8 *=(2.31374222506);
		if ((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)) weight_pu_sysplus8 *=(2.54319600245);
		if ((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)) weight_pu_sysplus8 *=(2.78724430301);
		if ((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)) weight_pu_sysplus8 *=(3.04707340275);
		if ((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)) weight_pu_sysplus8 *=(3.31429303739);
		if ((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)) weight_pu_sysplus8 *=(3.56161966349);
		if ((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)) weight_pu_sysplus8 *=(3.80974218256);
		if ((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)) weight_pu_sysplus8 *=(4.05230970884);
		if ((N_PileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)) weight_pu_sysplus8 *=(4.27119855299);
		if ((N_PileUpInteractions > 24.5)*(N_PileUpInteractions < 25.5)) weight_pu_sysplus8 *=(4.45358283315);
		if ((N_PileUpInteractions > 25.5)*(N_PileUpInteractions < 26.5)) weight_pu_sysplus8 *=(4.6210083076);
		if ((N_PileUpInteractions > 26.5)*(N_PileUpInteractions < 27.5)) weight_pu_sysplus8 *=(4.69553893978);
		if ((N_PileUpInteractions > 27.5)*(N_PileUpInteractions < 28.5)) weight_pu_sysplus8 *=(4.79226541944);
		if ((N_PileUpInteractions > 28.5)*(N_PileUpInteractions < 29.5)) weight_pu_sysplus8 *=(4.90898557824);
		if ((N_PileUpInteractions > 29.5)*(N_PileUpInteractions < 30.5)) weight_pu_sysplus8 *=(4.88722270965);
		if ((N_PileUpInteractions > 30.5)*(N_PileUpInteractions < 31.5)) weight_pu_sysplus8 *=(4.77074865948);
		if ((N_PileUpInteractions > 31.5)*(N_PileUpInteractions < 32.5)) weight_pu_sysplus8 *=(4.67125617297);
		if ((N_PileUpInteractions > 32.5)*(N_PileUpInteractions < 33.5)) weight_pu_sysplus8 *=(4.78457737387);
		if ((N_PileUpInteractions > 33.5)*(N_PileUpInteractions < 34.5)) weight_pu_sysplus8 *=(4.58784771674);
		if (N_PileUpInteractions > 34.5) weight_pu_sysplus8 *= 0.0;
		
		
		weight_pu_sysminus8 = weight;
		if ((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)) weight_pu_sysminus8 *=(0.0201084522235);
		if ((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)) weight_pu_sysminus8 *=(0.201872953791);
		if ((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)) weight_pu_sysminus8 *=(0.444291440305);
		if ((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)) weight_pu_sysminus8 *=(0.754784951423);
		if ((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)) weight_pu_sysminus8 *=(1.04300038865);
		if ((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)) weight_pu_sysminus8 *=(1.25373948702);
		if ((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)) weight_pu_sysminus8 *=(1.37815071794);
		if ((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)) weight_pu_sysminus8 *=(1.43249643277);
		if ((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)) weight_pu_sysminus8 *=(1.44824842983);
		if ((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)) weight_pu_sysminus8 *=(1.44760397441);
		if ((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)) weight_pu_sysminus8 *=(1.44595859288);
		if ((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)) weight_pu_sysminus8 *=(1.45056585209);
		if ((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)) weight_pu_sysminus8 *=(1.46233900245);
		if ((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)) weight_pu_sysminus8 *=(1.47682664198);
		if ((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)) weight_pu_sysminus8 *=(1.49703207679);
		if ((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)) weight_pu_sysminus8 *=(1.51206676472);
		if ((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)) weight_pu_sysminus8 *=(1.52066555932);
		if ((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)) weight_pu_sysminus8 *=(1.51950731213);
		if ((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)) weight_pu_sysminus8 *=(1.50475499659);
		if ((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)) weight_pu_sysminus8 *=(1.47887521537);
		if ((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)) weight_pu_sysminus8 *=(1.43996103898);
		if ((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)) weight_pu_sysminus8 *=(1.38034035275);
		if ((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)) weight_pu_sysminus8 *=(1.31320230704);
		if ((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)) weight_pu_sysminus8 *=(1.2392809902);
		if ((N_PileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)) weight_pu_sysminus8 *=(1.15650697488);
		if ((N_PileUpInteractions > 24.5)*(N_PileUpInteractions < 25.5)) weight_pu_sysminus8 *=(1.06581520421);
		if ((N_PileUpInteractions > 25.5)*(N_PileUpInteractions < 26.5)) weight_pu_sysminus8 *=(0.975973223375);
		if ((N_PileUpInteractions > 26.5)*(N_PileUpInteractions < 27.5)) weight_pu_sysminus8 *=(0.874112959041);
		if ((N_PileUpInteractions > 27.5)*(N_PileUpInteractions < 28.5)) weight_pu_sysminus8 *=(0.785480306938);
		if ((N_PileUpInteractions > 28.5)*(N_PileUpInteractions < 29.5)) weight_pu_sysminus8 *=(0.707777917329);
		if ((N_PileUpInteractions > 29.5)*(N_PileUpInteractions < 30.5)) weight_pu_sysminus8 *=(0.619354107892);
		if ((N_PileUpInteractions > 30.5)*(N_PileUpInteractions < 31.5)) weight_pu_sysminus8 *=(0.531056657066);
		if ((N_PileUpInteractions > 31.5)*(N_PileUpInteractions < 32.5)) weight_pu_sysminus8 *=(0.456479768112);
		if ((N_PileUpInteractions > 32.5)*(N_PileUpInteractions < 33.5)) weight_pu_sysminus8 *=(0.410264344317);
		if ((N_PileUpInteractions > 33.5)*(N_PileUpInteractions < 34.5)) weight_pu_sysminus8 *=(0.345060491391);
		if (N_PileUpInteractions > 34.5) weight_pu_sysminus8 *= 0.0;
		


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
			int filterjetcount = 0;
			for(unsigned int ijet = 0; ijet < PFJetPt->size(); ++ijet)
			{
				if (filterjetcount >=6) continue;
				if (PFJetPt->at(ijet) < 20.0) continue;
				if (PFJetPassLooseID->at(ijet) != 1) continue;		
				if ( fabs(PFJetEta->at(ijet)) > 2.4 ) continue;
				filterjetcount += 1;
				
				bool consider = true;
				TLorentzVector ThisPFJet;
				Double_t JetLepDR;
				ThisPFJet.SetPtEtaPhiM((*PFJetPt)[ijet],(*PFJetEta)[ijet],(*PFJetPhi)[ijet],0);

				for(unsigned int imuon = 0; imuon < MuonPt->size(); ++imuon)
				{
					TLorentzVector ThisLepton;	
					ThisLepton.SetPtEtaPhiM(MuonPt->at(imuon),MuonEta->at(imuon), MuonPhi->at(imuon),0.0);
					JetLepDR = ThisLepton.DeltaR(ThisPFJet);
					if (JetLepDR < .3) consider = false;
				}
				for(unsigned int iele = 0; iele < ElectronPt->size(); ++iele)
				{
					TLorentzVector ThisLepton;	
					ThisLepton.SetPtEtaPhiM(ElectronPt->at(iele),ElectronEta->at(iele),ElectronPhi->at(iele),0.0);
					JetLepDR = ThisLepton.DeltaR(ThisPFJet);
					if (JetLepDR < .3) consider = false;
				}
				
				if (!consider) continue;
				
				
				double NewJetRescalingFactor = JetRescaleFactor;
				
				if (false)
					{
					NewJetRescalingFactor = 1.0+NewJesUncertainty((JetRescaleFactor - 1.0), (*PFJetPtRaw)[ijet], (*PFJetEta)[ijet]);
					if (JetRescaleFactor < 1.0) NewJetRescalingFactor = 2.0 - NewJetRescalingFactor;
					}
				
				double NewJetPT = (*PFJetPt)[ijet];
				//double NewJetETA = (*PFJetEta)[ijet];


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
				if (false)
				{
					if (SmallestDeltaR<0.5) Standard_rescale = 0.1;
				}
				Double_t JetAdjustmentFactor = GetRecoGenJetScaleFactor(PFJetPt->at(ijet),ClosestGenJetPT,Standard_rescale);
				NewJetPT *=JetAdjustmentFactor;
				JetAdjustedMET = PropagatePTChangeToMET(JetAdjustedMET.Pt(),  JetAdjustedMET.Phi(), NewJetPT, (*PFJetPt)[ijet], PFJetPhi->at(ijet));
		
				if (JetSmearFactor > 0.0){

					Double_t JetEta = fabs(PFJetEta->at(ijet));
					Double_t Systematic_rescale = 	JERFactor(JetEta);				
					Double_t JetAdjustmentFactorSys = GetRecoGenJetScaleFactor(PFJetPt->at(ijet),ClosestGenJetPT,Systematic_rescale);
					NewJetPT *=JetAdjustmentFactorSys;
				
				}
				(*PFJetPt)[ijet] = NewJetPT ;	
			}
		}

		(*PFMET)[0] = JetAdjustedMET.Pt();
		(*PFMETPhi)[0] = JetAdjustedMET.Phi();
		
		//========================     Muon Rescaling / Smearing Sequence   ================================//

		TLorentzVector MuAdjustedMET;
		MuAdjustedMET.SetPtEtaPhiM(PFMET->at(0),0.0,PFMETPhi->at(0),0);
		
		if (!isData)
		{
			for(unsigned int imuon = 0; imuon < MuonPt->size(); ++imuon)
			{
				Double_t muonPt = MuonPt->at(imuon);
				Double_t muonEta = MuonEta->at(imuon);
				
				if  (muonPt < 20.0)  continue;
				if  ( fabs(muonEta) > 2.1 )      continue;
	
				bool PassGlobalTightPrompt =
					MuonIsGlobal ->at(imuon) == 1 &&
					MuonIsTracker ->at(imuon) == 1 &&
					//fabs(MuonRelIso->at(imuon)) < 0.1 &&
					(((MuonTrackerIsoSumPT->at(imuon))/muonPt) < 0.05) &&                             // Disable for EWK
					//((MuonHcalIso->at(imuon) + MuonTrkIso->at(imuon))/muonPt) < 0.15;  // Enable for EWK
					MuonTrkHitsTrackerOnly ->at(imuon) >= 11   ;                         
	
				bool PassPOGTight =
					MuonStationMatches->at(imuon) > 1 && 
					fabs(MuonPrimaryVertexDXY ->at(imuon)) < 0.1  &&
					MuonGlobalChi2 ->at(imuon) < 10.0 &&                         /// Disable for EWK
					MuonPixelHitCount ->at(imuon) >=1 &&
					MuonGlobalTrkValidHits->at(imuon)>=1 ;
	
				if ( ! (PassGlobalTightPrompt && PassPOGTight) ) continue;
			
							
				double NewMuonPT =  ScaleObject((*MuonPt)[imuon],MuonRescaleFactor); 
				NewMuonPT =  SmearObject(NewMuonPT,MuonSmearFactor); 
				MuAdjustedMET = PropagatePTChangeToMET(MuAdjustedMET.Pt(),  MuAdjustedMET.Phi(), NewMuonPT, (*MuonPt)[imuon], MuonPhi->at(imuon));
				(*MuonPt)[imuon] = NewMuonPT ;	
			}
		}
		(*PFMET)[0] = MuAdjustedMET.Pt();
		(*PFMETPhi)[0] = MuAdjustedMET.Phi();

		//========================    CaloJet Matching to PFJET   ================================//

		vector<int> PFJetCaloMatches;


		for(unsigned int ijet = 0; ijet < PFJetPt->size(); ++ijet)
		{
			TLorentzVector ThisPFJet;
			ThisPFJet.SetPtEtaPhiM((*PFJetPt)[ijet],(*PFJetEta)[ijet],(*PFJetPhi)[ijet],0);
			
			int closestcalojet = -1;
			Double_t SmallestDeltaR = 9999.9999;
			for(unsigned int icalojet = 0; icalojet < CaloJetPt->size(); ++icalojet)
			{
				if (CaloJetPassLooseID->at(icalojet)!=1) continue;
				TLorentzVector thisCaloJet;
				thisCaloJet.SetPtEtaPhiM(CaloJetPt->at(icalojet),CaloJetEta->at(icalojet),CaloJetPhi->at(icalojet),0);
				Double_t ThisCaloJetDR = fabs((thisCaloJet).DeltaR(ThisPFJet));
				if (ThisCaloJetDR<SmallestDeltaR) 
				{
					SmallestDeltaR = ThisCaloJetDR;
					closestcalojet = icalojet;
				}
			}
			PFJetCaloMatches.push_back(closestcalojet);
		}
		
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

			if  (CustomHeepID(e_pt,e_pt_real, e_eta, e_ecaldriven , e_dphi_sc, e_deta_sc, e_hoe, e_sigmann, e_e1x5_over_5x5, e_e2x5_over_5x5, e_em_had1iso , e_had2iso, e_trkiso, e_missinghits ) )
			{
				v_idx_ele_final.push_back(iele);
			}
		}

		EleCount = 1.0*v_idx_ele_final.size();
		

		//========================     Stricter Electron Conditions   =============================//
		
		vector<int> v_idx_ele_good_final;

		for(unsigned int iele = 0; iele < ElectronPt->size(); ++iele)
		{
			if (fabs(ElectronEta->at(iele))>2.1) continue;
			
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

		  
		  if ( CustomHeepID(e_pt,e_pt_real, e_eta, e_ecaldriven , e_dphi_sc, e_deta_sc, e_hoe, e_sigmann, e_e1x5_over_5x5, e_e2x5_over_5x5, e_em_had1iso , e_had2iso, e_trkiso, e_missinghits ) )  
		    {		      
		      v_idx_ele_good_final.push_back(iele);  
		    }
		}
		HEEPEleCount = 1.0*v_idx_ele_good_final.size();

		//========================      Muon Conditions   ================================//

		vector<TLorentzVector> RecoMuons, RecoJets;
		vector<int> v_idx_muon_final;
		bool checkPT = true;	 // Pt requirement only on first muon at this stage
		
		// SubRoutine for Muon Counts
		GlobalMuonCount = 0.0;
		GlobalMuonCount10GeV = 0.0;
		TrackerMuonCount=0.0;
		
		for(unsigned int imuon = 0; imuon < MuonPt->size(); ++imuon)
		{
			if (MuonIsGlobal  ->at(imuon) == 1) GlobalMuonCount += 1.0;
			if (MuonIsTracker ->at(imuon) == 1) TrackerMuonCount += 1.0;
			if ((MuonIsGlobal->at(imuon) == 1) && (MuonPt->at(imuon) > 10.0)) GlobalMuonCount10GeV += 1.0;
			
			Double_t muonPt = MuonPt->at(imuon);
			Double_t muonEta = MuonEta->at(imuon);

			if (checkPT && (muonPt < 45.0) ) continue;
			if  ( fabs(muonEta) > 2.1 )      continue;

			bool PassGlobalTightPrompt =
				MuonIsGlobal ->at(imuon) == 1 &&
				MuonIsTracker ->at(imuon) == 1 &&
				//fabs(MuonRelIso->at(imuon)) < 0.1 &&
				(((MuonTrackerIsoSumPT->at(imuon))/muonPt) < 0.05) &&                             // Disable for EWK
				//((MuonHcalIso->at(imuon) + MuonTrkIso->at(imuon))/muonPt) < 0.15;  // Enable for EWK
				MuonTrkHitsTrackerOnly ->at(imuon) >= 11   ;                         

			bool PassPOGTight =
				MuonStationMatches->at(imuon) > 1 && 
				fabs(MuonPrimaryVertexDXY ->at(imuon)) < 0.1  &&
				MuonGlobalChi2 ->at(imuon) < 10.0 &&                         // Disable for EWK
				MuonPixelHitCount ->at(imuon) >=1 &&
				MuonGlobalTrkValidHits->at(imuon)>=1 ;

			if ( ! (PassGlobalTightPrompt && PassPOGTight) ) continue;
			TLorentzVector muon;
			muon.SetPtEtaPhiM( MuonPt -> at(imuon), MuonEta-> at(imuon),    MuonPhi-> at(imuon),    0);
			RecoMuons.push_back(muon);
			v_idx_muon_final.push_back(imuon);
			if (v_idx_muon_final.size()>=1) checkPT=false;
		}						 // loop over muons

		MuonCount = 1.0*v_idx_muon_final.size();

		if ( MuonCount < 1 ) continue;

		int LeadMuonVertex=MuonVtxIndex->at(v_idx_muon_final[0]);
		

		//========================     PFJet Conditions   ================================//
		// Get Good Jets in general

		vector<TLorentzVector> jets;
		vector<int> v_idx_pfjet_prefinal;
		vector<int> v_idx_pfjet_final;
		BpfJetCount = 0.0;
		FailIDPFThreshold = -1.0;
		TLorentzVector CurrentLepton,CurrentPFJet;


		// Initial Jet Quality Selection
		for(unsigned int ijet = 0; ijet < PFJetPt->size(); ++ijet)
		{
			double jetPt = PFJetPt -> at(ijet);
			double jetEta = PFJetEta -> at(ijet);
			CurrentPFJet.SetPtEtaPhiM((*PFJetPt)[ijet],(*PFJetEta)[ijet],(*PFJetPhi)[ijet],0);

			if (PFJetBestVertexTrackAssociationIndex->at(ijet) != LeadMuonVertex) continue;

			bool IsLepton = false;

			if ((PFJetPassLooseID->at(ijet) != 1)&&(PFJetPt->at(ijet) > FailIDPFThreshold)&&(!IsLepton)) FailIDPFThreshold = PFJetPt->at(ijet);
			//if ( jetPt < 30.0 ) continue;			
			if ( fabs(jetEta) > 2.4 ) continue;
			if (PFJetPassLooseID->at(ijet) != 1) continue;   
			v_idx_pfjet_prefinal.push_back(ijet);
		}
		// Filter out jets that are actually muons or electrons
		TLorentzVector thisjet, thismu, thise;

		int muindex = 99;
		int eindex = 99;
		int jetindex = 99;

		for(unsigned int ijet=0; ijet<v_idx_pfjet_prefinal.size(); ijet++)
		{
			jetindex = v_idx_pfjet_prefinal[ijet];
			thisjet.SetPtEtaPhiM((*PFJetPt)[jetindex],(*PFJetEta)[jetindex],(*PFJetPhi)[jetindex],0);

			bool KeepJet=true;

			for(unsigned int imu=0; imu<v_idx_muon_final.size(); imu++)
			{
				muindex = v_idx_muon_final[imu];
				thismu.SetPtEtaPhiM(MuonPt->at(muindex),MuonEta->at(muindex),MuonPhi->at(muindex),0);
				if (thismu.Pt()<20.0) continue;
				if (thismu.DeltaR(thisjet) < 0.3)		KeepJet=false;
			}

			for(unsigned int ie=0; ie<v_idx_ele_good_final.size(); ie++)
			{
				eindex = v_idx_ele_good_final[ie];
				thise.SetPtEtaPhiM(ElectronPt->at(eindex),ElectronEta->at(eindex),ElectronPhi->at(eindex),0);
				if (thise.DeltaR(thisjet) < 0.3)		KeepJet=false;
			}
			
			if (!KeepJet) continue;
			if ( PFJetTrackCountingHighEffBTag->at(jetindex) > 2.0 ) BpfJetCount = BpfJetCount + 1.0;
			RecoJets.push_back(thisjet);
			v_idx_pfjet_final.push_back(jetindex);
		}
		PFJetCount = 1.0*v_idx_pfjet_final.size();

		//========================     Generator Level Module  ================================//

		if (!isData)
		{

			vector<TLorentzVector> GenMuons, GenJets, SortedGenMuons, SortedGenJets, GenMuNeutrinos;

			Pt_genjet1 = 0;       Phi_genjet1 = 0;       Eta_genjet1 = 0;
			Pt_genjet2 = 0;       Phi_genjet2 = 0;       Eta_genjet2 = 0;
			Pt_genjet3 = 0;       Phi_genjet3 = 0;       Eta_genjet3 = 0;
			Pt_genjet4 = 0;       Phi_genjet4 = 0;       Eta_genjet4 = 0;
			Pt_genjet5 = 0;       Phi_genjet5 = 0;       Eta_genjet5 = 0;
			Pt_genjet6 = 0;       Phi_genjet6 = 0;       Eta_genjet6 = 0;
			
			Pt_genmuon1 = 0;      Phi_genmuon1 = 0;      Eta_genmuon1 = 0;
			Pt_genmuon2 = 0;      Phi_genmuon2 = 0;      Eta_genmuon2 = 0;

			HT_genMG = 0.0;

			for(unsigned int ip = 0; ip != GenParticlePdgId->size(); ++ip)
			{
				int pdgId = GenParticlePdgId->at(ip);
				int motherIndex = GenParticleMotherIndex->at(ip);
				if ( motherIndex == -1 ) continue;

				if ( TMath::Abs(pdgId) == 13 )
				{
					TLorentzVector thisgenmuon;
					thisgenmuon.SetPtEtaPhiM(GenParticlePt->at(ip),GenParticleEta->at(ip),GenParticlePhi->at(ip),0.0);
					GenMuons.push_back(thisgenmuon);
				}
				if ( TMath::Abs(pdgId) == 14 )
				{
					TLorentzVector thisgenneutrino;
					thisgenneutrino.SetPtEtaPhiM(GenParticlePt->at(ip),GenParticleEta->at(ip),GenParticlePhi->at(ip),0.0);
					GenMuNeutrinos.push_back(thisgenneutrino);
				}
			}

			for(unsigned int ijet = 0; ijet != GenJetPt->size(); ++ijet)
			{
				if (fabs(GenJetEta->at(ijet))>2.4) continue;
				TLorentzVector(thisgenjet);
				thisgenjet.SetPtEtaPhiM(GenJetPt->at(ijet),GenJetEta->at(ijet),GenJetPhi->at(ijet),0.0);
				GenJets.push_back(thisgenjet);
			}


			for(unsigned int irecjet = 0; irecjet != RecoJets.size(); ++irecjet)
			{
				TLorentzVector matchedgenjet;
				matchedgenjet.SetPtEtaPhiM(0,0,0,0);
				float closestDR=9999.9;
				unsigned int closestindex=9999;
				
				for(unsigned int igenjet = 0; igenjet != GenJets.size(); ++igenjet)
				{
					float thisDR=(GenJets[igenjet].DeltaR(RecoJets[irecjet]));
					if (thisDR<closestDR)
					{
						closestDR=thisDR;
						closestindex=igenjet;
					}
				}
				
				if (closestDR<0.5) matchedgenjet=GenJets[closestindex];
				SortedGenJets.push_back(matchedgenjet);
			}
			
			for(unsigned int irecmuon = 0; irecmuon != RecoMuons.size(); ++irecmuon)
			{
				TLorentzVector matchedgenmuon;
				matchedgenmuon.SetPtEtaPhiM(0,0,0,0);
				float closestDR=9999.9;
				unsigned int closestindex=9999;
				
				for(unsigned int igenmuon = 0; igenmuon != GenMuons.size(); ++igenmuon)
				{
					float thisDR=(GenMuons[igenmuon].DeltaR(RecoMuons[irecmuon]));
					if (thisDR<closestDR)
					{
						closestDR=thisDR;
						closestindex=igenmuon;
					}
				}
				
				if (closestDR<0.5) matchedgenmuon=GenMuons[closestindex];
				SortedGenMuons.push_back(matchedgenmuon);
			}
			
			// Assign Muon Variables
			if (MuonCount>=1)	Pt_genmuon1  =	SortedGenMuons[0].Pt();
			if (MuonCount>=1)	Eta_genmuon1 =	SortedGenMuons[0].Eta();
			if (MuonCount>=1)	Phi_genmuon1 =	SortedGenMuons[0].Phi();
			if (MuonCount>=2)	Pt_genmuon2  =	SortedGenMuons[1].Pt();
			if (MuonCount>=2)	Eta_genmuon2 =	SortedGenMuons[1].Eta();
			if (MuonCount>=2)	Phi_genmuon2 =	SortedGenMuons[1].Phi();
						
			// Assign Jet Variables		
			if (PFJetCount>=1)	Pt_genjet1  =	SortedGenJets[0].Pt();
			if (PFJetCount>=1)	Eta_genjet1 =	SortedGenJets[0].Eta();
			if (PFJetCount>=1)	Phi_genjet1 =	SortedGenJets[0].Phi();
			if (PFJetCount>=2)	Pt_genjet2  =	SortedGenJets[1].Pt();
			if (PFJetCount>=2)	Eta_genjet2 =	SortedGenJets[1].Eta();
			if (PFJetCount>=2)	Phi_genjet2 =	SortedGenJets[1].Phi();
			if (PFJetCount>=3)	Pt_genjet3  =	SortedGenJets[2].Pt();
			if (PFJetCount>=3)	Eta_genjet3 =	SortedGenJets[2].Eta();
			if (PFJetCount>=3)	Phi_genjet3 =	SortedGenJets[2].Phi();
			if (PFJetCount>=4)	Pt_genjet4  =	SortedGenJets[3].Pt();
			if (PFJetCount>=4)	Eta_genjet4 =	SortedGenJets[3].Eta();
			if (PFJetCount>=4)	Phi_genjet4 =	SortedGenJets[3].Phi();
			if (PFJetCount>=5)	Pt_genjet5  =	SortedGenJets[4].Pt();
			if (PFJetCount>=5)	Eta_genjet5 =	SortedGenJets[4].Eta();
			if (PFJetCount>=5)	Phi_genjet5 =	SortedGenJets[4].Phi();
			if (PFJetCount>=6)	Pt_genjet6  =	SortedGenJets[5].Pt();
			if (PFJetCount>=6)	Eta_genjet6 =	SortedGenJets[5].Eta();
			if (PFJetCount>=6)	Phi_genjet6 =	SortedGenJets[5].Phi();

			Pt_genMET = GenMETTrue->at(0);
			Phi_genMET = GenMETPhiTrue->at(0);
			
			MT_genmuon1genMET =  TMass(Pt_genmuon1,Pt_genMET, fabs(Phi_genmuon1 - Phi_genMET) );
			
			TLorentzVector  v_GenMet;
			v_GenMet.SetPtEtaPhiM ( Pt_genMET, 0, Phi_genMET,0 );
			Pt_W_gen = (SortedGenMuons[0]+v_GenMet).Pt();
			Phi_W_gen = (SortedGenMuons[0]+v_GenMet).Phi();

		}


		//========================     Calculate Reco Variables  ================================//

	
			Pt_pfjet1 = 0;       Phi_pfjet1 = 0;       Eta_pfjet1 = 0;
			Pt_pfjet2 = 0;       Phi_pfjet2 = 0;       Eta_pfjet2 = 0;
			Pt_pfjet3 = 0;       Phi_pfjet3 = 0;       Eta_pfjet3 = 0;
			Pt_pfjet4 = 0;       Phi_pfjet4 = 0;       Eta_pfjet4 = 0;
			Pt_pfjet5 = 0;       Phi_pfjet5 = 0;       Eta_pfjet5 = 0;
			Pt_pfjet6 = 0;       Phi_pfjet6 = 0;       Eta_pfjet6 = 0;
			
			Pt_muon1 = 0;      Phi_muon1 = 0;      Eta_muon1 = 0;
			Pt_muon2 = 0;      Phi_muon2 = 0;      Eta_muon2 = 0;
	
			Pt_MET = 0;        Phi_MET = 0;        
	
			// Assign Muon Variables	
			if (MuonCount>=1)	Pt_muon1  =	RecoMuons[0].Pt();
			if (MuonCount>=1)	Eta_muon1 =	RecoMuons[0].Eta();
			if (MuonCount>=1)	Phi_muon1 =	RecoMuons[0].Phi();
			if (MuonCount>=2)	Pt_muon2  =	RecoMuons[1].Pt();
			if (MuonCount>=2)	Eta_muon2 =	RecoMuons[1].Eta();
			if (MuonCount>=2)	Phi_muon2 =	RecoMuons[1].Phi();
						
			// Assign Jet Variables		
			if (PFJetCount>=1)	Pt_pfjet1  =	RecoJets[0].Pt();
			if (PFJetCount>=1)	Eta_pfjet1 =	RecoJets[0].Eta();
			if (PFJetCount>=1)	Phi_pfjet1 =	RecoJets[0].Phi();
			if (PFJetCount>=2)	Pt_pfjet2  =	RecoJets[1].Pt();
			if (PFJetCount>=2)	Eta_pfjet2 =	RecoJets[1].Eta();
			if (PFJetCount>=2)	Phi_pfjet2 =	RecoJets[1].Phi();
			if (PFJetCount>=3)	Pt_pfjet3  =	RecoJets[2].Pt();
			if (PFJetCount>=3)	Eta_pfjet3 =	RecoJets[2].Eta();
			if (PFJetCount>=3)	Phi_pfjet3 =	RecoJets[2].Phi();
			if (PFJetCount>=4)	Pt_pfjet4  =	RecoJets[3].Pt();
			if (PFJetCount>=4)	Eta_pfjet4 =	RecoJets[3].Eta();
			if (PFJetCount>=4)	Phi_pfjet4 =	RecoJets[3].Phi();
			if (PFJetCount>=5)	Pt_pfjet5  =	RecoJets[4].Pt();
			if (PFJetCount>=5)	Eta_pfjet5 =	RecoJets[4].Eta();
			if (PFJetCount>=5)	Phi_pfjet5 =	RecoJets[4].Phi();
			if (PFJetCount>=6)	Pt_pfjet6  =	RecoJets[5].Pt();
			if (PFJetCount>=6)	Eta_pfjet6 =	RecoJets[5].Eta();
			if (PFJetCount>=6)	Phi_pfjet6 =	RecoJets[5].Phi();
	
			Pt_MET = PFMET->at(0);
			Phi_MET = PFMETPhi->at(0);
			
			MT_muon1MET =  TMass(Pt_muon1,Pt_MET, fabs(Phi_muon1 - Phi_MET) );
			
			TLorentzVector  v_Met;
			v_Met.SetPtEtaPhiM ( Pt_MET, 0, Phi_MET,0 );
			Pt_W = (RecoMuons[0]+v_Met).Pt();
			Phi_W = (RecoMuons[0]+v_Met).Phi();
	
			MET_pfsig = PFMETSig->at(0);
			MET_pf_charged = PFMETCharged->at(0);
			
			Pt_HEEPele1=0.0;
			if (HEEPEleCount>=1) Pt_HEEPele1 = ElectronPt->at(v_idx_ele_good_final[0]);
	
		if (Pt_muon1<45) continue;
		//if (Pt_MET<30) continue;
		if (Pt_muon2>20) continue;
		//if (MT_muon1MET<50) continue;
		if (Pt_HEEPele1>20.0) continue;
		//if (MT_muon1MET>110) continue;
		tree->Fill();
	}

	tree->Write();
	file1->Close();
}
