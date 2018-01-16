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
import subprocess

if __name__ == "__main__":
    
    path = []
    for i in range(1, 18):
        path.append("phy101_%i.pdf" %i)

    mergeCmd = "./join.py -o Phys101_Lectures.pdf" + ' '.join(path)
    print "*** Executing command:\n", mergeCmd
    p = subprocess.Popen("./join.py -o Phys101_Lectures.pdf " + ' '.join(path), shell = True, stdin = subprocess.PIPE)
