#!/bin/sh


hadd ZJets.root *Z*Jets*root    

hadd WJets.root *WJets*root     

hadd TTBar.root *TTJet*root

hadd SingleTop.root *TToBLNu*root

hadd VV.root *WW*root *WZ*root *ZZ*root

hadd GJets.root *GJets*

hadd QCDMu.root *QCD*root

hadd SingleMuMay10ReReco.root *SingleMu*root

mkdir SummaryFiles

mv SingleTop.root QCDMu.root TTBar.root VV.root SingleMuMay10ReReco.root ZJets.root WJets.root GJets.root SummaryFiles
