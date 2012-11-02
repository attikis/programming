#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example use of the finditer() function

# Import regular expressions
import re

def DisplayMatchObject(match):
    if match is None:
        return None
    for iMatch in range (0, len(match.groups())+1):
        print 'group(%s) = %s' % (iMatch, match.group(iMatch))
    return "match.group() = %r, match.groups() = %r>" % (match.group(), match.groups())

# List definitions here
myStringList = ["Isaac Newton, physicist"]
myPatternList  = [r"(\w+) (\w+)"] #'All alphanumberic characters (\w). Also, "+" causes RE to match 1 or more repetitions of the preceding RE. 
# i.e. ab+ will match "a" followed by any non-zero number of "b"s; it will not match just "a".'

# Double loop to search/match several patterns at different start positions
for iString in myStringList:
    print '%s String "%s"' % ("+"*3, iString)
    for iPattern in myPatternList:
        print '%s Pattern "%s"' % ("+"*6, iPattern)
        search = re.search(iPattern, iString)
        match = re.match(iPattern, iString)
        print 'reObject.search("%s") = %s' % (iPattern, DisplayMatchObject(search))
        print
        print 'reObject.match("%s") = %s' % (iPattern, DisplayMatchObject(match))

# A more complicated example
pattern = r"(?P<first_name>\w+) (?P<last_name>\w+)" # The substring matched by the group is accessible within the rest of the regular expression via the symbolic group name "name". Group names must be valid Python identifiers, and each group name must be defined only once within a regular expression.
string = ["Alexandros Attikis", "Malcolm Reynolds", "Xenios Attikis", "Andreas Sfikouris"]
print '%s A more complicated example' % ("+"*9)
# Loop over string list
for iString in string:
    reObject = re.compile(pattern)
    search = reObject.search(iString)
    match = reObject.match(iString)
    print 'reObject.search("%s", "%s") = %s' % (pattern, iString, DisplayMatchObject(search))
    print 'reObject.match("%s", "%s") = %s' % (pattern, iString, DisplayMatchObject(match))
    print "First name = " , search.group("first_name")
    print "Last name = " , search.group("last_name")
    print
