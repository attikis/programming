#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Demonstration of the find and index string commands.

myString = "Once upon a time, there was a brilliant physicist named Albert Einstein"
print '+++ Example of slicing the string:\n myString = "%s"' % (myString)
print

# Break string in two, according to a given index. 
index = myString.index(",")
print '+++ Use as index the substring:\n myString.index(",") = %s' % (index)
print

# Print index
print "+++ Printing:\n myString[%s] = %s" % (index, myString[index])
print

# Print only text before index
print "+++ Printing:\n myString[:%s] = %s[:%s]" % (index,myString,index)
print myString[:index]
print

# Print only text after index
print "+++ Printing:\n myString[%s:] = %s[%s:]" % (index,myString,index)
print myString[index:]
print
