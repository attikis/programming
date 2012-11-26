#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Show the difference of printing an object and showing the official string representation of it

class DoubleRep(object):
    def __str__(self):
        return "Hi, I am a __str__"
    def __repr__(self):
        return "Hi, I am a __repr__"

def main():
    myObj = DoubleRep()
    myNum = 12
    print "+++ Printing string format of object myObject: %s" % (myObj)
    # equivalent to calling in shell: print myObject
    print "+++ Printing representation format of object myObject: %r" % (myObj)
    # equivalent to calling in shell: myObject
    print "\n"
    print "+++ Printing string format of object myNum: %r" % (myNum)
    print "+++ Printing representation format of object myNum: %r" % (myNum)

main()
