
import FWCore.ParameterSet.Config as cms

process = cms.Process("runRivetAnalysis")

process.load('Configuration.StandardSequences.Services_cff')
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(10000)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:SourceFile')
)

process.GlobalTag.globaltag = 'MC_60_V4::All'


process.load("GeneratorInterface.RivetInterface.rivetAnalyzer_cfi")

process.rivetAnalyzer.AnalysisNames = cms.vstring('CMS_LQ_TEST')

process.p = cms.Path(process.rivetAnalyzer)

