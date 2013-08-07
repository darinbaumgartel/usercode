#!/bin/sh

for f in `ls *loop*list` ; do split -d -l 20 $f ${f}_ ; done

for f in `ls *real*list` ; do split -d -l 5 $f ${f}_ ; done

for f in `ls *vsub*list` ; do split -d -l 10 $f ${f}_ ; done

for f in `ls *born*list` ; do split -d -l 10 $f ${f}_ ; done
