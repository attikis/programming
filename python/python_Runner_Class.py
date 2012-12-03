#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a class based on Subprocess. It helps the user simplify and automate the process of executing multiple shell commands in sequence. 
Simplifies subprocess call and runs over a sequence of commands. Runner takes N positional arguments, and optionally:
[optional keyword parameters]
delay = 1 (for time delay in seconds)
verbose = True (for verbose output)

Usage: 
cmd = Runner("ls -l", "df -h", verbose = True, delay=3)
cmd.run()
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import subprocess
import time
import sys

class Runner(object):
    '''
    Base Argument Class that handles keyword argument parsing.
    '''
    
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

        # Take care of the delay argument (in seconds)
        if self.kwargs.has_key("delay"):
            print "Delay = %s seconds" % (kwargs["delay"])
            self.delay = self.kwargs["delay"]
        else:
            self.delay = 0

        # Check whether to use verbose option or silend-mode instead
        if self.kwargs.has_key("verbose"):
            print "Verbose = %s" % (kwargs["verbose"])
            self.verbose = self.kwargs["verbose"]
        else:
            self.verbose = False        

            
    def Run(self):
        # Loop over all commands and execute them
        for cmd in self.args:
            # Print informative message only if verbose is enabled
            if self.verbose:
                print "Running %s with delay = %s" % (cmd, self.delay)
            
            time.sleep(self.delay)
            subprocess.call(cmd, shell = True)    

    def Help(self):
        print "Print Class docstrings:\n\t%s" % (__doc__)
