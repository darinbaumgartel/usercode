#!/bin/tcsh


# Set up CMSSW
rm -r CMSSW_6_0_1_PUCALC
scram project -n CMSSW_6_0_1_PUCALC CMSSW_6_0_1
cd CMSSW_6_0_1_PUCALC/src
cmsenv

cvs co RecoLuminosity/LumiDB/scripts
scramv1 b -j 16
cd RecoLuminosity/LumiDB/scripts

###################################################################
# Create Good JSON File For up to 2012C
# https://twiki.cern.ch/twiki/bin/view/CMS/PdmV2012Analysis#Analysis_based_on_CMSSW_5_3_X_re
###################################################################

# Run2012A-13Jul2012 	190456 	193621 	JSON file 	*Run2012A-13Jul2012*/RECO
set json2012AJul13=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_v2.txt
filterJSON.py $json2012AJul13 --min 190456 --max 193621 --output json2012AJul13_skim.json

# Run2012A-recover-06Aug2012 	190782 	190949 	JSON file 	*Run2012A-06Aug2012*/RECO
set json2012AAug06Recover=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190782-190949_8TeV_06Aug2012ReReco_Collisions12_JSON.txt
filterJSON.py $json2012AAug06Recover --min 190782 --max 190949 --output json2012AAug06Recover_skim.json

# Run2012B-13Jul2012 	193833 	196531 	JSON file 	*Run2012B-13Jul2012*/RECO
set json2012B13Jul=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_v2.txt
filterJSON.py $json2012B13Jul --min 193833 --max 196531 --output json2012B13Jul_skim.json

# Run2012C-ReReco ( ) 	198022 	198913 	JSON file 	*Run2012C*24Aug*/RECO
set json2012CReReco=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_198022-198523_8TeV_24Aug2012ReReco_Collisions12_JSON.txt
filterJSON.py $json2012CReReco --min 198022 --max 198913 --output json2012CReReco_skim.json

# Run2012C-PromptReco-v2 (**) 	198934 	203746 	JSON file 	*Run2012C-PromptReco-v2*/RECO
set json2012CPrompt=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Prompt/Cert_190456-203002_8TeV_PromptReco_Collisions12_JSON_v2.txt
filterJSON.py $json2012CPrompt --min 198934 --max 203746 --output json2012CPrompt_skim.json

# Run2012C-EcalRecover_11Dec2012 	201191 	201191 	JSON file 	Run2012C-EcalRecover_11Dec*/RECO
set json2012CEcalReReco=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Reprocessing/Cert_201191-201191_8TeV_11Dec2012ReReco-recover_Collisions12_JSON.txt
filterJSON.py $json2012CEcalReReco --min 201191 --max 201191 --output json2012CEcalReReco_skim.json

# Run2012D-PromptReco-v1 	203768 	208686 	see below 	*Run2012D-PromptReco-v1*/RECO
set json2012DPrompt=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/Prompt/Cert_190456-208686_8TeV_PromptReco_Collisions12_JSON.txt 
filterJSON.py $json2012DPrompt --min 203768 --max 208686 --output json2012DPrompt_skim.json

mergeJSON.py  json2012AJul13_skim.json json2012AAug06Recover_skim.json json2012B13Jul_skim.json json2012CReReco_skim.json json2012CPrompt_skim.json json2012CEcalReReco_skim.json json2012DPrompt_skim.json --output=CustomJson2012ABCD.txt


###################################################################
# Integrated Luminosity and Pileup Calculation
# https://twiki.cern.ch/twiki/bin/view/CMS/PdmV2012Analysis#Analysis_based_on_CMSSW_5_3_X_re
###################################################################

# Set the LumiJSON and PUJSON for PU Calculations
set LumiJSON=CustomJson2012ABCD.txt

set PUJSON=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions12/8TeV/PileUp/pileup_JSON_DCSONLY_190389-208686_corr.txt

lumiCalc2.py -i $LumiJSON overview  > LumiLog.txt 

./pileupCalc.py -i $LumiJSON --inputLumiJSON $PUJSON --calcMode true --minBiasXsec 69400 --maxPileupBin 60 --numPileupBins 60 PU_Central.root

./pileupCalc.py -i $LumiJSON --inputLumiJSON $PUJSON --calcMode true --minBiasXsec 73564 --maxPileupBin 60 --numPileupBins 60 PU_Up.root

./pileupCalc.py -i $LumiJSON --inputLumiJSON $PUJSON --calcMode true --minBiasXsec 65236 --maxPileupBin 60 --numPileupBins 60 PU_Down.root

mv CustomJson2012ABCD.txt ../../../../../
mv *skim.json ../../../../../
mv LumiLog.txt ../../../../../
mv PU*root ../../../../../
cd ../../../../../
rm -r CMSSW_6_0_1_PUCALC

echo "Done!"
