#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Compliled regular expressions in python

# First import the regular expressions module
import re

# # Create a compliled regular expression object
# dataset_re = re.compile("^/(?P<name>\S+?)/")
# pileup_re  = re.compile("\w*PU\d*")
# 
# # Create some string
# dataset = "/TT_TuneCUETP8M1_14TeV-powheg-pythia8/PhaseIISpring17D-NoPU_pilot_90X_upgrade2023_realistic_v9-v1/GEN-SIM-DIGI-RAW"
# dataset = "/TT_TuneCUETP8M1_14TeV-powheg-pythia8/PhaseIISpring17D-PU140_pilot_90X_upgrade2023_realistic_v9-v1/GEN-SIM-DIGI-RAW"
# #dataset = "/TT_TuneCUETP8M1_14TeV-powheg-pythia8/PhaseIISpring17D-PU200_pilot_90X_upgrade2023_realistic_v9-v1/GEN-SIM-DIGI-RAW"
# 
# match = dataset_re.search(dataset)
# requestName =  ""
# 
# if match:
#     requestName = match.group("name")
#     
# match = pileup_re.search(dataset)
# if match:
#     requestName += "_" + match.group()
# 
# print "requestName = ", requestName


dataset = "/TT_TuneCUETP8M1_14TeV-powheg-pythia8/PhaseIISpring17D-NoPU_pilot_90X_upgrade2023_realistic_v9-v1/GEN-SIM-DIGI-RAW"
dataset = "/TT_TuneCUETP8M1_14TeV-powheg-pythia8/PhaseIISpring17D-PU140_pilot_90X_upgrade2023_realistic_v9-v1/GEN-SIM-DIGI-RAW"
dataset = "/TT_TuneCUETP8M1_14TeV-powheg-pythia8/PhaseIISpring17D-PU200_pilot_90X_upgrade2023_realistic_v9-v1/GEN-SIM-DIGI-RAW"
mcdataset_re   = re.compile("^/(?P<name>\S+?)/")
tune_re        = re.compile("Tune\w+_")
tev_re         = re.compile("\d*TeV")
pileup_re      = re.compile("\w*PU\d*")

# Scan through the string 'dataset' & look for any location where the compiled RE 'mcdataset_re' matches
match = mcdataset_re.search(dataset)
if match:
    requestName = match.group().split("_")[0]
if 0:
    print "1"*20
    print "requestName = ", requestName

# Append the MC-tune
tune_match = tune_re.search(dataset)
if tune_match:
    requestName += "_" + tune_match.group()
if 0:
    print "2"*20
    print "requestName = ", requestName

# Append the COM Energy
tev_match = tev_re.search(dataset)
if tev_match:
    requestName += tev_match.group()
if 0:
    print "3"*20
    print "requestName = ", requestName

# Append the Pileup
pileup_match = pileup_re.search(dataset)
if pileup_match:
    requestName += "_" + pileup_match.group()
if 0:
    print "4"*20
    print "requestName = ", requestName

print "requestName = ", requestName    
