#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a script that determines the operationg system it is called on.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()
import python_fingerPrintOS_Class as whichOS

if __name__ == "__main__":
    mf.StopWatchStart()    
    typeOS = whichOS.OpSysType()
    print typeOS.queryOS()
    mf.StopWatchStop()
