
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
	//if (!usevar) 
	//{
		//std::cout<<"\nWARNING: Branch for variable "<<var<<"  not found. Skipping plot for this variable. \n"<<std::endl;
		//return;
	//}

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
	//h_ttbar->Scale(165.0/121.0);


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
	std::cout<<"QCD  : "<<h_qcd->Integral()<<"  +- "<<h_qcd->Integral()*pow(1.0*(h_qcd->GetEntries()),-0.5)<<std::endl;

	
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
	//H_bkg->Add(h_qcd);
	H_bkg->Add(h_zjets);
	H_bkg->Add(h_singtop);


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
	//H_stack->Add(H_zjets);
	//H_stack->Add(H_singtop);
	H_stack->Add(H_ttbar);
	H_stack->Add(H_wjets);
	H_stack->Add(H_qcd);

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
	//leg->AddEntry(H_zjets,"Z/#gamma* + jets");
	leg->AddEntry(H_wjets,"W + jets");
	leg->AddEntry(H_ttbar,"t#bar{t}");
	//leg->AddEntry(H_singtop,"Single Top");
	leg->AddEntry(H_bkg,"Other backgrounds");
	leg->AddEntry(H_qcd,"QCD");

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

		}

		//std::cout<<"Chi^2 for this distribution is:  "<< chi2<<std::endl;
	}
	h_comp->GetYaxis()->SetTitle("Poisson N(#sigma) Diff");


	TLine *line0 = new TLine(xLow,0,xMax,0);
	TLine *line2u = new TLine(xLow,10,xMax,10);
	TLine *line2d = new TLine(xLow,-10,xMax,-10);

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



	c1->Print("PlotsMuNuSubQCDEstimation/"+varname+"_"+tag+".png");
	c1->Print("PlotsMuNuSubQCDEstimation/"+varname+"_"+tag+".pdf");

	
	TIter next(gDirectory->GetList());
	TObject* obj;
	while(obj= (TObject*)next()){
		if(obj->InheritsFrom(TH1::Class())){
			obj->Delete();
		}
	}

}

void MakePlotsMuNuSubQCDEstimation()
{


	// Load Files and Trees:
	 gROOT->ProcessLine(".x LoadCastorFilesQCDStudy.C");

	// Cut Conditions

	TString lumi ="2000"  ;
	TString cut_data ="(Pt_muon1>40)";
	cut_data +="*(Pt_muon2<15)";
	//cut_data += "*(TrackerkIsoSumPT_muon1 < 3.0)";
	////  TString cut_data ="(Pt_muon1>30)*(Pt_muon2>30)";
	////  cut_data +="*(Pt_W<40)*(Pt_W>0)";
	//cut_data +="*(Pt_ele1<15.0)";
	//cut_data +="*(Pt_pfjet1>30)*(Pt_pfjet2>30)";
	//cut_data +="*(abs(Eta_muon1)<2.1)";
	////cut_data +="*(FailIDJetPT25<0.5)";
	////cut_data +="*(ST_pf_munu>250.0)";
	//cut_data +="*(abs(deltaPhi_pfjet1pfMET)>.5)";
	//////  cut_data +="*(deltaPhi_pfjet2pfMET>.5)";
	//////  cut_data +="*(deltaPhi_pfjet1pfMET<2.65)";
	//cut_data +="*(abs(deltaPhi_muon1pfMET)>.8)";

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



cut_mc += "*(";
cut_mc += "((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)*(0.0752233034121))+";
cut_mc += "((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)*(0.361994702942))+";
cut_mc += "((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)*(0.787119271271))+";
cut_mc += "((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)*(1.31779962348))+";
cut_mc += "((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)*(1.76293927848))+";
cut_mc += "((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)*(1.99059826007))+";
cut_mc += "((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)*(2.00731349758))+";
cut_mc += "((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)*(1.82730847106))+";
cut_mc += "((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)*(1.56802352509))+";
cut_mc += "((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)*(1.26852456276))+";
cut_mc += "((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)*(0.993808726427))+";
cut_mc += "((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)*(0.760786688881))+";
cut_mc += "((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)*(0.566015549542))+";
cut_mc += "((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)*(0.41722578577))+";
cut_mc += "((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)*(0.303388545407))+";
cut_mc += "((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)*(0.220634364549))+";
cut_mc += "((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)*(0.155308189438))+";
cut_mc += "((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)*(0.110585960196))+";
cut_mc += "((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)*(0.0776646451932))+";
cut_mc += "((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)*(0.0543492223545))+";
cut_mc += "((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)*(0.037244740125))+";
cut_mc += "((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)*(0.0259826507587))+";
cut_mc += "((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)*(0.0175412449088))+";
cut_mc += "((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)*(0.0118325534711))+";
cut_mc += "((N_PileUpInteractions > 23.5)*(0.00))";
cut_mc += ")";


	float WNormalization = 0.89;
	TString filetag ="";
	TString xtag ="";


	TString cut_mc_store = cut_mc;
	TString cut_data_store = cut_data;




	TString filetag ="2011Data_LowMET";
	TString xtag =" [MET<10, No Isolation]";
		
	cut_mc = cut_mc_store + "*(MET_pf<10.0)";
	cut_data = cut_data_store + "*(MET_pf<10.0)";
	fillHisto(cut_mc, cut_data, true, 80,0,400,"TrackerkIsoSumPT_muon1", false,"","Track Iso (#mu 1)" +xtag,lumi,10,WNormalization,filetag);
	
	gROOT->Reset(); gROOT->ProcessLine(".q;");
	
	
	TString filetag ="2011Data_HighMET";
	TString xtag =" [MET>10, No Isolation]";
		
	cut_mc = cut_mc_store + "*(MET_pf>10.0)";
	cut_data = cut_data_store + "*(MET_pf>10.0)";

	fillHisto(cut_mc, cut_data, true, 80,0,400,"TrackerkIsoSumPT_muon1", false,"","Track Iso (#mu 1)" +xtag,lumi,10,WNormalization,filetag);




		//FullSel 250 
	cut_mc = cut_mc_store + "*((Pt_muon1>45)*(Pt_muon2<15.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5)*(FailIDPFThreshold<25.0)*(ST_pf_munu > 440)*(MET_pf > 90)*(M_bestmupfjet_munu > 120)";
	cut_data = cut_data_store + "*((Pt_muon1>45)*(Pt_muon2<15.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5)*(FailIDPFThreshold<25.0)*(ST_pf_munu > 440)*(MET_pf > 90)*(M_bestmupfjet_munu > 120)";

	
	fillHisto(cut_mc, cut_data, true, 80,0,40000,"TrackerkIsoSumPT_muon1", false,"","Track Iso (#mu 1)" +xtag,lumi,10,WNormalization,filetag);
		
		
	//FullSel 350 
	cut_mc = cut_mc_store + "*((Pt_muon1>45)*(Pt_muon2<15.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5)*(FailIDPFThreshold<25.0)*(ST_pf_munu > 540)*(MET_pf > 125)*(M_bestmupfjet_munu > 280)";
	cut_data = cut_data_store + "*((Pt_muon1>45)*(Pt_muon2<15.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5)*(FailIDPFThreshold<25.0)*(ST_pf_munu > 540)*(MET_pf > 125)*(M_bestmupfjet_munu > 280)";



	fillHisto(cut_mc, cut_data, true, 80,0,40000,"TrackerkIsoSumPT_muon1", false,"","Track Iso (#mu 1)" +xtag,lumi,10,WNormalization,filetag);
	
	
	//FullSel 400
	cut_mc = cut_mc_store + "*((Pt_muon1>45)*(Pt_muon2<15.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5)*(FailIDPFThreshold<25.0)*(ST_pf_munu > 600)*(MET_pf > 135)*(M_bestmupfjet_munu > 310)";
	cut_data = cut_data_store + "*((Pt_muon1>45)*(Pt_muon2<15.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5)*(FailIDPFThreshold<25.0)*(ST_pf_munu > 600)*(MET_pf > 135)*(M_bestmupfjet_munu > 310)";



	fillHisto(cut_mc, cut_data, true, 80,0,40000,"TrackerkIsoSumPT_muon1", false,"","Track Iso (#mu 1)" +xtag,lumi,10,WNormalization,filetag);

	




	gROOT->Reset(); gROOT->ProcessLine(".q;");

}
