#!/bin/sh


pdf=""
case $1 in
    0 ) pdf=CT10 ;;
    1 ) pdf=cteq6m ;;
    2 ) pdf=MSTW2008nlo68cl ;;
    3 ) pdf=NNPDF21_100 ;;
    4 ) pdf=cteq6ll ;;
esac

scales="_r1.0_f1.0"
if [ $# -ge 3 ] ; then
    scales=_r$2_f$3
fi

inhistsdir=hists_$pdf$scales
outhistsdir=hists_$pdf$scales

#mkdir $inhistsdir
#mv hists/W*${pdf}*${scales}*root $inhistsdir

samples="
Wm1j
Wm2j
Wm3j
Wm4j
Wp1j
Wp2j
Wp3j
Wp4j
"

for s in $samples ; do

    echo ./combineHistograms.exe -outfile $outhistsdir/${s}_all.root $inhistsdir/${s}_*list*.root
    ./combineHistograms.exe -outfile $outhistsdir/${s}_all.root $inhistsdir/${s}_*list*.root

done

exit 0
