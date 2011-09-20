#!/bin/csh
cd MYPWD
eval `scramv1 runtime -csh`
cd -
sleep 5
cp MYPWD/RunStatsCombo.py .
cp MYPWD/combineCards.py .
python RunStatsCombo.py --do_mumu MYOPTIONS
sleep 5
cp ComboLog*txt /afs/cern.ch/user/d/darinb/scratch0/LimitCombinationHiggs/CMSSW_4_1_3/src
