#include "TROOT.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TH2F.h"
#include "TGraph.h"
#include "TF1.h"
#include "TLegend.h"
#include "TPolyLine.h"
#include "TPad.h"
#include "TLatex.h"

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
 gStyle->SetOptFit(1);
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

void makePlotsBH()
{
 // **********************************************
 // *            Input parameters                *
 // **********************************************
 // switch to include/exclude sytematics uncertainties
 bool systematics = true; // does nothing at the moment

 // total integrated luminosity (in pb-1)
 Double_t L_int = 4700;
 // relative uncertainty on the integrated luminosity (0.1 = 10% uncertainty)
 Double_t Sigma_L_int = 0.11;

 // array of signal efficiencies
 Double_t S_eff[4] = {.3353,.4574,.5276,.5763};
 // array of relative uncertainties on the signal efficiencies
 Double_t Sigma_S_eff[4] = {0.21, 0.21, 0.21,.21};

 // array of N_background for L_int
 Double_t N_bkg[4] = {.2724,.1786,.1098,.0753};
 // array of relative uncertainties on N_background (0.1 = 10%)
 Double_t Sigma_N_bkg[4] = {0.88, 0.88, 0.88, 0.88};

 // array of N_observed for L_int
 Double_t N_obs[4] = {0, 0, 0, 0};

 // array of LQ masses for calculation of upXS
Double_t mData[10] = {250, 350, 400, 450, 500, 550, 600, 650, 750, 850};
 // arrays of LQ masses for theoretical cross section
 //Double_t mTh[9] = {100, 150, 200, 250, 300, 350, 400,450,500};
 Double_t mTh[15] = { 150, 200, 250, 300, 350, 400,450,500,550,600,650,700,750,800,850};
 // array of theoretical cross-sections for different leptoquark masses
 //Double_t xsTh[9] = {386/2.0, 53.3/2.0, 11.9/2.0, 3.47/2.0, 1.21/2.0, 0.477/2.0, .205/2.0,.0949/2.0,.0463/2.0};
 Double_t xsTh[15] = { 53.3/2.0, 11.9/2.0, 3.47/2.0, 1.21/2.0, 0.477/2.0, .205/2.0,.0949/2.0,.0463/2.0,.0236/2.0,.0124/2.0,.00676/2.0,.00377/2.0,.00215/2.0,.00124/2.0,.000732/2.0};
  
 // filename for the final plot (NB: changing the name extension changes the file format)
 string fileName2 = "BR_Sigma_MuNu.pdf";
 string fileName3 = "BR_Sigma_MuNu.png";
 string fileName1 = "BR_Sigma_MuNu.eps";
  
 // axes labels for the final plot
 string title = ";M_{LQ} (GeV);2#beta(1-#beta)#times#sigma (pb)";

 // integrated luminosity
 string lint = "4.7 fb^{-1}";

 // region excluded by Tevatron limits
 Double_t x_shaded[5] = {250,362,362,250,250};// CHANGED FOR LQ2
 Double_t y_shaded[5] = {0.0001,0.0001,50,50,0.0001};// CHANGED FOR LQ2


 Double_t x_pdf[28] = {	150		,	200		,	250	,	300		,	350		,	400	,  450 	 ,  500, 600,	650,	700,	750,	800,	850,	850,	800,	750,	700,	650,	600  , 500  , 450 	,	400	,	350		,	300		,	250	, 200		, 150		};
 Double_t y_pdf[28] = {	61.4	/2.0,	13.7	/2.0,	4.1	/2.0,	1.43	/2.0, 0.57	/2.0,	.25	/2.0, .1167	 /2.0,	.058/2.0,0.01561/2.0,	0.00866/2.0,	0.00491/2.0,	0.00284/2.0,	0.001677/2.0,	0.001008/2.0,	0.000456/2.0,	0.000803/2.0,	0.00144/2.0,	0.00263/2.0,	0.00486/2.0,	0.00919 /2.0, .034	/2.0,	.072	/2.0, .16	/2.0,	0.38	/2.0, 0.98	/2.0, 2.9	/2.0, 10.0	/2.0, 45.2	/2.0};
 
Double_t x_shademasses[20]={250, 350, 400, 450, 500, 550, 600, 650, 750, 850, 850, 750, 650, 600, 550, 500, 450, 400, 350, 250};

  

//////////// ASYMPTOTIC /////////////////

Double_t xsUp_expected[10] = {0.1434845 , 0.03823155 , 0.0215455 , 0.01336192 , 0.009586415 , 0.0063543 , 0.00493272 , 0.00401882 , 0.003217045 , 0.0028029378 }; 


Double_t xsUp_observed[10] = {0.1368915 , 0.0289539 , 0.014268 , 0.009466275 , 0.006984355 , 0.00752368 , 0.00459048 , 0.003951558 , 0.0038120575 , 0.0035486994 }; 


Double_t y_1sigma[20]={0.1035795 , 0.02759445 , 0.01554925 , 0.00964184 , 0.00691722 , 0.00458548 , 0.00356004 , 0.00290004 , 0.0023216775 , 0.0020228088 , 0.0038932884 , 0.0044684525 , 0.00558207 , 0.00685162 , 0.0088264 , 0.01331588 , 0.018557695 , 0.02993 , 0.05311395 , 0.199178 }; 


Double_t y_2sigma[20]={0.0779015 , 0.0207495 , 0.01169525 , 0.00725036 , 0.005201805 , 0.00344796 , 0.00267654 , 0.002180438 , 0.00174537 , 0.00152073 , 0.0051727512 , 0.0059369025 , 0.007416396 , 0.00910346 , 0.01172684 , 0.01769123 , 0.02465502 , 0.03975975 , 0.07057215 , 0.264761 }; 





////////////  FULL CLS  /////////////////

  

//Double_t xsUp_expected[10] = {0.3165334 , 0.059536755 , 0.03237975 , 0.019297915 , 0.0128829287 , 0.0080891714 , 0.006322698 , 0.0053530412 , 0.00442430225 , 0.0037808532 }; 


//Double_t xsUp_observed[10] = {0.3323566 , 0.059536755 , 0.027971225 , 0.01767545715 , 0.01061355735 , 0.0079504624 , 0.0058610336 , 0.0064787164 , 0.0056629495 , 0.0053919852 }; 


//Double_t y_1sigma[20]={0.24801825 , 0.04442778 , 0.024162325 , 0.015120417 , 0.0100352935 , 0.0059720744 , 0.0046267128 , 0.0040133106 , 0.00334538925 , 0.00283745892 , 0.0052764756 , 0.00622165925 , 0.0075395632 , 0.008942384 , 0.0116223274 , 0.0177623005 , 0.0258607245 , 0.045562275 , 0.07978302 , 0.40399475 }; 


//Double_t y_2sigma[20]={0.1522636 , 0.036550125 , 0.01987885 , 0.011847316 , 0.0071747406 , 0.0042791166 , 0.0035134904 , 0.00320833994 , 0.002698637 , 0.00248859138 , 0.0070422426 , 0.0085735335 , 0.0103770056 , 0.012493434 , 0.015822856 , 0.023259268 , 0.03475489485 , 0.058149275 , 0.101827575 , 0.5413894 }; 




 //// **********************************************
 // *  Don't change anything below this point!   *
 // **********************************************




  // turn on/off batch mode
 gROOT->SetBatch(kTRUE);

 Int_t size = sizeof(S_eff)/sizeof(*S_eff);


////// MEDIAN



 // set ROOT style
//  myStyle();
 setTDRStyle();
 gStyle->SetPadLeftMargin(0.14);
 gROOT->ForceStyle();
 
 TCanvas *c = new TCanvas("c","",800,800);
 c->cd();
 
 TH2F *bg = new TH2F("bg",title.c_str(), 500, 250., 850., 500., 0.0001, 50.);
 bg->SetStats(kFALSE);
 bg->SetTitleOffset(1.,"X");
 bg->SetTitleOffset(1.15,"Y");
 
 bg->Draw();

 TPolyLine *pl = new TPolyLine(5,x_shaded,y_shaded,"F");
//  pl->SetFillStyle(3001);
 pl->SetLineColor(0);
 pl->SetFillColor(kGray);
 pl->SetLineColor(kGray);   // CHANGED FOR LQ2
 pl->Draw();

 TGraph *exshade1 = new TGraph(20,x_shademasses,y_1sigma);
 exshade1->SetFillColor(kGreen);
 TGraph *exshade2 = new TGraph(20,x_shademasses,y_2sigma);
 exshade2->SetFillColor(kYellow);

 exshade2->Draw("f");
 exshade1->Draw("f");

 gPad->RedrawAxis();


 TGraph *grshade = new TGraph(29,x_pdf,y_pdf);
 grshade->SetFillColor(kCyan-6);
 grshade->SetFillStyle(3001);
 grshade->Draw("f");



 // set ROOT style
//  myStyle();
 setTDRStyle();
 gStyle->SetPadLeftMargin(0.14);
 gROOT->ForceStyle();

 TGraph *xsTh_vs_m = new TGraph(15, mTh, xsTh);
 xsTh_vs_m->SetLineWidth(2);
 xsTh_vs_m->SetLineColor(kBlue);
 xsTh_vs_m->SetFillColor(kCyan-6);
 xsTh_vs_m->SetMarkerSize(0.00001);
 xsTh_vs_m->SetMarkerStyle(22);
 grshade->SetFillStyle(1001); 
 xsTh_vs_m->SetMarkerColor(kBlue);
 xsTh_vs_m->Draw("C");

 TGraph *xsData_vs_m_expected = new TGraph(10, mData, xsUp_expected);
 xsData_vs_m_expected->SetMarkerStyle(0);
 xsData_vs_m_expected->SetMarkerColor(kBlack);
 xsData_vs_m_expected->SetLineColor(kBlack);
 xsData_vs_m_expected->SetLineWidth(2);
 xsData_vs_m_expected->SetLineStyle(7);
 xsData_vs_m_expected->SetMarkerSize(0.001);
 xsData_vs_m_expected->Draw("CP");

 TGraph *xsData_vs_m_observed = new TGraph(10, mData, xsUp_observed);
 xsData_vs_m_observed->SetMarkerStyle(21);
 xsData_vs_m_observed->SetMarkerColor(kBlack);
 xsData_vs_m_observed->SetLineColor(kBlack);
 xsData_vs_m_observed->SetLineWidth(2);
 xsData_vs_m_observed->SetLineStyle(1);
 xsData_vs_m_observed->SetMarkerSize(1);
 xsData_vs_m_observed->Draw("CP");
 
 float mtest = 250.0;
 float xrat = 0.0;
 float orat = 0.0;
 while (mtest<850){
	 xrat = xsData_vs_m_expected->Eval(mtest)/xsTh_vs_m->Eval(mtest);
	 orat = xsData_vs_m_observed->Eval(mtest)/xsTh_vs_m->Eval(mtest);
	 std::cout<<mtest<<"   "<<xrat<<"    "<<orat<<"   "<<"   "<<xsData_vs_m_observed->Eval(mtest)<<"   "<<xsTh_vs_m->Eval(mtest)<<std::endl;
	 mtest = mtest + 1.0;

	}
 
 TLegend *legend = new TLegend(.37,.65,.94,.92);
 legend->SetBorderSize(1);
 legend->SetFillColor(0);
 //legend->SetFillStyle(0);
 legend->SetTextFont(42);
 legend->SetMargin(0.15);
 legend->SetHeader("LQ #bar{LQ} #rightarrow #mu q #nu q");
 legend->AddEntry(pl,"ATLAS exclusion (35 pb^{-1}, #beta=1/2)","f");
 legend->AddEntry(xsTh_vs_m,"2#beta(1-#beta)#times #sigma_{theory} with theory unc., (#beta=1/2)","lf");
 legend->AddEntry(xsData_vs_m_expected, "Expected 95% C.L. upper limit","lp");
 legend->AddEntry(xsData_vs_m_observed, "Observed 95% C.L. upper limit","lp");
 legend->Draw();

 TLatex l1;
 l1.SetTextAlign(12);
 l1.SetTextSize(0.045);
 l1.SetTextFont(42);
 l1.SetNDC();
 l1.DrawLatex(0.52,0.6,"CMS Preliminary");
 l1.DrawLatex(0.52,0.54,lint.c_str());

//  TLatex l2;
//  l2.SetTextAlign(12);
//  l2.SetTextSize(0.037);
//  l2.SetTextFont(42);
//  l2.SetNDC();
//  l2.DrawLatex(0.4,0.485,"EXO-10-005 scaled to #sqrt{s} = 7 TeV");

 c->SetGridx();
 c->SetGridy();


 c->SetLogy();
 c->SaveAs((fileName1).c_str());
 c->SaveAs((fileName2).c_str());
 c->SaveAs((fileName3).c_str());

 delete pl;
 delete xsTh_vs_m;
 delete bg;
 delete c;
}

