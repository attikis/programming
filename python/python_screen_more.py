#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a 
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

if __name__ == "__main__":
    mf.StopWatchStart()

    bDetach = False
    cmd = "ping -c 4 10.00.0.1"
    mf.RunScreenCmd(cmd, "p1", bDetach)

    mf.StopWatchStop()
