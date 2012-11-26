#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example script of how to retrieve email from a server

'''
Usage:
./python_email.py

Description:
This script is a simple interface to receive emails using the Gmail or CERN pop servers. Just follow the prompt commands once launced.

Example:
[attikis:python]> ./python_receiveEmailPop.py
[1] Current date and time (yyyy:mm:dd hh:mm:ss):
	2012-11-12 14:50:01.711933
[2] Last inbox check was (yyyy:mm:dd hh:mm:ss):
	2012-11-09 16:13:35.105956
[3] Time elapsed since last check:
	2 days, 22 hours, 36 minutes, 26 seconds ago
[4] Please provide your login password for alexandros.attikis@gmail.com to continue:
	Password = 
[5] Attempting to connect to:
	host = pop.gmail.com.
[6] +OK Gpop ready for requests from 62.12.75.180 x3pf15575650wid.4
[7] You have no mail. Exiting python shell.


...
'''

# Import modules here
import python_myFunctions as myFunctions
import poplib
from email import parser as eParser
import traceback
import sys
import getpass 
import time 
from datetime import datetime
from dateutil import parser 
import os
import pydoc

# Declarations here
f = myFunctions.CreateObject()
server = "gmail" #gmail or cern
myPath = "/Users/administrator/my_work/programming/python/inbox/" + server + "/"
iNewMail = 0
newMailFiles = []
timeStampFile = "timestamp.txt"    
today = datetime.now()

# Get time elaplsed since last email check
if not os.path.isfile(myPath + timeStampFile):
    try:
        myTimeStampFile = open(myPath + timeStampFile, "w")
        myTimeStampFile.write(str(today))
    finally:
        myTimeStampFile.close()

try:
    myTimeStampFile = open(myPath + timeStampFile, "r")
    lastCheckTime = myTimeStampFile.readline().lstrip().strip().rstrip()
    lastTime = parser.parse(lastCheckTime)
    dt = today - lastTime
finally:
    myTimeStampFile.close()
    days = dt.days
    hours   = int((dt.seconds - dt.seconds%3600.0) / 3600)
    minutes = int((dt.seconds - hours*3600) / 60)
    seconds = int(dt.seconds - hours*3600 - minutes*60.0)

# Inform user of last inbox check
f.Cout("Current date and time (yyyy:mm:dd hh:mm:ss):\n\t%s" % (today))
f.Cout("Last inbox check was (yyyy:mm:dd hh:mm:ss):\n\t%s" % (lastCheckTime) )
f.Cout("Time elapsed since last check:\n\t%s days, %s hours, %s minutes, %s seconds ago" % (days, hours, minutes, seconds) )

# Decide which of the two servers to use
if server == "cern":
    popHost = "pop.cern.ch"
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

# Prompt user to provide his login password
f.Cout("Please provide your login password for %s to continue:" % (popUsername))
popPassword = getpass.getpass("\tPassword = ")

# Connect to host server using login credentials
f.Cout("Attempting to connect to:\n\thost = %s." % (popHost))
connection = poplib.POP3_SSL(popHost)
connection.user(popUsername)
connection.pass_(popPassword)
f.Cout(connection.getwelcome())

# Get number of messages and mailbox status: Result is tuple of 2 ints (message count, mailbox size)
numMessages = len(connection.list()[1])
messageCount = connection.stat()[0] 
mailboxSize = connection.stat()[1]
if messageCount > 0:
    f.Cout("Your inbox has %s messages in total (%s Mbytes)." % (numMessages, mailboxSize/1000000.0) )
else:
    f.Cout("You have no mail. Exiting python shell.")
    sys.exit(1)
    
#Get messages from server in the form of a list ([ ])
messages = [connection.retr(i) for i in range(1, numMessages + 1)]

# Concat message pieces
messages = ["\n".join(mssg[1]) for mssg in messages]

# Parse message into an email object. The email.parser.Parser method creates an in-memory object tree representing the email message, 
# which can then be manipulated and turned over to a Generator to return the textual representation of the message.
messages = [eParser.Parser().parsestr(mssg) for mssg in messages]

# Loop over all messages and get subject+content of email
for message in messages:
    sender = str(message['From'])
    subject = str(message['subject'])
    content = str(message.get_payload())
    fileName = "%s.eml" % (subject.replace(": ", "-") ) #.replace(" ", "_")

    # Check if email has already been saved 
    if os.path.isfile(myPath + fileName):
        continue
    else:
        try:
            iNewMail = iNewMail+1
            newMailFiles.append(fileName)
            saveFile = open(myPath + fileName, "w")
            saveFile.write( "From: %s" % (sender) )
            saveFile.write( "\n")
            saveFile.write( "Subject: %s" % (subject) )
            saveFile.write( "\n")
            saveFile.write( "Content: %s" % (content) )
        finally:
            saveFile.close()

if iNewMail > 0:
    f.Cout("You have %s NEW mails:\n\t%s" % (iNewMail, [item for item in newMailFiles]) )
    f.Cout('Saving NEW mail to "%s":' % (myPath))
else:
    f.Cout("No NEW mail.")

# Before exiting save a time-stamp file to keep track of last time I checked my email
try:
    fileName = "timestamp.txt"
    f.Cout('Updating time-stamp file "%s".' % (myPath + fileName) )
    newTimeStampFile = open(myPath + fileName, "w")
    newTimeStampFile.write(str(today))
finally:
    newTimeStampFile.close()
    
# Before closing program open the new emails for the user
f.Cout('Paging NEW emails. Press "q" to read the next email.')
for mail in newMailFiles:
    myNewMail = open(myPath + mail, "r")
    pydoc.pager(myNewMail.read()) # similar to | less in shell. Press "q" to move to next email

# Once done close connection to server
f.Cout('Done. Exiting python shell.')
connection.quit()
