#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a script that performs a verbose directory walk.
'''

# All required modules here
import python_myFunctions as myFunctions
import os

# Object and variable declarations here
mf = myFunctions.CreateObject()
myPath = "/tmp/"
#myPath = "/Users/administrator/my_work/programming/python"
#myPath = "/" # Will require 1 hours, 11 minutes, 26.0 seconds.
#myPath = "/Users/administrator/my_work/cms/lxplus/QCD_A_v4"


def WalkPaths(path):
    '''
    Returns a list of the path to all files in a directory and all sub-directories, recursively.
    '''
    path_collection = []
    for dir_path, dir_names, file_names in os.walk(path):
        mf.Cout( 'Files found in path "%s":' % (dir_path) )
        if len(file_names) == 0:
            print "\tNo file found."
        else:
            for file in file_names:
                print "\t%s" % (file)
                full_path = os.path.join(dir_path, file)
                path_collection.append(full_path)

    return path_collection


def WalkFiles(path):
    ''' 
    Returns a list of all the files in a directory. Does exactly the same thing as the WalkPaths(path) function, but instead of the full path it only prints the standalone
 file name.
    '''
    file_collection = []
    for dir_path, dir_names, file_names in os.walk(path):
        mf.Cout( 'Files found in path "%s":' % (dir_path) )
        if len(file_names) == 0:
            print "\tNo file found."
        else:
            for file in file_names:
                print "\t%s" % (file)
                file_collection.append(file)
                
    return file_collection


def WalkDir(path):
    '''
    Returns a list of all the directories in a given directory.
    ''' 
    dir_collection = []
    for dir_path, dir_names, file_names in os.walk(path):
        mf.Cout( 'Directories found in path "%s":' % (dir_path) )
        if len(dir_names) == 0:
            continue #print "\tNo dir found."
        else:
            for dir in dir_names:
                print "\t%s" % (dir)
                dir_collection.append(dir)

    return dir_collection


if __name__ == "__main__":
    mf.StopWatchStart()

    mf.Cout("Recursive listing of all paths in a dir:")
    myPaths = WalkPaths(myPath) #list object

    mf.Cout("Recursive listing of all files in dir:\n")
    myFiles = WalkFiles(myPath) #list object

    mf.Cout("Recursive listing of all dirs in dir:\n")
    myDirs = WalkDir(myPath) #list object

    mf.StopWatchStop()
