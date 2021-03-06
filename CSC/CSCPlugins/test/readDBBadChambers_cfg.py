# The following comments couldn't be translated into the new config version:

# Configuration file for EventSetupTest_t

import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")
process.PoolDBESSource = cms.ESSource("PoolDBESSource",
    loadAll = cms.bool(True),
    timetype = cms.string('runnumber'),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('CSCBadChambersRcd'),
        #tag = cms.string('CSCBadChambers_none_FiveLiveME42')
        tag = cms.string('CSCBadChambers_prompt')

    )),
    #read from sqlite_file
    #connect=cms.string("oracle://cms_orcon_prod/CMS_COND_31X_CSC"),
     connect = cms.string('frontier://PromptProd/CMS_COND_31X_CSC'),	
    #connect = cms.string('sqlite_file:CSCBadChambers_04March2011_V2.db'),
    # read from database
    #connect=cms.string("frontier://FrontierDev/CMS_COND_CSC"),
    #connect =  cms.string("oracle://cms_orcoff_prep/CMS_COND_CSC"),
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb'),
        authenticationMethod = cms.untracked.uint32(1)
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.analyze = cms.EDAnalyzer("CSCReadBadChambersAnalyzer",
                              outputToFile = cms.bool(True),                           
                              readBadChambers = cms.bool(True),
                              me42installed = cms.bool(True)
)

process.output = cms.OutputModule("AsciiOutputModule")

process.p = cms.Path(process.analyze)
process.ep = cms.EndPath(process.output)

