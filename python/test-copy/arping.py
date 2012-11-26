#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py 192.168.1.104

Permissions: 
chmod +x fileName.py

Description:
This is a script that can be used as an arping tool. "Arping" is a computer software tool that is used to discover hosts on a computer network. The program tests whether a given IP address is in use on the local network, and can get additional information about the device using that address. It is analogous to "ping" and only works for the local network!
'''

# All required modules here
import python_myFunctions as myFunctions
import subprocess
import sys
import re

# Object and variable declarations here
mf = myFunctions.CreateObject()

def Arping(ipAddress):
    # Module docstrings
    ''' 
    Arping function used to discover hosts on a computer network. Takes IP Address or Network, returns nested map/ip list
    '''
    
    # Assuming use of arping on Red Hat Linux
    p = subprocess.Popen( "/usr/sbin/arp %s" % (ipAddress), shell=True, stdout=subprocess.PIPE )
    out = p.stdout.read()
    result = out.split()

    #pattern = re.compile(":")
    mf.Cout( "Printing result:\n\t%s" % (out) )
    for item in result:
        if ':' in item:
            mf.Cout("Printing the Ethernet MAC address mapped to the IP Address %s:\n\t%s" % (ipAddress, item))

if __name__ == "__main__":
    mf.StopWatchStart()
    
    if len(sys.argv) == 1+1:
        for ip in sys.argv[1:]:
            mf.Cout( "Arping IP Address:\n\t%s" % (ip) )
            Arping(ip)
    else:
        mf.Cout("ERROR! Wrong number of arguments (%s instead of 1) passed. Printing docstrings. Exiting python shell." % (len(sys.argv)-1))
        print __doc__
        sys.exit(1)
        
    mf.StopWatchStop()
