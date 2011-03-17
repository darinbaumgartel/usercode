
#include "TLorentzVector.h"
#include "TH1.h"
#include "TF1.h"
#include <iostream>
#include <fstream>
#include "TLegend.h"
#include <iomanip>
//#include "/home/darinb/CMSStyle.C"
#include "TROOT.h"
#include "TH2F.h"
#include "TGraph.h"
#include "TGraphErrors.h"
#include "TTree.h"
#include "TFile.h"
#include "TCanvas.h"
#include <sstream>
#include <fstream>

TFile f__WJets("/home/darinb/scratch0/LQ/Winter2010/Stage1_NTupleAnalysis/CurrentRootFilesNorm/WJets.root");
TFile f__TTbarJets("/home/darinb/scratch0/LQ/Winter2010/Stage1_NTupleAnalysis/CurrentRootFilesNorm/TTbarJets.root");
TFile f__ZJets("/home/darinb/scratch0/LQ/Winter2010/Stage1_NTupleAnalysis/CurrentRootFilesNorm/ZJets.root");
TFile f__VVJets("/home/darinb/scratch0/LQ/Winter2010/Stage1_NTupleAnalysis/CurrentRootFilesNorm/VVJets.root");
TFile f__SingleTop("/home/darinb/scratch0/LQ/Winter2010/Stage1_NTupleAnalysis/CurrentRootFilesNorm/SingleTop.root");
TFile f__CurrentData("/home/darinb/scratch0/LQ/Winter2010/Stage1_NTupleAnalysis/CurrentRootFilesNorm/CurrentData.root");

TTree* wjets = (TTree* )f__WJets.Get("PhysicalVariables");
TTree* ttbar = (TTree* )f__TTbarJets.Get("PhysicalVariables");
TTree* zjets = (TTree* )f__ZJets.Get("PhysicalVariables");
TTree* vvjets = (TTree* )f__VVJets.Get("PhysicalVariables");
TTree* singtop = (TTree* )f__SingleTop.Get("PhysicalVariables");
TTree* data = (TTree* )f__CurrentData.Get("PhysicalVariables");

TCanvas *c1 = new TCanvas("c1");
//std::cout<<"OK A"<<std::endl;
void datahisto( TString varname, TString version, TString currentcut, int bins, float low,float high, TString xlabel)
{

	//	gROOT->ProcessLine(".x LoadLocal.C");
	TH1F* thishisto = new TH1F("thishisto","",bins,low,high);
	data->Draw(varname +">>thishisto",currentcut);
	thishisto->Fit("gaus");
	thishisto->GetXaxis()->SetTitle(xlabel);
	c1->Print("plots/gaus/data"+varname+"_"+version+".png");
}


void zmchisto( TString varname, TString version, TString currentcut, int bins, float low,float high, TString xlabel)
{
	//	gROOT->ProcessLine(".x LoadLocal.C");
	TH1F* thishisto = new TH1F("thishisto","",bins,low,high);
	zjets->Draw(varname +">>thishisto",currentcut);
	//  thishisto->Sumw2();
	thishisto->Fit("gaus");
	thishisto->GetXaxis()->SetTitle(xlabel);
	c1->Print("plots/gaus/zmc"+varname+"_"+version+".png");
}


void wmchisto( TString varname, TString version, TString currentcut, int bins, float low,float high, TString xlabel)
{
	//	gROOT->ProcessLine(".x LoadLocal.C");
	TH1F* thishisto = new TH1F("thishisto","",bins,low,high);
	wjets->Draw(varname +">>thishisto",currentcut);
	//  thishisto->Sumw2();
	thishisto->Fit("gaus");
	thishisto->GetXaxis()->SetTitle(xlabel);
	c1->Print("plots/gaus/wmc"+varname+"_"+version+".png");
}


static int nbin = 8;

// This is the main function.

void GetRecoilBins()
{
	// ******************************  Some setup routines. ******************************//

bool UseZGen = false;
bool UseWGen = true;

int numentriesperbin = 100;
float PTMax = 250;
	// some setup stuff
	std::ostringstream strs;
	TString cutstring;  string cut;

//	gROOT->ProcessLine(".x LoadLocal.C");

	// Details of the main cuts for Z
	TString lumi = "36.1"   ;
	TString cut_data = "(Pt_muon1>30)&&(Pt_muon2>30)";
	TString cut_data_w = "(Pt_genmuon1>30)&&(MET_pf>30)";

	std::cout<<data->GetEntries()<<std::endl;
	std::cout<<data->GetEntries(cut_data)<<std::endl;
//	gROOT->ProcessLine(".q;");
	// Copy the tree with Z cuts for binning
	TFile f__temp("data_filter.root","recreate");
	TTree* newdata = data ->CopyTree(cut_data);

	// Binning setup
	float start = 0.000001; float stop = .00001;
	float goodcut = 0.0;    int num = 0;
	vector<float> bins;

	std::string str0;
	std::string str1;
	std::string str2;

	// ******************************  Get bin increments based on ACTUAL DATA ******************************//

	// Binning loop
	while (goodcut<PTMax)
	{
		goodcut = goodcut + .1;
		stop = goodcut;
		strs << start;  str0 = strs.str();  strs.str("");
		strs << stop;   str1 = strs.str();  strs.str("");
		cut = "(Pt_Z>" + str0 + ")&&(Pt_Z<" +str1+")";

		cutstring = cut;
		num = newdata->GetEntries(cutstring);

		if (num > numentriesperbin)
		{
			start = goodcut-.0001;
			bins.push_back(goodcut);
		}
	}

	bins.push_back(PTMax);

	nbin = bins.size();
std::cout<<"ok"<<std::endl;
	// ******************************  Make plots and data for ACTUAL DATA ******************************//

	// Setup to plot and evaluate each data z Pt bin
	int bindex = 0;
	float lowpoint = 0;
	float highpoint = bins[0];
	float U1Zmean = 999999;
	float U1Zrms = 999999;
	float U2Zmean = 999999;
	float U2Zrms = 999999;
	float Error_U1Zmean = 999999;
	float Error_U1Zrms = 999999;
	float Error_U2Zmean = 999999;
	float Error_U2Zrms = 999999;
	float U1Wmean = 999999;
	float U1Wrms = 999999;
	float U2Wmean = 999999;
	float U2Wrms = 999999;
	float Error_U1Wmean = 999999;
	float Error_U1Wrms = 999999;
	float Error_U2Wmean = 999999;
	float Error_U2Wrms = 999999;

	float mean_u1z[nbin]; float rms_u1z[nbin]; float mean_u2z[nbin]; float rms_u2z[nbin]; float bincenter[nbin]; float binhalfwidth[nbin];
	float Error_mean_u1z[nbin]; float Error_rms_u1z[nbin]; float Error_mean_u2z[nbin]; float Error_rms_u2z[nbin];

	// Loop over bins and evaulate each bin
	for (bindex=0;bindex<bins.size();bindex++)
	{

		TH1F* hZ1 = new TH1F("hZ1","",300000,-1000,1000);
		TH1F* hZ2 = new TH1F("hZ2","",300000,-1000,1000);
		highpoint = bins[bindex];
		strs << lowpoint;   str0 = strs.str();  strs.str("");
		strs << highpoint;  str1 = strs.str();  strs.str("");
		cut = "(Pt_Z>" + str0 + ")&&(Pt_Z<" +str1+")";
		cutstring = cut;

		strs << bindex;  str0 = strs.str();  strs.str("");
		strs << lowpoint;  str1 = strs.str();  strs.str("");
		strs << highpoint;  str2 = strs.str();  strs.str("");

								 //  hZ1->Draw();
		data->Draw("U1_Z>>hZ1",cutstring+"&&"+ cut_data);
		U1Zmean = hZ1->GetMean();   U1Zrms = hZ1->GetRMS();
		Error_U1Zmean = hZ1->GetMeanError();   Error_U1Zrms = hZ1->GetRMSError();

								 //  hZ2->Draw();
		data->Draw("U2_Z>>hZ2",cutstring+"&&"+ cut_data);
		U2Zmean = hZ2->GetMean();   U2Zrms = hZ2->GetRMS();
		Error_U2Zmean = hZ2->GetMeanError();   Error_U2Zrms = hZ2->GetRMSError();

		datahisto("U1_Z",str0,cutstring+"&&"+ cut_data,30,U1Zmean - 4*U1Zrms,U1Zmean + 4*U1Zrms,"U1(Z) [data]  p_T(Z): "+str1+" - "+str2);
		datahisto("U2_Z",str0,cutstring+"&&"+ cut_data,30,U2Zmean - 4*U2Zrms,U2Zmean + 4*U2Zrms,"U2(Z) [data]  p_T(Z): "+str1+" - "+str2);

		//		std::cout<<"BIN_"+str0<<","<<lowpoint<<","<<highpoint<<","<<U1Zmean<<","<<U1Zrms<<","<<U2Zmean<<","<<U2Zrms<<std::endl;

		mean_u1z[bindex] = (U1Zmean); rms_u1z[bindex] = (U1Zrms);
		mean_u2z[bindex] = (U2Zmean); rms_u2z[bindex] = (U2Zrms);
		Error_mean_u1z[bindex] = (Error_U1Zmean); Error_rms_u1z[bindex] = (Error_U1Zrms);
		Error_mean_u2z[bindex] = (Error_U2Zmean); Error_rms_u2z[bindex] = (Error_U2Zrms);

		bincenter[bindex] = (lowpoint + (highpoint-lowpoint)/2.0);
		binhalfwidth[bindex] = ((highpoint-lowpoint)/2.0);

		lowpoint = highpoint;
	}

	// ******************************  Run Z Analysis ******************************//

	float mean_u1z_zmc[nbin]; float  rms_u1z_zmc[nbin]; float  mean_u2z_zmc[nbin]; float  rms_u2z_zmc[nbin];
	float Error_mean_u1z_zmc[nbin]; float Error_rms_u1z_zmc[nbin]; float Error_mean_u2z_zmc[nbin]; float Error_rms_u2z_zmc[nbin];

	lowpoint =0;
	// Loop over bins and evaulate each bin



	if (!UseZGen)
	{
		for (bindex=0;bindex<bins.size();bindex++)
		{
			TH1F* hZ1 = new TH1F("hZ1","",300000,-1000,1000);
			TH1F* hZ2 = new TH1F("hZ2","",300000,-1000,1000);
			highpoint = bins[bindex];
			strs << lowpoint;  str0 = strs.str();  strs.str("");
			strs << highpoint;   str1 = strs.str();  strs.str("");
			cut = "(Pt_Z>" + str0 + ")&&(Pt_Z<" +str1+")";
			cutstring = cut;
			strs << bindex;   str0 = strs.str();  strs.str("");
			strs << lowpoint;   str1 = strs.str();  strs.str("");
			strs << highpoint;   str2 = strs.str();  strs.str("");

			hZ1->Sumw2();
								 //  hZ1->Draw();
			zjets->Draw("U1_Z>>hZ1","weight*36.1*"+cutstring+"&&"+ cut_data);
			hZ1->Sumw2();
			U1Zmean = hZ1->GetMean();   U1Zrms = hZ1->GetRMS();
			Error_U1Zmean = hZ1->GetMeanError();   Error_U1Zrms = hZ1->GetRMSError();

			hZ2->Sumw2();
								 //  hZ2->Draw();
			zjets->Draw("U2_Z>>hZ2","weight*36.1*"+cutstring+"&&"+ cut_data);
			hZ2->Sumw2();
			U2Zmean = hZ2->GetMean();   U2Zrms = hZ2->GetRMS();
			Error_U2Zmean = hZ2->GetMeanError();   Error_U2Zrms = hZ2->GetRMSError();
			zmchisto("U1_Z",str0,"weight*36.1*"+cutstring+"&&"+ cut_data,30,U1Zmean - 4*U1Zrms,U1Zmean + 4*U1Zrms,"U1(Z) [Z MC]  p_T(Z): "+str1+" - "+str2);
			zmchisto("U2_Z",str0,"weight*36.1*"+cutstring+"&&"+ cut_data,30,U2Zmean - 4*U2Zrms,U2Zmean + 4*U2Zrms,"U2(Z) [Z MC]  p_T(Z): "+str1+" - "+str2);

			mean_u1z_zmc[bindex] = (U1Zmean); rms_u1z_zmc[bindex] = (U1Zrms);
			mean_u2z_zmc[bindex] = (U2Zmean); rms_u2z_zmc[bindex] = (U2Zrms);
			Error_mean_u1z_zmc[bindex] = (Error_U1Zmean); Error_rms_u1z_zmc[bindex] = (Error_U1Zrms);
			Error_mean_u2z_zmc[bindex] = (Error_U2Zmean); Error_rms_u2z_zmc[bindex] = (Error_U2Zrms);
			lowpoint = highpoint;
		}
	}
	if (UseZGen)
	{
		for (bindex=0;bindex<bins.size();bindex++)
		{
			TH1F* hZ1 = new TH1F("hZ1","",300000,-1000,1000);
			TH1F* hZ2 = new TH1F("hZ2","",300000,-1000,1000);
			highpoint = bins[bindex];
			strs << lowpoint;  str0 = strs.str();  strs.str("");
			strs << highpoint;   str1 = strs.str();  strs.str("");
			cut = "(Pt_Z>" + str0 + ")&&(Pt_Z<" +str1+")";
			cutstring = cut;
			strs << bindex;   str0 = strs.str();  strs.str("");
			strs << lowpoint;   str1 = strs.str();  strs.str("");
			strs << highpoint;   str2 = strs.str();  strs.str("");

			hZ1->Sumw2();
								 //  hZ1->Draw();
			zjets->Draw("U1_Z_gen>>hZ1","weight*36.1*"+cutstring+"&&"+ cut_data);
			hZ1->Sumw2();
			U1Zmean = hZ1->GetMean();   U1Zrms = hZ1->GetRMS();
			Error_U1Zmean = hZ1->GetMeanError();   Error_U1Zrms = hZ1->GetRMSError();

			hZ2->Sumw2();
								 //  hZ2->Draw();
			zjets->Draw("U2_Z_gen>>hZ2","weight*36.1*"+cutstring+"&&"+ cut_data);
			hZ2->Sumw2();
			U2Zmean = hZ2->GetMean();   U2Zrms = hZ2->GetRMS();
			Error_U2Zmean = hZ2->GetMeanError();   Error_U2Zrms = hZ2->GetRMSError();

			zmchisto("U1_Z_gen",str0,"weight*36.1*"+cutstring+"&&"+ cut_data,30,U1Zmean - 4*U1Zrms,U1Zmean + 4*U1Zrms,"U1(Z) [Z MC Gen]  p_T(Z): "+str1+" - "+str2);
			zmchisto("U2_Z_gen",str0,"weight*36.1*"+cutstring+"&&"+ cut_data,30,U2Zmean - 4*U2Zrms,U2Zmean + 4*U2Zrms,"U2(Z) [Z MC Gen]  p_T(Z): "+str1+" - "+str2);

			mean_u1z_zmc[bindex] = (U1Zmean); rms_u1z_zmc[bindex] = (U1Zrms);
			mean_u2z_zmc[bindex] = (U2Zmean); rms_u2z_zmc[bindex] = (U2Zrms);

			Error_mean_u1z_zmc[bindex] = (Error_U1Zmean); Error_rms_u1z_zmc[bindex] = (Error_U1Zrms);
			Error_mean_u2z_zmc[bindex] = (Error_U2Zmean); Error_rms_u2z_zmc[bindex] = (Error_U2Zrms);
			lowpoint = highpoint;
		}
	}


	// ******************************  Run W Analysis ******************************//

	float mean_u1w_wmc[nbin]; float  rms_u1w_wmc[nbin]; float  mean_u2w_wmc[nbin]; float  rms_u2w_wmc[nbin];
	float Error_mean_u1w_wmc[nbin]; float Error_rms_u1w_wmc[nbin]; float Error_mean_u2w_wmc[nbin]; float Error_rms_u2w_wmc[nbin];

	lowpoint =0;
	// Loop over bins and evaulate each bin

	if (!UseWGen)
	{
		for (bindex=0;bindex<bins.size();bindex++)
		{
			TH1F* hW1 = new TH1F("hW1","",300000,-1000,1000);
			TH1F* hW2 = new TH1F("hW2","",300000,-1000,1000);
			highpoint = bins[bindex];
			strs << lowpoint;  str0 = strs.str();  strs.str("");
			strs << highpoint;   str1 = strs.str();  strs.str("");
			cut = "(Pt_W>" + str0 + ")&&(Pt_W<" +str1+")";
			cutstring = cut;
			strs << bindex;   str0 = strs.str();  strs.str("");
			strs << lowpoint;   str1 = strs.str();  strs.str("");
			strs << highpoint;   str2 = strs.str();  strs.str("");


			hW1->Sumw2();
								 //  hW1->Draw();
			wjets->Draw("U1_W>>hW1","weight*36.1*"+cutstring+"&&"+ cut_data_w);
			hW1->Sumw2();
			U1Wmean = hW1->GetMean();   U1Wrms = hW1->GetRMS();
			Error_U1Wmean = hW1->GetMeanError();   Error_U1Wrms = hW1->GetRMSError();

			hW2->Sumw2();
								 //  hW2->Draw();
			wjets->Draw("U2_W>>hW2","weight*36.1*"+cutstring+"&&"+ cut_data_w);
			hW2->Sumw2();
			U2Wmean = hW2->GetMean();   U2Wrms = hW2->GetRMS();
			Error_U2Wmean = hW2->GetMeanError();   Error_U2Wrms = hW2->GetRMSError();

			wmchisto("U1_W",str0,"weight*36.1*"+cutstring+"&&"+ cut_data_w,30,U1Wmean - 4*U1Wrms,U1Wmean + 4*U1Wrms,"U1(W) [W MC]  p_T(W): "+str1+" - "+str2);
			wmchisto("U2_W",str0,"weight*36.1*"+cutstring+"&&"+ cut_data_w,30,U2Wmean - 4*U2Wrms,U2Wmean + 4*U2Wrms,"U2(W) [W MC]  p_T(W): "+str1+" - "+str2);

			mean_u1w_wmc[bindex] = (U1Wmean); rms_u1w_wmc[bindex] = (U1Wrms);
			mean_u2w_wmc[bindex] = (U2Wmean); rms_u2w_wmc[bindex] = (U2Wrms);

			Error_mean_u1w_wmc[bindex] = (Error_U1Wmean); Error_rms_u1w_wmc[bindex] = (Error_U1Wrms);
			Error_mean_u2w_wmc[bindex] = (Error_U2Wmean); Error_rms_u2w_wmc[bindex] = (Error_U2Wrms);
			lowpoint = highpoint;
		}
	}
	if (UseWGen)
	{
		for (bindex=0;bindex<bins.size();bindex++)
		{
			TH1F* hW1 = new TH1F("hW1","",300000,-1000,1000);
			TH1F* hW2 = new TH1F("hW2","",300000,-1000,1000);
			highpoint = bins[bindex];
			strs << lowpoint;  str0 = strs.str();  strs.str("");
			strs << highpoint;   str1 = strs.str();  strs.str("");
			cut = "(Pt_W_gen>" + str0 + ")&&(Pt_W_gen<" +str1+")";
			cutstring = cut;
			strs << bindex;   str0 = strs.str();  strs.str("");
			strs << lowpoint;   str1 = strs.str();  strs.str("");
			strs << highpoint;   str2 = strs.str();  strs.str("");
//     std::cout<<"&&&&&&&&&&&&&&&&&&&&   "<<wjets->GetEntries()<<std::endl;
//     std::cout<<"&&&&&&&&&&&&&&&&&&&&   "<<wjets->GetEntries(cutstring)<<std::endl;
//     std::cout<<"&&&&&&&&&&&&&&&&&&&&   "<<wjets->GetEntries(cut_data_w)<<std::endl;
//     std::cout<<"&&&&&&&&&&&&&&&&&&&&   "<<wjets->GetEntries("weight*36.1*"+cutstring+"&&"+ cut_data_w)<<std::endl;
			hW1->Sumw2();
								 //  hW1->Draw();
			wjets->Draw("U1_W_gen>>hW1","weight*36.1*"+cutstring+"&&"+ cut_data_w);
			hW1->Sumw2();
			U1Wmean = hW1->GetMean();   U1Wrms = hW1->GetRMS();
			Error_U1Wmean = hW1->GetMeanError();   Error_U1Wrms = hW1->GetRMSError();

			hW2->Sumw2();
								 //  hW2->Draw();
			wjets->Draw("U2_W_gen>>hW2","weight*36.1*"+cutstring+"&&"+ cut_data_w);
			hW2->Sumw2();
			U2Wmean = hW2->GetMean();   U2Wrms = hW2->GetRMS();
			Error_U2Wmean = hW2->GetMeanError();   Error_U2Wrms = hW2->GetRMSError();

			wmchisto("U1_W_gen",str0,"weight*36.1*"+cutstring+"&&"+ cut_data_w,30,U1Wmean - 4*U1Wrms,U1Wmean + 4*U1Wrms,"U1(W) [W MC Gen]  p_T(W): "+str1+" - "+str2);
			wmchisto("U2_W_gen",str0,"weight*36.1*"+cutstring+"&&"+ cut_data_w,30,U2Wmean - 4*U2Wrms,U2Wmean + 4*U2Wrms,"U2(W) [W MC Gen]  p_T(W): "+str1+" - "+str2);

			mean_u1w_wmc[bindex] = (U1Wmean); rms_u1w_wmc[bindex] = (U1Wrms);
			mean_u2w_wmc[bindex] = (U2Wmean); rms_u2w_wmc[bindex] = (U2Wrms);

			Error_mean_u1w_wmc[bindex] = (Error_U1Wmean); Error_rms_u1w_wmc[bindex] = (Error_U1Wrms);
			Error_mean_u2w_wmc[bindex] = (Error_U2Wmean); Error_rms_u2w_wmc[bindex] = (Error_U2Wrms);
			lowpoint = highpoint;
		}
	}


	// ******************************  Make plots and data for Z MC ******************************//

	std::ofstream file("RecoilBinLog.txt");
	std::cout.rdbuf(file.rdbuf());

	std::cout<<"\n\n\n\n\n\n\n\n**********************************************************\n\n                      FITTING RESULTS                 \n\n****************************************************\n\n\n\n"<<std::endl;

  // Just Z and Data

	TGraphErrors *GR_data_u1 = new TGraphErrors(nbin,bincenter,mean_u1z, binhalfwidth,Error_mean_u1z);
	TGraphErrors *GR_zmc_u1 = new TGraphErrors(nbin,bincenter,mean_u1z_zmc, binhalfwidth,Error_mean_u1z_zmc);
	GR_data_u1->GetYaxis()->SetTitle("U_{1} [Mean]");
	GR_data_u1->GetXaxis()->SetTitle("p_{T} (Z)");
	GR_data_u1->GetHistogram()->SetMaximum(10);
	GR_data_u1->GetHistogram()->SetMinimum(-100);
	TCanvas *c_u1 = new TCanvas("c_u1");
	GR_data_u1->SetMarkerColor(1);   GR_data_u1->SetLineColor(1);
	GR_data_u1->SetMarkerStyle(7);  GR_data_u1->Draw("AP");
	GR_zmc_u1->SetMarkerColor(2);   GR_zmc_u1->SetLineColor(2);
	GR_zmc_u1->SetMarkerStyle(7);  GR_zmc_u1->Draw("P");
	std::cout<<"\n\n#################       Fit:: U1 Data       ################\n\n"<<std::endl;
	GR_data_u1->Fit("pol1");	std::cout<<"****************************"<<std::endl;
	GR_data_u1->GetFunction("pol1")->SetLineColor(1);
	GR_data_u1->GetFunction("pol1")->SetLineWidth(2);
	std::cout<<"\n\n#################       Fit:: U1 Z MC       ################\n\n"<<std::endl;
	GR_zmc_u1->Fit("pol1");	std::cout<<"****************************"<<std::endl;
	GR_zmc_u1->GetFunction("pol1")->SetLineColor(2);
	GR_zmc_u1->GetFunction("pol1")->SetLineWidth(2);
	c_u1->Print("plots/fits/U1_Z_mean.png");

	TGraphErrors *GR_data_u2 = new TGraphErrors(nbin,bincenter,mean_u2z, binhalfwidth,Error_mean_u2z);
	TGraphErrors *GR_zmc_u2 = new TGraphErrors(nbin,bincenter,mean_u2z_zmc, binhalfwidth,Error_mean_u2z_zmc);
	GR_data_u2->GetYaxis()->SetTitle("U_{2} [Mean]");
	GR_data_u2->GetXaxis()->SetTitle("p_{T} (Z)");
	GR_data_u2->GetHistogram()->SetMaximum(4);
	GR_data_u2->GetHistogram()->SetMinimum(-4);
	TCanvas *c_u2 = new TCanvas("c_u2");
	std::cout<<"\n\n#################       Fit:: U2 Data       ################\n\n"<<std::endl;
	GR_data_u2->Fit("pol1");	std::cout<<"****************************"<<std::endl;
	GR_data_u2->GetFunction("pol1")->SetLineColor(1);
	GR_data_u2->GetFunction("pol1")->SetLineWidth(2);
	std::cout<<"\n\n#################       Fit:: U2 Z MC       ################\n\n"<<std::endl;
	GR_zmc_u2->Fit("pol1");	std::cout<<"****************************"<<std::endl;
	GR_zmc_u2->GetFunction("pol1")->SetLineColor(2);
	GR_zmc_u2->GetFunction("pol1")->SetLineWidth(2);
	GR_data_u2->SetMarkerColor(1);   GR_data_u2->SetLineColor(1);
	GR_data_u2->SetMarkerStyle(7);  GR_data_u2->Draw("AP");
	GR_zmc_u2->SetMarkerColor(2);   GR_zmc_u2->SetLineColor(2);
	GR_zmc_u2->SetMarkerStyle(7);  GR_zmc_u2->Draw("P");

	c_u2->Print("plots/fits/U2_Z_mean.png");

	TGraphErrors *GR_rms__data_u1 = new TGraphErrors(nbin,bincenter,rms_u1z, binhalfwidth,Error_rms_u1z);
	TGraphErrors *GR_rms__zmc_u1 = new TGraphErrors(nbin,bincenter,rms_u1z_zmc, binhalfwidth,Error_rms_u1z_zmc);
	GR_rms__data_u1->GetYaxis()->SetTitle("U_{1} [RMS]");
	GR_rms__data_u1->GetXaxis()->SetTitle("p_{T} (Z)");
	GR_rms__data_u1->GetHistogram()->SetMaximum(40);
	GR_rms__data_u1->GetHistogram()->SetMinimum(0);
	TCanvas *c_rms_u1 = new TCanvas("c_rms_u1");
	std::cout<<"\n\n#################       Fit:: U1 rms Data       ################\n\n"<<std::endl;
	GR_rms__data_u1->Fit("pol2");	std::cout<<"****************************"<<std::endl;
	GR_rms__data_u1->GetFunction("pol2")->SetLineColor(1);
	GR_rms__data_u1->GetFunction("pol2")->SetLineWidth(2);
	std::cout<<"\n\n#################       Fit:: U1 rms Z MC       ################\n\n"<<std::endl;
	GR_rms__zmc_u1->Fit("pol2");	std::cout<<"****************************"<<std::endl;
	GR_rms__zmc_u1->GetFunction("pol2")->SetLineColor(2);
	GR_rms__zmc_u1->GetFunction("pol2")->SetLineWidth(2);
	GR_rms__data_u1->SetMarkerColor(1);   GR_rms__data_u1->SetLineColor(1);
	GR_rms__data_u1->SetMarkerStyle(7);  GR_rms__data_u1->Draw("AP");
	GR_rms__zmc_u1->SetMarkerColor(2);   GR_rms__zmc_u1->SetLineColor(2);
	GR_rms__zmc_u1->SetMarkerStyle(7);  GR_rms__zmc_u1->Draw("P");
	c_rms_u1->Print("plots/fits/U1_Z_rms.png");

	TGraphErrors *GR_rms__data_u2 = new TGraphErrors(nbin,bincenter,rms_u2z, binhalfwidth,Error_rms_u2z);
	TGraphErrors *GR_rms__zmc_u2 = new TGraphErrors(nbin,bincenter,rms_u2z_zmc, binhalfwidth,Error_rms_u2z_zmc);
	GR_rms__data_u2->GetYaxis()->SetTitle("U_{2} [RMS]");
	GR_rms__data_u2->GetXaxis()->SetTitle("p_{T} (Z)");
	GR_rms__data_u2->GetHistogram()->SetMaximum(40);
	GR_rms__data_u2->GetHistogram()->SetMinimum(0);
	TCanvas *c_rms_u2 = new TCanvas("c_rms_u2");
	std::cout<<"\n\n#################       Fit:: U2 rms Data       ################\n\n"<<std::endl;
	GR_rms__data_u2->Fit("pol2");	std::cout<<"****************************"<<std::endl;
	GR_rms__data_u2->GetFunction("pol2")->SetLineColor(1);
	GR_rms__data_u2->GetFunction("pol2")->SetLineWidth(2);
	std::cout<<"\n\n#################       Fit:: U2 rms Z MC       ################\n\n"<<std::endl;
	GR_rms__zmc_u2->Fit("pol2");	std::cout<<"****************************"<<std::endl;
	GR_rms__zmc_u2->GetFunction("pol2")->SetLineColor(2);
	GR_rms__zmc_u2->GetFunction("pol2")->SetLineWidth(2);
	GR_rms__data_u2->SetMarkerColor(1);   GR_rms__data_u2->SetLineColor(1);
	GR_rms__data_u2->SetMarkerStyle(7);  GR_rms__data_u2->Draw("AP");
	GR_rms__zmc_u2->SetMarkerColor(2);   GR_rms__zmc_u2->SetLineColor(2);
	GR_rms__zmc_u2->SetMarkerStyle(7);  GR_rms__zmc_u2->Draw("P");
	c_rms_u2->Print("plots/fits/U2_Z_rms.png");

  // Z and W and Data

	TGraphErrors *GRw__data_u1 = new TGraphErrors(nbin,bincenter,mean_u1z, binhalfwidth,Error_mean_u1z);
	TGraphErrors *GRw__wmc_u1 = new TGraphErrors(nbin,bincenter,mean_u1w_wmc, binhalfwidth,Error_mean_u1w_wmc);
	GRw__data_u1->GetYaxis()->SetTitle("U_{1} [Mean]");
	GRw__data_u1->GetXaxis()->SetTitle("p_{T} (Z or W)");
	GRw__data_u1->GetHistogram()->SetMaximum(20);
	GRw__data_u1->GetHistogram()->SetMinimum(-160);
	TCanvas *cw_u1 = new TCanvas("c_u1");
	std::cout<<"\n\n#################       Fit:: U1  Data       ################\n\n"<<std::endl;
	GRw__data_u1->Fit("pol1");	std::cout<<"****************************"<<std::endl;
	GRw__data_u1->GetFunction("pol1")->SetLineColor(1);
	GRw__data_u1->GetFunction("pol1")->SetLineWidth(2);
	std::cout<<"\n\n#################       Fit:: U1  W MC       ################\n\n"<<std::endl;
	GRw__wmc_u1->Fit("pol1");	std::cout<<"****************************"<<std::endl;
	GRw__wmc_u1->GetFunction("pol1")->SetLineColor(4);
	GRw__wmc_u1->GetFunction("pol1")->SetLineWidth(2);
	GRw__data_u1->SetMarkerColor(1);   GRw__data_u1->SetLineColor(1);  GRw__data_u1->SetFillColor(kWhite);
	GRw__data_u1->SetMarkerStyle(7);  GRw__data_u1->Draw("AP");
	GRw__wmc_u1->SetMarkerColor(4);   GRw__wmc_u1->SetLineColor(4); GRw__wmc_u1->SetFillColor(kWhite);
	GRw__wmc_u1->SetMarkerStyle(7);  GRw__wmc_u1->Draw("P"); 
	GR_zmc_u1->SetFillColor(kWhite);   ;  GR_zmc_u1->Draw("P"); 
  TLegend* l=new TLegend(0.6,0.7,0.85,0.9); 
 GRw__data_u1->SetName("GRw__data_u1");
 GR_zmc_u1->SetName("GR_zmc_u1");
 GRw__wmc_u1->SetName("GRw__wmc_u1");

  l->AddEntry("GRw__data_u1","Z events [data]");
  l->AddEntry("GR_zmc_u1","Z events [Alpgen Z MC]");
  l->AddEntry("GRw__wmc_u1","W events [Alpgen W MC]");
  l->Draw("same");


	cw_u1->Print("plots/fits/U1_W_.png");

	TGraphErrors *GRw__data_u2 = new TGraphErrors(nbin,bincenter,mean_u2z, binhalfwidth,Error_mean_u2z);
	TGraphErrors *GRw__wmc_u2 = new TGraphErrors(nbin,bincenter,mean_u2w_wmc, binhalfwidth,Error_mean_u2w_wmc);
	GRw__data_u2->GetYaxis()->SetTitle("U_{2} [Mean]");
	GRw__data_u2->GetXaxis()->SetTitle("p_{T} (Z or W)");
	GRw__data_u2->GetHistogram()->SetMaximum(7);
	GRw__data_u2->GetHistogram()->SetMinimum(-7);
	TCanvas *cw_u2 = new TCanvas("c_u2");
	std::cout<<"\n\n#################       Fit:: U2  Data       ################\n\n"<<std::endl;
	GRw__data_u2->Fit("pol1");	std::cout<<"****************************"<<std::endl;
	GRw__data_u2->GetFunction("pol1")->SetLineColor(1);
	GRw__data_u2->GetFunction("pol1")->SetLineWidth(2);
	std::cout<<"\n\n#################       Fit:: U2  W MC       ################\n\n"<<std::endl;
	GRw__wmc_u2->Fit("pol1");	std::cout<<"****************************"<<std::endl;
	GRw__wmc_u2->GetFunction("pol1")->SetLineColor(4);
	GRw__wmc_u2->GetFunction("pol1")->SetLineWidth(2);
	GRw__data_u2->SetMarkerColor(1);   GRw__data_u2->SetLineColor(1);
	GRw__data_u2->SetMarkerStyle(7);  GRw__data_u2->Draw("AP");
	GRw__wmc_u2->SetMarkerColor(4);   GRw__wmc_u2->SetLineColor(4);
	GRw__wmc_u2->SetMarkerStyle(7);  GRw__wmc_u2->Draw("P"); GR_zmc_u2->Draw("P");
  l->Draw("same");
	cw_u2->Print("plots/fits/U2_W_.png");



	TGraphErrors *GRw_rms__data_u1 = new TGraphErrors(nbin,bincenter,rms_u1z, binhalfwidth,Error_rms_u1z);
	TGraphErrors *GRw_rms__wmc_u1 = new TGraphErrors(nbin,bincenter,rms_u1w_wmc, binhalfwidth,Error_rms_u1w_wmc);
	GRw_rms__data_u1->GetYaxis()->SetTitle("U_{1} [RMS]");
	GRw_rms__data_u1->GetXaxis()->SetTitle("p_{T} (Z or W)");
	GRw_rms__data_u1->GetHistogram()->SetMaximum(90);
	GRw_rms__data_u1->GetHistogram()->SetMinimum(0);
	TCanvas *cw_rms_u1 = new TCanvas("c_rms_u1");
	std::cout<<"\n\n#################       Fit:: U1 rms Data       ################\n\n"<<std::endl;
	GRw_rms__data_u1->Fit("pol2");	std::cout<<"****************************"<<std::endl;
	GRw_rms__data_u1->GetFunction("pol2")->SetLineColor(1);
	GRw_rms__data_u1->GetFunction("pol2")->SetLineWidth(2);
	std::cout<<"\n\n#################       Fit:: U1 rms W MC       ################\n\n"<<std::endl;
	GRw_rms__wmc_u1->Fit("pol2");	std::cout<<"****************************"<<std::endl;
	GRw_rms__wmc_u1->GetFunction("pol2")->SetLineColor(4);
	GRw_rms__wmc_u1->GetFunction("pol2")->SetLineWidth(2);
	GRw_rms__data_u1->SetMarkerColor(1);   GRw_rms__data_u1->SetLineColor(1);
	GRw_rms__data_u1->SetMarkerStyle(7);  GRw_rms__data_u1->Draw("AP");
	GRw_rms__wmc_u1->SetMarkerColor(4);   GRw_rms__wmc_u1->SetLineColor(4);
	GRw_rms__wmc_u1->SetMarkerStyle(7);  GRw_rms__wmc_u1->Draw("P"); GR_rms__zmc_u1->Draw("P");
  l->Draw("same");
	cw_rms_u1->Print("plots/fits/U1_W_rms.png");

	TGraphErrors *GRw_rms__data_u2 = new TGraphErrors(nbin,bincenter,rms_u2z, binhalfwidth,Error_rms_u2z);
	TGraphErrors *GRw_rms__wmc_u2 = new TGraphErrors(nbin,bincenter,rms_u2w_wmc, binhalfwidth,Error_rms_u2w_wmc);
	GRw_rms__data_u2->GetYaxis()->SetTitle("U_{2} [RMS]");
	GRw_rms__data_u2->GetXaxis()->SetTitle("p_{T} (Z or W)");
	GRw_rms__data_u2->GetHistogram()->SetMaximum(100);
	GRw_rms__data_u2->GetHistogram()->SetMinimum(0);
	TCanvas *cw_rms_u2 = new TCanvas("c_rms_u2");
	std::cout<<"\n\n#################       Fit:: U2 rms Data       ################\n\n"<<std::endl;
	GRw_rms__data_u2->Fit("pol2");	std::cout<<"****************************"<<std::endl;
	GRw_rms__data_u2->GetFunction("pol2")->SetLineColor(1);
	GRw_rms__data_u2->GetFunction("pol2")->SetLineWidth(2);
	std::cout<<"\n\n#################       Fit:: U2 rms W MC       ################\n\n"<<std::endl;
	GRw_rms__wmc_u2->Fit("pol2");	std::cout<<"****************************"<<std::endl;
	GRw_rms__wmc_u2->GetFunction("pol2")->SetLineColor(4);
	GRw_rms__wmc_u2->GetFunction("pol2")->SetLineWidth(2);
	GRw_rms__data_u2->SetMarkerColor(1);   GRw_rms__data_u2->SetLineColor(1);
	GRw_rms__data_u2->SetMarkerStyle(7);  GRw_rms__data_u2->Draw("AP");
	GRw_rms__wmc_u2->SetMarkerColor(4);   GRw_rms__wmc_u2->SetLineColor(4);
	GRw_rms__wmc_u2->SetMarkerStyle(7);  GRw_rms__wmc_u2->Draw("P"); GR_rms__zmc_u2->Draw("P");
  l->Draw("same");
	cw_rms_u2->Print("plots/fits/U2_W_rms.png");


	std::cout<<"\n\n\n"<<std::endl;


}
