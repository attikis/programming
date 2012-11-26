#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : This module is a simple interface to check for new emails in the inbox of Gmail or CERN pop servers. If new emails are present they will be opened before the script exits the shell. All new emails will be written as .eml files to dedicated paths. A time-stamp text file provides information of the last check for email. When calling the module the only thing that needs to be specified is which server is to be used (cern or gmail). Just follow the prompt commands once launced.

import python_myFunctions as myFunctions

f = myFunctions.CreateObject()

if __name__ == "__main__":
    
    #f.Cout("Testing the CERN pop server")
    #f.getEmail("cern")
    #print
    #f.Cout("Testing the Gmail pop server")
    #f.getEmail("gmail")
    #print
    f.Cout("Testing the CERN imap server")
    f.getEmailImap("cern")
    print
    f.Cout("Testing the Gmail imap server")
    f.getEmailImap("gmail")
