#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a script that demonstrates a few more of the functionalities of the subprocess module.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import subprocess
import os

def checkExitStatus(exitValue):
    if exitValue !=0:
        print "Command execution failed with exit code: %s" % exitValue
    else:
        print "Command execution success"

if __name__ == "__main__":
    mf.StopWatchStart()
    
    # Create report on filesystem disk space usage
    cmd = "la -lt blah"
    retVal = subprocess.call(cmd, shell=True)
    print checkExitStatus(retVal)

    mf.StopWatchStop()
