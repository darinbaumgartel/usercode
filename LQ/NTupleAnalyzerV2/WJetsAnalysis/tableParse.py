import os
import sys
d = sys.argv[1]
cont = [d+'/' + x.replace('\n','') for x in os.listdir(d)]

tables = []

for c in cont:
	if "FINAL" in c and 'Tex' in c:
		tables.append(c)

for t in tables:
	print t

pairs = []
for t in tables:
	if "TexCount" not in t:
		continue
	p = []
	p.append(t)
	for tt in tables:
		if tt == t.replace('TexCount','TexXSec'):
			p.append(tt)
	if len(p)==2:
		pairs.append(p)


def TexTableFromPair(pair):
	print "-"*44
	
	for p in pair:
		if 'TexCount' in p:
			outfile = open(pair[0].replace('TexCount.txt','All.tex'),'w')

	alllines=[]
	for p in pair:	
		for line in open(p):
			line=line.replace('--','-')
			line=line.replace('&','')
			line=line.replace('\\','')
			line=line.replace('pm','\\pm')
			newline = ''
			dcount = 0
			for c in line:
				newline +=(c)
				if c == "$":
					dcount +=1
				if dcount ==2:
					dcount=0
					newline += '&' 
			newline = newline.split("&")
			alllines.append(newline)

	newtable = []
	for a in range(len(alllines)/2):
		c = alllines[a]
		x = alllines[a+len(alllines)/2]
		div = ' & '
		bin = c[0]
		print bin
		bin = bin.replace('-','')
		bin = bin.replace('$','')
		bin = bin.split()
		outbin = '$'
		outbin += str(round(float(bin[0]),2))
		outbin += '-'
		outbin += str(round(float(bin[1]),2))
		outbin += "$"
		newtable.append(outbin+div+c[1]+div+c[2]+div+x[1]+div+x[2]+' \\\\')
	# for n in newtable:
	# 	print n


	vmap = []
	vmap.append(["DeltaPhi_pfjet1muon1","$\\Delta \\phi (jet_1, \mu)$"])
	vmap.append(["DeltaPhi_pfjet2muon1","$\\Delta \\phi (jet_2, \mu)$"])
	vmap.append(["DeltaPhi_pfjet3muon1","$\\Delta \\phi (jet_3, \mu)$"])
	vmap.append(["DeltaPhi_pfjet4muon1","$\\Delta \\phi (jet_4, \mu)$"])
	vmap.append(["Eta_pfjet1","$\\eta(jet_1)$"])
	vmap.append(["Eta_pfjet2","$\\eta(jet_2)$"])
	vmap.append(["Eta_pfjet3","$\\eta(jet_3)$"])
	vmap.append(["Eta_pfjet4","$\\eta(jet_4)$"])
	vmap.append(["MT_muon1MET","$M_T(\\mu,E_T^{miss})$"])
	vmap.append(["PFJet40Count","Jet Mult."])
	vmap.append(["Pt_MET","$E_T^{miss}$"])
	vmap.append(["Pt_pfjet1","$p_T(jet_1)$"])
	vmap.append(["Pt_pfjet2","$p_T(jet_2)$"])
	vmap.append(["Pt_pfjet3","$p_T(jet_3)$"])
	vmap.append(["Pt_pfjet4","$p_T(jet_4)$"])

	var = 'BIN'
	for v in vmap:
		if v[0] in str(pair):
			var = v[1]

	outfile.write("\\begin{center}\n\\begin{tabular}{|l|ll|ll|}\\hline\n "+var+"     & Predicted Events  & Measured Events & Predicted $\\sigma$ & Measured $\\sigma$ \\\\ \\hline \\hline\n")
	for n in newtable:
		outfile.write(n+'\n')
	outfile.write('\\hline\n\\end{tabular}\n\\end{center}\n\n')

	outfile.close()

for pair in pairs:
	TexTableFromPair(pair)
