#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a script that demonstrates a few of the functionalities of the subprocess module.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import subprocess
import os
import socket

if __name__ == "__main__":
    mf.StopWatchStart()
    
    # Create report on filesystem disk space usage
    cmd = "df"
    options = " -k"
    subprocess.call(cmd+options, shell=True)
    a = subprocess.Popen(cmd+options, shell=True)
    print

    # Create report with estimate on file space usage
    cmd = "du"
    options = " -hs"
    path = " " + os.getcwd()
    subprocess.call(cmd+options+path, shell=True)
    print
    
    # Create report with estimate on file space usage
    myHostName = socket.gethostname()
    myIpAddress = socket.gethostbyname(myHostName)
    cmd = "ping"
    options = " -c 5" #ping 5 packets
    ip = " " + myIpAddress
    mf.Cout("None-verbose call of ping-1")
    subprocess.call(cmd+options+ip, shell=True, stdout = open("/dev/null", "w"), stderr = subprocess.STDOUT) #no stdout or stderr
    mf.Cout("None-verbose call of ping-2")
    subprocess.Popen(cmd+options+ip, shell=True, stdout = open("/dev/null", "w"), stderr = subprocess.STDOUT) #no stdout or stderr
    mf.Cout("Verbose call of ping")
    subprocess.call(cmd+options+ip, shell=True) #with stdout and stderr
    print

    mf.StopWatchStop()
