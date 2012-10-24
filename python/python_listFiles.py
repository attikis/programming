#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Lists files in current directory of desired extensiobs

import os
import subprocess

dir = os.getcwd()
print "+++ Listing files in %s" % (dir)
myInput=raw_input('File extenstion to list: ')
fileList = subprocess.check_output('ls -l *.' + myInput, shell=True)
print "+++ Saved to fileList, which is a variable of type %s" % ( type(fileList) )
print fileList
