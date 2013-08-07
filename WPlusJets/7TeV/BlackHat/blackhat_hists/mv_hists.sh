#!/bin/sh

for n in  `ls hists/Wp4j_born.list_00_*root` ; do

    pdf=` echo $n | sed 's#.*list_00_##' | sed 's#\.LH.*##' `
    scales=` echo $n | sed 's#.*_r#_r#' | sed 's#\.root*##' `

    newdir=hists_${pdf}${scales}
    mkdir $newdir
    mv hists/*${pdf}*${scales}* $newdir
    
done
