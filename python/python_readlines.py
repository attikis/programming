#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Alternative way of reading a file: readline (instead of "file.read()")

filePath = "/Users/administrator/my_work/programming/python/readlines.txt"
nLines = 10
# First need to create the file
try:
    inFile = open(filePath, "w")
    for i in range (0,nLines):
        string = "*** This is line number %s of file %s.\n" % (i, filePath)
        inFile.write(string)
finally:
    inFile.close()

# Read the file
nBytes = len(string)*nLines #approximately one character corresponds to 1 byte?
try: 
    inFile = open(filePath, "r")
    print inFile.readlines()        
    print
    print inFile.readlines(nBytes) # reads first nBytes bytes of the line only
finally:
    inFile.close()

