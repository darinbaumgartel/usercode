import FWCore.ParameterSet.Config as cms

############################################################################
######## NOTES
############################################################################

# TO MAKE THIS WORK YOU NEED TO MODIFY IT TO LOOK FOR THE LOWEST UNPRESCALED TRIGGER.
# GET THIS PACKAGE: cvs co -r  CMSSW_4_2_5 PhysicsTools/TagAndProbe
# ^^ Of course, use your current cmssw version.
# Edit PhysicsTools/TagAndProbe/src/TriggerCandProducer.icc
# Force it to choose the first unprescaled trigger. Edit at line 137:
# Change:        ++numOKHLTPaths;
# To             ++numOKHLTPaths;  break;
#
#

############################################################################
######## STORE SOME ID VARIABLES 
############################################################################


MUON_RELISO = "(isolationR03.hadEt+isolationR03.emEt+isolationR03.sumPt) < 0.1 * pt"
MUON_TRKISO = "(isolationR03.sumPt) < 0.1 * pt"
MUON_ID = "(isGlobalMuon && globalTrack().normalizedChi2<10 && globalTrack().hitPattern().numberOfValidMuonHits>0 && numberOfMatchedStations>1  && track().hitPattern().numberOfValidPixelHits>0 && track().hitPattern().numberOfValidTrackerHits>10)"

MUON_TAGCOND = "("+MUON_RELISO+")&&"+MUON_ID + "&&(pt>40.0)&&(abs(eta)<2.1)"

JET_COLL = "ak5PFJets"
JET_CUTS = "abs(eta)<2.4 && chargedHadronEnergyFraction>0 && chargedEmEnergyFraction < 0.99 && chargedMuEnergyFraction<0.5 && chargedMultiplicity> 0 && nConstituents>1 && neutralHadronEnergyFraction<0.99 && neutralEmEnergyFraction<0.99 && pt>30.0" 

############################################################################


process = cms.Process("TagProbe")

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("Configuration.StandardSequences.Geometry_cff")
process.GlobalTag.globaltag = 'GR_P_V22::All'

######### EXAMPLE CFG 
###  A simple test of runnning T&P on Zmumu to determine muon isolation and identification efficiencies
###  More a showcase of the tool than an actual physics example

process.load('FWCore.MessageService.MessageLogger_cfi')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source("PoolSource", 
    fileNames = cms.untracked.vstring( INPUTROOTFILE )
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )    

## Tags. In a real analysis we should require that the tag muon fires the trigger, 
##       that's easy with PAT muons but not RECO/AOD ones, so we won't do it here
##       (the J/Psi example shows it)
process.tagMuons = cms.EDFilter("MuonRefSelector",
    src = cms.InputTag("muons"),
    cut = cms.string(MUON_TAGCOND), 
)
## Probes. Now we just use Tracker Muons as probes
process.probeMuons = cms.EDFilter("MuonRefSelector",
    src = cms.InputTag("muons"),
    cut = cms.string("isTrackerMuon && pt > 20"), 
)

## Here we show how to define passing probes with a selector
## although for this case a string cut in the TagProbeFitTreeProducer would be enough
process.probesPassingCal = cms.EDFilter("MuonRefSelector",
    src = cms.InputTag("muons"),
    cut = cms.string(process.probeMuons.cut.value() + " && caloCompatibility > 0.6"),
)


## Here we show how to use a module to compute an external variable
process.drToNearestJet = cms.EDProducer("DeltaRNearestJetComputer",
    probes = cms.InputTag("muons"),
       # ^^--- NOTA BENE: if probes are defined by ref, as in this case, 
       #       this must be the full collection, not the subset by refs.
    objects = cms.InputTag(JET_COLL),
    objectSelection = cms.string(JET_CUTS),
)

process.JetMultiplicityInEvent = cms.EDProducer("CandMultiplicityCounter",
    probes = cms.InputTag("muons"),
    objects = cms.InputTag(JET_COLL),
    objectSelection = cms.string(JET_CUTS),
 )


## Combine Tags and Probes into Z candidates, applying a mass cut
process.tpPairs = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string("tagMuons@+ probeMuons@-"), # charge coniugate states are implied
    cut   = cms.string("85 < mass < 100"),
)

## Match muons to MC
process.muMcMatch = cms.EDFilter("MCTruthDeltaRMatcherNew",
    pdgId = cms.vint32(13),
    src = cms.InputTag("muons"),
    distMin = cms.double(0.3),
    matched = cms.InputTag("genParticles")
)


CommonStuff = cms.PSet( addRunLumiInfo   =  cms.bool (True),)
 

HLTProcessName = "HLT"

TagBase = 'HLT_Mu'
Extensions = ['20','24','30','40','40_eta2p1']
VersionMax = 25
mytags = []

for ex in Extensions:
	mytags.append(TagBase+ex)
	for v in range(VersionMax+1):
		mytags.append(TagBase+ex+"_v"+str(v))

process.PassingHLT = cms.EDProducer("trgMatchedMuonProducer",    
    InputProducer = cms.InputTag( "probeMuons" ),  
    matchUnprescaledTriggerOnly = cms.untracked.bool(True),
    hltTags = cms.VInputTag(  [cms.InputTag(path, "", "HLT") for path in mytags] ),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
)



process.muonEffs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # pairs
    CommonStuff,
    tagProbePairs = cms.InputTag("tpPairs"),
    arbitration   = cms.string("OneProbe"),
    # variables to use
    variables = cms.PSet(
        ## methods of reco::Candidate
        eta = cms.string("eta"),
        pt  = cms.string("pt"),
        ## a method of the reco::Muon object (thanks to the 3.4.X StringParser)
        nsegm = cms.string("numberOfMatches"), 
        ## this one is an external variable
        drj = cms.InputTag("drToNearestJet"),
        jetcount = cms.InputTag("JetMultiplicityInEvent"),
    ),
    # choice of what defines a 'passing' probe
    flags = cms.PSet(
        ## one defined by an external collection of passing probes
        passingCal = cms.InputTag("probesPassingCal"), 
        ## two defined by simple string cuts
        passingGlb = cms.string("isGlobalMuon"),
        passingIso = cms.string(MUON_TRKISO),
        passingTight = cms.string(MUON_ID),
        passingHLT = cms.InputTag("PassingHLT"),
    ),
    # mc-truth info
    isMC = cms.bool(False),
    #motherPdgId = cms.vint32(22,23),
    #makeMCUnbiasTree = cms.bool(False),
    #checkMotherInUnbiasEff = cms.bool(False),
    #tagMatches = cms.InputTag("muMcMatch"),
    #probeMatches  = cms.InputTag("muMcMatch"),
    #allProbes     = cms.InputTag("probeMuons"),
)
##    ____       _   _     
##   |  _ \ __ _| |_| |__  
##   | |_) / _` | __| '_ \ 
##   |  __/ (_| | |_| | | |
##   |_|   \__,_|\__|_| |_|
##                         
process.tagAndProbe = cms.Path( 
    (process.tagMuons + process.probeMuons) *   # 'A*B' means 'B needs output of A'; 
    (process.probesPassingCal +                 # 'A+B' means 'if you want you can re-arrange the order'
     process.drToNearestJet   +
     process.PassingHLT + 
     process.JetMultiplicityInEvent      +
     process.tpPairs )*#+
     #process.muMcMatch) *
    process.muonEffs
)

process.TFileService = cms.Service("TFileService", fileName = cms.string( THISROOTFILE ))




