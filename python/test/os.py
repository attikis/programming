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
    newDirName = cwd+"/tmp"
    newDirNameReplaced = cwd+"/tmp2"

    mf.Cout( "Printing current working directory (cwd):\n\t%s" % (os.getcwd()) )
    if not os.path.exists(newDirName):
        mf.Cout( "Making new directory:\n\t%s" % (newDirName) ) 
        os.mkdir(newDirName)
    else:
        mf.Cout( "Directory %s already exists!" % (newDirName) )
    mf.Cout( "Listing cwd:\n\t%s" % (os.listdir(cwd)) )
    mf.Cout( "Perform a stat system call on directory %s:\n\t%s" % (newDirName, os.stat(cwd)) )
    mf.Cout( "Rename directory:\n\t%s\nto :\n\t%s" % (newDirName, newDirNameReplaced ) )
    os.rename(newDirName, newDirNameReplaced)
    mf.Cout( "Listing cwd:\n\t%s" % (os.listdir(cwd)) )    
    mf.Cout( "Removing directory:\n\t%s" % (newDirNameReplaced) )
    os.rmdir(newDirNameReplaced)
    mf.StopWatchStop()
