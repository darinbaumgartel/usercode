
flogV = open('SysVerboseLog.txt','r')
normtag = 'StandardSelections_4p7fb_Feb03_2012'
scaletags = ['JetScaleUp','JetScaleDown','MuScaleUp','MuScaleDown','JetSmear','MuSmear']
#scaletags = ['JetScaleUp']
scaletags.append(normtag)
info = []
for line in flogV:
	info.append(line)

sel = []
sig = []
typ = []
mc = []
weight = []
tot = []
rate_err = []
for x in info:
	if len(x) < 5:
		continue
	x = x.split()
	#print x
	sel.append(x[0])
	sig.append(x[1])
	typ.append(x[2])
	mc.append(float(x[3]))
	weight.append(float(x[4]))
	tot.append(float(x[5]))
	rate_err.append(float(x[6]))
R = range(len(sel))

Lqsignals = []
Backgrounds = []

allsigs = []

for i in R:	
	if sig[i] not in allsigs:
		allsigs.append(sig[i])

for x in allsigs:
	if 'LQ' in x:
		Lqsignals.append(x)
	else:
		Backgrounds.append(x)


jetzpos = []
muzpos = []
unscaled = 0.0

mumuprejetscalez = 1.0
mumupremuscalez = 1.0

munuprejetscalew = 1.0
munuprejetscalett = 1.0
munupremuscalew = 1.0
munupremuscalett = 1.0

for i in range(len(sel)):
	if 'PreSel' not in sel[i]:
		continue
	if 'MuMu' not in sel[i]: 
		continue
	if 'ZJet' in sig[i] and 'JetScale' in typ[i]:
		jetzpos.append(tot[i])
	if 'ZJet' in sig[i] and 'MuScale' in typ[i]:
		muzpos.append(tot[i])	
	if 'ZJet' in sig[i] and 'StandardSelection' in typ[i]:
		unscaled = (tot[i])	
for x in jetzpos:
	if abs(x - unscaled) > mumuprejetscalez:
		mumuprejetscalez = (abs(x - unscaled) + unscaled)/unscaled
for x in muzpos:
	if abs(x - unscaled) > mumupremuscalez:
		mumupremuscalez = (abs(x - unscaled) + unscaled)/unscaled

jetwpos = []
muwpos = []
jetttpos = []
muttpos = []
unscaledw = 0.0
unscaledtt = 0.0

for i in range(len(sel)):
	if 'PreSel' not in sel[i]:
		continue
	if 'MuNu' not in sel[i]: 
		continue
	if 'WJet' in sig[i] and 'JetScale' in typ[i]:
		jetwpos.append(tot[i])
	if 'WJet' in sig[i] and 'MuScale' in typ[i]:
		muwpos.append(tot[i])	
	if 'TTBar' in sig[i] and 'JetScale' in typ[i]:
		jetttpos.append(tot[i])
	if 'TTBar' in sig[i] and 'MuScale' in typ[i]:
		muttpos.append(tot[i])			
	if 'WJet' in sig[i] and 'StandardSelection' in typ[i]:
		unscaledw = (tot[i])	
	if 'TTBar' in sig[i] and 'StandardSelection' in typ[i]:
		unscaledtt = (tot[i])	
for x in jetwpos:
	if abs(x - unscaledw) > munuprejetscalew:
		munuprejetscalew = (abs(x - unscaledw) + unscaledw)/unscaledw
for x in muwpos:
	if abs(x - unscaledw) > munupremuscalew:
		munupremuscalew = (abs(x - unscaledw) + unscaledw)/unscaledw
for x in jetttpos:
	if abs(x - unscaledtt) > munuprejetscalett:
		munuprejetscalett = (abs(x - unscaledtt) + unscaledtt)/unscaledtt
for x in muttpos:
	if abs(x - unscaledtt) > munupremuscalett:
		munupremuscalett = (abs(x - unscaledtt) + unscaledtt)/unscaledtt
		
from math import sqrt
for B in Backgrounds:
	print 'B:'+B+',R:Rate,E:Stat,E:Jes,E:Mes,E:Jres,E:Mres,E:Mod,E:Mrii,E:Lum'
	N = 0 
	w = 0
	for S in Lqsignals:
		for t in scaletags:
			exec('i_'+t+' = 0')
			
		for i in R:
			if (sel[i] != S or sig[i] !=B):
				continue
			for t in scaletags:
				if t == typ[i]:
					exec ('i_'+t+'= '+str(tot[i]))		
					exec ('ie_'+t+'= '+str(rate_err[i]))	
			#print sel[i]+'  '+sig[i]+'  '+typ[i] + '  '+str(tot[i] )
			if typ[i] == 'StandardSelections_4p7fb_Feb03_2012':
				N = mc[i]
				w = weight[i]
		jes = 1.0
		mes = 1.0
		jres = 1.0
		mres = 1.0
		mod = 1.0
		mrii = 1.0
		lum = 1.0
		rate = -1.0
		rateerr = -1.0
		
		if i_StandardSelections_4p7fb_Feb03_2012 != 0:
			rate = i_StandardSelections_4p7fb_Feb03_2012
			rateerr = 1.0+(ie_StandardSelections_4p7fb_Feb03_2012/i_StandardSelections_4p7fb_Feb03_2012)			
			jes = 1.0+abs(i_JetScaleDown - i_StandardSelections_4p7fb_Feb03_2012)/i_StandardSelections_4p7fb_Feb03_2012		
			if (abs(i_JetScaleUp - i_StandardSelections_4p7fb_Feb03_2012)>abs(i_JetScaleDown-i_StandardSelections_4p7fb_Feb03_2012)):
				jes = 1.0+ abs(i_JetScaleUp - i_StandardSelections_4p7fb_Feb03_2012)/i_StandardSelections_4p7fb_Feb03_2012	
			mes = 1.0+abs(i_MuScaleDown - i_StandardSelections_4p7fb_Feb03_2012)/i_StandardSelections_4p7fb_Feb03_2012		
			if (abs(i_MuScaleUp-i_StandardSelections_4p7fb_Feb03_2012)> abs(i_MuScaleDown-i_StandardSelections_4p7fb_Feb03_2012)):
				mes = 1.0+abs(i_MuScaleUp - i_StandardSelections_4p7fb_Feb03_2012)/i_StandardSelections_4p7fb_Feb03_2012		
			jres = 1.0+abs(i_JetSmear - i_StandardSelections_4p7fb_Feb03_2012)/i_StandardSelections_4p7fb_Feb03_2012		
			mres = 1.0+abs(i_MuSmear - i_StandardSelections_4p7fb_Feb03_2012)/i_StandardSelections_4p7fb_Feb03_2012
			if 'BetaHalf' not in S and 'ZJet' in B:
				if jes> mumuprejetscalez:
					j = 1.0 - jes
					J = 1.0 - mumuprejetscalez
					jes = 1+ sqrt( j*j - J*J )
				else:
					jes = 1.0		
					
				if mes> mumupremuscalez:
					m = 1.0 - mes
					M = 1.0 - mumupremuscalez
					mes = 1 + sqrt(m*m-M*M)
				else:
					mes = 1.0
			if 'BetaHalf' in S and 'WJet' in B:
				if jes> munuprejetscalew:
					j = 1.0 - jes
					J = 1.0 - munuprejetscalew
					jes = 1+ sqrt( j*j - J*J )
				else:
					jes = 1.0		
					
				if mes> munupremuscalew:
					m = 1.0 - mes
					M = 1.0 - munupremuscalew
					mes = 1 + sqrt(m*m-M*M)
				else:
					mes = 1.0	
			if 'BetaHalf' in S and 'TTBar' in B:
				if jes> munuprejetscalett:
					j = 1.0 - jes
					J = 1.0 - munuprejetscalett
					jes = 1+ sqrt( j*j - J*J )
				else:
					jes = 1.0		
					
				if mes> munupremuscalett:
					m = 1.0 - mes
					M = 1.0 - munupremuscalett
					mes = 1 + sqrt(m*m-M*M)
				else:
					mes = 1.0									
		if 'BetaHalf' not in S and 'DiBoson' in B:
			continue
		print S+','+str(int(N))+';'+str(w)+',R_'+str(rateerr)+'_'+str(rate)+','+str(jes)+','+str(mes)+','+str(jres)+','+str(mres)+','+str(mod)+','+str(mrii)+','+str(lum)
	print '\n'

print '\n\n'
for S in Lqsignals:
	print 'S:'+S+',R:Rate,E:Stat,E:Jes,E:Mes,E:Jres,E:Mres,E:Mod,E:Mrii,E:Lum'
	N = 0 
	w = 0
	for t in scaletags:
		exec('i_'+t+' = 0')
		
	for i in R:
		if sel[i] != S or sig[i] !=S:
			continue
		for t in scaletags:
			if t == typ[i]:
				exec ('i_'+t+'= '+str(tot[i]))		
				exec ('ie_'+t+'= '+str(rate_err[i]))	
	
		#print sel[i]+'  '+sig[i]+'  '+typ[i] + '  '+str(tot[i] )
		if typ[i] == 'StandardSelections_4p7fb_Feb03_2012':
			N = mc[i]
			w = weight[i]
	jes = 1.0
	mes = 1.0
	jres = 1.0
	mres = 1.0
	mod = 1.0
	mrii = 1.0
	lum = 1.0
	rate = -1.0
	rateerr = -1.0
	
	if i_StandardSelections_4p7fb_Feb03_2012 != 0:
		rate = i_StandardSelections_4p7fb_Feb03_2012
		rateerr = 1.0+(ie_StandardSelections_4p7fb_Feb03_2012/i_StandardSelections_4p7fb_Feb03_2012)			

		jes = 1.0+abs(i_JetScaleDown - i_StandardSelections_4p7fb_Feb03_2012)/i_StandardSelections_4p7fb_Feb03_2012		
		if (i_JetScaleUp>i_JetScaleDown):
			jes = 1.0+ abs(i_JetScaleUp - i_StandardSelections_4p7fb_Feb03_2012)/i_StandardSelections_4p7fb_Feb03_2012
		mes = abs(i_MuScaleDown - i_StandardSelections_4p7fb_Feb03_2012)/i_StandardSelections_4p7fb_Feb03_2012		
		if (i_MuScaleUp>i_MuScaleDown):
			mes = 1.0+abs(i_MuScaleUp - i_StandardSelections_4p7fb_Feb03_2012)/i_StandardSelections_4p7fb_Feb03_2012		
		jres = 1.0+abs(i_JetSmear - i_StandardSelections_4p7fb_Feb03_2012)/i_StandardSelections_4p7fb_Feb03_2012		
		mres = 1.0+abs(i_MuSmear - i_StandardSelections_4p7fb_Feb03_2012)/i_StandardSelections_4p7fb_Feb03_2012		
	print S+','+str(int(N))+';'+str(w)+',R_'+str(rateerr)+'_'+str(rate)+','+str(jes)+','+str(mes)+','+str(jres)+','+str(mres)+','+str(mod)+','+str(mrii)+','+str(lum)
	print '\n'
print '\n'
