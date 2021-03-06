#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : re no-compile code performance test

# import regular expressions module
import re

def run_re():
    pattern = "pDq"
    inFile = open("test.txt", "r")
    matchCount=0
    nLines=0
    for iLine in inFile:
        match = re.search(pattern, iLine)
        if match:
            matchCount += 1
        nLines += 1
    return (nLines, matchCount)

if __name__ == "__main__":
    nLines, matchCount = run_re()
    print "+++ Lines = ", nLines
    print "+++ Matches = ", matchCount
