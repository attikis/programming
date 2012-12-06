#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is an example of multiple queues with multiple thread pools.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
from threading import Thread
import subprocess
from Queue import Queue
import re

# Declarations here
nPingThreads = 3
nArpThreads = 3
inQueue = Queue()
outQueue = Queue()
ipAddresses = ["google.com", "cern.ch", "facebook.com"]
retVals = {}

def pinger(iThread, inQueue, outQueue):
    '''
    Pings a subnet.
    '''
    # Start an infinite loop
    while True:
        # Remove and return an item from the queue
        ip = inQueue.get()
        mf.Cout("Thread #s: Pinging %s" % (iThread, ip))
        cmd = "ping -c 1 %s" % (ip)
        retVal = subprocess.call(cmd, shell = True, stdout = open ("/dev/null", "w"), stderr = subprocess.STDOUT)
        # Store a mapping between ip and ping return value
        retVals[ip] = retVal
        if retVal == 0:
            # Put a task into the queue only if the ping was succesful
            outQueue.put(ip)
        # Indicate that this queue task is complete
        inQueue.task_done()
        
def arping(iThread, outQueue):
    ''' 
    Graps a valid IP address from a queue and gets the mac address.
    '''
    while True:
        # Get a task from the queue
        ip.outQueue.get()
        cmd = "arping -c 1 %s" % (ip)
        p = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE)
        out = p.stdout.read()

        # Match and extract the mac address from stdout
        result = out.split()
        reObj = re.compile(pattern = ":")
        macAddress = None
        for item in result:
            match = reObj.search(item)
            if match:
                macAddress = item
                
        mf.Cout("IP Address: %s | Mac Address: %s " % (ip, macAddress))
        # Indicate that this queue task is complete
        outQueue.task_done()

if __name__ == "__main__":
    mf.StopWatchStart()
    
    # Place all ip addresses into inQueue
    for ip in ipAddresses:
        inQueue.put(ip)
    
    # Spawn pool of (ping) threads
    for i in range(nPingThreads):
        
        # Create here the pool of threads
        worker = Thread(target = pinger, args = (i, inQueue, outQueue))
        # Set the thread as a Daemon process. If this is not set before the thread start() the script will run indefinitely.
        worker.setDaemon(True)
        # Start the thread's activity!
        worker.start()
        
    # Spawn pool of (arping) threads
    for i in range(nArpThreads):
        
        # Create pool of threads
        worker = Thread(target = arping, args = (i, outQueue))
        # Set the thread as a Daemon process. If this is not set before the thread start() the script will run indefinitely.
        worker.setDaemon(True)
        # Start the thread's activity 
        worker.start()
        
    mf.Cout("Main Thread Waiting")
    # Ensure that program does not exit until both queues have been emptied
    inQueue.join()
    outQueue.join()
                       
    mf.StopWatchStop()
