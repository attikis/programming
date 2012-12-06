#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This script performs a ping sweep without threading, but instead solely relying on subprocess. It should be used in parallel with the script python_pingSweep_threading.py to compare times.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import subprocess
import time

nPings = 10
ip_Addresses = []
retVals = {}

# Create a list of ip addresses
for i in range(0, nPings):
    ip = "192.168.1.10" + str(i)
    # print ip
    ip_Addresses.append(ip)

def pinger(iPing):
    '''
    This module pings a subnet.
    '''
    mf.Cout("Pinging %s" % (ip))
    cmd = "ping -c 2 %s" % (ip)
    retVal = subprocess.call(cmd, shell = True, stdout = open("/dev/null", "w"), stderr = subprocess.STDOUT)
    retVals[ip] = retVal
    return retVal

if __name__ == "__main__":
    mf.StopWatchStart()
    
    # Add all ip addresses to queue to launch threads
    mf.CountDown("Start pinging  in", 3)

    # Create threads but do not launch yet
    for iPing in range(1, nPings+1):
        pinger(iPing)
    
    # Inform users about the results
    for key in retVals:
        if retVals[key] == 0:
            retVal = "alive"
        else:
            retVal = "not responding"
        mf.Cout("IP %s retVal was %s (%s)" % (key, retVals[key], retVal))
        
    mf.StopWatchStop()
