#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a 
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import smtplib
import subprocess
import string

if __name__ == "__main__":
    mf.StopWatchStart()

    cmd = "df -h"
    p = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE)
    cmdMsg = p.stdout.read() #include as attachment
    fromWho = "attikis@cern.ch"
    toWhom = "alexandros.attikis@gmail.com"
    subject = "Nightly Disk Usage Report"
    msg = string.join( (
            "From: %s" % (fromWho),
            "To: %s" % (toWhom),
            "Subject: %s" % (subject),
            "",
            cmdMsg), "\r\n")
    server = smtplib.SMTP("smtp.cern.ch")
    server.sendmail(fromWho, toWhom, msg)
    server.quit()

    mf.StopWatchStop()
