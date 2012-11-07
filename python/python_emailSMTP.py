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
import re

# Declaration here
myFunc = myFunctions.CreateObject()
smtpHost = "smtp.gmail.com"
smtpPort = 587
#smtpUsername = raw_input("Username = ") + "@gmail.com"
#smtpPassword = raw_input("Password = ")
smtpUsername = "alexandros.attikis@gmail.com"
smtpPassword = "xKa[99448024]aa569282piasme"
sender = smtpUsername

# Function definitions here
def sendEmail(to, subject, content, addBCC):
    myFunc.Cout('Preparing to send email:\n\tfrom = %s\n\tto = %s' % (sender, receiver))
    retval = 1
    if not(hasattr(to, "__iter__")):
        to = [to]
    destination = to

    text_subtype = 'plain'
    try:
        # Create message to be sent
        msg = MIMEText(content, text_subtype)
        msg['Subject'] = subject
        msg['From'] = sender # Some SMTP servers will do this automatically, but not all
        myFunc.Cout("Preparing email with following details:\n\tsubject = %s \n\tcontext = %s" % (msg["Subject"], content))

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
            if addBCC:
                myFunc.Cout("Sending email to %s. Adding %s in BCC." % (receiver, sender) )
                conn.sendmail(receiver, destination, msg.as_string())
                conn.sendmail(sender  , destination, msg.as_string())
            else:
                myFunc.Cout("Sending email to %s. BCC is disabled." % (receiver) )
                conn.sendmail(receiver, destination, msg.as_string())
            retval = 0
        except Exception, e:
            myFunc.Cout("Got %s %s.\n\tShowing traceback:\n%s" % (type(e), e, traceback.format_exc()))
            retval = 1
        finally:
            myFunc.Cout("Closing connection.")
            conn.close()

    except Exception, e:
        myFunc.Cout("Got %s %s.\n\tShowing traceback:\n%s" % (type(e), e, traceback.format_exc()))
        retval = 1
    return retval

if __name__ == "__main__":

    # First check that all script arguments have been passed 
    if len(sys.argv) == 3:
        receiver = sys.argv[1]
        addBCC = sys.argv[2]
    elif len(sys.argv) == 2:
        receiver = sys.argv[1]
        addBCC = True
    else:
        myFunc.Cout("ERROR! Script execution not possible due to missing input arguments. Please refer to the module's docstrings. Exiting python shell.")
        print __doc__
        sys.exit(1)

    # Send email to destination
    myFunc.Cout("Running script with user-defined arguments:\n\treceiver = %s\n\tBBC = %s" % (receiver, addBCC))
    sendEmail(receiver, "Python test", "Sent from a python script!", addBCC)
