import os
import sys

from TMVASetup import *


dircontents = os.listdir(directory)
longdircontents = []
for x in range(len(dircontents)):
	longdircontents.append( directory + '/'+dircontents[x])


N = -1
for stype in signaltags:
	N += 1

	signals = []
	for x in dircontents:
		if stype in x:
			signals.append(x.replace('.root',''))
	for signal in signals:

		f = open('tmva/test/TMVAClassification_BAK.C','r')
		fout = open('TMVAClassification_'+signal+'.C','w')
		frun = open('tmvarun_'+signal+'.sh','w')
		frun.write('#!/bin/sh\n\n')
		frun.write('rm tmva/test/TMVAClassification.C\ncp TMVAClassification_'+signal+'.C tmva/test/TMVAClassification.C\n cd tmva/test\nroot -l TMVAClassification.C\n')
		frun.close()
		os.system('chmod 777 tmvarun_'+signal+'.sh')
		for line in f:
			if 'TString fname' in line:
				line2 = line + '\n'
				for n in range(len(dircontents)):
					line2 += (line.replace('fname','fname_'+dircontents[n].replace('.root',''))).replace('./tmva_class_example.root',longdircontents[n]) + '\n'
				line = line2
				
			if 'TFile *input' in line or 'Using input file' in line:
				line2 = ''
				for n in range(len(dircontents)):
					line2 += (line.replace('fname','fname_'+dircontents[n].replace('.root',''))).replace('input','input_'+dircontents[n].replace('.root','')) + '\n'		
				line = line2
			
			if 'TTree *signal' in line or 'factory->AddSignalTree' in line:
				line2 = ''
				line = line.replace('signalWeight','1.0')
				for n in range(len(dircontents)):
					if signal not in dircontents[n]:
						continue
					line2 += (line.replace('input','input_'+dircontents[n].replace('.root',''))).replace('signal','signal_'+dircontents[n].replace('.root','')) + '\n'		
				line2 = line2.replace('TreeS',treename)
				line = line2			
	
			if 'TTree *background' in line or 'factory->AddBackgroundTree' in line:
				line2 = ''
				line = line.replace('backgroundWeight','1.0')
				for n in range(len(dircontents)):
					keep = 0
					for background in backgroundtags:
						if background in dircontents[n]:
							keep = 1
					if keep != 1:
						continue
					line2 += (line.replace('input','input_'+dircontents[n].replace('.root',''))).replace('background','background_'+dircontents[n].replace('.root','')) + '\n'		
				line2 = line2.replace('TreeB',treename)
	
				line = line2	
	
			if 'factory->SetBackgroundWeightExpression("weight");' in line:
				line2 = line.replace('weight',weightexpression)
				line2 += line2.replace('Background','Signal') 
				
			if 'TCut mycuts' in line:
				line = 'TCut mycuts = "' +preselections[N]+ '";\n'
				
			if 'TCut mycutb' in line:
				line = 'TCut mycutb = "' +preselections[N]+ '";\n'
	
			if 'Use[' in line:
				keep = 0
				for x in methods:
					if '"'+x+'"' in line:
						keep = 1
				if keep != 1:
					line = line.replace('1;','0;')
					
			
					
			if 'factory->AddSpectator' in line:
				line = '//'+line
			
			if 'factory->AddVariable' in line:
				line = '//'+line
			
			if 'if (ReadDataFromAsciiIFormat) {' in line:
				line2 = ''
				for x in discriminatingvariables[N]:
					line2 += '\nfactory->AddVariable("'+x+'",\'F\');\n'
				line = line2 + line
		
			if 'factory->PrepareTrainingAndTestTree' in line and '//' not in line:
				line = '\n factory->PrepareTrainingAndTestTree( mycuts, "SplitMode=random:!V" );\n//'
			
	
		#newline = ''
		#replaceit = 0
		#for aline in line.split('\n'):
			#if '(TTree*)' in aline:
				#replaceit = 1
				
				#aline = aline.split()
				#source = aline[1].replace('*','')
				#sfile = (aline[3].split('->')[0]).split(')')[-1]
				#line1 = '\nTChain chain_'+source+'("'+treename+'");\n'
				#line2 = 'chain_'+source+'.Add(fname_'+(source.replace('signal_','')).replace('background','')+');\n'
				#line2 = line2.replace('__','_')
				#line3 = 'TTree *'+source+' =  (TTree*)chain_'+source+';\n'
				
				#newline += line1+line2+line3

		#if replaceit == 1:
			#line = newline
		
		
			fout.write(line)
		f.close()
		fout.close()
