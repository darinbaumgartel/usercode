# Get NTuple Information from CSV Table
import csv
from GetDirInfo import *
csvfile = open(AnalysisDirectory+'/bookkeeping/NTupleInfo.csv','r')
table=[]

for row in csv.reader(csvfile):

	if row[0][0]=='#':
		continue
	table.append(row)
#	print row

for r in range(1,len(table)):
	for c in range(1,len(table[0])):
		table[r][c]=float(table[r][c])
table2= map(list,zip(*table[1:]))
for x in range(0,len(table2)):
	exec (table[0][x]+'='+`table2[x]`)	
for x in range(0,len(HLTBit)):
	HLTBit[x]=int(HLTBit[x])
	SigOrBG[x]=int(SigOrBG[x])

