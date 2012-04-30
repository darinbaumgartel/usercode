#!/bin/bash

source  setupRivetProf.sh 

#rm /tmp/darinb/hepmc.fifo
#mkfifo /tmp/$USER/hepmc.fifo
#agile-runmc Pythia6:424 --beams=LHC:7000 -n 2000 -o /tmp/$USER/hepmc.fifo &
#rivet -a MC_GENERIC /tmp/$USER/hepmc.fifo

#compare-histos Rivet.aida
#make-plots --pdfpng *.dat

rivet-mkanalysis MY_TEST_ANALYSIS
rivet-buildplugin RivetMyTest.so MY_TEST_ANALYSIS.cc -m32

export RIVET_ANALYSIS_PATH=$PWD
