#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example of opening files with python

# Definitions here
filePath  = "/Users/administrator/my_work/programming/python/writeTest.txt"
inFile = open(filePath, "w")
stringToWrite = "+++ This is a simple string to be written on " + filePath

# Write a simple string to the file
inFile.write(stringToWrite)
inFile.close()

# Check that we have successfully writen on the file
inFile = open(filePath, "r")
print inFile.read()
inFile.close()
