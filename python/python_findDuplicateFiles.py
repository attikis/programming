#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is an example of performing an MD5 checksum on a directory tree to find duplicate files.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import os

if __name__ == "__main__":
    mf.StopWatchStart()
    cwd = os.getcwd()
    #cwd = "/Users/administrator/my_work/root/"

    # Get directory tree paths, files, and directories
    pathList = mf.WalkPaths(cwd)
    # mf.Cout("Printing list of walk-paths:\n\t%s" % pathList)

    # Create an empty list to store the path of duplicate files
    dupList = []

    # Create an empty dictionary which will map a compound-key(file-size, md5Checksum) to the file name
    record = {}

    # For all the paths in the directory tree, compare all files with each other and find duplicates
    maxValue = len(pathList)

    # Use progress bar to know how much time is left to finish
    pBar, CallBack = mf.StartProgressBar(maxValue)

    # Loop over all files in the pathList (created using a path-walk)
    for index, file in enumerate(pathList):

        # Update progress bar
        CallBack(index, maxValue)    

        # Create a key to be used in dictionary, 
        compound_key = (os.path.getsize(file), mf.md5Checksum(file))

         # If the key is found in the "record" dictionary, add file-path to the duplicate list.
        if compound_key in record:
            #mf.Cout( "Found duplicate:\n\t%s" % (file) )
            dupList.append(file)
        # If the key is NOT found in the "record" dictionary, update the dictionary with the specific key-file entry.
        else:
            record[compound_key] = file
    mf.StopProgressBar(pBar)

    mf.Cout("Listing duplicate files:\n\t%s" % (dupList) )
    mf.Cout("Number of duplicate files found:\n\t%s" % (len(dupList) ) )
    mf.StopWatchStop()
