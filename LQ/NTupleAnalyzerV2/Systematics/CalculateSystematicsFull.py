import os
import sys
from ROOT import *

castors = [
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_StandardSelections_ForLP_2011_08_09_22_42_53/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_JetScaleUp_0p04_ForLP_2011_08_10_03_58_37/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_JetScaleDown_0p04_ForLP_2011_08_10_04_20_57/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_MuScaleUp_0p01_ForLP_2011_08_10_04_05_41/SummaryFiles','/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_MuScaleDown_0p01_ForLP_2011_08_10_04_24_33/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_JetSmear_0p10_ForLP_2011_08_10_03_58_26/SummaryFiles',
'/castor/cern.ch/user/d/darinb/LQAnalyzerOutput/NTupleAnalyzer_V00_02_05_Default_MuSmear_0p04_ForLP_2011_08_10_04_28_17/SummaryFiles'
]

normtag = 'StandardSelections'
scaletags = ['JetScaleUp','JetScaleDown','MuScaleUp','MuScaleDown','JetSmear','MuSmear']
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
		
		
lumi = 1143.0


cut_mc = "*(";
cut_mc += "((N_PileUpInteractions > -0.5)*(N_PileUpInteractions < 0.5)*(0.137148419144))+";
cut_mc += "((N_PileUpInteractions > 0.5)*(N_PileUpInteractions < 1.5)*(0.570685400523))+";
cut_mc += "((N_PileUpInteractions > 1.5)*(N_PileUpInteractions < 2.5)*(1.14449974737))+";
cut_mc += "((N_PileUpInteractions > 2.5)*(N_PileUpInteractions < 3.5)*(1.8163157224))+";
cut_mc += "((N_PileUpInteractions > 3.5)*(N_PileUpInteractions < 4.5)*(2.270776812))+";
cut_mc += "((N_PileUpInteractions > 4.5)*(N_PileUpInteractions < 5.5)*(2.29783559215))+";
cut_mc += "((N_PileUpInteractions > 5.5)*(N_PileUpInteractions < 6.5)*(2.05828090818))+";
cut_mc += "((N_PileUpInteractions > 6.5)*(N_PileUpInteractions < 7.5)*(1.70525206573))+";
cut_mc += "((N_PileUpInteractions > 7.5)*(N_PileUpInteractions < 8.5)*(1.28872517493))+";
cut_mc += "((N_PileUpInteractions > 8.5)*(N_PileUpInteractions < 9.5)*(0.914713614527))+";
cut_mc += "((N_PileUpInteractions > 9.5)*(N_PileUpInteractions < 10.5)*(0.625159994865))+";
cut_mc += "((N_PileUpInteractions > 10.5)*(N_PileUpInteractions < 11.5)*(0.400496981648))+";
cut_mc += "((N_PileUpInteractions > 11.5)*(N_PileUpInteractions < 12.5)*(0.245671305417))+";
cut_mc += "((N_PileUpInteractions > 12.5)*(N_PileUpInteractions < 13.5)*(0.149501993628))+";
cut_mc += "((N_PileUpInteractions > 13.5)*(N_PileUpInteractions < 14.5)*(0.0943735268094))+";
cut_mc += "((N_PileUpInteractions > 14.5)*(N_PileUpInteractions < 15.5)*(0.055714218504))+";
cut_mc += "((N_PileUpInteractions > 15.5)*(N_PileUpInteractions < 16.5)*(0.032273131211))+";
cut_mc += "((N_PileUpInteractions > 16.5)*(N_PileUpInteractions < 17.5)*(0.0193368300632))+";
cut_mc += "((N_PileUpInteractions > 17.5)*(N_PileUpInteractions < 18.5)*(0.0109074260718))+";
cut_mc += "((N_PileUpInteractions > 18.5)*(N_PileUpInteractions < 19.5)*(0.00646596430331))+";
cut_mc += "((N_PileUpInteractions > 19.5)*(N_PileUpInteractions < 20.5)*(0.00324352812525))+";
cut_mc += "((N_PileUpInteractions > 20.5)*(N_PileUpInteractions < 21.5)*(0.00178440502281))+";
cut_mc += "((N_PileUpInteractions > 21.5)*(N_PileUpInteractions < 22.5)*(0.00111645018356))+";
cut_mc += "((N_PileUpInteractions > 22.5)*(N_PileUpInteractions < 23.5)*(0.000602006464283))+";
cut_mc += "((N_PileUpInteractions > 23.5)*(0.000602006464283))";
cut_mc += ")";


preselectionmumu = str(lumi)+'*weight*((Pt_muon1>40)*(Pt_muon2>40)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(ST_pf_mumu>250)*(deltaR_muon1muon2>0.3)*(M_muon1muon2>50)*((abs(Eta_muon1)<2.1)||(abs(Eta_muon2)<2.1)))' + cut_mc
preselectionmunu = str(lumi)+'*weight*(((Pt_muon1>40)*(Pt_muon2<15.0)*(MET_pf>45)*(Pt_pfjet1>30)*(Pt_pfjet2>30)*(Pt_ele1<15.0)*(ST_pf_munu>250)*(abs(Eta_muon1)<2.1))*(abs(deltaPhi_muon1pfMET)>.8)*(abs(deltaPhi_pfjet1pfMET)>.5)*(FailIDPFThreshold<25.0)*(MT_muon1pfMET>50.0))' +cut_mc



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

print selections

ignores = []

opt_n = []
sample_n = []
total_n = []
tag_n = []
issignal_n = []


for s in range(len(selections)):
	bgtotal = 0.0
	#if s<9:
		 #continue;
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
			scalefactor = '*1.0'
			if 'TTBar' in x:
				scalefactor = '*1.01'
			if 'WJets' in x:
				scalefactor = '*0.86'	
			
			#if "BetaHalf" in x:
				#continue
			if 'LQToCMu' in x and use not in  x: 
				continue;
			f = TFile.Open(x)
			t = f.Get("PhysicalVariables")
			h = TH1D('h','h',2,-1,3)
			t.Project('h','1.0',sel+scalefactor)
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
		if 'Standard' in t:
			exec('line += str(float(summary_int_StandardSelections_sig_var['+str(o)+']) )+"\t"')
		if 'Standard' not in t:
			exec('line += str(float(summary_int_'+t+'_sig_var['+str(o)+']) - float(summary_int_StandardSelections_sig_var['+str(o)+']) )+"\t"')
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
		if 'Standard'  in t:
			exec('line += str(float(summary_int_StandardSelections_bg_var['+str(o)+']) )+"\t"')
		if 'Standard' not in t:
			exec('line += str(float(summary_int_'+t+'_bg_var['+str(o)+']) - float(summary_int_StandardSelections_bg_var['+str(o)+']) )+"\t"')
	print line
	fout.write(line+'\n')

fout.close()
