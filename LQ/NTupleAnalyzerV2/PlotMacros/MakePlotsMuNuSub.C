
#include"TLorentzVector.h"
#include"TH1.h"
#include <iostream>
#include <fstream>
#include <iomanip>
#include"CMSStyle.C"

void fillHisto(TString cut_mc, TString cut_data,  bool drawHistograms,
int nBins, float xLow, float xMax, TString var, bool writeoutput, TString fileName,TString title, TString Luminosity,Double_t extrascalefactor,Double_t wnorm,TString tag)
{
	CMSStyle();
	//  TCanvas c1("c1","First canvas", 400, 300); // problems here
	//	c1->Divide(1,2);

	std::cout<<"\n Looking at variable:  "<<var<<"  \n"<<std::endl;

	TIter next(PhysicalVariables->GetListOfBranches());
	TObject* obj;
	bool usevar = false;
	while(obj= (TObject*)next()){
			if (var == obj->GetName()) usevar = true;
	}
	//std::cout<<usevar<<std::endl;
	if (!usevar) 
	{
		std::cout<<"\nWARNING: Branch for variable "<<var<<"  not found. Skipping plot for this variable. \n"<<std::endl;
		return;
	}

	TCanvas *c1 = new TCanvas("c1","",800,800);
	TPad *pad1 = new TPad("pad1","The pad 60% of the height",0.0,0.4,1.0,1.0,0);
	TPad *pad2 = new TPad("pad2","The pad 20% of the height",0.0,0.2,1.0,0.4,0);
	TPad *pad2r = new TPad("pad2r","The pad 20% of the height",0.0,0.0,1.0,0.2,0);
   //pad2->SetFillStyle(4000); //will be transparent
   //pad2r->SetFillStyle(4000); //will be transparent

	pad1->Draw();
	pad2->Draw();
	pad2r->Draw();

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
	TH1F* h_lq = new TH1F("h_lq","",nBins,xLow,xMax);

	zjets->Draw(var+">>h_zjets",cut_mc);
	wjets->Draw(var+">>h_wjets",cut_mc);
	ttbar->Draw(var+">>h_ttbar",cut_mc);
	vvjets->Draw(var+">>h_vvjets",cut_mc);
	singtop->Draw(var+">>h_singtop",cut_mc);
	qcd->Draw(var+">>h_qcd",cut_mc);
	lqmunu->Draw(var+">>h_lq",cut_mc);

	data->Draw(+var+">>h_data",cut_data);

	TH1F* H_data  = new TH1F("H_data","",nBins,xLow,xMax);
	TH1F* H_zjets = new TH1F("H_zjets","",nBins,xLow,xMax);
	TH1F* H_wjets = new TH1F("H_wjets","",nBins,xLow,xMax);
	TH1F* H_singtop = new TH1F("H_singtop","",nBins,xLow,xMax);
	TH1F* H_qcd = new TH1F("H_qcd","",nBins,xLow,xMax);
	TH1F* H_ttbar = new TH1F("H_ttbar","",nBins,xLow,xMax);
	TH1F* H_vvjets = new TH1F("H_vvjets","",nBins,xLow,xMax);
	TH1F* H_bkg   = new TH1F("H_bkg","",nBins,xLow,xMax);
	TH1F* H_lq   = new TH1F("H_lq","",nBins,xLow,xMax);

	THStack* H_stack = new THStack("H_stack","");

	// ******************************************************************************************************************************* //
	// Rescaling Routine and Event number Readout
	
	h_wjets->Scale(wnorm);
	h_ttbar->Scale(165.0/121.0);


	Double_t Nd = h_data->Integral();
	Double_t Nmc = h_zjets->Integral()+h_ttbar->Integral()+h_vvjets->Integral()+h_wjets->Integral()+h_singtop->Integral()+h_qcd->Integral();
	Double_t Nw = h_wjets->Integral();
	Double_t Nt = h_ttbar->Integral();
	Double_t Nz = h_zjets->Integral();
	Double_t Nlq = h_lq->Integral();
	Double_t N_other = Nmc - Nw;

	
	Double_t sigma_Nw = Nw*pow(1.0*(h_wjets->GetEntries()),-0.5);

	Double_t sigma_N_other = 0.0;
	if (h_ttbar->GetEntries()>0) sigma_N_other += h_ttbar->Integral()*pow((1.0*h_ttbar->GetEntries()),-0.5);
	if (h_zjets->GetEntries()>0) sigma_N_other += h_wjets->Integral()*pow((1.0*h_zjets->GetEntries() ),-0.5);
	if (h_vvjets->GetEntries()>0) sigma_N_other += h_vvjets->Integral()*pow((1.0*h_vvjets->GetEntries() ),-0.5);
	if (h_singtop->GetEntries()>0) sigma_N_other += h_singtop->Integral()*pow((1.0*singtop->GetEntries()),-0.5); 
	if (h_qcd->GetEntries()>0) sigma_N_other += h_qcd->Integral()*pow((1.0*h_qcd->GetEntries()),-0.5);

	Double_t sigam_Nd = sqrt(Nd);


	std::cout<<"Data   :"<<Nd<<std::endl;
	std::cout<<"All MC :"<<Nmc<<std::endl;
	std::cout<<"tt   :"<<h_ttbar->Integral()<<"  +-"<<h_ttbar->Integral()*pow(1.0*(h_ttbar->GetEntries()),-0.5)<<std::endl;
	std::cout<<"w    :"<<h_wjets->Integral()<<"  +-"<<h_wjets->Integral()*pow(1.0*(h_wjets->GetEntries()),-0.5)<<std::endl;
	std::cout<<"LQ    :"<<h_lq->Integral()<<"  +-"<<h_lq->Integral()*pow(1.0*(h_lq->GetEntries()),-0.5)<<std::endl;
	
	
	Double_t fac_Numerator = Nd - N_other;
	Double_t fac_Denominator = Nw;
	Double_t fac = fac_Numerator/fac_Denominator;

	Double_t sigma_fac_Numerator = sqrt( pow( sigam_Nd ,2.0) + pow( sigma_N_other ,2.0) ) ;
	Double_t sigma_fac_Denominator = sigma_Nw; 
	Double_t sigma_fac_over_fac = pow( pow((sigma_fac_Numerator/fac_Numerator),2.0)    +  pow((sigma_fac_Denominator/fac_Denominator),2.0)    ,0.5);
	Double_t sigma_fac = sigma_fac_over_fac*fac;

	std::cout<<"W Scale Factor:  "<<fac<<"  +-  "<<sigma_fac<<std::endl;
	
	// *******************************************************************************************************************************
	

	H_bkg->Add(h_vvjets);
	H_bkg->Add(h_qcd);

	H_data->Add(h_data);
	H_lq->Add(h_lq);
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
	H_qcd->SetFillStyle(3013);
	H_lq->SetFillStyle(0);

	H_zjets->SetFillColor(2);
	H_ttbar->SetFillColor(4);
	H_wjets->SetFillColor(6);
	H_singtop->SetFillColor(3);
	H_qcd->SetFillColor(11);
	H_bkg->SetFillColor(9);

	H_lq->SetLineStyle(3);
	H_lq->SetLineColor(1);
	H_zjets->SetLineColor(2);
	H_ttbar->SetLineColor(4);
	H_wjets->SetLineColor(6);
	H_singtop->SetLineColor(3);
	H_qcd->SetLineColor(11);
	H_bkg->SetLineColor(9);

	H_lq->SetMarkerColor(1);
	H_zjets->SetMarkerColor(2);
	H_wjets->SetMarkerColor(6);
	H_singtop->SetMarkerColor(3);
	H_qcd->SetMarkerColor(11);
	H_ttbar->SetMarkerColor(4);
	H_bkg->SetMarkerColor(9);

	H_lq->SetMarkerSize(.00000001);
	H_zjets->SetMarkerSize(.00000001);
	H_wjets->SetMarkerSize(.00000001);
	H_singtop->SetMarkerSize(.00000001);
	H_qcd->SetMarkerSize(.00000001);
	H_ttbar->SetMarkerSize(.00000001);
	H_bkg->SetMarkerSize(.00000001);

	H_lq->SetLineWidth(3);
	H_zjets->SetLineWidth(2);
	H_wjets->SetLineWidth(2);
	H_singtop->SetLineWidth(2);
	H_qcd->SetLineWidth(2);
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
	H_qcd->GetXaxis()->SetTitle(title);
	H_ttbar->GetXaxis()->SetTitle(title);
	H_data->GetXaxis()->SetTitle(title);
	H_data->GetYaxis()->SetTitle("Number of Events");
	H_data->GetXaxis()->SetTitleFont(132);
	H_data->GetYaxis()->SetTitleFont(132);

	H_data->SetMarkerStyle(21);
	H_data->SetMarkerSize(0.0);
	gStyle->SetOptStat(0);
	H_data->Draw("E");

	H_stack->Draw("SAME");
	H_lq->Draw("SAME");
	H_data->Draw("SAMEE");
	TLegend* leg = new TLegend(0.6,0.63,0.91,0.91,"","brNDC");
	leg->SetTextFont(132);
	leg->SetFillColor(0);
	leg->SetBorderSize(0);
	leg->AddEntry(H_data,"Data 2011,"+Luminosity+" pb^{-1}");
	leg->AddEntry(H_zjets,"Z/#gamma* + jets");
	leg->AddEntry(H_wjets,"W + jets");
	leg->AddEntry(H_ttbar,"t#bar{t}");
	leg->AddEntry(H_singtop,"Single Top");
	leg->AddEntry(H_bkg,"Other backgrounds");
	leg->AddEntry(H_lq,"LQ M = 250");
	leg->Draw("SAME");
	c1->SetLogy();

	H_data->SetMinimum(.1);
	H_data->SetMaximum(1.2*extrascalefactor*(H_data->GetMaximum()));

	TLatex* txt =new TLatex((xMax-xLow)*.02+xLow,.3*H_data->GetMaximum(),"CMS 2011 Preliminary");
	txt->SetTextFont(132);
	txt->SetTextSize(0.06);
	txt->Draw();
	//  c1->RedrawAxis();

	string str = Luminosity;
	string searchString("." );
	string replaceString("_" );

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
	//std::cout<<varname<<std::endl;

	pad2->cd();

	TH1F* h_comp = new TH1F("h_comp","",nBins,xLow,xMax);
	TH1F* h_compr = new TH1F("h_compr","",nBins,xLow,xMax);	


	if (true)
	{

		TH1F* h_bg = new TH1F("h_bg","",nBins,xLow,xMax);
		h_bg->Sumw2();
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
		float err_nbg = 0.0;
		float err_total = 0.0;

		float datmean = 0.0;
		float mcmean = 0.0;

		float xminl = 0;
		float xmaxl = 0;

		//std::cout<<" Starting bin analysis" <<std::endl;
		for (ibin=0;ibin<=nbinsx;ibin++)
		{
			ndat = 1.0*(h_data->GetBinContent(ibin));
			nbg = 1.0*(h_bg->GetBinContent(ibin));
			datmean += 1.0*(h_data->GetBinContent(ibin))*h_data->GetBinCenter(ibin);
			err_nbg = 1.0*(h_bg->GetBinError(ibin));
			err_total = sqrt(  pow(err_nbg,2.0) + ndat );

			mcmean += 1.0*(h_bg->GetBinContent(ibin))*h_bg->GetBinCenter(ibin);
			if (ndat!=0)   chi2 += pow((ndat -nbg),2.0)/pow(ndat,0.5);
			//if (nbg>.0010) std::cout<<h_data->GetBinCenter(ibin)<<"  "<<nbg<<" "<<"  "<<ndat/nbg<<"  "<<(ndat-nbg)/sqrt(ndat)<<std::endl;
			h_comp ->SetBinContent(ibin,0.0 );
			h_compr ->SetBinContent(ibin,0.0 );
			if (ndat!=0 && nbg != 0) h_comp ->SetBinContent(ibin, (ndat - nbg)/err_total );
			if (ndat!=0 && nbg != 0) h_compr ->SetBinContent(ibin, (ndat - nbg)/nbg );
			if (ndat!=0 && nbg != 0) h_compr ->SetBinError(ibin, (err_total)/nbg );
	//if (nbg!=0) std::cout<<"cut_mc += \"(("<<var<<">"<<h_bg->GetBinLowEdge(ibin)<<")*("<<var<<"<"<<h_bg->GetBinLowEdge(ibin)+h_bg->GetBinWidth(ibin)<<")*("<<ndat/nbg<<"))+\";"<<std::endl;
			//if ((ndat!=0)&&(abs((ndat - nbg)/sqrt(ndat))>7.99 )) h_comp ->SetBinContent(ibin, 7.95*(ndat>nbg) - 7.95*(ndat<nbg));
			//std::cout<<h_bg->GetBinCenter(ibin)<<","<<nbg<<std::endl;
		}

		//std::cout<<"Chi^2 for this distribution is:  "<< chi2<<std::endl;
	}
	h_comp->GetYaxis()->SetTitle("Poisson N(#sigma) Diff");


	TLine *line0 = new TLine(xLow,0,xMax,0);
	TLine *line2u = new TLine(xLow,2,xMax,2);
	TLine *line2d = new TLine(xLow,-2,xMax,-2);

	h_comp->SetMinimum(-8);
	h_comp->SetMaximum(8);
	h_comp->SetMarkerStyle(21);
	h_comp->SetMarkerSize(0.5);
	//h_comp->SetMarkerSize(0.0);


	h_comp->Draw("p");
	line0->Draw("SAME");
	line2u->Draw("SAME");
	line2d->Draw("SAME");
	
	
	pad2r->cd();

	h_compr->GetYaxis()->SetTitle("Fractional Diff");

   //TGaxis *axis = new TGaxis(xMax,-2,xMax,2,-2,2,50510,"+L");
   //axis->SetLabelColor(kRed);
//axis->Draw();

	h_compr->SetMinimum(-2);
	h_compr->SetMaximum(2);
	h_compr->SetLineColor(kRed);
	h_compr->SetLineWidth(2);
	h_compr->SetMarkerColor(kRed);
	h_compr->SetMarkerStyle(1);
	h_compr->SetMarkerSize(0.0);

	h_compr->Draw("ep");
	line0->Draw("SAME");



	c1->Print("PlotsMuNuSub/"+varname+"_"+tag+".png");
	c1->Print("PlotsMuNuSub/"+varname+"_"+tag+".pdf");

	
	
	TIter next(gDirectory->GetList());
	TObject* obj;
	while(obj= (TObject*)next()){
		if(obj->InheritsFrom(TH1::Class())){
			obj->Delete();
		}
	}

}

void MakePlotsMuNuSub()
{


	// Load Files and Trees:
	gROOT->ProcessLine(".x LoadCastorFiles_V00_02_05_Local.C");

	// Cut Conditions

	TString lumi ="964"  ;
	TString cut_data ="(Pt_muon1>40)*(MET_pf>45.0)";
	cut_data +="*(Pt_muon2<30)";
	////  TString cut_data ="(Pt_muon1>30)*(Pt_muon2>30)";
	////  cut_data +="*(Pt_W<40)*(Pt_W>0)";
	cut_data +="*(Pt_ele1<15.0)";
	cut_data +="*(Pt_pfjet1>30)*(Pt_pfjet2>30)";
	cut_data +="*(abs(Eta_muon1)<2.1)";
	//cut_data +="*(FailIDJetPT25<0.5)";
	//cut_data +="*(ST_pf_munu>250.0)";
	cut_data +="*(abs(deltaPhi_pfjet1pfMET)>.5)";
	////  cut_data +="*(deltaPhi_pfjet2pfMET>.5)";
	////  cut_data +="*(deltaPhi_pfjet1pfMET<2.65)";
	cut_data +="*(abs(deltaPhi_muon1pfMET)>.8)";
	cut_data +="*(FailIDPFThreshold<25.0)";
	cut_data +="*(MT_muon1pfMET>50.0)";


	//  cut_data +="*(Phi_muon1>.3)";
	//  cut_data +="*(Phi_muon1>.3)";

	//  cut_data +="*(NGlobalMuons<2.5)";
	//  cut_data +="*(Eta_pfjet1<0.0)";
	//  cut_data +="*(Eta_pfjet2<0.0)";

	//  cut_data +="&&(deltaPhi_muon1pfMET>2.10)";
	//  cut_data +="*(Pt_Clusters_muon1<1.0)";
	//  cut_data +="*(abs(MET_pf-Pt_muon1)/(MET_pf)>0.2)";
	//  cut_data +="*(PFJetCount<3.5)";
	//  cut_data +="*(1.0 - (EcalIso_muon1>0.1)*(HcalIso_muon1>0.1) )";
	//  cut_data +="*(BpfJetCount<1.5)";
	//  cut_data +="*((N_Vertices>2.5)||(N_Vertices<1.5))";
	//  cut_data +="*(ST_pf_munu>340.0)";
	//  cut_data +="*(Pt_muon1>85)*(MET_pf>85.0)";
	//  cut_data +="*(MT_muon1pfMET>125.0)";

	//  cut_data +="*(deltaR_muon1closestPFJet>.7)";
	//  cut_data +="*(deltaPhi_muon1caloMET<2.85)";
	//  cut_data +="*(BpfJetCount>1.5)";
	//  cut_data +="*(MT_muon1pfMET>125.0)";
	//cut_data +="*(MT_muon1pfMET<110.0)";
	//cut_data +="*(MT_muon1pfMET>50.0)";

	TString cut_mc = lumi+"*weight*("+cut_data+")";


// These are MC - driven Summer11 for the bug fix
cut_mc += "*(";
cut_mc += "((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)*(0.133068262644))+";
cut_mc += "((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)*(0.531177727826))+";
cut_mc += "((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)*(1.08393607934))+";
cut_mc += "((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)*(1.75485574706))+";
cut_mc += "((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)*(2.23265146857))+";
cut_mc += "((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)*(2.29302545029))+";
cut_mc += "((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)*(2.08187693395))+";
cut_mc += "((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)*(1.74354004493))+";
cut_mc += "((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)*(1.32963414181))+";
cut_mc += "((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)*(0.950884829018))+";
cut_mc += "((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)*(0.653989809522))+";
cut_mc += "((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)*(0.421230072952))+";
cut_mc += "((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)*(0.259599212011))+";
cut_mc += "((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)*(0.158601185413))+";
cut_mc += "((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)*(0.100442489896))+";
cut_mc += "((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)*(0.0594521650904))+";
cut_mc += "((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)*(0.0345162335823))+";
cut_mc += "((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)*(0.0207204183018))+";
cut_mc += "((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)*(0.0117033339315))+";
cut_mc += "((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)*(0.00694640146464))+";
cut_mc += "((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)*(0.00348689915421))+";
cut_mc += "((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)*(0.00191943200042))+";
cut_mc += "((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)*(0.00120128248423))+";
cut_mc += "((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)*(0.000647624891971))+";
cut_mc += "((N_PileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)*(0.000455476442992))+";
cut_mc += "((N_PileUpInteractions > 24.5)*(N_PileUpInteractions < 25.5)*(0.000196385472519))+";
cut_mc += "((N_PileUpInteractions > 25.5)*(N_PileUpInteractions < 26.5)*(0.000101079948326))+";
cut_mc += "((N_PileUpInteractions > 26.5)*(N_PileUpInteractions < 27.5)*(8.14199879897e-05))+";
cut_mc += "((N_PileUpInteractions > 27.5)*(N_PileUpInteractions < 28.5)*(4.89354471066e-05))+";
cut_mc += "((N_PileUpInteractions > 28.5)*(N_PileUpInteractions < 29.5)*(3.35058351289e-05))";
cut_mc += ")";

// These are MC - driven Summer11 for the bug fix using bunch weights
//cut_mc += "*(";
//cut_mc += "((N_WeightedPileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)*(0.133068262644))+";
//cut_mc += "((N_WeightedPileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)*(0.531177727826))+";
//cut_mc += "((N_WeightedPileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)*(1.08393607934))+";
//cut_mc += "((N_WeightedPileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)*(1.75485574706))+";
//cut_mc += "((N_WeightedPileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)*(2.23265146857))+";
//cut_mc += "((N_WeightedPileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)*(2.29302545029))+";
//cut_mc += "((N_WeightedPileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)*(2.08187693395))+";
//cut_mc += "((N_WeightedPileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)*(1.74354004493))+";
//cut_mc += "((N_WeightedPileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)*(1.32963414181))+";
//cut_mc += "((N_WeightedPileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)*(0.950884829018))+";
//cut_mc += "((N_WeightedPileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)*(0.653989809522))+";
//cut_mc += "((N_WeightedPileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)*(0.421230072952))+";
//cut_mc += "((N_WeightedPileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)*(0.259599212011))+";
//cut_mc += "((N_WeightedPileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)*(0.158601185413))+";
//cut_mc += "((N_WeightedPileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)*(0.100442489896))+";
//cut_mc += "((N_WeightedPileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)*(0.0594521650904))+";
//cut_mc += "((N_WeightedPileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)*(0.0345162335823))+";
//cut_mc += "((N_WeightedPileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)*(0.0207204183018))+";
//cut_mc += "((N_WeightedPileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)*(0.0117033339315))+";
//cut_mc += "((N_WeightedPileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)*(0.00694640146464))+";
//cut_mc += "((N_WeightedPileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)*(0.00348689915421))+";
//cut_mc += "((N_WeightedPileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)*(0.00191943200042))+";
//cut_mc += "((N_WeightedPileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)*(0.00120128248423))+";
//cut_mc += "((N_WeightedPileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)*(0.000647624891971))+";
//cut_mc += "((N_WeightedPileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)*(0.000455476442992))+";
//cut_mc += "((N_WeightedPileUpInteractions > 24.5)*(N_PileUpInteractions < 25.5)*(0.000196385472519))+";
//cut_mc += "((N_WeightedPileUpInteractions > 25.5)*(N_PileUpInteractions < 26.5)*(0.000101079948326))+";
//cut_mc += "((N_WeightedPileUpInteractions > 26.5)*(N_PileUpInteractions < 27.5)*(8.14199879897e-05))+";
//cut_mc += "((N_WeightedPileUpInteractions > 27.5)*(N_PileUpInteractions < 28.5)*(4.89354471066e-05))+";
//cut_mc += "((N_WeightedPileUpInteractions > 28.5)*(N_PileUpInteractions < 29.5)*(3.35058351289e-05))";
//cut_mc += ")";

// These are from the mixing module

//cut_mc += "*(";
//cut_mc += "((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)*(0.185626207798))+";
//cut_mc += "((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)*(0.42583555701))+";
//cut_mc += "((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)*(0.983425220588))+";
//cut_mc += "((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)*(1.60756198475))+";
//cut_mc += "((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)*(2.06101780086))+";
//cut_mc += "((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)*(2.20045322833))+";
//cut_mc += "((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)*(2.03181596181))+";
//cut_mc += "((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)*(1.66526505721))+";
//cut_mc += "((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)*(1.23451631687))+";
//cut_mc += "((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)*(0.83971609875))+";
//cut_mc += "((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)*(0.52995300733))+";
//cut_mc += "((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)*(0.332814874864))+";
//cut_mc += "((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)*(0.224446370555))+";
//cut_mc += "((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)*(0.156753261452))+";
//cut_mc += "((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)*(0.107016604049))+";
//cut_mc += "((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)*(0.0797487370731))+";
//cut_mc += "((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)*(0.0591346986699))+";
//cut_mc += "((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)*(0.0437285788856))+";
//cut_mc += "((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)*(0.0314714756899))+";
//cut_mc += "((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)*(0.0272704760569))+";
//cut_mc += "((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)*(0.0210989861712))+";
//cut_mc += "((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)*(0.0207102970854))+";
//cut_mc += "((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)*(0.0205646801805))+";
//cut_mc += "((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)*(0.0197259419363))+";
//cut_mc += "((N_PileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)*(0.0445172018043))";
//cut_mc += ")";


// These are mixing module for weighted PU interactions

//cut_mc += "*(";
//cut_mc += "((N_WeightedPileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)*(0.185626207798))+";
//cut_mc += "((N_WeightedPileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)*(0.42583555701))+";
//cut_mc += "((N_WeightedPileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)*(0.983425220588))+";
//cut_mc += "((N_WeightedPileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)*(1.60756198475))+";
//cut_mc += "((N_WeightedPileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)*(2.06101780086))+";
//cut_mc += "((N_WeightedPileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)*(2.20045322833))+";
//cut_mc += "((N_WeightedPileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)*(2.03181596181))+";
//cut_mc += "((N_WeightedPileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)*(1.66526505721))+";
//cut_mc += "((N_WeightedPileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)*(1.23451631687))+";
//cut_mc += "((N_WeightedPileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)*(0.83971609875))+";
//cut_mc += "((N_WeightedPileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)*(0.52995300733))+";
//cut_mc += "((N_WeightedPileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)*(0.332814874864))+";
//cut_mc += "((N_WeightedPileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)*(0.224446370555))+";
//cut_mc += "((N_WeightedPileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)*(0.156753261452))+";
//cut_mc += "((N_WeightedPileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)*(0.107016604049))+";
//cut_mc += "((N_WeightedPileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)*(0.0797487370731))+";
//cut_mc += "((N_WeightedPileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)*(0.0591346986699))+";
//cut_mc += "((N_WeightedPileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)*(0.0437285788856))+";
//cut_mc += "((N_WeightedPileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)*(0.0314714756899))+";
//cut_mc += "((N_WeightedPileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)*(0.0272704760569))+";
//cut_mc += "((N_WeightedPileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)*(0.0210989861712))+";
//cut_mc += "((N_WeightedPileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)*(0.0207102970854))+";
//cut_mc += "((N_WeightedPileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)*(0.0205646801805))+";
//cut_mc += "((N_WeightedPileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)*(0.0197259419363))+";
//cut_mc += "((N_WeightedPileUpInteractions > 23.5)*(N_PileUpInteractions < 24.5)*(0.0445172018043))";
//cut_mc += ")";

//cut_mc += "*(";

//cut_mc += "((N_Vertices>0.5)*(N_Vertices<1.5)*(0.293021))+";
//cut_mc += "((N_Vertices>1.5)*(N_Vertices<2.5)*(0.697263))+";
//cut_mc += "((N_Vertices>2.5)*(N_Vertices<3.5)*(1.06418))+";
//cut_mc += "((N_Vertices>3.5)*(N_Vertices<4.5)*(1.31721))+";
//cut_mc += "((N_Vertices>4.5)*(N_Vertices<5.5)*(1.50288))+";
//cut_mc += "((N_Vertices>5.5)*(N_Vertices<6.5)*(1.40802))+";
//cut_mc += "((N_Vertices>6.5)*(N_Vertices<7.5)*(1.27084))+";
//cut_mc += "((N_Vertices>7.5)*(N_Vertices<8.5)*(1.08064))+";
//cut_mc += "((N_Vertices>8.5)*(N_Vertices<9.5)*(0.953664))+";
//cut_mc += "((N_Vertices>9.5)*(N_Vertices<10.5)*(0.660632))+";
//cut_mc += "((N_Vertices>10.5)*(N_Vertices<11.5)*(0.446585))+";
//cut_mc += "((N_Vertices>11.5)*(N_Vertices<12.5)*(0.407942))+";
//cut_mc += "((N_Vertices>12.5)*(N_Vertices<13.5)*(0.299721))+";
//cut_mc += "((N_Vertices>13.5)*(N_Vertices<14.5)*(0.165068))+";
//cut_mc += "((N_Vertices>14.5)*(N_Vertices<15.5)*(0.0877606))+";
//cut_mc += "((N_Vertices>15.5)*(N_Vertices<16.5)*(0.0766323))+";
//cut_mc += "((N_Vertices>16.5)*(N_Vertices<17.5)*(0.0855867))+";
//cut_mc += "((N_Vertices>17.5)*(N_Vertices<18.5)*(0.0832984))";
//cut_mc += ")";



	float WNormalization = 1.19;
	TString filetag ="";
	TString xtag ="";


	

	// ------------- Normalization Calculation                         -------------- //

	if (WNormalization == 1.00){
		std::cout<<"\n\n W Normalization is unity. Program will calculate W rescaling factor and exit.\n\n"<<std::endl;
		filetag ="2011Data_NormalizationSelection";
		xtag =" [W Normalization Condition]";
		TString NormCondition ="*(ST_pf_munu>250)*(MT_muon1pfMET>50)*(MT_muon1pfMET<110)";
		fillHisto(cut_mc + NormCondition, cut_data+NormCondition, true, 60,50,110,"MT_muon1pfMET", false,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,1000,WNormalization,filetag);	
		gROOT->Reset();	gROOT->ProcessLine(".q;");
	}


	// ------------- Minimal Selection - Preselection Without ST Cut.  -------------- //

	filetag ="2011Data_MinimalSelection";
	xtag =" [Presel sans ST cut]";

	//fillHisto(cut_mc, cut_data, true, 40,0,800,"M_pfjet1pfjet2", false,"","M_{jj}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//////fillHisto(cut_mc, cut_data, true, 40,0,400,"MT_pfjet1pfjet2", false,"","M^{T}_{jj}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,8,"deltaR_pfjet1pfjet2", false,"","#Delta R (j_{1}j_{2})(GeV)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet1pfjet2", false,"","#Delta#phi (j_{1}j_{2})(GeV)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 60,0,600,"MT_pfjet1pfMET", false,"","M_{T}(j_{1},E_{T}^{miss})(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,400,"MT_pfjet2pfMET", false,"","M_{T}(j_{2},E_{T}^{miss})(GeV)" +xtag,lumi,10,WNormalization,filetag);

	//gROOT->Reset();	gROOT->ProcessLine(".q;");




	// ------------- Pre Selection - Preselection With ST>250 Cut      -------------- //

	cut_data +="*(ST_pf_munu>250.0)";
	cut_mc +="*(ST_pf_munu>250.0)";
	TString filetag ="2011Data_PreSelection";
	TString xtag =" [Preselection]";

	fillHisto(cut_mc, cut_data, true, 50,0,500,"MT_muon1pfMET", false,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,10,WNormalization,filetag);

	//fillHisto(cut_mc, cut_data, true, 50,-.5,49.5,"N_PileUpInteractions", false,"","PileUp Interactions " +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,-.5,49.5,"N_WeightedPileUpInteractions", false,"","Weighted PileUp Interactions " +xtag,lumi,100,WNormalization,filetag);

	//fillHisto(cut_mc, cut_data ,true,25,.-.5,24.5,"N_Vertices", false,"","N_{Vertices}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,0,500,"MT_muon1pfMET", false,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,10,WNormalization,filetag);

	//gROOT->Reset();	gROOT->ProcessLine(".q;");
	
	fillHisto(cut_mc, cut_data, true, 50,-.5,49.5,"PFJetNeutralMultiplicity_pfjet1", false,"","Neutral Mult. (Jet 1) " +xtag,lumi,100,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 25,0,1,"PFJetNeutralHadronEnergyFraction_pfjet1", false,"","Neutral Had Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 25,0,1,"PFJetNeutralEmEnergyFraction_pfjet1", false,"","NeutralEM Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
	
	fillHisto(cut_mc, cut_data, true, 50,-.5,49.5,"PFJetNeutralMultiplicity_pfjet2", false,"","Neutral Mult. (Jet 2) " +xtag,lumi,100,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 25,0,1,"PFJetNeutralHadronEnergyFraction_pfjet2", false,"","Neutral Had Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 25,0,1,"PFJetNeutralEmEnergyFraction_pfjet2", false,"","NeutralEM Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
	

	fillHisto(cut_mc, cut_data, true, 42,-2,40,"FailIDCaloThreshold", false,"","CaloJetID Failure p_{T} (GeV)" +xtag,lumi,10,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 42,-2,40,"FailIDPFThreshold", false,"","PFJetID Failure p_{T} (GeV)" +xtag,lumi,10,WNormalization,filetag);

	fillHisto(cut_mc, cut_data ,true,25,.-.5,24.5,"N_PileUpInteractions", false,"","N_{PU}" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(cut_mc, cut_data ,true,25,.-.5,24.5,"N_Vertices", false,"","N_{Vertices}" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(cut_mc, cut_data ,true,6,.-.5,5.5,"GlobalMuonCount", false,"","N_{Global #mu}" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(cut_mc, cut_data ,true,6,.-.5,5.5,"TrackerMuonCount", false,"","N_{Tracker #mu}" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(cut_mc, cut_data ,true,12,.-.5,11.5,"PFJetCount", false,"","N_{PFJet}" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(cut_mc, cut_data ,true,8,.-.5,7.5,"BpfJetCount", false,"","N_{BPFJet}" +xtag,lumi,100,WNormalization,filetag);
	
	fillHisto(cut_mc, cut_data, true, 50,0,500,"MT_muon1pfMET", false,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 25,70,170,"MT_muon1pfMET", false,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,100,WNormalization,filetag+"ZOOMRegion");
	fillHisto(cut_mc, cut_data, true, 50,0,500,"MET_pf",        false,"","E_{T}^{miss}(GeV)" +xtag  ,lumi,10,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,0,400,"Pt_W",        false,"","p_{T}(W)(GeV)" +xtag  ,lumi,500,WNormalization,filetag);
	
	fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_muon1pfMET", false,"","#Delta #phi (#mu,E_{T}^{miss})" +xtag,lumi,1000,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet1pfMET", false,"","#Delta #phi (j_{1},E_{T}^{miss})" +xtag,lumi,1000,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet2pfMET", false,"","#Delta #phi (j_{2},E_{T}^{miss})" +xtag,lumi,1000,WNormalization,filetag);

	fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPFJet", false,"","#Delta #phi (E_{T}^{miss},Closest PFJet)" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPFJet", false,"","#Delta #phi (E_{T}^{miss},Furthest PFJet)" +xtag,lumi,1000,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestCaloJet", false,"","#Delta #phi (E_{T}^{miss},Closest CaloJet)" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestCaloJet", false,"","#Delta #phi (E_{T}^{miss},Furthest CaloJet)" +xtag,lumi,1000,WNormalization,filetag);
	
	fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPT10PFJet", false,"","#Delta #phi (E_{T}^{miss},Closest 10GeV PFJet)" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPT10PFJet", false,"","#Delta #phi (E_{T}^{miss},Furthest 10GeV PFJet)" +xtag,lumi,1000,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPT10CaloJet", false,"","#Delta #phi (E_{T}^{miss},Closest 10GeV CaloJet)" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPT10CaloJet", false,"","#Delta #phi (E_{T}^{miss},Furthest 10GeV CaloJet)" +xtag,lumi,1000,WNormalization,filetag);

	fillHisto(cut_mc, cut_data, true, 60,0,30,"EcalIso_muon1", false,"","ECAL Iso_{#mu} (GeV)" +xtag,lumi,10,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 50,0,3,"HcalIso_muon1", false,"","HCAL Iso (#mu)" +xtag,lumi,10,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 35,0,3.5,"TrkIso_muon1", false,"","Track Iso (#mu)" +xtag,lumi,10,WNormalization,filetag);

	fillHisto(cut_mc, cut_data, true, 40,0,400,"Pt_muon1", false,"","p_{T} (#mu) (GeV)" +xtag,lumi,10,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 50,0,50,"PtError_muon1", false,"","#sigma(p_{T}) (#mu) (GeV)" +xtag,lumi,10,WNormalization,filetag);	
	fillHisto(cut_mc, cut_data, true, 42,-2.1,2.1,"Eta_muon1", false,"","#eta (#mu)" +xtag,lumi,1000,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 50,0,.001,"EtaError_muon1", false,"","#sigma(#eta) (#mu)" +xtag,lumi,1000,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true,30,-3.141593,3.141593,"Phi_muon1", false,"","#phi (#mu)" +xtag,lumi,2000,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 50,0,.0005,"PhiError_muon1", false,"","#sigma(#phi) (#mu)" +xtag,lumi,1000,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,0,.0008,"QOverPError_muon1", false,"","#sigma(Q/p)_{#mu}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	
	fillHisto(cut_mc, cut_data, true, 60,0,600,"Pt_pfjet1", false,"","p_{T} (jet_{1}) (GeV)" +xtag,lumi,10,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 50,0,500,"Pt_pfjet2", false,"","p_{T} (jet_{2}) (GeV)" +xtag,lumi,10,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,-3.0,3.0,"Eta_pfjet1", false,"","#eta (jet_{1})" +xtag,lumi,1000,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,-3.0,3.0,"Eta_pfjet2", false,"","#eta (jet_{2})" +xtag,lumi,1000,WNormalization,filetag);
	
	fillHisto(cut_mc, cut_data, true, 60,200,1200,"ST_pf_munu", false,"","S_{T} (GeV)" +xtag,lumi,50,WNormalization,filetag);

	fillHisto(cut_mc, cut_data, true, 100,0,2000,"M_bestmupfjet_munu", false,"","M_{#mu jet}" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,0,800,"M_pfjet1pfjet2", false,"","M_{jj}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 60,0,600,"MT_pfjet1pfMET", false,"","M_{T}(j_{1},E_{T}^{miss})(GeV)" +xtag,lumi,10,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,0,400,"MT_pfjet2pfMET", false,"","M_{T}(j_{2},E_{T}^{miss})(GeV)" +xtag,lumi,10,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,0,400,"MT_pfjet1pfjet2", false,"","M^{T}_{jj}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,0,8,"deltaR_pfjet1pfjet2", false,"","#Delta R (j_{1}j_{2})(GeV)" +xtag,lumi,1000,WNormalization,filetag);
	fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet1pfjet2", false,"","#Delta#phi (j_{1}j_{2})(GeV)" +xtag,lumi,1000,WNormalization,filetag);


	// ------------- Adding the Bad-Jet Veto      -------------- //

	//cut_data +="*(FailIDPFThreshold<0.0)";
	//cut_mc +="*(FailIDPFThreshold<0.0)";
	TString filetag ="2011Data_PreSelection_BadJetVeto";
	TString xtag =" [Preselection + Bad Jet Veto]";

	
	//fillHisto(cut_mc, cut_data, true, 50,-.5,49.5,"PFJetNeutralMultiplicity_pfjet1", false,"","Neutral Mult. (Jet 1) " +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 25,0,1,"PFJetNeutralHadronEnergyFraction_pfjet1", false,"","Neutral Had Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 25,0,1,"PFJetNeutralEmEnergyFraction_pfjet1", false,"","NeutralEM Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 50,-.5,49.5,"PFJetNeutralMultiplicity_pfjet2", false,"","Neutral Mult. (Jet 2) " +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 25,0,1,"PFJetNeutralHadronEnergyFraction_pfjet2", false,"","Neutral Had Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 25,0,1,"PFJetNeutralEmEnergyFraction_pfjet2", false,"","NeutralEM Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
	
	////gROOT->Reset();	gROOT->ProcessLine(".q;");

	//fillHisto(cut_mc, cut_data, true, 42,-2,40,"FailIDCaloThreshold", false,"","CaloJetID Failure p_{T} (GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 42,-2,40,"FailIDPFThreshold", false,"","PFJetID Failure p_{T} (GeV)" +xtag,lumi,10,WNormalization,filetag);


	//fillHisto(cut_mc, cut_data ,true,25,.-.5,24.5,"N_Vertices", false,"","N_{Vertices}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data ,true,6,.-.5,5.5,"GlobalMuonCount", false,"","N_{Global #mu}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data ,true,6,.-.5,5.5,"TrackerMuonCount", false,"","N_{Tracker #mu}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data ,true,12,.-.5,11.5,"PFJetCount", false,"","N_{PFJet}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data ,true,8,.-.5,7.5,"BpfJetCount", false,"","N_{BPFJet}" +xtag,lumi,100,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 50,0,500,"MT_muon1pfMET", false,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 25,70,170,"MT_muon1pfMET", false,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,100,WNormalization,filetag+"ZOOMRegion");
	//fillHisto(cut_mc, cut_data, true, 50,0,500,"MET_pf",        false,"","E_{T}^{miss}(GeV)" +xtag  ,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,400,"Pt_W",        false,"","p_{T}(W)(GeV)" +xtag  ,lumi,500,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_muon1pfMET", false,"","#Delta #phi (#mu,E_{T}^{miss})" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet1pfMET", false,"","#Delta #phi (j_{1},E_{T}^{miss})" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet2pfMET", false,"","#Delta #phi (j_{2},E_{T}^{miss})" +xtag,lumi,1000,WNormalization,filetag);

	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPFJet", false,"","#Delta #phi (E_{T}^{miss},Closest PFJet)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPFJet", false,"","#Delta #phi (E_{T}^{miss},Furthest PFJet)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestCaloJet", false,"","#Delta #phi (E_{T}^{miss},Closest CaloJet)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestCaloJet", false,"","#Delta #phi (E_{T}^{miss},Furthest CaloJet)" +xtag,lumi,1000,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPT10PFJet", false,"","#Delta #phi (E_{T}^{miss},Closest 10GeV PFJet)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPT10PFJet", false,"","#Delta #phi (E_{T}^{miss},Furthest 10GeV PFJet)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPT10CaloJet", false,"","#Delta #phi (E_{T}^{miss},Closest 10GeV CaloJet)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPT10CaloJet", false,"","#Delta #phi (E_{T}^{miss},Furthest 10GeV CaloJet)" +xtag,lumi,1000,WNormalization,filetag);

	//fillHisto(cut_mc, cut_data, true, 60,0,30,"EcalIso_muon1", false,"","ECAL Iso_{#mu} (GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,0,3,"HcalIso_muon1", false,"","HCAL Iso (#mu)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 35,0,3.5,"TrkIso_muon1", false,"","Track Iso (#mu)" +xtag,lumi,10,WNormalization,filetag);

	//fillHisto(cut_mc, cut_data, true, 40,0,400,"Pt_muon1", false,"","p_{T} (#mu) (GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,0,50,"PtError_muon1", false,"","#sigma(p_{T}) (#mu) (GeV)" +xtag,lumi,10,WNormalization,filetag);	
	//fillHisto(cut_mc, cut_data, true, 42,-2.1,2.1,"Eta_muon1", false,"","#eta (#mu)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,0,.001,"EtaError_muon1", false,"","#sigma(#eta) (#mu)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true,30,-3.141593,3.141593,"Phi_muon1", false,"","#phi (#mu)" +xtag,lumi,2000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,0,.0005,"PhiError_muon1", false,"","#sigma(#phi) (#mu)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,.0008,"QOverPError_muon1", false,"","#sigma(Q/p)_{#mu}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 60,0,600,"Pt_pfjet1", false,"","p_{T} (jet_{1}) (GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,0,500,"Pt_pfjet2", false,"","p_{T} (jet_{2}) (GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,-3.0,3.0,"Eta_pfjet1", false,"","#eta (jet_{1})" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,-3.0,3.0,"Eta_pfjet2", false,"","#eta (jet_{2})" +xtag,lumi,1000,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 60,200,1200,"ST_pf_munu", false,"","S_{T} (GeV)" +xtag,lumi,50,WNormalization,filetag);

	//fillHisto(cut_mc, cut_data, true, 100,0,2000,"M_bestmupfjet_munu", false,"","M_{#mu jet}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,800,"M_pfjet1pfjet2", false,"","M_{jj}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 60,0,600,"MT_pfjet1pfMET", false,"","M_{T}(j_{1},E_{T}^{miss})(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,400,"MT_pfjet2pfMET", false,"","M_{T}(j_{2},E_{T}^{miss})(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,400,"MT_pfjet1pfjet2", false,"","M^{T}_{jj}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,8,"deltaR_pfjet1pfjet2", false,"","#Delta R (j_{1}j_{2})(GeV)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet1pfjet2", false,"","#Delta#phi (j_{1}j_{2})(GeV)" +xtag,lumi,1000,WNormalization,filetag);

	// ------------- Excess Selection - Preselection Plus MT > 100 GeV      -------------- //

	xtag =" [M_{T}>100]";
	filetag ="2011Data_MT_Gr100";

	//cut_data +="*(MT_muon1pfMET>100.0)";
	//cut_mc +="*(MT_muon1pfMET>100.0)";

	//fillHisto(cut_mc, cut_data, true, 50,-.5,49.5,"PFJetNeutralMultiplicity_pfjet1", false,"","Neutral Mult. (Jet 1) " +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 25,0,1,"PFJetNeutralHadronEnergyFraction_pfjet1", false,"","Neutral Had Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 25,0,1,"PFJetNeutralEmEnergyFraction_pfjet1", false,"","NeutralEM Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 50,-.5,49.5,"PFJetNeutralMultiplicity_pfjet2", false,"","Neutral Mult. (Jet 2) " +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 25,0,1,"PFJetNeutralHadronEnergyFraction_pfjet2", false,"","Neutral Had Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 25,0,1,"PFJetNeutralEmEnergyFraction_pfjet2", false,"","NeutralEM Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
	
		////gROOT->Reset();	gROOT->ProcessLine(".q;");

	//fillHisto(cut_mc, cut_data, true, 42,-2,40,"FailIDCaloThreshold", false,"","CaloJetID Failure p_{T} (GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 42,-2,40,"FailIDPFThreshold", false,"","PFJetID Failure p_{T} (GeV)" +xtag,lumi,10,WNormalization,filetag);

	//fillHisto(cut_mc, cut_data ,true,25,.-.5,24.5,"N_Vertices", false,"","N_{Vertices}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data ,true,6,.-.5,5.5,"GlobalMuonCount", false,"","N_{Global #mu}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data ,true,6,.-.5,5.5,"TrackerMuonCount", false,"","N_{Tracker #mu}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data ,true,12,.-.5,11.5,"PFJetCount", false,"","N_{PFJet}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data ,true,8,.-.5,7.5,"BpfJetCount", false,"","N_{BPFJet}" +xtag,lumi,100,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 50,0,500,"MT_muon1pfMET", false,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 25,70,170,"MT_muon1pfMET", false,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,100,WNormalization,filetag+"ZOOMRegion");
	//fillHisto(cut_mc, cut_data, true, 50,0,500,"MET_pf",        false,"","E_{T}^{miss}(GeV)" +xtag  ,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,400,"Pt_W",        false,"","p_{T}(W)(GeV)" +xtag  ,lumi,500,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_muon1pfMET", false,"","#Delta #phi (#mu,E_{T}^{miss})" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet1pfMET", false,"","#Delta #phi (j_{1},E_{T}^{miss})" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet2pfMET", false,"","#Delta #phi (j_{2},E_{T}^{miss})" +xtag,lumi,1000,WNormalization,filetag);

	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPFJet", false,"","#Delta #phi (E_{T}^{miss},Closest PFJet)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPFJet", false,"","#Delta #phi (E_{T}^{miss},Furthest PFJet)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestCaloJet", false,"","#Delta #phi (E_{T}^{miss},Closest CaloJet)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestCaloJet", false,"","#Delta #phi (E_{T}^{miss},Furthest CaloJet)" +xtag,lumi,1000,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPT10PFJet", false,"","#Delta #phi (E_{T}^{miss},Closest 10GeV PFJet)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPT10PFJet", false,"","#Delta #phi (E_{T}^{miss},Furthest 10GeV PFJet)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPT10CaloJet", false,"","#Delta #phi (E_{T}^{miss},Closest 10GeV CaloJet)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPT10CaloJet", false,"","#Delta #phi (E_{T}^{miss},Furthest 10GeV CaloJet)" +xtag,lumi,1000,WNormalization,filetag);

	//fillHisto(cut_mc, cut_data, true, 60,0,30,"EcalIso_muon1", false,"","ECAL Iso_{#mu} (GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,0,3,"HcalIso_muon1", false,"","HCAL Iso (#mu)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 35,0,3.5,"TrkIso_muon1", false,"","Track Iso (#mu)" +xtag,lumi,10,WNormalization,filetag);

	//fillHisto(cut_mc, cut_data, true, 40,0,400,"Pt_muon1", false,"","p_{T} (#mu) (GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,0,50,"PtError_muon1", false,"","#sigma(p_{T}) (#mu) (GeV)" +xtag,lumi,10,WNormalization,filetag);	
	//fillHisto(cut_mc, cut_data, true, 42,-2.1,2.1,"Eta_muon1", false,"","#eta (#mu)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,0,.001,"EtaError_muon1", false,"","#sigma(#eta) (#mu)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true,30,-3.141593,3.141593,"Phi_muon1", false,"","#phi (#mu)" +xtag,lumi,2000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,0,.0005,"PhiError_muon1", false,"","#sigma(#phi) (#mu)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,.0008,"QOverPError_muon1", false,"","#sigma(Q/p)_{#mu}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 60,0,600,"Pt_pfjet1", false,"","p_{T} (jet_{1}) (GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,0,500,"Pt_pfjet2", false,"","p_{T} (jet_{2}) (GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,-3.0,3.0,"Eta_pfjet1", false,"","#eta (jet_{1})" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,-3.0,3.0,"Eta_pfjet2", false,"","#eta (jet_{2})" +xtag,lumi,1000,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 60,200,1200,"ST_pf_munu", false,"","S_{T} (GeV)" +xtag,lumi,50,WNormalization,filetag);

	//fillHisto(cut_mc, cut_data, true, 100,0,2000,"M_bestmupfjet_munu", false,"","M_{#mu jet}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,800,"M_pfjet1pfjet2", false,"","M_{jj}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 60,0,600,"MT_pfjet1pfMET", false,"","M_{T}(j_{1},E_{T}^{miss})(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,400,"MT_pfjet2pfMET", false,"","M_{T}(j_{2},E_{T}^{miss})(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,400,"MT_pfjet1pfjet2", false,"","M^{T}_{jj}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,8,"deltaR_pfjet1pfjet2", false,"","#Delta R (j_{1}j_{2})(GeV)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet1pfjet2", false,"","#Delta#phi (j_{1}j_{2})(GeV)" +xtag,lumi,1000,WNormalization,filetag);


	//// ------------- Excess Selection - Preselection Plus MT > 90 GeV, Jet2PT<70      -------------- //

	//xtag =" [M_{T}>90, p_{T}(j_2)<70]";
	//filetag ="2011Data_MT_Gr90_Jet2Less70";

	//cut_data +="*(Pt_pfjet2<70.0)";
	//cut_mc +="*(Pt_pfjet2<70.0)";

	

	//fillHisto(cut_mc, cut_data ,true,25,.-.5,24.5,"N_Vertices", false,"","N_{Vertices}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data ,true,6,.-.5,5.5,"GlobalMuonCount", false,"","N_{Global #mu}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data ,true,6,.-.5,5.5,"TrackerMuonCount", false,"","N_{Tracker #mu}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data ,true,12,.-.5,11.5,"PFJetCount", false,"","N_{PFJet}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data ,true,8,.-.5,7.5,"BpfJetCount", false,"","N_{BPFJet}" +xtag,lumi,100,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 50,0,500,"MT_muon1pfMET", false,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 25,70,170,"MT_muon1pfMET", false,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,100,WNormalization,filetag+"ZOOMRegion");
	//fillHisto(cut_mc, cut_data, true, 50,0,500,"MET_pf",        false,"","E_{T}^{miss}(GeV)" +xtag  ,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,400,"Pt_W",        false,"","p_{T}(W)(GeV)" +xtag  ,lumi,500,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_muon1pfMET", false,"","#Delta #phi (#mu,E_{T}^{miss})" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet1pfMET", false,"","#Delta #phi (j_{1},E_{T}^{miss})" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet2pfMET", false,"","#Delta #phi (j_{2},E_{T}^{miss})" +xtag,lumi,1000,WNormalization,filetag);

	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPFJet", false,"","#Delta #phi (E_{T}^{miss},Closest PFJet)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPFJet", false,"","#Delta #phi (E_{T}^{miss},Furthest PFJet)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestCaloJet", false,"","#Delta #phi (E_{T}^{miss},Closest CaloJet)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestCaloJet", false,"","#Delta #phi (E_{T}^{miss},Furthest CaloJet)" +xtag,lumi,1000,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPT10PFJet", false,"","#Delta #phi (E_{T}^{miss},Closest 10GeV PFJet)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPT10PFJet", false,"","#Delta #phi (E_{T}^{miss},Furthest 10GeV PFJet)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPT10CaloJet", false,"","#Delta #phi (E_{T}^{miss},Closest 10GeV CaloJet)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPT10CaloJet", false,"","#Delta #phi (E_{T}^{miss},Furthest 10GeV CaloJet)" +xtag,lumi,1000,WNormalization,filetag);

	//fillHisto(cut_mc, cut_data, true, 60,0,30,"EcalIso_muon1", false,"","ECAL Iso_{#mu} (GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,0,3,"HcalIso_muon1", false,"","HCAL Iso (#mu)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 35,0,3.5,"TrkIso_muon1", false,"","Track Iso (#mu)" +xtag,lumi,10,WNormalization,filetag);

	//fillHisto(cut_mc, cut_data, true, 40,0,400,"Pt_muon1", false,"","p_{T} (#mu) (GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,0,50,"PtError_muon1", false,"","#sigma(p_{T}) (#mu) (GeV)" +xtag,lumi,10,WNormalization,filetag);	
	//fillHisto(cut_mc, cut_data, true, 42,-2.1,2.1,"Eta_muon1", false,"","#eta (#mu)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,0,.001,"EtaError_muon1", false,"","#sigma(#eta) (#mu)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true,30,-3.141593,3.141593,"Phi_muon1", false,"","#phi (#mu)" +xtag,lumi,2000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,0,.0005,"PhiError_muon1", false,"","#sigma(#phi) (#mu)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,.0008,"QOverPError_muon1", false,"","#sigma(Q/p)_{#mu}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 60,0,600,"Pt_pfjet1", false,"","p_{T} (jet_{1}) (GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 50,0,500,"Pt_pfjet2", false,"","p_{T} (jet_{2}) (GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,-3.0,3.0,"Eta_pfjet1", false,"","#eta (jet_{1})" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,-3.0,3.0,"Eta_pfjet2", false,"","#eta (jet_{2})" +xtag,lumi,1000,WNormalization,filetag);
	
	//fillHisto(cut_mc, cut_data, true, 60,200,1200,"ST_pf_munu", false,"","S_{T} (GeV)" +xtag,lumi,50,WNormalization,filetag);

	//fillHisto(cut_mc, cut_data, true, 100,0,2000,"M_bestmupfjet_munu", false,"","M_{#mu jet}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,800,"M_pfjet1pfjet2", false,"","M_{jj}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 60,0,600,"MT_pfjet1pfMET", false,"","M_{T}(j_{1},E_{T}^{miss})(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,400,"MT_pfjet2pfMET", false,"","M_{T}(j_{2},E_{T}^{miss})(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,400,"MT_pfjet1pfjet2", false,"","M^{T}_{jj}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,0,8,"deltaR_pfjet1pfjet2", false,"","#Delta R (j_{1}j_{2})(GeV)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet1pfjet2", false,"","#Delta#phi (j_{1}j_{2})(GeV)" +xtag,lumi,1000,WNormalization,filetag);




	//// ------------- Pre Selection - Preselection With ST>250 Cut      -------------- //


	//xtag =" [Full Selection + Bad Jet Veto]";
	//filetag ="2011Data_FullSelection_BadJetVeto";

	//TString cut_mass_data = cut_data +"*(MT_muon1pfMET>125.0)*(Pt_muon1>85)*(MET_pf>85.0)*(ST_pf_munu>485)";
	//TString cut_mass_mc = lumi+"*weight*("+cut_mass_data+")";

	//TString cut_st_data = cut_data +"*(MT_muon1pfMET>125.0)*(Pt_muon1>85)*(MET_pf>85.0)*(ST_pf_munu>250)";
	//TString cut_st_mc = lumi+"*weight*("+cut_st_data+")";

	//fillHisto(cut_mass_mc, cut_mass_data, true, 40,0.0,2000.0,"M_bestmupfjet_munu", false,"","M_{#mu j}" +xtag,lumi,40,WNormalization,filetag);
	//fillHisto(cut_st_mc, cut_st_data, true, 30,200,1700,"ST_pf_munu", false,"","S_{T} (GeV)" +xtag,lumi,50,WNormalization,filetag);


	gROOT->Reset(); gROOT->ProcessLine(".q;");

}
