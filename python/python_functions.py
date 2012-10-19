#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Several function definitions

import subprocess 

# Define functions here
def printStuff():
    print "Hello World"
    print "My name is Alexandros"
    print "I want to learn python"

def addingOneAndOne():
    sum = 1+1
    print "1 + 1 = %s" % (sum)

def addition(num1, num2):
    sum = num1 + num2
    print "%s + %s = %s" % (num1, num2, sum)

def multiplication(num1, num2):
    product = num1 + num2
    print "%s x %s = %s" % (num1, num2, product)

# Call functions here
printStuff()
addingOneAndOne()
addition(3,2)
multiplication(10,3.5)
