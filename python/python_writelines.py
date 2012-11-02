#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Alternative way of reading a file: readline (instead of "file.read()")

filePath = "/Users/administrator/my_work/programming/python/writelines.txt"
nLines = 10
stringList = ["Alexandros", "Attikis", "1982", "University of Cyprus"]

# First need to create the file
try:
    inFile = open(filePath, "w")
    inFile.writelines("*** This is line number %s.\n" % i for i in range(nLines))
    inFile.write("\n")
    inFile.writelines("*** %s.\n" % j for j in stringList)
    #inFile.writelines("%s\n" % i for i in range(nLines))
finally:
    inFile.close()

# Read the file
try: 
    inFile = open(filePath, "r")
    #print inFile.readlines()
    print inFile.read()
finally:
    inFile.close()
