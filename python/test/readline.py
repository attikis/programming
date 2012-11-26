#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Alternative way of reading a file: readline (instead of "file.read()")

filePath = "/Users/administrator/my_work/programming/python/readline.txt"
nLines = 10
nBytes = 3
# First need to create the file
try:
    inFile = open(filePath, "w")
    for i in range (0,nLines):
        string = "*** This is line number %s of file %s.\n" % (i, filePath)
        inFile.write(string)
finally:
    inFile.close()

# Read the file
try: 
    inFile = open(filePath, "r")
    for i in range (0, nLines):
        print inFile.readline()        
        print inFile.readline(nBytes) # reads first nBytes bytes of the line only
finally:
    inFile.close()

