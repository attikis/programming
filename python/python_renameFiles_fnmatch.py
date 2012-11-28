#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a script that uses fnmatch to fina certain files and rename them
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import os
import shutil

if __name__ == "__main__":
    mf.StopWatchStart()
    
    # First Create some dumbie files to work on
    path = os.getcwd()+ "/fnmatchAndGlob/"
    fileExtOld = ".txt"
    fileExtNew = ".txt2"

    # Rename files
    mf.RenameFiles(path, fileExtOld, fileExtNew)
    
    # Rename back to original name
    mf.RenameFiles(path, fileExtNew, fileExtOld)
    
    mf.StopWatchStop()

    
