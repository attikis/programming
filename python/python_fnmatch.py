#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a script that uses fnmatch and glob to search for file matches.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
from fnmatch import fnmatch
from glob import glob
import os

if __name__ == "__main__":
    mf.StopWatchStart()
    
    # First Create some dumbie files to work on
    path = os.getcwd()
    fileExt = "*tmp*.txt"

    # Get the list of files matching this
    findList = mf.FindFiles(path, fileExt)

    mf.Cout("Found matching files:")

    # Print all matches
    for file in findList:
        print "\t%s" % (file)

    mf.StopWatchStop()

    
