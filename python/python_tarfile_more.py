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
import tarfile

# Declarations
dir = os.getcwd() + "/tar_test/"
fileName = "dumbie"
fileExt = ".txt"
nLines = 100
nFiles = 20+1
tarFileName = "dumbies.tar"
fileList = []

if __name__ == "__main__":
    mf.StopWatchStart()
    
    # First creaty a tmp directory
    mf.EnsureIsDir(dir)

    # Then create a large number of dumbie txt files
    for index in range (1, nFiles):
        file = fileName + str(index) + fileExt
        mf.CreateFile(dir, file, nLines)
        fileList.append(file)

    # Now that we have some dumbie files compress them with tar
    tar = tarfile.open(dir+tarFileName, "w")

    try:
        for file in fileList:
            mf.Cout( "Adding file %s to tarball %s." % (dir+file, tarFileName) )
            tar.add(dir+file)
    finally:
        tar.close()

    mf.StopWatchStop()
