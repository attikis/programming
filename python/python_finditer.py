#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example use of the finditer() function

# Import regular expressions
import re

myString  = "My name is Alexandros Attikis."
myStringPattern  = r"\bA.*?s\b" #find words beginning with "A" and ending with "s"
reObject = re.compile(myStringPattern)

findallOutput = reObject.findall(myString)
print "+++ findall() output: %s \n" % (findallOutput)

reIterator = reObject.finditer(myString)
for item in reIterator:
    print "+++ finditer() output: ", item
    print "+++ item.group() output:", item.group()


