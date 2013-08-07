#!/bin/sh

exe=./runList_batch.sh

#list=`ls lists/split/Wp2*list_??`
#list=`ls lists/split/Wm3j*real*list_??`
#list=`ls lists/split/Wp2*real*list_00`
list=`ls lists/split/*list_??`

ren=1.0
fac=1.0

pdf=CT10.LHgrid
case $1 in
    0 ) pdf=CT10.LHgrid ;;
    1 ) pdf=cteq6m.LHpdf ;;
    2 ) pdf=MSTW2008nlo68cl.LHgrid ;;
    3 ) pdf=NNPDF21_100.LHgrid ;;
    4 ) pdf=cteq6ll.LHpdf ;;
esac

echo "pdf = $pdf"

for l in $list ; do

    job=`basename $l`
    echo ./submitBatch.perl $job $exe $l $pdf $ren $fac
    ./submitBatch.perl $job $exe $l $pdf $ren $fac
    sleep 1
    wait_bjobs 8 USERNAME 60

done

exit 0
