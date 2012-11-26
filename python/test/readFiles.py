#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example of opening files with python

# Relevant imports of modules here
import subprocess

filePath  = "/Users/administrator/my_work/programming/python/test.txt"
inFile = open(filePath, "r")

print inFile.read()
#subprocess.call(["cat", filePath]) #alternatively
