#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a script that provides a system report.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

if __name__ == "__main__":
    mf.StopWatchStart()    
    sysReport = mf.SysReport()
    print
    # Can use dictionary as follows:
    print sysReport["architecture"]
    mf.StopWatchStop()
