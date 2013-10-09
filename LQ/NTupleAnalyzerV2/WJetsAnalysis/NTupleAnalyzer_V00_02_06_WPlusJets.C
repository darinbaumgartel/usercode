#define placeholder_cxx
#include "placeholder.h"
#include <TH2.h>
#include <TChain.h>
#include <TFile.h>
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

#define BRANCH(bname) Float_t bname = -99999.12345; tree->Branch(#bname,& bname," bname /F ");
#define VRESET(vname) vname = -99999.12345;

//===================================================================================================
//        Initial Setup and Special Functions
//===================================================================================================

TRandom3* rr = new TRandom3();

// Systematic factors, interchanged via python script. Do not modify here.
Double_t JetRescaleFactor = 1.00;
Double_t MuonRescaleFactor = 1.00;
Double_t JetSmearFactor = 0.0;
Double_t MuonSmearFactor = 0.0;



float HasMatchInCollection(TLorentzVector inputvector, std::vector<TLorentzVector>& coll)
{
	float ismatched = 0.0;
	for(unsigned int ic = 0; ic != coll.size(); ++ic)
	{
		if (inputvector.DeltaR(coll[ic]) < 0.5) ismatched = 1.0;
	}
	return ismatched;
}

// Recoil Correction Function. 
TLorentzVector Recoil_Corr(TLorentzVector L, TLorentzVector U, TLorentzVector P)
{

	Double_t piover2 = 0.5*3.1415926;
	Double_t x = 1.0*P.Pt();

	Double_t responseU1 = 1.33223-0.917782*x;
	Double_t responseU2 = -0.013;

	Double_t responseMCU1 = 1.26247-0.950094*x;
	Double_t responseMCU2 = -0.00544907;

	Double_t resolutionU1 = 11.1566+0.0654529*x+0.000124436*x*x;
	Double_t resolutionU2 = 11.1235+0.0449872*x-6.39822e-5*x*x;

	Double_t resolutionMCU1 = 10.6449+0.0436475*x+3.07554e-5*x*x;
	Double_t resolutionMCU2 = 10.5649+0.0225853*x-5.81371e-5*x*x;

	float PPhiOrig = 1.0*P.Phi();

	U.RotateZ(-1.0*PPhiOrig);
	P.RotateZ(-1.0*PPhiOrig);

	float UPSeparation = U.Phi();

	float U1 = fabs(U.Pt()*cos(UPSeparation));
	float U1Phi = 0.0;
	if (fabs(UPSeparation) > piover2)   U1Phi = 2*piover2;

	float U2 = fabs(U.Pt()*sin(UPSeparation));

	float U2Phi = piover2;

	if (UPSeparation < 0.0) U2Phi = -1.0*piover2;

	Double_t U1prime = U1*(responseU1/responseMCU1);
	Double_t U2prime = U2;

	Double_t S1 = sqrt(resolutionU1*resolutionU1 - resolutionMCU1*resolutionMCU1);
	Double_t S2 = sqrt(resolutionU2*resolutionU2 - resolutionMCU2*resolutionMCU2);
	Double_t C2 = responseU2-responseMCU2;

	U1prime += rr->Gaus(0.0,S1);
	U2prime += rr->Gaus(C2,S2);

	// U1prime = U1;
	// U2prime = U2;

	TLorentzVector V_U1prime;
	V_U1prime.SetPtEtaPhiM(U1prime,0.,U1Phi,0.);

	TLorentzVector V_U2prime;
	V_U2prime.SetPtEtaPhiM(U2prime,0.,U2Phi,0.);

	TLorentzVector UPrime;
	UPrime = V_U1prime +V_U2prime;

	UPrime.RotateZ(PPhiOrig);

	TLorentzVector METprime;
	METprime = (-L - UPrime);

	return METprime;

}



// Phi Modulation Correction
TLorentzVector PhiMod_Corr(TLorentzVector MET, float Nvtx, bool _isdata)
{
	float _met = MET.Pt();
	float _phi = MET.Phi();
	float _ex = _met*cos(_phi);
	float _ey = _met*sin(_phi);

	float px = 0.0;
	float py = 0.0;

	if (_isdata)
	{
		px = (3.64118e-01) + (2.93853e-01)*Nvtx;
		py = (-7.17757e-01) - (3.57309e-01)*Nvtx;
	}

	else
	{
		px = (-4.79178e-02) + (8.62653e-04)*Nvtx;
		py = (-4.54408e-01) - (1.89684e-01)*Nvtx;
	}
	float _exp = _ex - px;
	float _eyp = _ey - py;
	float _metprime = sqrt(_exp*_exp + _eyp*_eyp);

	TLorentzVector METprime;
	TLorentzVector METAngle;
	METAngle.SetPx(_exp);
	METAngle.SetPy(_eyp);
	float _metphiprime = 1.0*METAngle.Phi();
	METprime.SetPtEtaPhiM(_metprime,0.0,_metphiprime,0.0);
	return METprime;
}

// Transverse Mass
Double_t TMass(Double_t Pt1, Double_t Pt2, Double_t DPhi12)
{
	return sqrt( 2*Pt2*Pt1*(1-cos(DPhi12)) );
}

// PT Rescaling
Double_t ScaleObject(Double_t PT, Double_t fraction)
{
	return (PT*(fraction));
}

// PT Smearing
Double_t SmearObject(Double_t PT, Double_t fraction)
{
	return (rr->Gaus(PT,fraction*PT));
}

// Jet energy resolution smearing
Double_t JERFactor(Double_t J_ETA)
{
	// if ((abs(J_ETA)<0.5))                     return rr->Gaus(1.052,0.063);
	// if ((abs(J_ETA)>0.5)&&(abs(J_ETA)<1.1))   return rr->Gaus(1.057,0.057);
	// if ((abs(J_ETA)>1.1)&&(abs(J_ETA)<1.7))   return rr->Gaus(1.096,0.065);
	// if ((abs(J_ETA)>1.7)&&(abs(J_ETA)<2.3))   return rr->Gaus(1.134,0.094);
	// if ((abs(J_ETA)>2.3)&&(abs(J_ETA)<5.0))   return rr->Gaus(1.288,0.200);
	if ((abs(J_ETA)<0.5))                     return 1.052+0.063;
	if ((abs(J_ETA)>=0.5)&&(abs(J_ETA)<1.1))   return 1.057+0.057;
	if ((abs(J_ETA)>=1.1)&&(abs(J_ETA)<1.7))   return 1.096+0.065;
	if ((abs(J_ETA)>=1.7)&&(abs(J_ETA)<2.3))   return 1.134+0.094;
	if ((abs(J_ETA)>=2.3)&&(abs(J_ETA)<5.0))   return 1.288+0.200;
	return 1.0;
}

//Smearing function for jet resolution - increasing gen/reco pT difference
Double_t GetRecoGenJetScaleFactor(Double_t RecoPT,Double_t GenPT, Double_t SmearFactor)
{
	Double_t deltaPT = ((RecoPT-GenPT)*SmearFactor);
	return (GenPT+deltaPT)/RecoPT;
}

// Function to modify MET when another object pT is changed
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

// HEEP electron ID, not used in practice .
int CustomHeepID(double e_pt, double e_pt_real, double e_eta, bool e_ecaldriven , double e_dphi_sc, double e_deta_sc, double e_hoe, double e_sigmann, double e_e1x5_over_5x5, double e_e2x5_over_5x5, double e_em_had1iso , double e_had2iso, double e_trkiso, double e_losthits )
{
	int isgood = 1;

	if (e_pt_real<20.0) isgood = 0;
	if (!e_ecaldriven) isgood = 0;
	if (fabs(e_dphi_sc) > 0.09) isgood = 0;
	if (e_hoe > 0.05) isgood = 0;//OK
	if (e_losthits != 0) isgood = 0;
	bool barrel = (fabs(e_eta) < 1.442);
	bool endcap = (fabs(e_eta) > 1.560 && fabs(e_eta) < 2.5);

	if ((!barrel)&&(!endcap)) isgood = 0;

	if (barrel)
	{
		if (e_pt<35.0) isgood = 0;
		if (fabs(e_deta_sc) > 0.005) isgood = 0;
		if (( e_e1x5_over_5x5 < 0.83)&&( e_e2x5_over_5x5 < 0.94 )) isgood = 0;
		if ( e_em_had1iso > ( 2.0 + 0.03*e_pt )) isgood = 0;
		if (e_trkiso > 7.5) isgood = 0;
	}

	if (endcap)
	{
		if (e_pt<40.0) isgood = 0;
		if (fabs(e_deta_sc)> 0.007) isgood = 0;
		if (fabs(e_sigmann) > 0.03) isgood = 0;
		if ((e_pt < 50.0) && ( e_em_had1iso >  2.5 )) isgood = 0;
		if ((e_pt >= 50.0) && ( e_em_had1iso > ( 2.5 + 0.03*(e_pt-50.0) ))) isgood = 0;
		if ( e_had2iso > 0.5 ) isgood = 0;
		if (e_trkiso > 15.0)    isgood = 0;
	}

	return isgood;
}


// BTagging with data/MC rescaling for TCHPT
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
	// float mistag_nominal = 0.00284;
	float mistag_nominal = (-0.00101+(4.70405e-05*pt))+(8.3338e-09*(pt*pt));

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
	if (pt >= 670.) efferr =  0.0861122*2.0 ;

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

// BTagging with data/MC rescaling for SSVHPT
vector<bool> BTagSSVHPT(float pt, bool isdata,float discrim, float eta, int evt)
{

	double dseedmod = fabs(eta*eta*1000000+42);
	int dseed = int(floor(abs(dseedmod)));
	int evtseed = abs( int(floor((1.0*evt)+10000)) -42 );

	rr->SetSeed(evtseed + dseed );

	vector<bool> tags;
	float discrim_cut = 2.00;

	float eff_central  = 0.422556*((1.+(0.437396*pt))/(1.+(0.193806*pt)));
	float mistag_central = ((0.97409+(0.000646241*pt))+(-2.86294e-06*(pt*pt)))+(2.79484e-09*(pt*(pt*pt)));
	float mistag_down    = ((0.807222+(0.00103676*pt))+(-3.6243e-06*(pt*pt)))+(3.17368e-09*(pt*(pt*pt)));
	float mistag_up      = ((1.14091+(0.00025586*pt))+(-2.10157e-06*(pt*pt)))+(2.41599e-09*(pt*(pt*pt)));
	float mistag_nominal = (-2.9605e-05+(2.35624e-05*pt))+(-1.77552e-08*(pt*pt));

	float efferr = 0.0;

	if (pt >=  30. && pt <  40.) efferr =   0.0403485;
	if (pt >=  40. && pt <  50.) efferr =   0.0396907;
	if (pt >=  50. && pt <  60.) efferr =   0.0291837;
	if (pt >=  60. && pt <  70.) efferr =   0.0325778;
	if (pt >=  70. && pt <  80.) efferr =   0.0335716;
	if (pt >=  80. && pt < 100.) efferr =   0.0255023;
	if (pt >= 100. && pt < 120.) efferr =   0.0300639;
	if (pt >= 120. && pt < 160.) efferr =   0.0253228;
	if (pt >= 160. && pt < 210.) efferr =   0.0409739;
	if (pt >= 210. && pt < 260.) efferr =   0.043561;
	if (pt >= 260. && pt < 320.) efferr =   0.0458427;
	if (pt >= 320. && pt < 400.) efferr =   0.0763302;
	if (pt >= 400. && pt < 500.) efferr =   0.0781752;
	if (pt >= 500. && pt < 670.) efferr =   0.108927 ;
	if (pt >= 670.) efferr =  0.108927*2.0 ;

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

// BTagging with data/MC rescaling for JPT
vector<bool> BTagJPT(float pt, bool isdata,float discrim, float eta, int evt)
{

	double dseedmod = fabs(eta*eta*1000000+42);
	int dseed = int(floor(abs(dseedmod)));
	int evtseed = abs( int(floor((1.0*evt)+10000)) -42 );

	rr->SetSeed(evtseed + dseed );

	vector<bool> tags;
	float discrim_cut = 0.79;

	float eff_central  = 0.835882*((1.+(0.00167826*pt))/(1.+(0.00120221*pt)));

	float mistag_central = ((0.831392+(0.00269525*pt))+(-7.33391e-06*(pt*pt)))+(5.73942e-09*(pt*(pt*pt)));
	float mistag_down    = ((0.671888+(0.0020106*pt))+(-5.03177e-06*(pt*pt)))+(3.74225e-09*(pt*(pt*pt)));
	float mistag_up      = ((0.990774+(0.00338018*pt))+(-9.63606e-06*(pt*pt)))+(7.73659e-09*(pt*(pt*pt)));

	float mistag_nominal =  (0.000379966+(8.30969e-06*pt))+(1.10364e-08*(pt*pt));

	float efferr = 0.0;

	if (pt >=  30. && pt <  40.) efferr =   0.0475813;
	if (pt >=  40. && pt <  50.) efferr =   0.0472359;
	if (pt >=  50. && pt <  60.) efferr =   0.0378328;
	if (pt >=  60. && pt <  70.) efferr =   0.0334787;
	if (pt >=  70. && pt <  80.) efferr =   0.034681;
	if (pt >=  80. && pt < 100.) efferr =   0.0398312;
	if (pt >= 100. && pt < 120.) efferr =   0.0481646;
	if (pt >= 120. && pt < 160.) efferr =   0.0392262;
	if (pt >= 160. && pt < 210.) efferr =   0.0463086;
	if (pt >= 210. && pt < 260.) efferr =   0.0534565;
	if (pt >= 260. && pt < 320.) efferr =   0.0545823;
	if (pt >= 320. && pt < 400.) efferr =   0.102505;
	if (pt >= 400. && pt < 500.) efferr =   0.113198;
	if (pt >= 500. && pt < 670.) efferr =   0.138116;
	if (pt >= 670.) efferr =  0.138116*2.0 ;

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

// BTagging without data/MC rescaling for TCHPT. 
vector<bool> BTagTCHPTUnCorr(float pt, bool isdata,float discrim, float eta, int evt)
{
	double dseedmod = fabs(eta*eta*1000000+42);
	int dseed = int(floor(abs(dseedmod)));
	int evtseed = abs( int(floor((1.0*evt)+10000)) -42 );

	rr->SetSeed(evtseed + dseed );

	vector<bool> tags;
	float discrim_cut = 3.41;
	bool basic_tag = discrim > discrim_cut;

	bool tag_central  = basic_tag;

	tags.push_back(tag_central);
	tags.push_back(tag_central);
	tags.push_back(tag_central);
	tags.push_back(tag_central);
	tags.push_back(tag_central);
	return tags;

}


// BTagging with data/MC rescaling for TCHEM
vector<bool> BTagTCHEM(float pt, bool isdata,float discrim, float eta, int evt)
{

	double dseedmod = fabs(eta*eta*1000000+42);
	int dseed = int(floor(abs(dseedmod)));
	int evtseed = abs( int(floor((1.0*evt)+10000)) -42 );

	rr->SetSeed(evtseed + dseed );

	vector<bool> tags;
	float discrim_cut = 3.3;

	float eff_central  = 0.932251*((1.+(0.00335634*pt))/(1.+(0.00305994*pt)));

	float mistag_central = 0.0;
	float mistag_down    = 0.0;
	float mistag_up      = 0.0;
	float mistag_nominal = 0.0;

	if ((fabs(eta)>=0.0) &&  (fabs(eta)<=0.8))
	{
		mistag_central = (1.2875*((1+(-0.000356371*pt))+(1.08081e-07*(pt*pt))))+(-6.89998e-11*(pt*(pt*(pt/(1+(-0.0012139*pt))))));
		mistag_down = (1.11418*((1+(-0.000442274*pt))+(1.53463e-06*(pt*pt))))+(-4.93683e-09*(pt*(pt*(pt/(1+(0.00152436*pt))))));
		mistag_up = (1.47515*((1+(-0.000484868*pt))+(2.36817e-07*(pt*pt))))+(-2.05073e-11*(pt*(pt*(pt/(1+(-0.00142819*pt))))));
		mistag_nominal = (0.000919586+(0.00026266*pt))+(-1.75723e-07*(pt*pt));
	}

	if ((fabs(eta)>=0.8) &&  (fabs(eta)<=1.6))
	{
		mistag_central = (1.24986*((1+(-0.00039734*pt))+(5.37486e-07*(pt*pt))))+(-1.74023e-10*(pt*(pt*(pt/(1+(-0.00112954*pt))))));
		mistag_down = (1.08828*((1+(-0.000208737*pt))+(1.50487e-07*(pt*pt))))+(-2.54249e-11*(pt*(pt*(pt/(1+(-0.00141477*pt))))));
		mistag_up = (1.41211*((1+(-0.000559603*pt))+(9.50754e-07*(pt*pt))))+(-5.81148e-10*(pt*(pt*(pt/(1+(-0.000787359*pt))))));
		mistag_nominal = (-0.00364137+(0.000350371*pt))+(-1.89967e-07*(pt*pt));
	}

	if ((fabs(eta)>=1.6) &&  (fabs(eta)<=2.4))
	{
		mistag_central = (1.10763*((1+(-0.000105805*pt))+(7.11718e-07*(pt*pt))))+(-5.3001e-10*(pt*(pt*(pt/(1+(-0.000821215*pt))))));
		mistag_down = (0.958079*((1+(0.000327804*pt))+(-4.09511e-07*(pt*pt))))+(-1.95933e-11*(pt*(pt*(pt/(1+(-0.00143323*pt))))));
		mistag_up = (1.26236*((1+(-0.000524055*pt))+(2.08863e-06*(pt*pt))))+(-2.29473e-09*(pt*(pt*(pt/(1+(-0.000276268*pt))))));
		mistag_nominal = (-0.00483904+(0.000367751*pt))+(-1.36152e-07*(pt*pt));
	}

	float efferr = 0.0;
	if (pt >=  30. && pt <  40.) efferr =   0.0311456;
	if (pt >=  40. && pt <  50.) efferr =   0.0303825;
	if (pt >=  50. && pt <  60.) efferr =   0.0209488;
	if (pt >=  60. && pt <  70.) efferr =   0.0216987;
	if (pt >=  70. && pt <  80.) efferr =   0.0227149;
	if (pt >=  80. && pt < 100.) efferr =   0.0260294;
	if (pt >= 100. && pt < 120.) efferr =   0.0205766;
	if (pt >= 120. && pt < 160.) efferr =   0.0227065;
	if (pt >= 160. && pt < 210.) efferr =   0.0260481;
	if (pt >= 210. && pt < 260.) efferr =   0.0278001;
	if (pt >= 260. && pt < 320.) efferr =   0.0295361;
	if (pt >= 320. && pt < 400.) efferr =   0.0306555;
	if (pt >= 400. && pt < 500.) efferr =   0.0367805;
	if (pt >= 500. && pt < 670.) efferr =   0.0527368;
	if (pt >= 670.) efferr  =   0.0527368*2.0;

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


// BTagging with data/MC rescaling for TCHEL
vector<bool> BTagTCHEL(float pt, bool isdata,float discrim, float eta, int evt)
{

	double dseedmod = fabs(eta*eta*1000000+42);
	int dseed = int(floor(abs(dseedmod)));
	int evtseed = abs( int(floor((1.0*evt)+10000)) -42 );

	rr->SetSeed(evtseed + dseed );

	vector<bool> tags;
	float discrim_cut = 1.7;

	float eff_central  = 0.603913*((1.+(0.286361*pt))/(1.+(0.170474*pt)));

	float mistag_central = 0.0;
	float mistag_down    = 0.0;
	float mistag_up      = 0.0;
	float mistag_nominal = 0.0;

	if ((fabs(eta)>=0.0) &&  (fabs(eta)<=0.5))
	{
		mistag_central =(1.13615*((1+(-0.00119852*pt))+(1.17888e-05*(pt*pt))))+(-9.8581e-08*(pt*(pt*(pt/(1+(0.00689317*pt))))));
		mistag_down = (1.0369*((1+(-0.000945578*pt))+(7.73273e-06*(pt*pt))))+(-4.47791e-08*(pt*(pt*(pt/(1+(0.00499343*pt))))));
		mistag_up = (1.22179*((1+(-0.000946228*pt))+(7.37821e-06*(pt*pt))))+(-4.8451e-08*(pt*(pt*(pt/(1+(0.0047976*pt))))));
		mistag_nominal = (((-0.0235318+(0.00268868*pt))+(-6.47688e-06*(pt*pt)))+(7.92087e-09*(pt*(pt*pt))))+(-4.06519e-12*(pt*(pt*(pt*pt))));
	}

	if ((fabs(eta)>=0.5) &&  (fabs(eta)<=1.0))
	{
		mistag_central =(1.13277*((1+(-0.00084146*pt))+(3.80313e-06*(pt*pt))))+(-8.75061e-09*(pt*(pt*(pt/(1+(0.00118695*pt))))));
		mistag_down = (0.983748*((1+(7.13613e-05*pt))+(-1.08648e-05*(pt*pt))))+(2.96162e-06*(pt*(pt*(pt/(1+(0.282104*pt))))));
		mistag_up = (1.22714*((1+(-0.00085562*pt))+(3.74425e-06*(pt*pt))))+(-8.91028e-09*(pt*(pt*(pt/(1+(0.00109346*pt))))));
		mistag_nominal = (((-0.0257274+(0.00289337*pt))+(-7.48879e-06*(pt*pt)))+(9.84928e-09*(pt*(pt*pt))))+(-5.40844e-12*(pt*(pt*(pt*pt))));
	}

	if ((fabs(eta)>=1.0) &&  (fabs(eta)<=1.5))
	{
		mistag_central =(1.17163*((1+(-0.000828475*pt))+(3.0769e-06*(pt*pt))))+(-4.692e-09*(pt*(pt*(pt/(1+(0.000337759*pt))))));
		mistag_down = (1.0698*((1+(-0.000731877*pt))+(2.56922e-06*(pt*pt))))+(-3.0318e-09*(pt*(pt*(pt/(1+(5.04118e-05*pt))))));
		mistag_up = (1.27351*((1+(-0.000911891*pt))+(3.5465e-06*(pt*pt))))+(-6.69625e-09*(pt*(pt*(pt/(1+(0.000590847*pt))))));
		mistag_nominal = (((-0.0310046+(0.00307803*pt))+(-7.94145e-06*(pt*pt)))+(1.06889e-08*(pt*(pt*pt))))+(-6.08971e-12*(pt*(pt*(pt*pt))));
	}

	if ((fabs(eta)>=1.5) &&  (fabs(eta)<=2.4))
	{
		mistag_central =(1.14554*((1+(-0.000128043*pt))+(4.10899e-07*(pt*pt))))+(-2.07565e-10*(pt*(pt*(pt/(1+(-0.00118618*pt))))));
		mistag_down = (1.04766*((1+(-6.87499e-05*pt))+(2.2454e-07*(pt*pt))))+(-1.18395e-10*(pt*(pt*(pt/(1+(-0.00128734*pt))))));
		mistag_up = (1.24367*((1+(-0.000182494*pt))+(5.92637e-07*(pt*pt))))+(-3.3745e-10*(pt*(pt*(pt/(1+(-0.00107694*pt))))));
		mistag_nominal = (((-0.0274561+(0.00301096*pt))+(-8.89588e-06*(pt*pt)))+(1.40142e-08*(pt*(pt*pt))))+(-8.95723e-12*(pt*(pt*(pt*pt))));
	}

	float efferr = 0.0;

	if (pt >=  30. && pt <  40.) efferr =   0.0244956;
	if (pt >=  40. && pt <  50.) efferr =   0.0237293;
	if (pt >=  50. && pt <  60.) efferr =   0.0180131;
	if (pt >=  60. && pt <  70.) efferr =   0.0182411;
	if (pt >=  70. && pt <  80.) efferr =   0.0184592;
	if (pt >=  80. && pt < 100.) efferr =   0.0106444;
	if (pt >= 100. && pt < 120.) efferr =   0.011073;
	if (pt >= 120. && pt < 160.) efferr =   0.0106296;
	if (pt >= 160. && pt < 210.) efferr =   0.0175259;
	if (pt >= 210. && pt < 260.) efferr =   0.0161566;
	if (pt >= 260. && pt < 320.) efferr =   0.0158973;
	if (pt >= 320. && pt < 400.) efferr =   0.0186782;
	if (pt >= 400. && pt < 500.) efferr =   0.0371113;
	if (pt >= 500. && pt < 670.) efferr =   0.0289788;
	if (pt >= 670.) efferr  =   0.0289788*2.0;

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


// The Main analysis loop. 
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
	//         DECLARATION OF BRANCHES IN TREE
	//*****************************************************************

	int ngood = 0;
	int nbad = 0;

	Double_t weight=0.0;
	Double_t xsection=0.0;
	Double_t Events_Orig=0.0;
	Double_t N_PileUpInteractions=0.0;
	Double_t Pt_HEEPele1=0.0;

	// Particle Counts
	BRANCH(PFJetCount); BRANCH(BpfJetCount);
	BRANCH(GenJet30Count);
	BRANCH(PFJet30Count);

	BRANCH(PFJet30TCHPTCountCentral);
	BRANCH(PFJet30TCHPTCountEffUp);
	BRANCH(PFJet30TCHPTCountEffDown);
	BRANCH(PFJet30TCHPTCountMisUp);
	BRANCH(PFJet30TCHPTCountMisDown);

	BRANCH(PFJet30SSVHPTCountCentral);
	BRANCH(PFJet30SSVHPTCountEffUp);
	BRANCH(PFJet30SSVHPTCountEffDown);
	BRANCH(PFJet30SSVHPTCountMisUp);
	BRANCH(PFJet30SSVHPTCountMisDown);

	BRANCH(PFJet30JPTCountCentral);
	BRANCH(PFJet30JPTCountEffUp);
	BRANCH(PFJet30JPTCountEffDown);
	BRANCH(PFJet30JPTCountMisUp);
	BRANCH(PFJet30JPTCountMisDown);

	BRANCH(PFJet30TCHEMCountCentral);
	BRANCH(PFJet30TCHEMCountEffUp);
	BRANCH(PFJet30TCHEMCountEffDown);
	BRANCH(PFJet30TCHEMCountMisUp);
	BRANCH(PFJet30TCHEMCountMisDown);

	BRANCH(PFJet30TCHELCountCentral);
	BRANCH(PFJet30TCHELCountEffUp);
	BRANCH(PFJet30TCHELCountEffDown);
	BRANCH(PFJet30TCHELCountMisUp);
	BRANCH(PFJet30TCHELCountMisDown);

	BRANCH(PFJet30TCHPTUnCorrCountCentral);

	// Event Information
	UInt_t run_number,event_number,ls_number;
	tree->Branch("event_number",&event_number,"event_number/i");
	tree->Branch("run_number",&run_number,"run_number/i");
	tree->Branch("ls_number",&ls_number,"ls_number/i");
	BRANCH(bx);
	BRANCH(N_Vertices);
	BRANCH(N_GoodVertices);
	BRANCH(weight_pu_central); BRANCH(weight_pu_sysplus); BRANCH(weight_pu_sysminus); BRANCH(weight_gen);
	BRANCH(pass_HBHENoiseFilter); BRANCH(pass_isBPTX0); BRANCH(pass_passBeamHaloFilterLoose);
	BRANCH(pass_passBeamHaloFilterTight);
	BRANCH(pass_isTrackingFailure);


	// Generator Level Variables
	BRANCH(Pt_genjet1);  BRANCH(Phi_genjet1);  BRANCH(Eta_genjet1);
	BRANCH(Pt_genjet2);  BRANCH(Phi_genjet2);  BRANCH(Eta_genjet2);
	BRANCH(Pt_genjet3);  BRANCH(Phi_genjet3);  BRANCH(Eta_genjet3);
	BRANCH(Pt_genjet4);  BRANCH(Phi_genjet4);  BRANCH(Eta_genjet4);
	BRANCH(Pt_genjet5);  BRANCH(Phi_genjet5);  BRANCH(Eta_genjet5);

	BRANCH(DeltaPhi_genjet1genmuon1);
	BRANCH(DeltaPhi_genjet2genmuon1);
	BRANCH(DeltaPhi_genjet3genmuon1);
	BRANCH(DeltaPhi_genjet4genmuon1);
	BRANCH(DeltaPhi_genjet5genmuon1);

	BRANCH(HT_genjets);


	BRANCH(Pt_genmuon1);  BRANCH(Phi_genmuon1);  BRANCH(Eta_genmuon1);
	BRANCH(Pt_genmuon2);  BRANCH(Phi_genmuon2);  BRANCH(Eta_genmuon2);

	BRANCH(Pt_genmuonneutrino1);  BRANCH(Phi_genmuonneutrino1);  BRANCH(Eta_genmuonneutrino1);
	BRANCH(Pt_genMET);  BRANCH(Phi_genMET);

	BRANCH(MT_genmuon1genMET);
	BRANCH(MT_genmuon1genneutrino);



	// Reco Level Variables
	BRANCH(Pt_pfjet1);  BRANCH(Phi_pfjet1);  BRANCH(Eta_pfjet1);
	BRANCH(Pt_pfjet2);  BRANCH(Phi_pfjet2);  BRANCH(Eta_pfjet2);
	BRANCH(Pt_pfjet3);  BRANCH(Phi_pfjet3);  BRANCH(Eta_pfjet3);
	BRANCH(Pt_pfjet4);  BRANCH(Phi_pfjet4);  BRANCH(Eta_pfjet4);
	BRANCH(Pt_pfjet5);  BRANCH(Phi_pfjet5);  BRANCH(Eta_pfjet5);

	BRANCH(DeltaPhi_pfjet1muon1);
	BRANCH(DeltaPhi_pfjet2muon1);
	BRANCH(DeltaPhi_pfjet3muon1);
	BRANCH(DeltaPhi_pfjet4muon1);
	BRANCH(DeltaPhi_pfjet5muon1);

	BRANCH(Pt_pfjet1_pt20);   BRANCH(Eta_pfjet1_eta2p5);
	BRANCH(Pt_pfjet2_pt20);   BRANCH(Eta_pfjet2_eta2p5);
	BRANCH(Pt_pfjet3_pt20);   BRANCH(Eta_pfjet3_eta2p5);
	BRANCH(Pt_pfjet4_pt20);   BRANCH(Eta_pfjet4_eta2p5);
	BRANCH(Pt_pfjet5_pt20);   BRANCH(Eta_pfjet5_eta2p5);


	BRANCH(DeltaPhi_pfjet1muon1_hasgenmatch);
	BRANCH(DeltaPhi_pfjet2muon1_hasgenmatch);
	BRANCH(DeltaPhi_pfjet3muon1_hasgenmatch);
	BRANCH(DeltaPhi_pfjet4muon1_hasgenmatch);
	BRANCH(DeltaPhi_pfjet5muon1_hasgenmatch);

	BRANCH(Pt_pfjet1_pt20_hasgenmatch);   BRANCH(Eta_pfjet1_eta2p5_hasgenmatch);
	BRANCH(Pt_pfjet2_pt20_hasgenmatch);   BRANCH(Eta_pfjet2_eta2p5_hasgenmatch);
	BRANCH(Pt_pfjet3_pt20_hasgenmatch);   BRANCH(Eta_pfjet3_eta2p5_hasgenmatch);
	BRANCH(Pt_pfjet4_pt20_hasgenmatch);   BRANCH(Eta_pfjet4_eta2p5_hasgenmatch);
	BRANCH(Pt_pfjet5_pt20_hasgenmatch);   BRANCH(Eta_pfjet5_eta2p5_hasgenmatch);

	BRANCH(HT_pfjets);

	BRANCH(Pt_muon1);  BRANCH(Phi_muon1);  BRANCH(Eta_muon1);
	BRANCH(Pt_muon2);  BRANCH(Phi_muon2);  BRANCH(Eta_muon2);
	BRANCH(RelIso_muon1);
	BRANCH(RelIso_muon2);

	BRANCH(Pt_MET);  BRANCH(Phi_MET);
	BRANCH(Pt_METUnProp);  BRANCH(Phi_METUnProp);

	BRANCH(Pt_MET1);  BRANCH(Phi_MET1);
	BRANCH(Pt_MET1UnProp);  BRANCH(Phi_MET1UnProp);

	BRANCH(Pt_METR);  BRANCH(Phi_METR);

	BRANCH(MT_muon1MET);
	BRANCH(MT_muon1METUnProp);
	BRANCH(MT_muon1MET1);
	BRANCH(MT_muon1MET1UnProp);
	BRANCH(MT_muon1METR);

	BRANCH(M_muon1muon2);

	BRANCH(U1_Z);
	BRANCH(U2_Z);
	BRANCH(U1_W);
	BRANCH(U2_W);

	BRANCH(Pt_W);  BRANCH(Pt_Z);

	// Trigger and other
	BRANCH(Mu24Pass);
	BRANCH(Mu24PassPrescale);

	BRANCH(IsoMu24Pass);

	Double_t HLTIsoMu24Pass=0.0; 
	Double_t HLTMu24Pass=0.0;	 				 
	Double_t HLTMu24PassPrescale=0.0;
	Double_t HLTMu24TriggerPass=0.0;

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

	// Another placeHolder. Needed because recoil corrections only get applied to W MC.
	bool IsW = IsItWMC;
	bool IsSherpa = IsItSherpa;
	bool IsPhiCorr = IsItPhiCorr;

	//===================================================================================================
	//===================================================================================================

	//===================================================================================================
	//           LOOP OVER ENTRIES AND MAKE MAIN CALCULATIONS
	//===================================================================================================

	if (fChain == 0) return;	 //check for correctly assigned chain from h file

	Long64_t nentries = fChain->GetEntriesFast();
	Long64_t nbytes = 0, nb = 0;

	for (Long64_t jentry=0; jentry<nentries;jentry++)
	{
		Long64_t ientry = LoadTree(jentry);
		if (ientry < 0) break;
		nb = fChain->GetEntry(jentry);   nbytes += nb;

		//if (jentry>5) break;  // comment this!!! testing only !

		// Important Event Informations
		run_number = run;
		event_number = event;
		int nevent = 1*event;
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
		pass_passBeamHaloFilterLoose = 1.0*passBeamHaloFilterLoose ;
		pass_passBeamHaloFilterTight = 1.0*passBeamHaloFilterTight ;
		pass_isTrackingFailure = 1.00*(1.0-1.0*isTrackingFailure);

		//========================= MET CORRECTIONS ===============================================//

		if (IsPhiCorr)
		{
			TLorentzVector __MET;
			__MET.SetPtEtaPhiM(PFMET->at(0),0.0,PFMETPhi->at(0),0.0);
			TLorentzVector CorrectedMET;
			CorrectedMET = PhiMod_Corr(__MET, N_Vertices, isData);
			PFMET->at(0) = 1.0*CorrectedMET.Pt();
			PFMETPhi->at(0) = CorrectedMET.Phi();
		}

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

		weight_pu_sysplus = weight;
		if ((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)) weight_pu_sysplus *=(0.0112175149831);
		if ((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)) weight_pu_sysplus *=(0.121087734395);
		if ((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)) weight_pu_sysplus *=(0.287818611927);
		if ((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)) weight_pu_sysplus *=(0.527626529094);
		if ((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)) weight_pu_sysplus *=(0.783696354059);
		if ((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)) weight_pu_sysplus *=(1.00650439276);
		if ((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)) weight_pu_sysplus *=(1.17348981006);
		if ((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)) weight_pu_sysplus *=(1.28401095679);
		if ((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)) weight_pu_sysplus *=(1.357600308);
		if ((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)) weight_pu_sysplus *=(1.41316079322);
		if ((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)) weight_pu_sysplus *=(1.46840359255);
		if ((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)) weight_pu_sysplus *=(1.53584652637);
		if ((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)) weight_pu_sysplus *=(1.62231760959);
		if ((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)) weight_pu_sysplus *=(1.7281969113);
		if ((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)) weight_pu_sysplus *=(1.86149776904);
		if ((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)) weight_pu_sysplus *=(2.01240230333);
		if ((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)) weight_pu_sysplus *=(2.18057433714);
		if ((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)) weight_pu_sysplus *=(2.36135499357);
		if ((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)) weight_pu_sysplus *=(2.54687256712);
		if ((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)) weight_pu_sysplus *=(2.73766248268);
		if ((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)) weight_pu_sysplus *=(2.92573330254);
		if ((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)) weight_pu_sysplus *=(3.08732938139);
		if ((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)) weight_pu_sysplus *=(3.24129022175);
		if ((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)) weight_pu_sysplus *=(3.38259901992);
		if ((N_PileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)) weight_pu_sysplus *=(3.49697385281);
		if ((N_PileUpInteractions > 24.5)*(N_PileUpInteractions < 25.5)) weight_pu_sysplus *=(3.57554823181);
		if ((N_PileUpInteractions > 25.5)*(N_PileUpInteractions < 26.5)) weight_pu_sysplus *=(3.63731823179);
		if ((N_PileUpInteractions > 26.5)*(N_PileUpInteractions < 27.5)) weight_pu_sysplus *=(3.62307016401);
		if ((N_PileUpInteractions > 27.5)*(N_PileUpInteractions < 28.5)) weight_pu_sysplus *=(3.62434601903);
		if ((N_PileUpInteractions > 28.5)*(N_PileUpInteractions < 29.5)) weight_pu_sysplus *=(3.63862461648);
		if ((N_PileUpInteractions > 29.5)*(N_PileUpInteractions < 30.5)) weight_pu_sysplus *=(3.55010065753);
		if ((N_PileUpInteractions > 30.5)*(N_PileUpInteractions < 31.5)) weight_pu_sysplus *=(3.39605083666);
		if ((N_PileUpInteractions > 31.5)*(N_PileUpInteractions < 32.5)) weight_pu_sysplus *=(3.25850301355);
		if ((N_PileUpInteractions > 32.5)*(N_PileUpInteractions < 33.5)) weight_pu_sysplus *=(3.27052653183);
		if ((N_PileUpInteractions > 33.5)*(N_PileUpInteractions < 34.5)) weight_pu_sysplus *=(3.07305167562);

		weight_pu_sysminus = weight;

		if ((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)) weight_pu_sysminus *=(0.0174672651878);
		if ((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)) weight_pu_sysminus *=(0.178898832821);
		if ((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)) weight_pu_sysminus *=(0.401652393124);
		if ((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)) weight_pu_sysminus *=(0.695533833086);
		if ((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)) weight_pu_sysminus *=(0.978362056364);
		if ((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)) weight_pu_sysminus *=(1.19500460721);
		if ((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)) weight_pu_sysminus *=(1.33210542995);
		if ((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)) weight_pu_sysminus *=(1.4014869583);
		if ((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)) weight_pu_sysminus *=(1.4320486024);
		if ((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)) weight_pu_sysminus *=(1.44568599859);
		if ((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)) weight_pu_sysminus *=(1.45867953698);
		if ((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)) weight_pu_sysminus *=(1.47958829465);
		if ((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)) weight_pu_sysminus *=(1.5104596995);
		if ((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)) weight_pu_sysminus *=(1.54748743432);
		if ((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)) weight_pu_sysminus *=(1.59422320097);
		if ((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)) weight_pu_sysminus *=(1.63924419015);
		if ((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)) weight_pu_sysminus *=(1.68076565709);
		if ((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)) weight_pu_sysminus *=(1.71442150291);
		if ((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)) weight_pu_sysminus *=(1.7349217562);
		if ((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)) weight_pu_sysminus *=(1.74389791031);
		if ((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)) weight_pu_sysminus *=(1.73791143581);
		if ((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)) weight_pu_sysminus *=(1.70611386863);
		if ((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)) weight_pu_sysminus *=(1.66307074529);
		if ((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)) weight_pu_sysminus *=(1.60874288266);
		if ((N_PileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)) weight_pu_sysminus *=(1.53939902456);
		if ((N_PileUpInteractions > 24.5)*(N_PileUpInteractions < 25.5)) weight_pu_sysminus *=(1.45511270561);
		if ((N_PileUpInteractions > 25.5)*(N_PileUpInteractions < 26.5)) weight_pu_sysminus *=(1.3670186575);
		if ((N_PileUpInteractions > 26.5)*(N_PileUpInteractions < 27.5)) weight_pu_sysminus *=(1.25636754216);
		if ((N_PileUpInteractions > 27.5)*(N_PileUpInteractions < 28.5)) weight_pu_sysminus *=(1.15870268872);
		if ((N_PileUpInteractions > 28.5)*(N_PileUpInteractions < 29.5)) weight_pu_sysminus *=(1.07173897222);
		if ((N_PileUpInteractions > 29.5)*(N_PileUpInteractions < 30.5)) weight_pu_sysminus *=(0.962813980476);
		if ((N_PileUpInteractions > 30.5)*(N_PileUpInteractions < 31.5)) weight_pu_sysminus *=(0.847622106151);
		if ((N_PileUpInteractions > 31.5)*(N_PileUpInteractions < 32.5)) weight_pu_sysminus *=(0.748135881033);
		if ((N_PileUpInteractions > 32.5)*(N_PileUpInteractions < 33.5)) weight_pu_sysminus *=(0.690478414815);
		if ((N_PileUpInteractions > 33.5)*(N_PileUpInteractions < 34.5)) weight_pu_sysminus *=(0.596395110807);

		//========================     Trigger Scanning  ================================//

		string hltmu ("HLT_Mu");
		string hltisomu ("HLT_IsoMu24");
		string eta2p1 ("eta2p1");
		string hltmu24 ("HLT_Mu24");
		string hltmu24eta2p1 ("HLT_Mu24_eta2p1_v");

		HLTMu24TriggerPass = -1.;

		vector <double> SingleMuThresholds;
		vector <int> SingleMuPrescales;
		vector <int> SingleMuPasses;

		// std::cout<<" - - - - - - - - - - "<<run<<"  muon pt = "<< MuonPt->at(0)<<std::endl;
		HLTIsoMu24Pass = 0;
		for(unsigned int iHLT = 0; iHLT != HLTInsideDatasetTriggerNames->size(); ++iHLT)
		{
			string thishlt = HLTInsideDatasetTriggerNames->at(iHLT);
			bool isSingleMuTrigger = (thishlt.compare(0,11,hltisomu)==0) && (thishlt.length()>7) && (thishlt.length()<24);
			if (!isSingleMuTrigger) continue;
			// std::cout<<thishlt<<"   "<<HLTInsideDatasetTriggerPrescales->at(iHLT)<<std::endl;
			// if (!(HLTInsideDatasetTriggerPrescales->at(iHLT)) == 1) continue;
			// std::cout<<"  -- using, pass= "<<HLTInsideDatasetTriggerDecisions->at(iHLT)<<std::endl;
			HLTIsoMu24Pass = HLTInsideDatasetTriggerDecisions->at(iHLT);
			if (HLTIsoMu24Pass  > 0) break;
		}
		IsoMu24Pass = HLTIsoMu24Pass;

		HLTMu24Pass = 0;
		HLTMu24PassPrescale = 0;

		for(unsigned int iHLT = 0; iHLT != HLTInsideDatasetTriggerNames->size(); ++iHLT)
		{
			string thishlt = HLTInsideDatasetTriggerNames->at(iHLT);
			bool isSingleMuTrigger = (thishlt.compare(0,8,hltmu24)==0) && (thishlt.length()>7) && (thishlt.length()<14);
			if (!isSingleMuTrigger) continue;
			// std::cout<<thishlt<<"   "<<HLTInsideDatasetTriggerPrescales->at(iHLT)<<std::endl;
			HLTMu24PassPrescale = double(HLTInsideDatasetTriggerPrescales->at(iHLT));
			HLTMu24Pass = HLTInsideDatasetTriggerDecisions->at(iHLT);
			if (HLTIsoMu24Pass  > 0) break;
		}
		Mu24Pass = HLTMu24Pass;
		Mu24PassPrescale = HLTMu24PassPrescale;

		//std::cout<<Mu24Pass<<"   "<<Mu24PassPrescale<<std::endl;

		//========================     Jet Rescaling / Smearing Sequence   ================================//

		TLorentzVector JetAdjustedMET;
		JetAdjustedMET.SetPtEtaPhiM(PFMET->at(0),0.0,PFMETPhi->at(0),0);

		TLorentzVector JetAdjustedMET1;
		JetAdjustedMET1.SetPtEtaPhiM(PFMETType1Cor->at(0),0.0,PFMETPhiType1Cor->at(0),0);

		TLorentzVector JetAdjustedMETUnProp;
		JetAdjustedMETUnProp.SetPtEtaPhiM(PFMET->at(0),0.0,PFMETPhi->at(0),0);

		TLorentzVector JetAdjustedMET1UnProp;
		JetAdjustedMET1UnProp.SetPtEtaPhiM(PFMETType1Cor->at(0),0.0,PFMETPhiType1Cor->at(0),0);


		// Loop over jets and modify pT for systematics
		int filterjetcount = 0;
		for(unsigned int ijet = 0; ijet < PFJetPt->size(); ++ijet)
		{
			if (filterjetcount >=20) continue;
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
				if (ThisLepton.Pt() < 20) continue;
				JetLepDR = ThisLepton.DeltaR(ThisPFJet);
				if (JetLepDR < .3) consider = false;
				break;		 // lead muon only
			}

			if (!consider) continue;

			double NewJetRescalingFactor = JetRescaleFactor;

			if (false)
			{
				NewJetRescalingFactor = 1.0+NewJesUncertainty((JetRescaleFactor - 1.0), (*PFJetPtRaw)[ijet], (*PFJetEta)[ijet]);
				if (JetRescaleFactor < 1.0) NewJetRescalingFactor = 2.0 - NewJetRescalingFactor;
			}

			double NewJetPT = (*PFJetPt)[ijet];

			if (JetRescaleFactor > 1.00) NewJetPT *= (1+PFJetJECUnc->at(ijet))  ;
			if (JetRescaleFactor < 1.00) NewJetPT *= (1-PFJetJECUnc->at(ijet))  ;


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
			Double_t Standard_rescale = 1.0;
			if (false)
			{
				if (SmallestDeltaR<0.5) Standard_rescale = 1.1;
			}
			Double_t JetAdjustmentFactor = GetRecoGenJetScaleFactor(PFJetPt->at(ijet),ClosestGenJetPT,Standard_rescale);
			NewJetPT *=JetAdjustmentFactor;
			JetAdjustedMET = PropagatePTChangeToMET(JetAdjustedMET.Pt(),  JetAdjustedMET.Phi(), NewJetPT, (*PFJetPt)[ijet], PFJetPhi->at(ijet));
			JetAdjustedMET1 = PropagatePTChangeToMET(JetAdjustedMET1.Pt(),  JetAdjustedMET1.Phi(), NewJetPT, (*PFJetPt)[ijet], PFJetPhi->at(ijet));

			if (JetSmearFactor > 0.0)
			{

				Double_t JetEta = fabs(PFJetEta->at(ijet));
				Double_t Systematic_rescale =   JERFactor(JetEta);
				Double_t JetAdjustmentFactorSys = GetRecoGenJetScaleFactor(PFJetPt->at(ijet),ClosestGenJetPT,Systematic_rescale);
				if (SmallestDeltaR<0.5) NewJetPT *=JetAdjustmentFactorSys;
				// NewJetPT *=JetAdjustmentFactorSys;

			}


			JetAdjustedMET = PropagatePTChangeToMET(JetAdjustedMET.Pt(),  JetAdjustedMET.Phi(), NewJetPT, (*PFJetPt)[ijet], PFJetPhi->at(ijet));
			JetAdjustedMET1 = PropagatePTChangeToMET(JetAdjustedMET1.Pt(),  JetAdjustedMET1.Phi(), NewJetPT, (*PFJetPt)[ijet], PFJetPhi->at(ijet));

			(*PFJetPt)[ijet] = NewJetPT ;
		}
		// Reset MET values
		(*PFMET)[0] = JetAdjustedMET.Pt();
		(*PFMETPhi)[0] = JetAdjustedMET.Phi();

		//========================     Muon Rescaling / Smearing Sequence   ================================//

		TLorentzVector MuAdjustedMET;
		MuAdjustedMET.SetPtEtaPhiM(PFMET->at(0),0.0,PFMETPhi->at(0),0);
		// MuAdjustedMET1.SetPtEtaPhiM(PFMETType1Cor->at(0),0.0,PFMETPhiType1Cor->at(0),0);

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
				// MuonIsTracker ->at(imuon) == 1 &&
					MuonRelIso->at(imuon) < 0.15 &&
					MuonTrkHitsTrackerOnly ->at(imuon) >= 11   ;

				bool PassPOGTight =
					MuonStationMatches->at(imuon) > 1 &&
					fabs(MuonPrimaryVertexDXY ->at(imuon)) < 0.2  &&
								 /// Disable for EWK
					MuonGlobalChi2 ->at(imuon) < 10.0 &&
					MuonTrkPixelHitCount ->at(imuon) >=1 &&
					MuonGlobalTrkValidHits->at(imuon)>=1 ;

				if ( ! (PassGlobalTightPrompt && PassPOGTight) ) continue;

				double NewMuonPT =  ScaleObject((*MuonPt)[imuon],MuonRescaleFactor);
				NewMuonPT =  SmearObject(NewMuonPT,MuonSmearFactor);
				MuAdjustedMET = PropagatePTChangeToMET(MuAdjustedMET.Pt(),  MuAdjustedMET.Phi(), NewMuonPT, (*MuonPt)[imuon], MuonPhi->at(imuon));
				JetAdjustedMET1 = PropagatePTChangeToMET(JetAdjustedMET1.Pt(),  JetAdjustedMET1.Phi(), NewMuonPT, (*MuonPt)[imuon], MuonPhi->at(imuon));

				(*MuonPt)[imuon] = NewMuonPT ;
			}
		}
		(*PFMET)[0] = MuAdjustedMET.Pt();
		(*PFMETPhi)[0] = MuAdjustedMET.Phi();
		(*PFMETType1Cor)[0] = JetAdjustedMET1.Pt();
		(*PFMETPhiType1Cor)[0] = JetAdjustedMET1.Phi();


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
		int HEEPEle25Count = 1.0*v_idx_ele_good_final.size();

		//========================      Muon Conditions   ================================//

		vector<TLorentzVector> RecoMuons, RecoJets, RecoJetsLooseEta, RecoJetsLoosePt;
		vector<int> v_idx_muon_final;
		vector<double> RecoMuonIso;
		bool checkPT = true;	 // Pt requirement only on first muon at this stage
		bool checkIso = true;	 // Pt requirement only on first muon at this stage


		Double_t muoniso = 1.0;
		for(unsigned int imuon = 0; imuon < MuonPt->size(); ++imuon)
		{

			Double_t muonPt = MuonPt->at(imuon);
			Double_t muonEta = MuonEta->at(imuon);

			if (checkPT && (muonPt < 23.0) ) continue;
			if  ( fabs(muonEta) > 2.1 )      continue;

			bool PassGlobalTightPrompt =
				MuonIsGlobal ->at(imuon) == 1 &&
				MuonTrkHitsTrackerOnly ->at(imuon) >= 11   ;

			bool PassPOGTight =
				MuonStationMatches->at(imuon) > 1 &&
				fabs(MuonPrimaryVertexDXY ->at(imuon)) < 0.2  &&
				MuonGlobalChi2 ->at(imuon) < 10.0 &&
				MuonTrkPixelHitCount ->at(imuon) >=1 &&
				MuonGlobalTrkValidHits->at(imuon)>=1 ;

			if ( ! (PassGlobalTightPrompt && PassPOGTight) ) continue;
			TLorentzVector muon;
			muon.SetPtEtaPhiM( MuonPt -> at(imuon), MuonEta-> at(imuon),    MuonPhi-> at(imuon),    0);
			RecoMuons.push_back(muon);
			RecoMuonIso.push_back(MuonRelIso->at(imuon));
			checkIso = false;
			if (muoniso > 0.999) muoniso = MuonRelIso->at(imuon);
			v_idx_muon_final.push_back(imuon);
			if (v_idx_muon_final.size()>=1) checkPT=false;
		}						 // loop over muons

		RecoMuonIso.push_back(99.1);
		RecoMuonIso.push_back(99.2);

		TLorentzVector elorentz;

		elorentz.SetPtEtaPhiM(0.,0.,0.,0.);

		int LeadMuonVertex=0;
		if (v_idx_muon_final.size() <1)
		{
			RecoMuons.push_back(elorentz);
		}
		else
		{
			LeadMuonVertex=MuonVtxIndex->at(v_idx_muon_final[0]);

		}
		if (v_idx_muon_final.size() <2)
		{
			RecoMuons.push_back(elorentz);
		}

		int MuonCount = RecoMuons.size();


		//========================     PFJet Conditions   ================================//
		// Get Good Jets in general

		vector<TLorentzVector> jets;
		vector<int> v_idx_pfjet_prefinal;
		vector<int> v_idx_pfjet_final;
		BpfJetCount = 0.0;
		TLorentzVector CurrentLepton,CurrentPFJet;

		TLorentzVector thisjet, thismu, thise;

		int muindex = 99;
		int eindex = 99;
		int jetindex = 99;

		// Initial Jet Quality Selection, loose 20GeV jets
		for(unsigned int ijet = 0; ijet < PFJetPt->size(); ++ijet)
		{
			double jetPt = PFJetPt -> at(ijet);
			double jetEta = PFJetEta -> at(ijet);
			CurrentPFJet.SetPtEtaPhiM((*PFJetPt)[ijet],(*PFJetEta)[ijet],(*PFJetPhi)[ijet],0);

			if (PFJetBestVertexTrackAssociationIndex->at(ijet) != LeadMuonVertex) continue;

			bool IsLepton = false;

			// if ((PFJetPassLooseID->at(ijet) != 1)&&(PFJetPt->at(ijet) > FailIDPFThreshold)&&(!IsLepton)) FailIDPFThreshold = PFJetPt->at(ijet);
			if ( jetPt < 20.0 ) continue;
			if ( fabs(jetEta) > 2.5 ) continue;
			if (PFJetPassLooseID->at(ijet) != 1) continue;
			v_idx_pfjet_prefinal.push_back(ijet);
		}
		// Filter out jets that are actually muons or electrons

		PFJet30Count = 0.0;

		PFJet30TCHPTCountCentral = 0.0;
		PFJet30TCHPTCountEffUp = 0.0;
		PFJet30TCHPTCountEffDown = 0.0;
		PFJet30TCHPTCountMisUp = 0.0;
		PFJet30TCHPTCountMisDown = 0.0;
		PFJet30TCHPTUnCorrCountCentral = 0.0;

		PFJet30SSVHPTCountCentral = 0.0;
		PFJet30SSVHPTCountEffUp = 0.0;
		PFJet30SSVHPTCountEffDown = 0.0;
		PFJet30SSVHPTCountMisUp = 0.0;
		PFJet30SSVHPTCountMisDown = 0.0;

		PFJet30JPTCountCentral = 0.0;
		PFJet30JPTCountEffUp = 0.0;
		PFJet30JPTCountEffDown = 0.0;
		PFJet30JPTCountMisUp = 0.0;
		PFJet30JPTCountMisDown = 0.0;

		PFJet30TCHEMCountCentral = 0.0;
		PFJet30TCHEMCountEffUp = 0.0;
		PFJet30TCHEMCountEffDown = 0.0;
		PFJet30TCHEMCountMisUp = 0.0;
		PFJet30TCHEMCountMisDown = 0.0;

		PFJet30TCHELCountCentral = 0.0;
		PFJet30TCHELCountEffUp = 0.0;
		PFJet30TCHELCountEffDown = 0.0;
		PFJet30TCHELCountMisUp = 0.0;
		PFJet30TCHELCountMisDown = 0.0;

		HT_pfjets = 0.0;

		for(unsigned int ijet=0; ijet<v_idx_pfjet_prefinal.size(); ijet++)
		{
			jetindex = v_idx_pfjet_prefinal[ijet];
			thisjet.SetPtEtaPhiM((*PFJetPt)[jetindex],(*PFJetEta)[jetindex],(*PFJetPhi)[jetindex],0);

			bool KeepJet=true;

			for(unsigned int imu=0; imu<v_idx_muon_final.size(); imu++)
			{
				muindex = v_idx_muon_final[imu];
				thismu.SetPtEtaPhiM(MuonPt->at(muindex),MuonEta->at(muindex),MuonPhi->at(muindex),0);
				if (thismu.Pt()<25.0) continue;
				if (thismu.DeltaR(thisjet) < 0.5)       KeepJet=false;
				break;			 // lead muon only
			}

			if (!KeepJet) continue;
			if ( PFJetTrackCountingHighEffBTag->at(jetindex) > 2.0 ) BpfJetCount = BpfJetCount + 1.0;

			v_idx_pfjet_final.push_back(jetindex);

			if (thisjet.Pt() > 30.0 && fabs(thisjet.Eta()) < 2.4)
			{
				RecoJets.push_back(thisjet);
			}

			if (thisjet.Pt() > 20.0 && fabs(thisjet.Eta()) < 2.4)
			{
				RecoJetsLoosePt.push_back(thisjet);
			}

			if (thisjet.Pt() > 30.0 && fabs(thisjet.Eta()) < 2.5)
			{
				RecoJetsLooseEta.push_back(thisjet);
			}


			if (thisjet.Pt() > 30.0 && fabs(thisjet.Eta()) < 2.4)
			{


				HT_pfjets +=thisjet.Pt();

				float tchpt   = PFJetTrackCountingHighPurBTag->at(jetindex);
				float tchem   = PFJetTrackCountingHighEffBTag->at(jetindex);
				float tchel   = PFJetTrackCountingHighEffBTag->at(jetindex);

				float ssvhpt  = PFJetSimpleSecondaryVertexHighPurBTag->at(jetindex);
				float jpt     = PFJetJetProbabilityBTag->at(jetindex);

				// vector<bool> btags = BTags(thisjet.Pt(),isData,tchpt,ssvhpt,jpt,jpbt);
				vector<bool> btags_tchpt = BTagTCHPT(thisjet.Pt(),isData,tchpt,thisjet.Eta(), event);
				vector<bool> btags_tchpt_uncorr = BTagTCHPTUnCorr(thisjet.Pt(),isData,tchpt,thisjet.Eta(), event);

				vector<bool> btags_ssvhpt = BTagSSVHPT(thisjet.Pt(),isData,ssvhpt,thisjet.Eta(), event);
				vector<bool> btags_jpt = BTagJPT(thisjet.Pt(),isData,jpt,thisjet.Eta(), event);

				vector<bool> btags_tchem = BTagTCHEM(thisjet.Pt(),isData,tchem,thisjet.Eta(), event);
				vector<bool> btags_tchel = BTagTCHEL(thisjet.Pt(),isData,tchel,thisjet.Eta(), event);

				PFJet30Count += 1.0;
				PFJet30TCHPTCountCentral += 1.0*(btags_tchpt[0]);
				PFJet30TCHPTCountEffUp   += 1.0*(btags_tchpt[1]);
				PFJet30TCHPTCountEffDown += 1.0*(btags_tchpt[2]);
				PFJet30TCHPTCountMisUp   += 1.0*(btags_tchpt[3]);
				PFJet30TCHPTCountMisDown += 1.0*(btags_tchpt[4]);

				PFJet30SSVHPTCountCentral += 1.0*(btags_ssvhpt[0]);
				PFJet30SSVHPTCountEffUp   += 1.0*(btags_ssvhpt[1]);
				PFJet30SSVHPTCountEffDown += 1.0*(btags_ssvhpt[2]);
				PFJet30SSVHPTCountMisUp   += 1.0*(btags_ssvhpt[3]);
				PFJet30SSVHPTCountMisDown += 1.0*(btags_ssvhpt[4]);

				PFJet30JPTCountCentral += 1.0*(btags_jpt[0]);
				PFJet30JPTCountEffUp   += 1.0*(btags_jpt[1]);
				PFJet30JPTCountEffDown += 1.0*(btags_jpt[2]);
				PFJet30JPTCountMisUp   += 1.0*(btags_jpt[3]);
				PFJet30JPTCountMisDown += 1.0*(btags_jpt[4]);

				PFJet30TCHEMCountCentral += 1.0*(btags_tchem[0]);
				PFJet30TCHEMCountEffUp   += 1.0*(btags_tchem[1]);
				PFJet30TCHEMCountEffDown += 1.0*(btags_tchem[2]);
				PFJet30TCHEMCountMisUp   += 1.0*(btags_tchem[3]);
				PFJet30TCHEMCountMisDown += 1.0*(btags_tchem[4]);

				PFJet30TCHELCountCentral += 1.0*(btags_tchel[0]);
				PFJet30TCHELCountEffUp   += 1.0*(btags_tchel[1]);
				PFJet30TCHELCountEffDown += 1.0*(btags_tchel[2]);
				PFJet30TCHELCountMisUp   += 1.0*(btags_tchel[3]);
				PFJet30TCHELCountMisDown += 1.0*(btags_tchel[4]);

			}
		}


		//========================     Generator Level Calculations  ================================//
		TLorentzVector GenW,GenZ;
		GenW.SetPtEtaPhiM(0.,0.,0.,0.);
		GenZ.SetPtEtaPhiM(0.,0.,0.,0.);

		TLorentzVector  v_GenMet;
		vector<TLorentzVector> GenMuons, GenJets, GenJetsLoose, GenJetsBare, SortedGenMuons, SortedGenJets, GenMuNeutrinos;

		int GenMuonCount = 0;
		if (!isData)
		{

			// Reset Gen Variables
			Pt_genjet1 = 0;       Phi_genjet1 = 0;       Eta_genjet1 = 0; DeltaPhi_genjet1genmuon1 = -1.0;
			Pt_genjet2 = 0;       Phi_genjet2 = 0;       Eta_genjet2 = 0; DeltaPhi_genjet2genmuon1 = -1.0;
			Pt_genjet3 = 0;       Phi_genjet3 = 0;       Eta_genjet3 = 0; DeltaPhi_genjet3genmuon1 = -1.0;
			Pt_genjet4 = 0;       Phi_genjet4 = 0;       Eta_genjet4 = 0; DeltaPhi_genjet4genmuon1 = -1.0;
			Pt_genjet5 = 0;       Phi_genjet5 = 0;       Eta_genjet5 = 0; DeltaPhi_genjet5genmuon1 = -1.0;

			Pt_genjet1 = 0;       Phi_genjet1 = 0;       Eta_genjet1 = 0; DeltaPhi_genjet1genmuon1 = -1.0;
			Pt_genjet2 = 0;       Phi_genjet2 = 0;       Eta_genjet2 = 0; DeltaPhi_genjet2genmuon1 = -1.0;
			Pt_genjet3 = 0;       Phi_genjet3 = 0;       Eta_genjet3 = 0; DeltaPhi_genjet3genmuon1 = -1.0;
			Pt_genjet4 = 0;       Phi_genjet4 = 0;       Eta_genjet4 = 0; DeltaPhi_genjet4genmuon1 = -1.0;
			Pt_genjet5 = 0;       Phi_genjet5 = 0;       Eta_genjet5 = 0; DeltaPhi_genjet5genmuon1 = -1.0;

			Pt_genmuon1 = 0;      Phi_genmuon1 = 0;      Eta_genmuon1 = 0;
			Pt_genmuon1 = 0;      Phi_genmuon1 = 0;      Eta_genmuon1 = 0;

			GenJet30Count = 0.0;
			Pt_genmuonneutrino1 = 0;      Phi_genmuonneutrino1 = 0;      Eta_genmuonneutrino1 = 0;

			HT_genjets = 0.0;

			MT_genmuon1genMET = 0 ;  MT_genmuon1genneutrino = 0;
			MT_genmuon1genMET = 0;

			// Gen W/Z info, for recoil stuff
			for(unsigned int ip = 0; ip != GenParticlePdgId->size(); ++ip)
			{
				int pdgId = GenParticlePdgId->at(ip);
				if ( TMath::Abs(pdgId) == 23 )
				{
					GenZ.SetPtEtaPhiM(GenParticlePt->at(ip),GenParticleEta->at(ip),GenParticlePhi->at(ip),0.0);
					break;
				}
			}

			for(unsigned int ip = 0; ip != GenParticlePdgId->size(); ++ip)
			{
				int pdgId = GenParticlePdgId->at(ip);
				if ( TMath::Abs(pdgId) == 24 )
				{
					GenW.SetPtEtaPhiM(GenParticlePt->at(ip),GenParticleEta->at(ip),GenParticlePhi->at(ip),0.0);
					break;
				}
			}



			for(unsigned int ip = 0; ip != GenParticlePdgId->size(); ++ip)
			{
				int pdgId = GenParticlePdgId->at(ip);
				int status = GenParticleStatus->at(ip);

				// Store dressed muons for MadGraph
				if ( (!IsSherpa) &&  TMath::Abs(pdgId) == 713 ) // PDGID 713 is made up - for dressed muon
				{
					TLorentzVector thisgenmuon;
					thisgenmuon.SetPtEtaPhiM(GenParticlePt->at(ip),GenParticleEta->at(ip),GenParticlePhi->at(ip),0.0);

					bool KeepMuon=true;
					for(unsigned int igenmuon = 0; igenmuon != GenMuons.size(); ++igenmuon)
					{
						if ( (GenMuons[igenmuon].Pt() == thisgenmuon.Pt())&&(GenMuons[igenmuon].Eta() == thisgenmuon.Eta())&&(GenMuons[igenmuon].Phi() == thisgenmuon.Phi()) )
						{
							KeepMuon=false; // Check for duplicate muons
						}
					}
					if (KeepMuon==true) GenMuons.push_back(thisgenmuon);
				}

				// Store status 3 regular munos for Sherpa
				if ( (IsSherpa) &&  TMath::Abs(pdgId) == 13 && abs(status) == 3)
				{

					TLorentzVector thisgenmuon;
					thisgenmuon.SetPtEtaPhiM(GenParticlePt->at(ip),GenParticleEta->at(ip),GenParticlePhi->at(ip),0.0);

					bool KeepMuon=true;
					for(unsigned int igenmuon = 0; igenmuon != GenMuons.size(); ++igenmuon)
					{
						if ( (GenMuons[igenmuon].Pt() == thisgenmuon.Pt())&&(GenMuons[igenmuon].Eta() == thisgenmuon.Eta())&&(GenMuons[igenmuon].Phi() == thisgenmuon.Phi()) )
						{
							KeepMuon=false;// Check for duplicate muons
						}
					}
					if (KeepMuon==true) GenMuons.push_back(thisgenmuon);
				}

				// Store Gen Neutrino
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


			GenMuonCount= GenMuons.size();


			// Store Gen Jets passing PT30/Eta2p4
			for(unsigned int ijet = 0; ijet != GenJetPt->size(); ++ijet)
			{

				TLorentzVector(thisgenjet);
				thisgenjet.SetPtEtaPhiM(GenJetPt->at(ijet),GenJetEta->at(ijet),GenJetPhi->at(ijet),0.0);
				if (fabs(GenJetEta->at(ijet))>3.0) continue;

				bool KeepGenJet=true;
				for(unsigned int igmu = 0; igmu != GenMuons.size(); ++igmu)
				{
					if ((GenMuons[igmu]).DeltaR(thisgenjet) < 0.5)      KeepGenJet=false;
					break;		 // lead muon only
				}

				if (!KeepGenJet) continue;

				GenJets.push_back(thisgenjet);

				if ((fabs(thisgenjet.Eta())<2.6)&&( thisgenjet.Pt() > 15.0)) GenJetsLoose.push_back(thisgenjet);

				if (fabs(GenJetEta->at(ijet))>2.4) continue;
				if (thisgenjet.Pt()<30.0) continue;
				GenJetsBare.push_back(thisgenjet);
				GenJet30Count+= 1.0;
				HT_genjets += thisgenjet.Pt();
			}


			// Assign Muon Variables
			if (GenMuonCount>=1)    Pt_genmuon1  = GenMuons[0].Pt();
			if (GenMuonCount>=1)    Eta_genmuon1 = GenMuons[0].Eta();
			if (GenMuonCount>=1)    Phi_genmuon1 = GenMuons[0].Phi();

			// Assign Jet Variables
			if (GenJet30Count>=1) Pt_genjet1  =  GenJetsBare[0].Pt();
			if (GenJet30Count>=1) Eta_genjet1 =  GenJetsBare[0].Eta();
			if (GenJet30Count>=1) Phi_genjet1 =  GenJetsBare[0].Phi();

			if (GenJet30Count>=2) Pt_genjet2  =  GenJetsBare[1].Pt();
			if (GenJet30Count>=2) Eta_genjet2 =  GenJetsBare[1].Eta();
			if (GenJet30Count>=2) Phi_genjet2 =  GenJetsBare[1].Phi();

			if (GenJet30Count>=3) Pt_genjet3  =  GenJetsBare[2].Pt();
			if (GenJet30Count>=3) Eta_genjet3 =  GenJetsBare[2].Eta();
			if (GenJet30Count>=3) Phi_genjet3 =  GenJetsBare[2].Phi();

			if (GenJet30Count>=4) Pt_genjet4  =  GenJetsBare[3].Pt();
			if (GenJet30Count>=4) Eta_genjet4 =  GenJetsBare[3].Eta();
			if (GenJet30Count>=4) Phi_genjet4 =  GenJetsBare[3].Phi();

			if (GenJet30Count>=5) Pt_genjet5  =  GenJetsBare[4].Pt();
			if (GenJet30Count>=5) Eta_genjet5 =  GenJetsBare[4].Eta();
			if (GenJet30Count>=5) Phi_genjet5 =  GenJetsBare[4].Phi();

			if (GenMuonCount>=1)
			{
				if (GenJet30Count>=1) DeltaPhi_genjet1genmuon1 = fabs(GenJetsBare[0].DeltaPhi(GenMuons[0]));
				if (GenJet30Count>=2) DeltaPhi_genjet2genmuon1 = fabs(GenJetsBare[1].DeltaPhi(GenMuons[0]));
				if (GenJet30Count>=3) DeltaPhi_genjet3genmuon1 = fabs(GenJetsBare[2].DeltaPhi(GenMuons[0]));
				if (GenJet30Count>=4) DeltaPhi_genjet4genmuon1 = fabs(GenJetsBare[3].DeltaPhi(GenMuons[0]));
				if (GenJet30Count>=5) DeltaPhi_genjet5genmuon1 = fabs(GenJetsBare[4].DeltaPhi(GenMuons[0]));
			}

			// GenMet variables
			Pt_genMET = GenMETTrue->at(0);
			Phi_genMET = GenMETPhiTrue->at(0);
			MT_genmuon1genMET =  TMass(Pt_genmuon1,Pt_genMET, fabs(Phi_genmuon1 - Phi_genMET) );
			MT_genmuon1genMET =  TMass(Pt_genmuon1,Pt_genMET, fabs(Phi_genmuon1 - Phi_genMET) );

			// Neutrinos, not used in practice
			if (GenMuNeutrinos.size()>0)
			{
				MT_genmuon1genneutrino = TMass(Pt_genmuon1, GenMuNeutrinos[0].Pt() , fabs(Phi_genmuon1 - GenMuNeutrinos[0].Phi()) );
				Pt_genmuonneutrino1 = GenMuNeutrinos[0].Pt();
				Phi_genmuonneutrino1 = GenMuNeutrinos[0].Phi();
				Eta_genmuonneutrino1 = GenMuNeutrinos[0].Eta();
			}

			// Gen Met - Used in practice
			v_GenMet.SetPtEtaPhiM ( Pt_genMET, 0, Phi_genMET,0 );

		}

		//========================     Reco Level Calculations  ================================//

		// Reset Variables
		Pt_pfjet1 = 0;       Phi_pfjet1 = 0;       Eta_pfjet1 = 0;    DeltaPhi_pfjet1muon1 = -1.0;
		Pt_pfjet2 = 0;       Phi_pfjet2 = 0;       Eta_pfjet2 = 0;    DeltaPhi_pfjet2muon1 = -1.0;
		Pt_pfjet3 = 0;       Phi_pfjet3 = 0;       Eta_pfjet3 = 0;    DeltaPhi_pfjet3muon1 = -1.0;
		Pt_pfjet4 = 0;       Phi_pfjet4 = 0;       Eta_pfjet4 = 0;    DeltaPhi_pfjet4muon1 = -1.0;
		Pt_pfjet5 = 0;       Phi_pfjet5 = 0;       Eta_pfjet5 = 0;    DeltaPhi_pfjet5muon1 = -1.0;

		Pt_pfjet1_pt20 = 0;   Eta_pfjet1_eta2p5 = 99;
		Pt_pfjet2_pt20 = 0;   Eta_pfjet2_eta2p5 = 99;
		Pt_pfjet3_pt20 = 0;   Eta_pfjet3_eta2p5 = 99;
		Pt_pfjet4_pt20 = 0;   Eta_pfjet4_eta2p5 = 99;
		Pt_pfjet5_pt20 = 0;   Eta_pfjet5_eta2p5 = 99;


		DeltaPhi_pfjet1muon1_hasgenmatch = 0;
		DeltaPhi_pfjet2muon1_hasgenmatch = 0;
		DeltaPhi_pfjet3muon1_hasgenmatch = 0;
		DeltaPhi_pfjet4muon1_hasgenmatch = 0;
		DeltaPhi_pfjet5muon1_hasgenmatch = 0;

		Pt_pfjet1_pt20_hasgenmatch = 0;   Eta_pfjet1_eta2p5_hasgenmatch = 0;
		Pt_pfjet2_pt20_hasgenmatch = 0;   Eta_pfjet2_eta2p5_hasgenmatch = 0;
		Pt_pfjet3_pt20_hasgenmatch = 0;   Eta_pfjet3_eta2p5_hasgenmatch = 0;
		Pt_pfjet4_pt20_hasgenmatch = 0;   Eta_pfjet4_eta2p5_hasgenmatch = 0;
		Pt_pfjet5_pt20_hasgenmatch = 0;   Eta_pfjet5_eta2p5_hasgenmatch = 0;

		Pt_muon1 = 0;      Phi_muon1 = 0;      Eta_muon1 = 0;
		Pt_muon2 = 0;      Phi_muon2 = 0;      Eta_muon2 = 0;

		Pt_MET = 0;        Phi_MET = 0;
		MT_muon1MET = 0;
		Pt_MET1 = 0;        Phi_MET1 = 0;
		Pt_METR = 0;        Phi_METR = 0;

		MT_muon1MET1 = 0;
		MT_muon1METR = 0;

		Pt_METUnProp = 0;        Phi_METUnProp = 0;
		MT_muon1METUnProp = 0;
		Pt_MET1UnProp = 0;        Phi_MET1UnProp = 0;
		MT_muon1MET1UnProp = 0;
		M_muon1muon2 = 0.0;

		TLorentzVector  _v_Met;


		// Get MET
		_v_Met.SetPtEtaPhiM ( PFMET->at(0), 0, PFMETPhi->at(0),0 );

		// Some recoil fixes
		if ( true && IsW)
		{
			PFMET->at(0) = PFMET->at(0);
			PFMETPhi->at(0) = PFMETPhi->at(0);

			U1_W = -99.0;
			U2_W = -99.0;
			Pt_W = -99.0;
			TLorentzVector PW;
			TLorentzVector UW;

			if (isData) break;
			if (MuonCount<1) break;

			UW = -_v_Met - RecoMuons[0];
			PW = v_GenMet + RecoMuons[0];

			_v_Met =  Recoil_Corr(RecoMuons[0], UW,PW);

		}


		// Assign Muon Variables
		if (MuonCount>=1)   Pt_muon1  = RecoMuons[0].Pt();
		if (MuonCount>=1)   Eta_muon1 = RecoMuons[0].Eta();
		if (MuonCount>=1)   Phi_muon1 = RecoMuons[0].Phi();
		if (MuonCount>=2)   Pt_muon2  = RecoMuons[1].Pt();
		if (MuonCount>=2)   Eta_muon2 = RecoMuons[1].Eta();
		if (MuonCount>=2)   Phi_muon2 = RecoMuons[1].Phi();
		if (MuonCount>=2)   M_muon1muon2 =  (RecoMuons[0]+RecoMuons[1]).M();


		// Assign Jet Variables
		if (PFJet30Count>=1)  Pt_pfjet1  =    RecoJets[0].Pt();
		if (PFJet30Count>=1)  Eta_pfjet1 =    RecoJets[0].Eta();
		if (PFJet30Count>=1)  Phi_pfjet1 =    RecoJets[0].Phi();
		if (PFJet30Count>=1)  DeltaPhi_pfjet1muon1 =  fabs(RecoJets[0].DeltaPhi(RecoMuons[0]));
		if (PFJet30Count>=1)  DeltaPhi_pfjet1muon1_hasgenmatch =  HasMatchInCollection(RecoJets[0],GenJetsLoose);


		if (PFJet30Count>=2)  Pt_pfjet2  =    RecoJets[1].Pt();
		if (PFJet30Count>=2)  Eta_pfjet2 =    RecoJets[1].Eta();
		if (PFJet30Count>=2)  Phi_pfjet2 =    RecoJets[1].Phi();
		if (PFJet30Count>=2)  DeltaPhi_pfjet2muon1 =  fabs(RecoJets[1].DeltaPhi(RecoMuons[0]));
		if (PFJet30Count>=2)  DeltaPhi_pfjet2muon1_hasgenmatch =  HasMatchInCollection(RecoJets[1],GenJetsLoose);


		if (PFJet30Count>=3)  Pt_pfjet3  =    RecoJets[2].Pt();
		if (PFJet30Count>=3)  Eta_pfjet3 =    RecoJets[2].Eta();
		if (PFJet30Count>=3)  Phi_pfjet3 =    RecoJets[2].Phi();
		if (PFJet30Count>=3)  DeltaPhi_pfjet3muon1 =  fabs(RecoJets[2].DeltaPhi(RecoMuons[0]));
		if (PFJet30Count>=3)  DeltaPhi_pfjet3muon1_hasgenmatch =  HasMatchInCollection(RecoJets[2],GenJetsLoose);

		if (PFJet30Count>=4)  Pt_pfjet4  =    RecoJets[3].Pt();
		if (PFJet30Count>=4)  Eta_pfjet4 =    RecoJets[3].Eta();
		if (PFJet30Count>=4)  Phi_pfjet4 =    RecoJets[3].Phi();
		if (PFJet30Count>=4)  DeltaPhi_pfjet4muon1 =  fabs(RecoJets[3].DeltaPhi(RecoMuons[0]));
		if (PFJet30Count>=4)  DeltaPhi_pfjet4muon1_hasgenmatch =  HasMatchInCollection(RecoJets[3],GenJetsLoose);

		if (PFJet30Count>=5)  Pt_pfjet5  =    RecoJets[4].Pt();
		if (PFJet30Count>=5)  Eta_pfjet5 =    RecoJets[4].Eta();
		if (PFJet30Count>=5)  Phi_pfjet5 =    RecoJets[4].Phi();
		if (PFJet30Count>=5)  DeltaPhi_pfjet5muon1 =  fabs(RecoJets[4].DeltaPhi(RecoMuons[0]));
		if (PFJet30Count>=5)  DeltaPhi_pfjet5muon1_hasgenmatch =  HasMatchInCollection(RecoJets[4],GenJetsLoose);



		// Assign jet variables with underflows for unfolding



		// Add empty vectors to recojet vectors so code doesn't crash
		for(unsigned int ii=0; ii<6; ii++)
		{
			RecoJetsLoosePt.push_back(elorentz);
			RecoJetsLooseEta.push_back(elorentz);
		}



		// Set the Pt_pfjetX_pt20 to a value if all jets < X meet good pT>30 conditions (i.e. give underflow to only the Xth jet)
		Pt_pfjet1_pt20 = RecoJetsLoosePt[0].Pt(); 
		Pt_pfjet1_pt20_hasgenmatch = HasMatchInCollection(RecoJetsLoosePt[0],GenJetsLoose);
		if (RecoJetsLoosePt[0].Pt()>30)
		{
			Pt_pfjet2_pt20 = RecoJetsLoosePt[1].Pt();
			Pt_pfjet2_pt20_hasgenmatch = HasMatchInCollection(RecoJetsLoosePt[1],GenJetsLoose);

			if (RecoJetsLoosePt[1].Pt()>30)
			{
				Pt_pfjet3_pt20 = RecoJetsLoosePt[2].Pt();
				Pt_pfjet3_pt20_hasgenmatch = HasMatchInCollection(RecoJetsLoosePt[2],GenJetsLoose);

				if (RecoJetsLoosePt[2].Pt()>30)
				{
					Pt_pfjet4_pt20 = RecoJetsLoosePt[3].Pt();
					Pt_pfjet4_pt20_hasgenmatch = HasMatchInCollection(RecoJetsLoosePt[3],GenJetsLoose);

					if (RecoJetsLoosePt[3].Pt()>30)
					{
						Pt_pfjet5_pt20 = RecoJetsLoosePt[4].Pt();
						Pt_pfjet5_pt20_hasgenmatch = HasMatchInCollection(RecoJetsLoosePt[4],GenJetsLoose);

					}
				}
			}	
		}



		// Set the Eta_pfjetX_eta2p5 to a value if all jets < X meet good eta<2.4 conditions (i.e. give under/overflow to only the Xth jet)
		Eta_pfjet1_eta2p5 = RecoJetsLooseEta[0].Eta(); 
		Eta_pfjet1_eta2p5_hasgenmatch = HasMatchInCollection(RecoJetsLooseEta[0],GenJetsLoose);

		if ( fabs(RecoJetsLooseEta[0].Pt())>30.0)
		{
			Eta_pfjet2_eta2p5 = RecoJetsLooseEta[1].Eta();
			Eta_pfjet2_eta2p5_hasgenmatch = HasMatchInCollection(RecoJetsLooseEta[1],GenJetsLoose);

			if (fabs(RecoJetsLooseEta[1].Pt())>30.0)
			{
				Eta_pfjet3_eta2p5 = RecoJetsLooseEta[2].Eta();
				Eta_pfjet3_eta2p5_hasgenmatch = HasMatchInCollection(RecoJetsLooseEta[2],GenJetsLoose);

				if (fabs(RecoJetsLooseEta[2].Pt())>30.0)
				{
					Eta_pfjet4_eta2p5 = RecoJetsLooseEta[3].Eta();
					Eta_pfjet4_eta2p5_hasgenmatch = HasMatchInCollection(RecoJetsLooseEta[3],GenJetsLoose);

					if (fabs(RecoJetsLooseEta[3].Pt())>30.0)
					{
						Eta_pfjet5_eta2p5 = RecoJetsLooseEta[4].Eta();
						Eta_pfjet5_eta2p5_hasgenmatch = HasMatchInCollection(RecoJetsLooseEta[4],GenJetsLoose);
					}
				}
			}	
		}



		Pt_MET = PFMET->at(0);
		Phi_MET = PFMETPhi->at(0);

		Pt_MET1 = PFMETType1Cor->at(0);
		Phi_MET1 = PFMETPhiType1Cor->at(0);

		Pt_METR = _v_Met.Pt();
		Phi_METR = _v_Met.Phi();

		Pt_METUnProp = JetAdjustedMETUnProp.Pt();
		Phi_METUnProp = JetAdjustedMETUnProp.Phi();

		Pt_MET1UnProp = JetAdjustedMET1UnProp.Pt();
		Phi_MET1UnProp = JetAdjustedMET1UnProp.Phi();

		MT_muon1MET =  TMass(Pt_muon1,Pt_MET, fabs(Phi_muon1 - Phi_MET) );
		MT_muon1MET1 =  TMass(Pt_muon1,Pt_MET1, fabs(Phi_muon1 - Phi_MET1) );

		MT_muon1METR =  TMass(Pt_muon1,Pt_METR, fabs(Phi_muon1 - Phi_METR) );

		MT_muon1METUnProp =  TMass(Pt_muon1,Pt_METUnProp, fabs(Phi_muon1 - Phi_METUnProp) );
		MT_muon1MET1UnProp =  TMass(Pt_muon1,Pt_MET1UnProp, fabs(Phi_muon1 - Phi_MET1UnProp) );

		RelIso_muon1 = RecoMuonIso[0];
		RelIso_muon2 = RecoMuonIso[1];

		TLorentzVector  v_Met;
		v_Met.SetPtEtaPhiM ( Pt_MET, 0, Phi_MET,0 );
		// DeltaPhi_muon1MET = RecoMuons[0].DeltaPhi(v_Met);


		Pt_HEEPele1=0.0;
		if (HEEPEle25Count>=1) Pt_HEEPele1 = ElectronPt->at(v_idx_ele_good_final[0]);

		//========================     Set The Recoil Variables  ================================//

		U1_Z = -99.0;
		U2_Z = -99.0;
		U1_W = -99.0;
		U2_W = -99.0;

		Pt_W = -99.0;
		Pt_Z = -99.0;

		TLorentzVector UZ;
		TLorentzVector UW;

		TLorentzVector PZ;
		TLorentzVector PW;


		if (MuonCount>=2) UZ = -v_Met - RecoMuons[0] - RecoMuons[1];
		if (MuonCount>=1) UW = -v_Met - RecoMuons[0];
		if (MuonCount>=2) PZ = RecoMuons[0] + RecoMuons[1];

		if (!isData)
		{
			if (GenMuonCount>=1) PW = v_GenMet + GenMuons[0];
		}


		float UZx = UZ.Px();
		float UZy = UZ.Py();
		float UWx = UW.Px();
		float UWy = UW.Py();
		float PZx = PZ.Px();
		float PZy = PZ.Py();
		float PWx = PW.Px();
		float PWy = PW.Py();

		float UZr = sqrt(UZx*UZx + UZy*UZy);
		float UWr = sqrt(UWx*UWx + UWy*UWy);
		float PZr = sqrt(PZx*PZx + PZy*PZy);
		float PWr = sqrt(PWx*PWx + PWy*PWy);

		float UPZdphi = UZ.DeltaPhi(PZ);
		float UPWdphi = UW.DeltaPhi(PW);

		U1_Z = UZr*cos(UPZdphi);
		U2_Z = UZr*sin(UPZdphi);

		U1_W = UWr*cos(UPWdphi);
		U2_W = UWr*sin(UPWdphi);

		Pt_Z = PZr;
		Pt_W = PWr;

		//========================     Skimming and such  ================================//

		bool skipevent = true;
		bool hasmuon = false;
		bool hasjet = false;

		if (Pt_muon1>25) hasmuon = true;
		if (Pt_genmuon1 > 24) hasmuon = true;
		if (Pt_pfjet1>30) hasjet = true;
		if (RecoJetsLooseEta[0].Pt()>20) hasjet = true;
		if (RecoJetsLoosePt[0].Pt()>20) hasjet = true;
		if (Pt_genjet1>30) hasjet = true;

		if (hasjet && hasmuon) skipevent = false;
		if (skipevent) continue;

		tree->Fill();

	}

	tree->Write();
	file1->Close();
}
