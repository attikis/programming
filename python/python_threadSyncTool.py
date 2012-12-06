#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is an example of a threaded event handler. Basically, we take a delayed thread and mix in an event loop that watched two directories for changes in filames.
So, it uses rsync -av --delete to keep 2 directories in sync if they fall out of sync, in a delayed background thread. Obviously, the delay is not strictly necessary. But,
it can have some benefits. If you add a delay (say 10 seconds), you could tell the thread to cancel if you discovered another event, such as if your master directory was 
accidentally deleted. A thread delay is a great mechanism to create conditional future operations that can still be cancelled.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
from threading import Timer
import sys
import time 
import copy
import os
from subprocess import call

class EventLoopDelaySpawn(object):
    '''
    An Event loop class that spawns a method in delayed thread.
    '''
    
    def __init__(self, poll=20, wait = 1, verbose = True, dir1 = "/Users/administrator/my_work/programming/python/dir1/", dir2 = "/Users/administrator/my_work/programming/python/dir2/"):
        self.poll = int(poll)
        self.wait = int(wait)
        self.verbose = verbose
        self.dir1 = dir1
        self.dir2 = dir2

    def poller(self):
        '''
        Creates a poll interval.
        '''
        # Sleep for self.poll
        time.sleep(self.poll)
        if self.verbose:
            mf.Cout("Checking at %s sec interval" % (self.poll))

    def action(self):
        if self.verbose:
            mf.Cout("Waiting %s second to run Action" % (self.wait))
        # Call Rsync command to syncronise the two directories
        retVal = mf.Rsync(self.dir1, self.dir2)

    def eventHandler(self):
        '''
        Take action (rsync) if the two directory contents are found to be different. Inform user if verbose set to true.
        '''
        if os.listdir(self.dir1) != os.listdir(self.dir2):
            mf.Cout(os.listdir(self.dir1))
            # Create thread with a built-in delay of self.wait seconds
            t = Timer((self.wait), self.action)
            # Launch thread
            t.start()
            if self.verbose:
                mf.Cout("Event Registered")
        else:
            if self.verbose:
                mf.Cout("No Event Registered")

    def run(self):
        '''
        Runs an event loop wiath a delayed action method.
        '''
        try:
            # Infinite Loop!
            while True:
                self.eventHandler()
                self.poller()


        except Exception, err:
            mf.Cout("ERROR! %s" % (err))

        finally:
            sys.exit(0)
                   
            
if __name__ == "__main__":
    mf.StopWatchStart()
    
    E = EventLoopDelaySpawn()
    E.run()
    
    mf.StopWatchStop()
