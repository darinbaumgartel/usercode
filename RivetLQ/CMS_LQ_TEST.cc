// -*- C++ -*-
// AUTHOR:  Anil Singh (anil@cern.ch), Lovedeep Saini (lovedeep@cern.ch)
// Modified for 2011 analysis for wjets with jet pt/eta, D Baumgartel (darinb@cern.ch)

#include "Rivet/Analysis.hh"
#include "Rivet/RivetAIDA.hh"
#include "Rivet/Tools/Logging.hh"
#include "Rivet/Projections/FinalState.hh"
#include "Rivet/Projections/InitialQuarks.hh"
#include "Rivet/Projections/FastJets.hh"
#include "Rivet/Projections/VetoedFinalState.hh"
#include "Rivet/Projections/InvMassFinalState.hh"
#include "Rivet/Tools/ParticleIdUtils.hh"
#include "Rivet/Projections/MissingMomentum.hh"
#include "TTree.h"
#include "TFile.h"
#include "TString.h"
#include <iostream>
#include <ostream>
#include <iomanip>
namespace Rivet
{

	class CMS_LQ_TEST : public Analysis
	{
		public:

			CMS_LQ_TEST()
				: Analysis("CMS_LQ_TEST")
			{
				setBeams(PROTON, PROTON);
				setNeedsCrossSection(true);
			}

			/// Book histograms and initialise projections before the run
			void init()
			{

				const FinalState fs(-MAXRAPIDITY,MAXRAPIDITY);
				addProjection(fs, "FS");

      			const FinalState fsb;
				addProjection(fsb, "FSB");

      			MissingMomentum missing(fs);
      			addProjection(missing, "MET");

				// addProjection(FastJets(fs, FastJets::ANTIKT, 0.5), "Jets");


				_treeFileName = "rivetTree.root";
    			_treeFile = new TFile(_treeFileName, "recreate");
    			_rivetTree = new TTree("RivetTree", "RivetTree");	


    			_rivetTree->Branch("nevt", &_nevt, "nevt/I");	
    			_rivetTree->Branch("njet_WMuNu", &_njet_WMuNu, "njet_WMuNu/I");

    			_rivetTree->Branch("evweight", &_evweight, "evweight/D");			

    			_rivetTree->Branch("mt_munu", &_mt_munu, "mt_munu/D");			
    			_rivetTree->Branch("mt_mumet", &_mt_mumet, "mt_mumet/D");			

    			_rivetTree->Branch("htjets", &_htjets, "htjets/D");			

    			_rivetTree->Branch("ptmuon1", &_ptmuon1, "ptmuon1/D");			
    			_rivetTree->Branch("etamuon1", &_etamuon1, "etamuon1/D");			
    			_rivetTree->Branch("phimuon1", &_phimuon1, "phimuon1/D");			

    			_rivetTree->Branch("ptmuon2", &_ptmuon2, "ptmuon2/D");			
    			_rivetTree->Branch("etamuon2", &_etamuon2, "etamuon2/D");			
    			_rivetTree->Branch("phimuon2", &_phimuon2, "phimuon2/D");			

    			_rivetTree->Branch("ptneutrino", &_ptneutrino, "ptneutrino/D");			
    			_rivetTree->Branch("etaneutrino", &_etaneutrino, "etaneutrino/D");			
    			_rivetTree->Branch("phineutrino", &_phineutrino, "phineutrino/D");			

    			_rivetTree->Branch("ptmet", &_ptmet, "ptmet/D");			
    			_rivetTree->Branch("phimet", &_phimet, "phimet/D");	

    			_rivetTree->Branch("ptjet1", &_ptjet1, "ptjet1/D");			
    			_rivetTree->Branch("etajet1", &_etajet1, "etajet1/D");			
    			_rivetTree->Branch("phijet1", &_phijet1, "phijet1/D");
    			_rivetTree->Branch("dphijet1muon", &_dphijet1muon, "dphijet1muon/D");			

    			_rivetTree->Branch("ptjet2", &_ptjet2, "ptjet2/D");			
    			_rivetTree->Branch("etajet2", &_etajet2, "etajet2/D");			
    			_rivetTree->Branch("phijet2", &_phijet2, "phijet2/D");
    			_rivetTree->Branch("dphijet2muon", &_dphijet2muon, "dphijet2muon/D");			

    			_rivetTree->Branch("ptjet3", &_ptjet3, "ptjet3/D");			
    			_rivetTree->Branch("etajet3", &_etajet3, "etajet3/D");			
    			_rivetTree->Branch("phijet3", &_phijet3, "phijet3/D");
    			_rivetTree->Branch("dphijet3muon", &_dphijet3muon, "dphijet3muon/D");			

    			_rivetTree->Branch("ptjet4", &_ptjet4, "ptjet4/D");			
    			_rivetTree->Branch("etajet4", &_etajet4, "etajet4/D");			
    			_rivetTree->Branch("phijet4", &_phijet4, "phijet4/D");
    			_rivetTree->Branch("dphijet4muon", &_dphijet4muon, "dphijet4muon/D");			

    			_rivetTree->Branch("ptjet5", &_ptjet5, "ptjet5/D");			
    			_rivetTree->Branch("etajet5", &_etajet5, "etajet5/D");			
    			_rivetTree->Branch("phijet5", &_phijet5, "phijet5/D");
    			_rivetTree->Branch("dphijet5muon", &_dphijet5muon, "dphijet5muon/D");			

    		}

			double DeltaPhi(double phi1, double phi2)
			{
				double pi = 3.14159265358;
				double dphi = fabs(phi1-phi2);
				if (dphi>pi) dphi = 2.0*pi-dphi;
				return dphi; 
			}

			


			void analyze(const Event& event)
			{

				_mt_munu = -5.0;
	    		_ptmuon1 = -5.0;
	    		_etamuon1 = -5.0;
	    		_phimuon1 = -5.0;

	    		_ptmuon2 = -5.0;
	    		_etamuon2 = -5.0;
	    		_phimuon2 = -5.0;

	    		_ptmet = -5.0;
	    		_phimet = -5.0;
	    		_mt_mumet = -5.0;
	    		_htjets = 0.0;

	    		_ptneutrino = -1.0;
	    		_etaneutrino = -5.0;
	    		_phineutrino = -5.0;

	    		_ptjet1 = -5.0;
	    		_etajet1 = -5.0;
	    		_phijet1 = -5.0;
	    		_dphijet1muon = -1.0;

	    		_ptjet2 = -5.0;
	    		_etajet2 = -5.0;
	    		_phijet2 = -5.0;
	    		_dphijet2muon = -1.0;

	    		_ptjet3 = -5.0;
	    		_etajet3 = -5.0;
	    		_phijet3 = -5.0;
	    		_dphijet3muon = -1.0;

	    		_ptjet4 = -5.0;
	    		_etajet4 = -5.0;
	    		_phijet4 = -5.0;
	    		_dphijet4muon = -1.0;

	    		_ptjet5 = -5.0;
	    		_etajet5 = -5.0;
	    		_phijet5 = -5.0;
	    		_dphijet5muon = -1.0;

				_njet_WMuNu = -1;

				_evweight = -1.0;
				_nevt = -1;

				const double weight = event.weight();
				//std::cout<<"&&&  "<<event.weight()<<std::endl;
				_nevt = (event.genEvent()).event_number();
				_evweight = weight;
				const FinalState& totalfinalstate = applyProjection<FinalState>(event, "FS");
				const ParticleVector& AllParticles = totalfinalstate.particles();


				if (true) {


					for (unsigned int nn = 0; nn<AllParticles.size(); nn++)
					{
						unsigned int _nn_pid = 1*std::abs(AllParticles[nn].pdgId());
						if (_nn_pid != 13) continue;

						float _nn_pt  = AllParticles[nn].momentum().pT();
						float _nn_eta = AllParticles[nn].momentum().eta();
						float _nn_phi = AllParticles[nn].momentum().phi();		

						if (_ptmuon1 < 0.0)
						{
							_ptmuon1 = _nn_pt;
							_etamuon1 = _nn_eta;
							_phimuon1 = _nn_phi;
						}

						if ( (_ptmuon1 > 0.0) &&  (_ptmuon2 < 0.0) )
						{
							_ptmuon2 = _nn_pt;
							_etamuon2 = _nn_eta;
							_phimuon2 = _nn_phi;
						}

					}


					for (unsigned int nn = 0; nn<AllParticles.size(); nn++)
					{
						unsigned int _nn_pid = 1*std::abs(AllParticles[nn].pdgId());
						if (_nn_pid != 14) continue;

						_ptneutrino  = AllParticles[nn].momentum().pT();
						_etaneutrino = AllParticles[nn].momentum().eta();
						_phineutrino = AllParticles[nn].momentum().phi();		

					}



					//Obtain the jets.
					vector<FourMomentum> finaljet_list;


    				foreach (const GenParticle* p, Rivet::particles(event.genEvent())) {

	     				PdgId pid = abs(p->pdg_id());
	     				int _nn_pid = std::abs(1*pid);
						int st = p->status();
	     				
	     				if (pid > 19) continue;
						if ( (_nn_pid != 4)  && (_nn_pid != 3) ) continue;
						if (st != 3) continue;

						finaljet_list.push_back(p->momentum());

 					}


					_njet_WMuNu = finaljet_list.size();


    			  	const MissingMomentum& met = applyProjection<MissingMomentum>(event, "MET");
   				   	_ptmet = met.visibleMomentum().pT();
   				   	_phimet = met.visibleMomentum().phi();
   				   	_phimet -= 3.1415926;
   				   	if (_phimet < 0.0) _phimet += 2.0*3.1415926;
					_mt_mumet = sqrt(2.0*_ptmuon1*_ptmet*(1.0-cos(_phimet-_phimuon1)));



					if (finaljet_list.size()>0){
						_ptjet1=finaljet_list[0].pT();
						_etajet1=finaljet_list[0].eta();
						_phijet1=finaljet_list[0].phi();
						_dphijet1muon = DeltaPhi(_phijet1,_phimuon1);
					}

					if (finaljet_list.size()>1){
						_ptjet2=finaljet_list[1].pT();
						_etajet2=finaljet_list[1].eta();
						_phijet2=finaljet_list[1].phi();
						_dphijet2muon = DeltaPhi(_phijet2,_phimuon1);
					}

					if (finaljet_list.size()>2){
						_ptjet3=finaljet_list[2].pT();
						_etajet3=finaljet_list[2].eta();
						_phijet3=finaljet_list[2].phi();
						_dphijet3muon = DeltaPhi(_phijet3,_phimuon1);
					}

					if (finaljet_list.size()>3){
						_ptjet4=finaljet_list[3].pT();
						_etajet4=finaljet_list[3].eta();
						_phijet4=finaljet_list[3].phi();
						_dphijet4muon = DeltaPhi(_phijet4,_phimuon1);
					}

					if (finaljet_list.size()>4){
						_ptjet5=finaljet_list[4].pT();
						_etajet5=finaljet_list[4].eta();
						_phijet5=finaljet_list[4].phi();
						_dphijet5muon = DeltaPhi(_phijet5,_phimuon1);
					}

				_rivetTree->Fill();

				}	



			}

			/// Normalise histograms etc., after the run
			void finalize()
			{

				_rivetTree->Write();
				_treeFile->Close();
			}

		private:

			TTree* _rivetTree;
			TString _treeFileName;
			TFile* _treeFile;

    		int _nevt; 
    		int _njet_WMuNu;

    		double _evweight;

			double _mt_munu;
			double _mt_mumet;
			double _htjets;
			double _ptmet;
			double _phimet;

    		double _ptmuon1;
    		double _etamuon1;
    		double _phimuon1;

    		double _ptmuon2;
    		double _etamuon2;
    		double _phimuon2;

    		double _ptneutrino;
    		double _etaneutrino;
    		double _phineutrino;

    		double _ptjet1;
    		double _etajet1;
    		double _phijet1;
    		double _dphijet1muon;

    		double _ptjet2;
    		double _etajet2;
    		double _phijet2;
    		double _dphijet2muon;

    		double _ptjet3;
    		double _etajet3;
    		double _phijet3;
    		double _dphijet3muon;

    		double _ptjet4;
    		double _etajet4;
    		double _phijet4;
    		double _dphijet4muon;

    		double _ptjet5;
    		double _etajet5;
    		double _phijet5;
    		double _dphijet5muon;

	};

	AnalysisBuilder<CMS_LQ_TEST> plugin_CMS_LQ_TEST;

}
