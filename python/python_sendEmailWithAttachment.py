#!/usr/bin/env python
# Permissions : chmod +x fileName.py

'''
Usage:
./python_sendEmailAttachment.py

Description:
This script is a simple interface to sending emails with attachments, using the gmail or CERN SMTP servers. Just follow the prompt commands once launced.

Example:
[attikis:python]> ./python_sendEmailAttachment.py
'''

import python_myFunctions as myFunctions

f = myFunctions.CreateObject()

def sendEmail(server):
    ''' sendEmail(host_server):
    This module is a simple interface to send emails using the gmail or cern SMTP servers. When calling the module the only thing that needs to be specified is 
    which server is to be used (cern or gmail). Just follow the prompt commands once launched. The "smtplib" is a low-level package interface for the Simple Mail
    Transfer Protocol (SMTP) protocol. The "email" package assists with parsing (analyzing a sentence into its parts and describe their syntactic roles) and
    generating emails.
    '''

    # Import modules here
    import traceback
    import email
    from smtplib import SMTP
    from email.MIMEText import MIMEText
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEBase import MIMEBase
    from email import encoders
    import mimetypes
    import sys
    import datetime
    import getpass 
    
    # Define SMTP port to use and decide which of the two servers to use
    smtpPort = 587 #or 25
    if server == "cern":
        smtpHost = "smtp.cern.ch"
        emailAddress = "@cern.ch"
        smtpUsername = "attikis@cern.ch"
    elif server == "gmail":
        smtpHost = "smtp.gmail.com"
        emailAddress = "@gmail.com"
        smtpUsername = "alexandros.attikis@gmail.com"
    else:
        f.Cout('ERROR! The server argument %s is invalid. Please select between "cern" and "gmail". Exiting python shell.')
        print __doc__
        sys.exit(1)
        
    # Get SMTP authorisation details
    f.Cout("Please provide your login credentials for %s to continue:" % (smtpUsername) )
    sender = smtpUsername
    smtpPassword = getpass.getpass("\tPassword = ")

    # Connect to host using specified port
    f.Cout("Attempting to connect to:\n\thost = %s\n\tport = %s" % (smtpHost, smtpPort))
    connection = SMTP(host=smtpHost, port=smtpPort)
    connection.set_debuglevel(False) #True
    if smtpUsername is not False:
        connection.ehlo()
        if smtpPort != 25:
            connection.starttls()
            connection.ehlo()
            if smtpUsername and smtpPassword:
                connection.login(smtpUsername, smtpPassword)
                f.Cout("Succesfully logged on to:\n\tusername = %s\n\tpassword = %s" % (smtpUsername, f.obscureString(smtpPassword)))
            else:
                f.Cout("Unsuccesfull login. False credentials provided:\n\tusername = %s\n\tpassword = %s" % (smtpUsername, f.obscureString(smtpPassword)))
                print __doc__
                sys.exit(1)

    # Get user input regarding email details
    f.Cout("Please provide the email details:")
    recipients = raw_input("\tTo: ")
    Cc = raw_input("\tCc: ")
    Bcc = raw_input("\tBcc (self excluded): ")
    subject = raw_input("\tSubject: ")
    content = raw_input("\tContent: ")
    attachment = raw_input("\tAttachment: ")
    if attachment == "":
        f.Cout("Nothing to attach.")
        bAttach = False
    else:
        f.Cout("Attachment file:\n\t%s" % (attachment) )
        bAttach = True
    
    # Define return value as success == 0,  failure == 1
    returnValue = 1
    # Take care of recipient lists
    if not(hasattr(recipients, "__iter__")):
        recipients = [recipients]
    if not(hasattr(Cc, "__iter__")):
        Cc = [Cc]
    if not(hasattr(Bcc, "__iter__")):
        Bcc = [Bcc]
        Bcc.append(smtpUsername)
            
    # Define message details, including attachments
    try:
        if bAttach == False:
            text_subtype = 'plain'
            mainMsg = MIMEText(content, text_subtype)
        else:
            mainMsg = MIMEMultipart()
            # Guess the type of a file based on its filename or URL, given by url. 
            ctype, encoding = mimetypes.guess_type(attachment)
            print "ctype, encoding = %s, %s" % (ctype, encoding)
            maintype, subtype = ctype.split("/", 1)
            print "maintype, subtype = %s, %s" % (maintype, subtype)

        # The following do not depend on attachment
        mainMsg['From'] = sender # Some SMTP servers will do this automatically, but not all
        mainMsg['To']   = ", ".join(recipients)
        mainMsg['cc']   = ", ".join(Cc)
        mainMsg['Bcc']  = ", ".join(Bcc)
        mainMsg['Subject'] = subject
        
       # Send emails body and attachments
        f.Cout("Sending email to %s" % (recipients) )
        try:
            if bAttach:
                mainMsg.attach(MIMEText(content))
                fp = open(attachment, "rb") # open attachment in read/binary mode
                subMsg = MIMEBase(maintype, subtype)
                subMsg.set_payload(fp.read())
                fp.close()
                encoders.encode_base64(subMsg)
                subMsg.add_header("Content-Disposition", "attachment", filename=attachment)
                mainMsg.attach(subMsg)
            # Connect to server and send complete email
            connection.sendmail( sender, recipients+Cc+Bcc, mainMsg.as_string() )
            returnValue = 0 # (success)
        except Exception, e:
            f.Cout("Got %s %s.\n\tShowing traceback:\n%s" % (type(e), e, traceback.format_exc()))
            returnValue = 1 # (failure)
            print __doc__
        finally:
            f.Cout("Closing connection.")
            connection.close()
            
    except Exception, e:
        f.Cout("Got %s %s.\n\tShowing traceback:\n%s" % (type(e), e, traceback.format_exc()))
        returnValue = 1 # (failure)
        print __doc__
        
    return returnValue


if __name__ == "__main__":
    f.Cout("Testing the CERN server")
    sendEmail("cern")
    
