
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
	while(obj= (TObject*)next())
	{
		if (var == obj->GetName()) usevar = true;
	}

	//if (!usevar)
	//{
	//std::cout<<"\nWARNING: Branch for variable "<<var<<"  not found. Skipping plot for this variable. \n"<<std::endl;
	//return;
	//}

	//if (drawSub) TCanvas *c1 = new TCanvas("c1","",800,800);
	//if (!drawSub) TCanvas *c1 = new TCanvas("c1","",800,480);

	//if (drawSub) TPad *pad1 = new TPad("pad1","The pad 60% of the height",0.0,0.4,1.0,1.0,0);
	//if (!drawSub) TPad *pad1 = new TPad("pad1","The pad 60% of the height",0.0,0.0,1.0,1.0,0);
	//if (drawSub) TPad *pad2 = new TPad("pad2","The pad 20% of the height",0.0,0.2,1.0,0.4,0);
	//if (drawSub) TPad *pad2r = new TPad("pad2r","The ptad 20% of the height",0.0,0.0,1.0,0.2,0);

	if (drawSub) TCanvas *c1 = new TCanvas("c1","",800,680);
	if (!drawSub) TCanvas *c1 = new TCanvas("c1","",800,480);

	if (drawSub) TPad *pad1 = new TPad("pad1","The pad 60% of the height",0.0,0.25,1.0,1.0,0);
	if (!drawSub) TPad *pad1 = new TPad("pad1","The pad 60% of the height",0.0,0.0,1.0,1.0,0);
	//if (drawSub) TPad *pad2 = new TPad("pad2","The pad 20% of the height",0.0,0.2,1.0,0.4,0);
	if (drawSub) TPad *pad2r = new TPad("pad2r","The ptad 20% of the height",0.0,0.0,1.0,0.25,0);

	pad1->Draw();
	//if (drawSub) pad2->Draw();
	if (drawSub) pad2r->Draw();

	pad1->cd();
	pad1->SetLogy();
	//pad1->SetLogx();

	gStyle->SetOptLogy();
	//gStyle->SetOptLogx();

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
	//qcd->Draw(var+">>H_qcd",cut_mc);
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
	H_zjets->Scale(1.27);
	H_ttbar->Scale(0.88);
	H_vvjets->Scale(0.92);
	H_singtop->Scale(0.92);
	H_lq->Scale(0.92);
	// ***************************************         SCREEN READOUT       *************************************************** //

	Double_t Nd = H_data->Integral();
	Double_t Nmc = H_zjets->Integral()+H_ttbar->Integral()+H_vvjets->Integral()+H_wjets->Integral()+H_singtop->Integral()+H_qcd->Integral();
	Double_t Nw = H_wjets->Integral();
	Double_t Nt = H_ttbar->Integral();
	Double_t Nz = H_zjets->Integral();
	Double_t Nlq = H_lq->Integral();
	Double_t N_other_w = Nmc - Nw;
	Double_t N_other_tt = Nmc - Nt;

	std::cout<<"Data   :"<<Nd<<std::endl;
	std::cout<<"All MC :"<<Nmc<<std::endl;
	std::cout<<"TT   :"<<H_ttbar->Integral()<<"  +-"<<H_ttbar->Integral()*pow(1.0*(H_ttbar->GetEntries()),-0.5)<<"   --- Entries:  "<<H_ttbar->GetEntries()<<std::endl;
	std::cout<<"W    :"<<H_wjets->Integral()<<"  +-"<<H_wjets->Integral()*pow(1.0*(H_wjets->GetEntries()),-0.5)<<"   --- Entries:  "<<H_wjets->GetEntries()<<std::endl;
	std::cout<<"LQ    :"<<H_lq->Integral()<<"  +-"<<H_lq->Integral()*pow(1.0*(H_lq->GetEntries()),-0.5)<<std::endl;

	Double_t fac_w = (Nd-N_other_w)/Nw;

	Double_t fac_werr = Nd ;
	fac_werr +=  (H_ttbar->Integral())*(H_ttbar->Integral())/(H_ttbar->GetEntries());
	fac_werr +=  (H_zjets->Integral())*(H_zjets->Integral())/(H_zjets->GetEntries());
	fac_werr +=  (H_vvjets->Integral())*(H_vvjets->Integral())/(H_vvjets->GetEntries());
	fac_werr +=  (H_singtop->Integral())*(H_singtop->Integral())/(H_singtop->GetEntries());
	fac_werr = fac_werr/((Nd-N_other_w)*(Nd-N_other_w));
	fac_werr += 1.0/(1.0*(H_wjets->GetEntries()));
	fac_werr = pow(fac_werr,0.5);
	fac_werr *= fac_w;
	std::cout<<"W Scale factor: "<<fac_w<<"  +-  "<<fac_werr<<std::endl;

	Double_t fac_tt = (Nd-N_other_tt)/Nt;

	Double_t fac_tterr = Nd ;
	fac_tterr +=  (H_wjets->Integral())*(H_wjets->Integral())/(H_wjets->GetEntries());
	fac_tterr +=  (H_zjets->Integral())*(H_zjets->Integral())/(H_zjets->GetEntries());
	fac_tterr +=  (H_vvjets->Integral())*(H_vvjets->Integral())/(H_vvjets->GetEntries());
	fac_tterr +=  (H_singtop->Integral())*(H_singtop->Integral())/(H_singtop->GetEntries());
	fac_tterr = fac_tterr/((Nd-N_other_tt)*(Nd-N_other_tt));
	fac_tterr += 1.0/(1.0*(H_ttbar->GetEntries()));
	fac_tterr = pow(fac_tterr,0.5);
	fac_tterr *= fac_tt;
	std::cout<<"TT Scale factor: "<<fac_tt<<"  +-  "<<fac_tterr<<std::endl;

	//Double_t sigma_Nw = Nw*pow(1.0*(H_wjets->GetEntries()),-0.5);
	//Double_t sigma_Nt = Nt*pow(1.0*(H_ttbar->GetEntries()),-0.5);

	//Double_t sigma_N_other = 0.0;
	//if (H_ttbar->GetEntries()>0) sigma_N_other += pow((H_ttbar->Integral()*pow((1.0*H_ttbar->GetEntries()),-0.5)),2);
	//if (H_zjets->GetEntries()>0) sigma_N_other += pow((H_zjets->Integral()*pow((1.0*H_zjets->GetEntries() ),-0.5)),2);
	//if (H_vvjets->GetEntries()>0) sigma_N_other += pow((H_vvjets->Integral()*pow((1.0*H_vvjets->GetEntries() ),-0.5)),2);
	//if (H_singtop->GetEntries()>0) sigma_N_other += pow((H_singtop->Integral()*pow((1.0*singtop->GetEntries()),-0.5)),2);
	//if (H_qcd->GetEntries()>0) sigma_N_other +=pow((H_qcd->Integral()*pow((1.0*H_qcd->GetEntries()),-0.5)),2);
	//sigma_N_other = sqrt(sigma_N_other);

	//Double_t sigma_N_other2 = 0.0;
	//if (H_wjets->GetEntries()>0) sigma_N_other2 += pow((H_wjets->Integral()*pow((1.0*H_wjets->GetEntries()),-0.5)),2);
	//if (H_zjets->GetEntries()>0) sigma_N_other2 += pow((H_zjets->Integral()*pow((1.0*H_zjets->GetEntries() ),-0.5)),2);
	//if (H_vvjets->GetEntries()>0) sigma_N_other2 += pow((H_vvjets->Integral()*pow((1.0*H_vvjets->GetEntries() ),-0.5)),2);
	//if (H_singtop->GetEntries()>0) sigma_N_other2 +=pow( (H_singtop->Integral()*pow((1.0*singtop->GetEntries()),-0.5)),2);
	//if (H_qcd->GetEntries()>0) sigma_N_other2 +=pow( (H_qcd->Integral()*pow((1.0*H_qcd->GetEntries()),-0.5)),2);
	//sigma_N_other2 = sqrt(sigma_N_other2);

	//Double_t sigam_Nd = sqrt(Nd);
	//Double_t fac_Numerator = Nd - N_other;
	//Double_t fac_Denominator = Nw;
	//Double_t fac = fac_Numerator/fac_Denominator;

	//Double_t sigma_fac_Numerator = sqrt( pow( sigam_Nd ,2.0) + pow( sigma_N_other ,2.0) ) ;
	//Double_t sigma_fac_Denominator = sigma_Nw;
	//Double_t sigma_fac_over_fac = pow( pow((sigma_fac_Numerator/fac_Numerator),2.0)    +  pow((sigma_fac_Denominator/fac_Denominator),2.0)    ,0.5);
	//Double_t sigma_fac = sigma_fac_over_fac*fac;

	//std::cout<<"W Scale Factor:  "<<fac<<"  +-  "<<sigma_fac<<std::endl;

	//Double_t fac2_Numerator = Nd - N_other2 ;
	//Double_t fac2_Denominator = Nt;
	//Double_t fac2 = fac2_Numerator/fac2_Denominator;

	//Double_t sigma_fac2_Numerator = sqrt( pow( sigam_Nd ,2.0) + pow( sigma_N_other2 ,2.0) ) ;
	////std::cout<<"sN "<< sigma_fac2_Numerator<<std::endl;
	////std::cout<<"N  "<<fac2_Numerator<<std::endl;

	//Double_t sigma_fac2_Denominator = sigma_Nt;

	////std::cout<<"sD "<< sigma_fac2_Denominator<<std::endl;
	////std::cout<<"D  "<<fac2_Denominator<<std::endl;

	//Double_t sigma_fac2_over_fac2 = pow( pow((sigma_fac2_Numerator/fac2_Numerator),2.0)    +  pow((sigma_fac2_Denominator/fac2_Denominator),2.0)    ,0.5);
	//Double_t sigma_fac2 = sigma_fac2_over_fac2*fac2;

	//std::cout<<"TT Scale factor:  "<<fac2<<"  +-  "<<sigma_fac2<<std::endl;

	// *******************************************************************************************************************************

	TH1F* H_bkg = new TH1F("H_bkg","",nBins,xLow,xMax);
	H_bkg->Add(H_vvjets);
	H_bkg->Add(H_qcd);
	H_bkg->Add(H_zjets);
	H_bkg->Add(H_singtop);
	


	float num_lq = 0.0;
	float num_zjets = 0.0;
	float num_wjets = 0.0;
	float num_singtop = 0.0;
	float num_qcd = 0.0;
	float num_ttbar = 0.0;
	float num_bkg = 0.0;
	float num_data = 0.0;

	int nbinsx = H_data->GetXaxis()->GetNbins();

	if (Use_integral)
	{
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

	//H_lq->SetLineStyle();
	H_lq->SetLineColor(8);
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
	//H_stack->Add(H_zjets);
	//H_stack->Add(H_singtop);
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
	H_data->SetMarkerSize(0.7);
	gStyle->SetOptStat(0);
	H_data->Draw("E");

	H_stack->Draw("SAME");
	H_lq->Draw("SAME");
	H_data->Draw("SAMEE");
	TLegend* leg = new TLegend(0.6,0.63,0.91,0.91,"","brNDC");
	leg->SetTextFont(132);
	leg->SetFillColor(0);
	leg->SetBorderSize(0);
	leg->AddEntry(H_data,"Data 2011, 4.98 fb^{-1}");
	//leg->AddEntry(H_zjets,"Z/#gamma* + jets");
	leg->AddEntry(H_wjets,"W + jets");
	leg->AddEntry(H_ttbar,"t#bar{t}");
	//leg->AddEntry(H_singtop,"Single Top");
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
	//c1->SetLogx();

	H_data->SetMinimum(0.010);
	H_data->SetMaximum(1.2*extrascalefactor*(H_data->GetMaximum()));

	TLatex* txt =new TLatex((xMax-xLow)*.05+xLow,.1*H_data->GetMaximum(),"CMS 2011");
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

	if (drawSub)
	{
		//pad2->cd();

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

			if (var == "N_Vertices") std::cout<<"Optional Vertex Rescaling Procedure: \n\ncut_mc += \"*(0\";"<<std::endl;
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

				//float lhs = datmean - H_data->GetBinWidth();
				//float rhs = datmean + H_data->GetBinWidth();

				float lhs = H_data->GetBinCenter(ibin) - 0.5*(xMax-xLow)/(1.0*nBins);
				float rhs = H_data->GetBinCenter(ibin) + 0.5*(xMax-xLow)/(1.0*nBins);
				//std::cout<<H_lq->GetBinCenter(ibin)<<"  LQ: "<<H_lq->GetBinContent(ibin)<<std::endl;
				if  (var == "N_Vertices" && ndat!=0 && nbg != 0) std::cout<< "cut_mc += \"+( ("<<var<<">"<<lhs<<")*("<<var<<"<"<<rhs<<")*("<<ndat/nbg<<") )\""<<";"<<std::endl;

			}
		}
		if (var == "N_Vertices") std::cout<<"cut_mc += \");\";"<<std::endl;

		H_comp->GetYaxis()->SetTitle("N(#sigma) Diff.");
		H_comp->GetYaxis()->SetTitleFont(132);
		H_comp->GetYaxis()->SetTitleSize(.15);
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

		//H_comp->Draw("p");
		//line0->Draw("SAME");
		//line2u->Draw("SAME");
		//line2d->Draw("SAME");

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
		H_compr->SetMarkerStyle(21);
		H_compr->SetMarkerSize(0.7);

		H_compr->Draw("ep");
		line0->Draw("SAME");

	}

	if (Use_integral) tag =tag+ "_integral";

	//c1->Print("PlotsMuNuSubInt/test.png");

	//c1->Print("PlotsMuNuSubInt/test.pdf");
	c1->Print("PlotsMuNuSubInt/"+varname+"_"+tag+".png");
	c1->Print("PlotsMuNuSubInt/"+varname+"_"+tag+".pdf");

	TIter next(gDirectory->GetList());
	TObject* obj;
	while(obj= (TObject*)next())
	{
		if(obj->InheritsFrom(TH1::Class()))
		{
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

	TString lumi ="4980"  ;
	TString cut_data ="(Pt_muon1>40)*(MET_pf>55.0)";
	cut_data +="*(Pt_muon2<40)";
	////  TString cut_data ="(Pt_muon1>30)*(Pt_muon2>30)";
	////  cut_data +="*(Pt_W<40)*(Pt_W>0)";
	cut_data +="*(Pt_HEEPele1<40.0)";
	cut_data +="*(Pt_pfjet1>40)*(Pt_pfjet2>40)";
	cut_data += "*(deltaR_muon1pfjet1>0.7)*(deltaR_muon1pfjet2>0.7)";
	cut_data +="*(abs(Eta_muon1)<2.1)";
	//cut_data +="*(FailIDJetPT25<0.5)";
	cut_data +="*(ST_pf_munu>250.0)";
	cut_data +="*(abs(deltaPhi_pfjet1pfMET)>.5)";
	////  cut_data +="*(deltaPhi_pfjet2pfMET>.5)";
	////  cut_data +="*(deltaPhi_pfjet1pfMET<2.65)";
	cut_data +="*(abs(deltaPhi_muon1pfMET)>.8)";
	cut_data +="*(FailIDPFThreshold<25.0)";
	cut_data +="*(MT_muon1pfMET>50.0)";
	cut_data += "*(pass_HBHENoiseFilter>0.5)*(pass_passBeamHaloFilterTight>0.5)*(pass_isTrackingFailure>0.5)";

	//cut_data +="*(abs(deltaPhi_pfjet1pfMET)>0.7)";
	//cut_data +="*(abs(deltaPhi_pfjet2pfMET)>.5)";
	//cut_data +="*(abs(deltaPhi_muon1pfMET)>1.0)";
	//cut_data +="*(PFJetCount>2.5)";

	//cut_data +="*(MET_pf>330)";
	//cut_data +="*(MET_pf<350)";
	//cut_data +="*(weight_pileup4p7fb>0.001)";

	//cut_data +="*(NGlobalMuons<2.5)";
	//cut_data +="*(Eta_pfjet1<0.0)";
	//cut_data +="*(Eta_pfjet2<0.0)";
	//cut_data +="*(MET_pfsig>50)";

	//cut_data +="&&(deltaPhi_muon1pfMET>2.10)";
	//cut_data +="*(Pt_Clusters_muon1<1.0)";
	//cut_data +="*(abs(MET_pf-Pt_muon1)/(MET_pf)>0.2)";
	//cut_data +="*(PFJetCount<3.5)";
	//cut_data +="*(((EcalIso_muon1 + HcalIso_muon1>0.1 + TrkIso_muon1)/Pt_muon1 )<0.15)";
	//cut_data +="*(BpfJetCount<1.5)";
	//cut_data +="*((N_Vertices>2.5)||(N_Vertices<1.5))";
	//cut_data +="*(ST_pf_munu>340.0)";
	//cut_data +="*(Pt_muon1>85)*(MET_pf>85.0)";
	//cut_data +="*(MT_muon1pfMET>125.0)";

	//cut_data +="*(deltaR_muon1closestPFJet>.7)";
	//cut_data +="*(deltaPhi_muon1caloMET<2.85)";
	//cut_data +="*(BpfJetCount>1.5)";
	//cut_data +="*(PFJetCount>3.5)";

	//cut_data +="*(MT_muon1pfMET>125.0)";
	//cut_data +="*(MT_muon1pfMET<110.0)";
	//cut_data +="*(MT_muon1pfMET>50.0)";
	//cut_data +="*(N_GoodVertices< 7.5)";
	//cut_data += "*(ST_pf_munu > 600)*(MET_pf > 135)*(M_bestmupfjet_munu > 310)*(Pt_muon1 > 80)";
	//cut_data += "*(PFJetTrackAssociatedVertex_pfjet1<0.5)*(PFJetTrackAssociatedVertex_pfjet2<0.5)";
	//cut_data += "*(((Pt_pfjet1-Pt_pfjet2)/(Pt_pfjet1+Pt_pfjet2))>0.01)";
	TString cut_mc = lumi+"*weight_pileup4p7fb_higgs*("+cut_data+")";
	cut_data += "*(LowestUnprescaledTriggerPass>0.5)*(pass_isBPTX0>0.5)";

	float WNormalization = 1.21;
	bool do_tt_est = false;
	bool use_integral = false;
	TString filetag ="";
	TString xtag ="";

	// ------------- Normalization Calculation                         -------------- //

	if (WNormalization == 1.00)
	{
		std::cout<<"\n\n W Normalization is unity. Program will calculate W rescaling factor and exit.\n\n"<<std::endl;
		filetag ="2011Data_NormalizationSelection";
		xtag =" [W Normalization Condition]";
		TString NormCondition ="*(ST_pf_munu>250)*(MT_muon1pfMET>50)*(MT_muon1pfMET<110)";

		fillHisto(lq_choice, cut_mc + NormCondition, cut_data+NormCondition, true, 60,50,110,"MT_muon1pfMET", false,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,10000,WNormalization,filetag);
		gROOT->Reset(); gROOT->ProcessLine(".q;");
	}

	if (do_tt_est)
	{
		std::cout<<"\n\n W Normalization is unity. Program will calculate TT rescaling factor and exit.\n\n"<<std::endl;
		filetag ="2011Data_NormalizationSelection";
		xtag =" [TT Normalization Condition]";

		std::cout<<" \n\n -------------- REQUIRING 4 OR MORE JETS -------------- "<<std::endl;
		TString NormCondition ="*(PFJetCount>3.5)";

		fillHisto(lq_choice, cut_mc + NormCondition, cut_data+NormCondition, true, 60,00,10000,"MT_muon1pfMET", false,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,10000,WNormalization,filetag);

		std::cout<<" \n\n -------------- REQUIRING 2 OR MORE BJETS -------------- "<<std::endl;

		NormCondition ="*(BpfJetCount>1.5)*(PFJetCount>3.5)";

		fillHisto(lq_choice, cut_mc + NormCondition, cut_data+NormCondition, true, 60,00,10000,"MT_muon1pfMET", false,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,10000,WNormalization,filetag);
		gROOT->Reset(); gROOT->ProcessLine(".q;");

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
	TString xtag =" [Preselelection]";

	if (false)
	{
		//fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,500,"MET_pf",        use_integral,"","E_{T}^{miss}(GeV)" +xtag  ,lumi,100,WNormalization,filetag);
		//fillHisto("lqmunu250", cut_mc, cut_data, false, 100,-0.5,0.5,"BDTLQToCMu_BetaHalf_M_250",        use_integral,"","BDT, 250 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu350", cut_mc, cut_data, false, 100,-0.5,0.5,"BDTLQToCMu_BetaHalf_M_350",        use_integral,"","BDT, 350 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu400", cut_mc, cut_data, false, 100,-0.5,0.5,"BDTLQToCMu_BetaHalf_M_400",        use_integral,"","BDT, 400 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu450", cut_mc, cut_data, false, 100,-0.5,0.5,"BDTLQToCMu_BetaHalf_M_450",        use_integral,"","BDT, 450 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu500", cut_mc, cut_data, false, 100,-0.5,0.5,"BDTLQToCMu_BetaHalf_M_500",        use_integral,"","BDT, 500 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu550", cut_mc, cut_data, false, 100,-0.5,0.5,"BDTLQToCMu_BetaHalf_M_550",        use_integral,"","BDT, 550 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu600", cut_mc, cut_data, false, 100,-0.5,0.5,"BDTLQToCMu_BetaHalf_M_600",        use_integral,"","BDT, 600 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu650", cut_mc, cut_data, false, 100,-0.5,0.5,"BDTLQToCMu_BetaHalf_M_650",        use_integral,"","BDT, 650 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu750", cut_mc, cut_data, false, 100,-0.5,0.5,"BDTLQToCMu_BetaHalf_M_750",        use_integral,"","BDT, 750 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu850", cut_mc, cut_data, false, 100,-0.5,0.5,"BDTLQToCMu_BetaHalf_M_850",        use_integral,"","BDT, 850 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);

		//float xstarting = 0.9;
		//fillHisto("lqmunu250", cut_mc, cut_data, false, 50,xstarting,1.0,"LikelihoodLQToCMu_BetaHalf_M_250",        use_integral,"","Likelihood, 250 GeV LQ" +xtag  ,lumi,10000,WNormalization,filetag);
		//xstarting = 0.99;
		//fillHisto("lqmunu350", cut_mc, cut_data, false, 50,xstarting,1.0,"LikelihoodLQToCMu_BetaHalf_M_350",        use_integral,"","Likelihood, 350 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//xstarting = 0.99999;
		//fillHisto("lqmunu400", cut_mc, cut_data, false, 50,xstarting,1.0,"LikelihoodLQToCMu_BetaHalf_M_400",        use_integral,"","Likelihood, 400 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//xstarting = 0.99999;
		//fillHisto("lqmunu450", cut_mc, cut_data, false, 50,xstarting,1.0,"LikelihoodLQToCMu_BetaHalf_M_450",        use_integral,"","Likelihood, 450 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//xstarting = 0.99999;
		//fillHisto("lqmunu500", cut_mc, cut_data, false, 50,xstarting,1.0,"LikelihoodLQToCMu_BetaHalf_M_500",        use_integral,"","Likelihood, 500 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//xstarting = 0.99999995;
		//fillHisto("lqmunu550", cut_mc, cut_data, false, 50,xstarting,1.0,"LikelihoodLQToCMu_BetaHalf_M_550",        use_integral,"","Likelihood, 550 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//xstarting = 0.999999;
		//fillHisto("lqmunu600", cut_mc, cut_data, false, 50,xstarting,1.0,"LikelihoodLQToCMu_BetaHalf_M_600",        use_integral,"","Likelihood, 600 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//xstarting = 0.9999995;
		//fillHisto("lqmunu650", cut_mc, cut_data, false, 50,xstarting,1.0,"LikelihoodLQToCMu_BetaHalf_M_650",        use_integral,"","Likelihood, 650 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//xstarting = 0.9999999;
		//fillHisto("lqmunu750", cut_mc, cut_data, false, 50,xstarting,1.0,"LikelihoodLQToCMu_BetaHalf_M_750",        use_integral,"","Likelihood, 750 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//xstarting = 0.99999995;
		//fillHisto("lqmunu850", cut_mc, cut_data, false, 50,xstarting,1.0,"LikelihoodLQToCMu_BetaHalf_M_850",        use_integral,"","Likelihood, 850 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);

		//fillHisto("lqmunu250", cut_mc, cut_data, false, 50,0.98,1.0,"LikelihoodDLQToCMu_BetaHalf_M_250",        use_integral,"","LikelihoodD, 250 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu350", cut_mc, cut_data, false, 50,0.98,1.0,"LikelihoodDLQToCMu_BetaHalf_M_350",        use_integral,"","LikelihoodD, 350 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu400", cut_mc, cut_data, false, 50,0.98,1.0,"LikelihoodDLQToCMu_BetaHalf_M_400",        use_integral,"","LikelihoodD, 400 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu450", cut_mc, cut_data, false, 50,0.98,1.0,"LikelihoodDLQToCMu_BetaHalf_M_450",        use_integral,"","LikelihoodD, 450 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu500", cut_mc, cut_data, false, 50,0.98,1.0,"LikelihoodDLQToCMu_BetaHalf_M_500",        use_integral,"","LikelihoodD, 500 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu550", cut_mc, cut_data, false, 50,0.98,1.0,"LikelihoodDLQToCMu_BetaHalf_M_550",        use_integral,"","LikelihoodD, 550 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu600", cut_mc, cut_data, false, 50,0.98,1.0,"LikelihoodDLQToCMu_BetaHalf_M_600",        use_integral,"","LikelihoodD, 600 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu650", cut_mc, cut_data, false, 50,0.98,1.0,"LikelihoodDLQToCMu_BetaHalf_M_650",        use_integral,"","LikelihoodD, 650 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu750", cut_mc, cut_data, false, 50,0.98,1.0,"LikelihoodDLQToCMu_BetaHalf_M_750",        use_integral,"","LikelihoodD, 750 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);
		//fillHisto("lqmunu850", cut_mc, cut_data, false, 50,0.98,1.0,"LikelihoodDLQToCMu_BetaHalf_M_850",        use_integral,"","LikelihoodD, 850 GeV LQ" +xtag  ,lumi,1000,WNormalization,filetag);


		gROOT->ProcessLine(".q;");
	}

	if (true)
	{

		//fillHisto(lq_choice, cut_mc, cut_data, true, 20,200,2200,"ST_pf_munu", use_integral,"","S_{T} (GeV)" +xtag,lumi,500,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 20,200,2200,"ST_pf_munu", true,"","S_{T} (GeV)" +xtag,lumi,500,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 10,1200,82200,"ST_pf_munu", use_integral,"","S_{T} (GeV)" +xtag,lumi,500,WNormalization,filetag+"highST");

		//fillHisto(lq_choice, cut_mc, cut_data, true, 10,1200,2200,"ST_pf_munu", true,"","S_{T} (GeV)" +xtag,lumi,500,WNormalization,filetag+"highST");

		//gROOT->ProcessLine(".q;");

		//TString LQpredict = " (run_number<2)*(1.0*( abs(MT_muon1pfjet1-MT_pfjet2pfMET) < abs(MT_muon1pfjet2-MT_pfjet1pfMET) ) + 2.0*( abs(MT_muon1pfjet1-MT_pfjet2pfMET) > abs(MT_muon1pfjet2-MT_pfjet1pfMET) )  -JetMatchMuon1)";
		//TString LQpredict = " (run_number<2)*(1.0*( abs(MT_muon1pfjet1-MT_pfjet2pfMET)/(MT_muon1pfjet1+MT_pfjet2pfMET) < abs(MT_muon1pfjet2-MT_pfjet1pfMET)/(MT_muon1pfjet2+MT_pfjet1pfMET) ) + 2.0*( abs(MT_muon1pfjet1-MT_pfjet2pfMET)/(MT_muon1pfjet1+MT_pfjet2pfMET) > abs(MT_muon1pfjet2-MT_pfjet1pfMET)/(MT_muon1pfjet2+MT_pfjet1pfMET) )  -JetMatchMuon1)";

		//TString LQpredict = " (run_number<2)*( 1.0*( abs(M_muon1pfjet1-MT_pfjet2pfMET) < abs(M_muon1pfjet2-MT_pfjet1pfMET) ) + 2.0*( abs(M_muon1pfjet1-MT_pfjet2pfMET) > abs(M_muon1pfjet2-MT_pfjet1pfMET) )  -JetMatchMuon1)";

		//TString LQpredict = " (run_number<2)*( 1.0*( abs(M_muon1pfjet1-MT_pfjet2pfMET)/(M_muon1pfjet1+MT_pfjet2pfMET) < abs(M_muon1pfjet2-MT_pfjet1pfMET)/(M_muon1pfjet2+MT_pfjet1pfMET) ) + 2.0*( abs(M_muon1pfjet1-MT_pfjet2pfMET)/(M_muon1pfjet1+MT_pfjet2pfMET) > abs(M_muon1pfjet2-MT_pfjet1pfMET)/(M_muon1pfjet2+MT_pfjet1pfMET) )  -JetMatchMuon1)";

		//TString LQpredict = " (run_number<2)*(1.0*( abs(MT_muon1pfjet1-MT_pfjet2pfMET) < abs(MT_muon1pfjet2-MT_pfjet1pfMET) ) + 2.0*( abs(MT_muon1pfjet1-MT_pfjet2pfMET) > abs(MT_muon1pfjet2-MT_pfjet1pfMET) )  -JetMatchMuon1)  -  (run_number<2)*( 1.0*( abs(M_muon1pfjet1-MT_pfjet2pfMET) < abs(M_muon1pfjet2-MT_pfjet1pfMET) ) + 2.0*( abs(M_muon1pfjet1-MT_pfjet2pfMET) > abs(M_muon1pfjet2-MT_pfjet1pfMET) )  -JetMatchMuon1)";

		//fillHisto(lq_choice, cut_mc, cut_data, true, 50,-2,2,"CosmicCompatibility_muon1", use_integral,"","Cosmic Compatibility Muon 1 " +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 50,-2,2,"BackToBackCompatibility_muon1", use_integral,"","B2b Compatibility Muon 1 " +xtag,lumi,1000,WNormalization,filetag);

		//fillHisto(lq_choice, cut_mc, cut_data, true, 5, -2.5,2.5 ,LQpredict, use_integral,""," LQ Prediction " +xtag,lumi,1000,WNormalization,filetag);

		fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,500,"MET_pf",        use_integral,"","E_{T}^{miss}(GeV)" +xtag  ,lumi,100,WNormalization,filetag);

		//fillHisto(lq_choice, cut_mc, cut_data, false, 50,0,500,"MET_pf",        use_integral,"","E_{T}^{miss}(GeV)" +xtag  ,lumi,100,WNormalization,filetag+"nosub");

		//fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,500,"MET_pfsig",        use_integral,"","E_{T}^{miss} Significance (GeV)" +xtag  ,lumi,100,WNormalization,filetag);

		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_muon1pfMET", use_integral,"","#Delta #phi (#mu,E_{T}^{miss})" +xtag,lumi,10000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet1pfMET", use_integral,"","#Delta #phi (j_{1},E_{T}^{miss})" +xtag,lumi,10000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet2pfMET", use_integral,"","#Delta #phi (j_{2},E_{T}^{miss})" +xtag,lumi,10000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data ,true,40,.-.5,39.5,"N_GoodVertices", use_integral,"","N_{Vertices}" +xtag,lumi,1000,WNormalization,filetag);

		//fillHisto(lq_choice, cut_mc, cut_data, true, 50,-3.15,3.15,"deltaPhi_pfjet2pfMET", use_integral,"","#Delta #phi (j_{2},E_{T}^{miss})" +xtag,lumi,10000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 50,-3.15,3.15,"deltaPhi_pfjet2pfMET", use_integral,"","#Delta #phi (j_{2},E_{T}^{miss})" +xtag,lumi,10000,WNormalization,filetag);

		//fillHisto(lq_choice, cut_mc, cut_data, true, 50,-.5,49.5,"PFJetNeutralMultiplicity_pfjet1", use_integral,"","Neutral Mult. (Jet 1) " +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,1,"PFJetNeutralHadronEnergyFraction_pfjet1", use_integral,"","Neutral Had Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,1,"PFJetNeutralEmEnergyFraction_pfjet1", use_integral,"","NeutralEM Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 50,-.5,49.5,"PFJetNeutralMultiplicity_pfjet2", use_integral,"","Neutral Mult. (Jet 2) " +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,1,"PFJetNeutralHadronEnergyFraction_pfjet2", use_integral,"","Neutral Had Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,1,"PFJetNeutralEmEnergyFraction_pfjet2", use_integral,"","NeutralEM Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,250,"Pt_pfjet2", use_integral,"","p_{T} (jet_{2}) (GeV)" +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,250,"Pt_pfjet1", use_integral,"","p_{T} (jet_{1}) (GeV)" +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, false, 250,40,1000,"MET_pf",        use_integral,"","E_{T}^{miss}(GeV)" +xtag  ,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, false, 250,0,1000,"Pt_muon1", use_integral,"","p_{T} (#mu) (GeV)" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, false, 250,0,1000,"Pt_pfjet1", use_integral,"","p_{T} (jet_{1}) (GeV)" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, false, 250,0,2000,"M_bestmupfjet_munu", use_integral,"","M_{#mu jet}" +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, false, 40,-3.15,3.15,"deltaPhi_muon1pfMET", use_integral,"","#Delta #phi (#mu,E_{T}^{miss})" +xtag,lumi,100000,WNormalization,filetag);

		//fillHisto(lq_choice, cut_mc, cut_data ,true,40,.-.5,39.5,"N_PileUpInteractions", use_integral,"","N_{PileUpInteractions}" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data ,true,200,0,0.02,"weight_pileup4p7fb", use_integral,"","weight_pileup4p7fb" +xtag,lumi,100,WNormalization,filetag);

		//gROOT->ProcessLine(".q;");
		////fillHisto(lq_choice, cut_mc, cut_data ,true,25,.-.5,24.5,"N_PileUpInteractions", use_integral,"","N_{PileUpInteractions}" +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 100,0,10,"METRatio_pfcalo", use_integral,"","METRatio_pfcalo " +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 100,0,10,"METRatio_lqpf", use_integral,"","METRatio_lqpf " +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 100,0,10,"METRatio_lqcalo", use_integral,"","METRatio_lqcalo " +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 100,0,10,"METRatio_lqpf", use_integral,"","METRatio_lqpf " +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 100,0,10,"METRatio_lqpf", use_integral,"","METRatio_lqpf " +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,500,"RangeTransverseMass_BestLQCombo", use_integral,"","RangeTransverseMass_BestLQCombo " +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,2.5,"RangeCenterTransverseMassRatio_BestLQCombo", use_integral,"","RangeCenterTransverseMassRatio_BestLQCombo " +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 50,-.5,49.5,"PFJetNeutralMultiplicity_pfjet1", use_integral,"","Neutral Mult. (Jet 1) " +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 25,0,1,"PFJetNeutralHadronEnergyFraction_pfjet1", use_integral,"","Neutral Had Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 25,0,1,"PFJetNeutralEmEnergyFraction_pfjet1", use_integral,"","NeutralEM Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 50,-.5,49.5,"PFJetNeutralMultiplicity_pfjet2", use_integral,"","Neutral Mult. (Jet 2) " +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 25,0,1,"PFJetNeutralHadronEnergyFraction_pfjet2", use_integral,"","Neutral Had Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 25,0,1,"PFJetNeutralEmEnergyFraction_pfjet2", use_integral,"","NeutralEM Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 42,-2,40,"FailIDCaloThreshold", use_integral,"","CaloJetID Failure p_{T} (GeV)" +xtag,lumi,10,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 42,-2,40,"FailIDPFThreshold", use_integral,"","PFJetID Failure p_{T} (GeV)" +xtag,lumi,20,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data ,true,50,.-.5,49.5,"N_PileUpInteractions", use_integral,"","N_{PU}" +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data ,true,40,.-.5,39.5,"N_GoodVertices", use_integral,"","N_{Vertices}" +xtag,lumi,1000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data ,true,6,.-.5,5.5,"GlobalMuonCount", use_integral,"","N_{Global #mu}" +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data ,true,6,.-.5,5.5,"TrackerMuonCount", use_integral,"","N_{Tracker #mu}" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data ,true,12,.-.5,11.5,"PFJetCount", use_integral,"","N_{PFJet}" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data ,true,8,.-.5,7.5,"BpfJetCount", use_integral,"","N_{BPFJet}" +xtag,lumi,100,WNormalization,filetag);
		fillHisto(lq_choice, cut_mc, cut_data, true, 80,0,800,"MT_muon1pfMET", use_integral,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, false, 50,0,500,"MT_muon1pfMET", use_integral,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,100,WNormalization,filetag+"nosub");

		//fillHisto(lq_choice, cut_mc, cut_data, true, 80,0,800,"MT_muon1pfMET", true,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,100,WNormalization,filetag);

		////fillHisto(lq_choice, cut_mc, cut_data, true, 25,70,170,"MT_muon1pfMET", use_integral,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,100,WNormalization,filetag+"ZOOMRegion");
		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,400,"Pt_W",        use_integral,"","p_{T}(W)(GeV)" +xtag  ,lumi,5000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_muon1pfMET", use_integral,"","#Delta #phi (#mu,E_{T}^{miss})" +xtag,lumi,10000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet1pfMET", use_integral,"","#Delta #phi (j_{1},E_{T}^{miss})" +xtag,lumi,10000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet2pfMET", use_integral,"","#Delta #phi (j_{2},E_{T}^{miss})" +xtag,lumi,10000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPFJet", use_integral,"","#Delta #phi (E_{T}^{miss},Closest PFJet)" +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPFJet", use_integral,"","#Delta #phi (E_{T}^{miss},Furthest PFJet)" +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestCaloJet", use_integral,"","#Delta #phi (E_{T}^{miss},Closest CaloJet)" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestCaloJet", use_integral,"","#Delta #phi (E_{T}^{miss},Furthest CaloJet)" +xtag,lumi,1000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPT10PFJet", use_integral,"","#Delta #phi (E_{T}^{miss},Closest 10GeV PFJet)" +xtag,lumi,100,WNormalization,filetag);
		//////fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPT10PFJet", use_integral,"","#Delta #phi (E_{T}^{miss},Furthest 10GeV PFJet)" +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METClosestPT10CaloJet", use_integral,"","#Delta #phi (E_{T}^{miss},Closest 10GeV CaloJet)" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,3.15,"deltaPhi_METFurthestPT10CaloJet", use_integral,"","#Delta #phi (E_{T}^{miss},Furthest 10GeV CaloJet)" +xtag,lumi,1000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 60,0,30,"EcalIso_muon1", use_integral,"","ECAL Iso_{#mu} (GeV)" +xtag,lumi,10,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,3,"HcalIso_muon1", use_integral,"","HCAL Iso (#mu)" +xtag,lumi,10,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 35,0,3.5,"TrkIso_muon1", use_integral,"","Track Iso (#mu)" +xtag,lumi,10,WNormalization,filetag);
		fillHisto(lq_choice, cut_mc, cut_data, true, 70,0,700,"Pt_muon1", use_integral,"","p_{T} (#mu) (GeV)" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,50,"PtError_muon1", use_integral,"","#sigma(p_{T}) (#mu) (GeV)" +xtag,lumi,10,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 42,-2.1,2.1,"Eta_muon1", use_integral,"","#eta (#mu)" +xtag,lumi,10000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,.001,"EtaError_muon1", use_integral,"","#sigma(#eta) (#mu)" +xtag,lumi,10000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true,30,-3.141593,3.141593,"Phi_muon1", use_integral,"","#phi (#mu)" +xtag,lumi,2000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 50,0,.0005,"PhiError_muon1", use_integral,"","#sigma(#phi) (#mu)" +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,.0008,"QOverPError_muon1", use_integral,"","#sigma(Q/p)_{#mu}(GeV)" +xtag,lumi,100,WNormalization,filetag);
		fillHisto(lq_choice, cut_mc, cut_data, true, 90,0,900,"Pt_pfjet1", use_integral,"","p_{T} (jet_{1}) (GeV)" +xtag,lumi,100,WNormalization,filetag);
		fillHisto(lq_choice, cut_mc, cut_data, true, 90,0,900,"Pt_pfjet2", use_integral,"","p_{T} (jet_{2}) (GeV)" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3.0,3.0,"Eta_pfjet1", use_integral,"","#eta (jet_{1})" +xtag,lumi,10000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3.0,3.0,"Eta_pfjet2", use_integral,"","#eta (jet_{2})" +xtag,lumi,10000,WNormalization,filetag);

		fillHisto(lq_choice, cut_mc, cut_data, true, 90,200,2000,"ST_pf_munu", use_integral,"","S_{T} (GeV)" +xtag,lumi,500,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, false, 90,200,2000,"ST_pf_munu", use_integral,"","S_{T} (GeV)" +xtag,lumi,500,WNormalization,filetag+"nosub");

		//fillHisto(lq_choice, cut_mc, cut_data, true, 90,200,2000,"ST_pf_munu", true,"","S_{T} (GeV)" +xtag,lumi,500,WNormalization,filetag);

		fillHisto(lq_choice, cut_mc, cut_data, true, 100,0,2000,"M_bestmupfjet_munu", use_integral,"","M_{#mu j} (GeV)" +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 100,0,2000,"M_bestmupfjet_munu", true,"","M_{#mu jet}" +xtag,lumi,1000,WNormalization,filetag);

		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,800,"M_pfjet1pfjet2", use_integral,"","M_{jj}(GeV)" +xtag,lumi,10,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 60,0,600,"MT_pfjet1pfMET", use_integral,"","M_{T}(j_{1},E_{T}^{miss})(GeV)" +xtag,lumi,10,WNormalization,filetag);
		////fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,400,"MT_pfjet2pfMET", use_integral,"","M_{T}(j_{2},E_{T}^{miss})(GeV)" +xtag,lumi,10,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,400,"MT_pfjet1pfjet2", use_integral,"","M^{T}_{jj}(GeV)" +xtag,lumi,10,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,0,8,"deltaR_pfjet1pfjet2", use_integral,"","#Delta R (j_{1}j_{2})(GeV)" +xtag,lumi,10000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, true, 40,-3.15,3.15,"deltaPhi_pfjet1pfjet2", use_integral,"","#Delta#phi (j_{1}j_{2})(GeV)" +xtag,lumi,1000,WNormalization,filetag);

	}

	////// -------------    Full Selection      -------------- //

	if (true)
	{

		// LQ 450
		filetag = "2011Data_FullSelection_lqmunu450";
		xtag = " [Full Selection]";
		lq_choice = "lqmunu450";

		TString cut_full_data = cut_data +"*(ST_pf_munu > 700)*(MET_pf  > 140)*(M_bestmupfjet_munu > 360)*(MT_muon1pfMET>120.0)";
		TString cut_full_mc = cut_mc +"*(ST_pf_munu > 700)*(MET_pf  > 140)*(M_bestmupfjet_munu > 360)*(MT_muon1pfMET>120.0)";

		fillHisto(lq_choice, cut_full_mc, cut_full_data, false, 25,0.0,2500.0,"M_bestmupfjet_munu", use_integral,"","M_{#mu j} (GeV)" +xtag,lumi,40,WNormalization,filetag);
		fillHisto(lq_choice,  cut_full_mc, cut_full_data, use_integral, 25,250,2750,"ST_pf_munu", use_integral,"","S_{T} (GeV)" +xtag,lumi,50,WNormalization,filetag);

		////fillHisto(lq_choice, cut_full_mc, cut_full_data, false, 25,0.0,2500.0,"M_bestmupfjet_munu", true,"","M_{#mu j}" +xtag,lumi,40,WNormalization,filetag);
		////fillHisto(lq_choice,  cut_full_mc, cut_full_data, use_integral, 25,250,2250,"ST_pf_munu",true,"","S_{T} (GeV)" +xtag,lumi,50,WNormalization,filetag);

		//////fillHisto(lq_choice,  cut_full_mc, cut_full_data, use_integral, 25,-3.141593,3.141593,"deltaPhi_pfjet1pfMET", use_integral,""," #Delta#phi (j_{1},MET)" +xtag,lumi,50,WNormalization,filetag);
		//////fillHisto(lq_choice,  cut_full_mc, cut_full_data, use_integral, 25,-3.141593,3.141593,"deltaPhi_pfjet2pfMET", use_integral,""," #Delta#phi (j_{2},MET)" +xtag,lumi,50,WNormalization,filetag);
		fillHisto(lq_choice,  cut_full_mc, cut_full_data, use_integral, 50,0,1000,"MT_muon1pfMET", use_integral,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,100,WNormalization,filetag);
		//////fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 60,0,900,"Pt_pfjet1", use_integral,"","p_{T} (jet_{1}) (GeV)" +xtag,lumi,100,WNormalization,filetag);
		//////fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 60,0,900,"Pt_pfjet2", use_integral,"","p_{T} (jet_{2}) (GeV)" +xtag,lumi,100,WNormalization,filetag);
		fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 40,80,880,"MET_pf",        use_integral,"","E_{T}^{miss}(GeV)" +xtag  ,lumi,100,WNormalization,filetag);
		fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 35,0,700,"Pt_muon1", use_integral,"","p_{T} (#mu) (GeV)" +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data ,use_integral,12,.-.5,11.5,"PFJetCount", use_integral,"","N_{PFJet}" +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data ,use_integral,50,.-.5,49.5,"N_Vertices", use_integral,"","N_{Vertices}" +xtag,lumi,1000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data ,use_integral,50,.-.5,49.5,"N_PileUpInteractions", use_integral,"","N_{PU}" +xtag,lumi,1000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 40,-3.0,3.0,"Eta_pfjet1", use_integral,"","#eta (jet_{1})" +xtag,lumi,10000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 40,-3.0,3.0,"Eta_pfjet2", use_integral,"","#eta (jet_{2})" +xtag,lumi,10000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 12,.-.5,11.5,"PFJetCount", use_integral,"","N_{PFJet}" +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 8,.-.5,7.5,"BpfJetCount", use_integral,"","N_{BPFJet}" +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral,  50,0,1,"PFJetNeutralHadronEnergyFraction_pfjet1", use_integral,"","Neutral Had Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral,  50,0,1,"PFJetNeutralEmEnergyFraction_pfjet1", use_integral,"","NeutralEM Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral,  50,0,1,"PFJetNeutralHadronEnergyFraction_pfjet2", use_integral,"","Neutral Had Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral,  50,0,1,"PFJetNeutralEmEnergyFraction_pfjet2", use_integral,"","NeutralEM Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data, false, 55,0.0,1.0,"DeltaPtOverPt_muon1", use_integral,"","#Delta(p_{T})/p_{T}" +xtag,lumi,40,WNormalization,filetag);
		fillHisto(lq_choice, cut_full_mc, cut_full_data, false, 25,0.0,2000.0,"MT_bestMETpfjet_munu", use_integral,"","M^{T}_{#nu j} (GeV)" +xtag,lumi,40,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data, false, 25,0.0,2000.0,"MT_bestMETpfjet_munu", true,"","M^{T}_{#nu j}" +xtag,lumi,40,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data, false, 40,-3.15,3.15,"deltaPhi_muon1pfMET", use_integral,"","#Delta #phi (#mu,E_{T}^{miss})" +xtag,lumi,10000,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 30,0,600,"MET_pfsig",        use_integral,"","E_{T}^{miss} [Sig] (GeV)" +xtag  ,lumi,100,WNormalization,filetag);

		// LQ 600
		filetag = "2011Data_FullSelection_lqmunu600";
		xtag = " [Full Selection]";
		lq_choice = "lqmunu600";

		//TString cut_full_data = cut_data +"";
		//TString cut_full_mc = cut_mc+"";
		TString cut_full_data = cut_data +"*(ST_pf_munu > 890)*(MET_pf  > 180)*(M_bestmupfjet_munu > 480)*(MT_muon1pfMET>120.0)";
		TString cut_full_mc = cut_mc+"*(ST_pf_munu > 890)*(MET_pf  > 180)*(M_bestmupfjet_munu > 480)*(MT_muon1pfMET>120.0)";

		fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 25,0.0,2500.0,"M_bestmupfjet_munu", use_integral,"","M_{#mu j} (GeV)" +xtag,lumi,40,WNormalization,filetag);
		fillHisto(lq_choice,  cut_full_mc, cut_full_data, false , 25,250,2750,"ST_pf_munu", use_integral,"","S_{T} (GeV)" +xtag,lumi,50,WNormalization,filetag);

		//fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 25,0.0,2500.0,"M_bestmupfjet_munu", true,"","M_{#mu j}" +xtag,lumi,40,WNormalization,filetag);
		//fillHisto(lq_choice,  cut_full_mc, cut_full_data, false , 25,250,2250,"ST_pf_munu", true,"","S_{T} (GeV)" +xtag,lumi,50,WNormalization,filetag);

		////fillHisto(lq_choice,  cut_full_mc, cut_full_data, false , 25,-3.141593,3.141593,"deltaPhi_pfjet1pfMET", use_integral,""," #Delta#phi (j_{1},MET)" +xtag,lumi,50,WNormalization,filetag);
		////fillHisto(lq_choice,  cut_full_mc, cut_full_data, false , 25,-3.141593,3.141593,"deltaPhi_pfjet2pfMET", use_integral,""," #Delta#phi (j_{2},MET)" +xtag,lumi,50,WNormalization,filetag);
		fillHisto(lq_choice,  cut_full_mc, cut_full_data, false , 40,0,2200,"MT_muon1pfMET", use_integral,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,10,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 30,0,900,"Pt_pfjet1", use_integral,"","p_{T} (jet_{1}) (GeV)" +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 30,0,900,"Pt_pfjet2", use_integral,"","p_{T} (jet_{2}) (GeV)" +xtag,lumi,100,WNormalization,filetag);
		fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 40,80,880,"MET_pf",        use_integral,"","E_{T}^{miss}(GeV)" +xtag  ,lumi,100,WNormalization,filetag);
		fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 35,0,700,"Pt_muon1", use_integral,"","p_{T} (#mu) (GeV)" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data ,false ,12,.-.5,11.5,"PFJetCount", use_integral,"","N_{PFJet}" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data ,false ,50,.-.5,49.5,"N_Vertices", use_integral,"","N_{Vertices}" +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data ,false ,50,.-.5,49.5,"N_PileUpInteractions", use_integral,"","N_{PU}" +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 40,-3.0,3.0,"Eta_pfjet1", use_integral,"","#eta (jet_{1})" +xtag,lumi,10000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 40,-3.0,3.0,"Eta_pfjet2", use_integral,"","#eta (jet_{2})" +xtag,lumi,10000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 12,.-.5,11.5,"PFJetCount", use_integral,"","N_{PFJet}" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 8,.-.5,7.5,"BpfJetCount", use_integral,"","N_{BPFJet}" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral,  50,0,1,"PFJetNeutralHadronEnergyFraction_pfjet1", use_integral,"","Neutral Had Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral,  50,0,1,"PFJetNeutralEmEnergyFraction_pfjet1", use_integral,"","NeutralEM Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral,  50,0,1,"PFJetNeutralHadronEnergyFraction_pfjet2", use_integral,"","Neutral Had Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral,  50,0,1,"PFJetNeutralEmEnergyFraction_pfjet2", use_integral,"","NeutralEM Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, false, 55,0.0,1.0,"DeltaPtOverPt_muon1", use_integral,"","#Delta(p_{T})/p_{T}" +xtag,lumi,40,WNormalization,filetag);

		fillHisto(lq_choice, cut_full_mc, cut_full_data, false, 25,0.0,2000.0,"MT_bestMETpfjet_munu", use_integral,"","M^{T}_{#nu j} (GeV)" +xtag,lumi,40,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, false, 25,0.0,2000.0,"MT_bestMETpfjet_munu", true,"","M^{T}_{#nu j}" +xtag,lumi,40,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, false, 40,-3.15,3.15,"deltaPhi_muon1pfMET", use_integral,"","#Delta #phi (#mu,E_{T}^{miss})" +xtag,lumi,10000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 30,0,600,"MET_pfsig",        use_integral,"","E_{T}^{miss} [Sig] (GeV)" +xtag  ,lumi,100,WNormalization,filetag);

		// LQ 750
		filetag = "2011Data_FullSelection_lqmunu750";
		xtag = " [Full Selection]";
		lq_choice = "lqmunu750";

		TString cut_full_data = cut_data +"*(ST_pf_munu > 1000)*(MET_pf  > 220)*(M_bestmupfjet_munu > 540)*(MT_muon1pfMET>120.0)";
		TString cut_full_mc = cut_mc+"*(ST_pf_munu > 1000)*(MET_pf  > 220)*(M_bestmupfjet_munu > 540)*(MT_muon1pfMET>120.0)";

		fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 25,0.0,2500.0,"M_bestmupfjet_munu", use_integral,"","M_{#mu j} (GeV)" +xtag,lumi,40,WNormalization,filetag);
		fillHisto(lq_choice,  cut_full_mc, cut_full_data, false , 25,250,2750,"ST_pf_munu", use_integral,"","S_{T} (GeV)" +xtag,lumi,50,WNormalization,filetag);

		//fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 25,0.0,2500.0,"M_bestmupfjet_munu", true,"","M_{#mu j}" +xtag,lumi,40,WNormalization,filetag);
		//fillHisto(lq_choice,  cut_full_mc, cut_full_data, false , 25,250,2250,"ST_pf_munu", true,"","S_{T} (GeV)" +xtag,lumi,50,WNormalization,filetag);

		////fillHisto(lq_choice,  cut_full_mc, cut_full_data, false , 25,-3.141593,3.141593,"deltaPhi_pfjet1pfMET", use_integral,""," #Delta#phi (j_{1},MET)" +xtag,lumi,50,WNormalization,filetag);
		////fillHisto(lq_choice,  cut_full_mc, cut_full_data, false , 25,-3.141593,3.141593,"deltaPhi_pfjet2pfMET", use_integral,""," #Delta#phi (j_{2},MET)" +xtag,lumi,50,WNormalization,filetag);
		fillHisto(lq_choice,  cut_full_mc, cut_full_data, false , 40,0,2200,"MT_muon1pfMET", use_integral,"","M^{T}_{#mu#nu}(GeV)" +xtag,lumi,10,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 30,0,900,"Pt_pfjet1", use_integral,"","p_{T} (jet_{1}) (GeV)" +xtag,lumi,100,WNormalization,filetag);
		////fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 30,0,900,"Pt_pfjet2", use_integral,"","p_{T} (jet_{2}) (GeV)" +xtag,lumi,100,WNormalization,filetag);
		fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 40,80,880,"MET_pf",        use_integral,"","E_{T}^{miss}(GeV)" +xtag  ,lumi,100,WNormalization,filetag);
		fillHisto(lq_choice, cut_full_mc, cut_full_data, false , 35,0,700,"Pt_muon1", use_integral,"","p_{T} (#mu) (GeV)" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data ,false ,12,.-.5,11.5,"PFJetCount", use_integral,"","N_{PFJet}" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data ,false ,50,.-.5,49.5,"N_Vertices", use_integral,"","N_{Vertices}" +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data ,false ,50,.-.5,49.5,"N_PileUpInteractions", use_integral,"","N_{PU}" +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 40,-3.0,3.0,"Eta_pfjet1", use_integral,"","#eta (jet_{1})" +xtag,lumi,10000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 40,-3.0,3.0,"Eta_pfjet2", use_integral,"","#eta (jet_{2})" +xtag,lumi,10000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 12,.-.5,11.5,"PFJetCount", use_integral,"","N_{PFJet}" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 8,.-.5,7.5,"BpfJetCount", use_integral,"","N_{BPFJet}" +xtag,lumi,100,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral,  50,0,1,"PFJetNeutralHadronEnergyFraction_pfjet1", use_integral,"","Neutral Had Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral,  50,0,1,"PFJetNeutralEmEnergyFraction_pfjet1", use_integral,"","NeutralEM Fraction (Jet 1) " +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral,  50,0,1,"PFJetNeutralHadronEnergyFraction_pfjet2", use_integral,"","Neutral Had Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral,  50,0,1,"PFJetNeutralEmEnergyFraction_pfjet2", use_integral,"","NeutralEM Fraction (Jet 2) " +xtag,lumi,1000,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, false, 55,0.0,1.0,"DeltaPtOverPt_muon1", use_integral,"","#Delta(p_{T})/p_{T}" +xtag,lumi,40,WNormalization,filetag);

		//fillHisto(lq_choice, cut_full_mc, cut_full_data, use_integral, 30,0,600,"MET_pfsig",        use_integral,"","E_{T}^{miss} [Sig] (GeV)" +xtag  ,lumi,100,WNormalization,filetag);

		fillHisto(lq_choice, cut_full_mc, cut_full_data, false, 25,0.0,2000.0,"MT_bestMETpfjet_munu", use_integral,"","M^{T}_{#nu j} (GeV)" +xtag,lumi,40,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, false, 25,0.0,2000.0,"MT_bestMETpfjet_munu", true,"","M^{T}_{#nu j}" +xtag,lumi,40,WNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data, false, 40,-3.15,3.15,"deltaPhi_muon1pfMET", use_integral,"","#Delta #phi (#mu,E_{T}^{miss})" +xtag,lumi,10000,WNormalization,filetag);

	}
	gROOT->Reset(); gROOT->ProcessLine(".q;");

}
