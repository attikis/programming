#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : Strictly an input module to be used in other executable scripts
# Definition  : My very first generic functions class, to be used for simple coding.
 
''' 
Usage:
import python_myFunctions as myFs

Description:
In this python module I define some generic functions that can be used in many executable scripts. 
The list of functions defined here will grow significantly over time, at which stage I should perhaps
consider its further break-down to more classes and functions.
''' 

class CreateObject:
    
    def __init__(self):
        self.counter = 0

    def DisplayMatchObject(self, match):
        ''' DisplayMatchObject(self, match):
        A function to display match objects
        '''
        if match is None:
            return None
        print "match.group() = %r, match.groups() = %r>" % (match.group(), match.groups())
    # Loop over all groups and print them
        for iMatch in range (0, len(match.groups())+1):
            print 'group(%r) = %r' % (iMatch, match.group(iMatch))
            print 'groupdict(%r) = ' % (match.groupdict(iMatch))
        return 0
        
    def Cout(self, text):
        ''' sortedDictKeys(dict):
        A function to cout each time with an extra "+" symbol
        '''
        self.counter = self.counter+1
        print "%s %s" % ("+"*self.counter, text)        
        return 0
    
    def sortedDictKeys(self, dict):
        ''' sortedDictKeys(dict):
        A function to sort keys of a dictionary. A mapping (such as a "dictionary) has NO order, thus it cannot be sorted. Still, its keys can be extracted as a list, which can then be sorted.
        '''
        keys = dict.keys()
        keys.sort()
        return [key for key in keys]

    def sortedDictValues(self, dict):
        ''' sortedDictKeys(dict):
        A function to sort values of a dictionary, according to sorted keys. A mapping (such as a "dictionary) has NO order, thus it cannot be sorted. Still, its keys can be extracted as a list, which can then be sorted.
        '''
        
        keys = dict.keys()
        keys.sort()
        return [dict[key] for key in keys]
    
    def obscureString(self, inputString):
        ''' obscureString(dict):
        A function to obscure a string by replacing all ascii printable characters with asterisks (*). This is mainly used in cases when you want to print a password without revealing its meaning, but just the number of characters.
        '''
        import string

        outputString = inputString
        # Create a characters list
        CharactersList = []
        
        # Fill the list with all printable ascii characters
        for item in string.printable:
            CharactersList.append(item)
        # Now loop over all readable characters and replace those in the input string with an asterisk
        for char in CharactersList:
            outputString = outputString.replace(char, "*")
        # Return the asterisk-obscured string
        return outputString
    
    def sendEmail(self, server):
        ''' sendEmail(host_server):
        This module is a simple interface to send emails using the gmail or cern SMTP servers. When calling the module the only thing that needs to be specified is 
        which server is to be used (cern or gmail). Just follow the prompt commands once launced.
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
        if server == "cern":
            smtpHost = "smtp.cern.ch"
            emailAddress = "@cern.ch"
            smtpUsername = "attikis@cern.ch"
        elif server == "gmail":
            smtpHost = "smtp.gmail.com"
            emailAddress = "@gmail.com"
            smtpUsername = "alexandros.attikis@gmail.com"
        else:
            self.Cout('ERROR! The server argument %s is invalid. Please select between "cern" and "gmail". Exiting python shell.')
            print __doc__
            sys.exit(1)
        smtpPort = 587 #or 25

        self.Cout("Please provide your login credentials for %s to continue:" % (smtpUsername))
        smtpPassword = getpass.getpass("\tPassword = ")
        sender = smtpUsername

        # First get user input regarding email details
        self.Cout("Please provide the email details:")
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
            self.Cout("Attempting to connect to:\n\thost = %s\n\tport = %s" % (smtpHost, smtpPort))
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
                        self.Cout("Succesfully logged on to:\n\tusername = %s\n\tpassword = %s" % (smtpUsername, self.obscureString(smtpPassword)))
                    else:
                        self.Cout("Unsuccesfull login. False credentials provided:\n\tusername = %s\n\tpassword = %s" % (smtpUsername, self.obscureString(smtpPassword)))
                        print __doc__
                        sys.exit(1)
                # Send emails
                self.Cout("Sending email to %s" % (recipients) )
                connection.sendmail(sender, recipients+Cc+Bcc, msg.as_string())
                # Set return value to 0 (success)
                retval = 0
            except Exception, e:
                self.Cout("Got %s %s.\n\tShowing traceback:\n%s" % (type(e), e, traceback.format_exc()))
                # Set return value to 1 (failure)
                retval = 1
                print __doc__
            finally:
                self.Cout("Closing connection.")
                connection.close()
                
        except Exception, e:
            self.Cout("Got %s %s.\n\tShowing traceback:\n%s" % (type(e), e, traceback.format_exc()))
            # Set return value to 1 (failure)        
            retval = 1
            print __doc__
            
        return retval


    
