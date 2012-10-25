#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Demonstration of the startswith and endswith string commands.

myString = "Once upon a time, there was a brilliant physicst named Albert Einstein"

# Simple use example
print "+++ Demonstration of 'startswith' and 'endswith' string commands"
print myString.startswith("Once")
print myString.startswith("SomeString")
print
print myString.endswith("Einstein")
print myString.endswith("SomeString")

# The same thing can be done with the slicing command, but it can be more involved:
print "+++ Demonstration of replicating 'startswith' and 'endswith' string commands with string slicing-1"
print myString[:len("Once")] == "Once"
print myString[:len("Once")] == "SomeString"
print
print myString[-len("Einstein"):] == "Einstein"
print myString[-len("Einstein"):] == "SomeString"
print

# OR, equivalently: Do it in a way I can understood what lies behind method
print "+++ Demonstration of replicating 'startswith' and 'endswith' string commands with string slicing-2"
# Define word that you want to test your string starts/ends with.
startString    = "Once"
endString      = "Einstein"
# Get their length
startStringLen = len(startString)
endStringLen   = len(endString)

#Use index slicing to look for the startString a given number of characters (startStringLen) BEFORE the START of myString
print myString[:startStringLen] == startString
print myString[:startStringLen] == "SomeString"
print
#Use index slicing to look for the endString a given number of characters (startStringLen) BEFORE the END of myString
print myString[-endStringLen:] == endString
print myString[-endStringLen:] == "SomeString"
