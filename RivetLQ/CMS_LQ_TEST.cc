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
#include "TLorentzVector.h"
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

				_rivetTree->Branch("ptjet2", &_ptjet2, "ptjet2/D");
				_rivetTree->Branch("etajet2", &_etajet2, "etajet2/D");
				_rivetTree->Branch("phijet2", &_phijet2, "phijet2/D");

				_rivetTree->Branch("m_muon1jet1", &_m_muon1jet1, "m_muon1jet1/D");
				_rivetTree->Branch("m_muon1jet2", &_m_muon1jet2, "m_muon1jet2/D");
				_rivetTree->Branch("m_muon2jet1", &_m_muon2jet1, "m_muon2jet1/D");
				_rivetTree->Branch("m_muon2jet2", &_m_muon2jet2, "m_muon2jet2/D");

				_rivetTree->Branch("mt_muon1jet1", &_mt_muon1jet1, "mt_muon1jet1/D");
				_rivetTree->Branch("mt_muon1jet2", &_mt_muon1jet2, "mt_muon1jet2/D");
				_rivetTree->Branch("mt_muon2jet1", &_mt_muon2jet1, "mt_muon2jet1/D");
				_rivetTree->Branch("mt_muon2jet2", &_mt_muon2jet2, "mt_muon2jet2/D");

				_rivetTree->Branch("mt_metjet1", &_mt_metjet1, "mt_metjet1/D");
				_rivetTree->Branch("mt_metjet2", &_mt_metjet2, "mt_metjet2/D");
			}

			double DeltaPhi(double phi1, double phi2)
			{
				double pi = 3.14159265358;
				double dphi = fabs(phi1-phi2);
				if (dphi>pi) dphi = 2.0*pi-dphi;
				return dphi;
			}

			Double_t TMass(TLorentzVector p1, TLorentzVector p2)
			{
				double Pt1 = p1.Pt();
				double Pt2 = p2.Pt();
				double DPhi12 = p1.DeltaPhi(p2);
				return sqrt( 2*Pt2*Pt1*(1-cos(DPhi12)) );
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

				_ptjet2 = -5.0;
				_etajet2 = -5.0;
				_phijet2 = -5.0;

				_njet_WMuNu = -1;

				_evweight = -1.0;
				_nevt = -1;

				_m_muon1jet1 = -5.0;
				_m_muon1jet2 = -5.0;
				_m_muon2jet1 = -5.0;
				_m_muon2jet2 = -5.0;

				_mt_muon1jet1 = -5.0;
				_mt_muon1jet2 = -5.0;
				_mt_muon2jet1 = -5.0;
				_mt_muon2jet2 = -5.0;
				_mt_metjet1 = -5.0;
				_mt_metjet2 = -5.0;

				const double weight = event.weight();
				//std::cout<<"&&&  "<<event.weight()<<std::endl;
				_nevt = (event.genEvent()).event_number();
				_evweight = weight;
				const FinalState& totalfinalstate = applyProjection<FinalState>(event, "FS");
				const ParticleVector& AllParticles = totalfinalstate.particles();

				for (unsigned int nn = 0; nn<AllParticles.size(); nn++)
				{
					unsigned int _nn_pid = 1*std::abs(AllParticles[nn].pdgId());
					if (_nn_pid != 13) continue;

					float _nn_pt  = AllParticles[nn].momentum().pT();
					float _nn_eta = AllParticles[nn].momentum().eta();
					float _nn_phi = AllParticles[nn].momentum().phi();

					if ( (_ptmuon1 > 0.0) &&  (_ptmuon2 < 0.0) )
					{
						_ptmuon2 = _nn_pt;
						_etamuon2 = _nn_eta;
						_phimuon2 = _nn_phi;
					}

					if (_ptmuon1 < 0.0)
					{
						_ptmuon1 = _nn_pt;
						_etamuon1 = _nn_eta;
						_phimuon1 = _nn_phi;
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

				foreach (const GenParticle* p, Rivet::particles(event.genEvent()))
				{

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

				if (finaljet_list.size()>0)
				{
					_ptjet1=finaljet_list[0].pT();
					_etajet1=finaljet_list[0].eta();
					_phijet1=finaljet_list[0].phi();
				}

				if (finaljet_list.size()>1)
				{
					_ptjet2=finaljet_list[1].pT();
					_etajet2=finaljet_list[1].eta();
					_phijet2=finaljet_list[1].phi();
				}

				if (_ptjet2 > _ptjet1)
				{
					double _ptleadjet = _ptjet2;
					double _etaleadjet = _etajet2;
					double _phileadjet = _phijet2;

					_ptjet2 = _ptjet1;
					_etajet2 = _etajet1;
					_phijet2 = _phijet1;

					_ptjet1 = _ptleadjet;
					_etajet1 = _etaleadjet;
					_phijet1 = _phileadjet;

				}

				TLorentzVector _m1,_m2,_met,_j1,_j2;
				_m1.SetPtEtaPhiM(_ptmuon1,_etamuon1,_phimuon1,0.0);
				_m2.SetPtEtaPhiM(_ptmuon2,_etamuon2,_phimuon2,0.0);
				_m1.SetPtEtaPhiM(_ptjet1,_etajet1,_phijet1,0.0);
				_m2.SetPtEtaPhiM(_ptjet2,_etajet2,_phijet2,0.0);
				_met.SetPtEtaPhiM(_ptmet,0.0,_phimet,0.0);

				_m_muon1jet1 = (_m1+_j1).M();
				_m_muon1jet2 = (_m1+_j2).M();
				_m_muon2jet1 = (_m2+_j1).M();
				_m_muon2jet2 = (_m2+_j2).M();

				_mt_muon1jet1 = TMass(_m1,_j1);
				_mt_muon1jet2 = TMass(_m1,_j2);
				_mt_muon2jet1 = TMass(_m2,_j1);
				_mt_muon2jet2 = TMass(_m2,_j2);
				_mt_metjet1 = TMass(_met,_j1);
				_mt_metjet2 = TMass(_met,_j2);

				_rivetTree->Fill();

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

			double _ptjet2;
			double _etajet2;
			double _phijet2;

			double _m_muon1jet1;
			double _m_muon1jet2;
			double _m_muon2jet1;
			double _m_muon2jet2;
			double _mt_muon1jet1;
			double _mt_muon1jet2;
			double _mt_muon2jet1;
			double _mt_muon2jet2;
			double _mt_metjet1;
			double _mt_metjet2;

	};

	AnalysisBuilder<CMS_LQ_TEST> plugin_CMS_LQ_TEST;

}
