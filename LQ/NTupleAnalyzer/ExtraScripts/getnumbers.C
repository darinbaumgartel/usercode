
TFile f_placeholder("FILEINPUT");
TH1F* h_placeholder = (TH1F*)f_placeholder.Get("/LJFilter/EventCount/EventCounter");
int N_placeholder = h_placeholder->GetBinContent(1);
std::cout<<"placeholder"<<"\t\t"<<N_placeholder<<std::endl;

