#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example script of how to retrieve email from a server

'''
Usage:
./python_email.py

Description:
This script is a simple interface to receive emails using the gmail or CERN SMTP servers. Just follow the prompt commands once launced.

Example:

...
'''

# Import modules here
import python_myFunctions as myFunctions
import imaplib
import time
import os
import re

f = myFunctions.CreateObject()

server = "cern"
# Decide which of the two servers to use
if server == "cern":
    popHost = "imap.cern.ch"
    emailAddress = "@cern.ch"
    popUsername = "attikis@cern.ch"
elif server == "gmail":
    popHost = "pop.gmail.com"
    emailAddress = "@gmail.com"
    popUsername = "alexandros.attikis@gmail.com"
else:
    f.Cout('ERROR! The server argument %s is invalid. Please select between "cern" and "gmail". Exiting python shell.')
    print __doc__
    sys.exit(1)

imap_host = 'imap.gmail.com'
mail = imaplib.IMAP4_SSL(imap_host)
mail.login("alexandros.attikis", "xKa[99448024]aa569282piasme")
mail.select("inbox") # connect to inbox.

while True:
    try:
        result, data = mail.uid('search', None, 'UNSEEN')
        uid_list = data[0].split()
        print len(uid_list), 'Unseen emails.'
        if len(uid_list) > 20:
         os.system('heroku restart --app xxx')
         time.sleep(60)
    except KeyboardInterrupt:
        print 'Quitting'
        pass
