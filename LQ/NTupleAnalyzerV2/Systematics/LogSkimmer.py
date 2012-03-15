
flogV = open('SysVerboseLog.txt','r')
normtag = 'StandardSelections_4p7fb_Mar03fix_2012'
scaletags = ['JetScaleUp','JetScaleDown','MuScaleUp','MuScaleDown','JetSmear','MuSmear']
scaletags.append('PUScaleUp')
scaletags.append('PUScaleDown')

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
jetzpos_smear = []
muzpos_smear = []
pilezpos = []

unscaled = 0.0
unsmeard = 0.0


mumuprejetscalez = 1.0
mumupremuscalez = 1.0

mumuprepuscalez = 1.0

munuprejetscalew = 1.0
munuprejetscalett = 1.0
munupremuscalew = 1.0
munupremuscalett = 1.0

mumuprejetsmearz = 1.0
mumupremusmearz = 1.0

munuprejetsmearw = 1.0
munuprejetsmeartt = 1.0
munupremusmearw = 1.0
munupremusmeartt = 1.0

munuprepuscalew = 1.0
munuprepuscalett = 1.0


for i in range(len(sel)):
	if 'PreSel' not in sel[i]:
		continue
	if 'MuMu' not in sel[i]: 
		continue
	if 'ZJet' in sig[i] and 'JetScale' in typ[i]:
		jetzpos.append(tot[i])
	if 'ZJet' in sig[i] and 'PUScale' in typ[i]:
		pilezpos.append(tot[i])
	if 'ZJet' in sig[i] and 'MuScale' in typ[i]:
		muzpos.append(tot[i])	
	if 'ZJet' in sig[i] and 'JetSmear' in typ[i]:
		jetzpos_smear.append(tot[i])
	if 'ZJet' in sig[i] and 'MuSmear' in typ[i]:
		muzpos_smear.append(tot[i])	
	if 'ZJet' in sig[i] and 'StandardSelection' in typ[i]:
		unscaled = (tot[i])
		unsmeard = (tot[i])	
for x in jetzpos:
	if abs(x - unscaled) > mumuprejetscalez:
		mumuprejetscalez = (abs(x - unscaled) + unscaled)/unscaled
for x in muzpos:
	if abs(x - unscaled) > mumupremuscalez:
		mumupremuscalez = (abs(x - unscaled) + unscaled)/unscaled
for x in jetzpos_smear:
	if abs(x - unsmeard) > mumuprejetsmearz:
		mumuprejetsmearz = (abs(x - unsmeard) + unsmeard)/unsmeard
for x in muzpos_smear:
	if abs(x - unsmeard) > mumupremusmearz:
		mumupremusmearz = (abs(x - unsmeard) + unsmeard)/unsmeard
for x in pilezpos:
	if abs(x - unscaled) > mumuprepuscalez:
		mumuprepuscalez = (abs(x - unscaled) + unscaled)/unscaled

jetwpos = []
muwpos = []
jetttpos = []
muttpos = []
jetwpos_smear = []
muwpos_smear = []
jetttpos_smear = []
muttpos_smear = []

pilewpos = []
pilettpos=[]

unscaledw = 0.0
unscaledtt = 0.0

unsmeardw = 0.0
unsmeardtt = 0.0


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
		
	if 'WJet' in sig[i] and 'JetSmear' in typ[i]:
		jetwpos_smear.append(tot[i])
	if 'WJet' in sig[i] and 'MuSmear' in typ[i]:
		muwpos_smear.append(tot[i])	
	if 'TTBar' in sig[i] and 'JetSmear' in typ[i]:
		jetttpos_smear.append(tot[i])
	if 'TTBar' in sig[i] and 'MuSmear' in typ[i]:
		muttpos_smear.append(tot[i])					
		
	if 'WJet' in sig[i] and 'StandardSelection' in typ[i]:
		unscaledw = (tot[i])	
		unsmeardw = (tot[i])	

	if 'TTBar' in sig[i] and 'StandardSelection' in typ[i]:
		unscaledtt = (tot[i])	
		unsmeardtt = (tot[i])	

	if 'WJet' in sig[i] and 'PUScale' in typ[i]:
		pilewpos.append(tot[i])
	if 'TTBar' in sig[i] and 'PUScale' in typ[i]:
		pilettpos.append(tot[i])

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

for x in jetwpos_smear:
	if abs(x - unsmeardw) > munuprejetsmearw:
		munuprejetsmearw = (abs(x - unsmeardw) + unsmeardw)/unsmeardw
for x in muwpos_smear:
	if abs(x - unsmeardw) > munupremusmearw:
		munupremusmearw = (abs(x - unsmeardw) + unsmeardw)/unsmeardw
for x in jetttpos_smear:
	if abs(x - unsmeardtt) > munuprejetsmeartt:
		munuprejetsmeartt = (abs(x - unsmeardtt) + unsmeardtt)/unsmeardtt
for x in muttpos_smear:
	if abs(x - unsmeardtt) > munupremusmeartt:
		munupremusmeartt = (abs(x - unsmeardtt) + unsmeardtt)/unsmeardtt

for x in pilewpos:
	if abs(x - unscaledw) > munuprepuscalew:
		munuprepuscalew = (abs(x - unscaledw) + unscaledw)/unscaledw

for x in pilettpos:
	if abs(x - unscaledtt) > munuprepuscalett:
		munuprepuscalett = (abs(x - unscaledtt) + unscaledtt)/unscaledtt

from math import sqrt
for B in Backgrounds:
	print 'B:'+B+',R:Rate,E:Stat,E:Jes,E:Mes,E:Jres,E:Mres,E:Mod,E:Mrii,E:Lum,E:Pileup'
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
			if typ[i] == 'StandardSelections_4p7fb_Mar03fix_2012':
				N = mc[i]
				w = weight[i]
		jes = 1.0
		mes = 1.0
		jres = 1.0
		mres = 1.0
		mod = 1.0
		mrii = 1.0
		lum = 1.0
		pu = 1.0
		rate = -1.0
		rateerr = -1.0
		
		if i_StandardSelections_4p7fb_Mar03fix_2012 != 0:
			rate = i_StandardSelections_4p7fb_Mar03fix_2012
			rateerr = 1.0+(ie_StandardSelections_4p7fb_Mar03fix_2012/i_StandardSelections_4p7fb_Mar03fix_2012)			
			jes = 1.0+abs(i_JetScaleDown - i_StandardSelections_4p7fb_Mar03fix_2012)/i_StandardSelections_4p7fb_Mar03fix_2012		
			if (abs(i_JetScaleUp - i_StandardSelections_4p7fb_Mar03fix_2012)>abs(i_JetScaleDown-i_StandardSelections_4p7fb_Mar03fix_2012)):
				jes = 1.0+ abs(i_JetScaleUp - i_StandardSelections_4p7fb_Mar03fix_2012)/i_StandardSelections_4p7fb_Mar03fix_2012	

			mes = 1.0+abs(i_MuScaleDown - i_StandardSelections_4p7fb_Mar03fix_2012)/i_StandardSelections_4p7fb_Mar03fix_2012		
			if (abs(i_MuScaleUp-i_StandardSelections_4p7fb_Mar03fix_2012)> abs(i_MuScaleDown-i_StandardSelections_4p7fb_Mar03fix_2012)):
				mes = 1.0+abs(i_MuScaleUp - i_StandardSelections_4p7fb_Mar03fix_2012)/i_StandardSelections_4p7fb_Mar03fix_2012		

			pu = 1.0+abs(i_PUScaleDown - i_StandardSelections_4p7fb_Mar03fix_2012)/i_StandardSelections_4p7fb_Mar03fix_2012		
			if (abs(i_PUScaleUp - i_StandardSelections_4p7fb_Mar03fix_2012)>abs(i_PUScaleDown-i_StandardSelections_4p7fb_Mar03fix_2012)):
				pu = 1.0+ abs(i_PUScaleUp - i_StandardSelections_4p7fb_Mar03fix_2012)/i_StandardSelections_4p7fb_Mar03fix_2012	

			jres = 1.0+abs(i_JetSmear - i_StandardSelections_4p7fb_Mar03fix_2012)/i_StandardSelections_4p7fb_Mar03fix_2012		
			mres = 1.0+abs(i_MuSmear - i_StandardSelections_4p7fb_Mar03fix_2012)/i_StandardSelections_4p7fb_Mar03fix_2012
			if 'BetaHalf' not in S and 'ZJet' in B:
				j = jes
				J = mumuprejetscalez
				jes = 1.0+ abs(1.0/j-1.0/J)/(1.0/j)
					
				m = mes
				M = mumupremuscalez
				mes = 1.0+abs(1.0/m - 1.0/M)/(1.0/m)

				j = jres
				J = mumuprejetsmearz
				jres = 1.0+ abs(1.0/j-1.0/J)/(1.0/j)
					
				m = mres
				M = mumupremusmearz
				mres = 1.0+abs(1.0/m - 1.0/M)/(1.0/m)
				
				p = pu
				P = mumuprepuscalez
				pu = 1.0+abs(1.0/p - 1.0/P)/(1.0/p)
				
			if 'BetaHalf' in S and 'WJet' in B:
				j = jes
				J = munuprejetscalew
				jes = 1.0+ abs(1.0/j-1.0/J)/(1.0/j)
				#print '@@ '+str(j) + '  '+str(J) + '  '+str(res)

				m =  mes
				M =  munupremuscalew
				mes = 1.0+abs(1.0/m - 1.0/M)/(1.0/m)

				j = jres
				J = munuprejetsmearw
				jres = 1.0+ abs(1.0/j-1.0/J)/(1.0/j)
				#print '@@ '+str(j) + '  '+str(J) + '  '+str(jres)
				m =  mres
				M =  munupremusmearw
				mres = 1.0+abs(1.0/m - 1.0/M)/(1.0/m)
				#print ' @@ -------------------------'
				
				p = pu
				P = munuprepuscalew
				pu = 1.0+abs(1.0/p - 1.0/P)/(1.0/p)		
				
			if 'BetaHalf' in S and 'TTBar' in B:
				j = jes
				J = munuprejetscalett
				jes = 1.0+ abs(1.0/j-1.0/J)/(1.0/j)
				
				m = mes
				M = munupremuscalett
				mes = 1.0+abs(1.0/m - 1.0/M)/(1.0/m)

				j = jres
				J = munuprejetsmeartt
				jres = 1.0+ abs(1.0/j-1.0/J)/(1.0/j)
				
				m = mres
				M = munupremusmeartt
				mres = 1.0+abs(1.0/m - 1.0/M)/(1.0/m)

				p = pu
				P = munuprepuscalett
				pu = 1.0+abs(1.0/p - 1.0/P)/(1.0/p)
					
		#if 'BetaHalf' not in S and 'DiBoson' in B:
		#if 'BetaHalf' not in S :

			#continue
		print S+','+str(int(N))+';'+str(w)+',R_'+str(rateerr)+'_'+str(rate)+','+str(jes)+','+str(mes)+','+str(jres)+','+str(mres)+','+str(mod)+','+str(mrii)+','+str(lum)+','+str(pu)
	print '\n'

print '\n\n'
for S in Lqsignals:
	print 'S:'+S+',R:Rate,E:Stat,E:Jes,E:Mes,E:Jres,E:Mres,E:Mod,E:Mrii,E:Lum,E:Pileup'
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
		if typ[i] == normtag:
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
	
	if i_StandardSelections_4p7fb_Mar03fix_2012 != 0:
		rate = i_StandardSelections_4p7fb_Mar03fix_2012
		rateerr = 1.0+(ie_StandardSelections_4p7fb_Mar03fix_2012/i_StandardSelections_4p7fb_Mar03fix_2012)			
		jes = 1.0+abs(i_JetScaleDown - i_StandardSelections_4p7fb_Mar03fix_2012)/i_StandardSelections_4p7fb_Mar03fix_2012		
		if (i_JetScaleUp>i_JetScaleDown):
			jes = 1.0+ abs(i_JetScaleUp - i_StandardSelections_4p7fb_Mar03fix_2012)/i_StandardSelections_4p7fb_Mar03fix_2012
		mes = 1.0+abs(i_MuScaleDown - i_StandardSelections_4p7fb_Mar03fix_2012)/i_StandardSelections_4p7fb_Mar03fix_2012		
		if (i_MuScaleUp>i_MuScaleDown):
			mes = 1.0+abs(i_MuScaleUp - i_StandardSelections_4p7fb_Mar03fix_2012)/i_StandardSelections_4p7fb_Mar03fix_2012
			
		pu = 1.0+abs(i_PUScaleDown - i_StandardSelections_4p7fb_Mar03fix_2012)/i_StandardSelections_4p7fb_Mar03fix_2012		
		if (abs(i_PUScaleUp - i_StandardSelections_4p7fb_Mar03fix_2012)>abs(i_PUScaleDown-i_StandardSelections_4p7fb_Mar03fix_2012)):
			pu = 1.0+ abs(i_PUScaleUp - i_StandardSelections_4p7fb_Mar03fix_2012)/i_StandardSelections_4p7fb_Mar03fix_2012	

		jres = 1.0+abs(i_JetSmear - i_StandardSelections_4p7fb_Mar03fix_2012)/i_StandardSelections_4p7fb_Mar03fix_2012		
		mres = 1.0+abs(i_MuSmear - i_StandardSelections_4p7fb_Mar03fix_2012)/i_StandardSelections_4p7fb_Mar03fix_2012		
	print S+','+str(int(N))+';'+str(w)+',R_'+str(rateerr)+'_'+str(rate)+','+str(jes)+','+str(mes)+','+str(jres)+','+str(mres)+','+str(mod)+','+str(mrii)+','+str(lum)+','+str(pu)
	print '\n'
print '\n'
