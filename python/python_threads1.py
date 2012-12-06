#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a simple example of threading. Launches 5 threads in parallel which do literally nothing.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import threading
import time

# Declarations here
count = 1

class KissThread(threading.Thread):
    
    def run(self):
        global count
        mf.Cout("Thread #%s: Pretending to do stuff" % (count))
        count += 1
        time.sleep(4)
        mf.Cout("Done!")
        
        
if __name__ == "__main__":
    # Launch 5 threads
    for p in range(5):
        KissThread().start() # will run threads in parallel
        #KissThread().run() # will not run threads in parallel
