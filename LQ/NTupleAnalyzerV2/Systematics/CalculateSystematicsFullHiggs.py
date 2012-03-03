import os
import sys
from ROOT import *


#castors = ['/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan10_2012_01_10_23_03_00/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan10_JetScaleUp_2012_01_11_00_38_03/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan10_JetScaleDown_2012_01_11_01_29_06/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan10_MuScaleUp_2012_01_11_02_10_50/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan10_MuScaleDown_2012_01_11_04_20_45/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan10_JetSmear_2012_01_11_05_08_45/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan10_MuSmear_2012_01_11_05_46_18/SummaryFiles']

#castors = ['/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan20_2012_01_16_22_03_27/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan16_JetScaleUp_2012_01_16_22_59_44/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan16_JetScaleDown_2012_01_16_23_42_35/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan16_MuScaleUp_2012_01_17_00_22_34/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan16_MuScaleDown_2012_01_17_00_59_38/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan16_JetSmear_2012_01_17_01_35_20/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan16_MuSmear_2012_01_17_02_09_25/SummaryFiles']

#castors = ['/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan20_2012_01_20_17_30_11/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan20_JetScaleDown_2012_01_20_20_12_27/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan20_JetScaleUp_2012_01_20_19_19_40/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan20_JetSmear_2012_01_21_02_37_45/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan20_MuScaleDown_2012_01_20_22_07_44/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan20_MuScaleUp_2012_01_20_20_54_33/SummaryFiles',
#'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Jan20_MuSmear_2012_01_21_07_37_21/SummaryFiles']


castors = ['/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Feb03_2012_02_07_21_01_29/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Feb12_JetScaleUp_2012_02_13_04_00_59/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Feb12_JetScaleDown_2012_02_13_05_28_31/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Feb12_MuScaleUp_2012_02_13_08_01_25/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Feb12_MuScaleDown_2012_02_13_10_27_44/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Feb12_JetSmear_2012_02_13_12_17_12/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_06_Default_StandardSelections_4p7fb_Feb12_MuSmear_2012_02_13_15_06_37/SummaryFiles']

KeepFiles = ['LQToCMu_BetaHalf_M_250.root',
'LQToCMu_BetaHalf_M_350.root',
'LQToCMu_BetaHalf_M_400.root',
'LQToCMu_BetaHalf_M_450.root',
'LQToCMu_BetaHalf_M_500.root',
'LQToCMu_BetaHalf_M_550.root',
'LQToCMu_BetaHalf_M_600.root',
'LQToCMu_BetaHalf_M_650.root',
'LQToCMu_BetaHalf_M_750.root',
'LQToCMu_BetaHalf_M_850.root',
'LQToCMu_M_250.root',
'LQToCMu_M_350.root',
'LQToCMu_M_400.root',
'LQToCMu_M_450.root',
'LQToCMu_M_500.root',
'LQToCMu_M_550.root',
'LQToCMu_M_600.root',
'LQToCMu_M_650.root',
'LQToCMu_M_750.root',
'LQToCMu_M_850.root',
'DiBoson.root',
'SingleTop.root',
'TTBar.root',
'WJets_Sherpa.root',
'ZJets_Sherpa.root'] 

TTScale = 0.93
TTDDScale = 0.55
WScale = 1.23
ZScale = 1.34
OtherScale = 0.9


normtag = 'StandardSelections_4p7fb_Feb03_2012'
scaletags = ['JetScaleUp','JetScaleDown','MuScaleUp','MuScaleDown','JetSmear','MuSmear']
#scaletags = ['JetScaleUp']
tags = []
tags.append(normtag)
for x in scaletags:
	tags.append(x)

prefix = 'rfio'
lsqry = 'nsls'
if "--neuswitch" in sys.argv:
	#os.system('sshfs -o nonempty darinb@neu:/home/darinb/ ~/neuhome;')
	castors2 = []
	for x in castors:
		castors2.append(x.replace(x.split('LQAnalyzerOutput')[0],'~/neuhome/'))
	castors = castors2
	prefix = 'file'
	lsqry = 'ls'
	

for c in castors:
	print '-'*100
	print 'Evaluating files in directory: \n\n  ' +c + '\n\n'
	files = os.popen(lsqry+' '+c).readlines()
	cfiles = []
	for x in files:
		cfiles.append(c+'/'+x.replace('\n',''))
	if lsqry == 'nsls':
		for x in cfiles:
			os.system('stager_qry -M '+x)
			os.system('stager_get -M '+x)
		
		
lumi = 4700.0

cut_mc = ''

preselectionmumu = str(lumi)+'*weight_pileup4p7fb_higgs*((Pt_muon1>40)*(Pt_muon2>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_mumu>250)*(deltaR_muon1muon2>0.3)*(M_muon1muon2>50)*((abs(Eta_muon1)<2.1)&&(abs(Eta_muon2)<2.1)))' + cut_mc
preselectionmunu = str(lumi)+'*weight_pileup4p7fb_higgs*(pass_HBHENoiseFilter>0.5)*(pass_passBeamHaloFilterTight>0.5)*(pass_EcalMaskedCellDRFilter>0.5)*(pass_isTrackingFailure>0.5)*(((Pt_muon1>40)*(Pt_muon2<15.0)*(MET_pf>55)*(Pt_pfjet1>40)*(Pt_pfjet2>40)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5)*(FailIDPFThreshold<25.0)*(MT_muon1pfMET>50.0)*(deltaR_muon1pfjet1>0.7)*(deltaR_muon1pfjet2>0.7))' +cut_mc
preselectionemu = '0.55*(LowestUnprescaledTriggerPass>0.5)*(pass_isBPTX0>0.5)*(Pt_muon1>40)*(Pt_HEEPele1>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_emu>250)*(M_muon1HEEPele1>50)*(deltaR_muon1HEEPele1>0.3)*((abs(Eta_muon1)<2.1)&&(abs(Eta_HEEPele1)<2.1))';



selections = []
selections.append(preselectionmumu)
selections.append(preselectionmunu)
signaluse = []
signaluse.append('MuMuPreSel')
signaluse.append('MuNuPreSel')
fullsel = 0
for x in range(len(sys.argv)):
	if sys.argv[x] == '-i':
		fullsel = 1
		fullfile = sys.argv[x+1]
if (fullsel):
	log = open(fullfile,'r')
	for line in log:
		if 'LQToCMu' in line:
			signaluse.append(line.replace('\n',''))
			if 'BetaHalf' in line:
				presel = preselectionmunu
			else:
				presel = preselectionmumu
		if '>' in line:
			selections.append(presel+line.replace('\n','').replace('1.0*(','*('))
			#break


ignores = []

opt_n = []
sample_n = []
total_n = []
tag_n = []
issignal_n = []
MCint_n = []
weight_n = []

pfiles = []
for c in castors:
	files = os.popen(lsqry+' '+c).readlines()
	for x in files:
		#if 'SingleMuData' in x or 'HighHT' in x:
			#continue
		tocontinue = 1
		for k in KeepFiles:
			if k in x:
				tocontinue = 0
		if tocontinue:
			continue
		pfiles.append(prefix+'://'+c+'/'+x.replace('\n',''))

#for x in pfiles:
	#print x
#exit()

person = os.popen('whoami').readlines()[0].replace('\n','')
tmp = '/tmp/'+person+'/tmpfiles/'


skip = 0
if '--skip_copytree' in sys.argv:
	skip = 1

if skip == 0:

	print '\n\nShrinking files with pre-selection...\n\n'
	os.system('rm -r '+tmp)
	os.system('mkdir '+tmp)
	for x in pfiles:
		fname = x.split('/')[-1]
		
		thistag = ''
		for t in tags:
			if t in x:
				thistag = t
		os.system('mkdir '+tmp+thistag)
		fout1 = 'file://'+tmp+thistag+'/mumu_'+fname
		fout2 = 'file://'+tmp+thistag+'/munu_'+fname
		
		print fout1
		f = TFile.Open(x)
		t = f.Get("PhysicalVariables")	
		f1 = TFile(fout1,"NEW")
		t1 = t.CopyTree(preselectionmumu)
		f1.Write()
		f1.Close()
		f.Close()
		del t 
		del t1
		
		print fout2
		f = TFile.Open(x)
		t = f.Get("PhysicalVariables")	
		f2 = TFile(fout2,"NEW")
		t2 = t.CopyTree(preselectionmunu)
		f2.Write()
		f2.Close()
		f.Close()
		del t 
		del t2	
	

flogV = open('SysVerboseLog.txt','w')
for s in range(len(selections)):
	bgtotal = 0.0

	sel = selections[s]
	use = signaluse[s]
	
	for c in castors:
		tag = ''
		for t in tags:
			if t in c:
				tag = t
		files = os.popen(lsqry+' '+c).readlines()
		cfiles = []
		for x in files:
			#if 'SingleMuData' in x  or 'HighHT' in x:				
				#continue
			tocontinue = 1
			for k in KeepFiles:
				if k in x:
					tocontinue = 0
			if tocontinue:
				continue				
			cfiles.append(prefix+'://'+c+'/'+x.replace('\n',''))
		for x in cfiles:
			sel = selections[s]

			scalefactor = '*1.0'
			if 'TTBar' in x:
				scalefactor = '*'+(str(TTScale))
			if 'WJets' in x:
				scalefactor = '*'+(str(WScale))	
			if 'ZJets' in x:
				scalefactor = '*'+(str(ZScale))
			if 'LQToCMu' in x and use not in  x: 
				continue;
			if 'LQToCMu' in x and 'BetaHalf' in x:
				scalefactor = '*(0.9)'
			marker = 'mumu'
			if "_BetaHalf_" in use or "MuNu" in use:
				marker = 'munu'
			fname = x.split('/')[-1]

			isTT = 0
			if 'TTBar' in x and ('BetaHalf' not in use and 'MuNu' not in use):
				isTT = 1
				scalefactor = '*'+(str(TTDDScale))				
			if ('DiBoson' in x or 'SingleTo' in x) and ('BetaHalf' in use or 'MuNu' in use): 
				scalefactor = '*'+str(OtherScale)
			thistag = ''
			for t in tags:
				if t in x:
					thistag = t
			fout = 'file://'+tmp+thistag+'/'+marker+'_'+fname
			
			if isTT == 1:
				fout = x.replace('TTBar.root','SingleMuData.root')
				sel = sel.replace(preselectionmumu.replace(cut_mc,''),preselectionemu)
				sel = sel.replace(cut_mc,'')
				sel = sel.replace('ST_pf_mumu','ST_pf_emu')

				sel = sel.replace('muon1muon2','muon1HEEPele1')
				sel = sel.replace('LowestMass_BestLQCombo','LowestMass_BestLQCombo_emuselection')		
						
			
						
			f = TFile.Open(fout)
			t = f.Get("PhysicalVariables")
			h = TH1D('h','h',1,-1,3)
			h.Sumw2()
			hw = TH1D('hw','hw',1,0.0,2.0)
			hw.Sumw2()
			t.Project('h','1.0',sel+scalefactor)
			if isTT == 0:
				n = h.Integral()
			if isTT ==1:
				n = TTDDScale*h.GetEntries()
			
			if 'BetaHalf' in use or 'MuNu' in use:
				t.Project('hw','1.0',preselectionmunu+scalefactor)

			else:
				t.Project('hw','1.0',preselectionmumu+scalefactor)
			
			nerr = h.GetBinError(1)		
			rootfile = (x.split('/')[-1]).replace('.root','')
			opt_n.append(use)
			sample_n.append(rootfile)
			total_n.append(n)
			tag_n.append(tag)
			MCint  = h.GetEntries()
			MCint_n.append(MCint)
			if (MCint>0.00001) and (n>0.001):
				thisweight = n/MCint
			elif hw.GetEntries()>0.00001:
				thisweight = (1.0*(hw.Integral()))/(1.0*(hw.GetEntries()))
			else:
				thisweight = 0.0
			if isTT==1:
				thisweight = TTDDScale
			weight_n.append(thisweight)
			if 'LQToCMu' in x:
				issignal_n.append('sig')
			else:
				issignal_n.append('bg')
			#print rootfile +(25-len(rootfile))*' '+ str(n) 
			print use + '   ' + rootfile + (50 - len(rootfile))*' ' +tag+(50 - len(tag))*' '+str(MCint)+'   '+str(thisweight)+'  '+str(n)+'  '+str(nerr)
			flogV.write(use + '   ' + rootfile + (50 - len(rootfile))*' ' +tag+(50 - len(tag))*' '+str(MCint)+'   '+str(thisweight)+'  '+str(n)+'  '+str(nerr)+'\n')
			f.Close()
			del t
flogV.close()			
opts = []
samples = []
tags = []
for x in opt_n:
	if x not in opts:
		opts.append(x)
		print x
for x in sample_n:
	if x not in samples:
		samples.append(x)
for x in tag_n:
	if x not in tags:
		tags.append(x)

print 'samples'
for x in samples:
	print x
print 'samples'

R = range(len(opt_n))

summary_opts = []

for t in tags:
	exec('summary_int_'+t+'_sig=[]')
	exec('summary_int_'+t+'_bg=[]')
	exec('summary_int_'+t+'_sig_var=[]')
	exec('summary_int_'+t+'_bg_var=[]')	
for t in tags:		
	for o in opts:
		exec('summary_int_'+t+'_sig.append(0.0)')
		exec('summary_int_'+t+'_bg.append(0.0)')
		exec('summary_int_'+t+'_sig_var.append(0.0)')
		exec('summary_int_'+t+'_bg_var.append(0.0)')
for o in range(len(opts)):
	if 'BetaHalf' in opts[o]:
		ignores = ['TTBar','WJets']
		ignores = []

	else:
		ignores = ['TTBar','ZJetsMG','DiBoson']
		ignores = ['TTBar']

	summary_opts.append(opts[o])
	for i in R:		
		if opt_n[i] != opts[o]:
			continue
		exec('summary_int_'+tag_n[i]+'_'+issignal_n[i]+'['+str(o)+']+='+str(total_n[i]))
		if sample_n[i] not in ignores:
			exec('summary_int_'+tag_n[i]+'_'+issignal_n[i]+'_var['+str(o)+']+='+str(total_n[i]))

fout = open('SystematicsLog_FullSel.txt','w')

hline = '\n\nLeptoquarks\n\n\nOptimized\tMagnitude\tVariations\nSelection\t'
for t in tags:
	if 'Standard' not in t:
		hline += t + '\t'
		
fout.write(hline+'\n')		
print hline
for o in range(len(opts)):
	line = opts[o] + '\t'
	for t in tags:
		if t==normtag:
			exec('line += str(float(summary_int_'+t+'_sig_var['+str(o)+']) )+"\t"')
		if t!=normtag:
			exec('line += str(float(summary_int_'+t+'_sig_var['+str(o)+']) - float(summary_int_'+normtag+'_sig_var['+str(o)+']) )+"\t"')
	print line
	fout.write(line+'\n')


hline = '\n\nBackgrounds\n\n\nOptimized\tMagnitude\tVariations\nSelection\t'
for t in tags:
	if 'Standard' not in t:
		hline += t + '\t'
		
fout.write(hline+'\n')		
print hline
for o in range(len(opts)):
	line = opts[o] + '\t'
	for t in tags:
		if t==normtag:
			exec('line += str(float(summary_int_'+t+'_bg_var['+str(o)+']) )+"\t"')
		if t!=normtag:
			exec('line += str(float(summary_int_'+t+'_bg_var['+str(o)+']) - float(summary_int_'+normtag+'_bg_var['+str(o)+']) )+"\t"')
	print line
	fout.write(line+'\n')

fout.close()

