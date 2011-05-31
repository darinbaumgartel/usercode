# Register your signal/BG types (these should also be directories) below
SignalType=['LQ300','LQ400','LQ500','TTbar','WW','Zmumu','QCD_100_to_250','QCD_250_to_500','QCD_500_to_1000','QCD_1000_to_inf'];
# Register the cross-sections in pb for all types above
Xsections=[1.21,.206,.0463,90.0,28.0,2350.0,329906.0,3364.0,59.5,.3401]
# Register the appropriate HLT Bit below
HLTBit=[1,1,1,1,1,1,1,1,1,1]#,31,31,31,31,31,31,31,31,31,31,31,31] # HLT_Mu3
# Register whether signal or background (signal =1, background =0)
SigOrBG=[1,1,1,0,0,0,0,0,0,0]#,0,0,0,0,0,0,0,0,0,0,0,0]
# Below is your directory to your root file input
TMVAMacrosDirectory='/home/darinb/scratch0/LQ/LQ_Optimization/TMVA/macros/LQ_Macros_betaHalf/TMVA_LQ_Inputs.root'

variables=['tmva_ST_tc','tmva_MT_mumet_tc','tmva_M_mu1j1','tmva_M_mu1j2','tmva_MT_j1met_tc','tmva_MT_j2met_tc']              

minvars=[491,6.812 ,172.675,196.913,5.86926,.10852]
maxvars=[3446.7,1696.3,2402.56157,2296.6,1904.444,936.755]

WhatType=['Background','Signal']
import os
basic_r = open("BasicAnalysis_Template.C")
basic_w = open("BasicAnalysis_2.C", 'w')
basic_w.write('{\nfloat S_orig_weighted=0.0;\nfloat B_orig_weighted=0.0;')
basic_w.write('\nint ii=0;\nint jj=0;\nint kk=0;\nint SigOrBG=0;\n\n \nfloat STCut;\nfloat MT_mumetCut;\nfloat S=0;\nfloat B=0;\nint S_pass_MC;\nint B_pass_MC;\nint S_orig_MC=0;\nint B_orig_MC=0;\n\n')



basic_w.close()
basic_w2 = open("BasicAnalysis_2.C", 'a')
for line in basic_r.readlines():
	basic_w2.write(line)
	if 'list_tracer_000' in line:
		for z in range(len(SignalType)):
			basic_w2.write('\nint use_'+SignalType[z]+' =1;\n')
	if 'list_tracer_001' in line:
		for z in range(len(SignalType)):
			basic_w2.write('\nif (use_'+SignalType[z]+' ==1){')
			basic_w2.write('\n\tstd::cout<<\"Evaluating For '+WhatType[SigOrBG[z]]+' Type '+SignalType[z] +'\"<<std::endl;')
			basic_w2.write('\n\tSigOrBG='+`SigOrBG[z]`+';')
			basic_w2.write('\n\tfloat '+SignalType[z]+'_passingEvents;')

			basic_w2.write('\n\t\t\t'+SignalType[z]+'_passingEvents=0.0;\n\t')
			basic_w2.write('\n\tTChain '+SignalType[z]+'tree(\"'+SignalType[z]+'\");')
			basic_w2.write('\n\t'+SignalType[z]+'tree->Add(\"'+TMVAMacrosDirectory+'\");')
			basic_w2.write('\n\tTTree *'+SignalType[z]+'Signal = (TTree*)'+SignalType[z]+'tree;')
			basic_w2.write('\n\tfloat '+SignalType[z]+'_N;')
			basic_w2.write('\n\tfloat '+SignalType[z]+'_weight;')
			basic_w2.write('\n\t'+SignalType[z]+'Signal->SetBranchAddress(\"tmva_weight\",&'+SignalType[z]+'_weight);')
			basic_w2.write('\n\t'+SignalType[z]+'Signal->SetBranchAddress(\"TotalEvents_OriginalAndPrecut\",&'+SignalType[z]+'_N);')
			basic_w2.write('\n\t'+SignalType[z]+'Signal->GetEntry(1);')
			basic_w2.write('\n\tif (SigOrBG==1) S_orig_MC=S_orig_MC+'+SignalType[z]+'_N;')
			basic_w2.write('\n\tif (SigOrBG==0) B_orig_MC=B_orig_MC+'+SignalType[z]+'_N;')
			basic_w2.write('\n\tif (SigOrBG==1) S_orig_weighted=S_orig_weighted+'+SignalType[z]+'_N*'+SignalType[z]+'_weight;')
			basic_w2.write('\n\tif (SigOrBG==0) B_orig_weighted=B_orig_weighted+'+SignalType[z]+'_N*'+SignalType[z]+'_weight;')
			basic_w2.write('\n\tstd::cout<<B_orig_weighted<<std::endl;')
			basic_w2.write('\n\tfloat tmva_Precut_ALL=0.0;')
			basic_w2.write('\n\t'+SignalType[z]+'Signal->SetBranchAddress(\"tmva_precut_ALL\",&tmva_Precut_ALL);')
			
			for q in range(len(variables)):
				basic_w2.write('\n\tfloat '+variables[q]+'=0.0;')
				basic_w2.write('\n\t'+SignalType[z]+'Signal->SetBranchAddress(\"'+variables[q]+'\",&'+variables[q]+');')
				

			basic_w2.write('\n\t\tfor (ii=0;ii<'+SignalType[z]+'_N; ii++) {')
			basic_w2.write('\n\t\t\t'+SignalType[z]+'Signal->GetEntry(ii);')
			
			basic_w2.write('\n\t\t\t\t\tif((tmva_Precut_ALL>0.0)')
			for q in range(len(variables)):			
				basic_w2.write('&&('+variables[q]+'>'+`minvars[q]`+')&&('+variables[q]+'<'+`maxvars[q]`+')')
				
			basic_w2.write('){')
			basic_w2.write('\n\t\t\t\t\t\tif (SigOrBG==1) S= S+'+SignalType[z]+'_weight;')
			basic_w2.write('\n\t\t\t\t\t\tif (SigOrBG==0) B= B+'+SignalType[z]+'_weight;')
			basic_w2.write('\n\t\t\t\t\t\tif (SigOrBG==1) S_pass_MC= S_pass_MC+1;')
			basic_w2.write('\n\t\t\t\t\t\tif (SigOrBG==0) B_pass_MC= B_pass_MC+1;')
			basic_w2.write('\n\t\t\t\t\t\tif (SigOrBG==1) '+ SignalType[z]+'_passingEvents= '+ SignalType[z]+'_passingEvents +'+SignalType[z]+'_weight;')
			basic_w2.write('\n\t\t\t\t\t\tif (SigOrBG==0) '+ SignalType[z]+'_passingEvents= '+ SignalType[z]+'_passingEvents +'+SignalType[z]+'_weight;')
			basic_w2.write('\n\t\t\t\t\t}')
			basic_w2.write('\n\t\t\t\t}')
			basic_w2.write('\n\t\t\t}')

	if 'list_tracer_002' in line:


		basic_w2.write('std::cout<<"Significance maximization cuts results as follows:"<<std::endl;\n')
		basic_w2.write('std::cout<<"    "<<std::endl;\n')

		
		basic_w2.write('std::cout<<"    "<<std::endl;\n')
		basic_w2.write('std::cout<<"    "<<std::endl;\n')
		basic_w2.write('std::cout<<"*** Log of passing events at optimal cut for each signal/BG type"<<std::endl;\n\n')			
		
		for z in range(len(SignalType)):
			basic_w2.write('\nif (use_'+SignalType[z]+' ==1){')
			basic_w2.write('\n\tstd::cout<<"'+WhatType[SigOrBG[z]]+'\\t\\t\\t'+SignalType[z]+'\\t\\t\\t"<<'+SignalType[z]+'_passingEvents<<std::endl;\n\t}\n')
			
		basic_w2.write('std::cout<<"    "<<std::endl;\n')
		basic_w2.write('std::cout<<"    "<<std::endl;\n')
		basic_w2.write('std::cout<<"Original weighted event numbers were:"<<std::endl;\n\n')
		basic_w2.write('std::cout<<"    Signal:  "<<S_orig_weighted<<std::endl;\n\n')
		basic_w2.write('std::cout<<"Background:  "<<B_orig_weighted<<std::endl;\n\n')

		
basic_r.close()
basic_w2.write('\n}')
basic_w2.close()
