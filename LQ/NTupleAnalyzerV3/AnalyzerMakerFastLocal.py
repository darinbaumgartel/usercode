#################################################################################################
##########                    N Tuple Analyzer Script Producer                        ###########
##########      Store NTuple Info In NTupleInfo.csv File in current Directory         ###########
##########      Darin Baumgartel - May 31, 2011 - darin.carl.baumgartel@cern.ch      ###########
#################################################################################################

import os # For direcory scanning abilities, etc
from time import strftime
import sys



a = sys.argv
tagname = 'default'
json = ''
for x in range(len(a)):
	if a[x] == '-i':
		ifile = a[x+1]
	if a[x] == '-py':
		pyfile = a[x+1]
	if a[x] == '-t':
		tagname = a[x+1]
	if a[x] == '-j':
		json = a[x+1]

if pyfile == ''  or ifile == '' or json == '':
	print 'Must specify input python script, .csv file, and json file, e.g.:\n\npython AnalyzerMakerFast.py -i NTupleInfoSpring2011.csv -py NTupleAnalyzer.py \n   Exiting   \n\n'
	sys.exit()

import csv
csvfile = open(ifile,'r')
table=[]

for row in csv.reader(csvfile):
	if len(row) == 0:
		continue
	if row[0][0]=='#':
		continue
	table.append(row)
for r in range(1,len(table)):
	for c in range(1,len(table[0])):
		table[r][c]=(table[r][c])
table2= map(list,zip(*table[1:]))
for x in range(0,len(table2)):
	exec (table[0][x]+'='+`table2[x]`)	

###----------------------------------------------------------------------###


c2file = pyfile.split('/')[-1]

now=str(strftime("%Y-%m-%d-%H:%M:%S"))
now = now.replace(" ","")
now = now.replace("\t","")
now = now.replace("-","_")
now = now.replace(":","_")

# initialize file that stores root processes to be run

f_sub = open("sub_AllAnalyzer.csh", 'w')
f_sub.write('#!/bin/csh')


thisdir = os.popen('pwd').readlines()[0].replace('\n','')
person = os.popen('whoami').readlines()[0].replace('\n','')
thiseos = thisdir+'/'+c2file.replace('.py','')+'_'+tagname+'_'+now

os.system(' mkdir '+ thiseos)
print ' \n-------------------------------------------------------------------'
bjobs = []

possiblemasterdirs = []
posdir = ''
for p in EOSDirectory[0]:
	posdir += p
	possiblemasterdirs.append(posdir)

masterdir = ''
for p in possiblemasterdirs:
	isgood=1
	for c in EOSDirectory:
		if p not in c:
			isgood = 0
	if isgood==1 and p[-1]=='/':
		masterdir=p

print '\n\n Reading File List, please wait ...\n\n'



def GetGoodFiles(edir):

	def GetSpaceUse():
		command =  'cmsLs -R '+edir + '| grep root'
		dircont = [ x.replace('\n','') for x in os.popen(command).readlines()]
		print len(dircont)
		return dircont

	i = GetSpaceUse()

	def identifier(f):
		fsp = f.split('_')
		i = ''
		for x in range(len(fsp)):
			i += fsp[x] + '_'
			if x > (len(fsp)-4):
				break
		return i
	files = []
	for x in i:
		if ".root" not in x:
			continue
		x = x.split()
		size = int(x[1])
		name = x[-1]
		ident = identifier(name)
		files.append([size,name,ident])

	checkedfiles = []


	def checkid(f):
		checkedfiles = []
		goodfiles = []
		dups = []
		for x in files:
			if x[-1]==f[-1]:
				dups.append(x)
				checkedfiles.append(x)

		maxsize = -1	
		for x in checkedfiles:
			if x[0]>maxsize:
				maxsize=x[0]
			 	bestfile=x

		for c in checkedfiles:
			if c == bestfile:
				goodfiles.append(c[1])
				# print c[1]

		return [goodfiles,checkedfiles]

	allgoodfiles = []
	allcheckedfiles = []
	nfiles = len(files)
	for f in range(nfiles):
		if f%1000 == 0: 
			print 'Checking file',f,'of',nfiles,'.'

		[gg,cc] = checkid(files[f])
		if files[f] not in allcheckedfiles:
			allgoodfiles += gg
		allcheckedfiles += cc

	return allgoodfiles

masterdirlist = masterdir.replace('/','__')+'.txt'

if masterdirlist not in os.listdir('.') or  '--FileRefresh' in sys.argv:
	print '\n','(Re)'*('--FileRefresh' in sys.argv)+'Generating file list',masterdirlist,' for files in ',masterdir,'\n'
	# allfiles = os.popen('cmsLs  -R '+masterdir+' | grep ".root" | awk \'{print $5}\'').readlines()
	allfiles = GetGoodFiles(masterdir)
	print len(allfiles)
	fmas = open(masterdirlist,'w')
	for x in allfiles:
		fmas.write(x+'\n')
	fmas.close()
else:
	print '\n Reading files from: ',masterdirlist
	print '\n *** NOTE: You can refresh the file list at anytime with the argument: --FileRefresh\n\n'
	allfiles = [line for line in open(masterdirlist,'r')]

# sys.exit()

jobs = []

for x in range(len(SignalType)):

	signal = SignalType[x]
	path = EOSDirectory[x]	
	sigma = Xsections[x]
	Norig = N_orig[x]
	group = Group[x]


	fcont = []
	for subfile in allfiles:
		if path.replace('\n','') in subfile and signal in subfile:
			fcont.append(subfile)

	print 'Preparing '+ SignalType[x],':', len(fcont),'files.'

	for f in fcont:
		jobs.append('python '+pyfile.replace('\n','')+' -f '+f.replace('\n','')+' -s '+sigma+' -n '+Norig+' -j '+json + ' -l 1.0 -d '+thiseos.replace('\n',''))

def MakeJobs(njobs):
	Nj = 0

	jlist = []
	jstr = str(os.popen('ls '+thiseos).readlines())
	for j in jobs:
		filesig = (((j.split(' -f ')[-1]).split(' ')[0]).split('/')[-1]).replace('.root','')
		if filesig not in jstr:
			jlist.append(j)

	bsubs = []

	jobgroups = []
	jobset = []
	nj=0
	for ii in range(len(jlist)):
		nj += 1
		if nj > njobs:
			jobgroups.append(jobset)
			jobset = []
			nj=0
		else:
			jobset.append(jlist[ii])
	if len(jobset)>0:
		jobgroups.append(jobset)

	for j in jobgroups:
		Nj += 1
		subber = open(thiseos+'/subber_'+str(Nj)+'.tcsh','w')
		subber.write('#!/bin/tcsh\n\ncd /afs/cern.ch/work/d/darinb/CMSSW_4_2_8/src\ncmsenv\n\n')
		subber.write('\ncd '+thisdir+'\n\n')
		for x in j:
			subber.write(x+'\n')

		subber.close()
		os.system('chmod 777 '+thiseos+'/subber_'+str(Nj)+'.tcsh')
		os.system( 'bsub -q 8nh -o /dev/null -e /dev/null -J job_'+str(Nj)+'_'+now+' < '+thiseos+'/subber_'+str(Nj)+'.tcsh')
		os.system('sleep 0.4')
	return len(jlist)

keep_going = 1

while keep_going != 0:
	print 'Launching jobs...'
	keep_going = MakeJobs(10)
	if keep_going == 0:
		break

	print 'Jobs remaining, waiting for jobs to finish'

	done=0
	ncheck = 0
	while done!=1:
		os.system('sleep 120')
		jobinfo = os.popen('bjobs -w | grep '+now).readlines()
		if 'PEND' not in str(jobinfo):
			ncheck += 1
		jobinfo = len(jobinfo)
		jobsleft = jobinfo -1
		if jobsleft == -1:
			done = 1
		if jobsleft>=0:
			print  str(jobsleft+1) +' jobs remaining.'

		if ncheck > 65:
			 os.system('bjobs -w | awk \'{if (NR!=1) print $1}\' | xargs bkill')
			 os.system('sleep 20')
			 print "\nJobs taking too long. Killing remaining jobs. \n"
			 break

os.system('rm '+thiseos+'/subber_*tcsh')

if 'Counter' in pyfile:
	txtfiles = os.popen('ls -1 '+thiseos+' | grep txt').readlines()
	countlog = open(thisdir+ '/'+ifile.replace('.','_EventCountLog.'),'w')
	for x in range(len(SignalType)):
		print 'Collecting results for',SignalType[x]
		sigfiles = []
		for ftxt in txtfiles:
			if SignalType[x] in ftxt:
				sigfiles.append(ftxt)
		OCount = 0
		for s in sigfiles:
			scount = (os.popen('cat '+thiseos+'/'+s).readlines()[0]).replace(' ','')
			scount = scount.replace('\n','')
			scount = float(scount)
			OCount += scount

		Ostr = str(SignalType[x]) +' , '+ str(OCount)+'\n'
		countlog.write(Ostr)
	countlog.close()
	print 'Output is in ',thisdir+ '/'+ifile.replace('.','_EventCountLog.'),' ...'
	os.system('cat '+thisdir+ '/'+ifile.replace('.','_EventCountLog.'))

if 'Analyz' in pyfile:
	groups = []
	for x in range(len(SignalType)):
		if Group[x] not in groups:
			groups.append(Group[x])
	Contents = []
	for g in groups:
		Contents.append([])
	for g in range(len(groups)):
		for x in range(len(SignalType)):
			if groups[g] == Group[x]:
				Contents[g].append(SignalType[x])
	os.system('mkdir '+thiseos+'/SummaryFiles')
	for g in range(len(groups)):
		haddstring = 'hadd '+thiseos+'/SummaryFiles/'+groups[g]+'.root'
		for c in Contents[g]:
			haddstring += ' '+thiseos+'/*'+c.replace('-','_')+'*root'+' '
		print haddstring
		os.system(haddstring)


# subjobs = ''
# if '--autorun' in sys.argv:
# 	subjobs='y'
# while subjobs != 'y' and subjobs != 'n':
# 	subjobs = raw_input('\n\n  Would you like to automatically submit and check jobs now? (answer y/n):  ')
# if subjobs == 'n':
# 	print '\n\n Jobs can be submitted now using the submission command:\n\n    ./sub_AllAnalyzer.csh\n'
# 	print '\n If you wish to test functionality, run a single root process like:\n'
# 	print '  root -l RootProcesses_TTJetspart1of4  (or whatever RootProcesses file you have available)\n\n'
# 	sys.exit()

# #os.system('./sub_AllAnalyzer.csh')   ##FIXME

# def gather_remaining_jobs():
# 	listofrootoutputfiles = [ x.replace('\n','') for x in os.popen('cat sub*part**.csh | grep ".root" | awk \'{print $2}\'').readlines() ]
# 	listofcompletedrootfiles = os.listdir(thiseos)
	
# 	for_submission = []
	
# 	print 'Total: ', len(listofrootoutputfiles), '       Finished: ',len(listofcompletedrootfiles)
# 	for x in listofrootoutputfiles:
# 		if x not in listofcompletedrootfiles:
# 			for_submission.append(x)
			
# 	corresponding_csh = []
# 	for x in for_submission:
# 		corresponding_csh.append( (os.popen('grep '+x+' sub*part*csh').readlines()[0]).split(':')[0]  )

# 	bsub_commands = []
	
# 	for x in corresponding_csh:
# 		bsub_commands.append( (os.popen('grep '+x+' sub_AllAnalyzer.csh').readlines()[0]).split(':')[-1]  ) 
	
# 	for b in bsub_commands:
# 		os.system(b)
# 		os.system('sleep .2')
		
# 	if bsub_commands == []:
# 		return 1
# 	else:
# 		return 0


# def WaitForJobs():
# 	done=0
# 	n = 0
# 	while done!=1:
# 		os.system('sleep 120')
# 		jobinfo = os.popen('bjobs -w | grep '+now).readlines()
# 		if 'PEND' not in str(jobinfo):
# 			n += 1
# 		jobinfo = len(jobinfo)
# 		jobsleft = jobinfo -1
# 		if jobsleft == -1:
# 			done = 1
# 		if jobsleft>=0:
# 			print  str(jobsleft+1) +' jobs remaining.'

# 		if n > 65:
# 			 os.system('bjobs -w | awk \'{if (NR!=1) print $1}\' | xargs bkill')
# 			 os.system('sleep 20')
# 			 print "\nJobs taking too long. Killing remaining jobs. \n"
# 			 break

# 	print 'Checking the file output...\n\n'


# def LoopUntilFinished():
# 	execute = 0
# 	while execute != 1:
# 		execute = gather_remaining_jobs()
# 		WaitForJobs()
		
# LoopUntilFinished()

# groups = []
# for x in range(len(SignalType)):
# 	if Group[x] not in groups:
# 		groups.append(Group[x])
# Contents = []
# for g in groups:
# 	Contents.append([])
# for g in range(len(groups)):
# 	for x in range(len(SignalType)):
# 		if groups[g] == Group[x]:
# 			Contents[g].append(SignalType[x])
# os.system('mkdir '+thiseos+'/SummaryFiles')
# for g in range(len(groups)):
# 	haddstring = 'hadd '+thiseos+'/SummaryFiles/'+groups[g]+'.root'
# 	for c in Contents[g]:
# 		haddstring += ' '+thiseos+'/*'+c.replace('-','_')+'*root'+' '
# 	print haddstring
# 	os.system(haddstring)

# print '-------------------------------------------------------------------'
# print '         Cleaning up temporary files\n'
# from subprocess import call
# print '         Removing Root Run Processes' 
# call('rm RootProcess*',shell=True)
# print '         Removing Temporary C/h modules'
# call('rm *part*',shell=True)
# print '         Removing batch submission scripts'
# call('rm sub*csh',shell=True)
# print (' ')
# os.system('rm '+thiseos+'/NTupleAnalyzer*part*root')
# print '-------------------------------------------------------------------'

# print ('\n\n'+140*'*'+ '\n\n      Analysis Complete. A full set of output files can be found in  \n\n       '+thiseos+'/SummaryFiles\n')
# os.system('ls '+thiseos+'/SummaryFiles')
# print ('\n\n'+140*'*'+ '\n\n')

# if neucopy == False:
# 	sys.exit()

# print ('Please wait - transfering output additionally to neu machine. ')
# neudir =  '~/neuhome/LQAnalyzerOutput/'
# os.system('rm '+thiseos+'/*.*')
# os.system('cp -r '+thiseos+' '+neudir)
# os.system('rm '+thiseos+'/SummaryFiles/*root')

# print ('Transfer Complete. ')

