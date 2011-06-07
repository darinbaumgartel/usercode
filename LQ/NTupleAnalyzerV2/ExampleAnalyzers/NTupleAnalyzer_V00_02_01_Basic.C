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
#include "JSONFilterFunction.h"

#define BRANCH(bname) Double_t bname = -99999.12345; tree->Branch(#bname,& bname," bname /D ");
#define VRESET(vname) vname = -99999.12345;

float TMass(float Pt1, float Pt2, float DPhi12)
{
	return sqrt( 2*Pt2*Pt1*(1-cos(DPhi12)) );
}


// Recoil Correction Function for U1
float F_U1Prime(float P)
{
	float newU1 =+(0.444896)/(0.860121)*(0.766883)+(-0.808669)/(-0.834743)*(-0.789876)*(P)+(-0.00219386)/(-0.00292147)*(-0.00311338)*(pow(P,2.0));
	float newsU1 =+(5.8243)/(4.67677)*(4.39298)+(0.0542917)/(0.0868557)*(0.0919195)*(P)+(0.000606564)/(0.000149318)*(0.000734456)*(pow(P,2.0));
	return gRandom->Gaus(newU1,newsU1);
}


// Recoil Correction Function for U1
float F_U2Prime(float P)
{
	float newU2 =+(-0.257587)/(-0.0294369)*(-0.0447997)+(0.0318125)/(0.00367515)*(0.00493626)*(P)+(-0.00054509)/(-5.08201e-05)*(-0.000106641)*(pow(P,2.0));
	float newsU2 =+(5.94468)/(4.80093)*(4.45511)+(0.00960053)/(0.0373637)*(0.063819)*(P)+(0.000780935)/(0.000569114)*(0.00042653)*(pow(P,2.0));
	return gRandom->Gaus(newU2,newsU2);
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
	BRANCH(MuonCount); BRANCH(EleCount); BRANCH(PFJetCount); BRANCH(BpfJetCount);

	// Leading muon 1
	BRANCH(TrkD0_muon1);     BRANCH(NHits_muon1);   BRANCH(TrkDZ_muon1);   BRANCH(ChiSq_muon1);
	BRANCH(TrkIso_muon1); BRANCH(EcalIso_muon1); BRANCH(HcalIso_muon1); BRANCH(RelIso_muon1);
	BRANCH(Phi_muon1);    BRANCH(Eta_muon1);     BRANCH(Pt_muon1);      BRANCH(Charge_muon1);

	// Leading muon 2
	BRANCH(TrkD0_muon2);     BRANCH(NHits_muon2);   BRANCH(TrkDZ_muon2);   BRANCH(ChiSq_muon2);
	BRANCH(TrkIso_muon2); BRANCH(EcalIso_muon2); BRANCH(HcalIso_muon2); BRANCH(RelIso_muon2);
	BRANCH(Phi_muon2);    BRANCH(Eta_muon2);     BRANCH(Pt_muon2);      BRANCH(Charge_muon2);

	// PFJet 1
	BRANCH(Phi_pfjet1); BRANCH(Eta_pfjet1); BRANCH(Pt_pfjet1); BRANCH(BDisc_pfjet1);
	BRANCH(PFJetNeutralMultiplicity_pfjet1);         BRANCH(PFJetNeutralHadronEnergyFraction_pfjet1);
	BRANCH(PFJetNeutralEmEnergyFraction_pfjet1);     BRANCH(PFJetChargedMultiplicity_pfjet1);
	BRANCH(PFJetChargedHadronEnergyFraction_pfjet1); BRANCH(PFJetChargedEmEnergyFraction_pfjet1);

	// PFJet 2
	BRANCH(Phi_pfjet2); BRANCH(Eta_pfjet2); BRANCH(Pt_pfjet2); BRANCH(BDisc_pfjet2);
	BRANCH(PFJetNeutralMultiplicity_pfjet2);         BRANCH(PFJetNeutralHadronEnergyFraction_pfjet2);
	BRANCH(PFJetNeutralEmEnergyFraction_pfjet2);     BRANCH(PFJetChargedMultiplicity_pfjet2);
	BRANCH(PFJetChargedHadronEnergyFraction_pfjet2); BRANCH(PFJetChargedEmEnergyFraction_pfjet2);

	// Electron (If any)
	BRANCH(Pt_ele1);

	// Event Information
	BRANCH(run_number); BRANCH(event_number); BRANCH(bx);
	BRANCH(xsection);   BRANCH(weight);
	BRANCH(Events_AfterLJ); BRANCH(Events_Orig);
	BRANCH(N_Vertices);

	// PFMET
	BRANCH(MET_pf); BRANCH(Phi_MET_pf);

	// Delta Phi Variables
	BRANCH(deltaPhi_muon1muon2);  BRANCH(deltaPhi_pfjet1pfjet2);
	BRANCH(deltaPhi_muon1pfMET);  BRANCH(deltaPhi_muon2pfMET);
	BRANCH(deltaPhi_pfjet1pfMET); BRANCH(deltaPhi_pfjet2pfMET);
	BRANCH(deltaPhi_muon1pfjet1); BRANCH(deltaPhi_muon1pfjet2);
	BRANCH(deltaPhi_muon2pfjet1); BRANCH(deltaPhi_muon2pfjet2);

	// Delta R Variables
	BRANCH(deltaR_muon1muon2);  BRANCH(deltaR_pfjet1pfjet2);
	BRANCH(deltaR_muon1pfjet1); BRANCH(deltaR_muon1pfjet2);
	BRANCH(deltaR_muon2pfjet1); BRANCH(deltaR_muon2pfjet2);
	BRANCH(deltaR_muon1closestPFJet);

	// Mass Combinations
	BRANCH(M_muon1muon2);  BRANCH(M_pfjet1pfjet2);
	BRANCH(M_muon1pfjet1); BRANCH(M_muon1pfjet2);
	BRANCH(M_muon2pfjet1); BRANCH(M_muon2pfjet2);
	BRANCH(M_muon1muon2pfjet1pfjet2);
	BRANCH(M_bestmupfjet1_mumu); BRANCH(M_bestmupfjet2_mumu);
	BRANCH(M_bestmupfjet_munu);

	// Transverse Mass Combinations
	BRANCH(MT_muon1pfMET);
	BRANCH(MT_pfjet1pfMET); BRANCH(MT_pfjet2pfMET);
	BRANCH(MT_muon1pfjet1); BRANCH(MT_muon1pfjet2);
	BRANCH(MT_muon2pfjet1); BRANCH(MT_muon2pfjet2);

	// ST Variables
	BRANCH(ST_pf_mumu); BRANCH(ST_pf_munu);

	// Other Variables
	BRANCH(minval_muon1pfMET);
	BRANCH(Pt_Z);  BRANCH(Pt_W);
	BRANCH(Phi_Z); BRANCH(Phi_W);
  BRANCH(N_PileUpInteractions);

	// Generator Level Variables
	BRANCH(Pt_genjet1);     BRANCH(Pt_genjet2);
	BRANCH(Pt_genmuon1);    BRANCH(Pt_genmuon2);
	BRANCH(Phi_genmuon1);   BRANCH(Phi_genmuon2);
	BRANCH(Eta_genmuon1);   BRANCH(Eta_genmuon2);
	BRANCH(Pt_genMET);      BRANCH(Phi_genMET);    BRANCH(Eta_genMET);
	BRANCH(Pt_genneutrino); BRANCH(Phi_genneutrino); BRANCH(Eta_genneutrino);
	BRANCH(genWTM);
	BRANCH(Pt_Z_gen);       BRANCH(Pt_W_gen);
	BRANCH(Phi_Z_gen);      BRANCH(Phi_W_gen);

	// Recoil variables
	BRANCH(U1_Z_gen); BRANCH(U2_Z_gen);
	BRANCH(U1_W_gen); BRANCH(U2_W_gen);
	BRANCH(U1_Z);     BRANCH(U2_Z);
	BRANCH(U1_W);     BRANCH(U2_W);
	BRANCH(UdotMu);   BRANCH(UdotMu_overmu);

	//===================================================================================================
	//===================================================================================================

	//===================================================================================================
	//        SETUP WITH SOME TEMPLATE INPUTS AND THRESHOLDS
	//===================================================================================================

	// "desired_luminosity" is a PlaceHolder that gets replaced from the python template replicator
	Double_t lumi=desired_luminosity;

	// Number of events passing LJ Filter
//	Events_AfterLJ = 1.0*(fChain->GetEntries());

	// PlaceHolder, values stored in bookkeeping/NTupleInfo.csv
	Events_Orig = Numberofevents;

	// Another placeHolder. Needed because recoil corrections only get applied to W MC.
	bool IsW = IsItWMC;

	xsection = crosssection;	 // Another PlaceHolder for the cross sections in bookkeeping/NTupleInfo.csv
	Double_t eff = efficiency;	 // Another PlaceHolder, for filter efficiency or what have you. Multiply by sigma for "effective cross section"

	//	Event Weight Calculation
	weight = eff*lumi*xsection/Events_Orig;

	int xx=0;					 //dummy variable used for progress %

	// Display status to screen
//	std::cout<<"            "<<std::endl;
//	std::cout<<" Evaluating for: placeholder \n MC events: "<<Events_AfterLJ
//		<< " \n Actual Events: "<<weight*Events_Orig<<" \n Integrated Luminosity: "
//		<<lumi<<" pb^(-1) \n Cross Section: "<<xsection<<" pb "<<std::endl;
//	std::cout<<"            "<<std::endl;

	//===================================================================================================
	//===================================================================================================

	//===================================================================================================
	//           LOOP OVER ENTRIES AND MAKE MAIN CALCULATIONS
	//===================================================================================================

	if (fChain == 0) return;	 //check for correctly assigned chain from h file

	Long64_t nentries = fChain->GetEntriesFast();
	Long64_t nbytes = 0, nb = 0;

	//N=1000;  /// TEST>>>>>> COMMENT THIS ALWAYS

	for (Long64_t jentry=0; jentry<nentries;jentry++)
	{
		//-------------------------------------------------------
		// Show progress so you know the program hasn't failed...
		//-------------------------------------------------------
//		for (xx=0; xx<100; xx=xx+1)
//		{
//			if ((100*jentry/(Events_AfterLJ)>xx)&&(100*(jentry-1)/(Events_AfterLJ)<xx))
//			{
//				std::cout<<xx<<" % complete"<<std::endl;
//			}
//		}
		//-------------------------------------------------------
		//-------------------------------------------------------

		Long64_t ientry = LoadTree(jentry);
		if (ientry < 0) break;
		nb = fChain->GetEntry(jentry);   nbytes += nb;

		//		if (jentry>1000) break;

		// Important Event Informations
		run_number = run;
		event_number = event;
		bx = bunch;

		//========================     HLT Conditions   ================================//

		//		if (run_number<1000)
		//		{
		//			if ( ((*HLTResults)[60] ==1) ||((*HLTResults)[0] ==1) ) precut_HLT=1.0;
		//			else continue;
		//		}

		//		if ((run_number>1000)&&(run_number<146000))
		//		{
		//			if ((*HLTResults)[60] ==1) precut_HLT=1.0;
		//			else continue;
		//		}

		//		if ((run_number>146000)&&(run_number<147455))
		//		{
		//			if ((*HLTResults)[61] ==1) precut_HLT=1.0;
		//			else continue;
		//		}

		//		if (run_number>=147455)
		//		{
		//			if ((*HLTResults)[66] ==1) precut_HLT=1.0;
		//			else continue;
		//		}


		//========================     JSON   Conditions   ================================//

		if (isData){
		bool KeepEvent = PassFilter(run, ls);
		if (!KeepEvent) continue;
		}
		//========================     Vertex Conditions   ================================//

		if ( isBeamScraping ) continue;

		bool vtxFound = false;
		for(unsigned int ivtx = 0; ivtx != VertexZ->size(); ++ivtx)
		{
			if ( VertexIsFake->at(ivtx) == true ) continue;
			if ( VertexNDF->at(ivtx) <= 4.0 ) continue;
			if ( TMath::Abs(VertexZ->at(ivtx)) > 24.0 ) continue;
			if ( TMath::Abs(VertexRho->at(ivtx)) >= 2.0 ) continue;
			vtxFound = true;
			break;
		}
		if ( !vtxFound ) continue;

		N_Vertices = VertexZ->size();

		if (!isData) N_PileUpInteractions = 1.0*PileUpInteractions;

		//========================     Electron Conditions   ================================//

		vector<int> v_idx_ele_final;
		// check if there are electrons
		int nelectrons = 0;
		for(unsigned int iele = 0; iele < ElectronPt->size(); ++iele)
		{
			//			if ( ElectronPt->at(iele) < 15.0 ) continue;
			if ( (ElectronPassID->at(iele) & 1 << 5 ) && ElectronOverlaps->at(iele) == 0 )
			{
				++nelectrons;

				v_idx_ele_final.push_back(iele);
			}
		}

		//========================      Muon Conditions   ================================//

		vector<int> v_idx_muon_final;
		// container for muons
		vector<TLorentzVector> muons;
		int iMUON = -1;
		// select muons

		bool checkPT = true;	 // Pt requirement only on first muon at this stage

		for(unsigned int imuon = 0; imuon < MuonPt->size(); ++imuon)
		{

			float muonPt = MuonPt->at(imuon);
			float muonEta = MuonEta->at(imuon);

			if (checkPT && (muonPt < 30.0) ) continue;

			bool quality =
								 // Fiducial Region
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
			muon.SetPtEtaPhiM( MuonPt -> at(imuon), MuonEta-> at(imuon),    MuonPhi-> at(imuon),    0);

			muons.push_back(muon);
			checkPT=false;

			v_idx_muon_final.push_back(imuon);
		}						 // loop over muons

		MuonCount = 1.0*v_idx_muon_final.size();

		if ( MuonCount < 1 ) continue;

		TLorentzVector muon = muons[0];

		//========================     PFJet Conditions   ================================//

		// Get Good Jets in general

		deltaR_muon1closestPFJet = 999.9;
		float deltaR_thisjet = 9999.9;
		vector<TLorentzVector> jets;
		vector<int> v_idx_pfjet_prefinal;
		vector<int> v_idx_pfjet_final_unseparated;
		vector<int> v_idx_pfjet_final;
		BpfJetCount = 0.0;

		// Initial Jet Quality Selection
		for(unsigned int ijet = 0; ijet < PFJetPt->size(); ++ijet)
		{
			double jetPt = PFJetPt -> at(ijet);
			double jetEta = PFJetEta -> at(ijet);

			if ( jetPt < 30.0 ) continue;
			if ( fabs(jetEta) > 3.0 ) continue;

			if (PFJetPassLooseID->at(ijet) != 1) continue;
			//if (PFJetPassTightID->at(ijet) != 1) continue;

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

				if (thisdeltar < 0.3)
				{
					jetstoremove.push_back(jetindex);
				}
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

			deltaR_thisjet =  newjet.DeltaR(muon);
			if ( deltaR_thisjet < deltaR_muon1closestPFJet)  deltaR_muon1closestPFJet = deltaR_thisjet ;

//			if ( deltaR_thisjet < 0.5 ) continue;

			if ( PFJetTrackCountingHighEffBTag->at(jetindex) > 1.7 )
			{
				BpfJetCount = BpfJetCount + 1.0;
			}

			// if we are here, the jet is good
			v_idx_pfjet_final.push_back(jetindex);
		}
		PFJetCount = 1.0*v_idx_pfjet_final.size();

		//========================     Generator Level Module  ================================//

		float piover2 = 3.1415926/2.0;
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
		VRESET(genWTM);
		VRESET(Pt_Z_gen);       VRESET(Pt_W_gen);
		VRESET(Phi_Z_gen);      VRESET(Phi_W_gen);

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
				int pdgIdMother = GenParticlePdgId->at(motherIndex);

				//muon
								 // && TMath::Abs(pdgIdMother) == 23 ) {
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

			Pt_Z_gen = (v_GenMuon1 + v_GenMuon2).Pt();
			Phi_Z_gen = (v_GenMuon1 + v_GenMuon2).Phi();

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

				float U1Phi = - BW_gen.Phi();
				float U2Phi = BW_gen.Phi() + piover2;

				if ((BW_gen.DeltaPhi(UW_gen)) < 0)   U2Phi = BW_gen.Phi() - piover2;

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

		//========================     Set variables to zero  ================================//

		// Leading muon 1
		VRESET(TrkD0_muon1);     VRESET(NHits_muon1);   VRESET(TrkDZ_muon1);   VRESET(ChiSq_muon1);
		VRESET(TrkIso_muon1); VRESET(EcalIso_muon1); VRESET(HcalIso_muon1); VRESET(RelIso_muon1);
		VRESET(Phi_muon1);    VRESET(Eta_muon1);     VRESET(Pt_muon1);      VRESET(Charge_muon1);

		// Leading muon 2
		VRESET(TrkD0_muon2);     VRESET(NHits_muon2);   VRESET(TrkDZ_muon2);   VRESET(ChiSq_muon2);
		VRESET(TrkIso_muon2); VRESET(EcalIso_muon2); VRESET(HcalIso_muon2); VRESET(RelIso_muon2);
		VRESET(Phi_muon2);    VRESET(Eta_muon2);     VRESET(Pt_muon2);      VRESET(Charge_muon2);

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
		// PFMET
		VRESET(MET_pf); VRESET(Phi_MET_pf);

		// Delta Phi Variables
		VRESET(deltaPhi_muon1muon2);  VRESET(deltaPhi_pfjet1pfjet2);
		VRESET(deltaPhi_muon1pfMET);  VRESET(deltaPhi_muon2pfMET);
		VRESET(deltaPhi_pfjet1pfMET); VRESET(deltaPhi_pfjet2pfMET);
		VRESET(deltaPhi_muon1pfjet1); VRESET(deltaPhi_muon1pfjet2);
		VRESET(deltaPhi_muon2pfjet1); VRESET(deltaPhi_muon2pfjet2);

		// Delta R Variables
		VRESET(deltaR_muon1muon2);  VRESET(deltaR_pfjet1pfjet2);
		VRESET(deltaR_muon1pfjet1); VRESET(deltaR_muon1pfjet2);
		VRESET(deltaR_muon2pfjet1); VRESET(deltaR_muon2pfjet2);
		VRESET(deltaR_muon1closestPFJet);

		// Mass Combinations
		VRESET(M_muon1muon2);  VRESET(M_pfjet1pfjet2);
		VRESET(M_muon1pfjet1); VRESET(M_muon1pfjet2);
		VRESET(M_muon2pfjet1); VRESET(M_muon2pfjet2);
		VRESET(M_muon1muon2pfjet1pfjet2);
		VRESET(M_bestmupfjet1_mumu); VRESET(M_bestmupfjet2_mumu);
		VRESET(M_bestmupfjet_munu);

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

		// Recoil variables
		VRESET(U1_Z);     VRESET(U2_Z);
		VRESET(U1_W);     VRESET(U2_W);
		VRESET(UdotMu);   VRESET(UdotMu_overmu);

		//===================================================================================================
		//      Run the Calculations of physical variables using selected particles.
		//===================================================================================================

		// 4-Vectors for Particles
		TLorentzVector jet1, jet2, pfjet1, pfjet2, muon1,muon3, caloMET,muon2,pfMET,tcMET;

		//========================     MET Basics  ================================//

		MET_pf = PFMET->at(0);
		pfMET.SetPtEtaPhiM(MET_pf,0.0,PFMETPhi->at(0),0.0);

		//========================     MET Recoil Correction  ================================//

		// Recoil Corrections
		if (IsW && DoRecoilCorrections && true)
		{

			// Very careful calculation of the geometry of the recoil vectors.
			float U1Phi =  BW_gen.Phi() + 2*piover2;
			if (U1Phi> (2*piover2)) U1Phi = U1Phi - 4*piover2;

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

			// Get the new recoil vectors
			float U2Phi = check_phi_u2;
			float reco_Pt_W = (muon1test + v_GenNu).Pt();
			float U1Prime = F_U1Prime(reco_Pt_W);
			float U2Prime = F_U2Prime(reco_Pt_W);

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
			ChiSq_muon1 = MuonGlobalChi2->at(v_idx_muon_final[0]);

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
			ChiSq_muon2 = MuonGlobalChi2->at(v_idx_muon_final[1]);

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

		}

		//========================   2 Muon 1 Jet ================================//

		if ((MuonCount>1) && (PFJetCount> 0))
		{
			deltaPhi_muon2pfjet1 = (muon2.DeltaPhi(pfjet1));
			deltaR_muon2pfjet1 = (muon2.DeltaR(pfjet1));
			M_muon2pfjet1 = (pfjet1+muon2).M();
			MT_muon2pfjet1 = TMass(Pt_pfjet1,Pt_muon2,deltaPhi_muon2pfjet1);
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

		//========================   LQ Mass Concepts ================================//

		// DiMuon, minimizing differene between mu-jet masses
		if ((MuonCount>1) && (PFJetCount> 1))
		{
			if (abs(M_muon1pfjet1 - M_muon2pfjet2) < abs(M_muon1pfjet2 - M_muon2pfjet1) )
			{
				M_bestmupfjet1_mumu = M_muon1pfjet1;
				M_bestmupfjet2_mumu = M_muon2pfjet2;
			}

			if (abs(M_muon1pfjet1 - M_muon2pfjet2) > abs(M_muon1pfjet2 - M_muon2pfjet1) )
			{
				M_bestmupfjet1_mumu = M_muon2pfjet1;
				M_bestmupfjet2_mumu = M_muon1pfjet2;
			}
		}

		// Beta - Half production - minimize difference of transverse masses
		if ((MuonCount>0) && (PFJetCount> 1))
		{
			if (abs(MT_muon1pfjet1 - MT_pfjet2pfMET) < abs(MT_muon1pfjet2 - MT_pfjet1pfMET) )
			{
				M_bestmupfjet_munu= M_muon1pfjet1;
			}

			if (abs(MT_muon1pfjet1 - MT_pfjet2pfMET) > abs(MT_muon1pfjet2 - MT_pfjet1pfMET) )
			{
				M_bestmupfjet_munu= M_muon1pfjet2;
			}
		}

		tree->Fill();			 // FILL FINAL TREE

	}

	tree->Write();
	file1->Close();
}
