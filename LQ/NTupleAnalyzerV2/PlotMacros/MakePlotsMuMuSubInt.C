
#include "TLorentzVector.h"
#include "TH1.h"
#include <iostream>
#include <fstream>
#include <iomanip>
#include "CMSStyle.C"

void fillHisto(TString lq_choice, TString cut_mc, TString cut_data,  TString cut_data_emu,  bool Use_emu, bool drawSub,
int nBins, float xLow, float xMax, TString var, TString var_emu, bool Use_integral, TString fileName,TString title, TString Luminosity,Double_t extrascalefactor,Double_t znorm,TString tag)
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

	if (!usevar)
	{
		std::cout<<"\nWARNING: Branch for variable "<<var<<"  not found. Skipping plot for this variable. \n"<<std::endl;
		//return;
	}

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
	if (!Use_emu) {ttbar->Draw(var+">>H_ttbar",cut_mc);}
	else if (Use_emu) {data->Draw(var_emu+">>H_ttbar",cut_data_emu);}
	vvjets->Draw(var+">>H_vvjets",cut_mc);
	singtop->Draw(var+">>H_singtop",cut_mc);
	qcd->Draw(var+">>H_qcd",cut_mc);
	if (lq_choice == "lqmumu250")  lqmumu250->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmumu350")  lqmumu350->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmumu400")  lqmumu400->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmumu450")  lqmumu450->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmumu500")  lqmumu500->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmumu550")  lqmumu550->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmumu600")  lqmumu600->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmumu650")  lqmumu650->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmumu750")  lqmumu750->Draw(var+">>H_lq",cut_mc);
	if (lq_choice == "lqmumu850")  lqmumu850->Draw(var+">>H_lq",cut_mc);

	data->Draw(var+">>H_data",cut_data);

	if (var == "M_bestmupfjet1_mumu")
	{
		// Make histograms for second LQ mass in event and add to first
		TString var2 = "M_bestmupfjet2_mumu";
		TString var2_emu = "M_bestmuORelepfjet2_mumu_emuselection";
		TH1F* H2_zjets = new TH1F("H2_zjets","",nBins,xLow,xMax);
		TH1F* H2_wjets = new TH1F("H2_wjets","",nBins,xLow,xMax);
		TH1F* H2_vvjets = new TH1F("H2_vvjets","",nBins,xLow,xMax);
		TH1F* H2_singtop = new TH1F("H2_singtop","",nBins,xLow,xMax);
		TH1F* H2_qcd = new TH1F("H2_qcd","",nBins,xLow,xMax);
		TH1F* H2_ttbar = new TH1F("H2_ttbar","",nBins,xLow,xMax);
		TH1F* H2_data = new TH1F("H2_data","",nBins,xLow,xMax);
		TH1F* H2_lqmumu = new TH1F("H2_lqmumu","",nBins,xLow,xMax);

		zjets->Draw(var2+">>H2_zjets",cut_mc);
		wjets->Draw(var2+">>H2_wjets",cut_mc);
		if (!Use_emu) {ttbar->Draw(var2+">>H2_ttbar",cut_mc);}
		else if (Use_emu) {data->Draw(var2_emu+">>H2_ttbar",cut_data_emu);}
		//ttbar->Draw(var2+">>H2_ttbar",cut_mc);
		vvjets->Draw(var2+">>H2_vvjets",cut_mc);
		singtop->Draw(var2+">>H2_singtop",cut_mc);
		qcd->Draw(var2+">>H2_qcd",cut_mc);
		data->Draw(+var2+">>H2_data",cut_data);

		if (lq_choice == "lqmumu250")  lqmumu250->Draw(var+">>H2_lqmumu",cut_mc);
		if (lq_choice == "lqmumu350")  lqmumu350->Draw(var+">>H2_lqmumu",cut_mc);
		if (lq_choice == "lqmumu400")  lqmumu400->Draw(var+">>H2_lqmumu",cut_mc);
		if (lq_choice == "lqmumu450")  lqmumu450->Draw(var+">>H2_lqmumu",cut_mc);
		if (lq_choice == "lqmumu500")  lqmumu500->Draw(var+">>H2_lqmumu",cut_mc);
		if (lq_choice == "lqmumu550")  lqmumu550->Draw(var+">>H2_lqmumu",cut_mc);
		if (lq_choice == "lqmumu600")  lqmumu600->Draw(var+">>H2_lqmumu",cut_mc);
		if (lq_choice == "lqmumu650")  lqmumu650->Draw(var+">>H2_lqmumu",cut_mc);
		if (lq_choice == "lqmumu750")  lqmumu750->Draw(var+">>H2_lqmumu",cut_mc);
		if (lq_choice == "lqmumu850")  lqmumu850->Draw(var+">>H2_lqmumu",cut_mc);

		H_zjets->Add(H2_zjets);
		H_wjets->Add(H2_wjets);
		H_ttbar->Add(H2_ttbar);
		H_vvjets->Add(H2_vvjets);
		H_singtop->Add(H2_singtop);
		H_qcd->Add(H2_qcd);
		H_data->Add(H2_data);
		H_lq->Add(H2_lqmumu);

		// Rename variable
		var = "M_bestmupfjetcombo_mumu";
	}

	// Rescaling Routine
	H_zjets->Scale(znorm);
	H_wjets->Scale(1.21);
	//H_vvjets->Scale(0.9);
	//H_singtop->Scale(0.9);
	if (Use_emu) {H_ttbar->Scale(0.695);}
	if (!Use_emu) {H_ttbar->Scale(1.00);}


	// ***************************************         SCREEN READOUT       *************************************************** //

	Double_t Nd = H_data->Integral();
	Double_t Nmc = H_zjets->Integral()+H_ttbar->Integral()+H_vvjets->Integral()+H_wjets->Integral()+H_singtop->Integral()+H_qcd->GetEntries();
	Double_t Nw = H_wjets->Integral();
	Double_t Nt = H_ttbar->Integral();
	Double_t Nz = H_zjets->Integral();
	Double_t N_other = Nmc - Nz;

	//Double_t sigma_Nz = Nz*pow(1.0*(H_zjets->GetEntries()),-0.5);

	//Double_t sigma_N_other = 0.0;
	//if (H_ttbar->GetEntries()>0) sigma_N_other += H_ttbar->Integral()*pow((1.0*H_ttbar->GetEntries()),-0.5);
	//if (H_wjets->GetEntries()>0) sigma_N_other += H_wjets->Integral()*pow((1.0*H_wjets->GetEntries() ),-0.5);
	//if (H_vvjets->GetEntries()>0) sigma_N_other += H_vvjets->Integral()*pow((1.0*H_vvjets->GetEntries() ),-0.5);
	//if (H_singtop->GetEntries()>0) sigma_N_other += H_singtop->Integral()*pow((1.0*singtop->GetEntries()),-0.5);
	//if (H_qcd->GetEntries()>0) sigma_N_other += H_qcd->Integral()*pow((1.0*H_qcd->GetEntries()),-0.5);

	//Double_t sigam_Nd = sqrt(Nd);

	std::cout<<"Data   : "<<Nd<<std::endl;
	std::cout<<"All MC : "<<Nmc<<std::endl;
	if (H_ttbar->GetEntries()>0) std::cout<<"tt   : "<<H_ttbar->Integral()<<"  +- "<<H_ttbar->Integral()*pow(1.0*(H_ttbar->GetEntries()),-0.5)<<"   --- Entries:  "<<H_ttbar->GetEntries()<<std::endl;
	if (H_vvjets->GetEntries()>0) std::cout<<"VV   : "<<H_vvjets->Integral()<<"  +- "<<H_vvjets->Integral()*pow(1.0*(H_vvjets->GetEntries()),-0.5)<<"   --- Entries:  "<<H_vvjets->GetEntries()<<std::endl;
	if (H_singtop->GetEntries()>0) std::cout<<"singtop   : "<<H_singtop->Integral()<<"  +- "<<H_singtop->Integral()*pow(1.0*(H_singtop->GetEntries()),-0.5)<<"   --- Entries:  "<<H_singtop->GetEntries()<<std::endl;
	if (H_qcd->GetEntries()>0) std::cout<<"qcd   : "<<H_qcd->Integral()<<"  +- "<<H_qcd->Integral()*pow(1.0*(H_qcd->GetEntries()),-0.5)<<"   --- Entries:  "<<H_qcd->GetEntries()<<std::endl;
	if (H_wjets->GetEntries()>0)std::cout<<"w   : "<<H_wjets->Integral()<<"  +- "<<H_wjets->Integral()*pow(1.0*(H_wjets->GetEntries()),-0.5)<<"   --- Entries:  "<<H_wjets->GetEntries()<<std::endl;

	if (H_zjets->GetEntries()>0)std::cout<<"z   : "<<H_zjets->Integral()<<"  +- "<<H_zjets->Integral()*pow(1.0*(H_zjets->GetEntries()),-0.5)<<"   --- Entries:  "<<H_zjets->GetEntries()<<std::endl;

	Double_t fac_z = (Nd-N_other)/Nz;

	Double_t fac_zerr = Nd ;
	fac_zerr +=  (H_ttbar->Integral())*(H_ttbar->Integral())/(1.0*H_ttbar->GetEntries());
	fac_zerr +=  (H_wjets->Integral())*(H_wjets->Integral())/(1.0*H_wjets->GetEntries());
	fac_zerr +=  (H_vvjets->Integral())*(H_vvjets->Integral())/(1.0*H_vvjets->GetEntries());
	fac_zerr +=  (H_singtop->Integral())*(H_singtop->Integral())/(1.0*H_singtop->GetEntries());
	fac_zerr = fac_zerr/((Nd-N_other)*(Nd-N_other));
	fac_zerr += 1.0/(1.0*(H_zjets->GetEntries()));
	fac_zerr = pow(fac_zerr,0.5);
	fac_zerr *= fac_z;
	std::cout<<"Z Scale factor: "<<fac_z<<"  +-  "<<fac_zerr<<std::endl;

	//Double_t fac_Numerator = Nd - N_other;
	//Double_t fac_Denominator = Nz;
	//Double_t fac = fac_Numerator/fac_Denominator;

	//Double_t sigma_fac_Numerator = sqrt( pow( sigam_Nd ,2.0) + pow( sigma_N_other ,2.0) ) ;
	//Double_t sigma_fac_Denominator = sigma_Nz;
	//Double_t sigma_fac_over_fac = pow( pow((sigma_fac_Numerator/fac_Numerator),2.0)    +  pow((sigma_fac_Denominator/fac_Denominator),2.0)    ,0.5);
	//Double_t sigma_fac = sigma_fac_over_fac*fac;

	//std::cout<<"Z Scale Factor:  "<<fac<<"  +-  "<<sigma_fac<<std::endl;

	// ******************************************************************************************************************************* //

	TH1F* H_bkg = new TH1F("H_bkg","",nBins,xLow,xMax);

	H_bkg->Add(H_vvjets);
	H_bkg->Add(H_wjets);
	H_bkg->Add(H_singtop);
	//H_bkg->Add(H_qcd);

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
	H_singtop->SetFillStyle(3006);
	H_qcd->SetFillStyle(3006 );
	H_lq->SetFillStyle(0);

	H_zjets->SetFillColor(2);
	H_ttbar->SetFillColor(4);
	H_wjets->SetFillColor(6);
	H_singtop->SetFillColor(3);
	H_qcd->SetFillColor(3);
	H_bkg->SetFillColor(9);
	//H_lq->SetLineStyle(3);

	H_lq->SetLineColor(8);
	H_zjets->SetLineColor(2);
	H_ttbar->SetLineColor(4);
	H_wjets->SetLineColor(6);
	H_singtop->SetLineColor(3);
	H_qcd->SetLineColor(3);
	H_bkg->SetLineColor(9);

	H_lq->SetMarkerColor(8);
	H_zjets->SetMarkerColor(2);
	H_wjets->SetMarkerColor(6);
	H_singtop->SetMarkerColor(3);
	H_qcd->SetMarkerColor(3);
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
	//  H_stack->Add(H_singtop);
	//  H_stack->Add(H_qcd);

	H_stack->Add(H_ttbar);
	H_stack->Add(H_zjets);

	//  H_stack->Add(H_wjets);
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
	gStyle->SetOptStat(0H);
	H_data->Draw("E");

	H_stack->Draw("SAME");
	H_lq->Draw("SAME");
	H_data->Draw("SAMEE");
	TLegend* leg = new TLegend(0.6,0.63,0.91,0.91,"","brNDC");
	leg->SetTextFont(132);
	leg->SetFillColor(0);
	leg->SetBorderSize(0);
	leg->AddEntry(H_data,"Data 2011, 4.98 fb^{-1}");
	leg->AddEntry(H_zjets,"Z/#gamma* + jets");
	if (!Use_emu) leg->AddEntry(H_ttbar,"t#bar{t}");
	if (Use_emu) leg->AddEntry(H_ttbar,"t#bar{t} [Data Driven e-#mu]");

	leg->AddEntry(H_bkg,"Other backgrounds");

	if (lq_choice == "lqmumu250")  leg->AddEntry(H_lq,"LQ M = 250");
	if (lq_choice == "lqmumu350")  leg->AddEntry(H_lq,"LQ M = 350");
	if (lq_choice == "lqmumu400")  leg->AddEntry(H_lq,"LQ M = 400");
	if (lq_choice == "lqmumu450")  leg->AddEntry(H_lq,"LQ M = 450");
	if (lq_choice == "lqmumu500")  leg->AddEntry(H_lq,"LQ M = 500");
	if (lq_choice == "lqmumu550")  leg->AddEntry(H_lq,"LQ M = 550");
	if (lq_choice == "lqmumu600")  leg->AddEntry(H_lq,"LQ M = 600");
	if (lq_choice == "lqmumu650")  leg->AddEntry(H_lq,"LQ M = 650");
	if (lq_choice == "lqmumu750")  leg->AddEntry(H_lq,"LQ M = 750");
	if (lq_choice == "lqmumu850")  leg->AddEntry(H_lq,"LQ M = 850");

	leg->Draw("SAME");
	c1->SetLogy();

	H_data->SetMinimum(.01);
	H_data->SetMaximum(1.2*extrascalefactor*(H_data->GetMaximum()));

	TLatex* txt =new TLatex((xMax-xLow)*.05+xLow,.1*H_data->GetMaximum(), "CMS 2011");
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

		//H_comp->Draw("p");
		//line0->Draw("SAME");
		//line2u->Draw("SAME");
		//line2d->Draw("SAME");

		pad2r->cd();

		H_compr->GetYaxis()->SetTitle("Frac. Diff.");
		H_compr->GetYaxis()->SetTitleFont(132);
		H_compr->GetYaxis()->SetTitleSize(.15);
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

	TString addon = "";
	if (Use_integral) addon = "_integral";

	c1->Print("PlotsMuMuSubInt/"+varname+"_"+tag+addon+".png");
	c1->Print("PlotsMuMuSubInt/"+varname+"_"+tag+addon+".pdf");

	//c1->Print("PlotsMuMuSubInt/test.pdf");
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


void MakePlotsMuMuSubInt()
{

	// Load files and trees:
	gROOT->ProcessLine(".x LoadCastorFiles.C");

	// -------- PF ---------

	TString lumi = "4980"  ;
	TString cut_data = "(Pt_muon1>40)*(Pt_muon2>40)";
	cut_data += "*(Pt_pfjet1>30)*(Pt_pfjet2>30)";
	cut_data += "*(M_muon1muon2>50)*(ST_pf_mumu>250.0)";
	cut_data += "*(deltaR_muon1muon2>0.5)*(pass_HBHENoiseFilter>0.5)*(pass_passBeamHaloFilterTight>0.5)*(pass_isTrackingFailure>0.5)";
	cut_data += "*((abs(Eta_muon1)<2.1)&&(abs(Eta_muon2)<2.1))";
	//cut_data += "*(pass_HBHENoiseFilter>0.5)*(pass_passBeamHaloFilterTight>0.5)*(pass_EcalMaskedCellDRFilter> 0.5)";
	//cut_data += "*(PFJetCount>2.5)*(BpfJetCount>1.5)*(M_muon1muon2>120)";
	//cut_data += "*(M_muon1muon2>100)*(M_muon1muon2<120.0)";


	//----------Declare what lqmumu variable you'd like to display----
	TString lq_choice = "lqmumu400";

	//---------emu stuff--------
	bool Use_emu = false;
	bool use_integral = false;

	TString cut_data_emu = "(Pt_muon1>40)*(Pt_HEEPele1>40)";
	cut_data_emu += "*(Pt_pfjet1>30)*(Pt_pfjet2>30)";
	cut_data_emu += "*(M_muon1HEEPele1>50)*(ST_pf_emu>250.0)";
	cut_data_emu += "*(deltaR_muon1HEEPele1>0.5)*(pass_HBHENoiseFilter>0.5)*(pass_passBeamHaloFilterTight>0.5)*(pass_isTrackingFailure>0.5)";
	cut_data_emu += "*((abs(Eta_muon1)<2.1)&&(abs(Eta_HEEPele1)<2.1))";
	//cut_data_emu +=  "*(pass_HBHENoiseFilter>0.5)*(pass_passBeamHaloFilterTight>0.5)*(pass_EcalMaskedCellDRFilter> 0.5)";
	//cut_data_emu += "*(PFJetCount>2.5)*(BpfJetCount>1.5)*(M_muon1HEEPele1>120)";
	//cut_data_emu += "*(M_muon1HEEPele1>100)*(M_muon1HEEPele1<120)";

	TString cut_mc = lumi+ "*weight_pileup4p7fb_higgs*("+cut_data+")";
	TString cut_mc_emu = lumi+ "*weight_pileup4p7fb_higgs*("+cut_data_emu+")";

	cut_data += "*(LowestUnprescaledTriggerPass>0.5)*(pass_isBPTX0>0.5)";
	cut_data_emu += "*(LowestUnprescaledTriggerPass>0.5)*(pass_isBPTX0>0.5)";

	float ZNormalization = 1.27;
	TString filetag = " ";
	TString xtag = " ";

	// ------------- Normalization Calculation                         -------------- //

	if (ZNormalization == 1.00)
	{
		std::cout<<"\n\n Z Normalization is unity. Program will calculate Z rescaling factor and exit.\n\n"<<std::endl;
		filetag = "2011Data_NormalizationSelection";
		xtag = " [Z Normalization Condition]";
		TString NormCondition = "*(ST_pf_mumu>250)*(M_muon1muon2>80)*(M_muon1muon2<100)";

		Use_emu = false;
		fillHisto(lq_choice, cut_mc + NormCondition, cut_data+NormCondition, cut_data_emu, Use_emu , true, 20,80,100, "M_muon1muon2", "M_muon1muon2", false, "","M_{#mu#mu}(GeV) " +xtag,lumi,10000,ZNormalization,filetag);
		gROOT->Reset(); gROOT->ProcessLine(".q;");
	}

	// ------------- Minimal Selection - Preselection Without ST Cut.  -------------- //
	filetag = "2011Data_MinimalSelection";
	xtag = " [Presel sans ST cut]";

	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 40,0,800, "M_pfjet1pfjet2", false, "","M_{jj}(GeV)" +xtag,lumi,10,ZNormalization,filetag);
	////fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 40,0,400, "MT_pfjet1pfjet2", false, "","M^{T}_{jj}(GeV)" +xtag,lumi,10,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 40,0,8, "deltaR_pfjet1pfjet2", false, "","#Delta R (j_{1}j_{2})(GeV)" +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 40,-3.15,3.15, "deltaPhi_pfjet1pfjet2", false, "","#Delta#phi (j_{1}j_{2})(GeV)" +xtag,lumi,1000,ZNormalization,filetag);

	// ------------- Pre Selection - Preselection With ST>250 Cut    -------------- //

	//cut_data += "*(ST_pf_mumu>250.0)";
	//cut_mc += "*(ST_pf_mumu>250.0)";
	//cut_data_emu += "*(ST_pf_emu>250.0)";
	TString filetag = "2011Data_PreSelection";
	TString xtag = " [Preselection]";

	if (true)
	{

		//gROOT->Reset();	gROOT->ProcessLine(".q;");
		Use_emu = true;

		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 30,60,360, "MET_pf", "MET_pf",        use_integral, "","E_{T}^{miss}(GeV)" +xtag  ,lumi,50,ZNormalization,filetag+"emu");
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 25,250,10250, "ST_pf_mumu", "ST_pf_emu", use_integral, "","S_{T} (GeV)" +xtag,lumi,250,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 25,50,350, "M_muon1muon2", "M_muon1HEEPele1", use_integral, "","M_{#mu#mu}(GeV) " +xtag,lumi,50,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc_emu, cut_data_emu, cut_data_emu, false, true, 25,250,10250, "ST_pf_emu", "ST_pf_emu", use_integral, "","S_{T} (GeV)" +xtag,lumi,250,ZNormalization,filetag);

		
		//gROOT->ProcessLine(".q;");

		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,4000, "MET_pf", "MET_pf",        use_integral, "","E_{T}^{miss}(GeV) uu" +xtag  ,lumi,50,ZNormalization,filetag+"uu");


		//fillHisto(lq_choice, cut_mc_emu, cut_data_emu, cut_data_emu, false, true, 40,0,1000, "ST_pf_emu", "ST_pf_emu",        use_integral, "","ST eu" +xtag  ,lumi,50,ZNormalization,filetag+"eu");
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,1000, "ST_pf_mumu", "ST_pf_mumu",        use_integral, "","ST uu" +xtag  ,lumi,50,ZNormalization,filetag+"uu");

		//fillHisto(lq_choice, cut_mc_emu, cut_data_emu, cut_data_emu, false, true, 40,-3,3, "Eta_HEEPele1", "Eta_HEEPele1",        use_integral, "","ETA e eu" +xtag  ,lumi,5000,ZNormalization,filetag+"eu");
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,-3,3, "Eta_muon1", "Eta_muon1",        use_integral, "","ETA u uu" +xtag  ,lumi,5000,ZNormalization,filetag+"uu");

		//fillHisto(lq_choice, cut_mc_emu, cut_data_emu, cut_data_emu, false, true, 6,-.5,5.5, "MuonCount", "MuonCount",        use_integral, "","muon count eu" +xtag  ,lumi,5000,ZNormalization,filetag+"eu");
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 6,-0.5,5.5, "MuonCount", "MuonCount",        use_integral, "","muon count uu" +xtag  ,lumi,5000,ZNormalization,filetag+"uu");


		//fillHisto(lq_choice, cut_mc_emu, cut_data_emu, cut_data_emu, false, true, 6,-.5,5.5, "HEEPEleCount", "HEEPEleCount",        use_integral, "","HEEPele count eu" +xtag  ,lumi,5000,ZNormalization,filetag+"eu");
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 6,-0.5,5.5, "HEEPEleCount", "HEEPEleCount",        use_integral, "","HEEPele count uu" +xtag  ,lumi,5000,ZNormalization,filetag+"uu");
		
		//gROOT->ProcessLine(".q;");
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 50,0,250, "MET_pfsig", "MET_pfsig",        use_integral, "","E_{T}^{miss} Significance (GeV)" +xtag  ,lumi,50,ZNormalization,filetag);

		fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 60,40,340, "M_muon1muon2", "M_muon1HEEPele1", use_integral, "","M_{#mu#mu}(GeV) " +xtag,lumi,50,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, false, 60,40,340, "M_muon1muon2", "M_muon1HEEPele1", use_integral, "","M_{#mu#mu}(GeV) " +xtag,lumi,50,ZNormalization,filetag+"nosub");
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 60,40,340, "M_muon1muon2", "M_muon1HEEPele1", true, "","M_{#mu#mu}(GeV) " +xtag,lumi,50,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true,40,.-.5,39.5, "N_GoodVertices", "N_GoodVertices", use_integral, "","N_{Vertices} " +xtag,lumi,500,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true,6,.-.5,5.5, "GlobalMuonCount", "GlobalMuonCount", use_integral, "","N_{Global #mu} " +xtag,lumi,100,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true,6,.-.5,5.5, "TrackerMuonCount", "TrackerMuonCount", use_integral, "","N_{Tracker #mu} " +xtag,lumi,100,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true,12,.-.5,11.5, "PFJetCount", "PFJetCount", use_integral, "","N_{PFJet} " +xtag,lumi,500,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true,8,.-.5,7.5, "BpfJetCount", "BpfJetCount", use_integral, "","N_{BPFJet} " +xtag,lumi,500,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 60,0,30, "EcalIso_muon1", "EcalIso_muon1", use_integral, "","ECAL Iso_{#mu_{1}} (GeV) " +xtag,lumi,10,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 50,0,3, "HcalIso_muon1", "HcalIso_muon1", use_integral, "","HCAL Iso (#mu_{1}) " +xtag,lumi,10,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 35,0,3.5, "TrkIso_muon1", "TrkIso_muon1", use_integral, "","Track Iso (#mu_{1}) " +xtag,lumi,10,ZNormalization,filetag);
		fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false , true, 50,0,500, "Pt_muon1", "Pt_HEEPele", use_integral, "","p_{T} (#mu_{1}) (GeV) " +xtag,lumi,50,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 50,0,50, "PtError_muon1", "PtError_muon1", use_integral, "","#sigma(p_{T}) (#mu_{1}) (GeV) " +xtag,lumi,10,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false , true, 48,-2.4,2.4, "Eta_muon1", "Eta_muon1", use_integral, "","#eta (#mu_{1}) " +xtag,lumi,5000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 50,0,.001, "EtaError_muon1", "EtaError_muon1", use_integral, "","#sigma(#eta) (#mu_{1}) " +xtag,lumi,1000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true,30,-3.141593,3.141593, "Phi_muon1", "Phi_muon1", use_integral, "","#phi (#mu_{1}) " +xtag,lumi,2000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 50,0,.0005, "PhiError_muon1", "PhiError_muon1", use_integral, "","#sigma(#phi) (#mu_{1}) " +xtag,lumi,1000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 40,0,.0008, "QOverPError_muon1", "QOverPError_muon1", use_integral, "","#sigma(Q/p)_{#mu_{1}}(GeV) " +xtag,lumi,10,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 60,0,30, "EcalIso_muon2", "EcalIso_muon2", use_integral, "","ECAL Iso_{#mu_{2}} (GeV) " +xtag,lumi,10,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 50,0,3, "HcalIso_muon2", "HcalIso_muon2", use_integral, "","HCAL Iso (#mu_{2}) " +xtag,lumi,10,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 35,0,3.5, "TrkIso_muon2", "TrkIso_muon2", use_integral, "","Track Iso (#mu_{2}) " +xtag,lumi,10,ZNormalization,filetag);
		fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false , true, 40,0,400, "Pt_muon2", "Pt_muon2", use_integral, "","p_{T} (#mu_{2}) (GeV) " +xtag,lumi,50,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 50,0,50, "PtError_muon2", "PtError_muon2", use_integral, "","#sigma(p_{T}) (#mu_{2}) (GeV) " +xtag,lumi,10,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false , true, 48,-2.4,2.4, "Eta_muon2", "Eta_muon2", use_integral, "","#eta (#mu_{2}) " +xtag,lumi,5000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 50,0,.001, "EtaError_muon2", "EtaError_muon2", use_integral, "","#sigma(#eta) (#mu_{2}) " +xtag,lumi,1000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true,30,-3.141593,3.141593, "Phi_muon2", "Phi_muon2", use_integral, "","#phi (#mu_{2}) " +xtag,lumi,2000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 50,0,.0005, "PhiError_muon2", "PhiError_muon2", use_integral, "","#sigma(#phi) (#mu_{2}) " +xtag,lumi,1000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 40,0,.0008, "QOverPError_muon2", "QOverPError_muon2", use_integral, "","#sigma(Q/p)_{#mu_{2}}(GeV) " +xtag,lumi,10,ZNormalization,filetag);
		fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 65,200,1500, "ST_pf_mumu", "ST_pf_emu", use_integral, "","S_{T} (GeV)" +xtag,lumi,250,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, false, 65,200,1500, "ST_pf_mumu", "ST_pf_emu", use_integral, "","S_{T} (GeV)" +xtag,lumi,250,ZNormalization,filetag+"nosub");
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 65,200,1500, "ST_pf_mumu", "ST_pf_emu", true, "","S_{T} (GeV)" +xtag,lumi,250,ZNormalization,filetag);
		fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 60,0,600, "Pt_pfjet1", "Pt_pfjet1", use_integral, "","p_{T} (jet_{1}) (GeV) " +xtag,lumi,50,ZNormalization,filetag);
		fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 50,0,500, "Pt_pfjet2", "Pt_pfjet2", use_integral, "","p_{T} (jet_{2}) (GeV) " +xtag,lumi,50,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 40,-3.0,3.0, "Eta_pfjet1", "Eta_pfjet1", use_integral, "","#eta (jet_{1}) " +xtag,lumi,5000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 40,-3.0,3.0, "Eta_pfjet2", "Eta_pfjet2", use_integral, "","#eta (jet_{2}) " +xtag,lumi,5000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 63,-3.15,3.15, "deltaPhi_muon1pfjet1", "deltaPhi_muon1pfjet1", use_integral, "","#Delta#phi (#mu_{1}, j_{1}) " +xtag,lumi,10000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 63,-3.15,3.15, "deltaPhi_muon1pfjet2", "deltaPhi_muon1pfjet2", use_integral, "","#Delta#phi (#mu_{1}, j_{2}) " +xtag,lumi,10000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 63,-3.15,3.15, "deltaPhi_muon2pfjet1", "deltaPhi_muon2pfjet1", use_integral, "","#Delta#phi (#mu_{2}, j_{1}) " +xtag,lumi,10000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 63,-3.15,3.15, "deltaPhi_muon2pfjet2", "deltaPhi_muon2pfjet2", use_integral, "","#Delta#phi (#mu_{2}, j_{2}) " +xtag,lumi,10000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 60,0,6, "deltaR_muon1muon2", "deltaR_muon1muon21", use_integral, "","#Delta R (#mu_{1}, #mu_{2}) " +xtag,lumi,10000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 60,0,6, "deltaR_muon1pfjet1", "deltaR_muon1pfjet1", use_integral, "","#Delta R (#mu_{1}, j_{1}) " +xtag,lumi,10000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 60,0,6, "deltaR_muon1pfjet2", "deltaR_muon1pfjet2", use_integral, "","#Delta R (#mu_{1}, j_{2}) " +xtag,lumi,10000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 60,0,6, "deltaR_muon2pfjet1", "deltaR_muon2pfjet1", use_integral, "","#Delta R (#mu_{2}, j_{1}) " +xtag,lumi,10000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 60,0,6, "deltaR_muon2pfjet2", "deltaR_muon2pfjet2", use_integral, "","#Delta R (#mu_{2}, j_{2}) " +xtag,lumi,10000,ZNormalization,filetag);
		fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 100,10,2010, "M_bestmupfjet1_mumu", "M_bestmuORelepfjet1_mumu_emuselection", use_integral, "","M_{#mu j} (GeV)" +xtag,lumi,500,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 100,10,2010, "M_bestmupfjet1_mumu", "M_bestmuORelepfjet1_mumu_emuselection", use_integral, "","M_{#mu jet} " +xtag,lumi,500,ZNormalization,filetag+"nosub");
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 100,10,2010, "M_bestmupfjet1_mumu", "M_bestmuORelepfjet1_mumu_emuselection", true, "","M_{#mu jet} " +xtag,lumi,500,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 40,0,800, "M_pfjet1pfjet2", "M_pfjet1pfjet2", use_integral, "","M_{jj}(GeV)" +xtag,lumi,1000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 40,0,400, "MT_pfjet1pfjet2", "MT_pfjet1pfjet2", use_integral, "","M^{T}_{jj}(GeV)" +xtag,lumi,10,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 40,0,8, "deltaR_pfjet1pfjet2", "deltaR_pfjet1pfjet2", use_integral, "","#Delta R (j_{1}j_{2})(GeV)" +xtag,lumi,10000,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, Use_emu, true, 40,-3.15,3.15, "deltaPhi_pfjet1pfjet2", "deltaPhi_pfjet1pfjet2", use_integral, "","#Delta#phi (j_{1}j_{2})(GeV)" +xtag,lumi,10000,ZNormalization,filetag);
	}

	// -------------      Full Selection      -------------- //

	if (true)
	{
		Use_emu = true;

		// LQ 450
		filetag = "2011Data_FullSelection_lqmumu450";
		xtag = " [Full Selection]";
		lq_choice = "lqmumu450";

		TString cut_full_data = cut_data + "*(ST_pf_mumu > 610)*(M_muon1muon2 > 130)*(LowestMass_BestLQCombo > 250)";
		TString cut_full_data_emu = cut_data_emu + "*(ST_pf_emu > 610)*(M_muon1HEEPele1 > 130)*(LowestMass_BestLQCombo_emuselection > 250)";
		TString cut_full_mc = cut_mc +     "*(ST_pf_mumu > 610)*(M_muon1muon2 > 130)*(LowestMass_BestLQCombo > 250)";

		fillHisto(lq_choice, cut_full_mc, cut_full_data,cut_full_data_emu,  Use_emu, false, 25,0.0,2000.0, "M_bestmupfjet1_mumu", "M_bestmuORelepfjet1_mumu_emuselection", use_integral, "","M_{#mu j} (GeV)" +xtag,lumi,500,ZNormalization,filetag);
		fillHisto(lq_choice, cut_full_mc, cut_full_data,cut_full_data_emu, Use_emu, false, 25,250,2750, "ST_pf_mumu", "ST_pf_emu", use_integral, "","S_{T} (GeV)" +xtag,lumi,500,ZNormalization,filetag);
		fillHisto(lq_choice, cut_full_mc, cut_full_data,cut_full_data_emu,  Use_emu, false, 25,0.0,2000.0, "M_muon1muon2", "M_muon1HEEPele1", use_integral, "","M_{#mu#mu}(GeV) " +xtag,lumi,500,ZNormalization,filetag);

		//fillHisto(lq_choice, cut_full_mc, cut_full_data,cut_full_data_emu,  Use_emu, false, 25,0.0,2000.0, "M_bestmupfjet1_mumu", "M_bestmuORelepfjet1_mumu_emuselection", true, "","M_{#mu j} " +xtag,lumi,500,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data,cut_full_data_emu, Use_emu, false, 25,250,1750, "ST_pf_mumu", "ST_pf_emu", true, "","S_{T} (GeV)" +xtag,lumi,500,ZNormalization,filetag);

		//// LQ 600
		filetag = "2011Data_FullSelection_lqmumu600";
		xtag = " [Full Selection]";
		lq_choice = "lqmumu600";

		TString cut_full_data = cut_data + "*(ST_pf_mumu > 770)*(M_muon1muon2 > 130)*(LowestMass_BestLQCombo > 370)";
		TString cut_full_data_emu = cut_data_emu + "*(ST_pf_emu > 770)*(M_muon1HEEPele1 > 130)*(LowestMass_BestLQCombo_emuselection > 370)";
		TString cut_full_mc = cut_mc + "*(ST_pf_mumu > 770)*(M_muon1muon2 > 130)*(LowestMass_BestLQCombo > 370)";

		fillHisto(lq_choice, cut_full_mc, cut_full_data,cut_full_data_emu,  Use_emu, false, 25,0.0,2000.0, "M_bestmupfjet1_mumu", "M_bestmuORelepfjet1_mumu_emuselection", use_integral, "","M_{#mu j} (GeV)" +xtag,lumi,500,ZNormalization,filetag);
		fillHisto(lq_choice, cut_full_mc, cut_full_data,cut_full_data_emu, Use_emu, false, 25,250,2750, "ST_pf_mumu", "ST_pf_emu", use_integral, "","S_{T} (GeV)" +xtag,lumi,500,ZNormalization,filetag);
		fillHisto(lq_choice, cut_full_mc, cut_full_data,cut_full_data_emu,  Use_emu, false, 25,0.0,2000.0, "M_muon1muon2", "M_muon1HEEPele1", use_integral, "","M_{#mu#mu}(GeV) " +xtag,lumi,500,ZNormalization,filetag);

		//fillHisto(lq_choice, cut_full_mc, cut_full_data,cut_full_data_emu,  Use_emu, false, 25,0.0,2000.0, "M_bestmupfjet1_mumu", "M_bestmuORelepfjet1_mumu_emuselection", true, "","M_{#mu j} " +xtag,lumi,500,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data,cut_full_data_emu, Use_emu, false, 25,250,1750, "ST_pf_mumu", "ST_pf_emu", true, "","S_{T} (GeV)" +xtag,lumi,500,ZNormalization,filetag);

		//// LQ 750
		filetag = "2011Data_FullSelection_lqmumu750";
		xtag = " [Full Selection]";
		lq_choice = "lqmumu750";

		TString cut_full_data = cut_data + "*(ST_pf_mumu > 880)*(M_muon1muon2 > 140)*(LowestMass_BestLQCombo > 470)";
		TString cut_full_data_emu = cut_data_emu + "*(ST_pf_emu > 880)*(M_muon1HEEPele1 > 140)*(LowestMass_BestLQCombo_emuselection > 470)";
		TString cut_full_mc = cut_mc + "*(ST_pf_mumu > 880)*(M_muon1muon2 > 140)*(LowestMass_BestLQCombo > 470)";

		fillHisto(lq_choice, cut_full_mc, cut_full_data,cut_full_data_emu,  Use_emu, false, 25,0.0,2000.0, "M_bestmupfjet1_mumu", "M_bestmuORelepfjet1_mumu_emuselection", use_integral, "","M_{#mu j} (GeV)" +xtag,lumi,500,ZNormalization,filetag);
		fillHisto(lq_choice, cut_full_mc, cut_full_data,cut_full_data_emu, Use_emu, false, 25,250,2750, "ST_pf_mumu", "ST_pf_emu", use_integral, "","S_{T} (GeV)" +xtag,lumi,500,ZNormalization,filetag);
		fillHisto(lq_choice, cut_full_mc, cut_full_data,cut_full_data_emu,  Use_emu, false, 25,0.0,2000.0, "M_muon1muon2", "M_muon1HEEPele1", use_integral, "","M_{#mu#mu}(GeV) " +xtag,lumi,500,ZNormalization,filetag);

		//fillHisto(lq_choice, cut_full_mc, cut_full_data,cut_full_data_emu,  Use_emu, false, 25,0.0,2000.0, "M_bestmupfjet1_mumu", "M_bestmuORelepfjet1_mumu_emuselection", true, "","M_{#mu j} " +xtag,lumi,500,ZNormalization,filetag);
		//fillHisto(lq_choice, cut_full_mc, cut_full_data,cut_full_data_emu, Use_emu, false, 25,250,1750, "ST_pf_mumu", "ST_pf_emu", true, "","S_{T} (GeV)" +xtag,lumi,500,ZNormalization,filetag);

	}
	gROOT->Reset(); gROOT->ProcessLine(".q;");
}
