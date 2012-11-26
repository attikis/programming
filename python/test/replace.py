#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : A demonstration of the replace command, which takes two arguments. The string to replace and the string to replace it with. 

# Simple example
myString = "This is a string"
print "+++", myString

print '+++ myStringReplaced = myString.replace("string","sentence")'
myStringReplaced = myString.replace("string","sentence")
print "+++", myStringReplaced
print
