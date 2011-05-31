
#include "TLorentzVector.h"
#include "TH1.h"
#include <iostream>
#include <fstream>
#include <iomanip>
#include "/home/darinb/CMSStyle.C"


//float zbins[3] ={1,4.2,2.1};

//const int num_jj = 4;
//std::cout<<sizeof(zbins)<<std::endl;

void fillHisto(TString cut_mc, TString cut_data, bool drawHistograms, const int num, float xbins[num+1], TString var, bool writeoutput, TString fileName,TString title, TString Luminosity,Double_t extrascalefactor,int textbin) {
  CMSStyle();
  gStyle->SetOptLogy();
  
  TH1F* h_zjets = new TH1F("h_zjets","",num,xbins);
  TH1F* h_wjets = new TH1F("h_wjets","",num,xbins);
  TH1F* h_vvjets = new TH1F("h_vvjets","",num,xbins);
  TH1F* h_ttbar = new TH1F("h_ttbar","",num,xbins);
  TH1F* h_qcd = new TH1F("h_qcd","",num,xbins);
  TH1F* h_data = new TH1F("h_data","",num,xbins);
//  TH1F* h_LQToCMu_M_400 = new TH1F("h_LQToCMu_M_400","",num,xbins);

  //Histograms without weight
  TH1F* h_noweight_zjets = new TH1F("h_noweight_zjets","",num,xbins);
  TH1F* h_noweight_wjets = new TH1F("h_noweight_wjets","",num,xbins);
  TH1F* h_noweight_vvjets = new TH1F("h_noweight_vvjets","",num,xbins);
  TH1F* h_noweight_ttbar = new TH1F("h_noweight_ttbar","",num,xbins);
  TH1F* h_noweight_qcd = new TH1F("h_noweight_qcd","",num,xbins);
//  TH1F* h_noweight_LQToCMu_M_400 = new TH1F("h_noweight_LQToCMu_M_400","",num,xbins);

  zjets->Draw(var+">>h_zjets",cut_mc); 
  wjets->Draw(var+">>h_wjets",cut_mc);  
  ttbar->Draw(var+">>h_ttbar",cut_mc);  
  qcd->Draw(var+">>h_qcd",cut_mc); 
  vvjets->Draw(var+">>h_vvjets",cut_mc);  
//  LQToCMu_M_400->Draw(var+">>h_LQToCMu_M_400",cut_mc); 

  data->Draw(var+">>h_data",cut_data);
  zjets->Draw(var+">>h_noweight_zjets",cut_data); 
  wjets->Draw(var+">>h_noweight_wjets",cut_data);  
  ttbar->Draw(var+">>h_noweight_ttbar",cut_data);  
  qcd->Draw(var+">>h_noweight_qcd",cut_data); 
  vvjets->Draw(var+">>h_noweight_vvjets",cut_data);  
//  LQToCMu_M_400->Draw(var+">>h_moweight_LQToCMu_M_400",cut_mc); 

  TH1F* H_data  = new TH1F("H_data","",num,xbins);
  TH1F* H_zjets = new TH1F("H_zjets","",num,xbins);
  TH1F* H_wjets = new TH1F("H_wjets","",num,xbins);
  TH1F* H_ttbar = new TH1F("H_ttbar","",num,xbins);
  TH1F* H_vvjets = new TH1F("H_vvjets","",num,xbins);
  TH1F* H_qcd   = new TH1F("H_qcd","",num,xbins);
  TH1F* H_bkg   = new TH1F("H_bkg","",num,xbins);
//  TH1F* H_LQToCMu_M_400 = new TH1F("H_LQToCMu_M_400","",num,xbins);
  //  H_data->Sumw2();

  THStack* H_Pt_muon1 = new THStack("H_Pt_muon1","");
  

  h_zjets->Scale(1.28);
h_ttbar->Scale(194.0/165.0);
  H_bkg->Add(h_vvjets);
  H_bkg->Add(h_wjets);
  H_bkg->Add(h_qcd);

	H_data->Add(h_data);

	H_zjets->Add(h_zjets);
	H_ttbar->Add(h_ttbar);

  H_zjets->SetFillStyle(3004);
  H_ttbar->SetFillStyle(3005);
  H_bkg->SetFillStyle(3006);


  H_zjets->SetFillColor(2);
  H_ttbar->SetFillColor(4);
  H_bkg->SetFillColor(3);
  
  H_zjets->SetLineColor(2);
  H_ttbar->SetLineColor(4);
  H_bkg->SetLineColor(3);
    
  H_zjets->SetMarkerColor(2);
  H_ttbar->SetMarkerColor(4);
  H_bkg->SetMarkerColor(3);

	H_zjets->SetMarkerSize(.00000001);
	H_ttbar->SetMarkerSize(.00000001);
	H_bkg->SetMarkerSize(.00000001);

  H_zjets->SetLineWidth(2);
  H_ttbar->SetLineWidth(2);
  H_bkg->SetLineWidth(2);
  H_data->SetLineWidth(2);

  H_Pt_muon1->Add(H_bkg);
  H_Pt_muon1->Add(H_ttbar);
  H_Pt_muon1->Add(H_zjets);

	h_LQToCMu_M_400->SetLineStyle(2);
	h_LQToCMu_M_400->SetLineColor(1);
	h_LQToCMu_M_400->SetMarkerStyle(33);
	h_LQToCMu_M_400->SetMarkerSize(.00000001);
	h_LQToCMu_M_400->SetMarkerColor(1);
	h_LQToCMu_M_400->SetLineWidth(5);

  H_zjets->GetXaxis()->SetTitle(title);
  H_ttbar->GetXaxis()->SetTitle(title);
  H_data->GetXaxis()->SetTitle(title);
  H_data->GetYaxis()->SetTitle("Events/bin");
  H_data->GetXaxis()->SetTitleFont(132);
  H_data->GetYaxis()->SetTitleFont(132);

  
  gStyle->SetOptStat(0);
  H_data->Draw("E");
  H_Pt_muon1->Draw("SAME");
	h_LQToCMu_M_400->Draw("SAME");
  H_data->Draw("SAMEE");
  TLegend* leg = new TLegend(0.55,0.63,0.94,0.91,"","brNDC");
  leg->SetTextFont(132);
  leg->SetFillColor(0);
  leg->SetBorderSize(0);
  leg->AddEntry(H_data,"Data, " + Luminosity +" pb^{-1}");
  leg->AddEntry(H_zjets,"Z/#gamma* + jets");
  leg->AddEntry(H_ttbar,"t#bar{t}");
  leg->AddEntry(H_bkg,"Other backgrounds");
  leg->AddEntry(h_LQToCMu_M_400,"LQ, M = 400 GeV");
  leg->Draw("SAME");
  c1->SetLogy();

	H_data->SetMinimum((.0001*extrascalefactor)*(h_data->GetMaximum()));
	H_data->SetMaximum(extrascalefactor*15*(H_data->GetMaximum()));

  TLatex* txt =new TLatex((xbins[textbin]),.15*H_data->GetMaximum(), "CMS");  
  txt->SetTextFont(132); 
  txt->SetTextSize(0.06); 
  txt->Draw();
  c1->RedrawAxis();

    string str = Luminosity;
    string searchString( "." ); 
    string replaceString( "_" );

    assert( searchString != replaceString );

    string::size_type pos = 0;
    while ( (pos = str.find(searchString, pos)) != string::npos ) {
        str.replace( pos, searchString.size(), replaceString );
        pos++;
    }

	TString varname = var;
	varname +="_";
	varname += str;
	varname += "_VarBin";
	std::cout<<varname<<std::endl;
  c1->Print(varname+".png");
//  c1->Print(varname+".eps");

}


void MakeVarPlots() {

	TString lumi = "152.8"	;
  TString cut_data = "(Pt_muon1>30)*(Pt_muon2>30)";
  cut_data += "*(Pt_pfjet1>30)*(Pt_pfjet2>30)";
  cut_data += "*(M_muon1muon2>40)";
  cut_data += "*(ST_pf_mumu>250.0)";
	cut_mc = lumi+ "*weight*("+cut_data+")";
	gROOT->Reset();
	gROOT->ProcessLine(".x LoadLocal.C");
	float xbins_mm[19]={40,45,50,55,60,65,70,75,80,85,90,95,105,130,165,210,270,320,400};
  fillHisto(cut_mc, cut_data, true, 18,xbins_mm, "M_muon1muon2", false, "","M_{#mu#mu}(GeV)",lumi,1.0,7);


	// ST (With mass cut)
cut_data = "(precut_HLT==1)&&(muon_Pt_0>30)&&(muon_Pt_1>30)";
  cut_data += "&&(Jet_caloPt_0>30)&&(Jet_caloPt_1>30)";
  cut_data += "&&(abs(muon_Eta_0)<2.1||abs(muon_Eta_1)<2.1)";
	cut_data += "&&(M_muon1muon2>115)";
	cut_mc = lumi+ "*weight*("+cut_data+")";

	gROOT->Reset();
	gROOT->ProcessLine(".x LoadLocal.C");
float xbins_st[11]={120,150,180,210,240,270,300,340,400,480,800};

  fillHisto(cut_mc, cut_data, true, 10,xbins_st, "ST_calo", false, "","S_{T}(GeV)",lumi,12.0,4);
}
  


