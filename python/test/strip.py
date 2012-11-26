#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Examples of how to use the strip(), lstrip() and rstrip() methods.

# No arguments 
print "*" * 50
myString = "\n\t This is an example sentence.\n\t"
print "+++ Printing default form of myString"
print myString
print

print "+++ Printing myString.lstrip()"
print myString.lstrip()
print

print "+++ Printing myString.rstrip()"
print myString.rstrip()
print

print "+++ Printing myString.strip()"
print myString.strip()
print
print "*" * 50

# With optional arguments 
anotherString = "<This is another example sentence>"
print "+++ Printing default form of anotherString"
print anotherString
print

print '+++ Printing anotherString.lstrip("<")'
print anotherString.lstrip("<")
print

print '+++ Printing anotherString.rstrip(">")'
print anotherString.rstrip(">")
print

print '+++ Printing anotherString.strip(">").strip("<")'
print anotherString.strip("<").strip(">")
print

print '+++ Printing anotherString.strip("><")'
print anotherString.strip("<>")
print

otherString = "<><><>* Yet <> another <> string <*><*><*>"
print "+++ Printing default form of otherString"
print otherString
print '+++ Printing otherString.strip("><*")'
print otherString.strip("><*")
print
print '+++ Printing otherString.strip("><*").strip()'
print otherString.strip("><*").strip()
print

lastString1 = "<fooooooo> Last String <fo"
print "+++ Printing default form of lastString1"
print lastString1
print '+++ Printing lastString1.strip("><fo")'
print lastString1.strip("><fo")
print
lastString2 = "<fooooooo> Last String <fo!"
print "+++ Printing default form of lastString2"
print lastString2
print '+++ Printing lastString2.strip("><fo")'
print lastString2.strip("><fo")
print
print "*" * 50
