#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is another simple example of threading. It 
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import subprocess 
import time

# Declarations here
ipList = [
    "google.com",
    "yahoo.com",
    "store.apple.com",
    "amazon.com",
    ]
cmd = "ping -c 5 %s"

def DoPing(ipAddress):
    print time.asctime(), "- Pinging", ipAddress
    fullCmd = cmd % (ipAddress)
    return subprocess.Popen(fullCmd, shell = True, stdout = subprocess.PIPE)


if __name__ == "__main__":
    info = []
    # Loop over all ip-address and ping them
    for ip in ipList:
        p = DoPing(ip)
        info.append((p, ip))
    print

    # Loop over all threads and print return status
    for p, ip in info:
        print time.asctime(), "- Waiting for", ip
        p.wait()
        print time.asctime(), "- Return from", ip, "=", p.returncode
