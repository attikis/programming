#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : split() command used to split up a string

# Import regular expressions
import re
import subprocess
mLineString = "admin_blah blah blah 2038566_EI-2 Group A.txt"
myList = ["A5", "C5", "D2", "EI-2"]
reObject = re.compile(mLineString)

ls = subprocess.call(["ls","-l"])

# Loop over all items in the key-word list
for item in myList:
    if item in mLineString:
        print item
        #if item 
