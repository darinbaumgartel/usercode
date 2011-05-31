#!/bin/sh

cd ../
cd python
python NTupleTemplateUtility.py
cd -
cd Stage1_NTupleAnalysis

# Below permissions are enambled on the file "RootProceses", which stores root commands to run over the files
# created above. Edit RootProcesses as needed to include any new files added above. RootProcesses must have
# no file extension. 
chmod +x RootProcesses

# Run RootProcesses
root -l .x RootProcesses

# Clean up files. Root file should be created in current directory with physical variables for TMVA run. 

hadd WJets.root W*Pt*.root
hadd ZJets.root Z*Pt*root
hadd SingleTop.root Single*.root
hadd VVJets.root ZZ* WZ* WW*

#hadd ALLBKG.root  WJets.root ZJets.root TTbarJets.root VVJets.root SingleTop.root
rm -r CurrentRootFiles
mkdir CurrentRootFiles
mv *.root CurrentRootFiles
rm *_*.*
rm *Pt*.root
rm RootProcesses


