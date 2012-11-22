#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This script describes some basic commands that can be performed with the os module, in manipulating data (files, directories, paths, etc..).
'''

# All required modules here
import python_myFunctions as myFunctions
import os

# Object and variable declarations here
mf = myFunctions.CreateObject()

if __name__ == "__main__":
    mf.StopWatchStart()
    cwd = os.getcwd()
    dirName = cwd
    
    mf.Cout( "Printing current working directory (cwd):\n\t%s" % (os.getcwd()) )
    pyFiles = os.listdir(cwd)
    mf.Cout( "Listing files in cwd:\n\t%s" % (os.listdir(cwd)) )
    print pyFiles
    #os.rename(newDirName, newDirNameReplaced)
    mf.StopWatchStop()
