#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is an example class containing re-usable directory walking modules.
'''

# All required modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()
import os

class DiskWalk(object):
    ''' 
    An Application Programming Interface (API) for getting directory walking collections.
    '''

    def __init__ (self, path):
        self.path = path

    def WalkPaths(self):
        '''
        Returns the path to all the files in a directory as a list.
        '''
        path_collection = []
        # For each directory in the tree rooted at directory "path" (including "path" itself), the os.walk(path) yields a 3-tuple (dirpath, dirnames, filenames).
        for dirpath, dirnames, filenames in os.walk(self.path):
            for file in filenames:
                fullpath = os.path.join(dirpath, file)
                path_collection.append(fullpath)

        return path_collection

    def WalkFiles(self):
        '''
        Returns all the files in a directory as a list.
        '''
        file_collection = []
        # For each directory in the tree rooted at directory "path" (including "path" itself), the os.walk(path) yields a 3-tuple (dirpath, dirnames, filenames).
        for dirpath, dirnames, filenames in os.walk(self.path):
            file_collection = []
            for dirpath, dirnames, filenames in os.walk(self.path):
                for file in filenames:
                    file_collection.append(file)
                    
        return file_collection

    def WalkDir(self):
        '''
        Returns all the directories in a directory as a list.
        '''
        dir_collection = []
        # For each directory in the tree rooted at directory "path" (including "path" itself), the os.walk(path) yields a 3-tuple (dirpath, dirnames, filenames).
        for dirpath, dirnames, filenames in os.walk(self.path):
            for dir in dirnames:
                dir_collection.append(dir)

        return dir_collection
