#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example script of how to pass command-line arguments to the script during execution from the shell

''' 
Usage:
python_logFileParser.py arg1 arg2 arg3

Description:
This script takes 3 command line arguments (arg1 = grep option, arg2 = string to grep on, arg3 = file extension),
 and it performs a simple grep of the keyword using the user-defined options.
''' 

# Import necessary modules here
import os
import sys
import python_myGeneralFunctions as myGFs
import subprocess

# Define functions here
def myGrep(option, keyWord, fileExtension):
    command = "grep " + option + " " + keyWord + " *." + fileExtension.encode('unicode-escape')
    gf.Cout('Executing grep command:\n\t %s' % (command))
    output = subprocess.call(command, shell=True)
    return output

if __name__ == "__main__":
    gf = myGFs.GeneralFunctions()
    # Check that all arguments have been passed
    if not len(sys.argv)>3:
        gf.Cout("ERROR! No input arguments specified. Please provide a valid grep-command option and keyword. Exiting python shell.")
        print __doc__
        sys.exit(1)
    # Main manipulations here
    option = sys.argv[1]
    keyWord = sys.argv[2]
    fileExtension = sys.argv[3]
    gf.Cout("Input argumets:\n\t option = %s, keyword = %s, fileExtension = %s"  % (option, keyWord, fileExtension))
    results = myGrep(option, keyWord, fileExtension)
