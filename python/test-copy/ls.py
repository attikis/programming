#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./python.py 
# Definition  : Python wrapper for the "ls" bash command

import subprocess

subprocess.call(["ls","-l"])
