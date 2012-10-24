#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Saves the current date to 10 txt files number from 0 to 10

import subprocess
import datetime

now = datetime.datetime.now()
print "\n+++ Current date and time: %s" % (now)

# Loop here from 0 to 9
for i in range(10):
    fileName = str(i) + ".txt"
    file = open(fileName, 'w')
    file.write(str(now)+"\n")
    print "+++ Saved date to file with name \"%s\"" % (fileName)

print "\n+++ Listing files in current directory"
subprocess.call(["ls","-l"])
