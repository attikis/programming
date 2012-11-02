#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : My very first generic functions class, to be used for simple coding.
 
class GeneralFunctions:
    
    def __init__(self):
        self.counter = 0

    # Function to display match objects
    def DisplayMatchObject(self, match):
        if match is None:
            return None
        print "match.group() = %r, match.groups() = %r>" % (match.group(), match.groups())
    # Loop over all groups and print them
        for iMatch in range (0, len(match.groups())+1):
            print 'group(%r) = %r' % (iMatch, match.group(iMatch))
            print 'groupdict(%r) = ' % (match.groupdict(iMatch))
        return 0
        
    # Function to cout each time with an extra "+" symbol
    def Cout(self, text):
        self.counter = self.counter+1
        print "%s %s" % ("+"*self.counter, text)        
        return 0
