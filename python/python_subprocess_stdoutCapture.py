#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a 
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import subprocess

if __name__ == "__main__":
    mf.StopWatchStart()

    cmd = "df -h"
    # Capture the std output
    p = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE)
    out = p.stdout.readlines() # readlines() returns a list of newline characters.

    # Print the captures std output
    for line in out:
        print line.strip() #strip() needed to remove newlines from string.

    mf.StopWatchStop()
