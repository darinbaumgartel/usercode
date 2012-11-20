#!/bin/tcsh


# For up to 2012C

set LumiJSON=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Prompt/Cert_190456-204601_8TeV_PromptReco_Collisions12_JSON.txt

set PUJSON=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/PileUp/pileup_JSON_DCSONLY_190389-206102_corr.txt


# Set up CMSSW and get pileupCalc.py

scram project -n CMSSW_6_0_1_PUCALC CMSSW_6_0_1
cd CMSSW_6_0_1_PUCALC/src
cmsenv

cvs co RecoLuminosity/LumiDB/scripts
scramv1 b -j 16
cd RecoLuminosity/LumiDB/scripts

lumiCalc2.py -i $LumiJSON overview  > LumiLog.txt 

./pileupCalc.py -i $LumiJSON --inputLumiJSON $PUJSON --calcMode true --minBiasXsec 69400 --maxPileupBin 60 --numPileupBins 60 PU_Central.root

./pileupCalc.py -i $LumiJSON --inputLumiJSON $PUJSON --calcMode true --minBiasXsec 73564 --maxPileupBin 60 --numPileupBins 60 PU_Up.root

./pileupCalc.py -i $LumiJSON --inputLumiJSON $PUJSON --calcMode true --minBiasXsec 65236 --maxPileupBin 60 --numPileupBins 60 PU_Down.root

mv LumiLog.txt ../../../../../
mv PU*root ../../../../../
cd ../../../../../
rm -r CMSSW_6_0_1_PUCALC


