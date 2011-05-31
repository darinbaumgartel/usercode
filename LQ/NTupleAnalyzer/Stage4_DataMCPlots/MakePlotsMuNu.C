
#include "TLorentzVector.h"
#include "TH1.h"
#include <iostream>
#include <fstream>
#include <iomanip>
#include "/home/darinb/CMSStyle.C"

void fillHisto(TString cut_mc, TString cut_data,  bool drawHistograms,  
  	     int nBins, float xLow, float xMax, TString var, bool writeoutput, TString fileName,TString title, TString Luminosity,Double_t extrascalefactor,Double_t wnorm,TString tag) {
  CMSStyle();
//  gStyle->SetOptLogy();
  TH1F* h_zjets = new TH1F("h_zjets","",nBins,xLow,xMax);
  TH1F* h_wjets = new TH1F("h_wjets","",nBins,xLow,xMax);
  TH1F* h_vvjets = new TH1F("h_vvjets","",nBins,xLow,xMax);
  TH1F* h_singtop = new TH1F("h_singtop","",nBins,xLow,xMax);
  TH1F* h_ttbar = new TH1F("h_ttbar","",nBins,xLow,xMax);
  TH1F* h_data = new TH1F("h_data","",nBins,xLow,xMax);
  TH1F* h_lq = new TH1F("h_lq","",nBins,xLow,xMax);


  zjets->Draw(var+">>h_zjets",cut_mc); 
  wjets->Draw(var+">>h_wjets",cut_mc);  
  ttbar->Draw(var+">>h_ttbar",cut_mc);  
  vvjets->Draw(var+">>h_vvjets",cut_mc);  
  singtop->Draw(var+">>h_singtop",cut_mc);  
  lq->Draw(var+">>h_lq",cut_mc);  

  data->Draw(+var+">>h_data",cut_data);

  TH1F* H_data  = new TH1F("H_data","",nBins,xLow,xMax);
  TH1F* H_zjets = new TH1F("H_zjets","",nBins,xLow,xMax);
  TH1F* H_wjets = new TH1F("H_wjets","",nBins,xLow,xMax);
  TH1F* H_singtop = new TH1F("H_singtop","",nBins,xLow,xMax);
  TH1F* H_ttbar = new TH1F("H_ttbar","",nBins,xLow,xMax);
  TH1F* H_vvjets = new TH1F("H_vvjets","",nBins,xLow,xMax);
  TH1F* H_bkg   = new TH1F("H_bkg","",nBins,xLow,xMax);
  TH1F* H_lq   = new TH1F("H_lq","",nBins,xLow,xMax);


  THStack* H_stack = new THStack("H_stack","");

	h_wjets->Scale(wnorm);
		Double_t Nd = h_data->Integral();
		Double_t Nmc = h_zjets->Integral()+h_ttbar->Integral()+h_vvjets->Integral()+h_wjets->Integral()+h_singtop->Integral();
		Double_t Nw = h_wjets->Integral();
		Double_t Nt = h_ttbar->Integral();
		Double_t Nz = h_zjets->Integral();
				Double_t Nlq = h_lq->Integral();

		std::cout<<"Data   : "<<Nd<<std::endl;
		std::cout<<"All MC : "<<Nmc<<std::endl;
    std::cout<<"tt   : "<<h_ttbar->Integral()<<"  +- "<<h_ttbar->Integral()*pow(1.0*(h_ttbar->GetEntries()),-0.5)<<std::endl;
    std::cout<<"w    : "<<h_wjets->Integral()<<"  +- "<<h_wjets->Integral()*pow(1.0*(h_wjets->GetEntries()),-0.5)<<std::endl;
    std::cout<<"LQ    : "<<h_lq->Integral()<<"  +- "<<h_lq->Integral()*pow(1.0*(h_lq->GetEntries()),-0.5)<<std::endl;

//		std::cout<<"Ratio  :"<<1.0*(Nd /Nmc)<<"  +-  "<<sqrt(Nd)/Nmc<<std::endl;

float fac =1.0*( ( Nd - (Nmc - Nw) )/Nw );
//float fac =1.0*( Nd/Nmc);
//fac = 1.0;
std::cout<<"MC Scale Factor:  "<<fac<<std::endl;
//	h_wjets->Scale(fac);
//	h_zjets->Scale(fac);
//	h_vvjets->Scale(fac);
//	h_ttbar->Scale(fac);

  H_bkg->Add(h_vvjets);

	H_data->Add(h_data);
	H_lq->Add(h_lq);
	H_wjets->Add(h_wjets);
	H_zjets->Add(h_zjets);
	H_ttbar->Add(h_ttbar);
	H_singtop->Add(h_singtop);

  H_zjets->SetFillStyle(3004);
  H_ttbar->SetFillStyle(3005);
  H_bkg->SetFillStyle(3008);
  H_wjets->SetFillStyle(3007);
  H_singtop->SetFillStyle(3006 );
  H_lq->SetFillStyle(0);

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

  H_lq->SetMarkerColor(0);    
  H_zjets->SetMarkerColor(2);
  H_wjets->SetMarkerColor(6);
  H_singtop->SetMarkerColor(3);
  H_ttbar->SetMarkerColor(4);
  H_bkg->SetMarkerColor(9);

	H_lq->SetMarkerSize(1);
	H_zjets->SetMarkerSize(.00000001);
	H_wjets->SetMarkerSize(.00000001);
	H_singtop->SetMarkerSize(.00000001);
	H_ttbar->SetMarkerSize(.00000001);
	H_bkg->SetMarkerSize(.00000001);

  H_lq->SetLineWidth(2);
  H_zjets->SetLineWidth(2);
  H_wjets->SetLineWidth(2);
  H_singtop->SetLineWidth(2);
  H_ttbar->SetLineWidth(2);
  H_bkg->SetLineWidth(2);
  H_data->SetLineWidth(2);

  H_stack->Add(H_bkg);
  H_stack->Add(H_zjets);
  H_stack->Add(H_singtop);
  H_stack->Add(H_ttbar);
  H_stack->Add(H_wjets);
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
    H_lq->Draw("SAME");
  H_data->Draw("SAMEE");
  TLegend* leg = new TLegend(0.6,0.63,0.91,0.91,"","brNDC");
  leg->SetTextFont(132);
  leg->SetFillColor(0);
  leg->SetBorderSize(0);
    leg->AddEntry(H_data,"Data 2011, "+Luminosity+" pb^{-1}");
  leg->AddEntry(H_zjets,"Z/#gamma* + jets");
  leg->AddEntry(H_wjets,"W + jets");
  leg->AddEntry(H_ttbar,"t#bar{t}");
  leg->AddEntry(H_singtop,"Single Top");
  leg->AddEntry(H_bkg,"Other backgrounds");
    leg->AddEntry(H_lq,"LQ M = 300");
  leg->Draw("SAME");
  c1->SetLogy();

	H_data->SetMinimum(.1);
	H_data->SetMaximum(1.2*extrascalefactor*(H_data->GetMaximum()));

  TLatex* txt =new TLatex((xMax-xLow)*.02+xLow,.3*H_data->GetMaximum(), "CMS 2011 Preliminary");  
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
  c1->Print("PlotsMuNu/"+varname+"_"+tag+".png");

if (false){

  TH1F* h_bg = new TH1F("h_bg","",nBins,xLow,xMax);
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


void MakePlotsMuNu() {


// -------- PF ---------

	TString lumi = "152.8"	;
  TString cut_data = "(Pt_muon1>35)*(MET_pf>45.0)";
  cut_data += "*(Pt_muon2<30)";
////  TString cut_data = "(Pt_muon1>30)*(Pt_muon2>30)";
////  cut_data += "*(Pt_W<40)*(Pt_W>0)";
//  cut_data += "*(Pt_ele1<-99999.0)";
  cut_data += "*(Pt_pfjet1>30)*(Pt_pfjet2>30)";
  cut_data += "*(abs(Eta_muon1)<2.1)";
  cut_data += "*(ST_pf_munu>250.0)";
  cut_data += "*(abs(deltaPhi_pfjet1pfMET)>.5)";
////  cut_data += "*(deltaPhi_pfjet2pfMET>.5)";
////  cut_data += "*(deltaPhi_pfjet1pfMET<2.65)";
  cut_data += "*(abs(deltaPhi_muon1pfMET)>.8)";

//  cut_data += "*(Phi_muon1>.3)";
//  cut_data += "*(Phi_muon1>.3)";

//  cut_data += "*(NGlobalMuons<2.5)";
//  cut_data += "*(Eta_pfjet1<0.0)";
//  cut_data += "*(Eta_pfjet2<0.0)";

//  cut_data += "&&(deltaPhi_muon1pfMET>2.10)";
//  cut_data += "*(Pt_Clusters_muon1<1.0)";
//  cut_data += "*(abs(MET_pf-Pt_muon1)/(MET_pf)>0.2)";
//  cut_data += "*(PFJetCount<3.5)";
//  cut_data += "*(1.0 - (EcalIso_muon1>0.1)*(HcalIso_muon1>0.1) )";
//  cut_data += "*(BpfJetCount<1.5)";
//  cut_data += "*((N_Vertices>2.5)||(N_Vertices<1.5))";
//  cut_data += "*(ST_pf_munu>340.0)";
//  cut_data += "*(Pt_muon1>85)*(MET_pf>85.0)";
//  cut_data += "*(MT_muon1pfMET>125.0)";


//  cut_data +="*(deltaR_muon1closestPFJet>.7)";
//  cut_data += "*(deltaPhi_muon1caloMET<2.85)";
//  cut_data += "*(BpfJetCount>1.5)";
//  cut_data += "*(MT_muon1pfMET>125.0)";
//  cut_data += "*(MT_muon1pfMET<110.0)";
//  cut_data += "*(MT_muon1pfMET>50.0)";

	TString cut_mc = lumi+ "*weight*("+cut_data+")";



TString filetag = "2011Data_Preselection";

TString xtag = "[No PU]";

float WNormalization = 1.36;

//	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
//  fillHisto(cut_mc, cut_data, true, 4000,0,4000, "MT_muon1pfMET", false, "","M^{T}_{#mu#nu}(GeV) " +xtag,lumi,10,WNormalization,filetag);


	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data ,true,27,.-.5,9.5, "N_Vertices", false, "","N_{Vertices} " +xtag,lumi,10000,WNormalization,filetag);

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 40,0,400, "MT_muon1pfMET", false, "","M^{T}_{#mu#nu}(GeV) " +xtag,lumi,10,WNormalization,filetag);


	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 50,0,5, "EcalIso_muon1", false, "","ECAL Iso_{#mu} (GeV) " +xtag,lumi,10,WNormalization,filetag+"Large");

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 50,0,30, "HcalIso_muon1", false, "","HCAL Iso (#mu) " +xtag,lumi,10,WNormalization,filetag+"Large");

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 40,0,40, "TrkIso_muon1", false, "","Track Iso (#mu) " +xtag,lumi,10,WNormalization,filetag+"Large");

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 50,0,5, "EcalIso_muon1", false, "","ECAL Iso_{#mu} (GeV) " +xtag,lumi,10,WNormalization,filetag);

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 50,0,3, "HcalIso_muon1", false, "","HCAL Iso (#mu) " +xtag,lumi,10,WNormalization,filetag);

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 50,0,10, "TrkIso_muon1", false, "","Track Iso (#mu) " +xtag,lumi,10,WNormalization,filetag);


	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 50,0,500, "MET_pf",        false, "","E_{T}^{miss}(GeV) " +xtag  ,lumi,10,WNormalization,filetag);

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 42,-2.1,2.1, "Eta_muon1", false, "","#eta (#mu) " +xtag,lumi,100,WNormalization,filetag);

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true,20,-3.141593,3.141593, "Phi_muon1", false, "","#phi (#mu) " +xtag,lumi,200,WNormalization,filetag);

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 20,.8,3.15,"deltaPhi_muon1pfMET", false, "","#Delta #phi (#mu,E_{T}^{miss}) " +xtag,lumi,100,WNormalization,filetag);

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 40,200,1000, "ST_pf_munu", false, "","S_{T} (GeV)" +xtag,lumi,50,WNormalization,filetag);

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 40,0,400, "Pt_muon1", false, "","p_{T} (#mu) (GeV) " +xtag,lumi,10,WNormalization,filetag);

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 50,0,500, "Pt_pfjet1", false, "","p_{T} (jet_{1}) (GeV) " +xtag,lumi,10,WNormalization,filetag);

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 50,0,500, "Pt_pfjet2", false, "","p_{T} (jet_{2}) (GeV) " +xtag,lumi,10,WNormalization,filetag);

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 60,-3.0,3.0, "Eta_pfjet1", false, "","#eta (jet_{1}) " +xtag,lumi,100,WNormalization,filetag);

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 60,-3.0,3.0, "Eta_pfjet2", false, "","#eta (jet_{2}) " +xtag,lumi,100,WNormalization,filetag);

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mc, cut_data, true, 40,0,800, "M_bestmupfjet_munu", false, "","M_{#mu jet} " +xtag,lumi,100,WNormalization,filetag);




   
   filetag = "2011Data_FullSelection";

	TString cut_mass_data = cut_data + "*(MT_muon1pfMET>125.0)*(Pt_muon1>85)*(MET_pf>85.0)*(ST_pf_munu>485)";
	TString cut_mass_mc = lumi+ "*weight*("+cut_mass_data+")";

	TString cut_st_data = cut_data + "*(MT_muon1pfMET>125.0)*(Pt_muon1>85)*(MET_pf>85.0)*(ST_pf_munu>250)";
	TString cut_st_mc = lumi+ "*weight*("+cut_st_data+")";

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_mass_mc, cut_mass_data, true, 20,0.0,800.0, "M_bestmupfjet_munu", false, "","M_{#mu j} " +xtag,lumi,40,WNormalization,filetag);

	gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
  fillHisto(cut_st_mc, cut_st_data, true, 20,0,1000, "ST_pf_munu", false, "","S_{T} (GeV)" +xtag,lumi,50,WNormalization,filetag);





}
  


