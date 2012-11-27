#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a script that performs and md5 checksum on a given file. It is the official/solid way of ensuring whether two files are identical or not. 
However, a byte-by-by comparison is also 100% accurate.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

if __name__ == "__main__":
    mf.StopWatchStart()
    fileName1 = "/Users/administrator/my_work/programming/python/python_myFunctions.py"
    fileName2 = "/Users/administrator/my_work/programming/python/python_myGeneralFunctions.py"
    mf.CompareFiles(fileName1, fileName2)
    print
    mf.CompareFiles(fileName1, fileName1)
    mf.StopWatchStop()

