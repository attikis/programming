#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : The with statement, example

# Module import required before using "with"
from __future__ import with_statement

filePath  = "/Users/administrator/my_work/programming/python/writeTestWith.txt"
stringToWrite = "+++ This is another simple string to be written on " + filePath

with open(filePath, "w") as inFile: # will close file automatically
    inFile.write(stringToWrite)

# Since file is now closed the following line will give an IO Error:
#print inFile.read() 

with open(filePath, "r") as inFile: # will close file automatically
    print inFile.read()

# Since file is now closed the following line will give an IO Error:
#print inFile.read() 
