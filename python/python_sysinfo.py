#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Prints system information

import subprocess

# Command 1
uname = "uname"
uname_arg = "-a"
print "+++ Gathering system information with %s %s command:\n" % (uname, uname_arg)
subprocess.call([uname, uname_arg])

# Command 2
diskspace = "df"
diskspace_arg = "-h"
print "+++ Gathering system information with %s %s command:\n" % (diskspace, diskspace_arg)
subprocess.call([diskspace, diskspace_arg])

# Command 1 without splitting arguments also possible
uname_full = "uname -a"
print "+++ Gathering system information with %s command:\n" % (uname_full)
subprocess.call(uname_full, shell=True)
