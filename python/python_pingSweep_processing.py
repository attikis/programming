#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is and example that uses the processing module to make a subnet discovery script. It is almost identical to the threading script 
python_pingSweep_threading.py, but relies on processing instead of threading.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
from processing import Process, Queue, Pool
import time
import subprocess 
from IPy import IP  #sudo easy_install IPy
import sys

# Declarations here
queue = Queue()
# Create an instance of an IP object.  If no size specification is given a size of 1 address (/32 for IPv4 and /128 for IPv6) is assumed.
#ipAddresses = IP("10.0.1.0/24") #generates 10.0.1.0 -> 10.0.1.255
ipAddresses = ["172.20.43.175", "194.42.7.189", "194.42.7.57", "127.0.0.1"]
nProcesses = 2

def f(iProcess, queue):
    # Create an infinite loop!
    while True:
        # Place a conditional statement for exiting the loop
        if queue.empty():
            mf.Cout("Queue for Process #%s is empty. Exiting python shell." % (iProcess))
            #print __doc__
            sys.exit(1)

        mf.Cout("Process #%s started." % (iProcess))
        # Get an item from the queue in order to ping it (i.e. get an ip address) 
        ip = queue.get()
        cmd = "ping -c 2 %s" % (ip)
        retVal = subprocess.call(cmd, shell = True, stdout=open("/dev/null", "w"), stderr = subprocess.STDOUT)
        # Check return value; if else than zero inform user
        if retVal == 0:
            mf.Cout("Process #%s is alive." % (iProcess))
        else:
            mf.Cout("Process #%s is not responding for IP Address %s." % (iProcess, ip))
            
if __name__ == "__main__":
    mf.StopWatchStart()
    
    # Loop over all IP addresses
    for ip in ipAddresses:
        # Put an item into the queue
        queue.put(ip)

    # Loop over a given number of processes; 
    for iProcess in range(nProcesses):
        # Create process
        p = Process(target = f, args=[iProcess, queue])
        # Start process
        p.start()

    mf.Cout("Main process joins on queue.")
    # Join procees to on queue so that all processes are gotten and processed before exiting the program.
    p.join()
    mf.Cout("Main program finished.")
    
    #timer.sleep(5)
    mf.StopWatchStop()
