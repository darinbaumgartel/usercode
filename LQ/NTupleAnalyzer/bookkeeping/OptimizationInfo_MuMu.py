# Variables for cutting, starting points, interval, number of points to test
CutVariables=['ST_calo'] # Which variables do you want to cut on

VariableStartingPoint = [150] # Where to start cutting on the variable 
VariableInterval = [10] # Intervals in which you will test cuts
VariablePointsToTest = [70] # Number of cutting points to test at the given interval

# Other variable to precut on as they appear in the root file (these are not variable cuts, they are single static cuts):
PrecutVariables=['Pt_muon1','Pt_muon2','Pt_jet1','Pt_jet2','precut_HLT']
PrecutMinValues = [25,25,25,25,.5]
