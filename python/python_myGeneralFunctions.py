#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : My very first generic functions class, to be used for simple coding.
 
class GeneralFunctions:
    
    def __init__(self):
        self.counter = 0


    def DisplayMatchObject(self, match):
        ''' DisplayMatchObject(self, match):
        A function to display match objects
        '''
        if match is None:
            return None
        print "match.group() = %r, match.groups() = %r>" % (match.group(), match.groups())
    # Loop over all groups and print them
        for iMatch in range (0, len(match.groups())+1):
            print 'group(%r) = %r' % (iMatch, match.group(iMatch))
            print 'groupdict(%r) = ' % (match.groupdict(iMatch))
        return 0
        
    def Cout(self, text):
        ''' sortedDictKeys(dict):
        A function to cout each time with an extra "+" symbol
        '''
        self.counter = self.counter+1
        print "%s %s" % ("+"*self.counter, text)        
        return 0
    
    def sortedDictKeys(dict):
        ''' sortedDictKeys(dict):
        A function to sort keys of a dictionary. A mapping (such as a "dictionary) has NO order, thus it cannot be sorted. Still, its keys can be extracted as a list, which can then be sorted.
        '''
        keys = dict.keys()
        keys.sort()
        return [key for key in keys]

    def sortedDictValues(dict):
        ''' sortedDictKeys(dict):
        A function to sort values of a dictionary, according to sorted keys. A mapping (such as a "dictionary) has NO order, thus it cannot be sorted. Still, its keys can be extracted as a list, which can then be sorted.
        '''
        
        keys = dict.keys()
        keys.sort()
        return [dict[key] for key in keys]
