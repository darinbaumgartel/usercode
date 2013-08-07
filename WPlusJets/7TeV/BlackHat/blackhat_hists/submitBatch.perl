#!/usr/bin/perl

######################################################################
#Simple program to submit commands/scripts w/ args to the lxplus batch
#system.
#
# joseph.haley@cern.ch
######################################################################

sub usage(){
    print <<EOF;

Usage:
$0 <jobname> <command> [parameters]

EOF
}

use Cwd;

if ($#ARGV<0){
    &usage;
    exit(1);
}

$debug=1;
$promptuser=0;
#$QUEUE="8nm"; 	# 8nm 1nh 8nh 1nd 2nd 1nw 2nw (to get list of queues: bqueues -u jhaley)
$QUEUE="8nh";
$POOL="5000"; 	# Scratch space for job in MB (probably doesn't matter because job will run in submition area)
$MEM="";     	# I don't know how to specify this yet


($job,$exe,@params) = (@ARGV);
!$debug or print "exe=$exe params=@params\n";

###setup variables for submission
$pwd = getcwd;
!$debug or print "pwd=$pwd\n";

### get job name
#$job = $exe;
#$job =~s/\.\///;
#$job =~s/\.sh//;
!$debug or print "job=$job\n";

### add time stamp to job name
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
$stamp = sprintf ("%4d%02d%02d%02d%02d%02d",$year+1900,$mon+1,$mday,$hour,$min,$sec);
$job = "$job\_$stamp";
!$debug or print "stamp=$stamp\n";
!$debug or print "job=$job\n";

$log = "logs/$job.log";
$pfile = "job_$job.sh";

print "\n***********************************\n";
print "    Submitting Batch Job $job\n";
print "Executable: $exe\n";
print "Parameters: @params\n";
print "Logfile:    $log\n";
print "Script:     $pfile\n";
print "***********************************\n";

while( $promptuser ){
    print "Do you want to continue? [y]/n ";
    chop ($answer=<STDIN>);
    if ($answer eq "n"){
	exit 0;
    }elsif ($answer eq "y" or $answer eq ""){
	last;
    }
}


### construct the script to be sent to the batch system
open(FILE, ">$pfile");
print FILE <<EOS;
#!/bin/sh
echo "-------------------------------"
echo `/bin/hostname`
echo "LSB_SUBCWD: \$LSB_SUBCWD"

. /etc/bashrc

export BATCHDIR=`pwd`
echo "BATCHDIR: \$BATCHDIR"

pwd
if [ -d $pwd ] ; then
  cd $pwd
else
    echo "$pwd is not a directory on this node!  Aborting."
    exit 1
fi
pwd

#echo "PATH: $PATH"
echo -n "Exe: "
which $exe

if ! [ -d `dirname $log` ] ; then
  mkdir -p `dirname $log`
fi
$exe @params > $log

echo "-------------------------------"
exit 0
EOS
close(FILE);
chmod 0744, $pfile;


@bsub_command = ("/afs/cern.ch/cms/caf/scripts/bsub", "-R \"pool>$POOL\"", "-q $QUEUE", "-J $job", $pfile);

!$debug or print "@bsub_command";
print "\n";

# submit the job
system "@bsub_command";
system "sleep 1";

exit(0);
