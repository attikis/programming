#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This script copies all files in current working directory whose name includes python_*.py, to a "/test" directory. In the process, the files are renamed in a way as to remove 
the "python_" prefix.
'''

# All required modules here
import python_myFunctions as myFunctions
import os
import shutil #enables copying of file

# Object and variable declarations here
mf = myFunctions.CreateObject()

if __name__ == "__main__":
    mf.StopWatchStart()
    cwd = os.getcwd()
    dirName = cwd
    newDirName = cwd+"/test/"
    
    mf.Cout( "Printing current working directory (cwd):\n\t%s" % (os.getcwd()) )
    filesList = os.listdir(cwd)
    pyFilesList = []
    mf.Cout( "Listing files in cwd:\n\t%s" % (os.listdir(cwd)) )
    # Createa a list with all python scripts
    for file in filesList:
        if "python_" in file and file.endswith(".py"):
            pyFilesList.append(file)
            
    mf.Cout("Number of python files found:\n\t%s" % (len(pyFilesList))) # Can verify with bash shell command: [attikis:python]>  ls -1 python_* | wc -l 
    # mf.Cout("Printing their names:\n\t%s" % pyFilesList)

    # Loop over the python scripts list and fist copy them to the test/ directory 
    for pyFile in pyFilesList:
        newPyFileName = pyFile.replace("python_", "")
        path = newDirName+newPyFileName
        mf.Cout("Copying file %s to:\n\t%s" % (pyFile, path))
        shutil.copy(pyFile, path)
    
    mf.StopWatchStop()
