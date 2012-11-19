#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example script of how to pass command-line arguments to the script during execution from the shell

''' 
Usage:
python_arguments2.py arg1 arg2 arg3

Description:
This script takes 3 command line arguments (arg1 = grep option, arg2 = string to grep on, arg3 = file extension),
 and it performs a simple grep of the keyword using the user-defined options.

Help:
[attikis:python]> ./python_arguments2.py -h
Out[1] Number of arguments provided:
	2
Out[2] sys.argv[0] = ./python_arguments2.py
Out[3] sys.argv[1] = -h

Out[4] This script takes three (3) mandatory arguments. Please read the docstrings. Exiting python shell.
 
Example:
[attikis:python]> ./python_arguments2.py il ftplib py
Out[1] Number of arguments provided:
	4
Out[2] sys.argv[0] = ./python_arguments2.py
Out[3] sys.argv[1] = il
Out[4] sys.argv[2] = ftplib
Out[5] sys.argv[3] = py

Out[6] Input argumets:
	 option = il, keyword = ftplib, fileExtension = py
Out[7] Executing grep command:
	 grep -il ftplib *py
python_ftplib.py
''' 

# Import necessary modules here
import os
import sys
import python_myFunctions as myGFs
import subprocess

# Object declaration here
mf = myGFs.CreateObject()

# Define functions here
def myGrep(option, keyWord, fileExtension):
    command = "grep -" + option + " '" + keyWord + "' *" + fileExtension.encode('unicode-escape')
    mf.Cout('Executing grep command:\n\t %s' % (command))
    output = subprocess.call(command, shell=True)
    return output

if __name__ == "__main__":
    # Check that script execution is valid (includes mandatory options). If not help user.
    if not len(sys.argv) == 3+1:
        mf.Cout("This script takes three (3) mandatory arguments. Please read the docstrings. Exiting python shell.")
        print __doc__
        sys.exit(1)
    mf.Cout("Number of arguments provided:\n\t%s" % (len(sys.argv) ) )
    for item in range(0, len(sys.argv) ):
        mf.Cout("sys.argv[%s] = %s" % (item, sys.argv[item]))
    print ""

    if "-h" in sys.argv or "--help" in sys.argv:
        mf.Cout("This script takes three (3) mandatory arguments. Please read the docstrings. Exiting python shell.")
        print __doc__
        sys.exit(1)

    # Main manipulations here
    option = sys.argv[1]
    keyWord = sys.argv[2]
    fileExtension = sys.argv[3]
    mf.Cout("Input argumets:\n\t option = %s, keyword = %s, fileExtension = %s"  % (option, keyWord, fileExtension))
    results = myGrep(option, keyWord, fileExtension)
    
