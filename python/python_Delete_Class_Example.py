#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is an example of using the Delete class, that is dedicated to deleting anything (files, directories..)
'''

# All required modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()
import python_Delete_Class as DelClass
import os

myPath = os.getcwd() + "/tmp/tmp.txt"

delObj = DelClass.Delete(myPath)
delObj.Interactive()
delObj.DryRun()
#delObj.Delete()
