
#include "TLorentzVector.h"
#include "TH1.h"
#include <iostream>
#include <fstream>
#include <iomanip>
#include "CMSStyle.C"

void fillHisto(TString cut_mc, TString cut_data,  TString cut_data_emu,  bool Use_emu, bool drawHistograms,
	       int nBins, float xLow, float xMax, TString var, TString var_data, bool writeoutput, TString fileName,TString title, TString Luminosity,Double_t extrascalefactor,Double_t znorm,TString tag)
{
	CMSStyle();
	//  TCanvas c1("c1", "First canvas", 400, 300); // problems here
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

	//====Creating Histos
	TH1F* h_vvjets = new TH1F("h_vvjets","",nBins,xLow,xMax);
	TH1F* h_ttbar = new TH1F("h_ttbar","",nBins,xLow,xMax);
	TH1F* h_data = new TH1F("h_data","",nBins,xLow,xMax);
	//======Drawing histos
	ttbar->Draw(var+">>h_ttbar",cut_mc);
	vvjets->Draw(var+">>h_vvjets",cut_mc);
	data->Draw(var_data+">>h_data",cut_data);

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
		TH1F* h2_lqmumu = new TH1F("h2_lqmumu","",nBins,xLow,xMax);

		zjets->Draw(var2+">>h2_zjets",cut_mc);
		wjets->Draw(var2+">>h2_wjets",cut_mc);
		if (!Use_emu) {ttbar->Draw(va2r+">>h2_ttbar",cut_mc);}
		else if (Use_emu) {data->Draw(var+">>h2_ttbar",cut_data_emu);}
		ttbar->Draw(var2+">>h2_ttbar",cut_mc);
		vvjets->Draw(var2+">>h2_vvjets",cut_mc);
		singtop->Draw(var2+">>h2_singtop",cut_mc);
		qcd->Draw(var2+">>h2_qcd",cut_mc);
		data->Draw(+var2+">>h2_data",cut_data);
		lqmumu->Draw(var2+">>h2_lqmumu",cut_mc);

		h_zjets->Add(h2_zjets);
		h_wjets->Add(h2_wjets);
		h_ttbar->Add(h2_ttbar);
		h_vvjets->Add(h2_vvjets);
		h_singtop->Add(h2_singtop);
		h_qcd->Add(h2_qcd);
		h_data->Add(h2_data);
		h_lqmumu->Add(h2_lqmumu);

		// Rename variable
		var = "M_bestmupfjetcombo_mumu";
	}

	TH1F* H_data  = new TH1F("H_data","",nBins,xLow,xMax);
	TH1F* H_ttbar = new TH1F("H_ttbar","",nBins,xLow,xMax);
	TH1F* H_vvjets = new TH1F("H_vvjets","",nBins,xLow,xMax);
	TH1F* H_bkg   = new TH1F("H_bkg","",nBins,xLow,xMax);
	TH1F* H_lq   = new TH1F("H_lq","",nBins,xLow,xMax);

	THStack* H_stack = new THStack("H_stack","");

	// ******************************************************************************************************************************* //
	// Rescaling Routine and Event number Readout



	if (!Use_emu) {h_ttbar->Scale(1.00);}
	else if (Use_emu) {h_ttbar->Scale(1.00);}
	
	//====Here I added a piece to scale the data by .6284, since that is the emu part
	h_data->Scale(0.47);


	Double_t Nd = h_data->Integral();
	Double_t Nmc = h_ttbar->Integral()+h_vvjets->Integral();
	Double_t Nt = h_ttbar->Integral();
	Double_t N_other = Nmc;
	
	Double_t sigma_N_other = 0.0;
	if (h_ttbar->GetEntries()>0) sigma_N_other += h_ttbar->Integral()*pow((1.0*h_ttbar->GetEntries()),-0.5);
	
	if (h_vvjets->GetEntries()>0) sigma_N_other += h_vvjets->Integral()*pow((1.0*h_vvjets->GetEntries() ),-0.5);
	
	
	
	Double_t sigam_Nd = sqrt(Nd);
	
	

	std::cout<<"Data   : "<<Nd<<std::endl;
	std::cout<<"All MC : "<<Nmc<<std::endl;
	std::cout<<"tt   : "<<h_ttbar->Integral()<<"  +- "<<h_ttbar->Integral()*pow(1.0*(h_ttbar->GetEntries()),-0.5)<<std::endl;
	

	H_bkg->Add(h_vvjets);
	H_data->Add(h_data);
	H_ttbar->Add(h_ttbar);
	H_ttbar->SetFillStyle(3005);
	H_bkg->SetFillStyle(3008);
	H_ttbar->SetFillColor(4);
	H_bkg->SetFillColor(9);
	H_ttbar->SetLineColor(4);
	H_bkg->SetLineColor(9);
	H_ttbar->SetMarkerColor(4);
	H_bkg->SetMarkerColor(9);
	H_ttbar->SetMarkerSize(.00000001);
	H_bkg->SetMarkerSize(.00000001);
	H_ttbar->SetLineWidth(2);
	H_bkg->SetLineWidth(2);
	H_data->SetLineWidth(2);

	H_stack->Add(H_bkg);

	H_stack->Add(H_ttbar);
	
	H_ttbar->GetXaxis()->SetTitle(title);
	H_data->GetXaxis()->SetTitle(title);
	H_data->GetYaxis()->SetTitle("Number of Events");
	H_data->GetXaxis()->SetTitleFont(132);
	H_data->GetYaxis()->SetTitleFont(132);

	H_data->SetMarkerStyle(21);
	H_data->SetMarkerSize(0.0);
	gStyle->SetOptStat(0H);
	H_data->Draw("E");

	H_stack->Draw("SAME");
	
	H_data->Draw("SAMEE");
	TLegend* leg = new TLegend(0.6,0.63,0.91,0.91,"","brNDC");
	leg->SetTextFont(132);
	leg->SetFillColor(0);
	leg->SetBorderSize(0);
	leg->AddEntry(H_data,"Data 2011, "+Luminosity+" pb^{-1}");
	
	leg->AddEntry(H_ttbar,"t#bar{t}");
	leg->AddEntry(H_bkg,"Diboson");
	
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
		
		
		h_bg->Add(h_vvjets);
		h_bg->Add(h_ttbar);
		
		

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

			//if ((ndat!=0)&&(abs((ndat - nbg)/sqrt(ndat))>7.99 )) h_comp ->SetBinContent(ibin, 7.95*(ndat>nbg) - 7.95*(ndat<nbg));

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



	c1->Print("PlotsEMuComparison/"+varname+"_"+tag+".png");
	c1->Print("PlotsEMuComparison/"+varname+"_"+tag+".pdf");
	
	
	TIter next(gDirectory->GetList());
	TObject* obj;
	while(obj= (TObject*)next()){
		if(obj->InheritsFrom(TH1::Class())){
			obj->Delete();
		}
	}
}


void CompareEmuTTDiJet()
{

	// Load files and trees:
	 gROOT->ProcessLine(".x LoadCastorFiles.C");

	// -------- PF ---------


	//
	TString lumi = "2000"  ;
	TString cut_data = "(Pt_muon1>40)*(Pt_muon2>40)";
	cut_data += "*(Pt_pfjet1>30)*(Pt_pfjet2>30)";
	cut_data += "*(M_muon1muon2>50)";
	cut_data += "*(deltaR_muon1muon2>0.3)";
	cut_data += "*((abs(Eta_muon1)<2.1)||(abs(Eta_muon2)<2.1))";

	//---------emu stuff--------
	bool Use_emu = false;
	TString cut_data_emu = "(Pt_muon1>40)*(Pt_HEEPele1>40)";
	cut_data_emu += "*(Pt_pfjet1>30)*(Pt_pfjet2>30)";
	cut_data_emu += "*(M_muon1HEEPele1>50)";
	cut_data_emu += "*(deltaR_muon1HEEPele1>0.3)";
	cut_data_emu += "*((abs(Eta_muon1)<2.1)||(abs(Eta_HEEPele1)<2.1))";
	cut_data += "*(LowestUnprescaledTriggerPass>0.5)";
	cut_data_emu += "*(LowestUnprescaledTriggerPass>0.5)";	

	//cut_data += "*((M_muon1muon2>80)*(M_muon1muon2<100))";

	TString cut_mc = lumi+ "*weight*("+cut_data+")";
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



        float ZNormalization = 1.01; // 1.00;
	TString filetag = " ";
	TString xtag = " ";



	
	// ------------- Pre Selection - Preselection With ST>250 Cut      -------------- //
	
	cut_data += "*(ST_pf_mumu>250.0)";
	cut_mc += "*(ST_pf_mumu>250.0)";
	cut_data_emu += "*(ST_pf_emu>250.0)";
	TString filetag = "2011Data_PreSelection";
	TString xtag = " [preselection]";

	//NOTE: The first instance of cut_data_emu is in the field for the cut that is NOT on emu, rather just the standard cut
	//This is due to the fact that here we actually need the DATA itself to match emu cuts, with Monte Carlo being entirely dimuon

	//Also: The second ST is used for the variable var_data which is passed into the Draw function for h_data in the fillHisto function
	fillHisto(cut_mc, cut_data_emu, cut_data_emu, Use_emu, true, 80,200,1000, "ST_pf_mumu", "ST_pf_emu", false, "","S_{T} (GeV)" +xtag,lumi,50,ZNormalization,filetag);





	gROOT->Reset(); gROOT->ProcessLine(".q;");
}
