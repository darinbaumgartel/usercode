#include "TROOT.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TH2F.h"
#include "TGraph.h"
#include "TF1.h"
#include "TLegend.h"
#include "TPad.h"
#include "TLatex.h"
#include "TSpline.h"

using namespace std;

void myStyle()
{
 gStyle->Reset("Default");
 gStyle->SetCanvasColor(0);
 gStyle->SetPadColor(0);
 gStyle->SetTitleFillColor(10);
 gStyle->SetCanvasBorderMode(0);
 gStyle->SetStatColor(0);
 gStyle->SetPadBorderMode(0);
 gStyle->SetPadTickX(1);  // To get tick marks on the opposite side of the frame
 gStyle->SetPadTickY(1);
 gStyle->SetFrameBorderMode(0);
 gStyle->SetPalette(1);

   //gStyle->SetOptStat(kFALSE);
 gStyle->SetOptStat(111110);
 gStyle->SetOptFit(0);
 gStyle->SetStatFont(42);
 gStyle->SetPadLeftMargin(0.13);
 gStyle->SetPadRightMargin(0.07);
//    gStyle->SetTitleFont(42);
//    gStyle->SetTitleFont(42, "XYZ");
//    gStyle->SetLabelFont(42, "XYZ");
 gStyle->SetStatY(.9);
}

void setTDRStyle() {
  TStyle *tdrStyle = new TStyle("tdrStyle","Style for P-TDR");

  // For the canvas:
  tdrStyle->SetCanvasBorderMode(0);
  tdrStyle->SetCanvasColor(kWhite);
  tdrStyle->SetCanvasDefH(600); //Height of canvas
  tdrStyle->SetCanvasDefW(600); //Width of canvas
  tdrStyle->SetCanvasDefX(0);   //POsition on screen
  tdrStyle->SetCanvasDefY(0);

  // For the Pad:
  tdrStyle->SetPadBorderMode(0);
  // tdrStyle->SetPadBorderSize(Width_t size = 1);
  tdrStyle->SetPadColor(kWhite);
  tdrStyle->SetPadGridX(false);
  tdrStyle->SetPadGridY(false);
  tdrStyle->SetGridColor(0);
  tdrStyle->SetGridStyle(3);
  tdrStyle->SetGridWidth(1);

  // For the frame:
  tdrStyle->SetFrameBorderMode(0);
  tdrStyle->SetFrameBorderSize(1);
  tdrStyle->SetFrameFillColor(0);
  tdrStyle->SetFrameFillStyle(0);
  tdrStyle->SetFrameLineColor(1);
  tdrStyle->SetFrameLineStyle(1);
  tdrStyle->SetFrameLineWidth(1);

  // For the histo:
  tdrStyle->SetHistFillColor(63);
  // tdrStyle->SetHistFillStyle(0);
  tdrStyle->SetHistLineColor(1);
  tdrStyle->SetHistLineStyle(0);
  tdrStyle->SetHistLineWidth(1);
  // tdrStyle->SetLegoInnerR(Float_t rad = 0.5);
  // tdrStyle->SetNumberContours(Int_t number = 20);

//  tdrStyle->SetEndErrorSize(0);
//   tdrStyle->SetErrorX(0.);
//  tdrStyle->SetErrorMarker(20);

  tdrStyle->SetMarkerStyle(20);

  //For the fit/function:
  tdrStyle->SetOptFit(1);
  tdrStyle->SetFitFormat("5.4g");
  tdrStyle->SetFuncColor(2);
  tdrStyle->SetFuncStyle(1);
  tdrStyle->SetFuncWidth(1);

  //For the date:
  tdrStyle->SetOptDate(0);
  // tdrStyle->SetDateX(Float_t x = 0.01);
  // tdrStyle->SetDateY(Float_t y = 0.01);

  // For the statistics box:
  tdrStyle->SetOptFile(0);
  tdrStyle->SetOptStat(0); // To display the mean and RMS:   SetOptStat("mr");
  tdrStyle->SetStatColor(kWhite);
  tdrStyle->SetStatFont(42);
  tdrStyle->SetStatFontSize(0.025);
  tdrStyle->SetStatTextColor(1);
  tdrStyle->SetStatFormat("6.4g");
  tdrStyle->SetStatBorderSize(1);
  tdrStyle->SetStatH(0.1);
  tdrStyle->SetStatW(0.15);
  // tdrStyle->SetStatStyle(Style_t style = 1001);
  // tdrStyle->SetStatX(Float_t x = 0);
  // tdrStyle->SetStatY(Float_t y = 0);

  // Margins:
  tdrStyle->SetPadTopMargin(0.05);
  tdrStyle->SetPadBottomMargin(0.13);
  tdrStyle->SetPadLeftMargin(0.13);
  tdrStyle->SetPadRightMargin(0.05);

  // For the Global title:

  //  tdrStyle->SetOptTitle(0);
  tdrStyle->SetTitleFont(42);
  tdrStyle->SetTitleColor(1);
  tdrStyle->SetTitleTextColor(1);
  tdrStyle->SetTitleFillColor(10);
  tdrStyle->SetTitleFontSize(0.05);
  // tdrStyle->SetTitleH(0); // Set the height of the title box
  // tdrStyle->SetTitleW(0); // Set the width of the title box
  // tdrStyle->SetTitleX(0); // Set the position of the title box
  // tdrStyle->SetTitleY(0.985); // Set the position of the title box
  // tdrStyle->SetTitleStyle(Style_t style = 1001);
  // tdrStyle->SetTitleBorderSize(2);

  // For the axis titles:

  tdrStyle->SetTitleColor(1, "XYZ");
  tdrStyle->SetTitleFont(42, "XYZ");
  tdrStyle->SetTitleSize(0.06, "XYZ");
  // tdrStyle->SetTitleXSize(Float_t size = 0.02); // Another way to set the size?
  // tdrStyle->SetTitleYSize(Float_t size = 0.02);
  tdrStyle->SetTitleXOffset(0.9);
  tdrStyle->SetTitleYOffset(1.05);
  // tdrStyle->SetTitleOffset(1.1, "Y"); // Another way to set the Offset

  // For the axis labels:

  tdrStyle->SetLabelColor(1, "XYZ");
  tdrStyle->SetLabelFont(42, "XYZ");
  tdrStyle->SetLabelOffset(0.007, "XYZ");
  tdrStyle->SetLabelSize(0.05, "XYZ");

  // For the axis:

  tdrStyle->SetAxisColor(1, "XYZ");
  tdrStyle->SetStripDecimals(kTRUE);
  tdrStyle->SetTickLength(0.03, "XYZ");
  tdrStyle->SetNdivisions(510, "XYZ");
  tdrStyle->SetPadTickX(1);  // To get tick marks on the opposite side of the frame
  tdrStyle->SetPadTickY(1);

  // Change for log plots:
  tdrStyle->SetOptLogx(0);
  tdrStyle->SetOptLogy(0);
  tdrStyle->SetOptLogz(0);

  // Postscript options:
  // tdrStyle->SetPaperSize(15.,15.);
  // tdrStyle->SetLineScalePS(Float_t scale = 3);
  // tdrStyle->SetLineStyleString(Int_t i, const char* text);
  // tdrStyle->SetHeaderPS(const char* header);
  // tdrStyle->SetTitlePS(const char* pstitle);

  // tdrStyle->SetBarOffset(Float_t baroff = 0.5);
  // tdrStyle->SetBarWidth(Float_t barwidth = 0.5);
  // tdrStyle->SetPaintTextFormat(const char* format = "g");
  // tdrStyle->SetPalette(Int_t ncolors = 0, Int_t* colors = 0);
  // tdrStyle->SetTimeOffset(Double_t toffset);
  // tdrStyle->SetHistMinimumZero(kTRUE);

  tdrStyle->cd();
}

void makePlots()
{
 // **********************************************
 // *            Input parameters                *
 // **********************************************

 // array of LQ masses for calculation of upXS
 Double_t mData[4] = {150,200,250,300};
 // arrays of upper limits on the cross section
 @Double_t xsUp_expected[4] = {35.3837,24.8965,20.8915,18.7746};
 @Double_t xsUp_observed[4] = {27.9785,20.5078,17.7734,16.2817};

 // arrays of LQ masses for theoretical cross section
 Double_t mTh[9] = {100, 150, 200, 250, 300, 350, 400,450,500};
 // array of theoretical cross-sections for different leptoquark masses
 Double_t xsTh[9] = {386, 53.3, 11.9, 3.47, 1.21, 0.477, .205,.0949,.0463};
 // arays of upper and lower bounds with PDF and scale uncertainties included
 //Double_t xsTh_upper[6] = {445.5, 61.4, 13.7, 4.1, 1.43, 0.57}; // upper bounds with PDF and scale uncertainties included
 //Double_t xsTh_lower[6] = {330.3, 45.2, 10.0, 2.9, 0.98, 0.38}; // lower bounds with PDF and scale uncertainties included


 Double_t xsTh_upper[9]  = {445.5	,	61.4	,	13.7	,	4.1	,	1.43	, 0.57	,	.25	, .1167	 ,	.058 };
 Double_t xsTh_lower[9] = {330.3, 45.2, 10.0, 2.9, 0.98,	0.38	, .16	,	.072,	.034	};


 // filename for the final plot (NB: changing the name extension changes the file format)
 string fileName = "BetaPlot.eps";
 string fileName2 = "BetaPlot.pdf";
 string fileName3 = "BetaPlot.png";

 // axes labels for the final plot
 string title = ";M_{LQ} (GeV);#beta"; 

  // integrated luminosity
 string lint = "#intLdt=IntLumiValue pb^{-1}";

 // number of points used for beta vs m line
 Int_t nPts = 100;
 // range of LQ masses in which beta vs m line is derived
 Double_t mass_range[2] = {200, 500};

 // region excluded by Tevatron limits (1 fb-1)
 //Double_t x_excl[13] = {100,214.39,235.13,254.08,268.12,275.92,283.95,289.08,293.09,295.99,297.10,298.89,100};
 //Double_t y_excl[13] = {0,0,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1,1};

 Double_t x_excl[12] = {100, 152, 170, 200 ,230, 241, 252, 271, 286, 302, 316, 100 };
 Double_t y_excl[12] = {0.0, .05, .07, .13  ,.21, .27, .35, .52, .67, .82, 1.0, 1   };

 // turn on/off batch mode
 gROOT->SetBatch(kTRUE);
 // set ROOT style
//  myStyle();
 setTDRStyle();
//  gStyle->SetPadLeftMargin(0.14);
 gROOT->ForceStyle();

 TH2F *bg = new TH2F("bg",title.c_str(), 20, 200., 500., 100, 0., 1.);
 bg->SetStats(kFALSE);
 bg->SetTitleOffset(1.,"X");
 bg->SetTitleOffset(1.05,"Y");
 bg->GetXaxis()->SetNdivisions(505);

 TCanvas *c = new TCanvas("c","",800,800);
 c->cd();

 Int_t size_th = sizeof(xsTh)/sizeof(*xsTh);

 Double_t xsTh_log[size_th];
 Double_t xsTh_upper_log[size_th];
 Double_t xsTh_lower_log[size_th];
 
 for(Int_t i=0; i<size_th; i++) {
   xsTh_log[i] = log(xsTh[i]);
   xsTh_upper_log[i] = log(xsTh_upper[i]);
   xsTh_lower_log[i] = log(xsTh_lower[i]);
 }

 TGraph *xsTh_vs_m_log = new TGraph(size_th, mTh, xsTh_log);
 TGraph *xsTh_upper_vs_m_log = new TGraph(size_th, mTh, xsTh_upper_log);
 TGraph *xsTh_lower_vs_m_log = new TGraph(size_th, mTh, xsTh_lower_log);

 TSpline3 gs_xsTh_vs_m("gs_xsTh_vs_m", xsTh_vs_m_log);
 TSpline3 gs_xsTh_upper_vs_m("gs_xsTh_vs_m", xsTh_upper_vs_m_log);
 TSpline3 gs_xsTh_lower_vs_m("gs_xsTh_vs_m", xsTh_lower_vs_m_log);

 Int_t size_Data = sizeof(xsUp_expected)/sizeof(*xsUp_expected);

 Double_t xsUp_expected_log[size_Data];
 Double_t xsUp_observed_log[size_Data];

 for(Int_t i=0; i<size_Data; i++) {
   xsUp_expected_log[i] = log(xsUp_expected[i]);
   xsUp_observed_log[i] = log(xsUp_observed[i]);
 }

 TGraph *xsUp_expected_vs_m_log = new TGraph(size_Data, mData, xsUp_expected_log);
 TGraph *xsUp_observed_vs_m_log = new TGraph(size_Data, mData, xsUp_observed_log);

 TSpline3 gs_xsUp_expected_vs_m("gs_xsTh_vs_m", xsUp_expected_vs_m_log);
 TSpline3 gs_xsUp_observed_vs_m("gs_xsTh_vs_m", xsUp_observed_vs_m_log);
 
 /*******************************************
 ****         Debugging section          ****
 *******************************************/
 
//  Double_t mTh_int[11];
//  Double_t xsTh_int[11];
//  Double_t xsTh_upper_int[11];
//  Double_t xsTh_lower_int[11];
// 
//  Double_t step_th = (mTh[size_th-1]-mTh[0])/10;
// 
//  for(Int_t i=0; i<11; i++) {
//    mTh_int[i] = mTh[0]+step_th*i;
//    xsTh_int[i] = exp(gs_xsTh_vs_m.Eval(mTh_int[i]));
//    xsTh_upper_int[i] = exp(gs_xsTh_upper_vs_m.Eval(mTh_int[i]));
//    xsTh_lower_int[i] = exp(gs_xsTh_lower_vs_m.Eval(mTh_int[i]));
//  }
// 
//  TGraph *xsTh_vs_m = new TGraph(size_th, mTh, xsTh);
//  xsTh_vs_m->SetLineWidth(2);
//  xsTh_vs_m->SetLineColor(kBlack);
//  xsTh_vs_m->Draw("AC");
// 
//  TGraph *xsTh_vs_m_int = new TGraph(11, mTh_int, xsTh_int);
//  xsTh_vs_m_int->SetMarkerSize(1.);
//  xsTh_vs_m_int->SetMarkerStyle(24);
//  xsTh_vs_m_int->SetMarkerColor(kBlue);
//  xsTh_vs_m_int->Draw("P");
// 
//  c->SetGridx();
//  c->SetGridy();
//  c->SetLogy();
//  c->SaveAs("xsTh_vs_m.png");
// 
//  TGraph *xsTh_upper_vs_m = new TGraph(size_th, mTh, xsTh_upper);
//  xsTh_upper_vs_m->SetLineWidth(2);
//  xsTh_upper_vs_m->SetLineColor(kBlack);
//  xsTh_upper_vs_m->Draw("AC");
// 
//  TGraph *xsTh_upper_vs_m_int = new TGraph(11, mTh_int, xsTh_upper_int);
//  xsTh_upper_vs_m_int->SetMarkerSize(1.);
//  xsTh_upper_vs_m_int->SetMarkerStyle(24);
//  xsTh_upper_vs_m_int->SetMarkerColor(kBlue);
//  xsTh_upper_vs_m_int->Draw("P");
// 
//  c->SetGridx();
//  c->SetGridy();
//  c->SetLogy();
//  c->SaveAs("xsTh_upper_vs_m.png");
// 
//  TGraph *xsTh_lower_vs_m = new TGraph(size_th, mTh, xsTh_lower);
//  xsTh_lower_vs_m->SetLineWidth(2);
//  xsTh_lower_vs_m->SetLineColor(kBlack);
//  xsTh_lower_vs_m->Draw("AC");
// 
//  TGraph *xsTh_lower_vs_m_int = new TGraph(11, mTh_int, xsTh_lower_int);
//  xsTh_lower_vs_m_int->SetMarkerSize(1.);
//  xsTh_lower_vs_m_int->SetMarkerStyle(24);
//  xsTh_lower_vs_m_int->SetMarkerColor(kBlue);
//  xsTh_lower_vs_m_int->Draw("P");
// 
//  c->SetGridx();
//  c->SetGridy();
//  c->SetLogy();
//  c->SaveAs("xsTh_lower_vs_m.png");
// 
//  Double_t mData_int[11];
//  Double_t xsUp_expected_int[11];
//  Double_t xsUp_observed_int[11];
// 
//  Double_t step_Data = (mData[size_Data-1]-mData[0])/10;
// 
//  for(Int_t i=0; i<11; i++) {
//    mData_int[i] = mData[0]+step_Data*i;
//    xsUp_expected_int[i] = exp(gs_xsUp_expected_vs_m.Eval(mData_int[i]));
//    xsUp_observed_int[i] = exp(gs_xsUp_observed_vs_m.Eval(mData_int[i]));
//  }
// 
//  TGraph *xsUp_expected_vs_m = new TGraph(size_Data, mData, xsUp_expected);
//  xsUp_expected_vs_m->SetLineWidth(2);
//  xsUp_expected_vs_m->SetLineColor(kBlack);
//  xsUp_expected_vs_m->Draw("AC");
// 
//  TGraph *xsUp_expected_vs_m_int = new TGraph(11, mData_int, xsUp_expected_int);
//  xsUp_expected_vs_m_int->SetMarkerSize(1.);
//  xsUp_expected_vs_m_int->SetMarkerStyle(24);
//  xsUp_expected_vs_m_int->SetMarkerColor(kBlue);
//  xsUp_expected_vs_m_int->Draw("P");
// 
//  c->SetGridx();
//  c->SetGridy();
//  c->SetLogy();
//  c->SaveAs("xsUp_expected_vs_m.png");
// 
//  TGraph *xsUp_observed_vs_m = new TGraph(size_Data, mData, xsUp_observed);
//  xsUp_observed_vs_m->SetLineWidth(2);
//  xsUp_observed_vs_m->SetLineColor(kBlack);
//  xsUp_observed_vs_m->Draw("AC");
// 
//  TGraph *xsUp_observed_vs_m_int = new TGraph(11, mData_int, xsUp_observed_int);
//  xsUp_observed_vs_m_int->SetMarkerSize(1.);
//  xsUp_observed_vs_m_int->SetMarkerStyle(24);
//  xsUp_observed_vs_m_int->SetMarkerColor(kBlue);
//  xsUp_observed_vs_m_int->Draw("P");
// 
//  c->SetGridx();
//  c->SetGridy();
//  c->SetLogy();
//  c->SaveAs("xsUp_observed_vs_m.png");
// 
//  delete xsTh_vs_m;
//  delete xsTh_vs_m_int;
//  delete xsTh_upper_vs_m;
//  delete xsTh_upper_vs_m_int;
//  delete xsTh_lower_vs_m;
//  delete xsTh_lower_vs_m_int;
//  delete xsUp_expected_vs_m_int;
//  delete xsUp_observed_vs_m_int;
 
 /*******************************************
 ****       End of debugging section     ****
 *******************************************/

 bg->Draw();

 TGraph *gr_excl = new TGraph(12,x_excl,y_excl);
 gr_excl->SetLineColor(0);
 gr_excl->SetFillColor(kGray);
 gr_excl->Draw("f");

 Double_t step = (mass_range[1]-mass_range[0])/(nPts-1);
 Double_t m[nPts], beta_expected[nPts], beta_observed[nPts], beta_observed_upper[nPts], beta_observed_lower[nPts];

 for(Int_t i=0; i<nPts; i++) {
   m[i] = mass_range[0]+step*i;
   beta_expected[i] = sqrt(exp(gs_xsUp_expected_vs_m.Eval(m[i]))/exp(gs_xsTh_vs_m.Eval(m[i])));
   beta_observed[i] = sqrt(exp(gs_xsUp_observed_vs_m.Eval(m[i]))/exp(gs_xsTh_vs_m.Eval(m[i])));
   beta_observed_lower[i] = sqrt(exp(gs_xsUp_observed_vs_m.Eval(m[i]))/exp(gs_xsTh_upper_vs_m.Eval(m[i])));
   beta_observed_upper[i] = sqrt(exp(gs_xsUp_observed_vs_m.Eval(m[i]))/exp(gs_xsTh_lower_vs_m.Eval(m[i])));
 }

 TGraph *beta_observed_vs_m_band = new TGraph(2*nPts);
 for(Int_t i=0;i<nPts;i++) {
   beta_observed_vs_m_band->SetPoint(i,m[i],beta_observed_lower[i]);
   beta_observed_vs_m_band->SetPoint(nPts+i,m[nPts-i-1],beta_observed_upper[nPts-i-1]);
 }
 beta_observed_vs_m_band->SetLineColor(0);
 beta_observed_vs_m_band->SetFillColor(kGreen);
 beta_observed_vs_m_band->Draw("f");

 TGraph *beta_expected_vs_m = new TGraph(nPts, m, beta_expected);
 beta_expected_vs_m->SetLineWidth(2);
 beta_expected_vs_m->SetLineStyle(2);
 beta_expected_vs_m->SetLineColor(kBlue);
 beta_expected_vs_m->Draw("C");

 TGraph *beta_observed_vs_m = new TGraph(nPts, m, beta_observed);
 beta_observed_vs_m->SetLineWidth(2);
 beta_observed_vs_m->SetLineColor(kBlack);
 beta_observed_vs_m->SetFillColor(kGreen);
 beta_observed_vs_m->Draw("C");

 gPad->RedrawAxis();

 TLegend *legend = new TLegend(.56,.22,.92,.39);
 legend->SetBorderSize(1);
 legend->SetFillColor(0);
 //legend->SetFillStyle(0);
 legend->SetTextFont(42);
 legend->SetMargin(0.15);
 legend->SetHeader("LQ #rightarrow #mu q");
 legend->AddEntry(gr_excl,"D#oslash exclusion (1 fb^{-1})","f");
 legend->AddEntry(beta_expected_vs_m,"Expected 95% C.L. limit","l");
 legend->AddEntry(beta_observed_vs_m,"Observed 95% C.L. limit","lf");
 legend->Draw();

 TLatex l1;
 l1.SetNDC();
 l1.SetTextAlign(13);
 l1.SetTextSize(0.04);
 l1.SetTextFont(42);

 l1.DrawLatex(0.18,0.85,"CMS");
 l1.DrawLatex(0.18,0.78,lint.c_str());

 c->SetGridx();
 c->SetGridy();
 c->SaveAs(fileName.c_str());
 c->SaveAs(fileName2.c_str());
 c->SaveAs(fileName3.c_str());

 delete legend;
 delete beta_observed_vs_m;
 delete beta_expected_vs_m;
 delete beta_observed_vs_m_band;
 delete gr_excl;
 delete xsTh_vs_m_log;
 delete xsTh_upper_vs_m_log;
 delete xsTh_lower_vs_m_log;
 delete xsUp_expected_vs_m_log;
 delete xsUp_observed_vs_m_log;
 delete bg;
 delete c;
}
