import FWCore.ParameterSet.Config as cms


MUON_RELISO = "(isolationR03.hadEt+isolationR03.emEt+isolationR03.sumPt) < 0.1 * pt"
MUON_TRKISO = "(isolationR03.sumPt) < 0.1 * pt"
MUON_ID = "(isGlobalMuon && globalTrack().normalizedChi2<10 && globalTrack().hitPattern().numberOfValidMuonHits>0 && numberOfMatchedStations>1  && track().hitPattern().numberOfValidPixelHits>0 && track().hitPattern().numberOfValidTrackerHits>10)"

MUON_TAGCOND = "("+MUON_RELISO+")&&"+MUON_ID + "&&(pt>40.0)&&(abs(eta)<2.1)"

process = cms.Process("TagProbe")

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("Configuration.StandardSequences.Geometry_cff")
process.GlobalTag.globaltag = 'GR_P_V22::All'

######### EXAMPLE CFG 
###  A simple test of runnning T&P on Zmumu to determine muon isolation and identification efficiencies
###  More a showcase of the tool than an actual physics example

process.load('FWCore.MessageService.MessageLogger_cfi')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.source = cms.Source("PoolSource", 
    fileNames = cms.untracked.vstring(
#'rfio:///castor/cern.ch/user/d/darinb/RECO_AOD_Examples/SingleMu_2011B_Prompt_1.root'    
'rfio:///castor/cern.ch/user/d/darinb/RECO_AOD_Examples/SingleMu_2011B_Prompt_1.root')
 #'file:///tmp/darinb/SingleMu_2011B_Prompt_1.root')
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(2000) )    

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

JET_COLL = "ak5PFJets"
JET_CUTS = "abs(eta)<2.4 && chargedHadronEnergyFraction>0 && chargedEmEnergyFraction < 0.99 && chargedMuEnergyFraction<0.5 && chargedMultiplicity> 0 && nConstituents>1 && neutralHadronEnergyFraction<0.99 && neutralEmEnergyFraction<0.99 && pt>30.0" 

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


CommonStuff = cms.PSet(
   addRunLumiInfo   =  cms.bool (True),
)
 

#HLTPathpt40 = "HLT_Mu40"
#HLTPathpt40vE = "HLT_Mu40_eta2p1"

#HLTPathpt40vE0 = "HLT_Mu40_eta2p1_v0"
#HLTPathpt40vE1 = "HLT_Mu40_eta2p1_v1"
#HLTPathpt40vE2 = "HLT_Mu40_eta2p1_v2"
#HLTPathpt40vE3 = "HLT_Mu40_eta2p1_v3"
#HLTPathpt40vE4 = "HLT_Mu40_eta2p1_v4"
#HLTPathpt40vE5 = "HLT_Mu40_eta2p1_v5"
#HLTPathpt40vE6 = "HLT_Mu40_eta2p1_v6"
#HLTPathpt40vE7 = "HLT_Mu40_eta2p1_v7"
#HLTPathpt40vE8 = "HLT_Mu40_eta2p1_v8"

#HLTPathpt40v0 = "HLT_Mu40_v0"
#HLTPathpt40v1 = "HLT_Mu40_v1"
#HLTPathpt40v2 = "HLT_Mu40_v2"
#HLTPathpt40v3 = "HLT_Mu40_v3"
#HLTPathpt40v4 = "HLT_Mu40_v4"
#HLTPathpt40v5 = "HLT_Mu40_v5"
#HLTPathpt40v6 = "HLT_Mu40_v6"
#HLTPathpt40v7 = "HLT_Mu40_v7"
#HLTPathpt40v8 = "HLT_Mu40_v8"

HLTProcessName = "HLT"
#print run
##hltKey = GetHltKeyForRun(0)
#hltConfig = GetHltConfiguration(hltKey)

process.PassingHLT = cms.EDProducer("trgMatchedMuonProducer",    
    InputProducer = cms.InputTag( "probeMuons" ),  
    matchUnprescaledTriggerOnly = cms.untracked.bool(False),
    allowMultipleTriggers_ = cms.untracked.bool(True),
    #hltTags = cms.VInputTag(
        #[cms.InputTag(path, "", "HLT") for path in process.filterConfig.hltPaths]),    
                            
	#hltTags = ('HLT_Mu'),
    hltTags = cms.VInputTag(
        cms.InputTag("HLT_Mu40_eta2p1_v1","", HLTProcessName),       

        #cms.InputTag("HLT_Mu40","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v0","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v1","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v2","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v3","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v4","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v5","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v6","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v7","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v8","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v9","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v0","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v1","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v2","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v3","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v4","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v5","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v6","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v7","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_v8","", HLTProcessName),   
        #cms.InputTag("HLT_Mu40_eta2p1","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_eta2p1_v0","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_eta2p1_v1","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_eta2p1_v2","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_eta2p1_v3","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_eta2p1_v4","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_eta2p1_v5","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_eta2p1_v6","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_eta2p1_v7","", HLTProcessName),       
        #cms.InputTag("HLT_Mu40_eta2p1_v8","", HLTProcessName),       
        #cms.InputTag("HLT_Mu20_v1","", HLTProcessName), 
        #cms.InputTag("HLT_Mu20_v2","", HLTProcessName), 
        #cms.InputTag("HLT_Mu20_v3","", HLTProcessName), 
        #cms.InputTag("HLT_Mu20_v4","", HLTProcessName), 
        #cms.InputTag("HLT_Mu24_v1","", HLTProcessName), 
        #cms.InputTag("HLT_Mu24_v2","", HLTProcessName), 
        #cms.InputTag("HLT_Mu24_v3","", HLTProcessName), 
        #cms.InputTag("HLT_Mu24_v4","", HLTProcessName),         
        #cms.InputTag("HLT_Mu30_v1","", HLTProcessName), 
        #cms.InputTag("HLT_Mu30_v2","", HLTProcessName), 
        #cms.InputTag("HLT_Mu30_v3","", HLTProcessName), 
        #cms.InputTag("HLT_Mu30_v4","", HLTProcessName),                   
    ),
    triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
)

#process.PassingHLTpt40 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40v0 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40v0,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40v1 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40v1,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40v2 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40v2,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40v3 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40v3,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40v4 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40v4,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40v5 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40v5,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40v6 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40v6,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40v7 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40v7,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40v8 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40v8,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40vE = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40vE,"", HLTProcessName),        
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40vE0 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40vE0,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40vE1 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40vE1,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40vE2 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40vE2,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40vE3 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40vE3,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40vE4 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40vE4,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40vE5 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40vE5,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40vE6 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40vE6,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40vE7 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40vE7,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)


#process.PassingHLTpt40vE8 = cms.EDProducer("trgMatchedMuonProducer",    
    #InputProducer = cms.InputTag( "probeMuons" ),                          
    #hltTags = cms.VInputTag(
        #cms.InputTag(HLTPathpt40vE8,"", HLTProcessName),       
    #),
    #triggerEventTag = cms.untracked.InputTag("hltTriggerSummaryAOD","",HLTProcessName),
    #triggerResultsTag = cms.untracked.InputTag("TriggerResults","",HLTProcessName)   
#)








## Make the tree


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
        #passingHLTpt40 = cms.InputTag("PassingHLTpt40"),     
        #passingHLTpt40vE = cms.InputTag("PassingHLTpt40vE"),     
        #passingHLTpt40v0 = cms.InputTag("PassingHLTpt40v0"),     
        #passingHLTpt40v1 = cms.InputTag("PassingHLTpt40v1"),     
        #passingHLTpt40v2 = cms.InputTag("PassingHLTpt40v2"),     
        #passingHLTpt40v3 = cms.InputTag("PassingHLTpt40v3"),     
        #passingHLTpt40v4 = cms.InputTag("PassingHLTpt40v4"),     
        #passingHLTpt40v5 = cms.InputTag("PassingHLTpt40v5"),     
        #passingHLTpt40v6 = cms.InputTag("PassingHLTpt40v6"),     
        #passingHLTpt40v7 = cms.InputTag("PassingHLTpt40v7"),     
        #passingHLTpt40v8 = cms.InputTag("PassingHLTpt40v8"),     
        #passingHLTpt40vE0 = cms.InputTag("PassingHLTpt40vE0"),     
        #passingHLTpt40vE1 = cms.InputTag("PassingHLTpt40vE1"),     
        #passingHLTpt40vE2 = cms.InputTag("PassingHLTpt40vE2"),     
        #passingHLTpt40vE3 = cms.InputTag("PassingHLTpt40vE3"),     
        #passingHLTpt40vE4 = cms.InputTag("PassingHLTpt40vE4"),     
        #passingHLTpt40vE5 = cms.InputTag("PassingHLTpt40vE5"),     
        #passingHLTpt40vE6 = cms.InputTag("PassingHLTpt40vE6"),     
        #passingHLTpt40vE7 = cms.InputTag("PassingHLTpt40vE7"),     
        #passingHLTpt40vE8 = cms.InputTag("PassingHLTpt40vE8"),   

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
     #process.PassingHLTpt40 + 
     #process.PassingHLTpt40v0 + 
     #process.PassingHLTpt40v1 + 
     #process.PassingHLTpt40v2 + 
     #process.PassingHLTpt40v3 + 
     #process.PassingHLTpt40v4 + 
     #process.PassingHLTpt40v5 + 
     #process.PassingHLTpt40v6 + 
     #process.PassingHLTpt40v7 + 
     #process.PassingHLTpt40v8 + 
     #process.PassingHLTpt40vE + 

     #process.PassingHLTpt40vE0 + 
     #process.PassingHLTpt40vE1 + 
     #process.PassingHLTpt40vE2 + 
     #process.PassingHLTpt40vE3 + 
     #process.PassingHLTpt40vE4 + 
     #process.PassingHLTpt40vE5 + 
     #process.PassingHLTpt40vE6 + 
     #process.PassingHLTpt40vE7 + 
     #process.PassingHLTpt40vE8 + 

	process.JetMultiplicityInEvent      +
     process.tpPairs )*#+
     #process.muMcMatch) *
    process.muonEffs
)

process.TFileService = cms.Service("TFileService", fileName = cms.string("testTagProbeFitTreeProducer_ZMuMu.root"))




