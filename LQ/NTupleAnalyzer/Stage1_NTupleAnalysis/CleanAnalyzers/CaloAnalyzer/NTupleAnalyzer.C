#define NTupleAnalyzer_placeholder_cxx
#include "NTupleAnalyzer_placeholder.h"
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

#define BRANCH(bname) Double_t bname = -99999.12345; tree->Branch(#bname,& bname," bname /D ");
#define VRESET(vname) vname = -99999.12345;

 bool UseCalo = false;


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

void NTupleAnalyzer_placeholder::Loop()
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
	BRANCH(MuonCount); BRANCH(EleCount); BRANCH(CaloJetCount); BRANCH(BcaloJetCount);

	// Leading muon 1
	BRANCH(TrkD0_muon1);     BRANCH(NHits_muon1);   BRANCH(TrkDZ_muon1);   BRANCH(ChiSq_muon1);
	BRANCH(TrkIso_muon1); BRANCH(EcalIso_muon1); BRANCH(HcalIso_muon1); BRANCH(RelIso_muon1);
	BRANCH(Phi_muon1);    BRANCH(Eta_muon1);     BRANCH(Pt_muon1);      BRANCH(Charge_muon1);

	// Leading muon 2
	BRANCH(TrkD0_muon2);     BRANCH(NHits_muon2);   BRANCH(TrkDZ_muon2);   BRANCH(ChiSq_muon2);
	BRANCH(TrkIso_muon2); BRANCH(EcalIso_muon2); BRANCH(HcalIso_muon2); BRANCH(RelIso_muon2);
	BRANCH(Phi_muon2);    BRANCH(Eta_muon2);     BRANCH(Pt_muon2);      BRANCH(Charge_muon2);

	// CaloJet 1
	BRANCH(Phi_caloJet1); BRANCH(Eta_caloJet1); BRANCH(Pt_caloJet1); BRANCH(BDisc_caloJet1);
	BRANCH(CaloJetNeutralMultiplicity_caloJet1);         BRANCH(CaloJetNeutralHadronEnergyFraction_caloJet1);
	BRANCH(CaloJetNeutralEmEnergyFraction_caloJet1);     BRANCH(CaloJetChargedMultiplicity_caloJet1);
	BRANCH(CaloJetChargedHadronEnergyFraction_caloJet1); BRANCH(CaloJetChargedEmEnergyFraction_caloJet1);

	// CaloJet 2
	BRANCH(Phi_caloJet2); BRANCH(Eta_caloJet2); BRANCH(Pt_caloJet2); BRANCH(BDisc_caloJet2);
	BRANCH(CaloJetNeutralMultiplicity_caloJet2);         BRANCH(CaloJetNeutralHadronEnergyFraction_caloJet2);
	BRANCH(CaloJetNeutralEmEnergyFraction_caloJet2);     BRANCH(CaloJetChargedMultiplicity_caloJet2);
	BRANCH(CaloJetChargedHadronEnergyFraction_caloJet2); BRANCH(CaloJetChargedEmEnergyFraction_caloJet2);

	// Electron (If any)
	BRANCH(Pt_ele1);

	// Event Information
	BRANCH(run_number); BRANCH(event_number); BRANCH(bx);
	BRANCH(xsection);   BRANCH(weight);
	BRANCH(Events_AfterLJ); BRANCH(Events_Orig);
	BRANCH(N_Vertices);

	// PFMET
	BRANCH(MET_calo); BRANCH(Phi_MET_calo);

	// Delta Phi Variables
	BRANCH(deltaPhi_muon1muon2);  BRANCH(deltaPhi_caloJet1caloJet2);
	BRANCH(deltaPhi_muon1caloMET);  BRANCH(deltaPhi_muon2caloMET);
	BRANCH(deltaPhi_caloJet1caloMET); BRANCH(deltaPhi_caloJet2caloMET);
	BRANCH(deltaPhi_muon1caloJet1); BRANCH(deltaPhi_muon1caloJet2);
	BRANCH(deltaPhi_muon2caloJet1); BRANCH(deltaPhi_muon2caloJet2);

	// Delta R Variables
	BRANCH(deltaR_muon1muon2);  BRANCH(deltaR_caloJet1caloJet2);
	BRANCH(deltaR_muon1caloJet1); BRANCH(deltaR_muon1caloJet2);
	BRANCH(deltaR_muon2caloJet1); BRANCH(deltaR_muon2caloJet2);
	BRANCH(deltaR_muon1closestCaloJet);

	// Mass Combinations
	BRANCH(M_muon1muon2);  BRANCH(M_caloJet1caloJet2);
	BRANCH(M_muon1caloJet1); BRANCH(M_muon1caloJet2);
	BRANCH(M_muon2caloJet1); BRANCH(M_muon2caloJet2);
	BRANCH(M_muon1muon2caloJet1caloJet2);
	BRANCH(M_bestmucaloJet1_mumu); BRANCH(M_bestmucaloJet2_mumu);
	BRANCH(M_bestmucaloJet_munu);

	// Transverse Mass Combinations
	BRANCH(MT_muon1caloMET);
	BRANCH(MT_caloJet1caloMET); BRANCH(MT_caloJet2caloMET);
	BRANCH(MT_muon1caloJet1); BRANCH(MT_muon1caloJet2);
	BRANCH(MT_muon2caloJet1); BRANCH(MT_muon2caloJet2);

	// ST Variables
	BRANCH(ST_calo_mumu); BRANCH(ST_calo_munu);

	// Other Variables
	BRANCH(minval_muon1caloMET);
	BRANCH(Pt_Z);  BRANCH(Pt_W);
	BRANCH(Phi_Z); BRANCH(Phi_W);

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
	Events_AfterLJ = 1.0*(fChain->GetEntries());

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
	std::cout<<"            "<<std::endl;
	std::cout<<" Evaluating for: placeholder \n MC events: "<<Events_AfterLJ
		<< " \n Actual Events: "<<weight*Events_Orig<<" \n Integrated Luminosity: "
		<<lumi<<" pb^(-1) \n Cross Section: "<<xsection<<" pb "<<std::endl;
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

	for (Long64_t jentry=0; jentry<Events_AfterLJ;jentry++)
	{
		//-------------------------------------------------------
		// Show progress so you know the program hasn't failed...
		//-------------------------------------------------------
		for (xx=0; xx<100; xx=xx+1)
		{
			if ((100*jentry/(Events_AfterLJ)>xx)&&(100*(jentry-1)/(Events_AfterLJ)<xx))
			{
				std::cout<<xx<<" % complete"<<std::endl;
			}
		}
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

			bool separatedmuon = true;

			if (v_idx_muon_final.size() > 0)
			{
				for(unsigned int imu=0; imu<v_idx_muon_final.size(); imu++)
				{

					TLorentzVector oldmuon;
					int muindex = v_idx_muon_final[imu];
					oldmuon.SetPtEtaPhiM(MuonPt->at(muindex),MuonEta->at(muindex),MuonPhi->at(muindex),0);

					if (oldmuon.DeltaR(muon)<0.3) separatedmuon = false;

				}
			}
			else
			{
				separatedmuon = true;
			}

			if (!separatedmuon) continue;
			muons.push_back(muon);

			v_idx_muon_final.push_back(imuon);
		}						 // loop over muons

		MuonCount = 1.0*v_idx_muon_final.size();

		if ( MuonCount < 1 ) continue;

		TLorentzVector muon = muons[0];

		//========================     CaloJet Conditions   ================================//

		// Get Good Jets in general

		deltaR_muon1closestCaloJet = 999.9;
		float deltaR_thisjet = 9999.9;
		vector<TLorentzVector> jets;
		vector<int> v_idx_caloJet_prefinal;
		vector<int> v_idx_caloJet_final_unseparated;
		vector<int> v_idx_caloJet_final;
		BcaloJetCount = 0.0;

		// Initial Jet Quality Selection
		for(unsigned int ijet = 0; ijet < CaloJetPt->size(); ++ijet)
		{
			double jetPt = CaloJetPt -> at(ijet);
			double jetEta = CaloJetEta -> at(ijet);

			if ( jetPt < 30.0 ) continue;
			if ( fabs(jetEta) > 3.0 ) continue;

						if (CaloJetPassLooseID->at(ijet) != 1) continue;
//			if (CaloJetPassTightID->at(ijet) != 1) continue;

//			if ( CaloJetNeutralHadronEnergyFraction->at(ijet) >= 0.99) continue;
//			if ( CaloJetNeutralEmEnergyFraction    ->at(ijet) >= 0.99) continue;
//			if ( CaloJetChargedMultiplicity -> at(ijet) +
//				CaloJetNeutralMultiplicity -> at(ijet) <= 1 ) continue;
//			if ( TMath::Abs(jetEta) < 2.4 )
//			{
//				if ( CaloJetChargedHadronEnergyFraction->at(ijet) <= 0 ) continue;
//				if ( CaloJetChargedMultiplicity        ->at(ijet) <= 0 ) continue;
//				if ( CaloJetChargedEmEnergyFraction    ->at(ijet) >= 0.99) continue;
//			}

			v_idx_caloJet_prefinal.push_back(ijet);
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

		for(unsigned int imu=0; imu<MuonPt->size(); imu++)
		{
			mindeltar = 999999;
			//			muindex = v_idx_muon_final[imu];
			thismu.SetPtEtaPhiM(MuonPt->at(imu),MuonEta->at(imu),MuonPhi->at(imu),0);

			for(unsigned int ijet=0; ijet<v_idx_caloJet_prefinal.size(); ijet++)
			{
				jetindex = v_idx_caloJet_prefinal[ijet];
				thisjet.SetPtEtaPhiM((*CaloJetPt)[jetindex],(*CaloJetEta)[jetindex],(*CaloJetPhi)[jetindex],0);

				int ok = 1;

				if (thismu.Pt()==thisjet.Pt()) ok = 0;

				//				std::cout<<thisjet.Pt()<<"    "<<thismu.Pt()<<"   "<<ok<<std::endl;
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
		for(unsigned int ijet=0; ijet<v_idx_caloJet_prefinal.size(); ijet++)
		{
			int jetgood = 1;
			jetindex = v_idx_caloJet_prefinal[ijet];
			for(unsigned int kjet=0; kjet<jetstoremove.size(); kjet++)
			{
				remjetindex = jetstoremove[kjet];
				if (jetindex == remjetindex) jetgood=0;

			}

			if (jetgood ==1) v_idx_caloJet_final_unseparated.push_back(jetindex);
		}

		// Take filtered jets and eliminate those too close to the muon. save b variables

		jetindex = 99;

		for(unsigned int ijet=0; ijet<v_idx_caloJet_final_unseparated.size(); ijet++)
		{
			jetindex = v_idx_caloJet_final_unseparated[ijet];
			double jetPt = CaloJetPt -> at(jetindex);
			double jetEta = CaloJetEta -> at(jetindex);

			TLorentzVector newjet;
			newjet.SetPtEtaPhiM(jetPt,  jetEta, CaloJetPhi->at(jetindex),     0);
			// require a separation between a muon and a jet

			deltaR_thisjet =  newjet.DeltaR(muon);
			if ( deltaR_thisjet < deltaR_muon1closestCaloJet)  deltaR_muon1closestCaloJet = deltaR_thisjet ;

			if ( deltaR_thisjet < 0.5 ) continue;

			if ( CaloJetTrackCountingHighEffBTag->at(jetindex) > 1.7 )
			{
				BcaloJetCount = BcaloJetCount + 1.0;
			}

			// if we are here, the jet is good
			v_idx_caloJet_final.push_back(jetindex);
		}
		CaloJetCount = 1.0*v_idx_caloJet_final.size();

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

			TLorentzVector caloMETtest;
			caloMETtest.SetPtEtaPhiM(PFMET->at(0),0.0,PFMETPhi->at(0),0.0);
			muon1test.SetPtEtaPhiM(MuonPt->at(v_idx_muon_final[0]),MuonEta->at(v_idx_muon_final[0]),MuonPhi->at(v_idx_muon_final[0]),0.0);

			Pt_W_gen = (muon1test + v_GenNu).Pt();
			Phi_W_gen = (muon1test + v_GenNu).Phi();

			UW_gen = -(caloMETtest + muon1test );
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

		// CaloJet 1
		VRESET(Phi_caloJet1); VRESET(Eta_caloJet1); VRESET(Pt_caloJet1); VRESET(BDisc_caloJet1);
		VRESET(CaloJetNeutralMultiplicity_caloJet1);         VRESET(CaloJetNeutralHadronEnergyFraction_caloJet1);
		VRESET(CaloJetNeutralEmEnergyFraction_caloJet1);     VRESET(CaloJetChargedMultiplicity_caloJet1);
		VRESET(CaloJetChargedHadronEnergyFraction_caloJet1); VRESET(CaloJetChargedEmEnergyFraction_caloJet1);

		// CaloJet 2
		VRESET(Phi_caloJet2); VRESET(Eta_caloJet2); VRESET(Pt_caloJet2); VRESET(BDisc_caloJet2);
		VRESET(CaloJetNeutralMultiplicity_caloJet2);         VRESET(CaloJetNeutralHadronEnergyFraction_caloJet2);
		VRESET(CaloJetNeutralEmEnergyFraction_caloJet2);     VRESET(CaloJetChargedMultiplicity_caloJet2);
		VRESET(CaloJetChargedHadronEnergyFraction_caloJet2); VRESET(CaloJetChargedEmEnergyFraction_caloJet2);

		// Electron (If any)

		VRESET(Pt_ele1);
		// PFMET
		VRESET(MET_calo); VRESET(Phi_MET_calo);

		// Delta Phi Variables
		VRESET(deltaPhi_muon1muon2);  VRESET(deltaPhi_caloJet1caloJet2);
		VRESET(deltaPhi_muon1caloMET);  VRESET(deltaPhi_muon2caloMET);
		VRESET(deltaPhi_caloJet1caloMET); VRESET(deltaPhi_caloJet2caloMET);
		VRESET(deltaPhi_muon1caloJet1); VRESET(deltaPhi_muon1caloJet2);
		VRESET(deltaPhi_muon2caloJet1); VRESET(deltaPhi_muon2caloJet2);

		// Delta R Variables
		VRESET(deltaR_muon1muon2);  VRESET(deltaR_caloJet1caloJet2);
		VRESET(deltaR_muon1caloJet1); VRESET(deltaR_muon1caloJet2);
		VRESET(deltaR_muon2caloJet1); VRESET(deltaR_muon2caloJet2);
		VRESET(deltaR_muon1closestCaloJet);

		// Mass Combinations
		VRESET(M_muon1muon2);  VRESET(M_caloJet1caloJet2);
		VRESET(M_muon1caloJet1); VRESET(M_muon1caloJet2);
		VRESET(M_muon2caloJet1); VRESET(M_muon2caloJet2);
		VRESET(M_muon1muon2caloJet1caloJet2);
		VRESET(M_bestmucaloJet1_mumu); VRESET(M_bestmucaloJet2_mumu);
		VRESET(M_bestmucaloJet_munu);

		// Transverse Mass Combinations
		VRESET(MT_muon1caloMET);
		VRESET(MT_caloJet1caloMET); VRESET(MT_caloJet2caloMET);
		VRESET(MT_muon1caloJet1); VRESET(MT_muon1caloJet2);
		VRESET(MT_muon1caloJet2); VRESET(MT_muon2caloJet2);

		// ST Variables
		VRESET(ST_calo_mumu); VRESET(ST_calo_munu);

		// Other Variables
		VRESET(minval_muon1caloMET);
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
		TLorentzVector jet1, jet2, caloJet1, caloJet2, muon1,muon3,muon2,caloMET,tcMET;

		//========================     MET Basics  ================================//

		MET_calo = PFMET->at(0);
		caloMET.SetPtEtaPhiM(MET_calo,0.0,PFMETPhi->at(0),0.0);

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

			caloMET.SetPtEtaPhiM(V_MetPrime.Pt(),0,V_MetPrime.Phi(),0);
			MET_calo = caloMET.Pt();

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

			deltaPhi_muon1caloMET = (caloMET.DeltaPhi(muon1));
			MT_muon1caloMET = TMass(Pt_muon1,MET_calo,deltaPhi_muon1caloMET);

			minval_muon1caloMET = Pt_muon1;
			if (MET_calo < Pt_muon1) minval_muon1caloMET = MET_calo;

			// Recoil Stuff
			Pt_W = (muon1 + caloMET).Pt();
			Phi_W = (muon1 + caloMET).Phi();

			TLorentzVector UW = -(caloMET + muon1);
			TLorentzVector BW = (muon1+caloMET);

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

			deltaPhi_muon1caloMET = (caloMET.DeltaPhi(muon1));

			deltaPhi_muon1muon2 = (muon1.DeltaPhi(muon2));
			deltaR_muon1muon2 = muon1.DeltaR(muon2);
			M_muon1muon2 = (muon1+muon2).M();

			// Boson PT
			TLorentzVector UZ = -(caloMET + muon1 + muon2);
			TLorentzVector BZ = (muon1+muon2);

			U1_Z = (UZ.Pt()) * (cos(UZ.DeltaPhi(BZ))) ;
			U2_Z = (UZ.Pt()) * (sin(UZ.DeltaPhi(BZ))) ;

			Pt_Z = (muon1 + muon2).Pt();
			Phi_Z = (muon1 + muon2).Phi();

		}

		//========================   At least 1 PFJET  ================================//

		if (CaloJetCount>=1)
		{

			// Pt/Eta/Phi
			Pt_caloJet1 = CaloJetPt->at(v_idx_caloJet_final[0]);
			Phi_caloJet1 = CaloJetPhi->at(v_idx_caloJet_final[0]);
			Eta_caloJet1 = CaloJetEta->at(v_idx_caloJet_final[0]);

			// Other Variables
			caloJet1.SetPtEtaPhiM(Pt_caloJet1,Eta_caloJet1,Phi_caloJet1,0);

			deltaPhi_caloJet1caloMET = (caloMET.DeltaPhi(caloJet1));
			MT_caloJet1caloMET = TMass(Pt_caloJet1,MET_calo,deltaPhi_caloJet1caloMET);
			BDisc_caloJet1 = CaloJetTrackCountingHighEffBTag->at(v_idx_caloJet_final[0]);

		}

		//========================   At least 2 PFJET  ================================//

		if (CaloJetCount>=2)
		{
			// Pt/Eta/Phi
			Pt_caloJet2 = CaloJetPt->at(v_idx_caloJet_final[1]);
			Phi_caloJet2 = CaloJetPhi->at(v_idx_caloJet_final[1]);
			Eta_caloJet2 = CaloJetEta->at(v_idx_caloJet_final[1]);

			// Other Variables
			caloJet2.SetPtEtaPhiM(Pt_caloJet2,Eta_caloJet2,Phi_caloJet2,0);

			BDisc_caloJet2 = CaloJetTrackCountingHighEffBTag->at(v_idx_caloJet_final[1]);

			deltaPhi_caloJet2caloMET = (caloMET.DeltaPhi(caloJet2));
			MT_caloJet2caloMET = TMass(Pt_caloJet2,MET_calo,deltaPhi_caloJet2caloMET);

			deltaR_caloJet1caloJet2 = caloJet1.DeltaR(caloJet2);
			deltaPhi_caloJet1caloJet2 = (caloJet1.DeltaPhi(caloJet2));
			M_caloJet1caloJet2 = (caloJet1 + caloJet2).M();
		}

		//========================   1 Muon 1 Jet ================================//

		if ((MuonCount>0) && (CaloJetCount> 0))
		{
			deltaPhi_muon1caloJet1 = (muon1.DeltaPhi(caloJet1));
			deltaR_muon1caloJet1 = (muon1.DeltaR(caloJet1));
			M_muon1caloJet1 = (caloJet1 + muon1).M();
			MT_muon1caloJet1 = TMass(Pt_caloJet1,Pt_muon1,deltaPhi_muon1caloJet1);
		}

		//========================   1 Muon 2 Jet ================================//

		if ((MuonCount>0) && (CaloJetCount> 1))
		{
			deltaPhi_muon1caloJet2 = (muon1.DeltaPhi(caloJet2));
			deltaR_muon1caloJet2 = (muon1.DeltaR(caloJet2));
			M_muon1caloJet2 = (caloJet2 + muon1).M();
			MT_muon1caloJet2 = TMass(Pt_caloJet2,Pt_muon1,deltaPhi_muon1caloJet2);
			ST_calo_munu= Pt_muon1 + MET_calo + Pt_caloJet1 + Pt_caloJet2;

		}

		//========================   2 Muon 1 Jet ================================//

		if ((MuonCount>1) && (CaloJetCount> 0))
		{
			deltaPhi_muon2caloJet1 = (muon2.DeltaPhi(caloJet1));
			deltaR_muon2caloJet1 = (muon2.DeltaR(caloJet1));
			M_muon2caloJet1 = (caloJet1+muon2).M();
			MT_muon2caloJet1 = TMass(Pt_caloJet1,Pt_muon2,deltaPhi_muon2caloJet1);
		}

		//========================   2 Muon 2 Jet ================================//

		if ((MuonCount>1) && (CaloJetCount> 1))
		{
			deltaPhi_muon2caloJet2 = (muon2.DeltaPhi(caloJet2));
			ST_calo_mumu= Pt_muon1 + Pt_muon2 + Pt_caloJet1 + Pt_caloJet2;
			M_muon2caloJet2 = (caloJet2 + muon2).M();
			MT_muon2caloJet2 = TMass(Pt_caloJet2,Pt_muon2,deltaPhi_muon2caloJet2);
			deltaR_muon2caloJet2 = (muon2.DeltaR(caloJet2));
			M_muon1muon2caloJet1caloJet2 = (muon1+muon2+caloJet1+caloJet2).M();
		}

		//========================   LQ Mass Concepts ================================//

		// DiMuon, minimizing differene between mu-jet masses
		if ((MuonCount>1) && (CaloJetCount> 1))
		{
			if (abs(M_muon1caloJet1 - M_muon2caloJet2) < abs(M_muon1caloJet2 - M_muon2caloJet1) )
			{
				M_bestmucaloJet1_mumu = M_muon1caloJet1;
				M_bestmucaloJet2_mumu = M_muon2caloJet2;
			}

			if (abs(M_muon1caloJet1 - M_muon2caloJet2) > abs(M_muon1caloJet2 - M_muon2caloJet1) )
			{
				M_bestmucaloJet1_mumu = M_muon2caloJet1;
				M_bestmucaloJet2_mumu = M_muon1caloJet2;
			}
		}

		// Beta - Half production - minimize difference of transverse masses
		if ((MuonCount>0) && (CaloJetCount> 1))
		{
			if (abs(MT_muon1caloJet1 - MT_caloJet2caloMET) < abs(MT_muon1caloJet2 - MT_caloJet1caloMET) )
			{
				M_bestmucaloJet_munu= M_muon1caloJet1;
			}

			if (abs(MT_muon1caloJet1 - MT_caloJet2caloMET) > abs(MT_muon1caloJet2 - MT_caloJet1caloMET) )
			{
				M_bestmucaloJet_munu= M_muon1caloJet2;
			}
		}

		tree->Fill();			 // FILL FINAL TREE

	}

	tree->Write();
	file1->Close();
}
