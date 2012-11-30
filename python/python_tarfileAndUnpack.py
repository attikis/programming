#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a script that demonstrates how to use tar  with python.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import os

# Declarations
cwd = os.getcwd()
compressionType = "w|bz2"

if __name__ == "__main__":
    mf.StopWatchStart()
    #mf.CreateTarball(cwd, "python") #default is tar
    mf.CreateTarball(cwd, "python", "tar")
    #mf.CreateTarball(cwd, "python", "bzip2")
    #mf.CreateTarball(cwd, "python", "gzip")

    mf.UnpackTarball(cwd + "/python.tar", "/Users/administrator/Desktop/")
    #mf.UnpackTarball(cwd + "/python.tar.bzip2", "/Users/administrator/Desktop/")
    #mf.UnpackTarball(cwd + "/python.tar.gzip", "/Users/administrator/Desktop/")
    mf.StopWatchStop()
