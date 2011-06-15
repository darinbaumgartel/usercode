# The following comments couldn't be translated into the new config version:

# Configuration file for EventSetupTest_t

import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")
process.PoolDBESSource = cms.ESSource("PoolDBESSource",
    loadAll = cms.bool(True),
    timetype = cms.string('runnumber'),
    toGet = cms.VPSet(cms.PSet(
        record = cms.string('CSCDBGainsRcd'),
        tag = cms.string('CSCDBGains_express')
    )),
    #read from sqlite_file
     connect = cms.string('frontier://FrontierInt/CMS_COND_31X_FRONTIER'),
    #connect=cms.string("oracle://cms_orcon_prod/CMS_COND_31X_CSC"),
    # read from database
    #connect="frontier://FrontierDev/CMS_COND_CSC"
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string('/nfshome0/popcondev/conddb/'),
        authenticationMethod = cms.untracked.uint32(1)
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.prod = cms.EDAnalyzer("CSCGainsDBReadAnalyzer")

process.output = cms.OutputModule("AsciiOutputModule")

process.p = cms.Path(process.prod)
process.ep = cms.EndPath(process.output)

