#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Demonstration of the join() string command

nameList = ["Alexandros", "Xenios", "Ino", "Constantinos"]
 print "+++ nameList = ", nameList
print

names1 = ", ".join(nameList)
print '+++ names1 = ", ".join(nameList)'
print "+++ The Attikis family is comprised of %s." % (names1)
print 

names2 = " + ".join(nameList)
print '+++ names2 = " + ".join(nameList)'
print "+++ The Attikis family is comprised of %s." % (names2)
print

stockMarket = ["100.8", "101.3", "101.9", "102.1"]
print "+++ stockMarket = ", stockMarket
print '+++ "$".join(stockMarket) = ', "$ ".join(stockMarket)
print "+++ So, sometimes it doesn't work as you might expect. The joining string is placed BETWEEN elements of a list."
print

numList = []
for i in range(20,0,-1):
    numList.append(i)

print "+++ numList = %s " % (numList)
print '+++ Converting integer list to a string list with the "join()" string function '
myString =  " , ".join(str(i) for i in numList)
print myString
