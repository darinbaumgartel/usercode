
#include "TLorentzVector.h"
#include "TH1.h"
#include <iostream>
#include <fstream>
#include <iomanip>
#include "CMSStyle.C"

void fillHisto(TString lq_choice, TString cut_mc, TString cut_data,  bool drawSub,
int nBins, float xLow, float xMax, TString var, bool Use_integral, TString fileName,TString title, TString Luminosity,Double_t extrascalefactor,Double_t wnorm,TString tag)
{
	CMSStyle();

	std::cout<<"\n Looking at variable:  "<<var<<"  \n"<<std::endl;

	TIter next(PhysicalVariables->GetListOfBranches());
	TObject* obj;
	bool usevar = false;
	while(obj= (TObject*)next()){
			if (var == obj->GetName()) usevar = true;
	}

	if (!usevar) 
	{
		std::cout<<"\nWARNING: Branch for variable "<<var<<"  not found. Skipping plot for this variable. \n"<<std::endl;
		return;
	}

	if (drawSub) TCanvas *c1 = new TCanvas("c1","",800,800);
	if (!drawSub) TCanvas *c1 = new TCanvas("c1","",800,480);

	if (drawSub) TPad *pad1 = new TPad("pad1","The pad 60% of the height",0.0,0.4,1.0,1.0,0);
	if (!drawSub) TPad *pad1 = new TPad("pad1","The pad 60% of the height",0.0,0.0,1.0,1.0,0);	
	if (drawSub) TPad *pad2 = new TPad("pad2","The pad 20% of the height",0.0,0.2,1.0,0.4,0);
	if (drawSub) TPad *pad2r = new TPad("pad2r","The ptad 20% of the height",0.0,0.0,1.0,0.2,0);

	pad1->Draw();
	if (drawSub) pad2->Draw();
	if (drawSub) pad2r->Draw();

	pad1->cd();
	pad1->SetLogy();
	gStyle->SetOptLogy();
	TH1F* H_zjets = new TH1F("H_zjets","",nBins,xLow,xMax);
	TH1F* H_wjets = new TH1F("H_wjets","",nBins,xLow,xMax);
	TH1F* H_vvjets = new TH1F("H_vvjets","",nBins,xLow,xMax);
	TH1F* H_singtop = new TH1F("H_singtop","",nBins,xLow,xMax);
	TH1F* H_qcd = new TH1F("H_qcd","",nBins,xLow,xMax);
	TH1F* H_ttbar = new TH1F("H_ttbar","",nBins,xLow,xMax);
	TH1F* H_data = new TH1F("H_data","",nBins,xLow,xMax);
	TH1F* H_lq = new TH1F("H_lq","",nBins,xLow,xMax);

	zjets->Draw(var+">>H_zjets",cut_mc);
	wjets->Draw(var+">>H_wjets",cut_mc);
	ttbar->Draw(var+">>H_ttbar",cut_mc);
	vvjets->Draw(var+">>H_vvjets",cut_mc);
	singtop->Draw(var+">>H_singtop",cut_mc);
	qcd->Draw(var+">>H_qcd",cut_mc);
	if (lq_choice == "lqmunu250")  lqmunu250->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmunu350")  lqmunu350->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmunu400")  lqmunu400->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmunu450")  lqmunu450->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmunu500")  lqmunu500->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmunu550")  lqmunu550->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmunu600")  lqmunu600->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmunu650")  lqmunu650->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmunu750")  lqmunu750->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmunu850")  lqmunu850->Draw(var+">>H_lq",cut_mc);	  
	data->Draw(+var+">>H_data",cut_data);



	// Rescaling Routine 
	//H_wjets->Scale(6.13);;
	H_wjets->Scale(wnorm);	
	H_zjets->Scale(1.29);	
	H_ttbar->Scale(0.97);

	// ***************************************         SCREEN READOUT       *************************************************** //

	Double_t Nd = H_data->Integral();
	Double_t Nmc = H_zjets->Integral()+H_ttbar->Integral()+H_vvjets->Integral()+H_wjets->Integral()+H_singtop->Integral()+H_qcd->Integral();
	Double_t Nw = H_wjets->Integral();
	Double_t Nt = H_ttbar->Integral();
	Double_t Nz = H_zjets->Integral();
	Double_t Nlq = H_lq->Integral();
	Double_t N_other = Nmc - Nw;

	
	Double_t sigma_Nw = Nw*pow(1.0*(H_wjets->GetEntries()),-0.5);

	Double_t sigma_N_other = 0.0;
	if (H_ttbar->GetEntries()>0) sigma_N_other += H_ttbar->Integral()*pow((1.0*H_ttbar->GetEntries()),-0.5);
	if (H_zjets->GetEntries()>0) sigma_N_other += H_wjets->Integral()*pow((1.0*H_zjets->GetEntries() ),-0.5);
	if (H_vvjets->GetEntries()>0) sigma_N_other += H_vvjets->Integral()*pow((1.0*H_vvjets->GetEntries() ),-0.5);
	if (H_singtop->GetEntries()>0) sigma_N_other += H_singtop->Integral()*pow((1.0*singtop->GetEntries()),-0.5); 
	if (H_qcd->GetEntries()>0) sigma_N_other += H_qcd->Integral()*pow((1.0*H_qcd->GetEntries()),-0.5);

	Double_t sigam_Nd = sqrt(Nd);


	std::cout<<"Data   :"<<Nd<<std::endl;
	std::cout<<"All MC :"<<Nmc<<std::endl;
	std::cout<<"tt   :"<<H_ttbar->Integral()<<"  +-"<<H_ttbar->Integral()*pow(1.0*(H_ttbar->GetEntries()),-0.5)<<std::endl;
	std::cout<<"w    :"<<H_wjets->Integral()<<"  +-"<<H_wjets->Integral()*pow(1.0*(H_wjets->GetEntries()),-0.5)<<std::endl;
	std::cout<<"LQ    :"<<H_lq->Integral()<<"  +-"<<H_lq->Integral()*pow(1.0*(H_lq->GetEntries()),-0.5)<<std::endl;
	
	
	Double_t fac_Numerator = Nd - N_other;
	Double_t fac_Denominator = Nw;
	Double_t fac = fac_Numerator/fac_Denominator;

	Double_t sigma_fac_Numerator = sqrt( pow( sigam_Nd ,2.0) + pow( sigma_N_other ,2.0) ) ;
	Double_t sigma_fac_Denominator = sigma_Nw; 
	Double_t sigma_fac_over_fac = pow( pow((sigma_fac_Numerator/fac_Numerator),2.0)    +  pow((sigma_fac_Denominator/fac_Denominator),2.0)    ,0.5);
	Double_t sigma_fac = sigma_fac_over_fac*fac;

	std::cout<<"W Scale Factor:  "<<fac<<"  +-  "<<sigma_fac<<std::endl;


	
	// *******************************************************************************************************************************
	
	TH1F* H_bkg = new TH1F("H_bkg","",nBins,xLow,xMax);
	H_bkg->Add(H_vvjets);
	H_bkg->Add(H_qcd);


	float num_lq = 0.0;
	float num_zjets = 0.0;
	float num_wjets = 0.0;
	float num_singtop = 0.0;
	float num_qcd = 0.0;
	float num_ttbar = 0.0;
	float num_bkg = 0.0;
	float num_data = 0.0;
	
	int nbinsx = H_data->GetXaxis()->GetNbins();
	
	if (Use_integral){
		for (ibin=nbinsx;ibin>=0;ibin=ibin-1)
		{	
			num_lq+= 1.0*( H_lq->GetBinContent(ibin));
			num_zjets+= 1.0*( H_zjets->GetBinContent(ibin));
			num_wjets+= 1.0*( H_wjets->GetBinContent(ibin));
			num_singtop+= 1.0*( H_singtop->GetBinContent(ibin));
			num_qcd+= 1.0*( H_qcd->GetBinContent(ibin));
			num_ttbar+= 1.0*( H_ttbar->GetBinContent(ibin));
			num_bkg+= 1.0*( H_bkg->GetBinContent(ibin));
			num_data+= 1.0*( H_data->GetBinContent(ibin));		
			
			H_lq->SetBinContent( ibin, num_lq );
			H_zjets->SetBinContent( ibin,num_zjets  );
			H_wjets->SetBinContent( ibin, num_wjets );
			H_singtop->SetBinContent( ibin, num_singtop  );
			H_qcd->SetBinContent( ibin, num_qcd );
			H_ttbar->SetBinContent( ibin, num_ttbar  );
			H_bkg->SetBinContent( ibin,num_bkg   );
			H_data->SetBinContent( ibin, num_data );			
			
		}	
	}

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

	THStack* H_stack = new THStack("H_stack","");
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
	leg->AddEntry(H_data,"Data 2011, 4.7 fb^{-1}");
	leg->AddEntry(H_zjets,"Z/#gamma* + jets");
	leg->AddEntry(H_wjets,"W + jets");
	leg->AddEntry(H_ttbar,"t#bar{t}");
	leg->AddEntry(H_singtop,"Single Top");
	leg->AddEntry(H_bkg,"Other backgrounds");

	if (lq_choice == "lqmunu250")  leg->AddEntry(H_lq,"LQ M = 250");
	if (lq_choice == "lqmunu350")  leg->AddEntry(H_lq,"LQ M = 350");
	if (lq_choice == "lqmunu400")  leg->AddEntry(H_lq,"LQ M = 400");
	if (lq_choice == "lqmunu450")  leg->AddEntry(H_lq,"LQ M = 450");
	if (lq_choice == "lqmunu500")  leg->AddEntry(H_lq,"LQ M = 500");
	if (lq_choice == "lqmunu550")  leg->AddEntry(H_lq,"LQ M = 550");
	if (lq_choice == "lqmunu600")  leg->AddEntry(H_lq,"LQ M = 600");
	if (lq_choice == "lqmunu650")  leg->AddEntry(H_lq,"LQ M = 650");
	if (lq_choice == "lqmunu750")  leg->AddEntry(H_lq,"LQ M = 750");
	if (lq_choice == "lqmunu850")  leg->AddEntry(H_lq,"LQ M = 850");
		
	leg->Draw("SAME");
	c1->SetLogy();

	H_data->SetMinimum(.01);
	H_data->SetMaximum(1.2*extrascalefactor*(H_data->GetMaximum()));

	TLatex* txt =new TLatex((xMax-xLow)*.02+xLow,.3*H_data->GetMaximum(),"CMS 2011 Preliminary");
	txt->SetTextFont(132);
	txt->SetTextSize(0.06);
	txt->Draw();

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

    if (drawSub) {
		pad2->cd();
	
		TH1F* H_comp = new TH1F("H_comp","",nBins,xLow,xMax);
		TH1F* H_compr = new TH1F("H_compr","",nBins,xLow,xMax);	
	
	
		if (true)
		{
	
			TH1F* H_bg = new TH1F("H_bg","",nBins,xLow,xMax);
			H_bg->Sumw2();
			H_bg->Add(H_zjets);
			H_bg->Add(H_wjets);
			H_bg->Add(H_vvjets);
			H_bg->Add(H_ttbar);
			H_bg->Add(H_singtop);
			H_bg->Add(H_qcd);
	
			int nbinsx = H_bg->GetXaxis()->GetNbins();
	
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
	
			for (ibin=0;ibin<=nbinsx;ibin++)
			{
				ndat = 1.0*(H_data->GetBinContent(ibin));
				nbg = 1.0*(H_bg->GetBinContent(ibin));
				datmean += 1.0*(H_data->GetBinContent(ibin))*H_data->GetBinCenter(ibin);
				err_nbg = 1.0*(H_bg->GetBinError(ibin));
				err_total = sqrt(  pow(err_nbg,2.0) + ndat );
	
				mcmean += 1.0*(H_bg->GetBinContent(ibin))*H_bg->GetBinCenter(ibin);
				if (ndat!=0)   chi2 += pow((ndat -nbg),2.0)/pow(ndat,0.5);
				H_comp ->SetBinContent(ibin,0.0 );
				H_compr ->SetBinContent(ibin,0.0 );
				if (ndat!=0 && nbg != 0) H_comp ->SetBinContent(ibin, (ndat - nbg)/err_total );
				if (ndat!=0 && nbg != 0) H_compr ->SetBinContent(ibin, (ndat - nbg)/nbg );
				if (ndat!=0 && nbg != 0) H_compr ->SetBinError(ibin, (err_total)/nbg );
				}
			}
			
			
		H_comp->GetYaxis()->SetTitle("N(#sigma) Diff.");
		H_comp->GetYaxis()->SetTitleFont(132);
		H_comp->GetYaxis()->SetTitleSize(.17);
		H_comp->GetYaxis()->SetLabelSize(.11);
		H_comp->GetXaxis()->SetLabelSize(.11);	
		H_comp->GetYaxis()->SetTitleOffset(.25);
	
		TLine *line0 = new TLine(xLow,0,xMax,0);
		TLine *line2u = new TLine(xLow,2,xMax,2);
		TLine *line2d = new TLine(xLow,-2,xMax,-2);
	
		H_comp->SetMinimum(-8);
		H_comp->SetMaximum(8);
		H_comp->SetMarkerStyle(21);
		H_comp->SetMarkerSize(0.5);
	
		H_comp->Draw("p");
		line0->Draw("SAME");
		line2u->Draw("SAME");
		line2d->Draw("SAME");
		
		
		pad2r->cd();
	
		H_compr->GetYaxis()->SetTitle("Frac. Diff.");
		H_compr->GetYaxis()->SetTitleFont(132);
		H_compr->GetYaxis()->SetTitleSize(.17);
		H_compr->GetYaxis()->SetLabelSize(.11);
		H_compr->GetXaxis()->SetLabelSize(.11);	
		H_compr->GetYaxis()->SetTitleOffset(.25);
		
		H_compr->SetMinimum(-2);
		H_compr->SetMaximum(2);
		H_compr->SetLineColor(kRed);
		H_compr->SetLineWidth(2);
		H_compr->SetMarkerColor(kRed);
		H_compr->SetMarkerStyle(1);
		H_compr->SetMarkerSize(0.0);
	
		H_compr->Draw("ep");
		line0->Draw("SAME");

	}
	
	if (Use_integral) tag += '_integral';

	c1->Print("PlotsMuNuSubInt/"+varname+"_"+tag+".png");
	c1->Print("PlotsMuNuSubInt/"+varname+"_"+tag+".pdf");

	
	TIter next(gDirectory->GetList());
	TObject* obj;
	while(obj= (TObject*)next()){
		if(obj->InheritsFrom(TH1::Class())){
			obj->Delete();
		}
	}

}

void MakePlotsMuNuSubInt()
{


	// Load Files and Trees:
	gROOT->ProcessLine(".x LoadCastorFiles.C");

	// Cut Conditions

	//------Choose which lq mass you want here----
	TString lq_choice = "lqmunu400";


	TString lumi ="4700"  ;
	TString cut_data ="(Pt_muon1>40)*(MET_pf>45.0)";
	cut_data +="*(Pt_muon2<15)";
	////  TString cut_data ="(Pt_muon1>30)*(Pt_muon2>30)";
	////  cut_data +="*(Pt_W<40)*(Pt_W>0)";
	cut_data +="*(Pt_ele1<25.0)";
	cut_data +="*(Pt_pfjet1>30)*(Pt_pfjet2>30)";
	cut_data +="*(abs(Eta_muon1)<2.1)";
	//cut_data +="*(FailIDJetPT25<0.5)";
	cut_data +="*(ST_pf_munu>250.0)";
	cut_data +="*(abs(deltaPhi_pfjet1pfMET)>.5)";
	////  cut_data +="*(deltaPhi_pfjet2pfMET>.5)";
	////  cut_data +="*(deltaPhi_pfjet1pfMET<2.65)";
	cut_data +="*(abs(deltaPhi_muon1pfMET)>.8)";
	cut_data +="*(FailIDPFThreshold<25.0)";
	cut_data +="*(MT_muon1pfMET>50.0)";
	 //cut_data +="*(PFJetCount>2.5)";

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
	  //cut_data +="*(PFJetCount>3.5)";
	
	//  cut_data +="*(MT_muon1pfMET>125.0)";
	//cut_data +="*(MT_muon1pfMET<110.0)";
	//cut_data +="*(MT_muon1pfMET>50.0)";
	//cut_data +="*(N_Vertices> 5.5)";

	TString cut_mc = lumi+"*weight_pileup4p7fb*("+cut_data+")";
	cut_data += "*(LowestUnprescaledTriggerPass>0.5)";


	float WNormalization = 1.188;
	bool use_integral = false;
	TString filetag ="";
	TString xtag ="";


	

	// ------------- Normalization Calculation                         -------------- //

	if (WNormalization == 1.00){
		std::cout<<"\n\n W Normalization is unity. Program will calculate W rescaling factor and exit.\n\n"<<std::endl;
		filetag ="2011Data_NormalizationSelection";
		xtag =" [W Normalization Condition]";
		TString NormCondition ="*(ST_pf_munu>250)*(MT_muon1pfMET>50)*(MT_muon1pfMET<110)";
		
		fillHisto(lq_choice, cut_mc + NormCondition, cut_data+NormCondition, true, 60,50,110,"MT_muon1pfMET", false,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,10000,WNormalization,filetag);	
		gROOT->Reset();	gROOT->ProcessLine(".q;");
	}


	// ------------- Minimal Selection - Preselection Without ST Cut.  -------------- //

	filetag ="2011Data_MinimalSelection";
	xtag =" [Presel sans ST cut]";

	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,800,"M_pfjet1pfjet2", false,"","M_{jj}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	////fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,400,"MT_pfjet1pfjet2", false,"","M^{T}_{jj}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,8,"deltaR_pfjet1pfjet2", false,"","#Delta R (j_{1}j_{2})(GeV)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet1pfjet2", false,"","#Delta#phi (j_{1}j_{2})(GeV)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 60,0,600,"MT_pfjet1pfMET", false,"","M_{T}(j_{1},E_{T}^{miss})(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,400,"MT_pfjet2pfMET", false,"","M_{T}(j_{2},E_{T}^{miss})(GeV)" +xtag,lumi,10,WNormalization,filetag);

	//gROOT->Reset();	gROOT->ProcessLine(".q;");




	// ------------- Pre Selection - Preselection With ST>250 Cut      -------------- //

	cut_data +="*(ST_pf_munu>250.0)";
	cut_mc +="*(ST_pf_munu>250.0)";
	TString filetag ="2011Data_PreSelection";
	TString xtag =" [Preselection]";



	if (false) {

	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,400,"Pt_ele1", use_integral,"","p_{T} (e) (GeV)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3,3,"Eta_ele1", use_integral,"","eta_{T} (e) (GeV)" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,500,"MET_pf",        use_integral,"","E_{T}^{miss}(GeV)" +xtag  ,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data ,true,25,.-.5,24.5,"N_PileUpInteractions", use_integral,"","N_{PileUpInteractions}" +xtag,lumi,100,WNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data, true, 100,0,10,"METRatio_pfcalo", use_integral,"","METRatio_pfcalo " +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 100,0,10,"METRatio_lqpf", use_integral,"","METRatio_lqpf " +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 100,0,10,"METRatio_lqcalo", use_integral,"","METRatio_lqcalo " +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 100,0,10,"METRatio_lqpf", use_integral,"","METRatio_lqpf " +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 100,0,10,"METRatio_lqpf", use_integral,"","METRatio_lqpf " +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,500,"RangeTransverseMass_BestLQCombo", use_integral,"","RangeTransverseMass_BestLQCombo " +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,2.5,"RangeCenterTransverseMassRatio_BestLQCombo", use_integral,"","RangeCenterTransverseMassRatio_BestLQCombo " +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 50,-.5,49.5,"PFJetNeutralMultiplicity_pfjet1", use_integral,"","Neutral Mult. (Jet 1) " +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 25,0,1,"PFJetNeutralHadronEnergyFraction_pfjet1", use_integral,"","Neutral Had Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 25,0,1,"PFJetNeutralEmEnergyFraction_pfjet1", use_integral,"","NeutralEM Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 50,-.5,49.5,"PFJetNeutralMultiplicity_pfjet2", use_integral,"","Neutral Mult. (Jet 2) " +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 25,0,1,"PFJetNeutralHadronEnergyFraction_pfjet2", use_integral,"","Neutral Had Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 25,0,1,"PFJetNeutralEmEnergyFraction_pfjet2", use_integral,"","NeutralEM Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 42,-2,40,"FailIDCaloThreshold", use_integral,"","CaloJetID Failure p_{T} (GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 42,-2,40,"FailIDPFThreshold", use_integral,"","PFJetID Failure p_{T} (GeV)" +xtag,lumi,20,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data ,true,50,.-.5,49.5,"N_PileUpInteractions", use_integral,"","N_{PU}" +xtag,lumi,1000,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data ,true,25,.-.5,24.5,"N_Vertices", use_integral,"","N_{Vertices}" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data ,true,6,.-.5,5.5,"GlobalMuonCount", use_integral,"","N_{Global #mu}" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data ,true,6,.-.5,5.5,"TrackerMuonCount", use_integral,"","N_{Tracker #mu}" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data ,true,12,.-.5,11.5,"PFJetCount", use_integral,"","N_{PFJet}" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data ,true,8,.-.5,7.5,"BpfJetCount", use_integral,"","N_{BPFJet}" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,500,"MT_muon1pfMET", use_integral,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 25,70,170,"MT_muon1pfMET", use_integral,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,100,WNormalization,filetag+"ZOOMRegion");
	fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,400,"Pt_W",        use_integral,"","p_{T}(W)(GeV)" +xtag  ,lumi,5000,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_muon1pfMET", use_integral,"","#Delta #phi (#mu,E_{T}^{miss})" +xtag,lumi,10000,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet1pfMET", use_integral,"","#Delta #phi (j_{1},E_{T}^{miss})" +xtag,lumi,10000,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet2pfMET", use_integral,"","#Delta #phi (j_{2},E_{T}^{miss})" +xtag,lumi,10000,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPFJet", use_integral,"","#Delta #phi (E_{T}^{miss},Closest PFJet)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPFJet", use_integral,"","#Delta #phi (E_{T}^{miss},Furthest PFJet)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestCaloJet", use_integral,"","#Delta #phi (E_{T}^{miss},Closest CaloJet)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestCaloJet", use_integral,"","#Delta #phi (E_{T}^{miss},Furthest CaloJet)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPT10PFJet", use_integral,"","#Delta #phi (E_{T}^{miss},Closest 10GeV PFJet)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPT10PFJet", use_integral,"","#Delta #phi (E_{T}^{miss},Furthest 10GeV PFJet)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPT10CaloJet", use_integral,"","#Delta #phi (E_{T}^{miss},Closest 10GeV CaloJet)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPT10CaloJet", use_integral,"","#Delta #phi (E_{T}^{miss},Furthest 10GeV CaloJet)" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 60,0,30,"EcalIso_muon1", use_integral,"","ECAL Iso_{#mu} (GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,3,"HcalIso_muon1", use_integral,"","HCAL Iso (#mu)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 35,0,3.5,"TrkIso_muon1", use_integral,"","Track Iso (#mu)" +xtag,lumi,10,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,400,"Pt_muon1", use_integral,"","p_{T} (#mu) (GeV)" +xtag,lumi,100,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,50,"PtError_muon1", use_integral,"","#sigma(p_{T}) (#mu) (GeV)" +xtag,lumi,10,WNormalization,filetag);	
	fillHisto(lq_choice, cut_mc, cut_data, true, 42,-2.1,2.1,"Eta_muon1", use_integral,"","#eta (#mu)" +xtag,lumi,10000,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,.001,"EtaError_muon1", use_integral,"","#sigma(#eta) (#mu)" +xtag,lumi,10000,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true,30,-3.141593,3.141593,"Phi_muon1", use_integral,"","#phi (#mu)" +xtag,lumi,2000,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,.0005,"PhiError_muon1", use_integral,"","#sigma(#phi) (#mu)" +xtag,lumi,1000,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,.0008,"QOverPError_muon1", use_integral,"","#sigma(Q/p)_{#mu}(GeV)" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data, true, 60,0,600,"Pt_pfjet1", use_integral,"","p_{T} (jet_{1}) (GeV)" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,500,"Pt_pfjet2", use_integral,"","p_{T} (jet_{2}) (GeV)" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3.0,3.0,"Eta_pfjet1", use_integral,"","#eta (jet_{1})" +xtag,lumi,10000,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3.0,3.0,"Eta_pfjet2", use_integral,"","#eta (jet_{2})" +xtag,lumi,10000,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data, true, 60,200,1200,"ST_pf_munu", use_integral,"","S_{T} (GeV)" +xtag,lumi,500,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data, true, 100,0,2000,"M_bestmupfjet_munu", use_integral,"","M_{#mu jet}" +xtag,lumi,1000,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,800,"M_pfjet1pfjet2", use_integral,"","M_{jj}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 60,0,600,"MT_pfjet1pfMET", use_integral,"","M_{T}(j_{1},E_{T}^{miss})(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,400,"MT_pfjet2pfMET", use_integral,"","M_{T}(j_{2},E_{T}^{miss})(GeV)" +xtag,lumi,10,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,400,"MT_pfjet1pfjet2", use_integral,"","M^{T}_{jj}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,8,"deltaR_pfjet1pfjet2", use_integral,"","#Delta R (j_{1}j_{2})(GeV)" +xtag,lumi,10000,WNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet1pfjet2", use_integral,"","#Delta#phi (j_{1}j_{2})(GeV)" +xtag,lumi,1000,WNormalization,filetag);

	}


	////// -------------    Full Selection      -------------- //


	if (true){

	// LQ 250
	filetag = "2011Data_FullSelection_lqmunu400";
	xtag = " [Full Selection]";
	lq_choice = "lqmunu400";

	TString cut_full_data = cut_data +"*(ST_pf_munu > 600)*(MET_pf > 135)*(M_bestmupfjet_munu > 310)*(Pt_muon1 > 80)";
	TString cut_full_mc = cut_mc +"*(ST_pf_munu > 600)*(MET_pf > 135)*(M_bestmupfjet_munu > 310)*(Pt_muon1 > 80)";

	fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 25,0.0,2000.0,"M_bestmupfjet_munu", use_integral,"","M_{#mu j}" +xtag,lumi,40,WNormalization,filetag);
	fillHisto(lq_choice,  cut_full_mc, cut_full_data, use_integral, 25,250,2250,"ST_pf_munu", use_integral,"","S_{T} (GeV)" +xtag,lumi,50,WNormalization,filetag);
	//fillHisto(lq_choice,  cut_full_mc, cut_full_data, use_integral, 25,-3.141593,3.141593,"deltaPhi_pfjet1pfMET", use_integral,""," #Delta#phi (j_{1},MET)" +xtag,lumi,50,WNormalization,filetag);	
	//fillHisto(lq_choice,  cut_full_mc, cut_full_data, use_integral, 25,-3.141593,3.141593,"deltaPhi_pfjet2pfMET", use_integral,""," #Delta#phi (j_{2},MET)" +xtag,lumi,50,WNormalization,filetag);	
	fillHisto(lq_choice,  cut_full_mc, cut_full_data, use_integral, 50,0,1000,"MT_muon1pfMET", use_integral,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 60,0,900,"Pt_pfjet1", use_integral,"","p_{T} (jet_{1}) (GeV)" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 60,0,900,"Pt_pfjet2", use_integral,"","p_{T} (jet_{2}) (GeV)" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 35,135,835,"MET_pf",        use_integral,"","E_{T}^{miss}(GeV)" +xtag  ,lumi,100,WNormalization,filetag);
	fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 30,0,600,"Pt_muon1", use_integral,"","p_{T} (#mu) (GeV)" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(lq_choice, cut_full_mc, cut_full_data ,use_integral,12,.-.5,11.5,"PFJetCount", use_integral,"","N_{PFJet}" +xtag,lumi,100,WNormalization,filetag);	
	fillHisto(lq_choice, cut_full_mc, cut_full_data ,use_integral,50,.-.5,49.5,"N_Vertices", use_integral,"","N_{Vertices}" +xtag,lumi,1000,WNormalization,filetag);
	fillHisto(lq_choice, cut_full_mc, cut_full_data ,use_integral,50,.-.5,49.5,"N_PileUpInteractions", use_integral,"","N_{PU}" +xtag,lumi,1000,WNormalization,filetag);
	
	
		
	// LQ 500
	filetag = "2011Data_FullSelection_lqmunu550";
	xtag = " [Full Selection]";
	lq_choice = "lqmunu550";

	TString cut_full_data = cut_data +"*(ST_pf_munu > 870)*(MET_pf > 195)*(M_bestmupfjet_munu > 380)*(Pt_muon1 > 80)";
	TString cut_full_mc = cut_mc+"*(ST_pf_munu > 870)*(MET_pf > 195)*(M_bestmupfjet_munu > 380)*(Pt_muon1 > 80)";

	fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 25,0.0,2000.0,"M_bestmupfjet_munu", use_integral,"","M_{#mu j}" +xtag,lumi,40,WNormalization,filetag);
	fillHisto(lq_choice,  cut_full_mc, cut_full_data, false , 25,250,2250,"ST_pf_munu", use_integral,"","S_{T} (GeV)" +xtag,lumi,50,WNormalization,filetag);
	//fillHisto(lq_choice,  cut_full_mc, cut_full_data, false , 25,-3.141593,3.141593,"deltaPhi_pfjet1pfMET", use_integral,""," #Delta#phi (j_{1},MET)" +xtag,lumi,50,WNormalization,filetag);
	//fillHisto(lq_choice,  cut_full_mc, cut_full_data, false , 25,-3.141593,3.141593,"deltaPhi_pfjet2pfMET", use_integral,""," #Delta#phi (j_{2},MET)" +xtag,lumi,50,WNormalization,filetag);	
	fillHisto(lq_choice,  cut_full_mc, cut_full_data, false , 40,0,2200,"MT_muon1pfMET", use_integral,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,10,WNormalization,filetag);
	fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 30,0,900,"Pt_pfjet1", use_integral,"","p_{T} (jet_{1}) (GeV)" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 30,0,900,"Pt_pfjet2", use_integral,"","p_{T} (jet_{2}) (GeV)" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 35,195,895,"MET_pf",        use_integral,"","E_{T}^{miss}(GeV)" +xtag  ,lumi,100,WNormalization,filetag);	
	fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 30,0,600,"Pt_muon1", use_integral,"","p_{T} (#mu) (GeV)" +xtag,lumi,100,WNormalization,filetag);
	fillHisto(lq_choice, cut_full_mc, cut_full_data ,false ,12,.-.5,11.5,"PFJetCount", use_integral,"","N_{PFJet}" +xtag,lumi,100,WNormalization,filetag);		
	fillHisto(lq_choice, cut_full_mc, cut_full_data ,false ,50,.-.5,49.5,"N_Vertices", use_integral,"","N_{Vertices}" +xtag,lumi,1000,WNormalization,filetag);
	fillHisto(lq_choice, cut_full_mc, cut_full_data ,false ,50,.-.5,49.5,"N_PileUpInteractions", use_integral,"","N_{PU}" +xtag,lumi,1000,WNormalization,filetag);
	
	}
	gROOT->Reset(); gROOT->ProcessLine(".q;");

}
