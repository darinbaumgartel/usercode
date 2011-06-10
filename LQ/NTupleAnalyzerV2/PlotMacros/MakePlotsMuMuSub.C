
#include "TLorentzVector.h"
#include "TH1.h"
#include <iostream>
#include <fstream>
#include <iomanip>
#include "/home/darinb/CMSStyle.C"

void fillHisto(TString cut_mc, TString cut_data,  bool drawHistograms,
int nBins, float xLow, float xMax, TString var, bool writeoutput, TString fileName,TString title, TString Luminosity,Double_t extrascalefactor,Double_t znorm,TString tag)
{
	CMSStyle();
	//  TCanvas c1("c1", "First canvas", 400, 300); // problems here
	//	c1->Divide(1,2);

	TCanvas *c1 = new TCanvas("c1","Example 2 pads (20,80)",800,800);
	TPad *pad1 = new TPad("pad1", "The pad 80% of the height",0.0,0.3,1.0,1.0,0);
	TPad *pad2 = new TPad("pad2", "The pad 20% of the height",0.0,0.0,1.0,0.3,0);
	pad1->Draw();
	pad2->Draw();
	pad1->cd();
	pad1->SetLogy();

	gStyle->SetOptLogy();
	TH1F* h_zjets = new TH1F("h_zjets","",nBins,xLow,xMax);
	TH1F* h_wjets = new TH1F("h_wjets","",nBins,xLow,xMax);
	TH1F* h_vvjets = new TH1F("h_vvjets","",nBins,xLow,xMax);
	TH1F* h_singtop = new TH1F("h_singtop","",nBins,xLow,xMax);
	TH1F* h_qcd = new TH1F("h_qcd","",nBins,xLow,xMax);
	TH1F* h_ttbar = new TH1F("h_ttbar","",nBins,xLow,xMax);
	TH1F* h_data = new TH1F("h_data","",nBins,xLow,xMax);
	//TH1F* h_lqmumu = new TH1F("h_lqmumu","",nBins,xLow,xMax);

	zjets->Draw(var+">>h_zjets",cut_mc);
	wjets->Draw(var+">>h_wjets",cut_mc);
	ttbar->Draw(var+">>h_ttbar",cut_mc);
	vvjets->Draw(var+">>h_vvjets",cut_mc);
	singtop->Draw(var+">>h_singtop",cut_mc);
	qcd->Draw(var+">>h_qcd",cut_mc);
	//lqmumu->Draw(var+">>h_lqmumu",cut_mc);

	data->Draw(+var+">>h_data",cut_data);

	if (var == "M_bestmupfjet1_mumu")
	{
		// Make histograms for second LQ mass in event and add to first
		TString var2 = "M_bestmupfjet2_mumu";
		TH1F* h2_zjets = new TH1F("h2_zjets","",nBins,xLow,xMax);
		TH1F* h2_wjets = new TH1F("h2_wjets","",nBins,xLow,xMax);
		TH1F* h2_vvjets = new TH1F("h2_vvjets","",nBins,xLow,xMax);
		TH1F* h2_singtop = new TH1F("h2_singtop","",nBins,xLow,xMax);
		TH1F* h2_qcd = new TH1F("h2_qcd","",nBins,xLow,xMax);
		TH1F* h2_ttbar = new TH1F("h2_ttbar","",nBins,xLow,xMax);
		TH1F* h2_data = new TH1F("h2_data","",nBins,xLow,xMax);
		//TH1F* h2_lqmumu = new TH1F("h2_lqmumu","",nBins,xLow,xMax);

		zjets->Draw(var2+">>h2_zjets",cut_mc);
		wjets->Draw(var2+">>h2_wjets",cut_mc);
		ttbar->Draw(var2+">>h2_ttbar",cut_mc);
		vvjets->Draw(var2+">>h2_vvjets",cut_mc);
		singtop->Draw(var2+">>h2_singtop",cut_mc);
		qcd->Draw(var2+">>h2_qcd",cut_mc);
		data->Draw(+var2+">>h2_data",cut_data);
		//lqmumu->Draw(var2+">>h2_lqmumu",cut_mc);

		h_zjets->Add(h2_zjets);
		h_wjets->Add(h2_wjets);
		h_ttbar->Add(h2_ttbar);
		h_vvjets->Add(h2_vvjets);
		h_singtop->Add(h2_singtop);
		h_singtop->Add(h2_qcd);
		h_data->Add(h2_data);
		//h_lqmumu->Add(h2_lqmumu);

		// Rename variable
		var = "M_bestmupfjetcombo_mumu";
	}

	TH1F* H_data  = new TH1F("H_data","",nBins,xLow,xMax);
	TH1F* H_zjets = new TH1F("H_zjets","",nBins,xLow,xMax);
	TH1F* H_wjets = new TH1F("H_wjets","",nBins,xLow,xMax);
	TH1F* H_singtop = new TH1F("H_singtop","",nBins,xLow,xMax);
	TH1F* H_qcd = new TH1F("H_qcd","",nBins,xLow,xMax);
	TH1F* H_ttbar = new TH1F("H_ttbar","",nBins,xLow,xMax);
	TH1F* H_vvjets = new TH1F("H_vvjets","",nBins,xLow,xMax);
	TH1F* H_bkg   = new TH1F("H_bkg","",nBins,xLow,xMax);
	//TH1F* H_lqmumu   = new TH1F("H_lqmumu","",nBins,xLow,xMax);

	THStack* H_stack = new THStack("H_stack","");

	h_zjets->Scale(znorm);
	h_ttbar->Scale(165.0/121.0);

	Double_t Nd = h_data->Integral();
	Double_t Nmc = h_zjets->Integral()+h_ttbar->Integral()+h_vvjets->Integral()+h_wjets->Integral()+h_singtop->Integral()+h_qcd->Integral();
	Double_t Nw = h_wjets->Integral();
	Double_t Nz = h_zjets->Integral();

	std::cout<<"Data   : "<<Nd<<std::endl;
	std::cout<<"All MC : "<<Nmc<<std::endl;
	std::cout<<"tt   : "<<h_ttbar->Integral()<<"  +- "<<h_ttbar->Integral()*pow(1.0*(h_ttbar->GetEntries()),-0.5)<<std::endl;
	std::cout<<"z   : "<<h_zjets->Integral()<<"  +- "<<h_zjets->Integral()*pow(1.0*(h_zjets->GetEntries()),-0.5)<<std::endl;

	float fac =1.0*( ( Nd - (Nmc - Nz) )/Nz );

	std::cout<<"Z Scale Factor:  "<<fac<<std::endl;

	H_bkg->Add(h_vvjets);
	H_bkg->Add(h_wjets);
	H_bkg->Add(h_singtop);
	H_bkg->Add(h_qcd);

	H_data->Add(h_data);
	//H_lqmumu->Add(h_lqmumu);
	H_wjets->Add(h_wjets);
	H_zjets->Add(h_zjets);
	H_ttbar->Add(h_ttbar);
	H_singtop->Add(h_singtop);
	H_qcd->Add(h_qcd);

	H_zjets->SetFillStyle(3004);
	H_ttbar->SetFillStyle(3005);
	H_bkg->SetFillStyle(3008);
	H_wjets->SetFillStyle(3007);
	H_singtop->SetFillStyle(3006 );
	H_qcd->SetFillStyle(3006 );
	//H_lqmumu->SetFillStyle(0);

	H_zjets->SetFillColor(2);
	H_ttbar->SetFillColor(4);
	H_wjets->SetFillColor(6);
	H_singtop->SetFillColor(3);
	H_qcd->SetFillColor(3);
	H_bkg->SetFillColor(9);

	H_zjets->SetLineColor(2);
	H_ttbar->SetLineColor(4);
	H_wjets->SetLineColor(6);
	H_singtop->SetLineColor(3);
	H_qcd->SetLineColor(3);
	H_bkg->SetLineColor(9);

	//H_lqmumu->SetMarkerColor(0);
	H_zjets->SetMarkerColor(2);
	H_wjets->SetMarkerColor(6);
	H_singtop->SetMarkerColor(3);
	H_qcd->SetMarkerColor(3);
	H_ttbar->SetMarkerColor(4);
	H_bkg->SetMarkerColor(9);

	//H_lqmumu->SetMarkerSize(1);
	H_zjets->SetMarkerSize(.00000001);
	H_wjets->SetMarkerSize(.00000001);
	H_singtop->SetMarkerSize(.00000001);
	H_qcd->SetMarkerSize(.00000001);
	H_ttbar->SetMarkerSize(.00000001);
	H_bkg->SetMarkerSize(.00000001);

	//H_lqmumu->SetLineWidth(2);
	H_zjets->SetLineWidth(2);
	H_wjets->SetLineWidth(2);
	H_singtop->SetLineWidth(2);
	H_qcd->SetLineWidth(2);
	H_ttbar->SetLineWidth(2);
	H_bkg->SetLineWidth(2);
	H_data->SetLineWidth(2);

	H_stack->Add(H_bkg);

	//  H_stack->Add(H_singtop);
	//  H_stack->Add(H_qcd);
	H_stack->Add(H_ttbar);
	H_stack->Add(H_zjets);
	//  H_stack->Add(H_wjets);
	//    H_stack->Add(H_lqmumu);

	H_zjets->GetXaxis()->SetTitle(title);
	H_wjets->GetXaxis()->SetTitle(title);
	H_singtop->GetXaxis()->SetTitle(title);
	H_qcd->GetXaxis()->SetTitle(title);
	H_ttbar->GetXaxis()->SetTitle(title);
	H_data->GetXaxis()->SetTitle(title);
	H_data->GetYaxis()->SetTitle("Number of Events");
	H_data->GetXaxis()->SetTitleFont(132);
	H_data->GetYaxis()->SetTitleFont(132);

	gStyle->SetOptStat(0);
	H_data->Draw("E");

	H_stack->Draw("SAME");
	//H_lqmumu->Draw("SAME");
	H_data->Draw("SAMEE");
	TLegend* leg = new TLegend(0.6,0.63,0.91,0.91,"","brNDC");
	leg->SetTextFont(132);
	leg->SetFillColor(0);
	leg->SetBorderSize(0);
	leg->AddEntry(H_data,"Data 2011, "+Luminosity+" pb^{-1}");
	leg->AddEntry(H_zjets,"Z/#gamma* + jets");
	leg->AddEntry(H_ttbar,"t#bar{t}");
	leg->AddEntry(H_bkg,"Other backgrounds");
	//leg->AddEntry(H_lqmumu,"LQ M = 400");
	leg->Draw("SAME");
	//  gPad->SetLogy();

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
	while ( (pos = str.find(searchString, pos)) != string::npos )
	{
		str.replace( pos, searchString.size(), replaceString );
		pos++;
	}

	TString varname = var;
	varname +="_";
	varname += str;
	std::cout<<varname<<std::endl;

	pad2->cd();

	TH1F* h_comp = new TH1F("h_comp","",nBins,xLow,xMax);
	TH1F* h_zero = new TH1F("h_zero","",nBins,xLow,xMax);
	TH1F* h_2p = new TH1F("h_2p","",nBins,xLow,xMax);
	TH1F* h_2m = new TH1F("h_2m","",nBins,xLow,xMax);

	if (true)
	{

		TH1F* h_bg = new TH1F("h_bg","",nBins,xLow,xMax);
		h_bg->Add(h_zjets);
		h_bg->Add(h_wjets);
		h_bg->Add(h_vvjets);
		h_bg->Add(h_ttbar);
		h_bg->Add(h_singtop);
		h_bg->Add(h_qcd);

		int nbinsx = h_bg->GetXaxis()->GetNbins();

		int ibin = 0;

		float chi2 = 0.0;

		float ndat = 0.0;
		float nbg = 0.0;

		float datmean = 0.0;
		float mcmean = 0.0;

		float xminl = 0;
		float xmaxl = 0;

		for (ibin=0;ibin<nbinsx;ibin++)
		{
			ndat = 1.0*(h_data->GetBinContent(ibin));
			nbg = 1.0*(h_bg->GetBinContent(ibin));
			datmean += 1.0*(h_data->GetBinContent(ibin))*h_data->GetBinCenter(ibin);

			mcmean += 1.0*(h_bg->GetBinContent(ibin))*h_bg->GetBinCenter(ibin);
			if (ndat!=0)   chi2 += pow((ndat -nbg),2.0)/pow(ndat,0.5);
			//if (nbg>.0010) std::cout<<h_data->GetBinCenter(ibin)<<"   "<<nbg<<"  "<<"   "<<ndat/nbg<<"   "<<(ndat-nbg)/sqrt(ndat)<<std::endl;
			if (ndat!=0) h_comp ->SetBinContent(ibin, (ndat - nbg)/sqrt(ndat) );
			if ((ndat!=0)&&(abs((ndat - nbg)/sqrt(ndat))>7.99 )) h_comp ->SetBinContent(ibin, 7.95*(ndat>nbg) - 7.95*(ndat<nbg));

		}

		std::cout<<"Chi^2 for this distribution is:  "<< chi2<<std::endl;
	}
	h_comp->GetYaxis()->SetTitle("Poisson N(#sigma) Diff");

	TLine *line0 = new TLine(xLow,0,xMax,0);
	TLine *line2u = new TLine(xLow,2,xMax,2);
	TLine *line2d = new TLine(xLow,-2,xMax,-2);

	h_comp->SetMinimum(-8);
	h_comp->SetMaximum(8);

	h_comp->Draw("p");
	line0->Draw("SAME");
	line2u->Draw("SAME");
	line2d->Draw("SAME");

	c1->Print("PlotsMuMuSub/"+varname+"_"+tag+".png");

}


void MakePlotsMuMuSub()
{

	// -------- PF ---------

	TString lumi = "341"  ;
	TString cut_data = "(Pt_muon1>40)*(Pt_muon2>30)";
	cut_data += "*(Pt_pfjet1>30)*(Pt_pfjet2>30)";
	cut_data += "*(M_muon1muon2>50)";
	cut_data += "*(ST_pf_mumu>250.0)";
	cut_data += "*(deltaR_muon1muon2>0.3)";
	cut_data += "*((abs(Eta_muon1)<2.1)||(abs(Eta_muon2)<2.1))";

	//cut_data += "*((M_muon1muon2>80)*(M_muon1muon2<100))";

	TString cut_mc = lumi+ "*weight*("+cut_data+")";
	cut_mc += "*(";
	cut_mc += "((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)*(0.232372731979))+";
	cut_mc += "((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)*(0.388956765388))+";
	cut_mc += "((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)*(0.884414938239))+";
	cut_mc += "((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)*(1.46191420958))+";
	cut_mc += "((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)*(1.91558522504))+";
	cut_mc += "((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)*(2.10231560025))+";
	cut_mc += "((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)*(2.00226419099))+";
	cut_mc += "((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)*(1.69652354267))+";
	cut_mc += "((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)*(1.30237189409))+";
	cut_mc += "((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)*(0.918437621623))+";
	cut_mc += "((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)*(0.601389960578))+";
	cut_mc += "((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)*(0.408547720502))+";
	cut_mc += "((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)*(0.282624064065))+";
	cut_mc += "((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)*(0.202614175963))+";
	cut_mc += "((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)*(0.14549324601))+";
	cut_mc += "((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)*(0.109602575187))+";
	cut_mc += "((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)*(0.0837977032697))+";
	cut_mc += "((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)*(0.0655930196444))+";
	cut_mc += "((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)*(0.0527469263172))+";
	cut_mc += "((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)*(0.0450732335015))+";
	cut_mc += "((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)*(0.0357775262413))+";
	cut_mc += "((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)*(0.0342231287046))+";
	cut_mc += "((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)*(0.0281747681069))+";
	cut_mc += "((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)*(0.0238662341278))+";
	cut_mc += "((N_PileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)*(0.0204890829612))";
	cut_mc += ")";

	TString filetag = "2011Data_PreSelection";

	TString xtag = " [preselection]";

	float ZNormalization = 1.33;

	//gROOT->Reset();	gROOT->ProcessLine(".x LoadLocal.C");
	//fillHisto(cut_mc, cut_data, true, 4000,40,4040, "M_muon1muon2", false, "","M_{#mu#mu}(GeV) " +xtag,lumi,10,ZNormalization,filetag);

	//gROOT->Reset();	gROOT->ProcessLine(".q;");

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 60,40,340, "M_muon1muon2", false, "","M_{#mu#mu}(GeV) " +xtag,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data ,true,25,.-.5,24.5, "N_Vertices", false, "","N_{Vertices} " +xtag,lumi,100,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data ,true,6,.-.5,5.5, "GlobalMuonCount", false, "","N_{Global #mu} " +xtag,lumi,100,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data ,true,6,.-.5,5.5, "TrackerMuonCount", false, "","N_{Tracker #mu} " +xtag,lumi,100,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data ,true,12,.-.5,11.5, "PFJetCount", false, "","N_{PFJet} " +xtag,lumi,100,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data ,true,8,.-.5,7.5, "BpfJetCount", false, "","N_{BPFJet} " +xtag,lumi,100,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 60,0,30, "EcalIso_muon1", false, "","ECAL Iso_{#mu_{1}} (GeV) " +xtag,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 50,0,3, "HcalIso_muon1", false, "","HCAL Iso (#mu_{1}) " +xtag,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 35,0,3.5, "TrkIso_muon1", false, "","Track Iso (#mu_{1}) " +xtag,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 50,0,500, "Pt_muon1", false, "","p_{T} (#mu_{1}) (GeV) " +xtag,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 50,0,50, "PtError_muon1", false, "","#sigma(p_{T}) (#mu_{1}) (GeV) " +xtag,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 42,-2.1,2.1, "Eta_muon1", false, "","#eta (#mu_{1}) " +xtag,lumi,1000,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 50,0,.001, "EtaError_muon1", false, "","#sigma(#eta) (#mu_{1}) " +xtag,lumi,1000,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true,30,-3.141593,3.141593, "Phi_muon1", false, "","#phi (#mu_{1}) " +xtag,lumi,2000,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 50,0,.0005, "PhiError_muon1", false, "","#sigma(#phi) (#mu_{1}) " +xtag,lumi,1000,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 40,0,.0008, "QOverPError_muon1", false, "","#sigma(Q/p)_{#mu_{1}}(GeV) " +xtag,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 60,0,30, "EcalIso_muon2", false, "","ECAL Iso_{#mu_{2}} (GeV) " +xtag,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 50,0,3, "HcalIso_muon2", false, "","HCAL Iso (#mu_{2}) " +xtag,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 35,0,3.5, "TrkIso_muon2", false, "","Track Iso (#mu_{2}) " +xtag,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 40,0,400, "Pt_muon2", false, "","p_{T} (#mu_{2}) (GeV) " +xtag,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 50,0,50, "PtError_muon2", false, "","#sigma(p_{T}) (#mu_{2}) (GeV) " +xtag,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 42,-2.1,2.1, "Eta_muon2", false, "","#eta (#mu_{2}) " +xtag,lumi,1000,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 50,0,.001, "EtaError_muon2", false, "","#sigma(#eta) (#mu_{2}) " +xtag,lumi,1000,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true,30,-3.141593,3.141593, "Phi_muon2", false, "","#phi (#mu_{2}) " +xtag,lumi,2000,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 50,0,.0005, "PhiError_muon2", false, "","#sigma(#phi) (#mu_{2}) " +xtag,lumi,1000,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 40,0,.0008, "QOverPError_muon2", false, "","#sigma(Q/p)_{#mu_{2}}(GeV) " +xtag,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 60,0,300, "MET_pf",        false, "","E_{T}^{miss}(GeV) " +xtag  ,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 65,200,1500, "ST_pf_mumu", false, "","S_{T} (GeV)" +xtag,lumi,50,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 60,0,600, "Pt_pfjet1", false, "","p_{T} (jet_{1}) (GeV) " +xtag,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 50,0,500, "Pt_pfjet2", false, "","p_{T} (jet_{2}) (GeV) " +xtag,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 40,-3.0,3.0, "Eta_pfjet1", false, "","#eta (jet_{1}) " +xtag,lumi,100,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 40,-3.0,3.0, "Eta_pfjet2", false, "","#eta (jet_{2}) " +xtag,lumi,100,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 63,-3.15,3.15, "deltaPhi_muon1pfjet1", false, "","#Delta#phi (#mu_{1}, j_{1}) " +xtag,lumi,100,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 63,-3.15,3.15, "deltaPhi_muon1pfjet2", false, "","#Delta#phi (#mu_{1}, j_{2}) " +xtag,lumi,100,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 63,-3.15,3.15, "deltaPhi_muon2pfjet1", false, "","#Delta#phi (#mu_{2}, j_{1}) " +xtag,lumi,100,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 63,-3.15,3.15, "deltaPhi_muon2pfjet2", false, "","#Delta#phi (#mu_{2}, j_{2}) " +xtag,lumi,100,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 60,0,6, "deltaR_muon1pfjet1", false, "","#Delta R (#mu_{1}, j_{1}) " +xtag,lumi,100,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 60,0,6, "deltaR_muon1pfjet2", false, "","#Delta R (#mu_{1}, j_{2}) " +xtag,lumi,100,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 60,0,6, "deltaR_muon2pfjet1", false, "","#Delta R (#mu_{2}, j_{1}) " +xtag,lumi,100,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 60,0,6, "deltaR_muon2pfjet2", false, "","#Delta R (#mu_{2}, j_{2}) " +xtag,lumi,100,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mc, cut_data, true, 100,0,2000, "M_bestmupfjet1_mumu", false, "","M_{#mu jet} " +xtag,lumi,100,ZNormalization,filetag);

	// Full Selection Plots Below

	filetag = "2011Data_FullSelection";

	xtag = " [full selection]";

	TString cut_mass_data = cut_data + "*(M_muon1muon2>115)*(ST_pf_mumu>440)";
	TString cut_mass_mc = lumi+ "*weight*("+cut_mass_data+")";

	TString cut_st_data = cut_data + "*(M_muon1muon2>115)*(ST_pf_mumu>250)";
	TString cut_st_mc = lumi+ "*weight*("+cut_st_data+")";

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_mass_mc, cut_mass_data, true, 40,0.0,2000.0, "M_bestmupfjet1_mumu", false, "","M_{#mu j} " +xtag,lumi,10,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".x LoadLocal.C");
	fillHisto(cut_st_mc, cut_st_data, true, 30,200,1700, "ST_pf_mumu", false, "","S_{T} (GeV)" +xtag,lumi,50,ZNormalization,filetag);

	gROOT->Reset(); gROOT->ProcessLine(".q;");
}