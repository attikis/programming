#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Demonstration of the find and index string commands.

string1 = "Once upon a time, there was a brilliant physicst named Albert Einstein"

# Find command
print "+++ Demonstration of print command"
print string1.find("Alexandros") #fail example: doesn't crash
print string1.find("Once")
print string1.find("upon")
print string1.find("a")
print string1.find("time")
print string1.find("Albert")
print string1.find("Alb")
print string1.find("Einstein")

# Index command
print "+++ Demonstration of index command"
#print string1.index("Alexandros") #fail example: crashes!
print string1.index("Once")
print string1.index("upon")
print string1.index("a")
print string1.index("time")
print string1.index("Albert")
print string1.index("Alb")
print string1.index("Einstein")

# More uses: Can break a sentence in two according to a given index. 
index1 = string1.index(",")

# Print index1
print string1[index1]

# Print only text before index1
print string1[:index1]

# Print only text after index1
print string1[index1:]
