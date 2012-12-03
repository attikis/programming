#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is an example of a subprocess piping factory.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# main function here
if __name__ == "__main__":
    mf.StopWatchStart()
    mf.CmdPipe("df -h", "ls -lt *.py", "tail -5 python_myFunctions.py", "grep -in 'CmdPipe' *.py")
    mf.StopWatchStop()
