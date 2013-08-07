#!/bin/sh

echo "==============================="
echo -n "START: "
date

if [ $# -lt 1 ] ; then
    echo "Need a list file"
    exit 1
fi
listfile=$1

pdf=cteq6ll.LHpdf
if [ $# -gt 1 ] ; then
    pdf=$2
fi

ren=1.0
if [ $# -gt 2 ] ; then
    ren=$3
fi

fac=1.0
if [ $# -gt 3 ] ; then
    fac=$4
fi

. ~/.bashrc
. ./setup.sh

#dir=BHSNtuples_mnt
dir=$BATCHDIR
histsdir=hists
logsdir=logs

echo $dir

echo -n "COPY: "
date

echo "Copying blackhat files: "
for f in `cat $listfile` ; do
    to=$dir/`basename $f`
    echo scp neu.cern.ch:/mnt/3TB/jhaley/Blackhat_ntuples/$f $to
    scp neu.cern.ch:/mnt/3TB/jhaley/Blackhat_ntuples/$f $to
    ls -l $to
    list="$list  $to"
done


if ! [ -d $histsdir ] ; then 
    echo "mkdir -p $histsdir"
    mkdir -p $histsdir
fi
if ! [ -d $logsdir ] ; then 
    echo "mkdir -p $logsdir"
    mkdir -p $logsdir
fi

outname=$histsdir/`basename $listfile`_${pdf}_r${ren}_f${fac}.root
log=$logsdir/`basename $listfile`_${pdf}_r${ren}_f${fac}.log

echo -n "RUN: "
date

# run the list
echo ./makeHistograms.exe -outfile $outname -pdf $pdf -ren $ren -fac $fac $list
./makeHistograms.exe -outfile $outname -pdf $pdf -ren $ren -fac $fac $list >& $log 

echo -n "DONE: "
date
echo "==============================="

exit 0
