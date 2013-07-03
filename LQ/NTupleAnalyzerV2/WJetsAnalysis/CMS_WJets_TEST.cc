// -*- C++ -*-
// AUTHOR:  Anil Singh (anil@cern.ch), Lovedeep Saini (lovedeep@cern.ch)
// Modified for 2011 analysis for wjets with jet pt/eta, D Baumgartel (darinb@cern.ch)

#include "Rivet/Analysis.hh"
#include "Rivet/RivetAIDA.hh"
#include "Rivet/Tools/Logging.hh"
#include "Rivet/Projections/FinalState.hh"
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

	class CMS_WJets_TEST : public Analysis
	{
		public:

			CMS_WJets_TEST()
				: Analysis("CMS_WJets_TEST")
			{
				setBeams(PROTON, PROTON);
				setNeedsCrossSection(true);
			}

			/// Book histograms and initialise projections before the run
			void init()
			{

				const FinalState fs(-MAXRAPIDITY,MAXRAPIDITY);
				addProjection(fs, "FS");

				vector<pair<PdgId,PdgId> > vidsZ;
				vidsZ.push_back(make_pair(ELECTRON, POSITRON));
				vidsZ.push_back(make_pair(MUON, ANTIMUON));

      			MissingMomentum missing(fs);
      			addProjection(missing, "MET");

				FinalState fsZ(-MAXRAPIDITY,MAXRAPIDITY);
				InvMassFinalState invfsZ(fsZ, vidsZ, 60*GeV, 120*GeV);
				addProjection(invfsZ, "INVFSZ");

				vector<pair<PdgId,PdgId> > vidsW;
				vidsW.push_back(make_pair(ELECTRON, NU_EBAR));
				vidsW.push_back(make_pair(POSITRON, NU_E));
				vidsW.push_back(make_pair(MUON, NU_MUBAR));
				vidsW.push_back(make_pair(ANTIMUON, NU_MU));

				FinalState fsW(-MAXRAPIDITY,MAXRAPIDITY);
				InvMassFinalState invfsW(fsW, vidsW, 0.01*GeV, 99990*GeV);
				addProjection(invfsW, "INVFSW");

		       // WFinder wfinder_dressed_mu(fs, std::vector<std::pair<-5.0,5.0>, 0.0, PdgId(13), 0.0*GeV, 11000.0*GeV, 0.0*GeV, 0.1,true,false);
		       // addProjection(wfinder_dressed_mu, "WFinder_dressed_mu");

				VetoedFinalState vfs(fs);
				vfs.addVetoOnThisFinalState(invfsZ);
				vfs.addVetoOnThisFinalState(invfsW);
				addProjection(vfs, "VFS");
				addProjection(FastJets(vfs, FastJets::ANTIKT, 0.5), "Jets");

				_histNoverN0Welec = bookDataPointSet(1,1,1);
				_histNoverNm1Welec = bookDataPointSet(2,1,1);
				_histNoverN0Wmu = bookDataPointSet(3,1,1);
				_histNoverNm1Wmu = bookDataPointSet(4,1,1);
				_histNoverN0Zelec = bookDataPointSet(5,1,1);
				_histNoverNm1Zelec = bookDataPointSet(6,1,1);
				_histNoverN0Zmu = bookDataPointSet(7,1,1);
				_histNoverNm1Zmu = bookDataPointSet(8,1,1);
				_histJetMultWelec  = bookHistogram1D("njetWenu", 5, -0.5, 4.5);
				_histJetMultWmu    = bookHistogram1D("njetWmunu", 5, -0.5, 4.5);
				_histJetMultZelec  = bookHistogram1D("njetZee", 5, -0.5, 4.5);
				_histJetMultZmu    = bookHistogram1D("njetZmumu", 5, -0.5, 4.5);

				_histJetMultWmuPlus = bookHistogram1D("njetWmuPlus", 5, -0.5, 4.5);
				_histJetMultWmuMinus = bookHistogram1D("njetWmuMinus", 5, -0.5, 4.5);
				_histJetMultWelPlus = bookHistogram1D("njetWePlus", 5, -0.5, 4.5);
				_histJetMultWelMinus = bookHistogram1D("njetWeMinus", 5, -0.5, 4.5);

				_histJetPT1Wmu    = bookHistogram1D("JetPT1Wmunu", 26,30,300);
				_histJetPT2Wmu    = bookHistogram1D("JetPT2Wmunu", 26,30,300);
				_histJetPT3Wmu    = bookHistogram1D("JetPT3Wmunu", 13,30,300);
				_histJetPT4Wmu    = bookHistogram1D("JetPT4Wmunu", 13,30,300);

				_histJetETA1Wmu    = bookHistogram1D("JetETA1Wmunu", 12,-2.4,2.4);
				_histJetETA2Wmu    = bookHistogram1D("JetETA2Wmunu", 12,-2.4,2.4);
				_histJetETA3Wmu    = bookHistogram1D("JetETA3Wmunu", 12,-2.4,2.4);
				_histJetETA4Wmu    = bookHistogram1D("JetETA4Wmunu", 12,-2.4,2.4);


				_histJetMultRatioWmuPlusMinus = bookDataPointSet(10, 1, 1);
				_histJetMultRatioWelPlusMinus = bookDataPointSet(9, 1, 1);

				_treeFileName = "rivetTree.root";
   		 		// Create a file for the Tree
    			_treeFile = new TFile(_treeFileName, "recreate");



    			// Book the ntuple.

    			_rivetTree = new TTree("RivetTree", "RivetTree");	


    			_rivetTree->Branch("nevt", &_nevt, "nevt/I");	
    			_rivetTree->Branch("njet_WMuNu", &_njet_WMuNu, "njet_WMuNu/I");
    			_rivetTree->Branch("nBjet_WMuNu", &_nBjet_WMuNu, "nBjet_WMuNu/I");

    			_rivetTree->Branch("evweight", &_evweight, "evweight/D");			

    			_rivetTree->Branch("mt_munu", &_mt_munu, "mt_munu/D");			
    			_rivetTree->Branch("mt_mumet", &_mt_mumet, "mt_mumet/D");			

    			_rivetTree->Branch("htjets", &_htjets, "htjets/D");			


    			_rivetTree->Branch("ptmuon", &_ptmuon, "ptmuon/D");			
    			_rivetTree->Branch("etamuon", &_etamuon, "etamuon/D");			
    			_rivetTree->Branch("phimuon", &_phimuon, "phimuon/D");			

    			_rivetTree->Branch("ptneutrino", &_ptneutrino, "ptneutrino/D");			
    			_rivetTree->Branch("etaneutrino", &_etaneutrino, "etaneutrino/D");			
    			_rivetTree->Branch("phineutrino", &_phineutrino, "phineutrino/D");			

    			_rivetTree->Branch("ptmet", &_ptmet, "ptmet/D");			
    			_rivetTree->Branch("phimet", &_phimet, "phimet/D");	

    			_rivetTree->Branch("ptjet1", &_ptjet1, "ptjet1/D");			
    			_rivetTree->Branch("etajet1", &_etajet1, "etajet1/D");			
    			_rivetTree->Branch("phijet1", &_phijet1, "phijet1/D");
    			_rivetTree->Branch("dphijet1muon", &_dphijet1muon, "dphijet1muon/D");			
    			_rivetTree->Branch("isBjet1", &_isBjet1, "isBjet1/D");			

    			_rivetTree->Branch("ptjet2", &_ptjet2, "ptjet2/D");			
    			_rivetTree->Branch("etajet2", &_etajet2, "etajet2/D");			
    			_rivetTree->Branch("phijet2", &_phijet2, "phijet2/D");
    			_rivetTree->Branch("dphijet2muon", &_dphijet2muon, "dphijet2muon/D");			
    			_rivetTree->Branch("isBjet2", &_isBjet2, "isBjet2/D");			

    			_rivetTree->Branch("ptjet3", &_ptjet3, "ptjet3/D");			
    			_rivetTree->Branch("etajet3", &_etajet3, "etajet3/D");			
    			_rivetTree->Branch("phijet3", &_phijet3, "phijet3/D");
    			_rivetTree->Branch("dphijet3muon", &_dphijet3muon, "dphijet3muon/D");			
    			_rivetTree->Branch("isBjet3", &_isBjet3, "isBjet3/D");			

    			_rivetTree->Branch("ptjet4", &_ptjet4, "ptjet4/D");			
    			_rivetTree->Branch("etajet4", &_etajet4, "etajet4/D");			
    			_rivetTree->Branch("phijet4", &_phijet4, "phijet4/D");
    			_rivetTree->Branch("dphijet4muon", &_dphijet4muon, "dphijet4muon/D");			
    			_rivetTree->Branch("isBjet4", &_isBjet4, "isBjet4/D");			

    			_rivetTree->Branch("ptjet5", &_ptjet5, "ptjet5/D");			
    			_rivetTree->Branch("etajet5", &_etajet5, "etajet5/D");			
    			_rivetTree->Branch("phijet5", &_phijet5, "phijet5/D");
    			_rivetTree->Branch("dphijet5muon", &_dphijet5muon, "dphijet5muon/D");			
    			_rivetTree->Branch("isBjet5", &_isBjet5, "isBjet5/D");			

    			NZE=0;
    			NZM=0;
    			NWE=0;
    			NWM=0;
    			NT=0;

			}

			double DeltaPhi(double phi1, double phi2)
			{
				double pi = 3.14159265358;
				double dphi = fabs(phi1-phi2);
				if (dphi>pi) dphi = 2.0*pi-dphi;
				return dphi; 
			}

			bool ApplyElectronCutsForZee(double pt1, double pt2, double eta1, double eta2)
			{
				bool isFid1 = ((fabs(eta1)<1.4442)||((fabs(eta1)>1.566)&&(fabs(eta1)<2.5)));
				bool isFid2 = ((fabs(eta2)<1.4442)||((fabs(eta2)>1.566)&&(fabs(eta2)<2.5)));
				if( isFid1 && isFid2 && pt1>20 && pt2 >10) return true;

				else return false;
			}

			bool ApplyMuonCutsForZmm(double pt1, double pt2, double eta1, double eta2)
			{
				bool isFid1 = ((fabs(eta1)<2.1));
				bool isFid2 = ((fabs(eta2)<2.4));
				if( isFid1 && isFid2 && pt1>20 && pt2 >10) return true;
				else return false;
			}

			bool ApplyElectronCutsForWen(double pt1, double eta1)
			{
				bool isFid1 = ((fabs(eta1)<1.4442)||((fabs(eta1)>1.566)&&(fabs(eta1)<2.5)));
				if( isFid1 && pt1>20 ) return true;
				return 0;
			}

			bool ApplyMuonCutsForWmn(double pt1, double eta1)
			{
				bool isFid1 = ((fabs(eta1)<2.1));
				if( isFid1 && pt1>20) return true;
				return 0;
			}

			void Fill(AIDA::IHistogram1D*& _histJetMult, const double& weight, std::vector<FourMomentum>& finaljet_list)
			{
				_histJetMult->fill(0, weight);
				for (size_t i=0 ; i<finaljet_list.size() ; ++i)
				{
					if (i==6) break;
								 // inclusive
					_histJetMult->fill(i+1, weight);
				}
			}


			void FillWithValue(AIDA::IHistogram1D*& _hist, const double& weight, const double &value)
			{
				_hist->fill(value, weight);
			}


			void FillNoverNm1(AIDA::IHistogram1D*& _histJetMult,AIDA::IDataPointSet* _histNoverNm1)
			{
				std::vector<double> y, yerr;
				for (int i=0; i<_histJetMult->axis().bins()-1; i++)
				{
					double val = 0.;
					double err = 0.;
					if (!fuzzyEquals(_histJetMult->binHeight(i), 0))
					{
						val = _histJetMult->binHeight(i+1) / _histJetMult->binHeight(i);
						err = val * sqrt(  pow(_histJetMult->binError(i+1)/_histJetMult->binHeight(i+1), 2)
							+ pow(_histJetMult->binError(i)  /_histJetMult->binHeight(i)  , 2) );
					}
					y.push_back(val);
					yerr.push_back(err);
				}
				_histNoverNm1->setCoordinate(1, y, yerr);
			}
			void FillNoverN0(AIDA::IHistogram1D*& _histJetMult,AIDA::IDataPointSet* _histNoverN0)
			{
				std::vector<double> y, yerr;
				for (int i=0; i<_histJetMult->axis().bins()-1; i++)
				{
					double val = 0.;
					double err = 0.;
					if (!fuzzyEquals(_histJetMult->binHeight(i), 0))
					{
						val = _histJetMult->binHeight(i+1) / _histJetMult->binHeight(0);
						err = val * sqrt(  pow(_histJetMult->binError(i+1)/_histJetMult->binHeight(i+1), 2)
							+ pow(_histJetMult->binError(0)  /_histJetMult->binHeight(0)  , 2) );
					}
					y.push_back(val);
					yerr.push_back(err);
				}
				_histNoverN0->setCoordinate(1, y, yerr);
			}

			void FillChargeAssymHistogramSet(  AIDA::IHistogram1D*& _histJetMult1,AIDA::IHistogram1D*& _histJetMult2, AIDA::IDataPointSet* _histJetMultRatio12 )
			{
				std::vector<double> yval, yerr;
				for (int i = 0; i < 4; ++i)
				{
					std::vector<double> xval; xval.push_back(i);
					std::vector<double> xerr; xerr.push_back(.5);
					double ratio = 0;
					double err = 0.;
					double num = _histJetMult1->binHeight(i)-_histJetMult2->binHeight(i);
					double den = _histJetMult1->binHeight(i)+_histJetMult2->binHeight(i);
					double errNum = 0;
					errNum = std::pow(_histJetMult1->binError(i),2)+std::pow(_histJetMult2->binError(i),2);
					double errDen = 0;
					errDen = std::pow(_histJetMult1->binError(i),2)+std::pow(_histJetMult2->binError(i),2);

					if (den)ratio = num/den;

					if(num) errNum = errNum/(num*num);
					if(den) errDen = errDen/(den*den);

					err = std::sqrt(errDen+errNum);
					if(!(err==err))err=0;
					yval.push_back(ratio);
					yerr.push_back(ratio*err);
				}

				_histJetMultRatio12->setCoordinate(1,yval,yerr);
			}

			void analyze(const Event& event)
			{
				NT+= 1;
				//std::cout<<"A: "<<NT<<std::endl;
				//some flag definitions.



				bool isZmm =false;
				bool isZee =false;
				bool isWmn =false;
				bool isWen =false;
				bool isWmnMinus =false;
				bool isWmnPlus  =false;
				bool isWenMinus =false;
				bool isWenPlus  =false;

				_mt_munu = -5.0;
	    		_ptmuon = -5.0;
	    		_etamuon = -5.0;
	    		_phimuon = -5.0;
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
	    		_isBjet1 = -1;
	    		_dphijet1muon = -1.0;

	    		_ptjet2 = -5.0;
	    		_etajet2 = -5.0;
	    		_phijet2 = -5.0;
	    		_isBjet2 = -1;
	    		_dphijet2muon = -1.0;

	    		_ptjet3 = -5.0;
	    		_etajet3 = -5.0;
	    		_phijet3 = -5.0;
	    		_isBjet3 = -1;
	    		_dphijet3muon = -1.0;

	    		_ptjet4 = -5.0;
	    		_etajet4 = -5.0;
	    		_phijet4 = -5.0;
	    		_isBjet4 = -1;
	    		_dphijet4muon = -1.0;

	    		_ptjet5 = -5.0;
	    		_etajet5 = -5.0;
	    		_phijet5 = -5.0;
	    		_isBjet5 = -1;
	    		_dphijet5muon = -1.0;

				_njet_WMuNu = -1;
				_nBjet_WMuNu = -1;

				_evweight = -1.0;
				_nevt = -1;

				const double weight = event.weight();
				//std::cout<<"&&&  "<<event.weight()<<std::endl;
				_nevt = (event.genEvent()).event_number();
				_evweight = weight;

				const InvMassFinalState& invMassFinalStateZ = applyProjection<InvMassFinalState>(event, "INVFSZ");
				const InvMassFinalState& invMassFinalStateW = applyProjection<InvMassFinalState>(event, "INVFSW");
				// const WFinder& wfinder_dressed_mu = applyProjection<WFinder>(event, "WFinder_dressed_mu");
				// const WFinder& wfinder_bare_mu    = applyProjection<WFinder>(event, "WFinder_bare_mu");
				const FinalState& totalfinalstate = applyProjection<FinalState>(event, "FS");


				bool isW(false); bool isZ(false);

				isW  = (invMassFinalStateZ.empty() && !(invMassFinalStateW.empty()));
				isZ  = (!(invMassFinalStateZ.empty()) && invMassFinalStateW.empty());

				const ParticleVector&  ZDecayProducts =  invMassFinalStateZ.particles();
				const ParticleVector&  WDecayProducts =  invMassFinalStateW.particles();
				const ParticleVector& AllParticles = totalfinalstate.particles();

				if (ZDecayProducts.size() < 2 && WDecayProducts.size() <2) vetoEvent;

				double pt1=-9999.,  pt2=-9999.;
				double phi1=-9999., phi2=-9999.;
				double eta1=-9999., eta2=-9999.;

				double mt = 999999;
				if(isZ)
				{
					pt1   = ZDecayProducts[0].momentum().pT();
					pt2   = ZDecayProducts[1].momentum().pT();
					eta1 = ZDecayProducts[0].momentum().eta();
					eta2 = ZDecayProducts[1].momentum().eta();
					phi1 = ZDecayProducts[0].momentum().phi();
					phi2 = ZDecayProducts[1].momentum().phi();
				}

				if(isW)
				{
					if(
						(fabs(WDecayProducts[1].pdgId()) == NU_MU) || (fabs(WDecayProducts[1].pdgId()) == NU_E))
					{
						pt1  = WDecayProducts[0].momentum().pT();
						pt2  = WDecayProducts[1].momentum().Et();
						eta1 = WDecayProducts[0].momentum().eta();
						eta2 = WDecayProducts[1].momentum().eta();
						phi1 = WDecayProducts[0].momentum().phi();
						phi2 = WDecayProducts[1].momentum().phi();
						mt=sqrt(2.0*pt1*pt2*(1.0-cos(phi1-phi2)));
					}
					else
					{
						pt1  = WDecayProducts[1].momentum().pT();
						pt2  = WDecayProducts[0].momentum().Et();
						eta1 = WDecayProducts[1].momentum().eta();
						eta2 = WDecayProducts[0].momentum().eta();
						phi1 = WDecayProducts[1].momentum().phi();
						phi2 = WDecayProducts[0].momentum().phi();
						mt=sqrt(2.0*pt1*pt2*(1.0-cos(phi1-phi2)));
					}
				}

				//if(isW && ( mt<50 || mt>110)) vetoEvent;

				isZmm = isZ && ((fabs(ZDecayProducts[0].pdgId()) == 13) && (fabs(ZDecayProducts[1].pdgId()) == 13));
				isZee = isZ && ((fabs(ZDecayProducts[0].pdgId()) == 11) && (fabs(ZDecayProducts[1].pdgId()) == 11));
				isWmn  = isW && ((fabs(WDecayProducts[0].pdgId()) == 14) || (fabs(WDecayProducts[1].pdgId()) == 14));
				isWen  = isW && ((fabs(WDecayProducts[0].pdgId()) == 12) || (fabs(WDecayProducts[1].pdgId()) == 12));

				NZE += isZee;
				NZM += isZmm;
				NWE += isWen;
				NWM += isWmn;
				//std::cout<<NZE<<" "<<NZM<<" "<<NWE<<" "<<NWM<<" "<<std::endl;
				// std::cout<<isWmn<<"  "<<isWen<<std::endl;

				if(isWmn)
				{
					if((WDecayProducts[0].pdgId()==-13)|| (WDecayProducts[1].pdgId()==-13))
					{
						isWmnMinus = false;
						isWmnPlus = true;
					}
					else
					{
						isWmnMinus = true;
						isWmnPlus  = false;
					}
				}

				if(isWen)
				{
					if((WDecayProducts[0].pdgId()==11)|| (WDecayProducts[1].pdgId()==11))
					{
						isWenMinus = true;
						isWenPlus = false;
					}
					else
					{
						isWenMinus = false;
						isWenPlus  = true;
					}
				}
				//std::cout<<" ----------- " <<std::endl;
				//std::cout<<isWmn<<std::endl;

				if(!((isZmm||isZee)||(isWmn||isWen)))vetoEvent;

				bool passBosonConditions = false;
				if(isZmm)passBosonConditions = ApplyMuonCutsForZmm(pt1,pt2,eta1,eta2);
				if(isZee)passBosonConditions = ApplyElectronCutsForZee(pt1,pt2,eta1,eta2);
				if(isWen)passBosonConditions = ApplyElectronCutsForWen(pt1,eta1);
				if(isWmn)passBosonConditions = ApplyMuonCutsForWmn(pt1,eta1);

				if(!passBosonConditions)vetoEvent;



				if (isWmn) {

					int muind = -1;
					int nuind=-1;
					if (fabs(WDecayProducts[0].pdgId()) == 13) muind = 0;
					if (fabs(WDecayProducts[1].pdgId()) == 13) muind = 1;
					nuind = 1*(muind==0);
					_mt_munu = mt;
					_ptmuon  = WDecayProducts[muind].momentum().pT();
					_etamuon = WDecayProducts[muind].momentum().eta();
					_phimuon = WDecayProducts[muind].momentum().phi();
					_ptneutrino  = WDecayProducts[nuind].momentum().pT();
					_etaneutrino = WDecayProducts[nuind].momentum().eta();
					_phineutrino = WDecayProducts[nuind].momentum().phi();		


					// std::cout<<" ------------------------- "<<std::endl;
					FourMomentum finalmuon(WDecayProducts[muind].momentum());
					// std::cout<<AllParticles.size()<<std::endl;
					// std::cout<<_ptmuon<<std::endl;

					for (unsigned int nn = 0; nn<AllParticles.size(); nn++)
					{
						unsigned int _nn_pid = 1*(AllParticles[nn].pdgId());
						if (_nn_pid != 22) continue;

						float _nn_pt  = AllParticles[nn].momentum().pT();
						float _nn_eta = AllParticles[nn].momentum().eta();
						float _nn_phi = AllParticles[nn].momentum().phi();		
						double dr = deltaR(AllParticles[nn].momentum(),WDecayProducts[muind].momentum());				
						// std::cout<<" --- "<<_nn_pid<<"  "<<_nn_pt<<"  "<<_nn_eta<<"  "<<dr<<std::endl;
						// std::cout<<" --- "<<_nn_pid<<"  |  "<<WDecayProducts[muind].momentum().eta()<<"  "<<_nn_eta<<"  |  "<<WDecayProducts[muind].momentum().phi()<<"  "<<_nn_phi<<"  |  "<<dr<<std::endl;

						if (dr<0.1) finalmuon = add(finalmuon,AllParticles[nn].momentum());
						// if (dr<0.1) std::cout<<"  !!!!!"<<std::endl;

					}


					_ptmuon  = finalmuon.pT();
					_etamuon = finalmuon.eta();
					_phimuon = finalmuon.phi();

					// std::cout<<_ptmuon<<std::endl;


					//Obtain the jets.
					vector<FourMomentum> finaljet_list;
					vector<int> finaljet_list_btags;
					vector<FourMomentum> finalBjet_list;


					// std::cout<<" ------------------- "<<std::endl;
					//foreach (const Jet& j, applyProjection<JetAlg>(event, "ANTIKT").jetsByPt(40.0*GeV))
					foreach (const Jet& j, applyProjection<FastJets>(event, "Jets").jetsByPt(30.0*GeV))
					{
						double jeta = j.momentum().eta();
						double jphi = j.momentum().phi();
						double jpt = j.momentum().pT();
						
						if ((fabs(jeta) < 2.4) && (jpt>30))
						{
							
							double leta = finalmuon.eta();
							double lphi = finalmuon.phi();
							double delta_phi = DeltaPhi(lphi,jphi);

							if( ((leta-jeta)*(leta-jeta) + (delta_phi*delta_phi)) > 0.5*0.5  )
							{
								finaljet_list.push_back(j.momentum());
								_htjets += fabs(1.0*(j.momentum()).pT());

								if (j.containsBottom())
								{	
									finalBjet_list.push_back(j.momentum());
									finaljet_list_btags.push_back(1);
								}
								else
								{
									finaljet_list_btags.push_back(0);
								}	
								// std::cout<<"   "<<jpt<<std::endl;
							}
							
						}
					}

					//Multiplicity plots.
					if(isWen)Fill(_histJetMultWelec, weight, finaljet_list);
					if(isWmn)Fill(_histJetMultWmu, weight, finaljet_list);
					if(isWmnPlus)Fill(_histJetMultWmuPlus, weight, finaljet_list);
					if(isWmnMinus)Fill(_histJetMultWmuMinus, weight, finaljet_list);
					if(isWenPlus)Fill(_histJetMultWelPlus, weight, finaljet_list);
					if(isWenMinus)Fill(_histJetMultWelMinus, weight, finaljet_list);
					if(isZee)Fill(_histJetMultZelec, weight, finaljet_list);
					if(isZmm)Fill(_histJetMultZmu, weight, finaljet_list);

					//if((isWmn)&&(finaljet_list.size()>=1)) std::cout<<finaljet_list[0].pT()<<std::endl;
					if((isWmn)&&(finaljet_list.size()>=1)) FillWithValue(_histJetPT1Wmu,weight,finaljet_list[0].pT());
					if((isWmn)&&(finaljet_list.size()>=2)) FillWithValue(_histJetPT2Wmu,weight,finaljet_list[1].pT());
					if((isWmn)&&(finaljet_list.size()>=3)) FillWithValue(_histJetPT3Wmu,weight,finaljet_list[2].pT());
					if((isWmn)&&(finaljet_list.size()>=4)) FillWithValue(_histJetPT4Wmu,weight,finaljet_list[3].pT());

					if((isWmn)&&(finaljet_list.size()>=1)) FillWithValue(_histJetETA1Wmu,weight,finaljet_list[0].eta());
					if((isWmn)&&(finaljet_list.size()>=2)) FillWithValue(_histJetETA2Wmu,weight,finaljet_list[1].eta());
					if((isWmn)&&(finaljet_list.size()>=3)) FillWithValue(_histJetETA3Wmu,weight,finaljet_list[2].eta());
					if((isWmn)&&(finaljet_list.size()>=4)) FillWithValue(_histJetETA4Wmu,weight,finaljet_list[3].eta());


					_njet_WMuNu = finaljet_list.size();
					_nBjet_WMuNu = finalBjet_list.size();
					//std::cout<<_njet_WMuNu<<" "<<_nBjet_WMuNu<<std::endl;




    			  	const MissingMomentum& met = applyProjection<MissingMomentum>(event, "MET");
   				   	_ptmet = met.visibleMomentum().pT();
   				   	_phimet = met.visibleMomentum().phi();
   				   	_phimet -= 3.1415926;
   				   	if (_phimet < 0.0) _phimet += 2.0*3.1415926;
					_mt_mumet = sqrt(2.0*_ptmuon*_ptmet*(1.0-cos(_phimet-_phimuon)));

					// std::cout<<_ptneutrino<<"  "<<_ptmet<<std::endl;
					// std::cout<<_phineutrino<<"  "<<_phimet<<std::endl;
					// std::cout<<_mt_munu<<"  "<<_mt_mumet<<std::endl;
					// std::cout<<"   ------------    "<<std::endl;

					if (finaljet_list.size()>0){
						_ptjet1=finaljet_list[0].pT();
						_etajet1=finaljet_list[0].eta();
						_phijet1=finaljet_list[0].phi();
						_isBjet1=finaljet_list_btags[0];
						_dphijet1muon = DeltaPhi(_phijet1,_phimuon);
					}

					if (finaljet_list.size()>1){
						_ptjet2=finaljet_list[1].pT();
						_etajet2=finaljet_list[1].eta();
						_phijet2=finaljet_list[1].phi();
						_isBjet2=finaljet_list_btags[1];
						_dphijet2muon = DeltaPhi(_phijet2,_phimuon);
					}

					if (finaljet_list.size()>2){
						_ptjet3=finaljet_list[2].pT();
						_etajet3=finaljet_list[2].eta();
						_phijet3=finaljet_list[2].phi();
						_isBjet3=finaljet_list_btags[2];
						_dphijet3muon = DeltaPhi(_phijet3,_phimuon);
					}

					if (finaljet_list.size()>3){
						_ptjet4=finaljet_list[3].pT();
						_etajet4=finaljet_list[3].eta();
						_phijet4=finaljet_list[3].phi();
						_isBjet4=finaljet_list_btags[3];
						_dphijet4muon = DeltaPhi(_phijet4,_phimuon);
					}

					if (finaljet_list.size()>4){
						_ptjet5=finaljet_list[4].pT();
						_etajet5=finaljet_list[4].eta();
						_phijet5=finaljet_list[4].phi();
						_isBjet5=finaljet_list_btags[4];
						_dphijet5muon = DeltaPhi(_phijet5,_phimuon);
					}
				//	std::cout<<_dphijet1muon<<" "<<_dphijet2muon<<" "<<_dphijet3muon<<" "<<_dphijet4muon<<" "<<_dphijet5muon<<" "<<std::endl;

				_rivetTree->Fill();

				}	



			}

			/// Normalise histograms etc., after the run
			void finalize()
			{
				FillNoverNm1(_histJetMultWelec,_histNoverNm1Welec);
				FillNoverN0(_histJetMultWelec,_histNoverN0Welec);
				FillNoverNm1(_histJetMultWmu,_histNoverNm1Wmu);
				FillNoverN0(_histJetMultWmu,_histNoverN0Wmu);
				FillNoverNm1(_histJetMultZelec,_histNoverNm1Zelec);
				FillNoverN0(_histJetMultZelec,_histNoverN0Zelec);
				FillNoverNm1(_histJetMultZmu,_histNoverNm1Zmu);
				FillNoverN0(_histJetMultZmu,_histNoverN0Zmu);
				FillChargeAssymHistogramSet(_histJetMultWmuPlus,_histJetMultWmuMinus, _histJetMultRatioWmuPlusMinus);
				FillChargeAssymHistogramSet(_histJetMultWelPlus,_histJetMultWelMinus, _histJetMultRatioWelPlusMinus);

				_rivetTree->Write();
				_treeFile->Close();
			}

		private:

			AIDA::IHistogram1D*  _histJetMultWelec;
								 // n/(n-1)
			AIDA::IDataPointSet* _histNoverNm1Welec;
								 // n/n(0)
			AIDA::IDataPointSet* _histNoverN0Welec;

			AIDA::IHistogram1D*  _histJetMultWmu;
								 // n/(n-1)
			AIDA::IDataPointSet* _histNoverNm1Wmu;
								 // n/n(0)
			AIDA::IDataPointSet* _histNoverN0Wmu;

			AIDA::IHistogram1D*  _histJetMultWelMinus;
			AIDA::IHistogram1D*  _histJetMultWelPlus;
			AIDA::IDataPointSet* _histJetMultRatioWelPlusMinus;

			AIDA::IHistogram1D*  _histJetMultWmuMinus;
			AIDA::IHistogram1D*  _histJetMultWmuPlus;
			AIDA::IDataPointSet* _histJetMultRatioWmuPlusMinus;

			AIDA::IHistogram1D*  _histJetMultZelec;
								 // n/(n-1)
			AIDA::IDataPointSet* _histNoverNm1Zelec;
								 // n/n(0)
			AIDA::IDataPointSet* _histNoverN0Zelec;

			AIDA::IHistogram1D*  _histJetMultZmu;
								 // n/(n-1)
			AIDA::IDataPointSet* _histNoverNm1Zmu;
								 // n/n(0)
			AIDA::IDataPointSet* _histNoverN0Zmu;
			
			AIDA::IHistogram1D*  _histJetPT1Wmu ;
			AIDA::IHistogram1D*  _histJetPT2Wmu ;
			AIDA::IHistogram1D*  _histJetPT3Wmu ;
			AIDA::IHistogram1D*  _histJetPT4Wmu ;

			AIDA::IHistogram1D*  _histJetETA1Wmu ;
			AIDA::IHistogram1D*  _histJetETA2Wmu ;
			AIDA::IHistogram1D*  _histJetETA3Wmu ;
			AIDA::IHistogram1D*  _histJetETA4Wmu ;

			TTree* _rivetTree;
			TString _treeFileName;
			TFile* _treeFile;

    		int _nevt; 
    		int _njet_WMuNu;
    		int _nBjet_WMuNu;

    		double _evweight;

			double _mt_munu;
			double _mt_mumet;
			double _htjets;
			double _ptmet;
			double _phimet;

    		double _ptmuon;
    		double _etamuon;
    		double _phimuon;

    		double _ptneutrino;
    		double _etaneutrino;
    		double _phineutrino;

    		double _ptjet1;
    		double _etajet1;
    		double _phijet1;
    		double _dphijet1muon;
			double _isBjet1;

    		double _ptjet2;
    		double _etajet2;
    		double _phijet2;
    		double _dphijet2muon;
			double _isBjet2;

    		double _ptjet3;
    		double _etajet3;
    		double _phijet3;
    		double _dphijet3muon;
			double _isBjet3;

    		double _ptjet4;
    		double _etajet4;
    		double _phijet4;
    		double _dphijet4muon;
			double _isBjet4;

    		double _ptjet5;
    		double _etajet5;
    		double _phijet5;
    		double _dphijet5muon;
			double _isBjet5;

    		int NZE;
    		int NZM;
    		int NWE; 
    		int NWM;
    		int NT;

	};

	AnalysisBuilder<CMS_WJets_TEST> plugin_CMS_WJets_TEST;

}
