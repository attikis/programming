#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
A simple script that uses a progress bar, to display how much of a program has been executed. A helper function from python_myFunctions.py is called to create, start, update, 
and stop the progress bar.

Example:

'''

# All required modules here
import python_myFunctions as myFunctions

# Object and variable declarations here
mf = myFunctions.CreateObject()
mf.StopWatchStart()

# Do a simple loop
maxValue = 1000000
pBar, CallBack = mf.StartProgressBar(maxValue)
for i in range (1, maxValue):
    CallBack(i, maxValue)
mf.StopProgressBar(pBar)

mf.StopWatchStop()
