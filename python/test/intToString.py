#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example of how to convert an int list to a string list

intList = []
for i in range(20,0,-1):
    intList.append(i)
    
print "+++ intList = %s " % (intList)
print 
print '+++ Converting integer list to a string with the "join()" string function '
myString =  " , ".join(str(i) for i in intList)
print myString
print 

print "+++ Converting an integer list to a string list (casting)"
intStringList = [str(i) for i in intList]
print intStringList
