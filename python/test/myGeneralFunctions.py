#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : Strictly an input module to be used in other executable scripts
# Definition  : My very first generic functions class, to be used for simple coding.
 
''' 
Usage:
import python_GeneralFunctions as myGFs

Description:
In this python module I define some generic functions that can be used in many executable scripts. 
The list of functions defined here will grow significantly over time, at which stage I should perhaps
consider its further break-down to more classes and functions.
''' 

# All module imports here
import string
        
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

    def obscureString(string):
        ''' obscureString(dict):
        A function to obscure a string by replacing all ascii printable characters with asterisks (*). This is mainly used in cases when you want to print a password without revealing its meaning, but just the number of characters.
        '''
        # Create a characters list
        CharactersList = []

        # Fill the list with all printable ascii characters
        for item in string.printable:
            CharactersList.append(item)
            obscuredString = string
        # Now loop over all readable characters and replace those in the input string with an asterisk
        for char in CharactersList:
            obscuredString = obscuredString.replace(char, "*")
        # Return the asterisk-obscured string
        return obscuredString
