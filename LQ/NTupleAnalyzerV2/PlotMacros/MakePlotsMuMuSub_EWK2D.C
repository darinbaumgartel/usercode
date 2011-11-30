
#include "TLorentzVector.h"
#include "TH1.h"
#include <iostream>
#include <fstream>
#include <iomanip>
#include "CMSStyle.C"

void fillHisto(TString cut_mc, TString cut_data, 
	       int nBinsX, float xMin, float xMax,int nBinsY, float yMin, float yMax, TString varX,TString varY, bool writeoutput, TString fileName,TString titleX,TString titleY, TString Luminosity,Double_t extrascalefactor,Double_t znorm,TString tag)
{
	CMSStyle();
	 TCanvas *c1 = new TCanvas("c1","",1400,800);

	TPad *pad1 = new TPad("pad1","The pad 60% of the height",0.0,0.0,0.5,1.0,0);
	TPad *pad2 = new TPad("pad1","The pad 60% of the height",0.5,0.0,1.0,1.0,0);


	pad1->Draw();
	pad2->Draw();
	pad1->cd();
	//pad1->SetLogy();

	gStyle->SetOptLogy();
	TH2F* h_zjets = new TH2F("h_zjets","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);
	TH2F* h_wjets = new TH2F("h_wjets","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);
	TH2F* h_vvjets = new TH2F("h_vvjets","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);
	TH2F* h_singtop = new TH2F("h_singtop","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);
	TH2F* h_qcd = new TH2F("h_qcd","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);
	TH2F* h_ttbar = new TH2F("h_ttbar","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);
	TH2F* h_data = new TH2F("h_data","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);
	TH2F* h_lqmumu = new TH2F("h_lqmumu","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);

	zjets->Draw(varY+":"+varX+">>h_zjets",cut_mc);
	wjets->Draw(varY+":"+varX+">>h_wjets",cut_mc);
	ttbar->Draw(varY+":"+varX+">>h_ttbar",cut_mc);
	vvjets->Draw(varY+":"+varX+">>h_vvjets",cut_mc);
	singtop->Draw(varY+":"+varX+">>h_singtop",cut_mc);
	qcd->Draw(varY+":"+varX+">>h_qcd",cut_mc);
	data->Draw(varY+":"+varX+">>h_data",cut_data);


	TH2F* H_data  = new TH2F("H_data","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);
	TH2F* H_zjets = new TH2F("H_zjets","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);
	TH2F* H_wjets = new TH2F("H_wjets","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);
	TH2F* H_singtop = new TH2F("H_singtop","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);
	TH2F* H_qcd = new TH2F("H_qcd","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);
	TH2F* H_ttbar = new TH2F("H_ttbar","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);
	TH2F* H_vvjets = new TH2F("H_vvjets","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);
	TH2F* H_bkg   = new TH2F("H_bkg","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);
	TH2F* H_lq   = new TH2F("H_lq","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);

	TH2F* H_stack = new TH2F("H_stack","",nBinsX,xMin,xMax,nBinsY,yMin,yMax);

	// ******************************************************************************************************************************* //
	// Rescaling Routine and Event number Readout

	h_zjets->Scale(znorm);
	h_ttbar->Scale(0.945);

	//Double_t Nd = h_data->Integral();
	//Double_t Nmc = h_zjets->Integral()+h_ttbar->Integral()+h_vvjets->Integral()+h_wjets->Integral()+h_singtop->Integral()+h_qcd->Integral();
	//Double_t Nw = h_wjets->Integral();
	//Double_t Nt = h_ttbar->Integral();
	//Double_t Nz = h_zjets->Integral();
	//Double_t N_other = Nmc - Nz;
	
	
	//Double_t sigma_Nz = Nz*pow(1.0*(h_zjets->GetEntries()),-0.5);
	
	//Double_t sigma_N_other = 0.0;
	//if (h_ttbar->GetEntries()>0) sigma_N_other += h_ttbar->Integral()*pow((1.0*h_ttbar->GetEntries()),-0.5);
	//if (h_wjets->GetEntries()>0) sigma_N_other += h_wjets->Integral()*pow((1.0*h_wjets->GetEntries() ),-0.5);
	//if (h_vvjets->GetEntries()>0) sigma_N_other += h_vvjets->Integral()*pow((1.0*h_vvjets->GetEntries() ),-0.5);
	//if (h_singtop->GetEntries()>0) sigma_N_other += h_singtop->Integral()*pow((1.0*singtop->GetEntries()),-0.5); 
	//if (h_qcd->GetEntries()>0) sigma_N_other += h_qcd->Integral()*pow((1.0*h_qcd->GetEntries()),-0.5);
	
	//Double_t sigam_Nd = sqrt(Nd);
	
	

	//std::cout<<"Data   : "<<Nd<<std::endl;
	//std::cout<<"All MC : "<<Nmc<<std::endl;
	//std::cout<<"tt   : "<<h_ttbar->Integral()<<"  +- "<<h_ttbar->Integral()*pow(1.0*(h_ttbar->GetEntries()),-0.5)<<std::endl;
	//std::cout<<"z   : "<<h_zjets->Integral()<<"  +- "<<h_zjets->Integral()*pow(1.0*(h_zjets->GetEntries()),-0.5)<<std::endl;



	//Double_t fac_Numerator = Nd - N_other;
	//Double_t fac_Denominator = Nz;
	//Double_t fac = fac_Numerator/fac_Denominator;

	//Double_t sigma_fac_Numerator = sqrt( pow( sigam_Nd ,2.0) + pow( sigma_N_other ,2.0) ) ;
	//Double_t sigma_fac_Denominator = sigma_Nz; 
	//Double_t sigma_fac_over_fac = pow( pow((sigma_fac_Numerator/fac_Numerator),2.0)    +  pow((sigma_fac_Denominator/fac_Denominator),2.0)    ,0.5);
	//Double_t sigma_fac = sigma_fac_over_fac*fac;

	//std::cout<<"Z Scale Factor:  "<<fac<<"  +-  "<<sigma_fac<<std::endl;

	// ******************************************************************************************************************************* //



	H_bkg->Add(h_vvjets);
	H_bkg->Add(h_wjets);
	H_bkg->Add(h_singtop);
	H_bkg->Add(h_qcd);

	H_data->Add(h_data);
	//H_lq->Add(h_lqmumu);
	//H_wjets->Add(h_wjets);
	//H_zjets->Add(h_zjets);
	//H_ttbar->Add(h_ttbar);
	//H_singtop->Add(h_singtop);
	//H_qcd->Add(h_qcd);

	//H_zjets->SetFillStyle(3004);
	//H_ttbar->SetFillStyle(3005);
	//H_bkg->SetFillStyle(3008);
	//H_wjets->SetFillStyle(3007);
	//H_singtop->SetFillStyle(3006 );
	//H_qcd->SetFillStyle(3006 );
	//H_lq->SetFillStyle(0);

	//H_zjets->SetFillColor(2);
	//H_ttbar->SetFillColor(4);
	//H_wjets->SetFillColor(6);
	//H_singtop->SetFillColor(3);
	//H_qcd->SetFillColor(3);
	//H_bkg->SetFillColor(9);
	//H_lq->SetLineStyle(3);
	H_stack->SetFillColor(2);


	//H_lq->SetLineColor(1);
	//H_zjets->SetLineColor(2);
	//H_ttbar->SetLineColor(4);
	//H_wjets->SetLineColor(6);
	//H_singtop->SetLineColor(3);
	//H_qcd->SetLineColor(3);
	//H_bkg->SetLineColor(9);
	H_stack->SetLineColor(2);
	H_stack->SetMarkerColor(2);

	//H_lq->SetMarkerColor(1);
	//H_zjets->SetMarkerColor(2);
	//H_wjets->SetMarkerColor(6);
	//H_singtop->SetMarkerColor(3);
	//H_qcd->SetMarkerColor(3);
	//H_ttbar->SetMarkerColor(4);
	//H_bkg->SetMarkerColor(9);


	//H_lq->SetMarkerSize(.00000001);
	//H_zjets->SetMarkerSize(.00000001);
	//H_wjets->SetMarkerSize(.00000001);
	//H_singtop->SetMarkerSize(.00000001);
	//H_qcd->SetMarkerSize(.00000001);
	//H_ttbar->SetMarkerSize(.00000001);
	//H_bkg->SetMarkerSize(.00000001);
	H_stack->SetMarkerSize(.1);


	//H_lq->SetLineWidth(3);
	//H_zjets->SetLineWidth(2);
	//H_wjets->SetLineWidth(2);
	//H_singtop->SetLineWidth(2);
	//H_qcd->SetLineWidth(2);
	//H_ttbar->SetLineWidth(2);
	//H_bkg->SetLineWidth(2);
	//H_data->SetLineWidth(2);

	H_stack->Add(H_bkg);

	//  H_stack->Add(H_singtop);
	//  H_stack->Add(H_qcd);
	H_stack->Add(H_ttbar);
	H_stack->Add(H_zjets);
	//  H_stack->Add(H_wjets);
	//    H_stack->Add(H_lqmumu);


	//H_zjets->GetXaxis()->SetTitle(title);
	//H_wjets->GetXaxis()->SetTitle(title);
	//H_singtop->GetXaxis()->SetTitle(title);
	//H_qcd->GetXaxis()->SetTitle(title);
	//H_ttbar->GetXaxis()->SetTitle(title);
	H_data->GetXaxis()->SetTitle(titleX);
	H_data->GetXaxis()->SetTitleFont(132);
	H_stack->GetXaxis()->SetTitle(titleX);
	H_stack->GetXaxis()->SetTitleFont(132);
	
	H_data->GetXaxis()->SetTitleSize(.04);
	H_data->GetYaxis()->SetTitleSize(.04);
	H_stack->GetXaxis()->SetTitleSize(.04);
	H_stack->GetYaxis()->SetTitleSize(.04);
	
	H_data->GetXaxis()->SetLabelSize(.03);
	H_data->GetYaxis()->SetLabelSize(.03);
	H_stack->GetXaxis()->SetLabelSize(.03);
	H_stack->GetYaxis()->SetLabelSize(.03);
    H_data->GetYaxis()->SetTitleOffset(1.7);
    H_stack->GetYaxis()->SetTitleOffset(1.7);

	
	H_data->GetYaxis()->SetTitle(titleY);
	H_data->GetYaxis()->SetTitleFont(132);
	H_stack->GetYaxis()->SetTitle(titleY);
	H_stack->GetYaxis()->SetTitleFont(132);

	H_data->SetMarkerStyle(21);
	H_data->SetMarkerSize(0.3);
	H_data->SetMarkerColor(1);
	
	H_stack->SetMarkerStyle(21);
	H_stack->SetMarkerSize(0.3);
	H_stack->SetMarkerColor(2);

	gStyle->SetOptStat(0H);
	
	
	

	TLatex* txtdat =new TLatex(	 xMin + (xMax-xMin)*0.04 ,0.9*yMax, "Data, 2.0/fb");
	txtdat->SetTextFont(132);
	txtdat->SetTextSize(0.04);
	TLatex* txtmc =new TLatex(	xMin + (xMax-xMin)*0.04,0.9*yMax, "MC");
	txtmc->SetTextFont(132);
	txtmc->SetTextSize(0.04);
	
	H_data->Draw("SCAT");
	txtdat->Draw();

	pad2->cd();

	H_stack->Draw("COLZ");
	txtmc->Draw();

	//H_data->Draw("SCATSAME");

	//H_lq->Draw("SAME");
	//H_data->Draw("SCATSAME");
	//TLegend* leg = new TLegend(0.6,0.63,0.91,0.91,"","brNDC");
	//leg->SetTextFont(132);
	//leg->SetFillColor(0);
	//leg->SetBorderSize(0);
	//leg->AddEntry(H_data,"Data 2011, "+Luminosity+" pb^{-1}");
	//leg->AddEntry(H_zjets,"Z/#gamma* + jets");
	//leg->AddEntry(H_ttbar,"t#bar{t}");
	//leg->AddEntry(H_ttbar,"t#bar{t} + VV [Data Driven e-#mu]");
	
	//leg->AddEntry(H_bkg,"Other backgrounds");

	//leg->Draw("SAME");
	//c1->SetLogy();

	//H_data->SetMinimum(.05);
	//H_data->SetMaximum(1.2*extrascalefactor*(H_data->GetMaximum()));
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

	TString varname = varX+'_'+varY;
	varname +="_";
	varname += str;
	//std::cout<<varname<<std::endl;


	//if (drawSub)  {
		//pad2->cd();
	
		//TH2F* h_comp = new TH2F("h_comp","",nBins,xLow,xMax,nBins,xLow,xMax);
		//TH2F* h_compr = new TH2F("h_compr","",nBins,xLow,xMax,nBins,xLow,xMax);	
	
	
		//if (true)
		//{
	
			//TH2F* h_bg = new TH2F("h_bg","",nBins,xLow,xMax,nBins,xLow,xMax);
			//h_bg->Sumw2();
			//h_bg->Add(h_zjets);
			//h_bg->Add(h_wjets);
			//h_bg->Add(h_vvjets);
			//h_bg->Add(h_ttbar);
			//h_bg->Add(h_singtop);
			//h_bg->Add(h_qcd);
	
			//int nbinsx = h_bg->GetXaxis()->GetNbins();
	
			//int ibin = 0;
	
			//float chi2 = 0.0;
	
			//float ndat = 0.0;
			//float nbg = 0.0;
			//float err_nbg = 0.0;
			//float err_total = 0.0;
	
			//float datmean = 0.0;
			//float mcmean = 0.0;
	
			//float xminl = 0;
			//float xmaxl = 0;
	
			////std::cout<<" Starting bin analysis" <<std::endl;
			//for (ibin=0;ibin<=nbinsx;ibin++)
			//{
				//ndat = 1.0*(h_data->GetBinContent(ibin));
				//nbg = 1.0*(h_bg->GetBinContent(ibin));
				//datmean += 1.0*(h_data->GetBinContent(ibin))*h_data->GetBinCenter(ibin);
				//err_nbg = 1.0*(h_bg->GetBinError(ibin));
				//err_total = sqrt(  pow(err_nbg,2.0) + ndat );
	
				//mcmean += 1.0*(h_bg->GetBinContent(ibin))*h_bg->GetBinCenter(ibin);
				//if (ndat!=0)   chi2 += pow((ndat -nbg),2.0)/pow(ndat,0.5);
				////if (nbg>.0010) std::cout<<h_data->GetBinCenter(ibin)<<"  "<<nbg<<" "<<"  "<<ndat/nbg<<"  "<<(ndat-nbg)/sqrt(ndat)<<std::endl;
				//h_comp ->SetBinContent(ibin,0.0 );
				//h_compr ->SetBinContent(ibin,0.0 );
				//if (ndat!=0 && nbg != 0) h_comp ->SetBinContent(ibin, (ndat - nbg)/err_total );
				//if (ndat!=0 && nbg != 0) h_compr ->SetBinContent(ibin, (ndat - nbg)/nbg );
				//if (ndat!=0 && nbg != 0) h_compr ->SetBinError(ibin, (err_total)/nbg );
	
				////if ((ndat!=0)&&(abs((ndat - nbg)/sqrt(ndat))>7.99 )) h_comp ->SetBinContent(ibin, 7.95*(ndat>nbg) - 7.95*(ndat<nbg));
				////std::cout<<nbg<<" \t ,\t # "<<h_bg->GetBinCenter(ibin)<<std::endl;
				////H_lq
				////std::cout<<H_lq->GetBinContent(ibin)<<" \t ,\t # "<<h_bg->GetBinCenter(ibin)<<std::endl;
	
			//}
	
			////std::cout<<"Chi^2 for this distribution is:  "<< chi2<<std::endl;
		//}
		//h_comp->GetYaxis()->SetTitle("N(#sigma) Diff.");
		//h_comp->GetYaxis()->SetTitleFont(132);
		//h_comp->GetYaxis()->SetTitleSize(.17);
		//h_comp->GetYaxis()->SetLabelSize(.11);
		//h_comp->GetXaxis()->SetLabelSize(.11);	
		//h_comp->GetYaxis()->SetTitleOffset(.25);
	
		//TLine *line0 = new TLine(xLow,0,xMax,0);
		//TLine *line2u = new TLine(xLow,2,xMax,2);
		//TLine *line2d = new TLine(xLow,-2,xMax,-2);
	
		//h_comp->SetMinimum(-8);
		//h_comp->SetMaximum(8);
		//h_comp->SetMarkerStyle(21);
		//h_comp->SetMarkerSize(0.5);
		////h_comp->SetMarkerSize(0.0);
	
	
		//h_comp->Draw("p");
		//line0->Draw("SAME");
		//line2u->Draw("SAME");
		//line2d->Draw("SAME");
		
		
		//pad2r->cd();
	
		//h_compr->GetYaxis()->SetTitle("Frac. Diff.");
		//h_compr->GetYaxis()->SetTitleFont(132);
		//h_compr->GetYaxis()->SetTitleSize(.17);
		//h_compr->GetYaxis()->SetLabelSize(.11);
		//h_compr->GetXaxis()->SetLabelSize(.11);	
		//h_compr->GetYaxis()->SetTitleOffset(.25);
	   ////TGaxis *axis = new TGaxis(xMax,-2,xMax,2,-2,2,50510,"+L");
	   ////axis->SetLabelColor(kRed);
	////axis->Draw();
	
		//h_compr->SetMinimum(-2);
		//h_compr->SetMaximum(2);
		//h_compr->SetLineColor(kRed);
		//h_compr->SetLineWidth(2);
		//h_compr->SetMarkerColor(kRed);
		//h_compr->SetMarkerStyle(1);
		//h_compr->SetMarkerSize(0.0);
	
		//h_compr->Draw("ep");
		//line0->Draw("SAME");

	//}


	c1->Print("PlotsMuMuSub_EWKCheck2D_Best_V00_02_05/"+varname+"_"+tag+".png");
	c1->Print("PlotsMuMuSub_EWKCheck2D_Best_V00_02_05/"+varname+"_"+tag+".pdf");
	
	
	TIter next(gDirectory->GetList());
	TObject* obj;
	while(obj= (TObject*)next()){
		if(obj->InheritsFrom(TH1::Class())){
			obj->Delete();
		}
	}
}


void MakePlotsMuMuSub_EWK2D()
{

	// Load files and trees:
	 gROOT->ProcessLine(".x LoadCastorFiles_EWK.C");

	// -------- PF ---------

	TString lumi = "2000"  ;
	TString cut_data = "(Pt_muon1>25)*(Pt_muon2>20)";
	cut_data += "*(Pt_pfjet1>25)*(Pt_pfjet2>25)";
	cut_data += "*(M_muon1muon2>50)*((M_muon1muon2<70)||(M_muon1muon2>100))";
	//cut_data += "*(deltaR_muon1muon2>0.3)";
	//cut_data += "*((abs(Eta_muon1)<2.1)||(abs(Eta_muon2)<2.1))";
	cut_data += "*((abs(Eta_muon1)<2.4)*(abs(Eta_muon2)<2.4))";
	
	cut_data += "*((BDisc_pfjet1>2.0)||(BDisc_pfjet2>2.0))";
		//cut_data+="*(BpfJetCount>1.50)";


	//----------Declare what lqmumu variable you'd like to display----
	//TString lq_choice = "lqmumu400";
	TString lq_choice = "nothing";

	//---------emu stuff--------
	bool Use_emu = false;

	TString cut_data_emu = "(((Pt_muon1>25)*(Pt_HEEPele1>20))||((Pt_muon1>20)*(Pt_HEEPele1>25)))";
	cut_data_emu += "*(Pt_pfjet1>120)*(Pt_pfjet2>30)";
	cut_data_emu += "*(M_muon1muon2>50)*((M_muon1muon2<70)||(M_muon1muon2>100))";
	cut_data_emu += "*(deltaR_muon1HEEPele1>0.3)";
	cut_data_emu += "*((abs(Eta_muon1)<2.1)||(abs(Eta_HEEPele1)<2.1))";

	//cut_data += "*((M_muon1muon2>80)*(M_muon1muon2<100))";

	TString cut_mc = lumi+ "*weight_pileup2fb*("+cut_data+")";

	//cut_data += "*(LowestUnprescaledTriggerPass>0.5)";
	//cut_data_emu += "*(LowestUnprescaledTriggerPass>0.5)";

//cut_mc += "*(";
//cut_mc += "((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)*(0.137148419144))+";
//cut_mc += "((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)*(0.570685400523))+";
//cut_mc += "((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)*(1.14449974737))+";
//cut_mc += "((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)*(1.8163157224))+";
//cut_mc += "((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)*(2.270776812))+";
//cut_mc += "((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)*(2.29783559215))+";
//cut_mc += "((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)*(2.05828090818))+";
//cut_mc += "((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)*(1.70525206573))+";
//cut_mc += "((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)*(1.28872517493))+";
//cut_mc += "((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)*(0.914713614527))+";
//cut_mc += "((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)*(0.625159994865))+";
//cut_mc += "((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)*(0.400496981648))+";
//cut_mc += "((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)*(0.245671305417))+";
//cut_mc += "((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)*(0.149501993628))+";
//cut_mc += "((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)*(0.0943735268094))+";
//cut_mc += "((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)*(0.055714218504))+";
//cut_mc += "((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)*(0.032273131211))+";
//cut_mc += "((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)*(0.0193368300632))+";
//cut_mc += "((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)*(0.0109074260718))+";
//cut_mc += "((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)*(0.00646596430331))+";
//cut_mc += "((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)*(0.00324352812525))+";
//cut_mc += "((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)*(0.00178440502281))+";
//cut_mc += "((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)*(0.00111645018356))+";
//cut_mc += "((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)*(0.000602006464283))+";
//cut_mc += "((N_PileUpInteractions > 23.5)*(0.000602006464283))";
//cut_mc += ")";


//cut_mc += "*(";
//cut_mc += "((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)*(0.0752233034121))+";
//cut_mc += "((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)*(0.361994702942))+";
//cut_mc += "((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)*(0.787119271271))+";
//cut_mc += "((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)*(1.31779962348))+";
//cut_mc += "((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)*(1.76293927848))+";
//cut_mc += "((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)*(1.99059826007))+";
//cut_mc += "((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)*(2.00731349758))+";
//cut_mc += "((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)*(1.82730847106))+";
//cut_mc += "((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)*(1.56802352509))+";
//cut_mc += "((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)*(1.26852456276))+";
//cut_mc += "((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)*(0.993808726427))+";
//cut_mc += "((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)*(0.760786688881))+";
//cut_mc += "((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)*(0.566015549542))+";
//cut_mc += "((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)*(0.41722578577))+";
//cut_mc += "((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)*(0.303388545407))+";
//cut_mc += "((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)*(0.220634364549))+";
//cut_mc += "((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)*(0.155308189438))+";
//cut_mc += "((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)*(0.110585960196))+";
//cut_mc += "((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)*(0.0776646451932))+";
//cut_mc += "((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)*(0.0543492223545))+";
//cut_mc += "((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)*(0.037244740125))+";
//cut_mc += "((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)*(0.0259826507587))+";
//cut_mc += "((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)*(0.0175412449088))+";
//cut_mc += "((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)*(0.0118325534711))+";
//cut_mc += "((N_PileUpInteractions > 23.5)*(0.00))";
//cut_mc += ")";



	float ZNormalization = 1.06;
	bool doTTStudy = false;
	TString filetag = " ";
	TString xtag = " ";



	TString cut_data_store = cut_data;
	TString cut_mc_store = cut_mc;
	TString cut_data_emu_store = cut_data_emu;

	// ------------- Normalization Calculation                         -------------- //



	// ------------- Plots and so forth                         -------------- //

	if (true){

	Use_emu = false;
	
	TString filetag = "2011Data_NormalSelection";
	TString xtag = " [ no additional cuts]";
	//gROOT->ProcessLine(".q;");	

	fillHisto(cut_mc, cut_data, 150,0,1500,150,0,1500, "M_muon1muon2pfjet1pfjet2", "M_pfjet1pfjet2", false, "","M_{#mu#mujj} (GeV)" +xtag,"M_{jj} (GeV)",lumi,100,ZNormalization,filetag);
	fillHisto(cut_mc, cut_data, 150,0,1500,150,0,1500, "M_muon1muon2pfjet1pfjet2", "M_muon1muon2", false, "","M_{#mu#mujj} (GeV)" +xtag,"M_{#mu #mu} (GeV)",lumi,100,ZNormalization,filetag);
	fillHisto(cut_mc, cut_data, 150,0,1500,150,0,1500, "M_muon1muon2pfjet1pfjet2", "M_muon1muon2pfjet1", false, "","M_{#mu#mujj} (GeV)" +xtag,"M_{#mu #mu j} (GeV)",lumi,100,ZNormalization,filetag);
	fillHisto(cut_mc, cut_data, 150,0,1500,150,0,1500, "M_muon1muon2pfjet1pfjet2", "M_muon1pfjet1pfjet2", false, "","M_{#mu#mujj} (GeV)" +xtag,"M_{#mu j j} (GeV)",lumi,100,ZNormalization,filetag);



	//fillHisto(lq_choice, cut_mc, cut_data,cut_data_emu, false, true, 50,0,2000, "M_muon1muon2pfjet1pfjet2", "M_muon1muon2pfjet1pfjet2", false, "","M_{#mu#mujj} (GeV)" +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false , true, 50,0,1000, "M_muon1muon2", "M_muon1muon2", false, "","M_{#mu#mu}(GeV) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false , true, 50,0,2000, "M_pfjet1pfjet2", "M_pfjet1pfjet2", false, "","M_{ j j }(GeV) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false , true, 50,0,2000, "M_muon1muon2pfjet1", "M_muon1muon2pfjet1", false, "","M_{ #mu #mu j}(GeV) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false , true, 50,0,2000, "M_muon1pfjet1pfjet2", "M_muon1pfjet1pfjet2", false, "","M_{ #mu j j }(GeV) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data,cut_data_emu, false, true,12,.-.5,11.5, "PFJetCount", "PFJetCount", false, "","Jet Count" +xtag,lumi,500,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data,cut_data_emu, false, true,12,.-.5,11.5, "BpfJetCount", "BpfJetCount", false, "","BJet Count" +xtag,lumi,500,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true,25,.-.5,24.5, "N_Vertices", "N_Vertices", false, "","N_{Vertices} " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 60,0,600, "Pt_muon2", "Pt_muon2", false, "","p_{T} (#mu_{2}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 80,0,800, "Pt_muon1", "Pt_HEEPele", false, "","p_{T} (#mu_{1}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 80,0,800, "Pt_muon1", "Pt_HEEPele", false, "","p_{T} (#mu_{1}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);

	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 50,0,100, "ChiSq_muon1", "ChiSq_muon1", false, "","#chi^{2} (#mu_{1}) " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 50,0,100, "ChiSq_muon2", "ChiSq_muon2", false, "","#chi^{2} (#mu_{2}) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,400, "MET_pf", "MET_pf",        false, "","E_{T}^{miss}(GeV) " +xtag  ,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_muon1muon2", "deltaR_muon1muon2", false, "","#Delta R (#mu_{1}, #mu_{2}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_muon1pfjet1", "deltaR_muon1pfjet1", false, "","#Delta R (#mu_{1}, j_{1}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_muon1pfjet2", "deltaR_muon1pfjet2", false, "","#Delta R (#mu_{1}, j_{2}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_muon2pfjet1", "deltaR_muon2pfjet1", false, "","#Delta R (#mu_{2}, j_{1}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_muon2pfjet2", "deltaR_muon2pfjet2", false, "","#Delta R (#mu_{2}, j_{2}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 60,0,600, "Pt_pfjet1", "Pt_pfjet1", false, "","p_{T} (jet_{1}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 50,0,500, "Pt_pfjet2", "Pt_pfjet2", false, "","p_{T} (jet_{2}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,-4,4, "Eta_pfjet1", "Eta_pfjet1", false, "","#eta (jet_{1}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,-4,4, "Eta_pfjet2", "Eta_pfjet2", false, "","#eta (jet_{2}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_pfjet1pfjet2", "deltaR_pfjet1pfjet2", false, "","#Delta R (j_{1}j_{2})(GeV)" +xtag,lumi,10000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 50,.01,1500.01, "M_bestmupfjet1_mumu", "M_bestmuORelepfjet1_mumu_emuselection", false, "","M_{#mu jet} " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "BDisc_pfjet1", "BDisc_pfjet1", false, "","BDiscrim (jet_{1}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "BDisc_pfjet2", "BDisc_pfjet2", false, "","BDiscrim (jet_{2}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);





	//TString filetag = "2011Data_2BJetSelection";
	//TString xtag = " [ 2 BJets ]";


	//cut_data = cut_data_store + "*((BDisc_pfjet1>2.0)||(BDisc_pfjet2>2.0))";
	//cut_mc = cut_mc_store + "*((BDisc_pfjet1>2.0)||(BDisc_pfjet2>2.0))";
	//cut_data_emu = cut_data_emu_store + "*((BDisc_pfjet1>2.0)||(BDisc_pfjet2>2.0))";



	//fillHisto(lq_choice, cut_mc, cut_data,cut_data_emu, false, true, 25,0,1500, "M_muon1muon2pfjet1pfjet2", "M_muon1muon2pfjet1pfjet2", false, "","M_{#mu#mujj} (GeV)" +xtag,lumi,100,ZNormalization,filetag+"EWKBinning");
	//fillHisto(lq_choice, cut_mc, cut_data,cut_data_emu, false, true, 50,0,2000, "M_muon1muon2pfjet1pfjet2", "M_muon1muon2pfjet1pfjet2", false, "","M_{#mu#mujj} (GeV)" +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false , true, 50,0,1000, "M_muon1muon2", "M_muon1muon2", false, "","M_{#mu#mu}(GeV) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false , true, 50,0,2000, "M_pfjet1pfjet2", "M_pfjet1pfjet2", false, "","M_{ j j }(GeV) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false , true, 50,0,2000, "M_muon1muon2pfjet1", "M_muon1muon2pfjet1", false, "","M_{ #mu #mu j}(GeV) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false , true, 50,0,2000, "M_muon1pfjet1pfjet2", "M_muon1pfjet1pfjet2", false, "","M_{ #mu j j }(GeV) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data,cut_data_emu, false, true,12,.-.5,11.5, "PFJetCount", "PFJetCount", false, "","Jet Count" +xtag,lumi,500,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data,cut_data_emu, false, true,12,.-.5,11.5, "BpfJetCount", "BpfJetCount", false, "","BJet Count" +xtag,lumi,500,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true,25,.-.5,24.5, "N_Vertices", "N_Vertices", false, "","N_{Vertices} " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 60,0,600, "Pt_muon2", "Pt_muon2", false, "","p_{T} (#mu_{2}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,400, "Pt_HEEPele1", "Pt_HEEPele1", false, "","p_{T} (e_{1}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 50,0,100, "ChiSq_muon1", "ChiSq_muon1", false, "","#chi^{2} (#mu_{1}) " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 50,0,100, "ChiSq_muon2", "ChiSq_muon2", false, "","#chi^{2} (#mu_{2}) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,400, "MET_pf", "MET_pf",        false, "","E_{T}^{miss}(GeV) " +xtag  ,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_muon1muon2", "deltaR_muon1muon2", false, "","#Delta R (#mu_{1}, #mu_{2}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_muon1pfjet1", "deltaR_muon1pfjet1", false, "","#Delta R (#mu_{1}, j_{1}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_muon1pfjet2", "deltaR_muon1pfjet2", false, "","#Delta R (#mu_{1}, j_{2}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_muon2pfjet1", "deltaR_muon2pfjet1", false, "","#Delta R (#mu_{2}, j_{1}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_muon2pfjet2", "deltaR_muon2pfjet2", false, "","#Delta R (#mu_{2}, j_{2}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 60,0,600, "Pt_pfjet1", "Pt_pfjet1", false, "","p_{T} (jet_{1}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 50,0,500, "Pt_pfjet2", "Pt_pfjet2", false, "","p_{T} (jet_{2}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,-4,4, "Eta_pfjet1", "Eta_pfjet1", false, "","#eta (jet_{1}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,-4,4, "Eta_pfjet2", "Eta_pfjet2", false, "","#eta (jet_{2}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_pfjet1pfjet2", "deltaR_pfjet1pfjet2", false, "","#Delta R (j_{1}j_{2})(GeV)" +xtag,lumi,10000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 50,.01,1500.01, "M_bestmupfjet1_mumu", "M_bestmuORelepfjet1_mumu_emuselection", false, "","M_{#mu jet} " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "BDisc_pfjet1", "BDisc_pfjet1", false, "","BDiscrim (jet_{1}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "BDisc_pfjet2", "BDisc_pfjet2", false, "","BDiscrim (jet_{2}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);





	//TString filetag = "2011Data_ExcessRegion";
	//TString xtag = " [ Excess Region 0.9 - 1.1 TeV ]";

	//cut_data = cut_data_store + "*(M_muon1muon2pfjet1pfjet2>900)*(M_muon1muon2pfjet1pfjet2<1100)";
	//cut_mc = cut_mc_store + "*(M_muon1muon2pfjet1pfjet2>900)*(M_muon1muon2pfjet1pfjet2<1100)";
	//cut_data_emu += cut_data_emu_store += "*(M_muon1muon2pfjet1pfjet2>900)*(M_muon1muon2pfjet1pfjet2<1100)";
	
	
	//fillHisto(lq_choice, cut_mc, cut_data,cut_data_emu, false, true, 25,0,1500, "M_muon1muon2pfjet1pfjet2", "M_muon1muon2pfjet1pfjet2", false, "","M_{#mu#mujj} (GeV)" +xtag,lumi,100,ZNormalization,filetag+"EWKBinning");
	//fillHisto(lq_choice, cut_mc, cut_data,cut_data_emu, false, true, 50,0,2000, "M_muon1muon2pfjet1pfjet2", "M_muon1muon2pfjet1pfjet2", false, "","M_{#mu#mujj} (GeV)" +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false , true, 50,0,1000, "M_muon1muon2", "M_muon1muon2", false, "","M_{#mu#mu}(GeV) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false , true, 50,0,2000, "M_pfjet1pfjet2", "M_pfjet1pfjet2", false, "","M_{ j j }(GeV) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false , true, 50,0,2000, "M_muon1muon2pfjet1", "M_muon1muon2pfjet1", false, "","M_{ #mu #mu j}(GeV) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false , true, 50,0,2000, "M_muon1pfjet1pfjet2", "M_muon1pfjet1pfjet2", false, "","M_{ #mu j j }(GeV) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data,cut_data_emu, false, true,12,.-.5,11.5, "PFJetCount", "PFJetCount", false, "","Jet Count" +xtag,lumi,500,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data,cut_data_emu, false, true,12,.-.5,11.5, "BpfJetCount", "BpfJetCount", false, "","BJet Count" +xtag,lumi,500,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true,25,.-.5,24.5, "N_Vertices", "N_Vertices", false, "","N_{Vertices} " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 60,0,600, "Pt_muon2", "Pt_muon2", false, "","p_{T} (#mu_{2}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 80,0,800, "Pt_muon1", "Pt_HEEPele", false, "","p_{T} (#mu_{1}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 50,0,100, "ChiSq_muon1", "ChiSq_muon1", false, "","#chi^{2} (#mu_{1}) " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 50,0,100, "ChiSq_muon2", "ChiSq_muon2", false, "","#chi^{2} (#mu_{2}) " +xtag,lumi,100,ZNormalization,filetag);	
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,400, "MET_pf", "MET_pf",        false, "","E_{T}^{miss}(GeV) " +xtag  ,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_muon1muon2", "deltaR_muon1muon2", false, "","#Delta R (#mu_{1}, #mu_{2}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_muon1pfjet1", "deltaR_muon1pfjet1", false, "","#Delta R (#mu_{1}, j_{1}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_muon1pfjet2", "deltaR_muon1pfjet2", false, "","#Delta R (#mu_{1}, j_{2}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_muon2pfjet1", "deltaR_muon2pfjet1", false, "","#Delta R (#mu_{2}, j_{1}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_muon2pfjet2", "deltaR_muon2pfjet2", false, "","#Delta R (#mu_{2}, j_{2}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 60,0,600, "Pt_pfjet1", "Pt_pfjet1", false, "","p_{T} (jet_{1}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 50,0,500, "Pt_pfjet2", "Pt_pfjet2", false, "","p_{T} (jet_{2}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,-4,4, "Eta_pfjet1", "Eta_pfjet1", false, "","#eta (jet_{1}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,-4,4, "Eta_pfjet2", "Eta_pfjet2", false, "","#eta (jet_{2}) " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "deltaR_pfjet1pfjet2", "deltaR_pfjet1pfjet2", false, "","#Delta R (j_{1}j_{2})(GeV)" +xtag,lumi,10000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 50,.01,1500.01, "M_bestmupfjet1_mumu", "M_bestmuORelepfjet1_mumu_emuselection", false, "","M_{#mu jet} " +xtag,lumi,1000,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "BDisc_pfjet1", "BDisc_pfjet1", false, "","BDiscrim (jet_{1}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);
	//fillHisto(lq_choice, cut_mc, cut_data, cut_data_emu, false, true, 40,0,8, "BDisc_pfjet2", "BDisc_pfjet2", false, "","BDiscrim (jet_{2}) (GeV) " +xtag,lumi,100,ZNormalization,filetag);



}


	gROOT->Reset(); gROOT->ProcessLine(".q;");
}
