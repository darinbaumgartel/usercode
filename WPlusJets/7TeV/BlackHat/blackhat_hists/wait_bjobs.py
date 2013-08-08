import os
import sys

user = (os.popen('whoami').readlines()[0]).replace('\n','')

def GetBJobCount():
	_c = os.popen('bjobs -w | grep '+user+' | wc -l ').readlines()[0]
	_c = _c.replace('\n','')
	_c = int(_c)
	return _c


n = 9999999

while n > 100:
	print 'Waiting for bjobs to be less than 100. Current bjobs count:',n
	n = GetBJobCount()
	os.system('sleep 60')

print 'Bjobs reduced sufficiently. Moving on....'
