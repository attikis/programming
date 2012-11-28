#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is an interactive script that uses fnmatch and glob to search for file matches.
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
    path = os.getcwd() + "/fnmatchAndGlob/"
    nFiles = 10+1
    for i in range (1, nFiles):
        mf.CreateFile(path, "dumbie" + str(i) + ".txt", nLines=100)
        
    # Now look for txt files in the user specified directory. Use mf.WalkPaths(path) to get the full paths
    pathList = mf.WalkPaths(path)
    fileExt = "*.txt"

    # Using fnmatch module: return boolean
    for file in pathList:
        if fnmatch(file, fileExt):
            mf.Cout("Found %s file:\n\t%s" %(fileExt, file))
            
    # Usig glob module: returns a list of files
    os.chdir(path)
    mf.Cout("Printing %s files under %s:" %(fileExt, path))
    for name in glob(fileExt):
        print "\t" + name
    mf.StopWatchStop()

    
