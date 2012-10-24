#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example of using functions from a different script/module

from python_sysinfoFunc2 import disk_func
import subprocess

def tmp_space():
    tmp_usage = "du"
    tmp_arg = "-h"
    path = "/tmp"
    print "+++ Gathering information on space used in %s directory with command %s %s :\n" % (path, tmp_usage, tmp_arg)
    subprocess.call([tmp_usage, tmp_arg, path])

def main():
    tmp_space()
    disk_func()

if __name__ == "__main__":
    main()
