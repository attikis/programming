#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a bit more involved example of threading. It is actually a threaded ping sweep which can be used to ping a network for responses. 
A solution without threads is of course possible (using subprocess.Popen or mf.CmdPipe(*cmds) but are highly inefficient, because the script will have to wait for every ping. 
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import threading
import subprocess
from Queue import Queue
import time

nThreads =  10
queue = Queue()
ip_Addresses = []
retVals = {}

# Create a list of ip addresses
for i in range(0, nThreads):
    ip = "192.168.1.10" + str(i)
    # print ip
    ip_Addresses.append(ip)

def pinger(iThread, queue):
    '''
    This module pings a subnet.
    '''
    # Define an infinite loop!
    while True:
        # Remove and return an item from the queue.
        ip = queue.get()
        # Inform user of thread number and ip to be pinged
        mf.Cout("Thread %s: Pinging %s" % (iThread, ip))
        # Define ping command with 2 packets to be sent (-c 2)
        cmd = "ping -c 2 %s" % (ip)
        retVal = subprocess.call(cmd, shell = True, stdout = open("/dev/null", "w"), stderr = subprocess.STDOUT) #retVal = subprocess.call(cmd, shell = True)
        # Save ip pinged and response (retVal) into a dictionary
        retVals[ip] = retVal
        # Indicate that this queue task is complete
        queue.task_done()
        return retVal

if __name__ == "__main__":
    mf.StopWatchStart()
    
    # Create threads but do not launch yet
    for iThread in range(1, nThreads+1):
        # Create the thread
        worker = threading.Thread(target = pinger, args=(iThread, queue))
        # Set the thread as a Daemon process. If this is not set before the thread start() the script will run indefinitely.
        worker.setDaemon(True)
        # Start the thread's activity 
        worker.start()
        

    # Add all ip addresses to queue to launch threads
    mf.CountDown("Launching threads in", 3)
    for ip in ip_Addresses:
        # Put an item into the queue
        queue.put(ip)
    
    print
    mf.Cout("Main Thread Waiting:")

    # Block thread until all items in the Queue have been gotten and processed.
    queue.join()

    # Inform users about the results
    for key in retVals:
        if retVals[key] == 0:
            retVal = "alive"
        else:
            retVal = "not responding"
        mf.Cout("IP %s retVal was %s (%s)" % (key, retVals[key], retVal))
        
    mf.StopWatchStop()
