{

TFile f("puweightsGoodCollisions2011.root");

TH1D *h = (TH1D*)f->Get("pileup");

int nbinsx = h->GetXaxis()->GetNbins();

Double_t ndat = -1.0;

Double_t ncenter = -1.0;for (int ibin=0;ibin<nbinsx;ibin++)
	{
	 ndat = 1.0*(h->GetBinContent(ibin));
	 ncenter = 1.0*(h->GetBinCenter(ibin));
  std::cout<<ncenter<<"  "<<ndat<<std::endl;

  }

	gROOT->Reset(); gROOT->ProcessLine(".q;");

}

