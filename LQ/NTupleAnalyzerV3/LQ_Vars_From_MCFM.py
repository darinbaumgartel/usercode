import os
import sys
from ROOT import *
from array import array
from optparse import OptionParser
import math

# Input Options - file, cross-section, number of vevents
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="input root file", metavar="FILE")
parser.add_option("-s", "--sigma", dest="crosssection", help="specify the process cross-section", metavar="SIGMA")
(options, args) = parser.parse_args()



# Here we get the file name, and adjust it accordingly for EOS, castor, or local directory
name = options.filename
if '/store' in name:
	name = 'root://eoscms//eos/cms'+name
if '/castor/cern.ch' in name:
	name = 'rfio://'+name

fin = TFile.Open(name,'READ')

_fout = name.replace('.root','_LQVariables.root')
t = fin.Get("h300")

fout = TFile.Open(_fout,'RECREATE')
tout=TTree("PhysicalVariables","PhysicalVariables")


_kinematicvariables = ['Pt_muon1','Pt_muon2','Pt_jet1','Pt_jet2','Pt_miss']
_kinematicvariables += ['Eta_muon1','Eta_muon2','Eta_jet1','Eta_jet2','Eta_miss']
_kinematicvariables += ['Phi_muon1','Phi_muon2','Phi_jet1','Phi_jet2','Phi_miss']
_kinematicvariables += ['St_uujj','St_uvjj']
_kinematicvariables += ['M_uu','MT_uv']
_kinematicvariables += ['DR_muon1muon2','DPhi_muon1met','DPhi_jet1met','DPhi_jet2met']
_kinematicvariables += ['DR_muon1jet1','DR_muon1jet2','DR_muon2jet1','DR_muon2jet2']
_kinematicvariables += ['DPhi_muon1jet1','DPhi_muon1jet2','DPhi_muon2jet1','DPhi_muon2jet2']
_kinematicvariables += ['M_uujj1','M_uujj2','M_uujjavg','MT_uvjj1','MT_uvjj2','M_uvjj','MT_uvjj']
_kinematicvariables == ['weight']
_variations = ['']

for b in _kinematicvariables:
	for v in _variations:
		exec(b+v+' = array("f",[0])')
		exec('tout.Branch("'+b+v+'",'+b+v+',"'+b+v+'/F")' )


ntotal = (1.0*t.GetEntries())
print ntotal


startingweight = float(options.crosssection)/float(ntotal)




def LortenzPE(px,py,pz,e):
	v = TLorentzVector()
	v.SetPxPyPzE(px,py,pz,e)
	return v

def TransMass(p1,p2):
	# Pupose: Simple calculation of transverse mass between two TLorentzVectors
	return math.sqrt( 2*p1.Pt()*p2.Pt()*(1-math.cos(p1.DeltaPhi(p2))) )

def InvMass(particles):
	# Pupose: Simple calculation of invariant mass between two TLorentzVectors	
	output=particles
	return (p1+p2).M()

def ST(particles):
	# Pupose: Calculation of the scalar sum of PT of a set of TLorentzVectors	
	st = 0.0
	for p in particles:
		st += p.Pt()
	return st


def TransMass(p1,p2):
	# Pupose: Simple calculation of transverse mass between two TLorentzVectors
	return math.sqrt( 2*p1.Pt()*p2.Pt()*(1-math.cos(p1.DeltaPhi(p2))) )

def InvMass(particles):
	# Pupose: Simple calculation of invariant mass between two TLorentzVectors	
	output=particles
	return (p1+p2).M()

def ST(particles):
	# Pupose: Calculation of the scalar sum of PT of a set of TLorentzVectors	
	st = 0.0
	for p in particles:
		st += p.Pt()
	return st

def GeomFilterCollection(collection_to_clean,good_collection,dRcut):
	# Pupose: Take a collection of TLorentzVectors that you want to clean (arg 1)
	#         by removing all objects within dR of dRcut (arg 3) of any element in
	#         the collection of other particles (arg 2)
	#         e.g.  argumments (jets,muons,0.3) gets rid of jets within 0.3 of muons. 
	output_collection = []
	for c in collection_to_clean:
		isgood = True
		for g in good_collection:
			if (c.DeltaR(g))<dRcut:
				isgood = False
		if isgood==True:
			output_collection.append(c)
	return output_collection

def GetLLJJMasses(l1,l2,j1,j2):
	# Pupose: For LLJJ channels, this function returns two L-J Masses, corresponding to the
	#         pair of L-Js which minimizes the difference between LQ masses in the event
	m11 = (l1+j1).M()
	m12 = (l1+j2).M()
	m21 = (l2+j1).M()
	m22 = (l2+j2).M()
	mh = 0.0
	diff1 = abs(m21-m12)
	diff2 = abs(m11-m22)
	if diff1 < diff2:
		pair =  [m21,m12]
		mh = m21
	else:
		pair = [m11,m22]
		mh = m11
	pair.sort()
	pair.reverse()
	pair.append(mh)
	return pair

def GetLVJJMasses(l1,met,j1,j2):
	# Pupose: For LVJJ channels, this function returns two L-J Masses, and an LJ mass and mT, 
	#         Quantities corresponding to the pair of L-Js which minimizes the difference 
	#         between LQ masses in the event
	m11 = (l1+j1).M()
	m12 = (l1+j2).M()
	mt11 = TransMass(l1,j1)
	mt12 = TransMass(l1,j2)
	mte1 = TransMass(met,j1)
	mte2 = TransMass(met,j2)
	mh = 0.0	
	diff1 = abs(mte1-mt12)
	diff2 = abs(mt11-mte2)
	if diff1 < diff2:
		pair =  [mte1,mt12]
		pairwithinv = [m12,mte1]
	else:
		pair = [mt11,mte2]
		invmass = m11
		mh = m11
		pairwithinv = [m11,mte2]
	pair.sort()
	pair.reverse()
	
	return [pair,pairwithinv,mh]


def FullKinematicCalculation(T,variation):
	# Pupose: This is the magic function which calculates all kinmatic quantities using
	#         the previous functions. It returns them as a simple list of doubles. 
	#         It will be used in the loop over events. The 'variation' argument is passed
	#         along when getting the sets of leptons and jets, so the kinematics will vary.
	#         This function is repeated for all the sytematic variations inside the event
	#         loop. The return arguments ABSOLUELY MUST be in the same order they are 
	#         listed in the branch declarations. Modify with caution.  

	# MET as a vector
	if name[0]=='w':
		met = LortenzPE(T.px3,T.py3,T.pz3,T.E3)
		muons = [LortenzPE(T.px4,T.py4,T.pz4,T.E4)]

	# print muons[0].Pt()
	jets = [LortenzPE(T.px5,T.py5,T.pz5,T.E5),LortenzPE(T.px6,T.py6,T.pz6,T.E6)]

	jets = GeomFilterCollection(jets,muons,0.3)

	# Empty lorenz vector for bookkeeping
	EmptyLorentz = TLorentzVector()
	EmptyLorentz.SetPtEtaPhiM(.01,0,0,0)

	# Muon and Jet Counts
	_mucount = len(muons)
	_jetcount = len(jets)

	# Make sure there are two of every object, even if zero
	if len(muons) < 1 : 
		muons.append(EmptyLorentz)

	if len(muons) < 2 : 
		muons.append(EmptyLorentz)

	if len(jets) < 1 : 
		jets.append(EmptyLorentz)
	if len(jets) < 2 : 
		jets.append(EmptyLorentz)

	# Get kinmetic quantities
	[_ptmu1,_etamu1,_phimu1] = [muons[0].Pt(),muons[0].Eta(),muons[0].Phi()]
	[_ptmu2,_etamu2,_phimu2] = [muons[1].Pt(),muons[1].Eta(),muons[1].Phi()]

	[_ptj1,_etaj1,_phij1]    = [jets[0].Pt(),jets[0].Eta(),jets[0].Phi()]
	[_ptj2,_etaj2,_phij2]    = [jets[1].Pt(),jets[1].Eta(),jets[1].Phi()]
	[_ptmet,_etamet,_phimet] = [met.Pt(),0,met.Phi()]

	_stuujj = ST([muons[0],muons[1],jets[0],jets[1]])
	_stuvjj = ST([muons[0],met,jets[0],jets[1]])


	_Muu = (muons[0]+muons[1]).M()
	_MTuv = TransMass(muons[0],met)
	_DRuu = (muons[0]).DeltaR(muons[1])
	_DPHIuv = abs((muons[0]).DeltaPhi(met))
	_DPHIj1v = abs((jets[0]).DeltaPhi(met))
	_DPHIj2v = abs((jets[1]).DeltaPhi(met))

	_DRu1j1 = abs(muons[0].DeltaR(jets[0]))
	_DRu1j2 = abs(muons[0].DeltaR(jets[1]))
	_DRu2j1 = abs(muons[1].DeltaR(jets[0]))
	_DRu2j2 = abs(muons[1].DeltaR(jets[1]))

	_DPhiu1j1 = abs(muons[0].DeltaPhi(jets[0]))
	_DPhiu1j2 = abs(muons[0].DeltaPhi(jets[1]))
	_DPhiu2j1 = abs(muons[1].DeltaPhi(jets[0]))
	_DPhiu2j2 = abs(muons[1].DeltaPhi(jets[1]))

	[_Muujj1, _Muujj2,_MHuujj] = GetLLJJMasses(muons[0],muons[1],jets[0],jets[1])
	[[_MTuvjj1, _MTuvjj2], [_Muvjj, _MTuvjj],_MHuvjj] = GetLVJJMasses(muons[0],met,jets[0],jets[1])

	_Muujjavg = 0.5*(_Muujj1+_Muujj2)

	_weight = startingweight*T.wt

	# This MUST have the same structure as _kinematic variables!
	toreturn = [_ptmu1,_ptmu2,_ptj1,_ptj2,_ptmet]
	toreturn += [_etamu1,_etamu2,_etaj1,_etaj2,_etamet]
	toreturn += [_phimu1,_phimu2,_phij1,_phij2,_phimet]
	toreturn += [_stuujj,_stuvjj]
	toreturn += [_Muu,_MTuv]
	toreturn += [_DRuu,_DPHIuv,_DPHIj1v,_DPHIj2v]
	toreturn += [_DRu1j1,_DRu1j2,_DRu2j1,_DRu2j2]
	toreturn += [_DPhiu1j1,_DPhiu1j2,_DPhiu2j1,_DPhiu2j2]
	toreturn += [_Muujj1, _Muujj2,_Muujjavg]
	toreturn += [_MTuvjj1, _MTuvjj2,_Muvjj, _MTuvjj]
	toreturn += [_weight]
	return toreturn	




##########################################################################################
#################    BELOW IS THE ACTUAL LOOP OVER ENTRIES         #######################
##########################################################################################
N=int(ntotal)
# Please don't edit here. It is static. The kinematic calulations are the only thing to edit!
for n in range(N):

	# This is the loop over events. Due to the heavy use of functions and automation of 
	# systematic variations, this loop is very small. It should not really be editted, 
	# except possibly to add a new flag or weight variable. 
	# All editable contents concerning kinematics are in the function defs.

	# Get the entry
	t.GetEntry(n)
	# if n > 1000:  # Testing....
	# 	break
	if n%1000==0:
		print 'Procesing event',n, 'of', N # where we are in the loop...
	# if n > 300:
	# 	break
	## ===========================  BASIC SETUP  ============================= ##
	# print '-----'
	# Assign Weights

	## ===========================  Calculate everything!  ============================= ##

	# Looping over systematic variations
	for v in _variations:
		# All calucations are done here
		calculations = FullKinematicCalculation(t,v)
		# Now cleverly cast the variables
		for b in range(len(_kinematicvariables)):
			exec(_kinematicvariables[b]+v+'[0] = calculations['+str(b)+']')


	## ===========================     Skim out events     ============================= ##

	# Feel like skimming? Do it here. The syntax is just {branchname}[0] > blah, or whatever condition
	# you want to impose. The [0] is because pyroot passes everything as an array of length 1.
	# BE MINDFUL: Just because the central (non-systematic) quantity meets the skim, does not mean 
	# that the systematic varied quantity will, and that will throw off systematics calculations later.
	# Make sure your skim is looser than any selection you will need afterward!

	if (Pt_muon1[0] < 42): continue
	if (Pt_muon2[0] < 42) and (Pt_miss[0] < 35): continue
	if (Pt_jet1[0] < 110): continue
	if (Pt_jet2[0] < 40): continue
	if (St_uujj[0] < 250) and (St_uvjj[0] < 250): continue
	# Fill output tree with event
	tout.Fill()

# All done. Write and close file.
tout.Write()
fout.Close()

