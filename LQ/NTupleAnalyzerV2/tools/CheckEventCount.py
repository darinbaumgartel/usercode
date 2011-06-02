import os # For direcory scanning abilities, etc


### This portion reads the NTupleInfo.csv file and gets the information ###
import csv
csvfile = open('NTupleInfo.csv','r')
table=[]

for row in csv.reader(csvfile):
	if row[0][0]=='#':
		continue
	table.append(row)
for r in range(1,len(table)):
	for c in range(1,len(table[0])):
		table[r][c]=(table[r][c])
table2= map(list,zip(*table[1:]))
for x in range(0,len(table2)):
	exec (table[0][x]+'='+`table2[x]`)	
for x in range(0,len(HLTBit)):
	HLTBit[x]=int(HLTBit[x])
	SigOrBG[x]=int(SigOrBG[x])

totals = []
for x in range(len(SignalType)):

	total = 0
	path = CastorDirectory[x]	
	FullList = os.popen('nsls '+path).readlines()
	print SignalType[x]
	dirList = []
	for y in FullList:
		thistype = y[0:len(SignalType[x])]
		if SignalType[x] ==thistype:
			dirList.append(y)
	nn = 0
	for y in dirList:
		os.system('stager_get -M '+path+'/'+y.replace('\n',''))
		os.system('sleep .2')
		f = open('temp_'+str(nn)+'_'+SignalType[x]+'.C','w')
		f.write('{\n\ngROOT->ProcessLine(\"gROOT->Reset()\");\nTFile *f = TFile::Open("root://castorcms/'+path+'/'+y.replace('\n','')+'");\nTH1F* h = (TH1F*)f.Get("/LJFilter/EventCount/EventCounter");\nstd::cout<<h->GetBinContent(1)<<std::endl;\n\ngROOT->ProcessLine(".q");}\n\n')
		f.close()
#		os.system('cat temp_'+str(nn)+'_'+SignalType[x]+'.C')
		os.system('root -l temp_'+str(nn)+'_'+SignalType[x]+'.C > log_'+SignalType[x]+'_'+str(nn)+'.txt &')
		nn =nn + 1



logs = os.popen('ls log_*').readlines()

working = 99
while working != 0:
	finished = 0
	working = 0
	for x in logs:
		thisinfo = os.popen('cat '+x).readlines()
	#	print thisinfo
		if len(thisinfo)==3:
			finished +=1
		if len(thisinfo)==2:
			working +=1

	print 'Jobs finsihed: ' +str(finished)
	print 'Jobs in Progress: '  + str(working)




