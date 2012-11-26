#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a script that performs a verbose directory walk in a multicrab directory.
'''

# All required modules here
import python_myFunctions as myFunctions
import os

# Object and variable declarations here
mf = myFunctions.CreateObject()
myPath = "/Users/administrator/my_work/cms/lxplus/QCD_A_v4"
myDatasets = []

if __name__ == "__main__":
    mf.StopWatchStart()

    #mf.Cout("Recursive listing of all paths in a dir:")
    #myPaths = mf.WalkPaths(myPath) #list object

    #mf.Cout( "Recursive listing of all files in %s:\n" % (myPath) )
    #myFiles = mf.WalkFiles(myPath) #list object

    mf.Cout( "Recursive listing of all dirs in %s:\n" % (myPath) )
    myDirs = mf.WalkDir(myPath) #list object

    # Loop over directory list and remove the res subdirectories
    for dir in myDirs:
        if not dir == "res":
            myDatasets.append(dir)
            
    mf.Cout( "Datasets found under %s:" % (myPath) )
    print "\t", myDatasets
    mf.StopWatchStop()
