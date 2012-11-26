#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Alternative way of reading a file: readline (instead of "file.read()")

filePath = "/Users/administrator/my_work/programming/python/writelines_more.txt"

# Define here a generator function
def myRange(max):
    i = 0
    while i < max:
        yield "*** Loop index = %s. File = %s.\n" % (i, filePath)
        i = i + 1

# Write to file using the aforementioned generator
try:
    inFile = open(filePath, "w")
    inFile.writelines(myRange(5))
finally:
    inFile.close()

# Read the file
try: 
    inFile = open(filePath, "r")
    print inFile.read()
finally:
    inFile.close()
