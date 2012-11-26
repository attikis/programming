#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is an example class containing re-usable directory walking modules.
'''

# All required modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()
import python_Walking_Class as WalkClass
import os

# Declarations 
myPath = os.getcwd()
walkObj = WalkClass.DiskWalk(myPath)

pathList = walkObj.WalkPaths()
fileList = walkObj.WalkFiles()
dirList =  walkObj.WalkDir()

# Print Statements here
#mf.Cout("Printing list of walk-paths:\n\t%s" % pathList)
#mf.Cout("Printing list of walk-files:\n\t%s" % fileList)
mf.Cout("Printing list of walk-dirs:\n\t%s" % dirList)
