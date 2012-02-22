#include "TROOT.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TH2F.h"
#include "TGraph.h"
#include "TPolyLine.h"
#include "TF1.h"
#include "TLegend.h"
#include "TPad.h"
#include "TLatex.h"
#include "TSpline.h"
#include "TFile.h"

using namespace std;

void myStyle();
void setTDRStyle();

void makePlots()
{
 // **********************************************
 // *            Input parameters                *
 // **********************************************

 // eejj limits
 Double_t m_eejj[50] = {200, 204.082, 208.163, 212.245, 216.327, 220.408, 224.49, 228.571, 232.653, 236.735, 240.816, 244.898, 248.98, 253.061, 257.143, 261.224, 265.306, 269.388, 273.469, 277.551, 281.633, 285.714, 289.796, 293.878, 297.959, 302.041, 306.122, 310.204, 314.286, 318.367, 322.449, 326.531, 330.612, 334.694, 338.776, 342.857, 346.939, 351.02, 355.102, 359.184, 363.265, 367.347, 371.429, 375.51, 379.592, 383.673, 387.755, 391.837, 395.918, 400};
 Double_t beta_eejj_observed[50] = {0.192489, 0.19659, 0.201503, 0.207225, 0.213753, 0.22109, 0.229236, 0.238191, 0.247955, 0.258521, 0.269878, 0.282008, 0.294884, 0.308466, 0.322705, 0.337534, 0.352872, 0.36862, 0.384659, 0.400849, 0.417033, 0.433163, 0.449359, 0.465779, 0.482607, 0.50005, 0.518231, 0.537171, 0.556886, 0.577391, 0.598696, 0.620759, 0.643492, 0.666788, 0.690524, 0.714573, 0.738955, 0.763793, 0.78923, 0.815419, 0.842533, 0.870765, 0.900329, 0.931232, 0.963129, 0.99559, 1.02813, 1.06019, 1.09116, 1.12037};
 Double_t beta_eejj_expected[50] = {0.245939, 0.253519, 0.261428, 0.269668, 0.278244, 0.287156, 0.296408, 0.306, 0.315931, 0.326199, 0.336802, 0.347735, 0.35899, 0.370562, 0.382438, 0.394609, 0.40706, 0.419774, 0.432735, 0.445919, 0.459306, 0.472926, 0.486888, 0.501318, 0.516357, 0.532157, 0.548729, 0.565929, 0.583583, 0.601491, 0.619447, 0.637443, 0.655653, 0.674277, 0.693538, 0.713666, 0.734725, 0.75667, 0.779442, 0.802968, 0.827162, 0.851925, 0.877147, 0.902767, 0.928813, 0.955325, 0.98235, 1.00994, 1.03814, 1.06702};
 // enujj limits
 Double_t m_enujj_observed[100] = {200, 202.45, 204.899, 207.349, 209.799, 212.249, 214.698, 217.148, 219.598, 222.048, 224.497, 226.947, 229.397, 231.846, 234.296, 236.746, 239.196, 241.645, 244.095, 246.545, 248.995, 251.444, 253.894, 256.344, 258.794, 261.243, 263.693, 266.143, 268.592, 271.042, 273.492, 275.942, 278.391, 280.841, 283.291, 285.741, 288.19, 290.64, 293.09, 295.539, 297.989, 300.439, 302.889, 305.338, 307.788, 310.238, 312.688, 315.137, 317.587, 320.037, 320.037, 317.587, 315.137, 312.688, 310.238, 307.788, 305.338, 302.889, 300.439, 297.989, 295.539, 293.09, 290.64, 288.19, 285.741, 283.291, 280.841, 278.391, 275.942, 273.492, 271.042, 268.592, 266.143, 263.693, 261.243, 258.794, 256.344, 253.894, 251.444, 248.995, 246.545, 244.095, 241.645, 239.196, 236.746, 234.296, 231.846, 229.397, 226.947, 224.497, 222.048, 219.598, 217.148, 214.698, 212.249, 209.799, 207.349, 204.899, 202.45, 200};
 Double_t beta_enujj_observed[100] = {0.0481969, 0.0466801, 0.0456334, 0.0450041, 0.0447534, 0.0448532, 0.0452845, 0.0460357, 0.0471008, 0.0484792, 0.0501742, 0.0521931, 0.0545457, 0.0572446, 0.060304, 0.0637395, 0.0675669, 0.0718019, 0.0764587, 0.0815493, 0.0870817, 0.0930582, 0.0994741, 0.106315, 0.113555, 0.121152, 0.129047, 0.137159, 0.145385, 0.153593, 0.16162, 0.169277, 0.176345, 0.182585, 0.187918, 0.192562, 0.196808, 0.200998, 0.20552, 0.210813, 0.21739, 0.225876, 0.236873, 0.250666, 0.26762, 0.288323, 0.31378, 0.345964, 0.389992, 0.5, 0.5, 0.610008, 0.654036, 0.68622, 0.711677, 0.73238, 0.749334, 0.763127, 0.774124, 0.78261, 0.789187, 0.79448, 0.799002, 0.803192, 0.807438, 0.812082, 0.817415, 0.823655, 0.830723, 0.83838, 0.846407, 0.854615, 0.862841, 0.870953, 0.878848, 0.886445, 0.893685, 0.900526, 0.906942, 0.912918, 0.918451, 0.923541, 0.928198, 0.932433, 0.936261, 0.939696, 0.942755, 0.945454, 0.947807, 0.949826, 0.951521, 0.952899, 0.953964, 0.954715, 0.955147, 0.955247, 0.954996, 0.954367, 0.95332, 0.951803};
 Double_t m_enujj_expected[100] = {200, 202.451, 204.902, 207.353, 209.804, 212.255, 214.706, 217.157, 219.608, 222.06, 224.511, 226.962, 229.413, 231.864, 234.315, 236.766, 239.217, 241.668, 244.119, 246.57, 249.021, 251.472, 253.923, 256.374, 258.825, 261.277, 263.728, 266.179, 268.63, 271.081, 273.532, 275.983, 278.434, 280.885, 283.336, 285.787, 288.238, 290.689, 293.14, 295.591, 298.042, 300.494, 302.945, 305.396, 307.847, 310.298, 312.749, 315.2, 317.651, 320.102, 320.102, 317.651, 315.2, 312.749, 310.298, 307.847, 305.396, 302.945, 300.494, 298.042, 295.591, 293.14, 290.689, 288.238, 285.787, 283.336, 280.885, 278.434, 275.983, 273.532, 271.081, 268.63, 266.179, 263.728, 261.277, 258.825, 256.374, 253.923, 251.472, 249.021, 246.57, 244.119, 241.668, 239.217, 236.766, 234.315, 231.864, 229.413, 226.962, 224.511, 222.06, 219.608, 217.157, 214.706, 212.255, 209.804, 207.353, 204.902, 202.451, 200};
 Double_t beta_enujj_expected[100] = {0.0609646, 0.0627263, 0.0645734, 0.0665095, 0.0685384, 0.0706638, 0.0728898, 0.0752207, 0.0776611, 0.0802155, 0.082889, 0.0856868, 0.0886142, 0.091677, 0.0948813, 0.0982333, 0.10174, 0.105408, 0.109245, 0.113259, 0.117458, 0.121851, 0.126448, 0.131258, 0.136293, 0.141564, 0.147084, 0.152867, 0.158927, 0.165281, 0.171947, 0.178944, 0.186296, 0.194026, 0.202163, 0.210738, 0.219789, 0.229358, 0.239497, 0.250267, 0.261746, 0.274031, 0.287265, 0.30168, 0.317612, 0.335569, 0.356396, 0.381717, 0.415655, 0.5, 0.5, 0.584345, 0.618283, 0.643604, 0.664431, 0.682388, 0.69832, 0.712735, 0.725969, 0.738254, 0.749733, 0.760503, 0.770642, 0.780211, 0.789262, 0.797837, 0.805974, 0.813704, 0.821056, 0.828053, 0.834719, 0.841073, 0.847133, 0.852916, 0.858436, 0.863707, 0.868742, 0.873552, 0.878149, 0.882542, 0.886741, 0.890755, 0.894592, 0.89826, 0.901767, 0.905119, 0.908323, 0.911386, 0.914313, 0.917111, 0.919784, 0.922339, 0.924779, 0.92711, 0.929336, 0.931462, 0.93349, 0.935427, 0.937274, 0.939035};
 // combined limits
 Double_t beta_comb_observed[22] = {0.050536, 0.06, 0.08, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1};
 Double_t m_comb_observed[22] = {200.000, 233.027, 245.546, 254.27, 271.625, 295.592, 308.938, 316.743, 322.712, 328.038, 333.486, 338.996, 344.965, 352.801, 359.229, 363.545, 367.646, 371.074, 374.197, 376.37, 379.614, 384.083};
 Double_t beta_comb_expected[21] = {0.062088, 0.08, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1};
 Double_t m_comb_expected[21] = {200.000, 220.141, 236.425, 264.034, 283.502, 298.99, 311.723, 322.039, 330.64, 337.833, 344.2, 349.617, 354.484, 358.892, 362.718, 366.636, 370.37, 374.594, 378.727, 383.93, 390.572};
 
 
 // PASTE INFORMATION HERE
//static int numbetas = 2;
//Double_t beta_vals[2] = {0.3, 0.5};


//Double_t m_expected_combo[2] = {564, 640};


//Double_t m_observed_combo[2] = {557, 636};


//Double_t m_1sigma_combo[4]={620, 680, 599, 509};


//Double_t m_2sigma_combo[4]={653, 717, 560, 463};


//Double_t m_expected_lljj[2] = {497, 614};


//Double_t m_observed_lljj[2] = {526, 631};


//Double_t m_1sigma_lljj[4]={540, 651, 580, 453};


//Double_t m_2sigma_lljj[4]={571, 685, 550, 418};


//Double_t m_expected_lvjj[2] = {533, 572};


//Double_t m_observed_lvjj[2] = {519, 540};


//Double_t m_1sigma_lvjj[4]={605, 628, 510, 485};


//Double_t m_2sigma_lvjj[4]={641, 660, 469, 442};

static int numbetas = 10;

Double_t beta_vals[10] = {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99};


Double_t m_expected_combo[10] = {405, 500, 564, 611, 640, 668, 698, 727, 756, 779};
Double_t m_observed_combo[10] = {411, 494, 557, 603, 636, 668, 702, 744, 790, 827};
Double_t m_1sigma_combo[20]={461, 555, 620, 651, 680, 710, 740, 768, 794, 815, 739, 714, 685, 656, 628, 599, 559, 509, 451, 353};
Double_t m_2sigma_combo[20]={502, 613, 653, 686, 717, 747, 775, 801, 825, 844, 703, 678, 650, 623, 595, 560, 517, 463, 407, 293};


Double_t m_expected_lljj[10] = {0, 394, 497, 568, 614, 655, 693, 727, 757, 780};
Double_t m_observed_lljj[10] = {0, 438, 526, 593, 631, 670, 710, 753, 793, 827};
Double_t m_1sigma_lljj[20]={0, 434, 540, 601, 651, 695, 735, 768, 795, 816, 740, 715, 685, 653, 617, 580, 530, 453, 346, 0};
Double_t m_2sigma_lljj[20]={0, 470, 571, 632, 685, 732, 770, 801, 826, 845, 703, 679, 651, 620, 588, 550, 492, 418, 280, 0};


Double_t m_expected_lvjj[10] = {400, 493, 533, 561, 572, 561, 533, 493, 400, 250};
Double_t m_observed_lvjj[10] = {408, 476, 519, 535, 540, 535, 519, 476, 408, 250};
Double_t m_1sigma_lvjj[20]={457, 543, 605, 623, 628, 623, 605, 543, 457, 0, 0, 342, 444, 485, 504, 510, 504, 485, 444, 342};
Double_t m_2sigma_lvjj[20]={498, 607, 641, 656, 660, 656, 641, 607, 498, 0, 0, 0, 393, 442, 463, 469, 463, 442, 393, 0};






// INFORMATION PASTING OVER

Double_t beta_valsdub[numbetas*2];
int ind = numbetas;
for (unsigned int ii = 0; ii < numbetas*2; ++ii){
	if (ii < numbetas) beta_valsdub[ii] = beta_vals[ii];
	else {
		ind = ind -1;
		beta_valsdub[ii] = beta_vals[ind];
	}
}



 // filename for the final plot (NB: changing the name extension changes the file format)
 string fileName0 = "LQ2Combination.eps";
 string fileName1 = "LQ2Combination.pdf";
 string fileName2 = "LQ2Combination.png";


 // axes labels for the final plot
 string title = ";M_{LQ} [GeV];#beta";

 // integrated luminosity
 string sqrts = "#sqrt{s} = 7 TeV";

 // region excluded by Tevatron limits (1 fb-1)
 Double_t x_excl_D0[11] = {214.39,235.13,254.08,268.12,275.92,283.95,289.08,293.09,295.99,297.10,298.89};
 Double_t y_excl_D0[11] = {0,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1};

 // region excluded by ATLAS limits (35 pb-1)
 Double_t x_excl_ATLAS[13] = {200,221.91,243.07,254.12,265.17,287.83,304.68,318.54,331.46,342.88,353.75,363.11,375.47};
 Double_t y_excl_ATLAS[13] = {0.095,0.10,0.126,0.151,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1.0};
 
 // region excluded by Tevatron limits (5.4 fb-1)
 Double_t x_excl_D0_new[11] = {243.13,275.12,308.18,320.02,325.95,327.96,325.95,320.02,308.18,275.12,243.13};
 Double_t y_excl_D0_new[11] = {0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,0.95};

Double_t AtlasComboMass[13] = {250,253.997194950912,278.541374474053,305.539971949509,341.374474053296,352.173913043478,362.973352033661,371.318373071529,385.063113604488,395.371669004208,413.534361851332,421.879382889201,250};
Double_t AtlasComboBeta[13] ={.1,0.12280701754386,0.14619883040936,0.19493177387914,0.34892787524366,0.39766081871345,0.51851851851852,0.60038986354776,0.74269005847953,0.79727095516569,0.93567251461988,0.99805068226121,1.0};

 // turn on/off batch mode
 gROOT->SetBatch(kTRUE);
 // set ROOT style
//  myStyle();
 setTDRStyle();
//  gStyle->SetPadLeftMargin(0.14);
 gROOT->ForceStyle();

 TH2F *bg = new TH2F("bg",title.c_str(), 20, 250., 950., 100, 0., 1.);
 bg->SetStats(kFALSE);
 bg->SetTitleOffset(1.,"X");
 bg->SetTitleOffset(1.05,"Y");
//  bg->GetXaxis()->SetNdivisions(505);

 TCanvas *c = new TCanvas("c","",800,800);
 c->cd();

 bg->Draw();

 TGraph *gr_excl_D0 = new TGraph(11,x_excl_D0,y_excl_D0);
 gr_excl_D0->SetLineWidth(3);
 gr_excl_D0->SetLineColor(49);
 gr_excl_D0->SetLineStyle(6);
 //gr_excl_D0->Draw("C");

 TPolyLine*gr_excl_ATLAS = new TPolyLine(13,AtlasComboMass,AtlasComboBeta,"F");
 //gr_excl_ATLAS->SetLineWidth(3);
 gr_excl_ATLAS->SetLineColor(kBlack);
 gr_excl_ATLAS->SetFillColor(kBlack);
 gr_excl_ATLAS->SetFillStyle(3244);
 gr_excl_ATLAS->Draw();

 TGraph *gr_excl_D0_new = new TGraph(11,x_excl_D0_new,y_excl_D0_new);
 gr_excl_D0_new->SetLineWidth(3);
 gr_excl_D0_new->SetLineColor(30);
 gr_excl_D0_new->SetLineStyle(7);
 //gr_excl_D0_new->Draw("C");


// ------------------------------------ LLJJ CURVES  -------------------------------------//
 TGraph *beta_vs_m_lljj_observed = new TGraph(numbetas, m_observed_lljj, beta_vals);
 TGraph *beta_vs_m_lljj_expected = new TGraph(numbetas, m_expected_lljj, beta_vals);
 //TGraph *beta_vs_m_lljj_observed_shade = new TGraph(numbetas*2, m_2sigma_lljj, beta_valsdub);
 
 beta_vs_m_lljj_observed->SetLineWidth(3);
 beta_vs_m_lljj_observed->SetLineColor(kBlue);
 beta_vs_m_lljj_observed->SetLineStyle(1);

 beta_vs_m_lljj_expected->SetLineWidth(3);
 beta_vs_m_lljj_expected->SetLineColor(kBlue);
 beta_vs_m_lljj_expected->SetLineStyle(2);
 
 
 //beta_vs_m_lljj_observed_shade->SetLineWidth(3);
 //beta_vs_m_lljj_observed_shade->SetLineColor(kGreen+2);
 //beta_vs_m_lljj_observed_shade->SetLineStyle(4);
 //beta_vs_m_lljj_observed_shade->SetFillStyle(3425);
 //beta_vs_m_lljj_observed_shade->SetFillColor(kGreen+2);
 //beta_vs_m_lljj_observed_shade->Draw("f");




// ------------------------------------ LVJJ CURVES  -------------------------------------//

 TPolyLine *beta_vs_m_lvjj_observed = new TPolyLine(numbetas, m_observed_lvjj, beta_vals);
 TPolyLine *beta_vs_m_lvjj_expected = new TPolyLine(numbetas, m_expected_lvjj, beta_vals);
 //TGraph *beta_vs_m_lvjj_observed_shade = new TGraph(numbetas*2, m_2sigma_lvjj, beta_valsdub);
 
 beta_vs_m_lvjj_observed->SetLineWidth(3);
 beta_vs_m_lvjj_observed->SetLineColor(kRed);
 beta_vs_m_lvjj_observed->SetLineStyle(1);
 
 beta_vs_m_lvjj_expected->SetLineWidth(3);
 beta_vs_m_lvjj_expected->SetLineColor(kRed);
 beta_vs_m_lvjj_expected->SetLineStyle(2);
 
 //beta_vs_m_lvjj_observed_shade->SetFillStyle(3452);
 //beta_vs_m_lvjj_observed_shade->SetFillColor(kRed);
 //beta_vs_m_lvjj_observed_shade->Draw("f");




// ------------------------------------ COMBO CURVES  -------------------------------------//

 TGraph *beta_vs_m_comb_observed = new TGraph(numbetas, m_observed_combo, beta_vals);
 TGraph *beta_vs_m_comb_expected = new TGraph(numbetas, m_expected_combo, beta_vals);
 TGraph *beta_vs_m_comb_expected_shade2 = new TGraph(numbetas*2, m_2sigma_combo, beta_valsdub);
 TGraph *beta_vs_m_comb_expected_shade1 = new TGraph(numbetas*2, m_1sigma_combo, beta_valsdub);

 
 beta_vs_m_comb_observed->SetLineWidth(3);
 beta_vs_m_comb_observed->SetLineColor(kBlack);
 beta_vs_m_comb_expected->SetLineStyle(1);

 //beta_vs_m_comb_expected_shade->SetLineWidth(1);
 beta_vs_m_comb_expected_shade1->SetFillStyle(1001);
 beta_vs_m_comb_expected_shade1->SetFillColor(kGreen);
 beta_vs_m_comb_expected_shade2->SetFillStyle(1001);
 beta_vs_m_comb_expected_shade2->SetFillColor(kYellow);

 
 beta_vs_m_comb_expected->SetLineWidth(3);
 beta_vs_m_comb_expected->SetLineColor(kBlack);
 beta_vs_m_comb_expected->SetLineStyle(2);

// ------------------------------------ DRAW  -------------------------------------//

 beta_vs_m_comb_expected_shade2->Draw("f");

 beta_vs_m_comb_expected_shade1->Draw("f");

 beta_vs_m_lljj_expected->Draw("C");
 beta_vs_m_lvjj_expected->Draw("C");
 beta_vs_m_comb_expected->Draw("C");
 beta_vs_m_lljj_observed->Draw("C");
 beta_vs_m_lvjj_observed->Draw("C");
 beta_vs_m_comb_observed->Draw("C");




 gPad->RedrawAxis();

 TLegend *legend = new TLegend(.59,.15,.92,.32);
 legend->SetBorderSize(1);
 legend->SetFillColor(0);
 //legend->SetFillStyle(0);
 legend->SetTextFont(132);
 legend->SetMargin(0.15);
 legend->SetHeader("95% CL limits");
 legend->AddEntry(beta_vs_m_comb_observed,"CMS #mu#mujj + #mu#nujj (Obs.)","l");
 //legend->AddEntry(beta_vs_m_comb_expected,"CMS #mu#mujj + #mu#nujj (Exp.)","l");
 legend->AddEntry(beta_vs_m_lvjj_observed,"CMS #mu#nujj (Obs.), 4.7 fb^{-1}","l");
 legend->AddEntry(beta_vs_m_lljj_observed,"CMS #mu#mujj (Obs.), 4.7 fb^{-1}","l");
 //legend->AddEntry(gr_excl_D0_new,"D#oslash (Obs.), fb^{-1}","l");
 legend->AddEntry(gr_excl_ATLAS,"ATLAS (Obs.), 35 pb^{-1}","f");
 //legend->AddEntry(gr_excl_D0,"D#oslash (Obs.), 1 fb^{-1}","l");

 legend->Draw();

 TLatex l1;
 l1.SetTextAlign(12);
 l1.SetTextFont(132);
 l1.SetNDC();
 l1.SetTextSize(0.04);
 l1.DrawLatex(0.68,0.41,"CMS Preliminary");
 l1.SetTextSize(0.04);
 l1.DrawLatex(0.68,0.36,sqrts.c_str());

 TLatex l2;
 l2.SetTextAlign(12);
 l2.SetTextFont(132);
 l2.SetNDC();
 l2.SetTextSize(0.04);
 l2.SetTextColor(kGreen+2);
 l2.SetTextAngle(35);
 //l2.DrawLatex(0.17,0.33,"#mu#mujj");
 l2.SetTextColor(kRed);
 l2.SetTextAngle(-35);
 //l2.DrawLatex(0.3,0.81,"#mu#nujj");
 l2.SetTextColor(kBlack);
 l2.SetTextAngle(75);
 //l2.DrawLatex(0.58,0.6,"#mu#mujj + #mu#nujj");

 c->SetGridx();
 c->SetGridy();
 c->SetLogy(0);
 c->SaveAs(fileName0.c_str());
 c->SaveAs(fileName1.c_str());
 c->SaveAs(fileName2.c_str());


 delete legend;
 delete beta_vs_m_lljj_observed;
 delete beta_vs_m_lvjj_observed;
 delete beta_vs_m_comb_observed;
 delete gr_excl_D0;
 delete gr_excl_ATLAS;
 delete gr_excl_D0_new;
 delete bg;
 delete c;
}

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
  tdrStyle->SetTitleFont(132, "XYZ");
  tdrStyle->SetTitleSize(0.06, "XYZ");
  // tdrStyle->SetTitleXSize(Float_t size = 0.02); // Another way to set the size?
  // tdrStyle->SetTitleYSize(Float_t size = 0.02);
  tdrStyle->SetTitleXOffset(0.9);
  tdrStyle->SetTitleYOffset(1.05);
  // tdrStyle->SetTitleOffset(1.1, "Y"); // Another way to set the Offset

  // For the axis labels:

  tdrStyle->SetLabelColor(1, "XYZ");
  tdrStyle->SetLabelFont(132, "XYZ");
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



