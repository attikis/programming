#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example script of how to retrieve email from a server

'''
Usage:
./python_logFileParser.py arg1 arg2 

Description:
This script takes 3 command line arguments (arg1 = grep option, arg2 = string to grep on, arg3 = file extension),
 and it performs a simple grep of the keyword using the user-defined options.
'''

# Import modules here
import traceback
from smtplib import SMTP
from email.MIMEText import MIMEText
import python_myFunctions as myFunctions
import sys
import datetime

# Declaration here
myFunc = myFunctions.CreateObject()
smtpHost = "smtp.gmail.com"
smtpPort = 587
emailAddress = "@gmail.com"
myFunc.Cout("Please provide your login credentials for %s to continue" % (emailAddress))
#smtpUsername = raw_input("Username = ") + emailAddress
#smtpPassword = raw_input("Password = ")
smtpUsername = "alexandros.attikis@gmail.com"
smtpPassword = "xKa[99448024]aa569282piasme"
sender = smtpUsername

# Function definitions here
def sendGmail():
    # First get user input regarding email details
    myFunc.Cout("Please provide the email details:")
    recipients = raw_input("\tTo: ")
    Cc = raw_input("\tCc: ")
    Bcc = raw_input("\tBcc: ")
    subject = raw_input("\tSubject: ")
    content = raw_input("\tContent: ")
    #recipients = ["attikis@cern.ch", "alexandros.attikis@gmail.com"]
    #recipients = "attikis@cern.ch"
    #Cc = "enmeeides@hotmail.com"
    #Bcc = "alexandros.attikis@gmail.com"
    #subject = "Subject: Test-6"
    #content = "This is a python-sent email. " + str(datetime.datetime.now())

    # Define return value as 0==success,  1==failure
    retval = 1
    if not(hasattr(recipients, "__iter__")):
        recipients = [recipients]
        Cc = [Cc]
        Bcc = [Bcc]
        destination = recipients
    
    # Define text type
    text_subtype = 'plain'
    try:
        # Create message to be sent
        msg = MIMEText(content, text_subtype)
        msg['From'] = sender # Some SMTP servers will do this automatically, but not all
        msg['To']   = ", ".join(recipients)
        msg['cc']   = ", ".join(Cc)
        msg['Bcc']  = ", ".join(Bcc)
        msg['Subject'] = subject

        # Connect to host using specified port
        conn = SMTP(host=smtpHost, port=smtpPort)
        conn.set_debuglevel(True)
        try:
            if smtpUsername is not False:
                conn.ehlo()
                if smtpPort != 25:
                    conn.starttls()
                    conn.ehlo()
                if smtpUsername and smtpPassword:
                    conn.login(smtpUsername, smtpPassword)
                    myFunc.Cout("Succesfully logged on to:\n\tusername = %s\n\tpassword = %s" % (smtpUsername, myFunc.obscureString(smtpPassword)))
                else:
                    myFunc.Cout("Unsuccesfull login. False credentials provided:\n\tusername = %s\n\tpassword = %s" % (smtpUsername, myFunc.obscureString(smtpPassword)))
                    sys.exit(1)
            # Send emails
            myFunc.Cout("Sending email to %s" % (recipients) )
            conn.sendmail(sender, recipients+Cc+Bcc, msg.as_string())
            # Set return value to 0 (success)
            retval = 0
        except Exception, e:
            myFunc.Cout("Got %s %s.\n\tShowing traceback:\n%s" % (type(e), e, traceback.format_exc()))
            # Set return value to 1 (failure)
            retval = 1
        finally:
            myFunc.Cout("Closing connection.")
            conn.close()

    except Exception, e:
        myFunc.Cout("Got %s %s.\n\tShowing traceback:\n%s" % (type(e), e, traceback.format_exc()))
        # Set return value to 1 (failure)        
        retval = 1
    return retval

if __name__ == "__main__":
    sendGmail()
