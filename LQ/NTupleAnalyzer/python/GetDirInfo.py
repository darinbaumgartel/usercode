bookkeepingdir = '/home/darinb/scratch0/LQ/Summer2011/bookkeeping'
import os
bookkeepingdir = ((os.popen('pwd')).readline()).replace('python\n','bookkeeping')
print ('\nUsing information in bookkeeping direcotory: \n        '+  bookkeepingdir + '\n\n')
dirfile = open(bookkeepingdir+'/DirectoryInformation.csv')
for line in dirfile:
	if "#" in line:
		continue
	else:
		WhatDirectory = (line.split(","))[0]
		WhereIsIt = (line.split(","))[-1]
		WhereIsIt = WhereIsIt.replace("\n","")
		exec(WhatDirectory+ " = \'" +WhereIsIt+"\'")


