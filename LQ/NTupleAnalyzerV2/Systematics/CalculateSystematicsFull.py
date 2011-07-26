import os
import sys
from ROOT import *

castors = ['/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_StandardSelections_2011_07_21_00_08_14/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_JetScaleUp0p4_2011_07_21_05_45_22/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_JetScaleDown0p4_2011_07_21_05_34_49/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_MuScaleUp0p1_2011_07_21_05_46_48/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_MuScaleDown0p1_2011_07_21_05_35_58/SummaryFiles'
]

normtag = 'StandardSelections'
scaletags = ['JetScaleUp','JetScaleDown','MuScaleUp','MuScaleDown']
tags = []
tags.append(normtag)
for x in scaletags:
	tags.append(x)

prefix = 'rfio'
lsqry = 'nsls'
if "--neuswitch" in sys.argv:
	os.system('sshfs -o nonempty darinb@neu:/home/darinb/ ~/neuhome;')
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
		
		
lumi = 964.0

preselectionmumu = str(lumi)+'*weight*((Pt_muon1>40)*(Pt_muon2>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_mumu>250)*(deltaR_muon1muon2>0.3)*(M_muon1muon2>50)*((abs(Eta_muon1)<2.1)||(abs(Eta_muon2)<2.1)))'
preselectionmunu = str(lumi)+'*weight*(((Pt_muon1>40)*(Pt_muon2<30.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5)*(FailIDPFThreshold<25.0)*(MT_muon1pfMET>50.0))'

selections = []
signaluse = []
fullsel = 0
for x in range(len(sys.argv)):
	if sys.argv[x] == '-i':
		fullsel = 1
		fullfile = sys.argv[x+1]
if (fullsel):
	log = open('OptimizationResultsV2.txt','r')
	for line in log:
		if 'LQToCMu' in line:
			signaluse.append(line.replace('\n',''))
			if 'BetaHalf' in line:
				presel = preselectionmunu
			else:
				presel = preselectionmumu
		if '>' in line:
			selections.append(presel+line.replace('\n','').replace('1.0*(','*('))



cut_mc = "*(";
cut_mc += "((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)*(0.133))+";
cut_mc += "((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)*(0.5311))+";
cut_mc += "((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)*(1.0839))+";
cut_mc += "((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)*(1.7548))+";
cut_mc += "((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)*(2.2326))+";
cut_mc += "((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)*(2.293))+";
cut_mc += "((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)*(2.0818))+";
cut_mc += "((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)*(1.74354))+";
cut_mc += "((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)*(1.329634))+";
cut_mc += "((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)*(0.950884))+";
cut_mc += "((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)*(0.65398))+";
cut_mc += "((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)*(0.4212))+";
cut_mc += "((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)*(0.2595))+";
cut_mc += "((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)*(0.158601))+";
cut_mc += "((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)*(0.100442))+";
cut_mc += "((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)*(0.05945))+";
cut_mc += "((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)*(0.034516))+";
cut_mc += "((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)*(0.02072))+";
cut_mc += "((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)*(0.01170))+";
cut_mc += "((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)*(0.006946))+";
cut_mc += "((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)*(0.003486))";
cut_mc += ")";

ignores = []

opt_n = []
sample_n = []
total_n = []
tag_n = []
issignal_n = []


for s in range(len(selections)):
	if s>0 :
		break
	bgtotal = 0.0
	
	sel = selections[s]
	use = signaluse[s]
	if 'BetaHalf' in use:
		ignores = ['TTBar','WJet']
	else:
		ignores = ['TTBar','ZJet']
	for c in castors:
		tag = ''
		for t in tags:
			if t in c:
				tag = t
		files = os.popen(lsqry+' '+c).readlines()
		cfiles = []
		for x in files:
			if 'SingleMuData' in x:
				continue
			cfiles.append(prefix+'://'+c+'/'+x.replace('\n',''))
		for x in cfiles:
			#if "BetaHalf" in x:
				#continue
			if 'LQToCMu' in x and use not in  x: 
				continue;
			f = TFile.Open(x)
			t = f.Get("PhysicalVariables")
			h = TH1D('h','h',2,-1,3)
			t.Project('h','1.0',sel)
			n = h.Integral()
			rootfile = (x.split('/')[-1]).replace('.root','')
			opt_n.append(use)
			sample_n.append(rootfile)
			total_n.append(n)
			tag_n.append(tag)
			if 'LQToCMu' in x:
				issignal_n.append('sig')
			else:
				issignal_n.append('bg')
			#print rootfile +(25-len(rootfile))*' '+ str(n) 
			print use + '   ' + rootfile + (30 - len(rootfile))*' ' +tag+(30 - len(tag))*' '+str(n)
			f.Close()
			del t
opts = []
samples = []
tags = []
for x in opt_n:
	if x not in opts:
		opts.append(x)
for x in sample_n:
	if x not in samples:
		samples.append(x)
for x in tag_n:
	if x not in tags:
		tags.append(x)
		
#print opts
#print samples
#print tags

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
	if 'BetaHalf' in opts[0]:
		ignores = ['TTBar','WJets']
	else:
		ignores = ['TTBar','ZJetsMG']
	summary_opts.append(opts[o])
	for i in R:		
		if opt_n[i] != opts[o]:
			continue
		exec('summary_int_'+tag_n[i]+'_'+issignal_n[i]+'['+str(o)+']+='+str(total_n[i]))
		if sample_n[i] not in ignores:
			exec('summary_int_'+tag_n[i]+'_'+issignal_n[i]+'_var['+str(o)+']+='+str(total_n[i]))

fout = open('SystematicsLog_FullSel.txt','w')

hline = '\n\nLeptoquarks\n\nSelection\t'
for t in tags:
	if 'Standard' not in t:
		hline += t + '\t'
		
fout.write(hline+'\n')		
print hline
for o in range(len(opts)):
	line = opts[o] + '\t'
	for t in tags:
		if 'Standard' not in t:
			exec('line += str(float(summary_int_'+t+'_sig_var['+str(o)+']) - float(summary_int_StandardSelections_sig_var['+str(o)+']) )+"\t"')
	print line
	fout.write(line+'\n')


hline = '\n\nBackgrounds\n\nSelection\t'
for t in tags:
	if 'Standard' not in t:
		hline += t + '\t'
		
fout.write(hline+'\n')		
print hline
for o in range(len(opts)):
	line = opts[o] + '\t'
	for t in tags:
		if 'Standard' not in t:
			exec('line += str(float(summary_int_'+t+'_bg_var['+str(o)+']) - float(summary_int_StandardSelections_bg_var['+str(o)+']) )+"\t"')
	print line
	fout.write(line+'\n')

fout.close()
