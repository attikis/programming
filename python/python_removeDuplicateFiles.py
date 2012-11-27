#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is an example of performing an MD5 checksum on a directory tree to find duplicate files. Instead of a list of the duplicates files, it creates
a dictionary mapping the two duplicate files
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()
import os

if __name__ == "__main__":
    mf.StopWatchStart()
    myPath = os.getcwd()
    #cwd = "/Users/administrator/my_work/root/"

    dupList, dupListMap = mf.FindDuplicateFiles(myPath)
    mf.Cout( "Number of duplicate files found: %s" % len(dupList) )
    mf.Cout("Listing duplicate files:")
    # Print mapping of duplicates
    for index, file in enumerate(dupList):
        print "\t%s -> %s" % (file, dupListMap[index])

    for file in dupList:
        mf.DeleteFile(file)
        
    #for file in dupListMap: #original scripts in this list
    #    mf.DeleteFile(file)
        
    mf.StopWatchStop()
