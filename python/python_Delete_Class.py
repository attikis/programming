#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is an example class that is dedicated to deleting anything (files, directories..)
'''

# All required modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()
import os

class Delete(object):
    ''' 
    An Application Programming Interface (API) for deleting file objects.
    '''
    
    def __init__ (self, path):
        self.path = path

    def Interactive(self):
        '''
        Interactive deletion mode. User verification required.
        '''
        rawInput = mf.Cin("Delete %s [N]/Y " % (self.path) )
        if rawInput.upper() == "Y":
            mf.Cout("Deleting: %s" % (self.path) )
            status = os.remove(self.path)
        else:
            mf.Cout("Skipping: %s" % (self.path) )


    def DryRun(self):
        '''
        Simulation deletion mode. Only prints a statements. Does not delete anything.
        '''
        mf.Cout( "Dry Run: %s [NOT DELETED]" % (self.path) )
        return

    
    def Delete(self):
        '''
        Non-interactive deletion mode, with additional conditions.
        '''
        mf.Cout("Deleting: %s" % (self.path) )
        try:
            status = os.remove(self.path)
        except Exception, err:
            mf.Cout("%s" % (err)) 
            return status
