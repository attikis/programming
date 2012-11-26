#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is an alternative and lightweight way of comparing directories. Think of os.listdir() as an ls command that returns a Python list of the files found.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import os
import shutil
cwd = os.getcwd()
testDir = cwd + "/test"
testDirCopy = cwd + "/test-copy"
dir1 = cwd + "/inbox/cern"
dir2 = cwd + "/inbox/gmail"
file1 = cwd + "/README"
file2 = cwd + "/README.txt"

if __name__ == "__main__":
    mf.StopWatchStart()

    # Copy the entire dir tree of "/test"
    if os.path.exists(testDirCopy):
        shutil.rmtree(testDirCopy)
    mf.Cout( 'Copying dir "%s" to "%s".' % (testDir, testDirCopy) )
    # Copy "/test" directory to "/test-copy" and artificially create differences between "/test" and "/test-copy"
    shutil.copytree(testDir, testDirCopy)
    shutil.copyfile(file1, testDirCopy + "/READMEcp")
    shutil.copyfile(file2, testDirCopy + "/READMEcp.txt")
    os.remove(testDirCopy + "/re.py")
    os.remove(testDirCopy + "/gmail.py")

    # Get directory ls
    lsTestDir      = os.listdir(testDir)
    lsTestDirCopy  = os.listdir(testDirCopy)
    lenTestDir     = len(lsTestDir)
    lenTestDirCopy = len(lsTestDirCopy)

    # Cast lists as sets in order to be able to subtract them (to find differences)
    setTestDir     = set(lsTestDir)
    setTestDirCopy = set(lsTestDirCopy)

    mf.Cout( 'Listing dir "%s": (len = %s)\n\t%s' % (testDir, lenTestDir, lsTestDir) )
    mf.Cout( 'Listing dir "%s": (len = %s)\n\t%s' % (testDirCopy, lenTestDirCopy, lsTestDirCopy) )
    mf.Cout( 'Looking for different files in dirs "%s" and "%s":\n\t"%s' % (testDir, testDirCopy, setTestDir - setTestDirCopy) )
    # N.B. : dir1-dir2  is NOT the same as dir2-dir1 since the one is a subset of the other and only extra items in the set will be marked as a difference.
    mf.Cout( 'Looking for different files in dirs "%s" and "%s":\n\t"%s' % (testDirCopy, testDir, setTestDirCopy - setTestDir) )

    # Finally, remove all the temporary "test-copy" directory.
    if os.path.exists(testDirCopy):
        rawInput = mf.Cin('Delete dir-tree:\n\t"%s"?' % (testDirCopy) )
        if rawInput == "y":
            shutil.rmtree(testDirCopy)
            mf.Cout('Deleted "%s".' % (testDirCopy) )
        else:
            mf.Cout('Did not delete "%s".' % (testDirCopy) )

    mf.StopWatchStop()
