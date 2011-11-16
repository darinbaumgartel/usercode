from ROOT import *

f = TFile.Open("~/neuhome/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_StandardSelections_PostLP_2fb_2011_08_24_05_33_55/SummaryFiles/SingleMuData.root")

t = f.Get("PhysicalVariables")

N = t.GetEntries()

selectionmumu = "((Pt_muon1>40)*(Pt_muon2>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_mumu>250)*(deltaR_muon1muon2>0.3)*(M_muon1muon2>50)*((abs(Eta_muon1)<2.1)||(abs(Eta_muon2)<2.1)))*(ST_pf_mumu > 740)*(M_muon1muon2 > 140)*(LowestMass_BestLQCombo > 350)"
selectionmunu = "(((Pt_muon1>40)*(Pt_muon2<15.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5)*(FailIDPFThreshold<25.0)*(MT_muon1pfMET>50.0))*(ST_pf_munu > 870)*(MET_pf > 195)*(M_bestmupfjet_munu > 380)"

tmumu = t.CopyTree(selectionmumu)
tmunu = t.CopyTree(selectionmunu)
del t

def num2str(num, precision):
	return "%0.*f" % (precision, num)

mumuheader = '  \\begin{tabular}{|c||c|c|c|c||c|c|c|c||c|c||c|c||c|c|}\hline\n$S_T$&$p_T^{\mu}$&$\eta^{\mu}$&$\sigma_{p_T}^{\mu}$ & $q^{\mu}$&$p_T^{\mu}$&$\eta^{\mu}$&$\sigma_{p_T}^{\mu}$&$q^{\mu}$ &$p_T^{\\text{jet}}$&$\eta^{\\text{jet}}$&$p_T^{\\text{jet}}$&$\eta^{\\text{jet}}$&$\MET$\\\\ \hline \hline\n'
munuheader = '  \\begin{tabular}{|c||c|c|c|c||c|c||c|c||c|c||c|c|}\hline\n$S_T$ &$p_T^{\mu}$ &$\eta^{\mu}$ &$\sigma_{p_T}^{\mu}$ & $q^{\mu}$ &$p_T^{\\text{jet}}$ &$\eta^{\\text{jet}}$ &$p_T^{\\text{jet}}$ &$\\eta^{\text{jet}}$ &$\MET$\\\\ \hline \hline'
headers = []
fillers = []
xxx = []
yyy = []
zzz = []
mutype = []
print '\n----------  evaluating mumu   ----------\n\n'
for n in range(tmumu.GetEntries()):
	tmumu.GetEntry(n)
	line = ' '
	line += num2str(tmumu.ST_pf_mumu,2)
	line += ' & '
	line += num2str(tmumu.Pt_muon1,2)
	line += ' & '
	line += num2str(tmumu.Eta_muon1,2)
	line += ' & '
	line += num2str(tmumu.PtError_muon1,2)
	line += ' & '
	line += (tmumu.Charge_muon1>0)*' + ' + (tmumu.Charge_muon1<0)*' - '
	line += ' & '
	line += num2str(tmumu.Pt_muon2,2)
	line += ' & '
	line += num2str(tmumu.Eta_muon2,2)
	line += ' & '
	line += num2str(tmumu.PtError_muon2,2)
	line += ' & '
	line += (tmumu.Charge_muon2>0)*' + ' + (tmumu.Charge_muon2<0)*' - '	
	line += ' & '
	line += num2str(tmumu.Pt_pfjet1,2)
	line += ' & '
	line += num2str(tmumu.Eta_pfjet1,2)	
	line += ' & '
	line += num2str(tmumu.Pt_pfjet2,2)
	line += ' & '
	line += num2str(tmumu.Eta_pfjet2,2)		
	line += ' & '
	line += num2str(tmumu.MET_pf,2)	
	line += ' \\\\ '
	XXX = str(tmumu.run_number)
	ZZZ =  str(tmumu.ls_number) 
	YYY = str(tmumu.event_number)
	
	print line
	headers.append(mumuheader)
	fillers.append(line+' \\hline')
	xxx.append(XXX)
	yyy.append(YYY)
	zzz.append(ZZZ)
	mutype.append('$\\mu\\mu jj$')


print '\n----------  evaluating munu   ----------\n\n'
for n in range(tmunu.GetEntries()):
	tmunu.GetEntry(n)
	line = ' '
	line += num2str(tmunu.ST_pf_munu,2)
	line += ' & '
	line += num2str(tmunu.Pt_muon1,2)
	line += ' & '
	line += num2str(tmunu.Eta_muon1,2)	
	line += ' & '
	line += num2str(tmunu.PtError_muon1,2)
	line += ' & '
	line += (tmunu.Charge_muon1>0)*' + ' + (tmunu.Charge_muon1<0)*' - '
	line += ' & '
	line += num2str(tmunu.Pt_pfjet1,2)
	line += ' & '
	line += num2str(tmunu.Eta_pfjet1,2)	
	line += ' & '
	line += num2str(tmunu.Pt_pfjet2,2)
	line += ' & '
	line += num2str(tmunu.Eta_pfjet2,2)		
	line += ' & '
	line += num2str(tmunu.MET_pf,2)	
	line += ' \\\\  '
	print line
	headers.append(munuheader)
	
	XXX = str(tmunu.run_number)
	ZZZ =  str(tmunu.ls_number) 
	YYY = str(tmunu.event_number)	
	fillers.append(line+' \\hline')
	xxx.append(XXX)
	yyy.append(YYY)
	zzz.append(ZZZ)
	mutype.append('$\\mu\\nu jj$')
		
myevents = []
print '\n----------  events for mumu   ----------\n\n'
for n in range(tmumu.GetEntries()):
	tmumu.GetEntry(n)
	line = str(tmumu.run_number) +':'+ str(tmumu.ls_number) +':'+ str(tmumu.event_number)
	myevents.append(line)
	print line


print '\n----------  events for  munu   ----------\n\n'
for n in range(tmunu.GetEntries()):
	tmunu.GetEntry(n)
	line = str(tmunu.run_number) +':'+ str(tmunu.ls_number) +':'+ str(tmunu.event_number)
	myevents.append(line)
	print line
	
print '\n\n'
import os

datasets = []

datasets.append(['/SingleMu/Run2011A-May10ReReco-v1/RECO',160329,163869]) 
datasets.append(['/SingleMu/Run2011A-PromptReco-v4/RECO',165071,168437])
#datasets.append(['/SingleMu/Run2011A-05Aug2011-v1/RECO',170053,172619])
datasets.append(['/SingleMu/Run2011A-PromptReco-v5/RECO',170053,172619])
datasets.append(['/SingleMu/Run2011A-PromptReco-v6/RECO',172620,173688])

CMSSWversions = []
for x in datasets:
	dset = x[0]
	os.system('rm log.txt')
	os.system('dbsql \'find release where dataset = '+dset+'\' > log.txt')
	logfile = open('log.txt','r')
	for line in logfile:
		if 'CMSSW' in line:
			CMSSWversions.append(line.replace('\n',''))
			break
	logfile.close()
print CMSSWversions

crabinfo = []
for ev in myevents:
	run = int(ev.split(':')[0])
	#print run
	for d in datasets:
		if run > d[1] and run < d[2]:
			dset = d[0]
	crabinfo.append(ev + ',' + dset)
	
f = open('makegetevents.sh','w')
f.write('#!/bin/sh\n\n')
os.system('rm runlocal.csh')
os.system("echo \#\!\/bin\/csh > runlocal.csh")
for x in CMSSWversions:
	os.system('echo "cmsrel '+x+' ">>runlocal.csh')
for x in crabinfo:
	cdir = x.split(',')[0]
	cdir = 'dir'+cdir.replace(':','_')
	f.write('rm -r '+cdir+'\nmkdir '+cdir+'\ncd '+cdir+'\n')
	for d in range(len(datasets)):
		if x.split(',')[1] in datasets[d][0]:
			thisrel = CMSSWversions[d]
	
	f.write('edmPickEvents.py "'+x.split(',')[1]+'" '+x.split(',')[0]+' --crab\n')
	os.system('echo "cd '+thisrel+'/src ">>runlocal.csh')
	os.system('echo cmsenv >>runlocal.csh')
	os.system('echo "cd -" >> runlocal.csh')
	os.system('edmPickEvents.py "'+x.split(',')[1]+'" '+x.split(',')[0]+' --output Event_'+(cdir.replace(':','_')).replace('dir','')+' >>runlocal.csh')
	f.write('crab -create -cfg pickevents_crab.config\ncrab -submit\ncd - \n\n')
	
	
f.close()
os.system('chmod 777 makegetevents.sh')
os.system('chmod 777 runlocal.csh')
os.system('rm texlines.txt')
os.system('touch texlines.txt')
import sys
if '--maketex' in sys.argv:
	
	for n in range(len(headers)):
		frag = open('fragment.txt','r')
		os.system('rm thisfragment.txt')
		fout = open('thisfragment.txt','w')
		for line in frag:
			line = line.replace('xxx',xxx[n])
			line = line.replace('yyy',yyy[n])
			line = line.replace('zzz',zzz[n])
			line = line.replace('HEADERLINE',headers[n])
			line = line.replace('FILLERLINE',fillers[n])
			line = line.replace('MUTYPE',mutype[n])
			fout.write(line)
		fout.close()
		os.system('cat thisfragment.txt >> texlines.txt')
			
			
		
