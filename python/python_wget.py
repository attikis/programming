#!/usr/bin/env python
# Permissions : chmod +x fileName.py

'''
Usage:
./python_wget.py

Description:
This script is a simple interface to send emails using the gmail or CERN SMTP servers. Just follow the prompt commands once launced.

Example:
[attikis:python]> ./python_wget.py 
'''

import python_myFunctions as myFunctions
import subprocess

f = myFunctions.CreateObject()

if __name__ == "__main__":
    
    f.Cout("Testing the CERN server")
    path = []
    for i in range(1, 18):
        path.append("http://www.ucy.ac.cy/data/phy101_%i.pdf" %i)

    for item in path:
        p = subprocess.Popen("wget " + item, shell = True, stdin = subprocess.PIPE)
