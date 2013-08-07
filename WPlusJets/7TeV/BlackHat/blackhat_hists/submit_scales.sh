#!/bin/sh

exe=./runList_batch.sh

list=`ls lists/split/*list_??`

pdf=CT10.LHgrid


#for ren in 0.5 1.0 2.0 ; do
#for ren in  2.0 ; do
#for fac in 0.5 1.0 2.0 ; do
 
ren=$1
fac=$1
    
for l in $list ; do
    
    job=`basename $l`
    echo ./submitBatch.perl $job $exe $l $pdf $ren $fac
    ./submitBatch.perl $job $exe $l $pdf $ren $fac
    sleep 1
    wait_bjobs 8 darinb 60
    
done
#done
#done

exit 0
