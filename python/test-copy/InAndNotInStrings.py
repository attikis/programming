#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : 'in' and 'not in' functions to chech whether a string contains another string.

import subprocess

res = subprocess.Popen(['uname', '-sv'], stdout=subprocess.PIPE)
# The strip function removes the leading and trailing characters.
uname = res.stdout.read().strip()
print uname

stringCheck1 = 'Darwin' in uname
print stringCheck1

stringCheck2 = 'Darwin' not in uname
print stringCheck2

stringCheck1 = 'Alexandros' in uname
print stringCheck1

stringCheck2 = 'Alexandros' not in uname
print stringCheck2

myName = "Alexandros Attikis"
stringCheck3 = 'Alexandros' in myName
print stringCheck3
stringCheck4 = 'Atikis' in myName
print stringCheck4
