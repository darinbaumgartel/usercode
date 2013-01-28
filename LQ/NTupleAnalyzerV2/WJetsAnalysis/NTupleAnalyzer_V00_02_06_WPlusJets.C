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

Double_t ScaleJet(Double_t PT, Double_t fraction)
{
	int sign = 1.0;
	if (fraction<1.0) sign =-1.0;
	if (PT >  10.045837015009878  ) fraction =  1.0816  ;
	if (PT >  10.914793145910853  ) fraction =  1.07331  ;
	if (PT >  11.189851524004983  ) fraction =  1.07075  ;
	if (PT >  11.809823908691957  ) fraction =  1.06727  ;
	if (PT >  12.259045129630636  ) fraction =  1.0642  ;
	if (PT >  12.831363365781058  ) fraction =  1.0613  ;
	if (PT >  13.655098586775988  ) fraction =  1.05633  ;
	if (PT >  14.352001430814637  ) fraction =  1.05359  ;
	if (PT >  15.21013385976414  ) fraction =  1.05044  ;
	if (PT >  15.723339390468372  ) fraction =  1.04895  ;
	if (PT >  16.73273083846727  ) fraction =  1.04522  ;
	if (PT >  19.347205427601036  ) fraction =  1.03909  ;
	if (PT >  22.838995888501916  ) fraction =  1.03412  ;
	if (PT >  26.51733610692726  ) fraction =  1.03006  ;
	if (PT >  30.916067683613512  ) fraction =  1.02649  ;
	if (PT >  37.26064411541987  ) fraction =  1.02293  ;
	if (PT >  44.721359549995796  ) fraction =  1.02003  ;
	if (PT >  54.57396572955423  ) fraction =  1.01746  ;
	if (PT >  68.84426735408334  ) fraction =  1.01547  ;
	if (PT >  85.41697259944324  ) fraction =  1.01431  ;
	if (PT >  108.20016239260036  ) fraction =  1.01373  ;
	if (PT >  134.246912074893  ) fraction =  1.01331  ;
	if (PT >  172.18386410651112  ) fraction =  1.01323  ;
	if (PT >  221.75941333248414  ) fraction =  1.01315  ;
	if (PT >  285.6088615315718  ) fraction =  1.01331  ;
	if (PT >  377.1117867826719  ) fraction =  1.01348  ;
	if (PT >  491.77237401567504  ) fraction =  1.01373  ;
	if (PT >  643.9610775470397  ) fraction =  1.01423  ;
	if (PT >  779.3404110640498  ) fraction =  1.01456  ;
	if (PT >  1127.3478597509404  ) fraction =  1.0153  ;
	if (PT >  1513.4296900580316  ) fraction =  1.01605  ;
	if (PT >  1846.8548557201623  ) fraction =  1.01646  ;

	if (sign < 0.0 ) fraction = 2.0 - fraction;
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
	if (!e_ecaldriven) isgood = 0; //OK
	if (fabs(e_dphi_sc) > 0.09) isgood = 0; //OK
	if (e_hoe > 0.05) isgood = 0; //OK
	if (e_losthits != 0) isgood = 0;
	bool barrel = (fabs(e_eta) < 1.442); //OK
	bool endcap = (fabs(e_eta) > 1.560 && fabs(e_eta) < 2.5); //OK
	
	if ((!barrel)&&(!endcap)) isgood = 0;
	
	if (barrel)
	{
		if (e_pt<35.0) isgood = 0; // OK
		if (fabs(e_deta_sc) > 0.005) isgood = 0; // OK
		if (( e_e1x5_over_5x5 < 0.83)&&( e_e2x5_over_5x5 < 0.94 )) isgood = 0; // OK
		if ( e_em_had1iso > ( 2.0 + 0.03*e_pt )) isgood = 0; //OK
		if (e_trkiso > 7.5) isgood = 0; //OK
	}
	
	if (endcap)
	{
		if (e_pt<40.0) isgood = 0; // OK	
		if (fabs(e_deta_sc)> 0.007) isgood = 0; //OK
		if (fabs(e_sigmann) > 0.03) isgood = 0; //OK
		if ((e_pt < 50.0) && ( e_em_had1iso >  2.5 )) isgood = 0; //OK
		if ((e_pt >= 50.0) && ( e_em_had1iso > ( 2.5 + 0.03*(e_pt-50.0) ))) isgood = 0; // OK
		if ( e_had2iso > 0.5 ) isgood = 0;
		if (e_trkiso > 15.0) 	isgood = 0; // OK
	}
	
	return isgood;
}

vector<bool> BTagTCHPT(float pt, bool isdata,float discrim, float eta, int evt)
{

	double dseedmod = fabs(eta*eta*1000000+42);
	int dseed = int(floor(abs(dseedmod)));
	int evtseed = abs( int(floor((1.0*evt)+10000)) -42 );
	
	rr->SetSeed(evtseed + dseed );

	vector<bool> tags;
	float discrim_cut = 3.41;

	float eff_central  = 0.895596*((1.+(9.43219e-05*pt))/(1.+(-4.63927e-05*pt)));

	float mistag_central = (1.20711+(0.000681067*pt)) + (-1.57062e-06*(pt*pt)) + (2.83138e-10*(pt*(pt*pt)));
	float mistag_down    = (1.03418+(0.000428273*pt)) + (-5.43024e-07*(pt*pt)) + (-6.18061e-10*(pt*(pt*pt)));
	float mistag_up      = (1.38002+(0.000933875*pt)) + (-2.59821e-06*(pt*pt)) + (1.18434e-09*(pt*(pt*pt)));
	float mistag_nominal = 0.00284;

	float efferr = 0.0;

	if (pt >=  30. && pt <  40.) efferr =  0.0543376;
	if (pt >=  40. && pt <  50.) efferr =  0.0534339;
	if (pt >=  50. && pt <  60.) efferr =   0.0266156;
	if (pt >=  60. && pt <  70.) efferr =  0.0271337;
	if (pt >=  70. && pt <  80.) efferr =  0.0276364;
	if (pt >=  80. && pt < 100.) efferr =  0.0308838;
	if (pt >= 100. && pt < 120.) efferr =  0.0381656;
	if (pt >= 120. && pt < 160.) efferr =  0.0336979;
	if (pt >= 160. && pt < 210.) efferr =  0.0336773;
	if (pt >= 210. && pt < 260.) efferr =  0.0347688;
	if (pt >= 260. && pt < 320.) efferr =  0.0376865;
	if (pt >= 320. && pt < 400.) efferr =  0.0556052;
	if (pt >= 400. && pt < 500.) efferr =  0.0598105;
	if (pt >= 500. && pt < 670.) efferr =  0.0861122 ;

	float eff_up = eff_central + efferr;
	float eff_down = eff_central - efferr;

	float rand_efftag = rr->Rndm();
	float rand_mistag = rr->Rndm();

	bool untag_central  = rand_efftag > eff_central;
	bool untag_up       = rand_efftag > eff_up;
	bool untag_down     = rand_efftag > eff_down;

	bool forcemistag_central = (rand_mistag > mistag_nominal) && (rand_mistag < mistag_nominal*mistag_central); 
	bool forcemistag_up      = (rand_mistag > mistag_nominal) && (rand_mistag < mistag_nominal*mistag_up); 
	bool forcemistag_down    = (rand_mistag > mistag_nominal) && (rand_mistag < mistag_nominal*mistag_down); 

	bool basic_tag = discrim > discrim_cut;

	bool tag_central  = basic_tag;
	bool tag_eff_up   = basic_tag;
	bool tag_eff_down = basic_tag;
	bool tag_mis_up   = basic_tag;
	bool tag_mis_down = basic_tag;
	
	if (isdata)
	{
		tags.push_back(tag_central);
		tags.push_back(tag_central);
		tags.push_back(tag_central);
		tags.push_back(tag_central);
		tags.push_back(tag_central);
		return tags;
	}

	if ( (tag_central == true ) && (untag_central == true) )         tag_central = false;
	if ( (tag_central == false) && (forcemistag_central == true) )   tag_central = true;

	if ( (tag_eff_up == true ) && (untag_up == true) )               tag_eff_up = false;
	if ( (tag_eff_up == false) && (forcemistag_central == true) )    tag_eff_up = true;

	if ( (tag_eff_down == true ) && (untag_down == true) )           tag_eff_down = false;
	if ( (tag_eff_down == false) && (forcemistag_central == true) )  tag_eff_down = true;

	if ( (tag_mis_up == true ) && (untag_central == true) )          tag_mis_up = false;
	if ( (tag_mis_up == false) && (forcemistag_up == true) )     tag_mis_up = true;

	if ( (tag_mis_down == true ) && (untag_central == true) )        tag_mis_down = false;
	if ( (tag_mis_down == false) && (forcemistag_down == true) ) tag_mis_down = true;

	tags.push_back(tag_central);
	tags.push_back(tag_eff_up);
	tags.push_back(tag_eff_down);
	tags.push_back(tag_mis_up);
	tags.push_back(tag_mis_down);
	return tags;
}

vector<bool> BTags(float pt, bool isdata,float tchpt, float ssvhpt,float jpt,float jpbt)
{

	float sf_tchpt  = 0.895596*((1.+(9.43219e-05*pt))/(1.+(-4.63927e-05*pt)));
	float sf_ssvhpt = 0.422556*((1.+(0.437396*pt))/(1.+(0.193806*pt)));
	float sf_jpt    = 0.835882*((1.+(0.00167826*pt))/(1.+(0.00120221*pt)));
	float sf_jpbt   = 0.827249*((1.+(0.00261855*pt))/(1.+(0.00194604*pt)));

	bool toss_tchpt  = rr->Rndm() > sf_tchpt;
	bool toss_ssvhpt = rr->Rndm() > sf_ssvhpt;
	bool toss_jpt    = rr->Rndm() > sf_jpt;
	bool toss_jpbt   = rr->Rndm() > sf_jpbt;

	if (isdata)
	{
		toss_tchpt = false;
		toss_ssvhpt = false;
		toss_jpt = false;
		toss_jpbt = false;
	}

	bool tag_tchpt   = (tchpt > 3.41)*(!toss_tchpt);
	bool tag_ssvhpt  = (ssvhpt > 2.00)*(!toss_ssvhpt);
	bool tag_jpt     = (jpt > 0.79)*(!toss_jpt);
	bool tag_jpbt    = (jpbt > 3.74)*(!toss_jpbt);

	vector<bool> tags;

	tags.push_back(tag_tchpt);
	tags.push_back(tag_ssvhpt);
	tags.push_back(tag_jpt);
	tags.push_back(tag_jpbt);

	return tags;
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
	BRANCH(MuonCount); BRANCH(EleCount); BRANCH(HEEPEle25Count);BRANCH(Muon25Count); BRANCH(PFJetCount); BRANCH(BpfJetCount);
	BRANCH(GlobalMuonCount); BRANCH(TrackerMuonCount);
	BRANCH(GlobalMuonCount10GeV);
	BRANCH(GenJetCount); BRANCH(GenJet30Count); 
	BRANCH(PFJet30Count); 
	BRANCH(PFJet30SSVHEMCount); BRANCH(PFJet30TCHPTCount);

	BRANCH(PFJet30TCHPTCountMod);
	BRANCH(PFJet30SSVHPTCountMod);
	BRANCH(PFJet30JPTCountMod);
	BRANCH(PFJet30JPBTCountMod);

	BRANCH(PFJet30TCHPTCountCentral);
	BRANCH(PFJet30TCHPTCountEffUp);
	BRANCH(PFJet30TCHPTCountEffDown);
	BRANCH(PFJet30TCHPTCountMisUp);
	BRANCH(PFJet30TCHPTCountMisDown);

	// Event Information
	UInt_t run_number,event_number,ls_number;
	tree->Branch("event_number",&event_number,"event_number/i");
	tree->Branch("run_number",&run_number,"run_number/i");
	tree->Branch("ls_number",&ls_number,"ls_number/i");
	BRANCH(bx);	
	BRANCH(N_Vertices);
	BRANCH(N_GoodVertices);
	// BRANCH(weight);
	BRANCH(weight_pu_central); BRANCH(weight_pu_sysplus8); BRANCH(weight_pu_sysminus8); BRANCH(weight_gen);
	BRANCH(pass_HBHENoiseFilter); BRANCH(pass_isBPTX0); BRANCH(pass_passBeamHaloFilterLoose); 
	BRANCH(pass_passBeamHaloFilterTight);
	BRANCH(pass_isTrackingFailure);

	// ID Efficiency Informations
	
	// vector<int> RecoJetsWithMatchesIDPass;
	// tree->Branch("RecoJetsWithMatchesIDPass",&RecoJetsWithMatchesIDPass);

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
	BRANCH(Pt_genjet6);  BRANCH(Phi_genjet6);  BRANCH(Eta_genjet6);  

	BRANCH(Pt_genjet1_bare);  BRANCH(Phi_genjet1_bare);  BRANCH(Eta_genjet1_bare);  
	BRANCH(Pt_genjet2_bare);  BRANCH(Phi_genjet2_bare);  BRANCH(Eta_genjet2_bare);  
	BRANCH(Pt_genjet3_bare);  BRANCH(Phi_genjet3_bare);  BRANCH(Eta_genjet3_bare);  
	BRANCH(Pt_genjet4_bare);  BRANCH(Phi_genjet4_bare);  BRANCH(Eta_genjet4_bare);  
	BRANCH(Pt_genjet5_bare);  BRANCH(Phi_genjet5_bare);  BRANCH(Eta_genjet5_bare);  
	BRANCH(Pt_genjet6_bare);  BRANCH(Phi_genjet6_bare);  BRANCH(Eta_genjet6_bare);  
	

	BRANCH(DeltaPhi_genjet1genmuon1);
	BRANCH(DeltaPhi_genjet2genmuon1);
	BRANCH(DeltaPhi_genjet3genmuon1);
	BRANCH(DeltaPhi_genjet4genmuon1);
	BRANCH(DeltaPhi_genjet5genmuon1);
	BRANCH(DeltaPhi_genjet6genmuon1);

	BRANCH(DeltaPhi_genjet1genmuon1_bare);
	BRANCH(DeltaPhi_genjet2genmuon1_bare);
	BRANCH(DeltaPhi_genjet3genmuon1_bare);
	BRANCH(DeltaPhi_genjet4genmuon1_bare);
	BRANCH(DeltaPhi_genjet5genmuon1_bare);
	BRANCH(DeltaPhi_genjet6genmuon1_bare);

	BRANCH(ST_genmuongenMET);
	BRANCH(ST_genmuongenMETgenjet1);
	BRANCH(ST_genmuongenMETgenjet12);
	BRANCH(ST_genmuongenMETgenjet123);
	BRANCH(ST_genmuongenMETgenjet1234);
	BRANCH(ST_genmuongenMETgenjet12345);
	BRANCH(ST_genmuongenMETgenjet123456);
	
	BRANCH(ST_genmuongenMET_bare);
	BRANCH(ST_genmuongenMETgenjet1_bare);
	BRANCH(ST_genmuongenMETgenjet12_bare);
	BRANCH(ST_genmuongenMETgenjet123_bare);
	BRANCH(ST_genmuongenMETgenjet1234_bare);
	BRANCH(ST_genmuongenMETgenjet12345_bare);
	BRANCH(ST_genmuongenMETgenjet123456_bare);
	

	BRANCH(Pt_genmuon1);  BRANCH(Phi_genmuon1);  BRANCH(Eta_genmuon1);  
	BRANCH(Pt_genmuon2);  BRANCH(Phi_genmuon2);  BRANCH(Eta_genmuon2);  

	BRANCH(Pt_genmuonneutrino1);  BRANCH(Phi_genmuonneutrino1);  BRANCH(Eta_genmuonneutrino1);  	
	BRANCH(Pt_genMET);  BRANCH(Phi_genMET);  

	BRANCH(MT_genmuon1genMET);
	BRANCH(MT_genmuon1genneutrino);
	BRANCH(Pt_W_gen);  BRANCH(Phi_W_gen);



	// Reco Level Variables	
	BRANCH(Pt_pfjet1);  BRANCH(Phi_pfjet1);  BRANCH(Eta_pfjet1);  BRANCH(SSVHEM_pfjet1);  BRANCH(TCHPT_pfjet1);
	BRANCH(Pt_pfjet2);  BRANCH(Phi_pfjet2);  BRANCH(Eta_pfjet2);  BRANCH(SSVHEM_pfjet2);  BRANCH(TCHPT_pfjet2);  
	BRANCH(Pt_pfjet3);  BRANCH(Phi_pfjet3);  BRANCH(Eta_pfjet3);  BRANCH(SSVHEM_pfjet3);  BRANCH(TCHPT_pfjet3);  
	BRANCH(Pt_pfjet4);  BRANCH(Phi_pfjet4);  BRANCH(Eta_pfjet4);  BRANCH(SSVHEM_pfjet4);  BRANCH(TCHPT_pfjet4);  
	BRANCH(Pt_pfjet5);  BRANCH(Phi_pfjet5);  BRANCH(Eta_pfjet5);  BRANCH(SSVHEM_pfjet5);  BRANCH(TCHPT_pfjet5);  
	BRANCH(Pt_pfjet6);  BRANCH(Phi_pfjet6);  BRANCH(Eta_pfjet6);  BRANCH(SSVHEM_pfjet6);  BRANCH(TCHPT_pfjet6);  

	BRANCH(DeltaPhi_pfjet1muon1);
	BRANCH(DeltaPhi_pfjet2muon1);
	BRANCH(DeltaPhi_pfjet3muon1);
	BRANCH(DeltaPhi_pfjet4muon1);
	BRANCH(DeltaPhi_pfjet5muon1);
	BRANCH(DeltaPhi_pfjet6muon1);


	BRANCH(ST_muonMET);
	BRANCH(ST_muonMETpfjet1);
	BRANCH(ST_muonMETpfjet12);
	BRANCH(ST_muonMETpfjet123);
	BRANCH(ST_muonMETpfjet1234);
	BRANCH(ST_muonMETpfjet12345);
	BRANCH(ST_muonMETpfjet123456);



	BRANCH(Pt_muon1);  BRANCH(Phi_muon1);  BRANCH(Eta_muon1);  
	BRANCH(Pt_muon2);  BRANCH(Phi_muon2);  BRANCH(Eta_muon2);  
	BRANCH(TrkRelIso_muon1);
	
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
		
		weight_gen =weight;
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
		

		// std::cout<<extraweight<<"  "<<lumi<<"  "<<xsection<<"  "<<Events_Orig<<"  "<<weight<<"  "<<weight_pu_central<<std::endl;

		
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
				// double NewJetPT2 = (*PFJetPt)[ijet];

				//double NewJetETA = (*PFJetEta)[ijet];


				// if (JetRescaleFactor != 1.00) NewJetPT = NewJetPT + ((ScaleObject((*PFJetPtRaw)[ijet],NewJetRescalingFactor)) - ((*PFJetPtRaw)[ijet])) ; 
				// if (JetRescaleFactor != 1.00) NewJetPT = NewJetPT + ((ScaleJet((*PFJetPtRaw)[ijet],NewJetRescalingFactor)) - ((*PFJetPtRaw)[ijet])) ; 

				if (JetRescaleFactor > 1.00) NewJetPT *= (1+PFJetJECUnc->at(ijet))  ; 
				if (JetRescaleFactor < 1.00) NewJetPT *= (1-PFJetJECUnc->at(ijet))  ; 


				// std::cout<<(NewJetPT - PFJetPt->at(ijet))/(PFJetPt->at(ijet))<<std::endl;


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
					(((MuonTrackerIsoSumPT->at(imuon))/muonPt) < 0.1) &&                             // Disable for EWK
					//((MuonHcalIso->at(imuon) + MuonTrkIso->at(imuon))/muonPt) < 0.15;  // Enable for EWK
					MuonTrkHitsTrackerOnly ->at(imuon) >= 11   ;                         
	
				bool PassPOGTight =
					MuonStationMatches->at(imuon) > 1 && 
					fabs(MuonPrimaryVertexDXY ->at(imuon)) < 0.2  &&
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
		HEEPEle25Count = 1.0*v_idx_ele_good_final.size();

		//========================      Muon Conditions   ================================//

		vector<TLorentzVector> RecoMuons, RecoJets; 
		vector<int> RecoJetSSVHEMtags, RecoJetTCHPTtags;
		vector<int> v_idx_muon_final;
		bool checkPT = true;	 // Pt requirement only on first muon at this stage
		
		// SubRoutine for Muon Counts
		GlobalMuonCount = 0.0;
		GlobalMuonCount10GeV = 0.0;
		Muon25Count = 0.0;
		TrackerMuonCount=0.0;
		
		Double_t muoniso = 1.0;
		for(unsigned int imuon = 0; imuon < MuonPt->size(); ++imuon)
		{
			if (MuonIsGlobal  ->at(imuon) == 1) GlobalMuonCount += 1.0;
			if (MuonIsTracker ->at(imuon) == 1) TrackerMuonCount += 1.0;
			if ((MuonIsGlobal->at(imuon) == 1) && (MuonPt->at(imuon) > 10.0)) GlobalMuonCount10GeV += 1.0;
			
			Double_t muonPt = MuonPt->at(imuon);
			Double_t muonEta = MuonEta->at(imuon);

			if (checkPT && (muonPt < 20.0) ) continue;
			if  ( fabs(muonEta) > 2.1 )      continue;

			bool PassGlobalTightPrompt =
				MuonIsGlobal ->at(imuon) == 1 &&
				MuonIsTracker ->at(imuon) == 1 &&
				//fabs(MuonRelIso->at(imuon)) < 0.1 &&
				(((MuonTrackerIsoSumPT->at(imuon))/muonPt) < 0.1) &&                             // Disable for EWK
				//((MuonHcalIso->at(imuon) + MuonTrkIso->at(imuon))/muonPt) < 0.15;  // Enable for EWK
				MuonTrkHitsTrackerOnly ->at(imuon) >= 11   ;                         

			bool PassPOGTight =
				MuonStationMatches->at(imuon) > 1 && 
				fabs(MuonPrimaryVertexDXY ->at(imuon)) < 0.2  &&
				MuonGlobalChi2 ->at(imuon) < 10.0 &&                         // Disable for EWK
				MuonPixelHitCount ->at(imuon) >=1 &&
				MuonGlobalTrkValidHits->at(imuon)>=1 ;

			if ( ! (PassGlobalTightPrompt && PassPOGTight) ) continue;
			TLorentzVector muon;
			muon.SetPtEtaPhiM( MuonPt -> at(imuon), MuonEta-> at(imuon),    MuonPhi-> at(imuon),    0);
			RecoMuons.push_back(muon);
			if (muoniso > 0.999) muoniso = ((MuonTrackerIsoSumPT->at(imuon))/muonPt);
			v_idx_muon_final.push_back(imuon);
			Muon25Count += 1.0;
			if (v_idx_muon_final.size()>=1) checkPT=false;
		}						 // loop over muons

		MuonCount = 1.0*v_idx_muon_final.size();

		if ( Muon25Count < 1 ) continue;

		int LeadMuonVertex=MuonVtxIndex->at(v_idx_muon_final[0]);
		

		//========================     PFJet Conditions   ================================//
		// Get Good Jets in general

		vector<TLorentzVector> jets;
		vector<int> v_idx_pfjet_prefinal;
		vector<int> v_idx_pfjet_final;
		BpfJetCount = 0.0;
		FailIDPFThreshold = -1.0;
		TLorentzVector CurrentLepton,CurrentPFJet;

		TLorentzVector thisjet, thismu, thise;

		int muindex = 99;
		int eindex = 99;
		int jetindex = 99;
		
		// Initial Jet Quality Selection
		for(unsigned int ijet = 0; ijet < PFJetPt->size(); ++ijet)
		{
			double jetPt = PFJetPt -> at(ijet);
			double jetEta = PFJetEta -> at(ijet);
			CurrentPFJet.SetPtEtaPhiM((*PFJetPt)[ijet],(*PFJetEta)[ijet],(*PFJetPhi)[ijet],0);

			if (PFJetBestVertexTrackAssociationIndex->at(ijet) != LeadMuonVertex) continue;

			bool IsLepton = false;

			if ((PFJetPassLooseID->at(ijet) != 1)&&(PFJetPt->at(ijet) > FailIDPFThreshold)&&(!IsLepton)) FailIDPFThreshold = PFJetPt->at(ijet);
			if ( jetPt < 30.0 ) continue;			
			if ( fabs(jetEta) > 2.4 ) continue;
			if (PFJetPassLooseID->at(ijet) != 1) continue;   
			v_idx_pfjet_prefinal.push_back(ijet);
		}
		// Filter out jets that are actually muons or electrons


		PFJet30Count = 0.0;
		PFJet30TCHPTCount = 0.0;
		PFJet30SSVHEMCount = 0.0;

		PFJet30JPTCountMod = 0.0;
		PFJet30JPBTCountMod = 0.0;
		PFJet30TCHPTCountMod = 0.0;
		PFJet30SSVHPTCountMod = 0.0;

		PFJet30TCHPTCountCentral = 0.0;
		PFJet30TCHPTCountEffUp = 0.0;
		PFJet30TCHPTCountEffDown = 0.0;
		PFJet30TCHPTCountMisUp = 0.0;
		PFJet30TCHPTCountMisDown = 0.0;

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

			// for(unsigned int imu=0; imu<v_idx_muon_final.size(); imu++)
			// {
			// 	muindex = v_idx_muon_final[imu];
			// 	thismu.SetPtEtaPhiM(MuonPt->at(muindex),MuonEta->at(muindex),MuonPhi->at(muindex),0);
			// 	if (thismu.Pt()<20.0) continue;
			// 	if (thismu.DeltaR(thisjet) < 0.3)		KeepJet=false;
			// }

			for(unsigned int ie=0; ie<v_idx_ele_good_final.size(); ie++)
			{
				eindex = v_idx_ele_good_final[ie];
				thise.SetPtEtaPhiM(ElectronPt->at(eindex),ElectronEta->at(eindex),ElectronPhi->at(eindex),0);
				if (thise.DeltaR(thisjet) < 0.3)		KeepJet=false;
			}
			
			if (!KeepJet) continue;
			if ( PFJetTrackCountingHighEffBTag->at(jetindex) > 2.0 ) BpfJetCount = BpfJetCount + 1.0;
			RecoJets.push_back(thisjet);
			RecoJetTCHPTtags.push_back( PFJetTrackCountingHighPurBTag->at(jetindex) );
			RecoJetSSVHEMtags.push_back( PFJetSimpleSecondaryVertexHighEffBTag->at(jetindex) );

			v_idx_pfjet_final.push_back(jetindex);
			if (thisjet.Pt() > 30.0) 
			{

				float tchpt   = PFJetTrackCountingHighPurBTag->at(jetindex);
				float ssvhpt  = PFJetSimpleSecondaryVertexHighPurBTag->at(jetindex);
				float jpt     = PFJetJetProbabilityBTag->at(jetindex);
				float jpbt    = PFJetJetBProbabilityBTag->at(jetindex);

				vector<bool> btags = BTags(thisjet.Pt(),isData,tchpt,ssvhpt,jpt,jpbt);
				vector<bool> btags_tchpt = BTagTCHPT(thisjet.Pt(),isData,tchpt,thisjet.Eta(), event);


				PFJet30TCHPTCountMod  += 1.0*btags[0];
				PFJet30SSVHPTCountMod += 1.0*btags[1];
				PFJet30JPTCountMod    += 1.0*btags[2];
				PFJet30JPBTCountMod   += 1.0*btags[3];

				PFJet30TCHPTCountCentral += 1.0*(btags_tchpt[0]);
				PFJet30TCHPTCountEffUp   += 1.0*(btags_tchpt[1]);
				PFJet30TCHPTCountEffDown += 1.0*(btags_tchpt[2]);
				PFJet30TCHPTCountMisUp   += 1.0*(btags_tchpt[3]);
				PFJet30TCHPTCountMisDown += 1.0*(btags_tchpt[4]);


				PFJet30Count += 1.0;
				PFJet30TCHPTCount += 1.0*(PFJetTrackCountingHighPurBTag->at(jetindex) > 3.41);
				PFJet30SSVHEMCount += 1.0*(PFJetSimpleSecondaryVertexHighEffBTag->at(jetindex) > 1.74);

			}
			// std::cout<<PFJet30TCHPTCountMod<<" "<<PFJet30SSVHPTCountMod<<std::endl;
			// std::cout<<"  "<<PFJet30TCHPTCountCentral<<"  "<<PFJet30TCHPTCountEffUp<<"  "<<PFJet30TCHPTCountEffDown<<"  "<<PFJet30TCHPTCountMisUp<<"  "<<PFJet30TCHPTCountMisDown<<std::endl;
		}

		PFJetCount = 1.0*v_idx_pfjet_final.size();
		//std::cout<<PFJet40Count<<"  "<<PFJet40SSVHEMCount<<"  "<<PFJet40TCHPTCount<<std::endl;

		// std::cout<<" --------------- "<<std::endl;

		//========================     Generator Level Module  ================================//

		if (!isData)
		{

			vector<TLorentzVector> GenMuons, GenJets, GenJetsBare, SortedGenMuons, SortedGenJets, GenMuNeutrinos;

			Pt_genjet1 = 0;       Phi_genjet1 = 0;       Eta_genjet1 = 0; DeltaPhi_genjet1genmuon1 = -1.0;
			Pt_genjet2 = 0;       Phi_genjet2 = 0;       Eta_genjet2 = 0; DeltaPhi_genjet2genmuon1 = -1.0; 
			Pt_genjet3 = 0;       Phi_genjet3 = 0;       Eta_genjet3 = 0; DeltaPhi_genjet3genmuon1 = -1.0;
			Pt_genjet4 = 0;       Phi_genjet4 = 0;       Eta_genjet4 = 0; DeltaPhi_genjet4genmuon1 = -1.0;
			Pt_genjet5 = 0;       Phi_genjet5 = 0;       Eta_genjet5 = 0; DeltaPhi_genjet5genmuon1 = -1.0;
			Pt_genjet6 = 0;       Phi_genjet6 = 0;       Eta_genjet6 = 0; DeltaPhi_genjet6genmuon1 = -1.0;
			
			Pt_genjet1_bare = 0;       Phi_genjet1_bare = 0;       Eta_genjet1_bare = 0; DeltaPhi_genjet1genmuon1_bare = -1.0;
			Pt_genjet2_bare = 0;       Phi_genjet2_bare = 0;       Eta_genjet2_bare = 0; DeltaPhi_genjet2genmuon1_bare = -1.0; 
			Pt_genjet3_bare = 0;       Phi_genjet3_bare = 0;       Eta_genjet3_bare = 0; DeltaPhi_genjet3genmuon1_bare = -1.0;
			Pt_genjet4_bare = 0;       Phi_genjet4_bare = 0;       Eta_genjet4_bare = 0; DeltaPhi_genjet4genmuon1_bare = -1.0;
			Pt_genjet5_bare = 0;       Phi_genjet5_bare = 0;       Eta_genjet5_bare = 0; DeltaPhi_genjet5genmuon1_bare = -1.0;
			Pt_genjet6_bare = 0;       Phi_genjet6_bare = 0;       Eta_genjet6_bare = 0; DeltaPhi_genjet6genmuon1_bare = -1.0;

			Pt_genmuon1 = 0;      Phi_genmuon1 = 0;      Eta_genmuon1 = 0;
			Pt_genmuon2 = 0;      Phi_genmuon2 = 0;      Eta_genmuon2 = 0;
			GenJetCount=0;        GenJet30Count = 0.0;  
			Pt_genmuonneutrino1 = 0;      Phi_genmuonneutrino1 = 0;      Eta_genmuonneutrino1 = 0;


			HT_genMG = 0.0;

			ST_genmuongenMET = 0 ;
			ST_genmuongenMETgenjet1 = 0 ;
			ST_genmuongenMETgenjet12 = 0 ;
			ST_genmuongenMETgenjet123 = 0 ;
			ST_genmuongenMETgenjet1234 = 0 ;
			ST_genmuongenMETgenjet12345 = 0 ;
			ST_genmuongenMETgenjet123456 = 0 ;

			ST_genmuongenMET_bare = 0 ;
			ST_genmuongenMETgenjet1_bare = 0 ;
			ST_genmuongenMETgenjet12_bare = 0 ;
			ST_genmuongenMETgenjet123_bare = 0 ;
			ST_genmuongenMETgenjet1234_bare = 0 ;
			ST_genmuongenMETgenjet12345_bare = 0 ;
			ST_genmuongenMETgenjet123456_bare = 0 ;

			MT_genmuon1genMET = 0 ;  MT_genmuon1genneutrino = 0;
			
			// std::cout<<" ---------------------------------------------- "<<std::endl;

			for(unsigned int ip = 0; ip != GenParticlePdgId->size(); ++ip)
			{
				int pdgId = GenParticlePdgId->at(ip);
				int motherIndex = GenParticleMotherIndex->at(ip);

				if ( TMath::Abs(pdgId) == 13 )
				{
					TLorentzVector thisgenmuon;
					thisgenmuon.SetPtEtaPhiM(GenParticlePt->at(ip),GenParticleEta->at(ip),GenParticlePhi->at(ip),0.0);

					bool KeepMuon=true;
					for(unsigned int igenmuon = 0; igenmuon != GenMuons.size(); ++igenmuon)
					{
						if ( (GenMuons[igenmuon].Pt() == thisgenmuon.Pt())&&(GenMuons[igenmuon].Eta() == thisgenmuon.Eta())&&(GenMuons[igenmuon].Phi() == thisgenmuon.Phi()) ) 
						{	
							KeepMuon=false;
						}
					}

					if (KeepMuon==true) GenMuons.push_back(thisgenmuon);
				}
				if ( TMath::Abs(pdgId) == 14 )
				{
					TLorentzVector thisgenneutrino;
					thisgenneutrino.SetPtEtaPhiM(GenParticlePt->at(ip),GenParticleEta->at(ip),GenParticlePhi->at(ip),0.0);
					
					bool KeepNeutrino=true;
					for(unsigned int igenneutrino = 0; igenneutrino != GenMuNeutrinos.size(); ++igenneutrino)
					{
						if ( (GenMuNeutrinos[igenneutrino].Pt() == thisgenneutrino.Pt())&&(GenMuNeutrinos[igenneutrino].Eta() == thisgenneutrino.Eta())&&(GenMuNeutrinos[igenneutrino].Phi() == thisgenneutrino.Phi()) ) 
						{	
							KeepNeutrino=false;
						}
					}

					if (KeepNeutrino==true) GenMuNeutrinos.push_back(thisgenneutrino);
				}
			}


			for(unsigned int ijet = 0; ijet != GenJetPt->size(); ++ijet)
			{

				if (fabs(GenJetEta->at(ijet))>3.0) continue;
				TLorentzVector(thisgenjet);
				thisgenjet.SetPtEtaPhiM(GenJetPt->at(ijet),GenJetEta->at(ijet),GenJetPhi->at(ijet),0.0);

				bool KeepGenJet=true;
				for(unsigned int igmu = 0; igmu != GenMuons.size(); ++igmu)
				{
					if ((GenMuons[igmu]).DeltaR(thisgenjet) < 0.3)		KeepGenJet=false;
				}
			
				if (!KeepGenJet) continue;

				GenJets.push_back(thisgenjet);
				if (fabs(GenJetEta->at(ijet))>2.4) continue;
				if (thisgenjet.Pt()>30.0) continue;
					GenJet30Count+= 1.0;				
					GenJetsBare.push_back(thisgenjet);
			}
			
			GenJetCount = 1.0*(GenJets.size());


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
				//std::cout<<matchedgenmuon.DeltaR(RecoMuons[0])<<std::endl;
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
			if (PFJetCount>=1)	DeltaPhi_genjet1genmuon1 =	fabs(SortedGenJets[0].DeltaPhi(SortedGenMuons[0]));

			if (PFJetCount>=2)	Pt_genjet2  =	SortedGenJets[1].Pt();
			if (PFJetCount>=2)	Eta_genjet2 =	SortedGenJets[1].Eta();
			if (PFJetCount>=2)	Phi_genjet2 =	SortedGenJets[1].Phi();
			if (PFJetCount>=2)	DeltaPhi_genjet2genmuon1 =	fabs(SortedGenJets[1].DeltaPhi(SortedGenMuons[0]));

			if (PFJetCount>=3)	Pt_genjet3  =	SortedGenJets[2].Pt();
			if (PFJetCount>=3)	Eta_genjet3 =	SortedGenJets[2].Eta();
			if (PFJetCount>=3)	Phi_genjet3 =	SortedGenJets[2].Phi();
			if (PFJetCount>=3)	DeltaPhi_genjet3genmuon1 =	fabs(SortedGenJets[2].DeltaPhi(SortedGenMuons[0]));

			if (PFJetCount>=4)	Pt_genjet4  =	SortedGenJets[3].Pt();
			if (PFJetCount>=4)	Eta_genjet4 =	SortedGenJets[3].Eta();
			if (PFJetCount>=4)	Phi_genjet4 =	SortedGenJets[3].Phi();
			if (PFJetCount>=4)	DeltaPhi_genjet4genmuon1 =	fabs(SortedGenJets[3].DeltaPhi(SortedGenMuons[0]));

			if (PFJetCount>=5)	Pt_genjet5  =	SortedGenJets[4].Pt();
			if (PFJetCount>=5)	Eta_genjet5 =	SortedGenJets[4].Eta();
			if (PFJetCount>=5)	Phi_genjet5 =	SortedGenJets[4].Phi();
			if (PFJetCount>=5)	DeltaPhi_genjet5genmuon1 =	fabs(SortedGenJets[4].DeltaPhi(SortedGenMuons[0]));

			if (PFJetCount>=6)	Pt_genjet6  =	SortedGenJets[5].Pt();
			if (PFJetCount>=6)	Eta_genjet6 =	SortedGenJets[5].Eta();
			if (PFJetCount>=6)	Phi_genjet6 =	SortedGenJets[5].Phi();
			if (PFJetCount>=6)	DeltaPhi_genjet6genmuon1 =	fabs(SortedGenJets[5].DeltaPhi(SortedGenMuons[0]));



			// Assign Bare Jet Variables		
			if (GenJet30Count>=1)	Pt_genjet1_bare  =	GenJetsBare[0].Pt();
			if (GenJet30Count>=1)	Eta_genjet1_bare =	GenJetsBare[0].Eta();
			if (GenJet30Count>=1)	Phi_genjet1_bare =	GenJetsBare[0].Phi();
			if (GenJet30Count>=1)	DeltaPhi_genjet1genmuon1_bare =	fabs(GenJetsBare[0].DeltaPhi(SortedGenMuons[0]));

			if (GenJet30Count>=2)	Pt_genjet2_bare  =	GenJetsBare[1].Pt();
			if (GenJet30Count>=2)	Eta_genjet2_bare =	GenJetsBare[1].Eta();
			if (GenJet30Count>=2)	Phi_genjet2_bare =	GenJetsBare[1].Phi();
			if (GenJet30Count>=2)	DeltaPhi_genjet2genmuon1_bare =	fabs(GenJetsBare[1].DeltaPhi(SortedGenMuons[0]));

			if (GenJet30Count>=3)	Pt_genjet3_bare  =	GenJetsBare[2].Pt();
			if (GenJet30Count>=3)	Eta_genjet3_bare =	GenJetsBare[2].Eta();
			if (GenJet30Count>=3)	Phi_genjet3_bare =	GenJetsBare[2].Phi();
			if (GenJet30Count>=3)	DeltaPhi_genjet3genmuon1_bare =	fabs(GenJetsBare[2].DeltaPhi(SortedGenMuons[0]));

			if (GenJet30Count>=4)	Pt_genjet4_bare  =	GenJetsBare[3].Pt();
			if (GenJet30Count>=4)	Eta_genjet4_bare =	GenJetsBare[3].Eta();
			if (GenJet30Count>=4)	Phi_genjet4_bare =	GenJetsBare[3].Phi();
			if (GenJet30Count>=4)	DeltaPhi_genjet4genmuon1_bare =	fabs(GenJetsBare[3].DeltaPhi(SortedGenMuons[0]));

			if (GenJet30Count>=5)	Pt_genjet5_bare  =	GenJetsBare[4].Pt();
			if (GenJet30Count>=5)	Eta_genjet5_bare =	GenJetsBare[4].Eta();
			if (GenJet30Count>=5)	Phi_genjet5_bare =	GenJetsBare[4].Phi();
			if (GenJet30Count>=5)	DeltaPhi_genjet5genmuon1_bare =	fabs(GenJetsBare[4].DeltaPhi(SortedGenMuons[0]));

			if (GenJet30Count>=6)	Pt_genjet6_bare  =	GenJetsBare[5].Pt();
			if (GenJet30Count>=6)	Eta_genjet6_bare =	GenJetsBare[5].Eta();
			if (GenJet30Count>=6)	Phi_genjet6_bare =	GenJetsBare[5].Phi();
			if (GenJet30Count>=6)	DeltaPhi_genjet6genmuon1_bare =	fabs(GenJetsBare[5].DeltaPhi(SortedGenMuons[0]));



			Pt_genMET = GenMETTrue->at(0);
			Phi_genMET = GenMETPhiTrue->at(0);
			
			MT_genmuon1genMET =  TMass(Pt_genmuon1,Pt_genMET, fabs(Phi_genmuon1 - Phi_genMET) );
			
			if (GenMuNeutrinos.size()>0)	
			{	
				MT_genmuon1genneutrino = TMass(Pt_genmuon1, GenMuNeutrinos[0].Pt() , fabs(Phi_genmuon1 - GenMuNeutrinos[0].Phi()) );
				Pt_genmuonneutrino1 = GenMuNeutrinos[0].Pt();     
				Phi_genmuonneutrino1 = GenMuNeutrinos[0].Phi();      
				Eta_genmuonneutrino1 = GenMuNeutrinos[0].Eta();
			}
			
			TLorentzVector  v_GenMet;
			v_GenMet.SetPtEtaPhiM ( Pt_genMET, 0, Phi_genMET,0 );
			Pt_W_gen = (SortedGenMuons[0]+v_GenMet).Pt();
			Phi_W_gen = (SortedGenMuons[0]+v_GenMet).Phi();

			ST_genmuongenMET = Pt_genMET+Pt_genmuon1 ;
			ST_genmuongenMETgenjet1 = ST_genmuongenMET + Pt_genjet1 ;
			ST_genmuongenMETgenjet12 = ST_genmuongenMETgenjet1 + Pt_genjet2 ;
			ST_genmuongenMETgenjet123 = ST_genmuongenMETgenjet12 + Pt_genjet3 ;
			ST_genmuongenMETgenjet1234 = ST_genmuongenMETgenjet123 + Pt_genjet4 ;
			ST_genmuongenMETgenjet12345 = ST_genmuongenMETgenjet1234 + Pt_genjet5 ;
			ST_genmuongenMETgenjet123456 = ST_genmuongenMETgenjet12345 + Pt_genjet6 ;
		
			ST_genmuongenMET_bare = Pt_genMET+Pt_genmuon1 ;
			ST_genmuongenMETgenjet1_bare = ST_genmuongenMET + Pt_genjet1_bare ;
			ST_genmuongenMETgenjet12_bare = ST_genmuongenMETgenjet1 + Pt_genjet2_bare ;
			ST_genmuongenMETgenjet123_bare = ST_genmuongenMETgenjet12 + Pt_genjet3_bare ;
			ST_genmuongenMETgenjet1234_bare = ST_genmuongenMETgenjet123 + Pt_genjet4_bare ;
			ST_genmuongenMETgenjet12345_bare = ST_genmuongenMETgenjet1234 + Pt_genjet5_bare ;
			ST_genmuongenMETgenjet123456_bare = ST_genmuongenMETgenjet12345 + Pt_genjet6_bare ;
		}


		//========================     Calculate Reco Variables  ================================//

	
			Pt_pfjet1 = 0;       Phi_pfjet1 = 0;       Eta_pfjet1 = 0;    DeltaPhi_pfjet1muon1 = -1.0;     SSVHEM_pfjet1 = -100.0;    TCHPT_pfjet1 = -100.0;
			Pt_pfjet2 = 0;       Phi_pfjet2 = 0;       Eta_pfjet2 = 0;    DeltaPhi_pfjet2muon1 = -1.0;     SSVHEM_pfjet2 = -100.0;    TCHPT_pfjet2 = -100.0;
			Pt_pfjet3 = 0;       Phi_pfjet3 = 0;       Eta_pfjet3 = 0;    DeltaPhi_pfjet3muon1 = -1.0;     SSVHEM_pfjet3 = -100.0;    TCHPT_pfjet3 = -100.0;
			Pt_pfjet4 = 0;       Phi_pfjet4 = 0;       Eta_pfjet4 = 0;    DeltaPhi_pfjet4muon1 = -1.0;     SSVHEM_pfjet4 = -100.0;    TCHPT_pfjet4 = -100.0;
			Pt_pfjet5 = 0;       Phi_pfjet5 = 0;       Eta_pfjet5 = 0;    DeltaPhi_pfjet5muon1 = -1.0;     SSVHEM_pfjet5 = -100.0;    TCHPT_pfjet5 = -100.0;
			Pt_pfjet6 = 0;       Phi_pfjet6 = 0;       Eta_pfjet6 = 0;    DeltaPhi_pfjet6muon1 = -1.0;     SSVHEM_pfjet6 = -100.0;    TCHPT_pfjet6 = -100.0;
			
			Pt_muon1 = 0;      Phi_muon1 = 0;      Eta_muon1 = 0;
			Pt_muon2 = 0;      Phi_muon2 = 0;      Eta_muon2 = 0;
	
			Pt_MET = 0;        Phi_MET = 0;        
			MT_muon1MET = 0;

	
			ST_muonMET = 0 ;
			ST_muonMETpfjet1 = 0 ;
			ST_muonMETpfjet12 = 0 ;
			ST_muonMETpfjet123 = 0 ;
			ST_muonMETpfjet1234 = 0 ;
			ST_muonMETpfjet12345 = 0 ;
			ST_muonMETpfjet123456 = 0 ;
	
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
			if (PFJetCount>=1)	SSVHEM_pfjet1 =	RecoJetSSVHEMtags[0];
			if (PFJetCount>=1)	TCHPT_pfjet1  =	RecoJetTCHPTtags[0];
			if (PFJetCount>=1)	DeltaPhi_pfjet1muon1 =	fabs(RecoJets[0].DeltaPhi(RecoMuons[0]));
			//std::cout<<DeltaPhi_pfjet1muon1<<std::endl;

			if (PFJetCount>=2)	Pt_pfjet2  =	RecoJets[1].Pt();
			if (PFJetCount>=2)	Eta_pfjet2 =	RecoJets[1].Eta();
			if (PFJetCount>=2)	Phi_pfjet2 =	RecoJets[1].Phi();
			if (PFJetCount>=2)	SSVHEM_pfjet2 =	RecoJetSSVHEMtags[1];
			if (PFJetCount>=2)	TCHPT_pfjet2  =	RecoJetTCHPTtags[1];
			if (PFJetCount>=2)	DeltaPhi_pfjet2muon1 =	fabs(RecoJets[1].DeltaPhi(RecoMuons[0]));			

			if (PFJetCount>=3)	Pt_pfjet3  =	RecoJets[2].Pt();
			if (PFJetCount>=3)	Eta_pfjet3 =	RecoJets[2].Eta();
			if (PFJetCount>=3)	Phi_pfjet3 =	RecoJets[2].Phi();
			if (PFJetCount>=3)	SSVHEM_pfjet3 =	RecoJetSSVHEMtags[2];
			if (PFJetCount>=3)	TCHPT_pfjet3  =	RecoJetTCHPTtags[2];
			if (PFJetCount>=3)	DeltaPhi_pfjet3muon1 =	fabs(RecoJets[2].DeltaPhi(RecoMuons[0]));			

			if (PFJetCount>=4)	Pt_pfjet4  =	RecoJets[3].Pt();
			if (PFJetCount>=4)	Eta_pfjet4 =	RecoJets[3].Eta();
			if (PFJetCount>=4)	Phi_pfjet4 =	RecoJets[3].Phi();
			if (PFJetCount>=4)	SSVHEM_pfjet4 =	RecoJetSSVHEMtags[3];
			if (PFJetCount>=4)	TCHPT_pfjet4  =	RecoJetTCHPTtags[3];
			if (PFJetCount>=4)	DeltaPhi_pfjet4muon1 =	fabs(RecoJets[3].DeltaPhi(RecoMuons[0]));			

			if (PFJetCount>=5)	Pt_pfjet5  =	RecoJets[4].Pt();
			if (PFJetCount>=5)	Eta_pfjet5 =	RecoJets[4].Eta();
			if (PFJetCount>=5)	Phi_pfjet5 =	RecoJets[4].Phi();
			if (PFJetCount>=5)	SSVHEM_pfjet5 =	RecoJetSSVHEMtags[4];
			if (PFJetCount>=5)	TCHPT_pfjet5  =	RecoJetTCHPTtags[4];
			if (PFJetCount>=5)	DeltaPhi_pfjet5muon1 =	fabs(RecoJets[4].DeltaPhi(RecoMuons[0]));			

			if (PFJetCount>=6)	Pt_pfjet6  =	RecoJets[5].Pt();
			if (PFJetCount>=6)	Eta_pfjet6 =	RecoJets[5].Eta();
			if (PFJetCount>=6)	Phi_pfjet6 =	RecoJets[5].Phi();
			if (PFJetCount>=6)	SSVHEM_pfjet6 =	RecoJetSSVHEMtags[5];
			if (PFJetCount>=6)	TCHPT_pfjet6  =	RecoJetTCHPTtags[5];
			if (PFJetCount>=6)	DeltaPhi_pfjet6muon1 =	fabs(RecoJets[5].DeltaPhi(RecoMuons[0]));	

			Pt_MET = PFMET->at(0);
			Phi_MET = PFMETPhi->at(0);
			
			MT_muon1MET =  TMass(Pt_muon1,Pt_MET, fabs(Phi_muon1 - Phi_MET) );
			TrkRelIso_muon1 =muoniso;
			
			TLorentzVector  v_Met;
			v_Met.SetPtEtaPhiM ( Pt_MET, 0, Phi_MET,0 );
			Pt_W = (RecoMuons[0]+v_Met).Pt();
			Phi_W = (RecoMuons[0]+v_Met).Phi();
	
			MET_pfsig = PFMETSig->at(0);
			MET_pf_charged = PFMETCharged->at(0);

			ST_muonMET = Pt_MET+Pt_muon1 ;
			ST_muonMETpfjet1 = ST_muonMET + Pt_pfjet1 ;
			ST_muonMETpfjet12 = ST_muonMETpfjet1 + Pt_pfjet2 ;
			ST_muonMETpfjet123 = ST_muonMETpfjet12 + Pt_pfjet3 ;
			ST_muonMETpfjet1234 = ST_muonMETpfjet123 + Pt_pfjet4 ;
			ST_muonMETpfjet12345 = ST_muonMETpfjet1234 + Pt_pfjet5 ;
			ST_muonMETpfjet123456 = ST_muonMETpfjet12345 + Pt_pfjet6 ;
	
			
			Pt_HEEPele1=0.0;
			if (HEEPEle25Count>=1) Pt_HEEPele1 = ElectronPt->at(v_idx_ele_good_final[0]);
	
		bool skipevent = true;

		if ((Pt_muon1>45)||(Pt_genmuon1>45)) skipevent = false;
		// if ((Muon25Count>0)&&(HEEPEle25Count>0)) skipevent = false;
		// if (Pt_muon2>25) skipevent = true;				

		//std::cout<<skipevent<<std::endl;
		if (skipevent) continue;

		tree->Fill();
	}

	tree->Write();
	file1->Close();
}
