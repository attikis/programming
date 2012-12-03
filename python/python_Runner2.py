#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a script than uses a class closely related to subprocess module, that sequentially executes commands in a simplified and automatic way. It 
support verbose and delay options.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import python_Runner_Class as r
import os 

if __name__ == "__main__":
    mf.StopWatchStart()
    path = os.getcwd() + "/test/"
    mf.Runner("ls -lt " + path, "du -h " + path, verbose = True, delay = 5)

    mf.StopWatchStop()
