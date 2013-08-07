#ifndef _H_EVENTREADERBASE_H
#define _H_EVENTREADERBASE_H

#include "NtupleInfo.h"



class RootFileReaderBase  {
	long d_startEvent;
	long d_endEvent;
	long d_iEntry;
	long d_maxTrueEvent;
protected:
	TChain* d_fin ;
public:
	//! Constructor
	RootFileReaderBase(NtupleInfo<MAX_NBR_PARTICLES>& NI,const std::string& treeName="t3");
	/** Reads the next event and returns true in case of success, false otherwise
	(including when the end of the file is reached )*/
	bool readNextEvent(NtupleInfo<MAX_NBR_PARTICLES>& NI);
	/** Sets the number of the event at which reading will start.
	 * */
	void setStartEvent(long i){d_startEvent=i;d_iEntry = d_startEvent;};
	/** Sets the number of the event at which reading will stop.
	 * */
	void setEndEvent(long i){d_endEvent=i;};
	/** Sets the number of the event-counter-event groups at which reading will stop,
	 * that is this event will not be read. If startEvent=0 and endEvent=1, only one event
	 * will be read. The number of events being read is therefore endEvent-startEvent
	 * */
	void setMaxTrueEvent(long i){d_maxTrueEvent=i;};
	/** Returns the number of the event at which reading will start.
	 * */
	long getStartEvent(){return d_startEvent;	};
	/** Returns the number of the event at which reading will stop.
	 * */
	long getEndEvent(){return d_endEvent;};
	/** Returns the number of events-counter-event groups after which reading will stop.
	 * */
	long getMaxTrueEvent(){return d_maxTrueEvent;};
	/** Returns the total number of entries
	 * */
	long getNumberOfEntries();
	/** Reads the entry corresponding to the index @param i. readNext() will start from that position.
	 \param i index of the event to be read
	 * */
	void getEntry(long i);
	/** returns the index of the next entry
	 * */
	long getINextEntry(){return d_iEntry;};
	/** Adds a file to the reader
	 * \param fileName is the name of the file
	 * */
	void addFile(const std::string& fileName);
	/** Adds a list of files to the reader
	 * \param fileNames is a vector of std::string containing the names of the files to be added.
	 * */
	void addFiles(std::vector<std::string> fileNames);
	virtual ~RootFileReaderBase();
};


#endif /* _H_EVENTREADERBASE_H */
