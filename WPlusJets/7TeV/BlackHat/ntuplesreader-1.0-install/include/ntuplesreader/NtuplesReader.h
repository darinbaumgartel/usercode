/*
 * NtuplesReader.h
 *
 *  Created on: Feb 13, 2012
 *      Author: daniel
 */

#ifndef NTUPLESREADER_H_
#define NTUPLESREADER_H_

#include "EventReaderBase.h"
#include <string>
#include <vector>
#include <iostream>


using namespace std;

class NtupleReader : public RootFileReaderBase {
	int d_member;
	short d_alphasPower;
	char d_part[2];
	bool d_useProperStats;
protected:
	NtupleInfo<MAX_NBR_PARTICLES> d_NI;
public:
	//! Constructor for a NtuplesReader object
	NtupleReader();
	/** Reads the next event and returns true in case of success, false otherwise
	(including when the end of the file is reached )*/
	bool nextEvent(){return readNextEvent(d_NI);};
	/** Sets the pdf set to be used.
	\param name is the name of the file to be loaded by LHAPDF. For example "CT10.LHgrid"
	*/
	void setPDF(const std::string& name);
	/** Sets the pdf member to be used.
	\param member is an integer labelling the member. Typically 0 is used for the central value.
	*/
	void setPDFmember(int member);
	/** Returns the ID of the event.
	*/
	int getID(){return d_NI.id;}
	/** Returns the number of final state particles in the event.
	*/
	int getParticleNbr(){return d_NI.nparticle;}
	/** Returns the energy of the i-th particle (0-based).
		\param i 0-based index
		Note that an argument larger than the number of final state
		particle will either return an unexpected value or result in a segmentation
		fault.
	*/
	double getEnergy(int i){return d_NI.E[i];};
	/** Returns the x component of the i-th particle (0-based).
		\param i 0-based index
		Note that an argument larger than the number of final state
		particle will either return an unexpected value or result in a segmentation
		fault.
	*/
	double getX(int i){return d_NI.px[i];};
	/** Returns the y component of the i-th particle (0-based).
		\param i 0-based index
		Note that an argument larger than the number of final state
		particle will either return an unexpected value or result in a segmentation
		fault.
	*/
	double getY(int i){return d_NI.py[i];};
	/** Returns the z component of the i-th particle (0-based).
		\param i 0-based index
		Note that an argument larger than the number of final state
		particle will either return an unexpected value or result in a segmentation
		fault.
	*/
	double getZ(int i){return d_NI.pz[i];};
	/** Returns the PDG code of the i-th particle (0-based).
		\param i 0-based index
		Note that an argument larger than the number of final state
		particle will either return an unexpected value or result in a segmentation
		fault.
	*/
	int getPDGcode(int i){return d_NI.kf[i];}
	/** Returns the power of the strong coupling constant.
	*/
	int getAlphasPower(){return d_alphasPower;}
	/** Returns the renormalisation scale used to compute the the weights for the current event.
	*/
	double getRenScale(){return d_NI.muR;}
	/** Returns the factorisation scale used to compute the the weights for the current event.
	*/
	double getFacScale(){return d_NI.muF;}
	/** Returns the weight for the current event.
	*/
	double getWeight(){return d_NI.wgt;}
	/** Returns the weight for the current event, that has to be used with the
	 * procedure described in the documentation to obtain the right statistical error.
	*/
	double getWeight2(){return d_NI.wgt2;}
	/** Returns the weight for the current event without pdf factors.
	*/
	double getMEWeight(){return d_NI.me_wgt;}
	/** Returns the weight for the current event without the pdf factors, that has to be used with the
	 * procedure described in the documentation to obtain the right statistical error.
	*/
	double getMEWeight2(){return d_NI.me_wgt2;}
	/** Returns the type of contribution. 'B' for born, 'I' for integrated subtraction,
	 * 'V' for the virtual part, 'R' for the real part (+ subtraction)
	*/
	char getPart(){return d_part[0];}
	/** Returns the weight recomputed for the new scales, using the current pdf set with the current number
	 * \param newFacScale new factorisation scale (in GeV)
	 * \param newRenScale new renormalisation scale (in GeV)
	*/
	double computeWeight(double newFacScale,double newRenScale);
	/** Sets whether to use the procedure to obtain a meaningful statistical error. Called with no argument
	 * switches the treatment of the statistical error on.
	 * \param doUse sets whether to use the weights adapted to the statistical error. */
	void useProperStats(bool doUse=true){d_useProperStats=doUse;}
	/** Sets the initial state to proton-proton
	 * */
	void setPP();
	/** Sets the initial state to proton-antiproton
	 * */
	void setPPbar();
	//! Destructor
	virtual ~NtupleReader(){};
};



#endif /* NTUPLESREADER_H_ */
