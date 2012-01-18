import os
import sys
print '\nLoading ROOT ... \n\n'
from ROOT import *
import math
print 'ROOT loaded.'

# FILL OUT INFORMATION BELOW ------------------------------------------------------------------------------------------------------------------
discriminatingvariables = ['MET_pf','Pt_muon1','ST_pf_munu','M_bestmupfjet_munu'] # Discriminating variables, in order, used for the TMVA
method = 'Likelihood'  # METHOD Used

fdir = '~/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan17_TEST_2012_01_17_18_23_52/SummaryFiles/' # Where your root files are kept
tag = 'MVABetaHalf'  # Tag to name your new directory of root files. DO NOT LEAVE BLANK

# Your preselection. Filter some events. It's fun.
preselection = '(((Pt_muon1>40)*(Pt_muon2<15.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5)*(FailIDPFThreshold<25.0)*(MT_muon1pfMET>50.0))'


TreeName = 'PhysicalVariables' # The name of the tree in which the discriminating variables are stored.
# These are the files you are using. 
OrigKeepFiles = ['LQToCMu_BetaHalf_M_250.root',
'LQToCMu_BetaHalf_M_350.root',
'LQToCMu_BetaHalf_M_400.root',
'LQToCMu_BetaHalf_M_450.root',
'LQToCMu_BetaHalf_M_500.root',
'LQToCMu_BetaHalf_M_550.root',
'LQToCMu_BetaHalf_M_600.root',
'LQToCMu_BetaHalf_M_650.root',
'LQToCMu_BetaHalf_M_750.root',
'LQToCMu_BetaHalf_M_850.root',
'DiBoson.root',
'SingleTop.root',
'TTBar.root',
'WJets_Sherpa.root',
'ZJets_Sherpa.root',
'SingleMuData.root']	

signal_tag = 'LQ' # This identifies which files are signal. Should be in each signal file name above. 
data_tag = 'Data' # This identifies which files are real data. 
# All files not meeting above tags are background!


# -----------------------------------------------------------------------------------------------------------------------------------------------
person = os.popen('whoami').readlines()[0].replace('\n','')
n = 0
Vars = []
tmp = '/tmp/'+person+'/tmpfiles/'
fdirout = fdirout = fdir + '/'+tag+'/'

skip = 0
if '--skip_copytree' in sys.argv:
	skip = 1

if skip == 0:

	print '\n\nShrinking files with pre-selection...\n\n'
	os.system('rm -r '+tmp)
	os.system('mkdir '+tmp)

	for x in OrigKeepFiles:
		fname = fdir+x
		fout1 = 'file://'+tmp+'/'+x
		print fout1
		f = TFile.Open(fname)
		t = f.Get(TreeName)	
		f1 = TFile(fout1,"NEW")
		t1 = t.CopyTree(preselection)
		f1.Write()
		f1.Close()
		f.Close()
		del t 
		del t1

KeepFiles = os.listdir(tmp)
KeepFiles.sort()
fdir = tmp


Signals = []
Backgrounds = []
Data = ''
DataFile = ''
BackgroundFiles = []

for K in KeepFiles:
	if signal_tag in K:
		Signals.append(K.split('.')[0])
	elif data_tag in K:
		Data = (K.split('.')[0])
		DataFile = fdir + K
	else:
		Backgrounds.append(K.split('.')[0])
		BackgroundFiles.append(fdir+K)

import numpy
import array
	
	
def UpdateFileWithMVA(a_file,a_meth,a_SigType):

	reader = TMVA.Reader()
	n=0
	for var in discriminatingvariables:
		exec('var'+str(n)+' = array.array(\'f\',[0])')
		exec('reader.AddVariable("'+var+'",var'+str(n)+')')
		exec('Vars.append(var'+str(n)+')')
		n += 1
	reader.BookMVA(a_meth,'/tmp/'+person+'/tmva_scratch/'+a_SigType+'/tmva/test/weights/TMVAClassification_'+a_meth+'.weights.xml')
	FIn = TFile.Open(a_file,"")
	TIn= FIn.Get(TreeName)

	MVAOutput = numpy.zeros(1, dtype=float)	
	FOut = TFile.Open(a_file.replace('.root','new.root'),"RECREATE")

	TOut = TIn.CopyTree('0')
	TOut.Branch(method+a_SigType, MVAOutput, method+a_SigType+'/D') 
	N = TIn.GetEntries()
	
	for n in range(N):
		if n%10000 == 1:
			print a_file+":   "+str(n) +' of '+str(N) +' events evaluated for '+a_SigType+'.'
		TIn.GetEntry(n)
		a = 0
		for var in discriminatingvariables:
			exec('var'+str(a)+'[0] = TOut.'+var)
			a += 1
		MVAOutput[0] = reader.EvaluateMVA(a_meth)
		TOut.Fill()
	
	FOut.Write("", TObject.kOverwrite)
	FOut.Close()
	os.system('mv '+a_file.replace('.root','new.root')+ ' '+a_file)


for Signal in Signals:
	SignalFile = fdir + Signal + '.root'
	UpdateFileWithMVA(SignalFile,method,Signal)
	UpdateFileWithMVA(DataFile,method,Signal)
	
	for Background in Backgrounds:
		BackgroundFile = fdir + Background + '.root'
		UpdateFileWithMVA(BackgroundFile,method,Signal)

print 'Finished modifying root files! Moving MVA-Modified Root Files to a mirrored directory of the original: '
print 'Using Directory '+fdirout
print 'Please Wait'
os.system('mkdir '+fdirout)
os.system('cp '+tmp+'/* ' + fdirout)
print 'Transfer Complete! Enjoy.'

