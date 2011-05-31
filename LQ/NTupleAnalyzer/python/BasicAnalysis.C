//#################################################################################
//###  Script to Optimize Cuts for Letoquarks by Significance and Produce        ###
//###  script to Optimize using the Limit Setting (CLA) tool.                   ###
//###  The _template version of this script is empty, and is manipulated by     ###
//###  a python file to mass-produce Optimization scripts for different LQ       ###
//###  masses. These scripts are disposable and are best used with the python   ###
//###  production tools (SimpleAnalysisfromInputFile.py)                        ###                                                      
//###                                                                           ###
//###  Darin Baumgartel - Northeastern University - darinb@CERN.ch  Aug-04-2010 ###
//###                                                                           ###
//#################################################################################

//list_tracer_000

int use_LQToCMu_MuNuJJFilter_M_150 =0;

int use_LQToCMu_MuNuJJFilter_M_175 =0;

int use_LQToCMu_MuNuJJFilter_M_200 =0;

int use_LQToCMu_MuNuJJFilter_M_225 =0;

int use_LQToCMu_MuNuJJFilter_M_250 =0;

int use_LQToCMu_MuNuJJFilter_M_280 =0;

int use_LQToCMu_MuNuJJFilter_M_300 =0;

int use_LQToCMu_MuNuJJFilter_M_320 =0;

int use_LQToCMu_MuNuJJFilter_M_340 =0;

int use_LQToCMu_MuNuJJFilter_M_400 =0;

int use_LQToCMu_MuNuJJFilter_M_450 =0;

int use_LQToCMu_MuNuJJFilter_M_500 =0;

int use_LQToCMu_MuNuJJFilter_M_600 =0;

int use_ALLBKG =1;
//list_tracer_001


				//#######################################################################################
				//                         LQToCMu_MuNuJJFilter_M_150                         
				//#######################################################################################

if (use_LQToCMu_MuNuJJFilter_M_150 ==1){
 SigOrBG = 1;

		//---------------------------------------------------------------------------------------//
		//----------------   Declare background trees/Temp Histograms   -------------------------//
		//---------------------------------------------------------------------------------------//

		TTree* Var__orig__LQToCMu_MuNuJJFilter_M_150 = (TTree*)f__LQToCMu_MuNuJJFilter_M_150->Get("PhysicalVariables");
		TH1D* h__LQToCMu_MuNuJJFilter_M_150= new TH1D("h__LQToCMu_MuNuJJFilter_M_150","title",100,0.0,10000.0);


		Var__orig__LQToCMu_MuNuJJFilter_M_150->Project("h__LQToCMu_MuNuJJFilter_M_150","weight*(2.71)","weight*(2.71)*Events_Orig/Events_AfterLJ");
		if (SigOrBG==1) const Double_t S_orig =h__LQToCMu_MuNuJJFilter_M_150->Integral();
		if (SigOrBG==0) const Double_t B_orig =h__LQToCMu_MuNuJJFilter_M_150->Integral();
		std::cout<<"@@@ Evaluating For Signal Type LQToCMu_MuNuJJFilter_M_150"<<std::endl;

		string precut = "1.0*(Pt_muon1>25)*(Pt_pfjet1>25)*(Pt_pfjet2>25)*(-1.0*deltaPhi_muon1pfMET>-3.0)*(precut_HLT>0.5)*(ST_pf_munu>140)*(MT_muon1pfMET>80)*(MET_pf>50)";
		TString precutstring = precut;

		TFile f__temp__LQToCMu_MuNuJJFilter_M_150("temp__LQToCMu_MuNuJJFilter_M_150.root","recreate");
		TTree* Var__LQToCMu_MuNuJJFilter_M_150 = Var__orig__LQToCMu_MuNuJJFilter_M_150 ->CopyTree(precutstring);

		std::cout<<"Precuts Complete. "<<Var__orig__LQToCMu_MuNuJJFilter_M_150->GetEntries()<<"  MC Events Reduced to "<<Var__LQToCMu_MuNuJJFilter_M_150->GetEntries()<<std::endl;


		//---------------------------------------------------------------------------------------//
		//-----------------   Loop over Cut vals, set Cut String, Evaluate   --------------------//
		//---------------------------------------------------------------------------------------//


		TH1D* h__Op__LQToCMu_MuNuJJFilter_M_150= new TH1D("h__Op__LQToCMu_MuNuJJFilter_M_150","title",100,0.0,10000.0);


	for (int_ST_pf_munu=0; int_ST_pf_munu < ST_pf_munu_points; int_ST_pf_munu++){
		for (int_MT_muon1pfMET=0; int_MT_muon1pfMET < MT_muon1pfMET_points; int_MT_muon1pfMET++){
			for (int_MET_pf=0; int_MET_pf < MET_pf_points; int_MET_pf++){

			std::ostringstream strs;
			strs << ST_pf_munu_Cut[int_ST_pf_munu];
			std::string str0 = strs.str();


			std::ostringstream strs;
			strs << MT_muon1pfMET_Cut[int_MT_muon1pfMET];
			std::string str1 = strs.str();


			std::ostringstream strs;
			strs << MET_pf_Cut[int_MET_pf];
			std::string str2 = strs.str();


			string cut = "weight*(2.71)*(ST_pf_munu>" + str0 + ")*(MT_muon1pfMET>" + str1 + ")*(MET_pf>" + str2 + ")";

			TString cutstring = cut;

			Var__LQToCMu_MuNuJJFilter_M_150->Project("h__Op__LQToCMu_MuNuJJFilter_M_150","ST_calo",cutstring);

			if (SigOrBG==1) S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_150->Integral();
			if (SigOrBG==0) B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_150->Integral();
			}
		}
	}}
		std::cout<<"Optimization Cuts Complete"<<std::endl;


				//#######################################################################################
				//                         LQToCMu_MuNuJJFilter_M_175                         
				//#######################################################################################

if (use_LQToCMu_MuNuJJFilter_M_175 ==1){
 SigOrBG = 1;

		//---------------------------------------------------------------------------------------//
		//----------------   Declare background trees/Temp Histograms   -------------------------//
		//---------------------------------------------------------------------------------------//

		TTree* Var__orig__LQToCMu_MuNuJJFilter_M_175 = (TTree*)f__LQToCMu_MuNuJJFilter_M_175->Get("PhysicalVariables");
		TH1D* h__LQToCMu_MuNuJJFilter_M_175= new TH1D("h__LQToCMu_MuNuJJFilter_M_175","title",100,0.0,10000.0);


		Var__orig__LQToCMu_MuNuJJFilter_M_175->Project("h__LQToCMu_MuNuJJFilter_M_175","weight*(2.71)","weight*(2.71)*Events_Orig/Events_AfterLJ");
		if (SigOrBG==1) const Double_t S_orig =h__LQToCMu_MuNuJJFilter_M_175->Integral();
		if (SigOrBG==0) const Double_t B_orig =h__LQToCMu_MuNuJJFilter_M_175->Integral();
		std::cout<<"@@@ Evaluating For Signal Type LQToCMu_MuNuJJFilter_M_175"<<std::endl;

		string precut = "1.0*(Pt_muon1>25)*(Pt_pfjet1>25)*(Pt_pfjet2>25)*(-1.0*deltaPhi_muon1pfMET>-3.0)*(precut_HLT>0.5)*(ST_pf_munu>140)*(MT_muon1pfMET>80)*(MET_pf>50)";
		TString precutstring = precut;

		TFile f__temp__LQToCMu_MuNuJJFilter_M_175("temp__LQToCMu_MuNuJJFilter_M_175.root","recreate");
		TTree* Var__LQToCMu_MuNuJJFilter_M_175 = Var__orig__LQToCMu_MuNuJJFilter_M_175 ->CopyTree(precutstring);

		std::cout<<"Precuts Complete. "<<Var__orig__LQToCMu_MuNuJJFilter_M_175->GetEntries()<<"  MC Events Reduced to "<<Var__LQToCMu_MuNuJJFilter_M_175->GetEntries()<<std::endl;


		//---------------------------------------------------------------------------------------//
		//-----------------   Loop over Cut vals, set Cut String, Evaluate   --------------------//
		//---------------------------------------------------------------------------------------//


		TH1D* h__Op__LQToCMu_MuNuJJFilter_M_175= new TH1D("h__Op__LQToCMu_MuNuJJFilter_M_175","title",100,0.0,10000.0);


	for (int_ST_pf_munu=0; int_ST_pf_munu < ST_pf_munu_points; int_ST_pf_munu++){
		for (int_MT_muon1pfMET=0; int_MT_muon1pfMET < MT_muon1pfMET_points; int_MT_muon1pfMET++){
			for (int_MET_pf=0; int_MET_pf < MET_pf_points; int_MET_pf++){

			std::ostringstream strs;
			strs << ST_pf_munu_Cut[int_ST_pf_munu];
			std::string str0 = strs.str();


			std::ostringstream strs;
			strs << MT_muon1pfMET_Cut[int_MT_muon1pfMET];
			std::string str1 = strs.str();


			std::ostringstream strs;
			strs << MET_pf_Cut[int_MET_pf];
			std::string str2 = strs.str();


			string cut = "weight*(2.71)*(ST_pf_munu>" + str0 + ")*(MT_muon1pfMET>" + str1 + ")*(MET_pf>" + str2 + ")";

			TString cutstring = cut;

			Var__LQToCMu_MuNuJJFilter_M_175->Project("h__Op__LQToCMu_MuNuJJFilter_M_175","ST_calo",cutstring);

			if (SigOrBG==1) S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_175->Integral();
			if (SigOrBG==0) B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_175->Integral();
			}
		}
	}}
		std::cout<<"Optimization Cuts Complete"<<std::endl;


				//#######################################################################################
				//                         LQToCMu_MuNuJJFilter_M_200                         
				//#######################################################################################

if (use_LQToCMu_MuNuJJFilter_M_200 ==1){
 SigOrBG = 1;

		//---------------------------------------------------------------------------------------//
		//----------------   Declare background trees/Temp Histograms   -------------------------//
		//---------------------------------------------------------------------------------------//

		TTree* Var__orig__LQToCMu_MuNuJJFilter_M_200 = (TTree*)f__LQToCMu_MuNuJJFilter_M_200->Get("PhysicalVariables");
		TH1D* h__LQToCMu_MuNuJJFilter_M_200= new TH1D("h__LQToCMu_MuNuJJFilter_M_200","title",100,0.0,10000.0);


		Var__orig__LQToCMu_MuNuJJFilter_M_200->Project("h__LQToCMu_MuNuJJFilter_M_200","weight*(2.71)","weight*(2.71)*Events_Orig/Events_AfterLJ");
		if (SigOrBG==1) const Double_t S_orig =h__LQToCMu_MuNuJJFilter_M_200->Integral();
		if (SigOrBG==0) const Double_t B_orig =h__LQToCMu_MuNuJJFilter_M_200->Integral();
		std::cout<<"@@@ Evaluating For Signal Type LQToCMu_MuNuJJFilter_M_200"<<std::endl;

		string precut = "1.0*(Pt_muon1>25)*(Pt_pfjet1>25)*(Pt_pfjet2>25)*(-1.0*deltaPhi_muon1pfMET>-3.0)*(precut_HLT>0.5)*(ST_pf_munu>140)*(MT_muon1pfMET>80)*(MET_pf>50)";
		TString precutstring = precut;

		TFile f__temp__LQToCMu_MuNuJJFilter_M_200("temp__LQToCMu_MuNuJJFilter_M_200.root","recreate");
		TTree* Var__LQToCMu_MuNuJJFilter_M_200 = Var__orig__LQToCMu_MuNuJJFilter_M_200 ->CopyTree(precutstring);

		std::cout<<"Precuts Complete. "<<Var__orig__LQToCMu_MuNuJJFilter_M_200->GetEntries()<<"  MC Events Reduced to "<<Var__LQToCMu_MuNuJJFilter_M_200->GetEntries()<<std::endl;


		//---------------------------------------------------------------------------------------//
		//-----------------   Loop over Cut vals, set Cut String, Evaluate   --------------------//
		//---------------------------------------------------------------------------------------//


		TH1D* h__Op__LQToCMu_MuNuJJFilter_M_200= new TH1D("h__Op__LQToCMu_MuNuJJFilter_M_200","title",100,0.0,10000.0);


	for (int_ST_pf_munu=0; int_ST_pf_munu < ST_pf_munu_points; int_ST_pf_munu++){
		for (int_MT_muon1pfMET=0; int_MT_muon1pfMET < MT_muon1pfMET_points; int_MT_muon1pfMET++){
			for (int_MET_pf=0; int_MET_pf < MET_pf_points; int_MET_pf++){

			std::ostringstream strs;
			strs << ST_pf_munu_Cut[int_ST_pf_munu];
			std::string str0 = strs.str();


			std::ostringstream strs;
			strs << MT_muon1pfMET_Cut[int_MT_muon1pfMET];
			std::string str1 = strs.str();


			std::ostringstream strs;
			strs << MET_pf_Cut[int_MET_pf];
			std::string str2 = strs.str();


			string cut = "weight*(2.71)*(ST_pf_munu>" + str0 + ")*(MT_muon1pfMET>" + str1 + ")*(MET_pf>" + str2 + ")";

			TString cutstring = cut;

			Var__LQToCMu_MuNuJJFilter_M_200->Project("h__Op__LQToCMu_MuNuJJFilter_M_200","ST_calo",cutstring);

			if (SigOrBG==1) S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_200->Integral();
			if (SigOrBG==0) B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_200->Integral();
			}
		}
	}}
		std::cout<<"Optimization Cuts Complete"<<std::endl;


				//#######################################################################################
				//                         LQToCMu_MuNuJJFilter_M_225                         
				//#######################################################################################

if (use_LQToCMu_MuNuJJFilter_M_225 ==1){
 SigOrBG = 1;

		//---------------------------------------------------------------------------------------//
		//----------------   Declare background trees/Temp Histograms   -------------------------//
		//---------------------------------------------------------------------------------------//

		TTree* Var__orig__LQToCMu_MuNuJJFilter_M_225 = (TTree*)f__LQToCMu_MuNuJJFilter_M_225->Get("PhysicalVariables");
		TH1D* h__LQToCMu_MuNuJJFilter_M_225= new TH1D("h__LQToCMu_MuNuJJFilter_M_225","title",100,0.0,10000.0);


		Var__orig__LQToCMu_MuNuJJFilter_M_225->Project("h__LQToCMu_MuNuJJFilter_M_225","weight*(2.71)","weight*(2.71)*Events_Orig/Events_AfterLJ");
		if (SigOrBG==1) const Double_t S_orig =h__LQToCMu_MuNuJJFilter_M_225->Integral();
		if (SigOrBG==0) const Double_t B_orig =h__LQToCMu_MuNuJJFilter_M_225->Integral();
		std::cout<<"@@@ Evaluating For Signal Type LQToCMu_MuNuJJFilter_M_225"<<std::endl;

		string precut = "1.0*(Pt_muon1>25)*(Pt_pfjet1>25)*(Pt_pfjet2>25)*(-1.0*deltaPhi_muon1pfMET>-3.0)*(precut_HLT>0.5)*(ST_pf_munu>140)*(MT_muon1pfMET>80)*(MET_pf>50)";
		TString precutstring = precut;

		TFile f__temp__LQToCMu_MuNuJJFilter_M_225("temp__LQToCMu_MuNuJJFilter_M_225.root","recreate");
		TTree* Var__LQToCMu_MuNuJJFilter_M_225 = Var__orig__LQToCMu_MuNuJJFilter_M_225 ->CopyTree(precutstring);

		std::cout<<"Precuts Complete. "<<Var__orig__LQToCMu_MuNuJJFilter_M_225->GetEntries()<<"  MC Events Reduced to "<<Var__LQToCMu_MuNuJJFilter_M_225->GetEntries()<<std::endl;


		//---------------------------------------------------------------------------------------//
		//-----------------   Loop over Cut vals, set Cut String, Evaluate   --------------------//
		//---------------------------------------------------------------------------------------//


		TH1D* h__Op__LQToCMu_MuNuJJFilter_M_225= new TH1D("h__Op__LQToCMu_MuNuJJFilter_M_225","title",100,0.0,10000.0);


	for (int_ST_pf_munu=0; int_ST_pf_munu < ST_pf_munu_points; int_ST_pf_munu++){
		for (int_MT_muon1pfMET=0; int_MT_muon1pfMET < MT_muon1pfMET_points; int_MT_muon1pfMET++){
			for (int_MET_pf=0; int_MET_pf < MET_pf_points; int_MET_pf++){

			std::ostringstream strs;
			strs << ST_pf_munu_Cut[int_ST_pf_munu];
			std::string str0 = strs.str();


			std::ostringstream strs;
			strs << MT_muon1pfMET_Cut[int_MT_muon1pfMET];
			std::string str1 = strs.str();


			std::ostringstream strs;
			strs << MET_pf_Cut[int_MET_pf];
			std::string str2 = strs.str();


			string cut = "weight*(2.71)*(ST_pf_munu>" + str0 + ")*(MT_muon1pfMET>" + str1 + ")*(MET_pf>" + str2 + ")";

			TString cutstring = cut;

			Var__LQToCMu_MuNuJJFilter_M_225->Project("h__Op__LQToCMu_MuNuJJFilter_M_225","ST_calo",cutstring);

			if (SigOrBG==1) S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_225->Integral();
			if (SigOrBG==0) B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_225->Integral();
			}
		}
	}}
		std::cout<<"Optimization Cuts Complete"<<std::endl;


				//#######################################################################################
				//                         LQToCMu_MuNuJJFilter_M_250                         
				//#######################################################################################

if (use_LQToCMu_MuNuJJFilter_M_250 ==1){
 SigOrBG = 1;

		//---------------------------------------------------------------------------------------//
		//----------------   Declare background trees/Temp Histograms   -------------------------//
		//---------------------------------------------------------------------------------------//

		TTree* Var__orig__LQToCMu_MuNuJJFilter_M_250 = (TTree*)f__LQToCMu_MuNuJJFilter_M_250->Get("PhysicalVariables");
		TH1D* h__LQToCMu_MuNuJJFilter_M_250= new TH1D("h__LQToCMu_MuNuJJFilter_M_250","title",100,0.0,10000.0);


		Var__orig__LQToCMu_MuNuJJFilter_M_250->Project("h__LQToCMu_MuNuJJFilter_M_250","weight*(2.71)","weight*(2.71)*Events_Orig/Events_AfterLJ");
		if (SigOrBG==1) const Double_t S_orig =h__LQToCMu_MuNuJJFilter_M_250->Integral();
		if (SigOrBG==0) const Double_t B_orig =h__LQToCMu_MuNuJJFilter_M_250->Integral();
		std::cout<<"@@@ Evaluating For Signal Type LQToCMu_MuNuJJFilter_M_250"<<std::endl;

		string precut = "1.0*(Pt_muon1>25)*(Pt_pfjet1>25)*(Pt_pfjet2>25)*(-1.0*deltaPhi_muon1pfMET>-3.0)*(precut_HLT>0.5)*(ST_pf_munu>140)*(MT_muon1pfMET>80)*(MET_pf>50)";
		TString precutstring = precut;

		TFile f__temp__LQToCMu_MuNuJJFilter_M_250("temp__LQToCMu_MuNuJJFilter_M_250.root","recreate");
		TTree* Var__LQToCMu_MuNuJJFilter_M_250 = Var__orig__LQToCMu_MuNuJJFilter_M_250 ->CopyTree(precutstring);

		std::cout<<"Precuts Complete. "<<Var__orig__LQToCMu_MuNuJJFilter_M_250->GetEntries()<<"  MC Events Reduced to "<<Var__LQToCMu_MuNuJJFilter_M_250->GetEntries()<<std::endl;


		//---------------------------------------------------------------------------------------//
		//-----------------   Loop over Cut vals, set Cut String, Evaluate   --------------------//
		//---------------------------------------------------------------------------------------//


		TH1D* h__Op__LQToCMu_MuNuJJFilter_M_250= new TH1D("h__Op__LQToCMu_MuNuJJFilter_M_250","title",100,0.0,10000.0);


	for (int_ST_pf_munu=0; int_ST_pf_munu < ST_pf_munu_points; int_ST_pf_munu++){
		for (int_MT_muon1pfMET=0; int_MT_muon1pfMET < MT_muon1pfMET_points; int_MT_muon1pfMET++){
			for (int_MET_pf=0; int_MET_pf < MET_pf_points; int_MET_pf++){

			std::ostringstream strs;
			strs << ST_pf_munu_Cut[int_ST_pf_munu];
			std::string str0 = strs.str();


			std::ostringstream strs;
			strs << MT_muon1pfMET_Cut[int_MT_muon1pfMET];
			std::string str1 = strs.str();


			std::ostringstream strs;
			strs << MET_pf_Cut[int_MET_pf];
			std::string str2 = strs.str();


			string cut = "weight*(2.71)*(ST_pf_munu>" + str0 + ")*(MT_muon1pfMET>" + str1 + ")*(MET_pf>" + str2 + ")";

			TString cutstring = cut;

			Var__LQToCMu_MuNuJJFilter_M_250->Project("h__Op__LQToCMu_MuNuJJFilter_M_250","ST_calo",cutstring);

			if (SigOrBG==1) S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_250->Integral();
			if (SigOrBG==0) B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_250->Integral();
			}
		}
	}}
		std::cout<<"Optimization Cuts Complete"<<std::endl;


				//#######################################################################################
				//                         LQToCMu_MuNuJJFilter_M_280                         
				//#######################################################################################

if (use_LQToCMu_MuNuJJFilter_M_280 ==1){
 SigOrBG = 1;

		//---------------------------------------------------------------------------------------//
		//----------------   Declare background trees/Temp Histograms   -------------------------//
		//---------------------------------------------------------------------------------------//

		TTree* Var__orig__LQToCMu_MuNuJJFilter_M_280 = (TTree*)f__LQToCMu_MuNuJJFilter_M_280->Get("PhysicalVariables");
		TH1D* h__LQToCMu_MuNuJJFilter_M_280= new TH1D("h__LQToCMu_MuNuJJFilter_M_280","title",100,0.0,10000.0);


		Var__orig__LQToCMu_MuNuJJFilter_M_280->Project("h__LQToCMu_MuNuJJFilter_M_280","weight*(2.71)","weight*(2.71)*Events_Orig/Events_AfterLJ");
		if (SigOrBG==1) const Double_t S_orig =h__LQToCMu_MuNuJJFilter_M_280->Integral();
		if (SigOrBG==0) const Double_t B_orig =h__LQToCMu_MuNuJJFilter_M_280->Integral();
		std::cout<<"@@@ Evaluating For Signal Type LQToCMu_MuNuJJFilter_M_280"<<std::endl;

		string precut = "1.0*(Pt_muon1>25)*(Pt_pfjet1>25)*(Pt_pfjet2>25)*(-1.0*deltaPhi_muon1pfMET>-3.0)*(precut_HLT>0.5)*(ST_pf_munu>140)*(MT_muon1pfMET>80)*(MET_pf>50)";
		TString precutstring = precut;

		TFile f__temp__LQToCMu_MuNuJJFilter_M_280("temp__LQToCMu_MuNuJJFilter_M_280.root","recreate");
		TTree* Var__LQToCMu_MuNuJJFilter_M_280 = Var__orig__LQToCMu_MuNuJJFilter_M_280 ->CopyTree(precutstring);

		std::cout<<"Precuts Complete. "<<Var__orig__LQToCMu_MuNuJJFilter_M_280->GetEntries()<<"  MC Events Reduced to "<<Var__LQToCMu_MuNuJJFilter_M_280->GetEntries()<<std::endl;


		//---------------------------------------------------------------------------------------//
		//-----------------   Loop over Cut vals, set Cut String, Evaluate   --------------------//
		//---------------------------------------------------------------------------------------//


		TH1D* h__Op__LQToCMu_MuNuJJFilter_M_280= new TH1D("h__Op__LQToCMu_MuNuJJFilter_M_280","title",100,0.0,10000.0);


	for (int_ST_pf_munu=0; int_ST_pf_munu < ST_pf_munu_points; int_ST_pf_munu++){
		for (int_MT_muon1pfMET=0; int_MT_muon1pfMET < MT_muon1pfMET_points; int_MT_muon1pfMET++){
			for (int_MET_pf=0; int_MET_pf < MET_pf_points; int_MET_pf++){

			std::ostringstream strs;
			strs << ST_pf_munu_Cut[int_ST_pf_munu];
			std::string str0 = strs.str();


			std::ostringstream strs;
			strs << MT_muon1pfMET_Cut[int_MT_muon1pfMET];
			std::string str1 = strs.str();


			std::ostringstream strs;
			strs << MET_pf_Cut[int_MET_pf];
			std::string str2 = strs.str();


			string cut = "weight*(2.71)*(ST_pf_munu>" + str0 + ")*(MT_muon1pfMET>" + str1 + ")*(MET_pf>" + str2 + ")";

			TString cutstring = cut;

			Var__LQToCMu_MuNuJJFilter_M_280->Project("h__Op__LQToCMu_MuNuJJFilter_M_280","ST_calo",cutstring);

			if (SigOrBG==1) S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_280->Integral();
			if (SigOrBG==0) B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_280->Integral();
			}
		}
	}}
		std::cout<<"Optimization Cuts Complete"<<std::endl;


				//#######################################################################################
				//                         LQToCMu_MuNuJJFilter_M_300                         
				//#######################################################################################

if (use_LQToCMu_MuNuJJFilter_M_300 ==1){
 SigOrBG = 1;

		//---------------------------------------------------------------------------------------//
		//----------------   Declare background trees/Temp Histograms   -------------------------//
		//---------------------------------------------------------------------------------------//

		TTree* Var__orig__LQToCMu_MuNuJJFilter_M_300 = (TTree*)f__LQToCMu_MuNuJJFilter_M_300->Get("PhysicalVariables");
		TH1D* h__LQToCMu_MuNuJJFilter_M_300= new TH1D("h__LQToCMu_MuNuJJFilter_M_300","title",100,0.0,10000.0);


		Var__orig__LQToCMu_MuNuJJFilter_M_300->Project("h__LQToCMu_MuNuJJFilter_M_300","weight*(2.71)","weight*(2.71)*Events_Orig/Events_AfterLJ");
		if (SigOrBG==1) const Double_t S_orig =h__LQToCMu_MuNuJJFilter_M_300->Integral();
		if (SigOrBG==0) const Double_t B_orig =h__LQToCMu_MuNuJJFilter_M_300->Integral();
		std::cout<<"@@@ Evaluating For Signal Type LQToCMu_MuNuJJFilter_M_300"<<std::endl;

		string precut = "1.0*(Pt_muon1>25)*(Pt_pfjet1>25)*(Pt_pfjet2>25)*(-1.0*deltaPhi_muon1pfMET>-3.0)*(precut_HLT>0.5)*(ST_pf_munu>140)*(MT_muon1pfMET>80)*(MET_pf>50)";
		TString precutstring = precut;

		TFile f__temp__LQToCMu_MuNuJJFilter_M_300("temp__LQToCMu_MuNuJJFilter_M_300.root","recreate");
		TTree* Var__LQToCMu_MuNuJJFilter_M_300 = Var__orig__LQToCMu_MuNuJJFilter_M_300 ->CopyTree(precutstring);

		std::cout<<"Precuts Complete. "<<Var__orig__LQToCMu_MuNuJJFilter_M_300->GetEntries()<<"  MC Events Reduced to "<<Var__LQToCMu_MuNuJJFilter_M_300->GetEntries()<<std::endl;


		//---------------------------------------------------------------------------------------//
		//-----------------   Loop over Cut vals, set Cut String, Evaluate   --------------------//
		//---------------------------------------------------------------------------------------//


		TH1D* h__Op__LQToCMu_MuNuJJFilter_M_300= new TH1D("h__Op__LQToCMu_MuNuJJFilter_M_300","title",100,0.0,10000.0);


	for (int_ST_pf_munu=0; int_ST_pf_munu < ST_pf_munu_points; int_ST_pf_munu++){
		for (int_MT_muon1pfMET=0; int_MT_muon1pfMET < MT_muon1pfMET_points; int_MT_muon1pfMET++){
			for (int_MET_pf=0; int_MET_pf < MET_pf_points; int_MET_pf++){

			std::ostringstream strs;
			strs << ST_pf_munu_Cut[int_ST_pf_munu];
			std::string str0 = strs.str();


			std::ostringstream strs;
			strs << MT_muon1pfMET_Cut[int_MT_muon1pfMET];
			std::string str1 = strs.str();


			std::ostringstream strs;
			strs << MET_pf_Cut[int_MET_pf];
			std::string str2 = strs.str();


			string cut = "weight*(2.71)*(ST_pf_munu>" + str0 + ")*(MT_muon1pfMET>" + str1 + ")*(MET_pf>" + str2 + ")";

			TString cutstring = cut;

			Var__LQToCMu_MuNuJJFilter_M_300->Project("h__Op__LQToCMu_MuNuJJFilter_M_300","ST_calo",cutstring);

			if (SigOrBG==1) S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_300->Integral();
			if (SigOrBG==0) B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_300->Integral();
			}
		}
	}}
		std::cout<<"Optimization Cuts Complete"<<std::endl;


				//#######################################################################################
				//                         LQToCMu_MuNuJJFilter_M_320                         
				//#######################################################################################

if (use_LQToCMu_MuNuJJFilter_M_320 ==1){
 SigOrBG = 1;

		//---------------------------------------------------------------------------------------//
		//----------------   Declare background trees/Temp Histograms   -------------------------//
		//---------------------------------------------------------------------------------------//

		TTree* Var__orig__LQToCMu_MuNuJJFilter_M_320 = (TTree*)f__LQToCMu_MuNuJJFilter_M_320->Get("PhysicalVariables");
		TH1D* h__LQToCMu_MuNuJJFilter_M_320= new TH1D("h__LQToCMu_MuNuJJFilter_M_320","title",100,0.0,10000.0);


		Var__orig__LQToCMu_MuNuJJFilter_M_320->Project("h__LQToCMu_MuNuJJFilter_M_320","weight*(2.71)","weight*(2.71)*Events_Orig/Events_AfterLJ");
		if (SigOrBG==1) const Double_t S_orig =h__LQToCMu_MuNuJJFilter_M_320->Integral();
		if (SigOrBG==0) const Double_t B_orig =h__LQToCMu_MuNuJJFilter_M_320->Integral();
		std::cout<<"@@@ Evaluating For Signal Type LQToCMu_MuNuJJFilter_M_320"<<std::endl;

		string precut = "1.0*(Pt_muon1>25)*(Pt_pfjet1>25)*(Pt_pfjet2>25)*(-1.0*deltaPhi_muon1pfMET>-3.0)*(precut_HLT>0.5)*(ST_pf_munu>140)*(MT_muon1pfMET>80)*(MET_pf>50)";
		TString precutstring = precut;

		TFile f__temp__LQToCMu_MuNuJJFilter_M_320("temp__LQToCMu_MuNuJJFilter_M_320.root","recreate");
		TTree* Var__LQToCMu_MuNuJJFilter_M_320 = Var__orig__LQToCMu_MuNuJJFilter_M_320 ->CopyTree(precutstring);

		std::cout<<"Precuts Complete. "<<Var__orig__LQToCMu_MuNuJJFilter_M_320->GetEntries()<<"  MC Events Reduced to "<<Var__LQToCMu_MuNuJJFilter_M_320->GetEntries()<<std::endl;


		//---------------------------------------------------------------------------------------//
		//-----------------   Loop over Cut vals, set Cut String, Evaluate   --------------------//
		//---------------------------------------------------------------------------------------//


		TH1D* h__Op__LQToCMu_MuNuJJFilter_M_320= new TH1D("h__Op__LQToCMu_MuNuJJFilter_M_320","title",100,0.0,10000.0);


	for (int_ST_pf_munu=0; int_ST_pf_munu < ST_pf_munu_points; int_ST_pf_munu++){
		for (int_MT_muon1pfMET=0; int_MT_muon1pfMET < MT_muon1pfMET_points; int_MT_muon1pfMET++){
			for (int_MET_pf=0; int_MET_pf < MET_pf_points; int_MET_pf++){

			std::ostringstream strs;
			strs << ST_pf_munu_Cut[int_ST_pf_munu];
			std::string str0 = strs.str();


			std::ostringstream strs;
			strs << MT_muon1pfMET_Cut[int_MT_muon1pfMET];
			std::string str1 = strs.str();


			std::ostringstream strs;
			strs << MET_pf_Cut[int_MET_pf];
			std::string str2 = strs.str();


			string cut = "weight*(2.71)*(ST_pf_munu>" + str0 + ")*(MT_muon1pfMET>" + str1 + ")*(MET_pf>" + str2 + ")";

			TString cutstring = cut;

			Var__LQToCMu_MuNuJJFilter_M_320->Project("h__Op__LQToCMu_MuNuJJFilter_M_320","ST_calo",cutstring);

			if (SigOrBG==1) S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_320->Integral();
			if (SigOrBG==0) B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_320->Integral();
			}
		}
	}}
		std::cout<<"Optimization Cuts Complete"<<std::endl;


				//#######################################################################################
				//                         LQToCMu_MuNuJJFilter_M_340                         
				//#######################################################################################

if (use_LQToCMu_MuNuJJFilter_M_340 ==1){
 SigOrBG = 1;

		//---------------------------------------------------------------------------------------//
		//----------------   Declare background trees/Temp Histograms   -------------------------//
		//---------------------------------------------------------------------------------------//

		TTree* Var__orig__LQToCMu_MuNuJJFilter_M_340 = (TTree*)f__LQToCMu_MuNuJJFilter_M_340->Get("PhysicalVariables");
		TH1D* h__LQToCMu_MuNuJJFilter_M_340= new TH1D("h__LQToCMu_MuNuJJFilter_M_340","title",100,0.0,10000.0);


		Var__orig__LQToCMu_MuNuJJFilter_M_340->Project("h__LQToCMu_MuNuJJFilter_M_340","weight*(2.71)","weight*(2.71)*Events_Orig/Events_AfterLJ");
		if (SigOrBG==1) const Double_t S_orig =h__LQToCMu_MuNuJJFilter_M_340->Integral();
		if (SigOrBG==0) const Double_t B_orig =h__LQToCMu_MuNuJJFilter_M_340->Integral();
		std::cout<<"@@@ Evaluating For Signal Type LQToCMu_MuNuJJFilter_M_340"<<std::endl;

		string precut = "1.0*(Pt_muon1>25)*(Pt_pfjet1>25)*(Pt_pfjet2>25)*(-1.0*deltaPhi_muon1pfMET>-3.0)*(precut_HLT>0.5)*(ST_pf_munu>140)*(MT_muon1pfMET>80)*(MET_pf>50)";
		TString precutstring = precut;

		TFile f__temp__LQToCMu_MuNuJJFilter_M_340("temp__LQToCMu_MuNuJJFilter_M_340.root","recreate");
		TTree* Var__LQToCMu_MuNuJJFilter_M_340 = Var__orig__LQToCMu_MuNuJJFilter_M_340 ->CopyTree(precutstring);

		std::cout<<"Precuts Complete. "<<Var__orig__LQToCMu_MuNuJJFilter_M_340->GetEntries()<<"  MC Events Reduced to "<<Var__LQToCMu_MuNuJJFilter_M_340->GetEntries()<<std::endl;


		//---------------------------------------------------------------------------------------//
		//-----------------   Loop over Cut vals, set Cut String, Evaluate   --------------------//
		//---------------------------------------------------------------------------------------//


		TH1D* h__Op__LQToCMu_MuNuJJFilter_M_340= new TH1D("h__Op__LQToCMu_MuNuJJFilter_M_340","title",100,0.0,10000.0);


	for (int_ST_pf_munu=0; int_ST_pf_munu < ST_pf_munu_points; int_ST_pf_munu++){
		for (int_MT_muon1pfMET=0; int_MT_muon1pfMET < MT_muon1pfMET_points; int_MT_muon1pfMET++){
			for (int_MET_pf=0; int_MET_pf < MET_pf_points; int_MET_pf++){

			std::ostringstream strs;
			strs << ST_pf_munu_Cut[int_ST_pf_munu];
			std::string str0 = strs.str();


			std::ostringstream strs;
			strs << MT_muon1pfMET_Cut[int_MT_muon1pfMET];
			std::string str1 = strs.str();


			std::ostringstream strs;
			strs << MET_pf_Cut[int_MET_pf];
			std::string str2 = strs.str();


			string cut = "weight*(2.71)*(ST_pf_munu>" + str0 + ")*(MT_muon1pfMET>" + str1 + ")*(MET_pf>" + str2 + ")";

			TString cutstring = cut;

			Var__LQToCMu_MuNuJJFilter_M_340->Project("h__Op__LQToCMu_MuNuJJFilter_M_340","ST_calo",cutstring);

			if (SigOrBG==1) S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_340->Integral();
			if (SigOrBG==0) B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_340->Integral();
			}
		}
	}}
		std::cout<<"Optimization Cuts Complete"<<std::endl;


				//#######################################################################################
				//                         LQToCMu_MuNuJJFilter_M_400                         
				//#######################################################################################

if (use_LQToCMu_MuNuJJFilter_M_400 ==1){
 SigOrBG = 1;

		//---------------------------------------------------------------------------------------//
		//----------------   Declare background trees/Temp Histograms   -------------------------//
		//---------------------------------------------------------------------------------------//

		TTree* Var__orig__LQToCMu_MuNuJJFilter_M_400 = (TTree*)f__LQToCMu_MuNuJJFilter_M_400->Get("PhysicalVariables");
		TH1D* h__LQToCMu_MuNuJJFilter_M_400= new TH1D("h__LQToCMu_MuNuJJFilter_M_400","title",100,0.0,10000.0);


		Var__orig__LQToCMu_MuNuJJFilter_M_400->Project("h__LQToCMu_MuNuJJFilter_M_400","weight*(2.71)","weight*(2.71)*Events_Orig/Events_AfterLJ");
		if (SigOrBG==1) const Double_t S_orig =h__LQToCMu_MuNuJJFilter_M_400->Integral();
		if (SigOrBG==0) const Double_t B_orig =h__LQToCMu_MuNuJJFilter_M_400->Integral();
		std::cout<<"@@@ Evaluating For Signal Type LQToCMu_MuNuJJFilter_M_400"<<std::endl;

		string precut = "1.0*(Pt_muon1>25)*(Pt_pfjet1>25)*(Pt_pfjet2>25)*(-1.0*deltaPhi_muon1pfMET>-3.0)*(precut_HLT>0.5)*(ST_pf_munu>140)*(MT_muon1pfMET>80)*(MET_pf>50)";
		TString precutstring = precut;

		TFile f__temp__LQToCMu_MuNuJJFilter_M_400("temp__LQToCMu_MuNuJJFilter_M_400.root","recreate");
		TTree* Var__LQToCMu_MuNuJJFilter_M_400 = Var__orig__LQToCMu_MuNuJJFilter_M_400 ->CopyTree(precutstring);

		std::cout<<"Precuts Complete. "<<Var__orig__LQToCMu_MuNuJJFilter_M_400->GetEntries()<<"  MC Events Reduced to "<<Var__LQToCMu_MuNuJJFilter_M_400->GetEntries()<<std::endl;


		//---------------------------------------------------------------------------------------//
		//-----------------   Loop over Cut vals, set Cut String, Evaluate   --------------------//
		//---------------------------------------------------------------------------------------//


		TH1D* h__Op__LQToCMu_MuNuJJFilter_M_400= new TH1D("h__Op__LQToCMu_MuNuJJFilter_M_400","title",100,0.0,10000.0);


	for (int_ST_pf_munu=0; int_ST_pf_munu < ST_pf_munu_points; int_ST_pf_munu++){
		for (int_MT_muon1pfMET=0; int_MT_muon1pfMET < MT_muon1pfMET_points; int_MT_muon1pfMET++){
			for (int_MET_pf=0; int_MET_pf < MET_pf_points; int_MET_pf++){

			std::ostringstream strs;
			strs << ST_pf_munu_Cut[int_ST_pf_munu];
			std::string str0 = strs.str();


			std::ostringstream strs;
			strs << MT_muon1pfMET_Cut[int_MT_muon1pfMET];
			std::string str1 = strs.str();


			std::ostringstream strs;
			strs << MET_pf_Cut[int_MET_pf];
			std::string str2 = strs.str();


			string cut = "weight*(2.71)*(ST_pf_munu>" + str0 + ")*(MT_muon1pfMET>" + str1 + ")*(MET_pf>" + str2 + ")";

			TString cutstring = cut;

			Var__LQToCMu_MuNuJJFilter_M_400->Project("h__Op__LQToCMu_MuNuJJFilter_M_400","ST_calo",cutstring);

			if (SigOrBG==1) S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_400->Integral();
			if (SigOrBG==0) B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_400->Integral();
			}
		}
	}}
		std::cout<<"Optimization Cuts Complete"<<std::endl;


				//#######################################################################################
				//                         LQToCMu_MuNuJJFilter_M_450                         
				//#######################################################################################

if (use_LQToCMu_MuNuJJFilter_M_450 ==1){
 SigOrBG = 1;

		//---------------------------------------------------------------------------------------//
		//----------------   Declare background trees/Temp Histograms   -------------------------//
		//---------------------------------------------------------------------------------------//

		TTree* Var__orig__LQToCMu_MuNuJJFilter_M_450 = (TTree*)f__LQToCMu_MuNuJJFilter_M_450->Get("PhysicalVariables");
		TH1D* h__LQToCMu_MuNuJJFilter_M_450= new TH1D("h__LQToCMu_MuNuJJFilter_M_450","title",100,0.0,10000.0);


		Var__orig__LQToCMu_MuNuJJFilter_M_450->Project("h__LQToCMu_MuNuJJFilter_M_450","weight*(2.71)","weight*(2.71)*Events_Orig/Events_AfterLJ");
		if (SigOrBG==1) const Double_t S_orig =h__LQToCMu_MuNuJJFilter_M_450->Integral();
		if (SigOrBG==0) const Double_t B_orig =h__LQToCMu_MuNuJJFilter_M_450->Integral();
		std::cout<<"@@@ Evaluating For Signal Type LQToCMu_MuNuJJFilter_M_450"<<std::endl;

		string precut = "1.0*(Pt_muon1>25)*(Pt_pfjet1>25)*(Pt_pfjet2>25)*(-1.0*deltaPhi_muon1pfMET>-3.0)*(precut_HLT>0.5)*(ST_pf_munu>140)*(MT_muon1pfMET>80)*(MET_pf>50)";
		TString precutstring = precut;

		TFile f__temp__LQToCMu_MuNuJJFilter_M_450("temp__LQToCMu_MuNuJJFilter_M_450.root","recreate");
		TTree* Var__LQToCMu_MuNuJJFilter_M_450 = Var__orig__LQToCMu_MuNuJJFilter_M_450 ->CopyTree(precutstring);

		std::cout<<"Precuts Complete. "<<Var__orig__LQToCMu_MuNuJJFilter_M_450->GetEntries()<<"  MC Events Reduced to "<<Var__LQToCMu_MuNuJJFilter_M_450->GetEntries()<<std::endl;


		//---------------------------------------------------------------------------------------//
		//-----------------   Loop over Cut vals, set Cut String, Evaluate   --------------------//
		//---------------------------------------------------------------------------------------//


		TH1D* h__Op__LQToCMu_MuNuJJFilter_M_450= new TH1D("h__Op__LQToCMu_MuNuJJFilter_M_450","title",100,0.0,10000.0);


	for (int_ST_pf_munu=0; int_ST_pf_munu < ST_pf_munu_points; int_ST_pf_munu++){
		for (int_MT_muon1pfMET=0; int_MT_muon1pfMET < MT_muon1pfMET_points; int_MT_muon1pfMET++){
			for (int_MET_pf=0; int_MET_pf < MET_pf_points; int_MET_pf++){

			std::ostringstream strs;
			strs << ST_pf_munu_Cut[int_ST_pf_munu];
			std::string str0 = strs.str();


			std::ostringstream strs;
			strs << MT_muon1pfMET_Cut[int_MT_muon1pfMET];
			std::string str1 = strs.str();


			std::ostringstream strs;
			strs << MET_pf_Cut[int_MET_pf];
			std::string str2 = strs.str();


			string cut = "weight*(2.71)*(ST_pf_munu>" + str0 + ")*(MT_muon1pfMET>" + str1 + ")*(MET_pf>" + str2 + ")";

			TString cutstring = cut;

			Var__LQToCMu_MuNuJJFilter_M_450->Project("h__Op__LQToCMu_MuNuJJFilter_M_450","ST_calo",cutstring);

			if (SigOrBG==1) S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_450->Integral();
			if (SigOrBG==0) B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_450->Integral();
			}
		}
	}}
		std::cout<<"Optimization Cuts Complete"<<std::endl;


				//#######################################################################################
				//                         LQToCMu_MuNuJJFilter_M_500                         
				//#######################################################################################

if (use_LQToCMu_MuNuJJFilter_M_500 ==1){
 SigOrBG = 1;

		//---------------------------------------------------------------------------------------//
		//----------------   Declare background trees/Temp Histograms   -------------------------//
		//---------------------------------------------------------------------------------------//

		TTree* Var__orig__LQToCMu_MuNuJJFilter_M_500 = (TTree*)f__LQToCMu_MuNuJJFilter_M_500->Get("PhysicalVariables");
		TH1D* h__LQToCMu_MuNuJJFilter_M_500= new TH1D("h__LQToCMu_MuNuJJFilter_M_500","title",100,0.0,10000.0);


		Var__orig__LQToCMu_MuNuJJFilter_M_500->Project("h__LQToCMu_MuNuJJFilter_M_500","weight*(2.71)","weight*(2.71)*Events_Orig/Events_AfterLJ");
		if (SigOrBG==1) const Double_t S_orig =h__LQToCMu_MuNuJJFilter_M_500->Integral();
		if (SigOrBG==0) const Double_t B_orig =h__LQToCMu_MuNuJJFilter_M_500->Integral();
		std::cout<<"@@@ Evaluating For Signal Type LQToCMu_MuNuJJFilter_M_500"<<std::endl;

		string precut = "1.0*(Pt_muon1>25)*(Pt_pfjet1>25)*(Pt_pfjet2>25)*(-1.0*deltaPhi_muon1pfMET>-3.0)*(precut_HLT>0.5)*(ST_pf_munu>140)*(MT_muon1pfMET>80)*(MET_pf>50)";
		TString precutstring = precut;

		TFile f__temp__LQToCMu_MuNuJJFilter_M_500("temp__LQToCMu_MuNuJJFilter_M_500.root","recreate");
		TTree* Var__LQToCMu_MuNuJJFilter_M_500 = Var__orig__LQToCMu_MuNuJJFilter_M_500 ->CopyTree(precutstring);

		std::cout<<"Precuts Complete. "<<Var__orig__LQToCMu_MuNuJJFilter_M_500->GetEntries()<<"  MC Events Reduced to "<<Var__LQToCMu_MuNuJJFilter_M_500->GetEntries()<<std::endl;


		//---------------------------------------------------------------------------------------//
		//-----------------   Loop over Cut vals, set Cut String, Evaluate   --------------------//
		//---------------------------------------------------------------------------------------//


		TH1D* h__Op__LQToCMu_MuNuJJFilter_M_500= new TH1D("h__Op__LQToCMu_MuNuJJFilter_M_500","title",100,0.0,10000.0);


	for (int_ST_pf_munu=0; int_ST_pf_munu < ST_pf_munu_points; int_ST_pf_munu++){
		for (int_MT_muon1pfMET=0; int_MT_muon1pfMET < MT_muon1pfMET_points; int_MT_muon1pfMET++){
			for (int_MET_pf=0; int_MET_pf < MET_pf_points; int_MET_pf++){

			std::ostringstream strs;
			strs << ST_pf_munu_Cut[int_ST_pf_munu];
			std::string str0 = strs.str();


			std::ostringstream strs;
			strs << MT_muon1pfMET_Cut[int_MT_muon1pfMET];
			std::string str1 = strs.str();


			std::ostringstream strs;
			strs << MET_pf_Cut[int_MET_pf];
			std::string str2 = strs.str();


			string cut = "weight*(2.71)*(ST_pf_munu>" + str0 + ")*(MT_muon1pfMET>" + str1 + ")*(MET_pf>" + str2 + ")";

			TString cutstring = cut;

			Var__LQToCMu_MuNuJJFilter_M_500->Project("h__Op__LQToCMu_MuNuJJFilter_M_500","ST_calo",cutstring);

			if (SigOrBG==1) S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_500->Integral();
			if (SigOrBG==0) B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_500->Integral();
			}
		}
	}}
		std::cout<<"Optimization Cuts Complete"<<std::endl;


				//#######################################################################################
				//                         LQToCMu_MuNuJJFilter_M_600                         
				//#######################################################################################

if (use_LQToCMu_MuNuJJFilter_M_600 ==1){
 SigOrBG = 1;

		//---------------------------------------------------------------------------------------//
		//----------------   Declare background trees/Temp Histograms   -------------------------//
		//---------------------------------------------------------------------------------------//

		TTree* Var__orig__LQToCMu_MuNuJJFilter_M_600 = (TTree*)f__LQToCMu_MuNuJJFilter_M_600->Get("PhysicalVariables");
		TH1D* h__LQToCMu_MuNuJJFilter_M_600= new TH1D("h__LQToCMu_MuNuJJFilter_M_600","title",100,0.0,10000.0);


		Var__orig__LQToCMu_MuNuJJFilter_M_600->Project("h__LQToCMu_MuNuJJFilter_M_600","weight*(2.71)","weight*(2.71)*Events_Orig/Events_AfterLJ");
		if (SigOrBG==1) const Double_t S_orig =h__LQToCMu_MuNuJJFilter_M_600->Integral();
		if (SigOrBG==0) const Double_t B_orig =h__LQToCMu_MuNuJJFilter_M_600->Integral();
		std::cout<<"@@@ Evaluating For Signal Type LQToCMu_MuNuJJFilter_M_600"<<std::endl;

		string precut = "1.0*(Pt_muon1>25)*(Pt_pfjet1>25)*(Pt_pfjet2>25)*(-1.0*deltaPhi_muon1pfMET>-3.0)*(precut_HLT>0.5)*(ST_pf_munu>140)*(MT_muon1pfMET>80)*(MET_pf>50)";
		TString precutstring = precut;

		TFile f__temp__LQToCMu_MuNuJJFilter_M_600("temp__LQToCMu_MuNuJJFilter_M_600.root","recreate");
		TTree* Var__LQToCMu_MuNuJJFilter_M_600 = Var__orig__LQToCMu_MuNuJJFilter_M_600 ->CopyTree(precutstring);

		std::cout<<"Precuts Complete. "<<Var__orig__LQToCMu_MuNuJJFilter_M_600->GetEntries()<<"  MC Events Reduced to "<<Var__LQToCMu_MuNuJJFilter_M_600->GetEntries()<<std::endl;


		//---------------------------------------------------------------------------------------//
		//-----------------   Loop over Cut vals, set Cut String, Evaluate   --------------------//
		//---------------------------------------------------------------------------------------//


		TH1D* h__Op__LQToCMu_MuNuJJFilter_M_600= new TH1D("h__Op__LQToCMu_MuNuJJFilter_M_600","title",100,0.0,10000.0);


	for (int_ST_pf_munu=0; int_ST_pf_munu < ST_pf_munu_points; int_ST_pf_munu++){
		for (int_MT_muon1pfMET=0; int_MT_muon1pfMET < MT_muon1pfMET_points; int_MT_muon1pfMET++){
			for (int_MET_pf=0; int_MET_pf < MET_pf_points; int_MET_pf++){

			std::ostringstream strs;
			strs << ST_pf_munu_Cut[int_ST_pf_munu];
			std::string str0 = strs.str();


			std::ostringstream strs;
			strs << MT_muon1pfMET_Cut[int_MT_muon1pfMET];
			std::string str1 = strs.str();


			std::ostringstream strs;
			strs << MET_pf_Cut[int_MET_pf];
			std::string str2 = strs.str();


			string cut = "weight*(2.71)*(ST_pf_munu>" + str0 + ")*(MT_muon1pfMET>" + str1 + ")*(MET_pf>" + str2 + ")";

			TString cutstring = cut;

			Var__LQToCMu_MuNuJJFilter_M_600->Project("h__Op__LQToCMu_MuNuJJFilter_M_600","ST_calo",cutstring);

			if (SigOrBG==1) S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_600->Integral();
			if (SigOrBG==0) B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__LQToCMu_MuNuJJFilter_M_600->Integral();
			}
		}
	}}
		std::cout<<"Optimization Cuts Complete"<<std::endl;


				//#######################################################################################
				//                         ALLBKG                         
				//#######################################################################################

if (use_ALLBKG ==1){
 SigOrBG = 0;

		//---------------------------------------------------------------------------------------//
		//----------------   Declare background trees/Temp Histograms   -------------------------//
		//---------------------------------------------------------------------------------------//

		TTree* Var__orig__ALLBKG = (TTree*)f__ALLBKG->Get("PhysicalVariables");
		TH1D* h__ALLBKG= new TH1D("h__ALLBKG","title",100,0.0,10000.0);


		Var__orig__ALLBKG->Project("h__ALLBKG","weight*(2.71)","weight*(2.71)*Events_Orig/Events_AfterLJ");
		if (SigOrBG==1) const Double_t S_orig =h__ALLBKG->Integral();
		if (SigOrBG==0) const Double_t B_orig =h__ALLBKG->Integral();
		std::cout<<"@@@ Evaluating For Background Type ALLBKG"<<std::endl;

		string precut = "1.0*(Pt_muon1>25)*(Pt_pfjet1>25)*(Pt_pfjet2>25)*(-1.0*deltaPhi_muon1pfMET>-3.0)*(precut_HLT>0.5)*(ST_pf_munu>140)*(MT_muon1pfMET>80)*(MET_pf>50)";
		TString precutstring = precut;

		TFile f__temp__ALLBKG("temp__ALLBKG.root","recreate");
		TTree* Var__ALLBKG = Var__orig__ALLBKG ->CopyTree(precutstring);

		std::cout<<"Precuts Complete. "<<Var__orig__ALLBKG->GetEntries()<<"  MC Events Reduced to "<<Var__ALLBKG->GetEntries()<<std::endl;


		//---------------------------------------------------------------------------------------//
		//-----------------   Loop over Cut vals, set Cut String, Evaluate   --------------------//
		//---------------------------------------------------------------------------------------//


		TH1D* h__Op__ALLBKG= new TH1D("h__Op__ALLBKG","title",100,0.0,10000.0);


	for (int_ST_pf_munu=0; int_ST_pf_munu < ST_pf_munu_points; int_ST_pf_munu++){
		for (int_MT_muon1pfMET=0; int_MT_muon1pfMET < MT_muon1pfMET_points; int_MT_muon1pfMET++){
			for (int_MET_pf=0; int_MET_pf < MET_pf_points; int_MET_pf++){

			std::ostringstream strs;
			strs << ST_pf_munu_Cut[int_ST_pf_munu];
			std::string str0 = strs.str();


			std::ostringstream strs;
			strs << MT_muon1pfMET_Cut[int_MT_muon1pfMET];
			std::string str1 = strs.str();


			std::ostringstream strs;
			strs << MET_pf_Cut[int_MET_pf];
			std::string str2 = strs.str();


			string cut = "weight*(2.71)*(ST_pf_munu>" + str0 + ")*(MT_muon1pfMET>" + str1 + ")*(MET_pf>" + str2 + ")";

			TString cutstring = cut;

			Var__ALLBKG->Project("h__Op__ALLBKG","ST_calo",cutstring);

			if (SigOrBG==1) S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__ALLBKG->Integral();
			if (SigOrBG==0) B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=h__Op__ALLBKG->Integral();
			}
		}
	}}
		std::cout<<"Optimization Cuts Complete"<<std::endl;
//list_tracer_002

 int ideal_int_ST_pf_munu=0.0;
 int ideal_int_MT_muon1pfMET=0.0;
 int ideal_int_MET_pf=0.0;
 float Signif_max =0.0;
 float Signif[ST_pf_munu_points][MT_muon1pfMET_points][MET_pf_points];

std::cout<<"\n\nDetermining optimal cut values for the discriminating variables ...\n\n"<<std::endl;

	for (int_ST_pf_munu=0; int_ST_pf_munu < ST_pf_munu_points; int_ST_pf_munu++){

		for (int_MT_muon1pfMET=0; int_MT_muon1pfMET < MT_muon1pfMET_points; int_MT_muon1pfMET++){

			for (int_MET_pf=0; int_MET_pf < MET_pf_points; int_MET_pf++){

		Signif[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]=1.0*S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]*pow(1.0*(S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]+B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]),-.5);

			if (Signif[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]>Signif_max) {
				Signif_max=Signif[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf];

				 ideal_int_ST_pf_munu=int_ST_pf_munu;
				 ideal_int_MT_muon1pfMET=int_MT_muon1pfMET;
				 ideal_int_MET_pf=int_MET_pf;
						}
					}
				}
	}



std::cout<<"Significance maximization cuts results as follows:"<<std::endl;
std::cout<<"    "<<std::endl;
std::cout<<"@@@ Best ST_pf_munu Cut:  ST_pf_munu   > "<<ST_pf_munu_Cut[ideal_int_ST_pf_munu]<<std::endl;
std::cout<<"    "<<std::endl;
std::cout<<"@@@ Best MT_muon1pfMET Cut:  MT_muon1pfMET   > "<<MT_muon1pfMET_Cut[ideal_int_MT_muon1pfMET]<<std::endl;
std::cout<<"    "<<std::endl;
std::cout<<"@@@ Best MET_pf Cut:  MET_pf   > "<<MET_pf_Cut[ideal_int_MET_pf]<<std::endl;
std::cout<<"    "<<std::endl;
std::cout<<"@@@ Significance at Optimizal Cut Levels:   S = "<<Signif_max<<std::endl;

std::cout<<"    "<<std::endl;
std::cout<<"    "<<std::endl;
if (use_LQToCMu_MuNuJJFilter_M_150==1){
	std::cout<<"Analysis Complete for LQToCMu_MuNuJJFilter_M_150"<<std::endl;
	std::ofstream file("CLAEvaluation_LQToCMu_MuNuJJFilter_M_150.C");
	std::cout.rdbuf(file.rdbuf());
	}

if (use_LQToCMu_MuNuJJFilter_M_175==1){
	std::cout<<"Analysis Complete for LQToCMu_MuNuJJFilter_M_175"<<std::endl;
	std::ofstream file("CLAEvaluation_LQToCMu_MuNuJJFilter_M_175.C");
	std::cout.rdbuf(file.rdbuf());
	}

if (use_LQToCMu_MuNuJJFilter_M_200==1){
	std::cout<<"Analysis Complete for LQToCMu_MuNuJJFilter_M_200"<<std::endl;
	std::ofstream file("CLAEvaluation_LQToCMu_MuNuJJFilter_M_200.C");
	std::cout.rdbuf(file.rdbuf());
	}

if (use_LQToCMu_MuNuJJFilter_M_225==1){
	std::cout<<"Analysis Complete for LQToCMu_MuNuJJFilter_M_225"<<std::endl;
	std::ofstream file("CLAEvaluation_LQToCMu_MuNuJJFilter_M_225.C");
	std::cout.rdbuf(file.rdbuf());
	}

if (use_LQToCMu_MuNuJJFilter_M_250==1){
	std::cout<<"Analysis Complete for LQToCMu_MuNuJJFilter_M_250"<<std::endl;
	std::ofstream file("CLAEvaluation_LQToCMu_MuNuJJFilter_M_250.C");
	std::cout.rdbuf(file.rdbuf());
	}

if (use_LQToCMu_MuNuJJFilter_M_280==1){
	std::cout<<"Analysis Complete for LQToCMu_MuNuJJFilter_M_280"<<std::endl;
	std::ofstream file("CLAEvaluation_LQToCMu_MuNuJJFilter_M_280.C");
	std::cout.rdbuf(file.rdbuf());
	}

if (use_LQToCMu_MuNuJJFilter_M_300==1){
	std::cout<<"Analysis Complete for LQToCMu_MuNuJJFilter_M_300"<<std::endl;
	std::ofstream file("CLAEvaluation_LQToCMu_MuNuJJFilter_M_300.C");
	std::cout.rdbuf(file.rdbuf());
	}

if (use_LQToCMu_MuNuJJFilter_M_320==1){
	std::cout<<"Analysis Complete for LQToCMu_MuNuJJFilter_M_320"<<std::endl;
	std::ofstream file("CLAEvaluation_LQToCMu_MuNuJJFilter_M_320.C");
	std::cout.rdbuf(file.rdbuf());
	}

if (use_LQToCMu_MuNuJJFilter_M_340==1){
	std::cout<<"Analysis Complete for LQToCMu_MuNuJJFilter_M_340"<<std::endl;
	std::ofstream file("CLAEvaluation_LQToCMu_MuNuJJFilter_M_340.C");
	std::cout.rdbuf(file.rdbuf());
	}

if (use_LQToCMu_MuNuJJFilter_M_400==1){
	std::cout<<"Analysis Complete for LQToCMu_MuNuJJFilter_M_400"<<std::endl;
	std::ofstream file("CLAEvaluation_LQToCMu_MuNuJJFilter_M_400.C");
	std::cout.rdbuf(file.rdbuf());
	}

if (use_LQToCMu_MuNuJJFilter_M_450==1){
	std::cout<<"Analysis Complete for LQToCMu_MuNuJJFilter_M_450"<<std::endl;
	std::ofstream file("CLAEvaluation_LQToCMu_MuNuJJFilter_M_450.C");
	std::cout.rdbuf(file.rdbuf());
	}

if (use_LQToCMu_MuNuJJFilter_M_500==1){
	std::cout<<"Analysis Complete for LQToCMu_MuNuJJFilter_M_500"<<std::endl;
	std::ofstream file("CLAEvaluation_LQToCMu_MuNuJJFilter_M_500.C");
	std::cout.rdbuf(file.rdbuf());
	}

if (use_LQToCMu_MuNuJJFilter_M_600==1){
	std::cout<<"Analysis Complete for LQToCMu_MuNuJJFilter_M_600"<<std::endl;
	std::ofstream file("CLAEvaluation_LQToCMu_MuNuJJFilter_M_600.C");
	std::cout.rdbuf(file.rdbuf());
	}


std::cout<<"#include \"CLA.C\""<<std::endl;
std::cout<<"void MakeData()"<<std::endl;
std::cout<<"{"<<std::endl;
std::cout<<"float ST_pf_munu_CutValue["<<ST_pf_munu_points<<"]["<<MT_muon1pfMET_points<<"]["<<MET_pf_points<<"];"<<std::endl;
std::cout<<"float MT_muon1pfMET_CutValue["<<ST_pf_munu_points<<"]["<<MT_muon1pfMET_points<<"]["<<MET_pf_points<<"];"<<std::endl;
std::cout<<"float MET_pf_CutValue["<<ST_pf_munu_points<<"]["<<MT_muon1pfMET_points<<"]["<<MET_pf_points<<"];"<<std::endl;
std::cout<<"float val_sys["<<ST_pf_munu_points<<"]["<<MT_muon1pfMET_points<<"]["<<MET_pf_points<<"];"<<std::endl;
std::cout<<"int index0=0;"<<std::endl;
	for (int_ST_pf_munu=0; int_ST_pf_munu < ST_pf_munu_points; int_ST_pf_munu++){

		for (int_MT_muon1pfMET=0; int_MT_muon1pfMET < MT_muon1pfMET_points; int_MT_muon1pfMET++){

			for (int_MET_pf=0; int_MET_pf < MET_pf_points; int_MET_pf++){

			std::cout<<"index0=index0+1;"<<std::endl;
			std::cout<<"ST_pf_munu_CutValue"<<"["<<int_ST_pf_munu<<"]"<<"["<<int_MT_muon1pfMET<<"]"<<"["<<int_MET_pf<<"]"<<"="<<ST_pf_munu_Cut[int_ST_pf_munu]<<";"<<std::endl;
			std::cout<<"MT_muon1pfMET_CutValue"<<"["<<int_ST_pf_munu<<"]"<<"["<<int_MT_muon1pfMET<<"]"<<"["<<int_MET_pf<<"]"<<"="<<MT_muon1pfMET_Cut[int_MT_muon1pfMET]<<";"<<std::endl;
			std::cout<<"MET_pf_CutValue"<<"["<<int_ST_pf_munu<<"]"<<"["<<int_MT_muon1pfMET<<"]"<<"["<<int_MET_pf<<"]"<<"="<<MET_pf_Cut[int_MET_pf]<<";"<<std::endl;
			std::cout<<"val_sys"<<"["<<int_ST_pf_munu<<"]"<<"["<<int_MT_muon1pfMET<<"]"<<"["<<int_MET_pf<<"]"<<" = CLA(2.71,0.29809999999999998, "<<(1.0*S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf])/(1.0*S_orig)<<","<< (0.0*S[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf])/(1.0*S_orig)<<","<<B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]<<","<<B[int_ST_pf_munu][int_MT_muon1pfMET][int_MET_pf]*0.0<<");"<<std::endl;
			std::cout<<"std::cout<<\" ****************************************************************** \"<<std::endl;"<<std::endl;
			std::cout<<"std::cout<<\"CLA Calculation    \"<<index0<<\"   of   \"<<"<<ST_pf_munu_points*MT_muon1pfMET_points*MET_pf_points*1.0<<"<<\"   Completed\"<<std::endl;"<<std::endl;
			std::cout<<"std::cout<<\" ****************************************************************** \"<<std::endl;"<<std::endl;
						}
					}
				}

std::cout<<"float xsys =99999999;"<<std::endl;
std::cout<<"float ST_pf_munu_syscut = 0.0;"<<std::endl;
std::cout<<"int jj_ST_pf_munu=0;"<<std::endl;
std::cout<<"float MT_muon1pfMET_syscut = 0.0;"<<std::endl;
std::cout<<"int jj_MT_muon1pfMET=0;"<<std::endl;
std::cout<<"float MET_pf_syscut = 0.0;"<<std::endl;
std::cout<<"int jj_MET_pf=0;"<<std::endl;
std::cout<<"	 for (jj_ST_pf_munu=0; jj_ST_pf_munu<"<<ST_pf_munu_points<<"; jj_ST_pf_munu++){"<<std::endl;
std::cout<<"	 for (jj_MT_muon1pfMET=0; jj_MT_muon1pfMET<"<<MT_muon1pfMET_points<<"; jj_MT_muon1pfMET++){"<<std::endl;
std::cout<<"	 for (jj_MET_pf=0; jj_MET_pf<"<<MET_pf_points<<"; jj_MET_pf++){"<<std::endl;
std::cout<<"			 if (val_sys[jj_ST_pf_munu][jj_MT_muon1pfMET][jj_MET_pf]<xsys){"<<std::endl;
std::cout<<"				 xsys=val_sys[jj_ST_pf_munu][jj_MT_muon1pfMET][jj_MET_pf];"<<std::endl;
std::cout<<"				 ST_pf_munu_syscut= ST_pf_munu_CutValue[jj_ST_pf_munu][jj_MT_muon1pfMET][jj_MET_pf];"<<std::endl;
std::cout<<"				 MT_muon1pfMET_syscut= MT_muon1pfMET_CutValue[jj_ST_pf_munu][jj_MT_muon1pfMET][jj_MET_pf];"<<std::endl;
std::cout<<"				 MET_pf_syscut= MET_pf_CutValue[jj_ST_pf_munu][jj_MT_muon1pfMET][jj_MET_pf];"<<std::endl;
std::cout<<"}}}}"<<std::endl;

std::cout<<"std::cout<<\"ST_pf_munu @@@cut for cross section upper limit minimization (No Systematics) is determined to be:   \"<<ST_pf_munu_syscut<<std::endl;"<<std::endl;
std::cout<<"std::cout<<\"MT_muon1pfMET @@@cut for cross section upper limit minimization (No Systematics) is determined to be:   \"<<MT_muon1pfMET_syscut<<std::endl;"<<std::endl;
std::cout<<"std::cout<<\"MET_pf @@@cut for cross section upper limit minimization (No Systematics) is determined to be:   \"<<MET_pf_syscut<<std::endl;"<<std::endl;

std::cout<<"}"<<std::endl;
}