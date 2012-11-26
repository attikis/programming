#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
The filecmp (aka file compare) module enables one to compare files, among other things, and check if they are identical (returns True) or not (returns False).
'''

# All required modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

import filecmp
import os
import shutil #for copying/moving/renaming files etc..

# Declarations here
cwd = os.getcwd()
file1 = cwd + "/README"
file2 = cwd + "/README.txt"
dir1 = cwd + "/inbox/cern"
dir2 = cwd + "/inbox/gmail"
testDir = cwd + "/test"
testDirCopy = cwd + "/test-copy"

if __name__ == "__main__":
    mf.StopWatchStart()
    mf.Cout( 'Comparing files "%s" and "%s":\n\t"%s' % (file1, file2, filecmp.cmp(file1, file2)) )
    mf.Cout( 'Comparing files "%s" and "%s":\n\t"%s' % (file1, file1, filecmp.cmp(file1, file1)) )

    # The command diff_files will compare ONLY the differences between files with the same name. The result is a list containg the identically named files in which
    # differences were found
    mf.Cout( 'Comparing differences between identically named files in dirs "%s" and "%s":\n\t"%s' % (dir1, dir2, filecmp.dircmp(dir1, dir2).diff_files) )

    # The command same_files will ONLY report  back files that are identical in two directories.
    mf.Cout( 'Looking for identical files in dirs "%s" and "%s":\n\t"%s' % (dir1, dir2, filecmp.dircmp(dir1, dir2).same_files) )
    
    # Lets try to get a non-empty list - Copy an entire tree
    if not os.path.exists(testDirCopy):
        mf.Cout( 'Copying dir "%s" to "%s".' % (testDir, testDirCopy) )
        shutil.copytree(testDir, testDirCopy)
    mf.Cout( 'Looking for identical files in dirs "%s" and "%s":\n\t"%s' % (testDir, testDirCopy, filecmp.dircmp(testDir, testDirCopy).same_files) )
    
    # Check out the filecmp.report() module. Generates a report of the differences between two directoris.
    mf.Cout( "Report for differences between dirs %s and %s:\n\t%s" % (dir1, dir2, filecmp.dircmp(dir1, dir2).report()) )
    # Since testDirCopy is a copy of testDir the will be  alist of identical files. For example-reasons copy two extra files in the testDirCopy directory.
    shutil.copyfile(file1, testDirCopy + "/READMEcp")
    shutil.copyfile(file2, testDirCopy + "/READMEcp.txt")
    if os.path.exists(testDirCopy + "/re.py"):
        os.remove(testDirCopy + "/re.py")
    mf.Cout( "Report for differences between dirs %s and %s:\n\t%s" % (testDir, testDirCopy, filecmp.dircmp(testDir, testDirCopy).report()) )

    # Finally, remove all the temporary "test-copy" directory.
    if os.path.exists(testDirCopy):
        rawInput = mf.Cin('Delete dir-tree:\n\t"%s"?' % (testDirCopy) )
        if rawInput == "y":
            shutil.rmtree(testDirCopy)
            mf.Cout('Deleted "%s".' % (testDirCopy) )
        else:
            mf.Cout('Did not delete "%s".' % (testDirCopy) )

    mf.StopWatchStop()
