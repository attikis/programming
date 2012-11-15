#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example script of how to retrieve email from a server

'''
Usage:
./python_getEmailImap.py

Description:
This is a simple example of how to use the IMAP protocol to receive emails. As I understand, the IMAP protocol is more involved in the python libraries 
than the POP3 analogue, with more complicated/obscure modules. It does however offer a mean of accessing unread email, unlike the POP3 protocol for which I had to 
create a time-stamp support to know when it was the last time I checked my inbox. Nevertheless, at present I prefer POP3.

Example:
[attikis:python]> ./python_getEmailImap.py
Out[1] Please provide your login password for attikis@cern.ch to continue:
Out[2] Attempting to connect to:
	host = imap.cern.ch.
Out[3] Connecting to INBOX.
('OK', ['74'])
Out[4] * OK The Microsoft Exchange IMAP4 service is ready.
Out[5] You have 74 messages (2 NEW) in your inbox.
Out[6] Saving NEW mail to "/Users/administrator/my_work/programming/python/inbox/cern/imap/":
Out[7] 	['73.eml', '74.eml']
In[1] To open NEW mail press "y": y
Out[8] Paging NEW emails. Press "q" to read the next email.
Out[9] Done. Exiting python shell.
...
'''

# Import modules here
import python_myFunctions as myFunctions
import imaplib
import email
import traceback
import sys
import getpass 
import time 
from datetime import datetime
from dateutil import parser 
import os
import pydoc

# Declaration here
f = myFunctions.CreateObject()
newMailFiles = []
server = "cern" #"gmail"
myPath = "/Users/administrator/my_work/programming/python/inbox/" + server + "/imap/"

# Decide which of the two servers to use
if server == "cern":
    imapHost = "imap.cern.ch"
    emailAddress = "@cern.ch"
    imapUsername = "attikis@cern.ch"
elif server == "gmail":
    imapHost = "imap.gmail.com"
    emailAddress = "@gmail.com"
    imapUsername = "alexandros.attikis@gmail.com"
else:
    f.Cout('ERROR! The server argument %s is invalid. Please select between "cern" and "gmail". Exiting python shell.')
    print __doc__
    sys.exit(1)

# Prompt user to provide his login password
f.Cout("Please provide your login password for %s to continue:" % (imapUsername))
imapPassword = getpass.getpass("\tPassword = ")

# Connect to IMAP host server over SSL using login credentials
f.Cout("Attempting to connect to:\n\thost = %s." % (imapHost))
connection = imaplib.IMAP4_SSL(imapHost)
connection.login(imapUsername, imapPassword)
f.Cout("Connecting to INBOX.")
print connection.select("INBOX", readonly=True) # connect to inbox.
f.Cout(connection.welcome)

# Search messages on server "INBOX" [search(self, charset, *criteria)] and get total number of messages in mailbox (both seen and unseen)
AllMail = connection.search(None, "ALL")[1][0].split()  # returns a nice list of messages
UnseenMail = connection.search(None, "UNSEEN")[1][0].split()  # returns a nice list of messages
numAllMail = len(AllMail)
numUnseenMail = len(UnseenMail)
f.Cout( "You have %s messages (%s NEW) in your inbox." % (numAllMail, numUnseenMail) )

# Loop over all messages and write them down to files
f.Cout('Saving NEW mail to "%s":' % (myPath))
for mailId in UnseenMail:
    try:
        fileName = "%s.eml" % (mailId)
        newMailFiles.append(fileName)
        saveFile = open(myPath + fileName, "w")
        mailBody = connection.fetch(mailId, '(RFC822)')[1][0][1]
        saveFile.write(mailBody)
    finally:
        saveFile.close()
f.Cout("\t%s" % ([item for item in newMailFiles]) )

# Before closing program ask user if he wants to open the new emails for the user
openMail = f.Cin('To open NEW mail press "y"')
if openMail == "y":
    f.Cout('Paging NEW emails. Press "q" to read the next email.')
    for mail in newMailFiles:
        myNewMail = open(myPath + mail, "r")
        pydoc.pager(myNewMail.read()) # similar to | less in shell. Press "q" to move to next email
f.Cout('Done. Exiting python shell.')
connection.logout()
