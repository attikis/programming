#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a ...
'''

# All required modules here
import python_myFunctions as myFunctions
import os
import shutil

# Object and variable declarations here
mf = myFunctions.CreateObject()
dirList = []

if __name__ == "__main__":
    mf.StopWatchStart()
    # Get current working directory
    cwd = os.getcwd()
    if cwd.endswith("/") == False:
        cwd = cwd + "/"
    mf.Cout("Current working directory (cwd):\n\t%s" % (cwd) )

    # Create directory tree!
    dirTree = "test/test1/test2/test3"
    #dirList.append(cwd+"test")

    # Make directories
    if not os.path.exists(dirTree):
        os.makedirs(dirTree)

    # Change directory to test3
    os.chdir(cwd+dirTree)

    # Print contents of current working directory
    ls = os.listdir(cwd+dirTree)
    mf.Cout("Listing files in %s:\n\t%s" % (cwd, ls) )

    # Copy entire tree
    if not os.path.exists(cwd+"test-copy"):
        mf.Cout( "Copying %s to:\n\t%s" % (cwd+"test", cwd+"test-copy") )
        shutil.copytree(cwd+"test", cwd+"test-copy")
        #dirList.append(cwd+"test-copy")
        ls = os.listdir(cwd+"test-copy")
        mf.Cout("Listing files in %s:\n\t%s" % (cwd+"test-copy", ls) )
        
    # Rename a directory tree
    if (os.path.exists(cwd+"test-copy") and not os.path.exists(cwd+"test-copy-moved")):
        mf.Cout( "Moving %s to:\n\t%s" % (cwd+"test-copy", cwd+"test-copy-moved") )
        shutil.move(cwd+"test-copy", cwd+"test-copy-moved")
        dirList.append(cwd+"test-copy-moved")
        ls = os.listdir(cwd+"test-copy-moved")
        mf.Cout("Listing files in %s:\n\t%s" % (cwd+"test-copy-moved", ls) )

    # Finally, remove all test directories.
    for item in dirList:
        if os.path.exists(item):
            rawInput = mf.Cin("Remove [%s]?" % (item) )
            if rawInput == "y":
                mf.Cout("Removing dir:\n\t%s" % (item) )
                shutil.rmtree(item)
            else:
                mf.Cout("Will not remove dir:\n\t%s" % (item) )

    mf.StopWatchStop()
