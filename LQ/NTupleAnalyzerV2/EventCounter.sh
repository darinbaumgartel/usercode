############################################################################
# This script counts the number of events in a given folder of MC
#                         INSTRUCTIONS
# Set up the csv file that you want to use for AnalyzerMakeFast.py
# Note: Signal Type should be column 1, Castor Folder column 8
# If this isn't correct, change "f1" and "f8" to match their column # below
# Make sure that there is no file in your folder called EventCountResults.txt
# Then type "sh EventCounter.sh {csv file name}" and hit enter
#############################################################################

cut -f1 -d',' $1 > SigType.txt
cut -f8 -d',' $1 > CastorFolders.txt
# ^ Here I make text files out of the 1st and 8th columns of the input csv file

N=`wc SigType.txt | gawk '(NR==1){print $1}'`


echo $1
rm -r LogFiles
mkdir LogFiles

for ((i = 2; i <N+1; i++))
do
    CurrentFolder=`gawk '(NR=='$i'){print $1}' CastorFolders.txt`
    CurrentSig=`gawk '(NR=='$i'){print $1}' SigType.txt`
    CurrentDir=`pwd`
    echo $CurrentFolder

    nsls $CurrentFolder > TotalFolderContents.txt
    grep $CurrentSig TotalFolderContents.txt > CurrentFiles.txt
    # ^ Here I take only files matching the current Signature and put them in a text file

    M=`wc CurrentFiles.txt | gawk '(NR==1){print $1}'`

    mkdir LogFiles/$CurrentSig

	echo LogFiles/$CurrentSig

    for ((j = 1; j <=M; j++))
    do
	CurrentFile=`gawk '(NR=='$j'){print $1}' CurrentFiles.txt`

	cat BlankScript.sh | sed -e 's,File=PLACEHOLDER,File='$CurrentFolder'/'$CurrentFile',g
s,PLACEHOLDER_TWO,'$CurrentDir'/LogFiles/'$CurrentSig'/Log_'$j'.txt,g
s,WORKINGDIR,'$CurrentDir',g' > $CurrentDir/LogFiles/$CurrentSig/Script_$j.sh
	# ^ This replaces the placeholders in BlankScript.sh

	bsub -o /dev/null -e /dev/null -q 1nh -J Count < $CurrentDir/LogFiles/$CurrentSig/Script_$j.sh
    done
    #sleep 60
    
    echo $CurrentFolder
    echo "Done"

done
echo " "
echo " Job creation and submission complete. Checking jobs... " 
echo "  "

bjobs > check.txt
NumRemaining=`wc check.txt | gawk '(NR==1){print $1}'`
until [ $NumRemaining -lt 1 ]
    do
	echo $NumRemaining jobs left
	rm check.txt
	sleep 300
	bjobs > check.txt
	NumRemaining=`wc check.txt | gawk '(NR==1){print $1}'`
    done
# ^ This until loop waits until all the jobs are done

touch ErrorLog.txt

for ((i = 2; i <=N; i++))
do
    CurrentFolder=`gawk '(NR=='$i'){print $1}' CastorFolders.txt`
    CurrentSig=`gawk '(NR=='$i'){print $1}' SigType.txt`
    nsls $CurrentFolder > TotalFolderContents.txt
    grep $CurrentSig TotalFolderContents.txt > CurrentFiles.txt
    M=`wc CurrentFiles.txt | gawk '(NR==1){print $1}'`
    Total=0
    for ((j = 1; j <=M; j++))
    do
	New=`gawk '(NR==1){print $1}' LogFiles/$CurrentSig/Log_$j.txt`

	if [[ "$New" =~ ^[0-9]+$ ]]
	then
	    let Total=$Total+$New	    
	else
	    echo Log_$j of $CurrentSig had no events >> ErrorLog.txt
	fi
	# ^ This if/else statement checks for empty output files
    done
    echo $CurrentSig >> EventCountResults.txt
    echo $Total >> EventCountResults.txt
    echo "  " >> EventCountResults.txt

done
