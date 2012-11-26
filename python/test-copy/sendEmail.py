#!/usr/bin/env python
# Permissions : chmod +x fileName.py

'''
Usage:
./python_email.py

Description:
This script is a simple interface to send emails using the gmail or CERN SMTP servers. Just follow the prompt commands once launced.

Example:
[attikis:python]> ./python_email.py 
+ Please provide your login credentials for @gmail.com to continue
Password = 
++ Please provide the email details:
	To: someOne@cern.ch,  someOne@hotmail.com, someOne@gmail.com
	Cc: someOneElse@cern.ch,  someOneElse@hotmail.com, someOneElse@gmail.com
	Bcc (self excluded): someSecretRecipient@cern.ch, someOtherSecretRecipient@cern.ch, 
	Subject: Test-1
	Content: This is an email sent from a python script.
+++ Attempting to connect to:
	host = smtp.gmail.com
	port = 587

...
'''

import python_myFunctions as myFunctions

f = myFunctions.CreateObject()

if __name__ == "__main__":
    
    f.Cout("Testing the CERN server")
    f.sendEmail("cern")

    f.Cout("Testing the Gmail server")
    f.sendEmail("gmail")
