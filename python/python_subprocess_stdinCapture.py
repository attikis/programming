#!/usr/bin/env python
from __future__ import with_statement

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a simple example of how to communicate so standard in with the subprocess module.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import subprocess
import sys

if __name__ == "__main__":
    mf.StopWatchStart()

    # Simple stdin
    p1 = subprocess.Popen("wc -c", shell = True, stdin = subprocess.PIPE)
    # Use p.communicate or p.stdin.write to write to the process. Use p.stdout.read to read from it.
    name = "alexandros"
    mf.Cout('p1.communicate("%s"):' % (name))
    p1.communicate(name)   # bash equivalent: |myMac> echo alexandros | wc -c
    # p.stdin.write("alexandros") # bash equivalent: |myMac> echo alexandros | wc -c

    # Lets emulate bash this time and redirect a file to stdin. Open file in write mode, write and close
    with open("stdin.txt", "w") as wFile:
        wFile.write("attikis")
        
    # Open file in read-only mode and close        
    with open("stdin.txt") as rFile:
        text = rFile.read()
        rFile.close()

    # Redirect the file output to our process
    p2 = subprocess.Popen("wc -c", shell = True, stdin = subprocess.PIPE)
    # Use p.communicate or p.stdin.write to write to the process. Use p.stdout.read to read from it.
    mf.Cout('p2.communicate("%s"):' % (text))
    #p2.stdin.write(text)
    p2.communicate(text)

    mf.StopWatchStop()
    
