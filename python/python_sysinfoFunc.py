#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Prints system info

# Import requred modules
import subprocess

# Function definitions here
def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print "+++ Gathering system information with %s %s command:\n" % (uname, uname_arg)
    subprocess.call([uname, uname_arg])

def disk_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print "+++ Gathering system information with %s %s command:\n" % (diskspace, diskspace_arg)
    subprocess.call([diskspace, diskspace_arg])

def main():
    uname_func()
    disk_func()

# Call functions here
main()
