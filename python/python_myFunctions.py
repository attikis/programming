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
        self.OutCounter = 0
        self.InCounter = 0

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
        ''' Cout(self, text):
        A function to cout, keeping track of number of lines.
        '''
        self.OutCounter = self.OutCounter+1
        print "Out[%s] %s" % (self.OutCounter, text)
        return 0

    def Cin(self, text):
        ''' Cin(self, text):
        A function to cin, keeping track of number of lines.
        '''
        self.InCounter = self.InCounter+1
        myRawInput = raw_input("In[%s] %s: " % (self.InCounter, text) )
        return myRawInput
    
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
    
    def sendEmailNoAttachment(self, server):
        ''' sendEmail(host_server):
        This module is a simple interface to send emails using the gmail or cern SMTP servers. When calling the module the only thing that needs to be specified is 
        which server is to be used (cern or gmail). Just follow the prompt commands once launched. The "smtplib" is a low-level package interface for the Simple Mail
        Transfer Protocol (SMTP) protocol. The "email" package assists with parsing (analyzing a sentence into its parts and describe their syntactic roles) and
        generating emails.
        '''

        # Import modules here
        import traceback
        from smtplib import SMTP
        from email.MIMEText import MIMEText
        import sys
        import datetime
        import getpass 
        
        # Declaration here
        myFunc = CreateObject()
        # Decide which of the two servers to use
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


    def getEmail(self, server):
        ''' getEmail(host_server):
        This module is a simple interface to check for new emails in the inbox of Gmail or CERN pop servers. In a nutshell the module retrieves all of the email that is stored on the specified server (Gmail or CERN) and wrties it to a set of files on disk. If new emails are present they will be opened before the script exits the shell. All new emails will be written as .eml files to dedicated paths. A time-stamp text file provides information of the last check for email. When calling the module the only thing that needs to be specified is which server is to be used (cern or gmail). Just follow the prompt commands once launced. Only thing the script does not do is to delete each email from the server after retrieving it. This is however possible by calling the connection.dele(i) after the connection.retr(i) command.
        '''
        # Import modules here
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
        self.Cout("Current date and time (yyyy:mm:dd hh:mm:ss):\n\t%s" % (today))
        self.Cout("Last inbox check was (yyyy:mm:dd hh:mm:ss):\n\t%s" % (lastCheckTime) )
        self.Cout("Time elapsed since last check:\n\t%s days, %s hours, %s minutes, %s seconds ago" % (days, hours, minutes, seconds) )

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
            self.Cout('ERROR! The server argument %s is invalid. Please select between "cern" and "gmail". Exiting python shell.')
            print __doc__
            sys.exit(1)

        # Prompt user to provide his login password
        self.Cout("Please provide your login password for %s to continue:" % (popUsername))
        popPassword = getpass.getpass("\tPassword = ")
    
        # Connect to host server using login credentials
        self.Cout("Attempting to connect to:\n\thost = %s." % (popHost))
        connection = poplib.POP3_SSL(popHost)
        connection.user(popUsername)
        connection.pass_(popPassword)
        self.Cout(connection.getwelcome())

        # Get number of messages and mailbox status: Result is tuple of 2 ints (message count, mailbox size)
        numMessages = len(connection.list()[1])
        messageCount = connection.stat()[0] 
        mailboxSize = connection.stat()[1]
        if messageCount > 0:
            self.Cout("Your inbox has %s messages in total (%s Mbytes)." % (numMessages, mailboxSize/1000000.0) )
        else:
            self.Cout("You have no mail. Exiting python shell.")
            sys.exit(1)
        
        # Get messages from server in the form of a list ([ ])
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
            fileName = "%s.eml" % (subject.replace(": ", "-").replace("/", "-") ) #.replace(" ", "_")
            
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
            self.Cout("You have %s NEW mails:\n\t%s" % (iNewMail, [item for item in newMailFiles]) )
            self.Cout('Saving NEW mail to "%s":' % (myPath))
        else:
            self.Cout("No NEW mail.")

        # Before exiting save a time-stamp file to keep track of last time I checked my email
        try:
            fileName = "timestamp.txt"
            self.Cout('Updating time-stamp file "%s".' % (myPath + fileName) )
            newTimeStampFile = open(myPath + fileName, "w")
            newTimeStampFile.write(str(today))
        finally:
            newTimeStampFile.close()
    
        # Before closing program ask user if he wants to open the new emails for the user
        openMail = self.Cin('To open NEW mail press "y"')
        if openMail == "y":
            self.Cout('Paging NEW emails. Press "q" to read the next email.')
            for mail in newMailFiles:
                myNewMail = open(myPath + mail, "r")
                pydoc.pager(myNewMail.read()) # similar to | less in shell. Press "q" to move to next email
        self.Cout('Done. Exiting python shell.')
        connection.quit()


    def getEmailImap(self, server):
        ''' getEmail(host_server):
        This module is a simple interface to check for new emails in the inbox of Gmail or CERN imap servers. 
        This is a simple example of how to use the IMAP protocol to receive emails. As I understand, the IMAP protocol is more involved in the python libraries 
        than the POP3 analogue, with more complicated/obscure modules. It does however offer a mean of accessing unread email, unlike the POP3 protocol for which I had to 
        create a time-stamp support to know when it was the last time I checked my inbox. Nevertheless, at present I prefer POP3.
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
            self.Cout('ERROR! The server argument %s is invalid. Please select between "cern" and "gmail". Exiting python shell.')
            print __doc__
            sys.exit(1)
            
        # Prompt user to provide his login password
        self.Cout("Please provide your login password for %s to continue:" % (imapUsername))
        imapPassword = getpass.getpass("\tPassword = ")

        # Connect to IMAP host server over SSL using login credentials
        self.Cout("Attempting to connect to:\n\thost = %s." % (imapHost))
        connection = imaplib.IMAP4_SSL(imapHost)
        connection.login(imapUsername, imapPassword)
        self.Cout("Connecting to INBOX.")
        print connection.select("INBOX", readonly=True) # connect to inbox.
        self.Cout(connection.welcome)

        # Search messages on server "INBOX" [search(self, charset, *criteria)] and get total number of messages in mailbox (both seen and unseen)
        AllMail = connection.search(None, "ALL")[1][0].split()  # returns a nice list of messages
        UnseenMail = connection.search(None, "UNSEEN")[1][0].split()  # returns a nice list of messages
        numAllMail = len(AllMail)
        numUnseenMail = len(UnseenMail)
        self.Cout( "You have %s messages (%s NEW) in your inbox." % (numAllMail, numUnseenMail) )

        # Loop over all messages and write them down to files
        self.Cout('Saving NEW mail to "%s":' % (myPath))
        for mailId in UnseenMail:
            try:
                fileName = "%s.eml" % (mailId)
                newMailFiles.append(fileName)
                saveFile = open(myPath + fileName, "w")
                mailBody = connection.fetch(mailId, '(RFC822)')[1][0][1]
                saveFile.write(mailBody)
            finally:
                saveFile.close()
        self.Cout("\t%s" % ([item for item in newMailFiles]) )

        # Before closing program ask user if he wants to open the new emails for the user
        openMail = self.Cin('To open NEW mail press "y"')
        if openMail == "y":
            self.Cout('Paging NEW emails. Press "q" to read the next email.')
            for mail in newMailFiles:
                myNewMail = open(myPath + mail, "r")
                pydoc.pager(myNewMail.read()) # similar to | less in shell. Press "q" to move to next email
        self.Cout('Done. Exiting python shell.')
        connection.logout()


    def sendEmail(self, server):
        ''' sendEmail(host_server):
        This module is a simple interface to send emails (with attachments) using the gmail or cern SMTP servers. When calling the module the only thing that needs 
        to be specified is which server is to be used (cern or gmail). Just follow the prompt commands once launched. The "smtplib" is a low-level package interface 
        for the Simple Mail Transfer Protocol (SMTP) protocol. The "email" package assists with parsing (analyzing a sentence into its parts and describe their 
        syntactic roles) and  generating emails.
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
            self.Cout('ERROR! The server argument %s is invalid. Please select between "cern" and "gmail". Exiting python shell.')
            print __doc__
            sys.exit(1)
        
        # Get SMTP authorisation details
        self.Cout("Please provide your login credentials for %s to continue:" % (smtpUsername) )
        sender = smtpUsername
        smtpPassword = getpass.getpass("\tPassword = ")

        # Connect to host using specified port
        self.Cout("Attempting to connect to:\n\thost = %s\n\tport = %s" % (smtpHost, smtpPort))
        connection = SMTP(host=smtpHost, port=smtpPort)
        connection.set_debuglevel(False) #True
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

        # Get user input regarding email details
        self.Cout("Please provide the email details:")
        recipients = raw_input("\tTo: ")
        Cc = raw_input("\tCc: ")
        Bcc = raw_input("\tBcc (self excluded): ")
        subject = raw_input("\tSubject: ")
        content = raw_input("\tContent: ")
        attachment = raw_input("\tAttachment: ")
        if attachment == "":
            self.Cout("Nothing to attach.")
            bAttach = False
        else:
            self.Cout("Attachment file:\n\t%s" % (attachment) )
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
            self.Cout("Sending email to %s" % (recipients) )
            try:
                if bAttach:
                    mainMsg.attach(subMsg)
                    fp = open(attachment, "rb") # open attachment in read/binary mode
                    subMsg = MIMEBase(maintype, subtype)
                    subMsg.set_payload(fp.read())
                    fp.close()
                    encoders.encode_base64(subMsg)
                    subMsg.add_header("Content-Disposition", "attachment", filename=attachment)
                    mainMsg.attach(MIMEText(content))
                # Connect to server and send complete email
                connection.sendmail( sender, recipients+Cc+Bcc, mainMsg.as_string() )
                returnValue = 0 # (success)
            except Exception, e:
                self.Cout("Got %s %s.\n\tShowing traceback:\n%s" % (type(e), e, traceback.format_exc()))
                returnValue = 1 # (failure)
                print __doc__
            finally:
                self.Cout("Closing connection.")
                connection.close()
        
        except Exception, e:
            self.Cout("Got %s %s.\n\tShowing traceback:\n%s" % (type(e), e, traceback.format_exc()))
            returnValue = 1 # (failure)
            print __doc__
            
        return returnValue
