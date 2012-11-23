#!/bin/tcsh


# Set up CMSSW
scram project -n CMSSW_6_0_1_PUCALC CMSSW_6_0_1
cd CMSSW_6_0_1_PUCALC/src
cmsenv

cvs co RecoLuminosity/LumiDB/scripts
scramv1 b -j 16
cd RecoLuminosity/LumiDB/scripts

# Create Good JSON File For up to 2012C

set json2012AJul13=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_v2.txt
set json2012AAug06Recover=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190782-190949_8TeV_06Aug2012ReReco_Collisions12_JSON.txt
set json2012B13Jul=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_v2.txt
set json2012CReReco=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_198022-198523_8TeV_24Aug2012ReReco_Collisions12_JSON.txt
set json2012CPrompt=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Prompt/Cert_190456-203002_8TeV_PromptReco_Collisions12_JSON_v2.txt

mergeJSON.py $json2012AJul13  $json2012AAug06Recover $json2012B13Jul $json2012CReReco  $json2012CPrompt --output=CustomJson2012ABC.txt



# Set the LumiJSON and PUJSON for PU Calculations
set LumiJSON=CustomJson2012ABC.txt

set PUJSON=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/PileUp/pileup_JSON_DCSONLY_190389-206102_corr.txt


# Set up CMSSW and get pileupCalc.py


lumiCalc2.py -i $LumiJSON overview  > LumiLog.txt 

./pileupCalc.py -i $LumiJSON --inputLumiJSON $PUJSON --calcMode true --minBiasXsec 69400 --maxPileupBin 60 --numPileupBins 60 PU_Central.root

./pileupCalc.py -i $LumiJSON --inputLumiJSON $PUJSON --calcMode true --minBiasXsec 73564 --maxPileupBin 60 --numPileupBins 60 PU_Up.root

./pileupCalc.py -i $LumiJSON --inputLumiJSON $PUJSON --calcMode true --minBiasXsec 65236 --maxPileupBin 60 --numPileupBins 60 PU_Down.root

mv LumiLog.txt ../../../../../
mv PU*root ../../../../../
cd ../../../../../
rm -r CMSSW_6_0_1_PUCALC


