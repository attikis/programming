#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example of using the enumerate function.

inFile = "/Users/administrator/my_work/programming/python/readlines.txt"

inLines = open(inFile).readlines()

print "Index: String"
for i, line in enumerate(inLines):
    print "%s: %s" % (i, line)

myList = ["Alexandros", "Attikis", "PhD", "Physics", "UCY"]
print myList
for counter, item in enumerate(myList):
    print "Counter = %s, List item = %s" % (counter, item)

    
