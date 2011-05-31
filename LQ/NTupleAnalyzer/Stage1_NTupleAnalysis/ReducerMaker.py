f0 = open('NTupleAnalyzerReducer.h','w')
f0.write('{\n\n')
f1 = open('NTupleAnalyzer.h','r')


variables = []
for line in f1:
	if 'SetBranchAddress' in line:
		var = (line.split('\"')[1])
		variables.append( ((var.replace('\n','')).replace('\r','')).replace(' ','')  )
#print(variables)

usevariables = []
for x in variables:

	use =0
	f2 = open('NTupleAnalyzer.C','r')
	for line in f2:
		if x in line:	
#			print(x)
			use = 1
	if use ==1:
		f0.write('fChain->SetBranchStatus("'+x+'",1);\n')
	else:
		f0.write('fChain->SetBranchStatus("'+x+'",0);\n')

f0.write('\n\n}\n')
f0.close()
