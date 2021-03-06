#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example script of how to retrieve email from a server

'''
Usage:
./python_cernMail.py

Description:
This script is a simple interface to send emails using the gmail SMTP server. Just follow the prompt commands once launced.

Example:
[attikis:python]> ./python_cernMail.py 
+ Please provide your login credentials for @gmail.com to continue
Password = 
++ Please provide the email details:
	To: someOne@cern.ch,  someOne@hotmail.com, someOne@gmail.com
	Cc: someOneElse@cern.ch,  someOneElse@hotmail.com, someOneElse@gmail.com
	Bcc (self excluded): someSecretRecipient@cern.ch, someOtherSecretRecipient@cern.ch, 
	Subject: Test-1
	Content: This is an email sent from a python script.
+++ Attempting to connect to:
	host = cernmx.cern.ch
	port = 587

...
'''

# Import modules here
import traceback
from smtplib import SMTP
from email.MIMEText import MIMEText
import python_myFunctions as myFunctions
import sys
import datetime
import getpass 

# Declaration here
myFunc = myFunctions.CreateObject()
smtpHost = "smtp.cern.ch"
smtpPort = 587 #or 25
emailAddress = "@cern.ch"
myFunc.Cout("Please provide your login credentials for %s to continue" % (emailAddress))
smtpUsername = "attikis@cern.ch"
smtpPassword = getpass.getpass("Password = ")
sender = smtpUsername

# Function definitions here
def sendCernMail():
    # First get user input regarding email details
    myFunc.Cout("Please provide the email details:")
    recipients = raw_input("\tTo: ")
    Cc = raw_input("\tCc: ")
    Bcc = raw_input("\tBcc (self excluded): ")
    subject = raw_input("\tSubject: ")
    content = raw_input("\tContent: ")

    # Define return value as 0==success,  1==failure
    retval = 1
    # Take care of recipient lists
    if not(hasattr(recipients, "__iter__")):
        recipients = [recipients]
    if not(hasattr(Cc, "__iter__")):
        Cc = [Cc]
    if not(hasattr(Bcc, "__iter__")):
        Bcc = [Bcc]
        Bcc.append(smtpUsername)
    
    try:
        # Assign message details
        text_subtype = 'plain'
        msg = MIMEText(content, text_subtype)
        msg['From'] = sender # Some SMTP servers will do this automatically, but not all
        msg['To']   = ", ".join(recipients)
        msg['cc']   = ", ".join(Cc)
        msg['Bcc']  = ", ".join(Bcc)
        msg['Subject'] = subject

        # Connect to host using specified port
        myFunc.Cout("Attempting to connect to:\n\thost = %s\n\tport = %s" % (smtpHost, smtpPort))
        connection = SMTP(host=smtpHost, port=smtpPort)
        connection.set_debuglevel(True)
        try:
            if smtpUsername is not False:
                connection.ehlo()
                if smtpPort != 25:
                    connection.starttls()
                    connection.ehlo()
                if smtpUsername and smtpPassword:
                    connection.login(smtpUsername, smtpPassword)
                    myFunc.Cout("Succesfully logged on to:\n\tusername = %s\n\tpassword = %s" % (smtpUsername, myFunc.obscureString(smtpPassword)))
                else:
                    myFunc.Cout("Unsuccesfull login. False credentials provided:\n\tusername = %s\n\tpassword = %s" % (smtpUsername, myFunc.obscureString(smtpPassword)))
                    print __doc__
                    sys.exit(1)
            # Send emails
            myFunc.Cout("Sending email to %s" % (recipients) )
            connection.sendmail(sender, recipients+Cc+Bcc, msg.as_string())
            # Set return value to 0 (success)
            retval = 0
        except Exception, e:
            myFunc.Cout("Got %s %s.\n\tShowing traceback:\n%s" % (type(e), e, traceback.format_exc()))
            # Set return value to 1 (failure)
            retval = 1
            print __doc__
        finally:
            myFunc.Cout("Closing connection.")
            connection.close()

    except Exception, e:
        myFunc.Cout("Got %s %s.\n\tShowing traceback:\n%s" % (type(e), e, traceback.format_exc()))
        # Set return value to 1 (failure)        
        retval = 1
        print __doc__

    return retval

# Main function here
if __name__ == "__main__":
    sendCernMail()
