#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a script that demonstrates how to examine the contents of a tarball with python.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import os

# Declarations
cwd = os.getcwd()

if __name__ == "__main__":
    mf.StopWatchStart()    
    #mf.ExamineTarball(cwd, "python.tar")
    mf.ExamineTarball(cwd, "dumbie.tar")
    mf.StopWatchStop()
