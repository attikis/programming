#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Compliled regular expressions in python

# First import the regular expressions module
import re

# Create a compliled regular expression object
reObject = re.compile("{{(.*?)}}")

# Create some string
myString = "At least one tau-jet with {{pT > 40 GeV/c}}, {{abs(eta) < 2.1}}  and {{LdgPt > 20 GeV/c}}."

# Loop over the results of the reObject module's findall() function, as it searches the string myString for the pattern defined in reString.
for i in reObject.findall(myString):
    print "+++ Match-> %s " % (i)

