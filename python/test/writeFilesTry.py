#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example of opening files with python using the "try" and "finally" conditionals

# Definitions here
filePath  = "/Users/administrator/my_work/programming/python/writeTest.txt"
stringToWrite = "+++ This is a simple string to be written on " + filePath

# Write a simple string to the file
try:
    inFile = open(filePath, "w")
    inFile.write(stringToWrite)
finally:
    inFile.close()

# Check that we have successfully writen on the file
try:
    inFile = open(filePath, "r")
    print inFile.read()
finally:
    inFile.close()
