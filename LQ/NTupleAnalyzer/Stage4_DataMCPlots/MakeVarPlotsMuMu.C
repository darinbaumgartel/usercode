
#include "TLorentzVector.h"
#include "TH1.h"
#include <iostream>
#include <fstream>
#include <iomanip>
#include "/home/darinb/CMSStyle.C"

void fillHisto(TString cut_mc, TString cut_data,  bool drawHistograms,  
  	     const int num, float xbins[num+1], TString var, bool writeoutput, TString fileName,TString title, TString Luminosity,Double_t extrascalefactor,Double_t znorm,TString tag) {
  CMSStyle();
//  gStyle->SetOptLogy();
  TH1F* h_zjets = new TH1F("h_zjets","",num,xbins);
  TH1F* h_wjets = new TH1F("h_wjets","",num,xbins);
  TH1F* h_vvjets = new TH1F("h_vvjets","",num,xbins);
  TH1F* h_singtop = new TH1F("h_singtop","",num,xbins);
  TH1F* h_ttbar = new TH1F("h_ttbar","",num,xbins);
  TH1F* h_data = new TH1F("h_data","",num,xbins);


  zjets->Draw(var+">>h_zjets",cut_mc); 
  wjets->Draw(var+">>h_wjets",cut_mc);  
  ttbar->Draw(var+">>h_ttbar",cut_mc);  
  vvjets->Draw(var+">>h_vvjets",cut_mc);  
  singtop->Draw(var+">>h_singtop",cut_mc);  

  data->Draw(+var+">>h_data",cut_data);
  
  if (var == "M_bestmupfjet1_mumu"){ 
   TString var2 = "M_bestmupfjet2_mumu"; 
  TH1F* h2_zjets = new TH1F("h2_zjets","",num,xbins);
  TH1F* h2_wjets = new TH1F("h2_wjets","",num,xbins);
  TH1F* h2_vvjets = new TH1F("h2_vvjets","",num,xbins);
  TH1F* h2_singtop = new TH1F("h2_singtop","",num,xbins);
  TH1F* h2_ttbar = new TH1F("h2_ttbar","",num,xbins);
  TH1F* h2_data = new TH1F("h2_data","",num,xbins);


  zjets->Draw(var2+">>h2_zjets",cut_mc); 
  wjets->Draw(var2+">>h2_wjets",cut_mc);  
  ttbar->Draw(var2+">>h2_ttbar",cut_mc);  
  vvjets->Draw(var2+">>h2_vvjets",cut_mc);  
  singtop->Draw(var2+">>h2_singtop",cut_mc);  
  data->Draw(+var2+">>h2_data",cut_data);
  
  h_zjets->Add(h2_zjets);
  h_wjets->Add(h2_wjets);
  h_ttbar->Add(h2_ttbar);
  h_vvjets->Add(h2_vvjets);
  h_singtop->Add(h2_singtop);
  h_data->Add(h2_data);
  }

  TH1F* H_data  = new TH1F("H_data","",num,xbins);
  TH1F* H_zjets = new TH1F("H_zjets","",num,xbins);
  TH1F* H_wjets = new TH1F("H_wjets","",num,xbins);
  TH1F* H_singtop = new TH1F("H_singtop","",num,xbins);
  TH1F* H_ttbar = new TH1F("H_ttbar","",num,xbins);
  TH1F* H_vvjets = new TH1F("H_vvjets","",num,xbins);
  TH1F* H_bkg   = new TH1F("H_bkg","",num,xbins);
//  TH1F* H_lq   = new TH1F("H_lq","",num,xbins);


  THStack* H_stack = new THStack("H_stack","");

	h_zjets->Scale(znorm);
		Double_t Nd = h_data->Integral();
		Double_t Nmc = h_zjets->Integral()+h_ttbar->Integral()+h_vvjets->Integral()+h_wjets->Integral()+h_singtop->Integral();
		Double_t Nw = h_wjets->Integral();
		Double_t Nt = h_ttbar->Integral();
		Double_t Nz = h_zjets->Integral();
//				Double_t Nlq = h_lq->Integral();

		std::cout<<"Data   : "<<Nd<<std::endl;
		std::cout<<"All MC : "<<Nmc<<std::endl;
    std::cout<<"tt   : "<<h_ttbar->Integral()<<"  +- "<<h_ttbar->Integral()*pow(1.0*(h_ttbar->GetEntries()),-0.5)<<std::endl;
    std::cout<<"z   : "<<h_zjets->Integral()<<"  +- "<<h_zjets->Integral()*pow(1.0*(h_zjets->GetEntries()),-0.5)<<std::endl;
//    std::cout<<"w    : "<<h_wjets->Integral()<<"  +- "<<h_wjets->Integral()*pow(1.0*(h_wjets->GetEntries()),-0.5)<<std::endl;
//    std::cout<<"LQ    : "<<h_lq->Integral()<<"  +- "<<h_lq->Integral()*pow(1.0*(h_lq->GetEntries()),-0.5)<<std::endl;

//		std::cout<<"Ratio  :"<<1.0*(Nd /Nmc)<<"  +-  "<<sqrt(Nd)/Nmc<<std::endl;

float fac =1.0*( ( Nd - (Nmc - Nz) )/Nz );
//float fac =1.0*( Nd/Nmc);
//fac = 1.0;
std::cout<<"MC Scale Factor:  "<<fac<<std::endl;
//	h_wjets->Scale(fac);
//	h_zjets->Scale(fac);
//	h_vvjets->Scale(fac);
//	h_ttbar->Scale(fac);

  H_bkg->Add(h_vvjets);
    H_bkg->Add(h_wjets);
  H_bkg->Add(h_singtop);
  
	H_data->Add(h_data);
//	H_lq->Add(h_lq);
	H_wjets->Add(h_wjets);
	H_zjets->Add(h_zjets);
	H_ttbar->Add(h_ttbar);
	H_singtop->Add(h_singtop);

  H_zjets->SetFillStyle(3004);
  H_ttbar->SetFillStyle(3005);
  H_bkg->SetFillStyle(3008);
  H_wjets->SetFillStyle(3007);
  H_singtop->SetFillStyle(3006 );
//  H_lq->SetFillStyle(0);

  H_zjets->SetFillColor(2);
  H_ttbar->SetFillColor(4);
	H_wjets->SetFillColor(6);
	H_singtop->SetFillColor(3);
  H_bkg->SetFillColor(9);
  
  H_zjets->SetLineColor(2);
  H_ttbar->SetLineColor(4);
  H_wjets->SetLineColor(6);
  H_singtop->SetLineColor(3);
  H_bkg->SetLineColor(9);

//  H_lq->SetMarkerColor(0);    
  H_zjets->SetMarkerColor(2);
  H_wjets->SetMarkerColor(6);
  H_singtop->SetMarkerColor(3);
  H_ttbar->SetMarkerColor(4);
  H_bkg->SetMarkerColor(9);

//	H_lq->SetMarkerSize(1);
	H_zjets->SetMarkerSize(.00000001);
	H_wjets->SetMarkerSize(.00000001);
	H_singtop->SetMarkerSize(.00000001);
	H_ttbar->SetMarkerSize(.00000001);
	H_bkg->SetMarkerSize(.00000001);

//  H_lq->SetLineWidth(2);
  H_zjets->SetLineWidth(2);
  H_wjets->SetLineWidth(2);
  H_singtop->SetLineWidth(2);
  H_ttbar->SetLineWidth(2);
  H_bkg->SetLineWidth(2);
  H_data->SetLineWidth(2);

  H_stack->Add(H_bkg);

//  H_stack->Add(H_singtop);
  H_stack->Add(H_ttbar);
  H_stack->Add(H_zjets);
//  H_stack->Add(H_wjets);
//    H_stack->Add(H_lq);

  H_zjets->GetXaxis()->SetTitle(title);
  H_wjets->GetXaxis()->SetTitle(title);
  H_singtop->GetXaxis()->SetTitle(title);
  H_ttbar->GetXaxis()->SetTitle(title);
  H_data->GetXaxis()->SetTitle(title);
  H_data->GetYaxis()->SetTitle("Number of Events");
  H_data->GetXaxis()->SetTitleFont(132);
  H_data->GetYaxis()->SetTitleFont(132);


  gStyle->SetOptStat(0);
  H_data->Draw("E");

  H_stack->Draw("SAME");
//    H_lq->Draw("SAME");
  H_data->Draw("SAMEE");
  TLegend* leg = new TLegend(0.6,0.63,0.91,0.91,"","brNDC");
  leg->SetTextFont(132);
  leg->SetFillColor(0);
  leg->SetBorderSize(0);
    leg->AddEntry(H_data,"Data 2011, "+Luminosity+" pb^{-1}");
  leg->AddEntry(H_zjets,"Z/#gamma* + jets");
//  leg->AddEntry(H_wjets,"W + jets");
  leg->AddEntry(H_ttbar,"t#bar{t}");
  leg->AddEntry(H_singtop,"Single Top");
  leg->AddEntry(H_bkg,"Other backgrounds");
//    leg->AddEntry(H_lq,"LQ M = 225");
  leg->Draw("SAME");
  c1->SetLogy();

	H_data->SetMinimum(.1);
	H_data->SetMaximum(1.2*extrascalefactor*(H_data->GetMaximum()));

  TLatex* txt =new TLatex(50.0,.3*H_data->GetMaximum(), "CMS 2011 Preliminary");  
  txt->SetTextFont(132); 
  txt->SetTextSize(0.06); 
  txt->Draw();
//  c1->RedrawAxis();

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
	std::cout<<varname<<std::endl;
//  c1->Print("GoodImages/"+varname+"March18_2011_"+tag+".pdf");
  c1->Print("PlotsMuMu/"+varname+"_"+tag+".png");

if (false){

  TH1F* h_bg = new TH1F("h_bg","",num,xbins);
  h_bg->Add(h_zjets);
  h_bg->Add(h_wjets);
  h_bg->Add(h_vvjets);
  h_bg->Add(h_ttbar);
  h_bg->Add(h_singtop);

  int nbinsx = h_bg->GetXaxis()->GetNbins(); 

  int ibin = 0;

  float chi2 = 0.0;
 
  float ndat = 0.0;
  float nbg = 0.0;

  float datmean = 0.0;
	float mcmean = 0.0;

 for (ibin=0;ibin<nbinsx;ibin++){

  ndat = 1.0*(h_data->GetBinContent(ibin));
  nbg = 1.0*(h_bg->GetBinContent(ibin));

  datmean += 1.0*(h_data->GetBinContent(ibin))*h_data->GetBinCenter(ibin);
  mcmean += 1.0*(h_bg->GetBinContent(ibin))*h_bg->GetBinCenter(ibin);

  if (ndat!=0)   chi2 += pow((ndat -nbg),2.0)/pow(ndat,0.5);

//   std::cout<<ndat<<"  "<<nbg<<"  "<<chi2<<std::endl;
    if (nbg>.0010) std::cout<<h_data->GetBinCenter(ibin)<<"   "<<nbg<<"  "<<"   "<<ndat/nbg<<"   "<<(ndat-nbg)/sqrt(ndat)<<std::endl;

}
	datmean = datmean/h_data->Integral();
	mcmean = mcmean/h_bg->Integral();
	std::cout<<datmean<<std::endl;
	std::cout<<mcmean<<std::endl;

  std::cout<<"Chi^2 for this distribution is:  "<< chi2<<std::endl;
  }

}


void MakeVarPlotsMuMu() {


// -------- PF ---------


	TString lumi = "152.8"	;
  TString cut_data = "(Pt_muon1>30)*(Pt_muon2>30)";
  cut_data += "*(Pt_pfjet1>30)*(Pt_pfjet2>30)";
  cut_data += "*(M_muon1muon2>40)";
  cut_data += "*(ST_pf_mumu>250.0)";
  
//    cut_data += "*((M_muon1muon2>80)*(M_muon1muon2<100))";

	TString cut_mc = lumi+ "*weight*("+cut_data+")";


TString filetag = "2011Data_VARBIN";

TString xtag = "[No PU]";

float ZNormalization = 1.16;
	float xbins_muj[12]={0,40,80,120,160,200,240,280,320,360,500,800};
float xbins_st[11]={120,150,180,210,240,270,300,340,400,480,800};

	TString cut_mass_data = cut_data + "*(M_muon1muon2>115)*(ST_pf_mumu>440)";
	TString cut_mass_mc = lumi+ "*weight*("+cut_mass_data+")";

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mass_mc, cut_mass_data, true, 11, xbins_muj, "M_bestmupfjet1_mumu", false, "","M_{#mu j} " +xtag,lumi,10,ZNormalization,filetag);

	TString cut_st_data = cut_data + "*(M_muon1muon2>115)*(ST_pf_mumu>250)";
	TString cut_st_mc = lumi+ "*weight*("+cut_st_data+")";


	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_st_mc, cut_st_data, true, 10, xbins_st, "ST_pf_mumu", false, "","S_{T} (GeV)" +xtag,lumi,50,ZNormalization,filetag);






}
  


