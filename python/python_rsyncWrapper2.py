#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a script that syncronizes two directories and prints out a failure message if the command does not work.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import subprocess
import sys
import os

# Declarations here
source = os.getcwd() + "/test/"
target = os.getcwd() + "/test_rsync/"

# Check that targer dir exists. If not create it
if __name__ == "__main__":
    mf.StopWatchStart()
    mf.Rsync2(source, target)
    mf.StopWatchStop()
