import os
import sys

f = open('OutputSysCards.txt','r')

cardinfo = []
for line in f:
	cardinfo.append(line)
sels = []

for l in cardinfo:
	if ':' in l:
		continue
	if len(l)<5:
		continue
	sel = l.split(',')[0]
	if sel not in sels:
		sels.append(sel)

errtypes = []

error_places = []
for l in cardinfo:
	ll = l.split(',')
	n = 0
	for y in ll:
		n += 1
		if 'E:' in y:
			e = y.split(':')[-1]
			if e.replace('\n','') not in errtypes and 'Stat' not in e:
				error_places.append(n)
				errtypes.append(e.replace('\n',''))

shortcards = []
for s in sels:
	shortcard = ''
	for l in cardinfo:
		ls =  l.split(',')
		if ':' in l:
			sample = ls[0]
		if s in l and ':' not in l:
			shortcard += sample + ','+l+'\n'
	shortcards.append(shortcard)
	
	#print shortcard
	
higgscards =[]
for x in shortcards:
	higgscard = ''
	imax = 0
	jmax = 0
	kmax = 0
	count = 0
	x = x.split('\n')
	bgs = []
	bgrates = []
	srate = '' 
	for y in x:
		print y
		if 'B:' in y:
			#print y
			jmax += 1
			bgs.append(y.split(',')[0].replace('B:',''))
			snip = y.split(',')
			for part in snip:
				if 'R_' in part:
					bgrates.append(part.split('_')[-1])

							
		if 'S:' in y:
			for s in sels:
				if s in y:
					thissel = s
			imax += 1
			line = y.split(',')
			for a in line:
				if '_' not in a and ';' not in a:
					kmax += 1
			snip = y.split(',')
			for part in snip:
				if 'R_' in part:
					srate = part.split('_')[-1]	
					srateerr = part.split('_')[-2]
		if ';' in y:
			kmax += 1
		if 'D:' in y:
			
			count = y.split(',')[-1]
	processline = thissel
	processline2 = '0'
	for b in bgs:
		processline += ' '+b
		processline2 += ' 1'
	
	rateline = 'rate ' +srate
	for r in bgrates:
		if float(r) == -1:
			r = '0.0' 
		rateline += ' ' + r
	for b in bgs:
		if 'stat_'+b not in errtypes:
			errtypes.append('stat_'+b)
			error_places.append(3)
	if 'stat_sig' not in errtypes:
		errtypes.append('stat_sig')
		error_places.append(3)

	errmethods = []
	for e in errtypes:
		if 'stat' not in e:
			errmethods.append('lnN')
		else:
			errmethods.append('gmN')
	
	errormatrix = []

	s_errors = []
	for y in x:
		if 'S:' in y:
			s_errors = y.split(',')

	b_errors = []
	for b in range(len(bgs)):
		these_b_errors = []
		for y in x:
			if bgs[b] in y:
				these_b_errors = y.split(',')
				print these_b_errors
		b_errors.append(these_b_errors)
		
	higgscard += '\n\n'+thissel+'.txt\n\n'
	higgscard += 'imax '+str(imax) +'\n'
	higgscard += 'jmax '+str(jmax) +'\n'
	higgscard += 'kmax '+str(kmax) +'\n\n'
	higgscard += 'bin 1 \n'
	higgscard += 'observation '+str(count)+'\n\n'
	higgscard += 'bin '+' 1'*(imax + jmax) + '\n'
	higgscard += 'process '+processline + '\n'
	higgscard += 'process '+processline2+'\n'
	higgscard += rateline + '\n'
	
	for e in range(len(errtypes)):
		if 'DiBoson' in errtypes[e] and 'BetaHalf' not in thissel:
			continue		
			
		if 'BetaHalf' in thissel:	
			higgscard += errtypes[e]+'  '+(str(errmethods[e])).replace('gmN','lnN')+'  '
		else:
			higgscard += errtypes[e]+'  '+str(errmethods[e])+'  '
			
		if 'stat_' not in errtypes[e]:
			higgscard+=str(s_errors[error_places[e]]) 
			for b in range(len(bgs)):
				higgscard += ' '*(b+1) +str(b_errors[b][error_places[e]]).replace(';',' ') + ' '
				
				
		elif 'stat_sig' in errtypes[e] and 'BetaHalf' not in thissel:
			higgscard+= str(s_errors[2].replace(';','  '))+ ' - '*len(bgs)
		elif 'stat_' in errtypes[e] and 'stat_sig' not in errtypes[e] and 'BetaHalf' not in thissel:
			if 'DiBoson' in errtypes[e] and 'BetaHalf' not in thissel:
				continue
			for b in range(len(bgs)):
				if bgs[b] not in errtypes[e]:
					continue
					
				higgscard +=  str(b_errors[b][2]).replace(';',' - '*(b+1)) + ' - '*(len(bgs) - (b+1)) 

				
		elif 'stat_sig' in errtypes[e] and 'BetaHalf' in thissel:
			higgscard+= str(s_errors[3].split('_')[-2])+ ' - '*len(bgs)
			
		elif ('stat_' in errtypes[e]) and ('stat_sig' not in errtypes[e]) and ('BetaHalf' in thissel):
			if 'DiBoson' in errtypes[e] and 'BetaHalf' not in thissel:
				continue
			for b in range(len(bgs)):
				if bgs[b] not in errtypes[e]:
					continue
					
				higgscard +=  ' - '*(b+1)+ str(b_errors[b][3]).split('_')[-2]+ ' - '*(len(bgs) - (b+1)) 
			
			
		else:
			higgscard += ' -  '
		higgscard += '\n'
			
	
	higgscard += '\n\n'
	print higgscard
	
	higgscards.append(higgscard)
	
fout = open('FinalCards.txt','w')
for x in higgscards:
	fout.write(x)
fout.close()
