#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : split() command used to split up a string

string1 = "pt1,pt2,pt3,pt4"
print "+++ string1 = ", string1
print '+++ string1.split(",") = %s' % (string1.split(","))
print

string2 = "pt1|pt2|pt3|pt4"
print "+++ string2 = ", string2
print '+++ string2.split("|") = %s' % (string2.split("|"))
print

string3 = "pt1 pt2 pt3 pt4"
print "+++ string3 = ", string3
print '+++ string3.split(" ") = %s' % (string3.split(" "))
print

string4 = "pt1 <**> pt2 <**> pt3 <**> pt4"
print "+++ string4 = ", string4
print '+++ string4.split(" <**> ") = %s' % (string4.split(" <**> "))
print '+++ string4.split(" <**> ", 1) = %s' % (string4.split(" <**> ",1))
print '+++ string4.split(" <**> ", 2) = %s' % (string4.split(" <**> ",2))
print

string5 = "My name is Alexandros Attikis"
print "+++ string5 = ", string5
print "+++ string5.split()", string5.split()
print '+++ string5.split(" ")', string5.split(" ")
print

mLineString = "This \n is \n a multiline \n string"
print "+++ mLineString = ", mLineString
print "+++ mLineString.split() = ", mLineString.split()
print "+++ mLineString.splitlines() = ", mLineString.splitlines()
print

print "+++ Printing all characters in a multi-line string"
for line in mLineString:
    print line.split()

print
print "+++ Printing all words in a multi-line string (in separate lists)"
for line in mLineString.splitlines():
    print line.split()
    print

print "+++ Printing all words in a multi-line string (in one list)"
print "+++ mLineString.splitlines() = ", mLineString.splitlines()
