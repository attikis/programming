#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example use of the finditer() function

# Import regular expressions
import re

def DisplayMatchObject(match):
    if match is None:
        return None
    return "match.group() = %r, match.groups() = %r>" % (match.group(), match.groups())

# List definitions here
#myPatternList  = ["abcd-1234", "bacd-2134", "abcd", "1234"]
myPatternList  = ["abcd", "The numbers 1234"]
myStringList = ["b", ".", ".*", "\w+", "\d+"] # "."=a single character, ".*"=any string of characters,  "\w+"=a string of letters, "\d+"=a string of digits
myStringDefList = ['Letter "b"', "A single character", "Any string of characters", "A string of lettters", "A string of digits"] 
startPosList = [0, 1, 2, 3]

# Double loop to search/match several patterns at different start positions
for iString, iStringDef in map(None, myStringList, myStringDefList):
    reObject = re.compile(iString)
    print '%s String "%s" (%s)' % ("+"*3, iString, iStringDef)
    for iPattern in myPatternList:
        print '%s Pattern "%s"' % ("+"*6, iPattern)
        search = reObject.search(iPattern)
        match = reObject.match(iPattern)
        print 'reObject.search("%s") = %s' % (iPattern, DisplayMatchObject(search))
        print 'reObject.match("%s") = %s' % (iPattern, DisplayMatchObject(match))
        for iPos in startPosList:
            endPos=len(iPattern)
            print '%s pos=%s, endpos=%s' % ("+"*9, iPos, endPos)
            searchPos = reObject.search(iPattern, pos=iPos, endpos = endPos)
            matchPos = reObject.match(iPattern, pos=iPos, endpos = endPos)
            print 'reObject.search("%s", pos=%s, endpos=%s) = %s' % (iPattern, iPos, len(iPattern), DisplayMatchObject(searchPos))
            print 'reObject.match("%s", pos=%s, endpos=%s) = %s' % (iPattern, iPos, len(iPattern), DisplayMatchObject(matchPos))
        print
