#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a script that chains together subprocess commands to look for the succesful logins to the screensaver on a Mac laptop.
The bash-analogue is:
|>cat /etc/passwd | grep 0:0 | cut -d ':' -f 7 
returns: /bin/sh
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import subprocess

if __name__ == "__main__":
    mf.StopWatchStart()
    
    p1 = subprocess.Popen("cat /etc/passwd", shell = True, stdout = subprocess.PIPE)
    p2 = subprocess.Popen("grep 0:0", shell = True, stdin = p1.stdout, stdout = subprocess.PIPE)
    p3 = subprocess.Popen("cut -d ':' -f 7", shell = True, stdin=p2.stdout, stdout = subprocess.PIPE)
    print p3.stdout.read()

    mf.StopWatchStop()
