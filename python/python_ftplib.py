#!/usr/bin/env python
# Permissions : chmod +x fileName.py

'''
Usage:
./python_ftplib.py 
or
python python_ftplib.py -a remote_host_address -r remote_file -l local_file -u username -p password 

Description:
This scripts connects to an FTP client application to retrieve a remote_file and save it as a local_file.

Help:
[attikis:python]> python python_ftplib.py --help
Usage: python_ftplib.py [options]

Usage:
[attikis:python]> python python_ftplib.py -a ftp.mozilla.org -r README -l README.txt
Out[1] Creating FTP client class with remote host address:
	ftp.mozilla.org
Out[2] Attempting anonymous login.
Out[3] Retrieving data in binary mode. Copying:
	remote file = README
to
	local file = README.txt
Out[4] Closing local file README.txt.
Out[5] Closing FTP connection with remote host address:
	ftp.mozilla.org.
(see ftp://ftp.mozilla.org/pub/)

Options:
  -h, --help            show this help message and exit
  -a REMOTE FTP HOST, --remote_host_address=REMOTE FTP HOST
                        REMOTE FTP HOST.
  -r REMOTE FILE NAME, --remote_file=REMOTE FILE NAME
                        REMOTE FILE NAME to download.
  -l LOCAL FILE NAME, --local_file=LOCAL FILE NAME
                        LOCAL FILE NAME to save the remote file to
  -u USERNAME, --username=USERNAME
                        USERNAME for ftp server
  -p PASSWORD, --password=PASSWORD
                        PASSWORD for ftp server
'''

# All required modules here
import python_myFunctions as myFunctions
from ftplib import FTP
import sys
from optparse import OptionParser 

# Object and variable declarations here
mf = myFunctions.CreateObject()

parser = OptionParser()
parser.add_option("-a", "--remote_host_address", dest = "remote_host_address", help = "REMOTE FTP HOST.", metavar = "REMOTE FTP HOST")

parser.add_option("-r", "--remote_file", dest = "remote_file", help = "REMOTE FILE NAME to download.", metavar = "REMOTE FILE NAME")

parser.add_option("-l", "--local_file", dest = "local_file", help = "LOCAL FILE NAME to save the remote file to", metavar = "LOCAL FILE NAME")

parser.add_option("-u", "--username", dest = "username", help = "USERNAME for ftp server", metavar = "USERNAME") 

parser.add_option("-p", "--password", dest = "password", help = "PASSWORD for ftp server", metavar = "PASSWORD")

(options, args) = parser.parse_args()

if not (options.remote_file and options.local_file and options.remote_host_address):
    print __doc__
    parser.error("REMOTE HOST, LOCAL FILE NAME, and REMOTE FILE NAME are mandatory")

if options.username and not options.password:
    print __doc__
    parser.error("PASSWORD is mandatory if USERNAME is present")

mf.StopWatchStart()
        
# Define the FTP server object; pass the desired FTP address to the constructor
#mf.Cout("Creating FTP client class with remote host address:\n\t%s" % (options.remote_host_address))
#ftp = FTP(options.remote_host_address) # also works
mf.Cout("Creating FTP client class")
ftp = FTP()
# Connect to FTP server
mf.Cout("Connectiong to remote host address:\n\t%s" % (options.remote_host_address))
ftp.connect(options.remote_host_address)

# Now login onto the FTP server
if options.username:
    try:
        mf.Cout("Attempting login with:\n\tusername = %s\n\tpassword = %s" % (options.username, mf.obscureString(options.password)))
        ftp.login(options.username, options.password)
    except ftplib.error_perm, e:
        mf.Cout("Login failed:\n\t%s" % (e))
        print __doc__
        sys.exit(1)
else:
    try:
        mf.Cout("Attempting anonymous login.")
        ftp.login()
    except ftplib.error_perm, e:
        mf.Cout("Anonymous login failed:\n\t%s" % (e))
        print __doc__
        sys.exit(1)

try:
    # Create a file object to store the data from the file on the FTP server. 
    mf.Cout("Retrieving data in binary mode. Copying:\n\tremote file = %s\nto\n\tlocal file = %s" % (options.remote_file, options.local_file))
    local_file = open(options.local_file, "wb") #write/binary mode
    # Retrieve the data in binary mode from the FTP server and write on file object. A new port is created for you.
    ftp.retrbinary("RETR %s" % (options.remote_file), local_file.write)
finally:
    mf.Cout("Closing local file %s." % (options.local_file))
    local_file.close()
    mf.Cout("Closing FTP connection with remote host address:\n\t%s." % (options.remote_host_address))
    ftp.close()

mf.StopWatchStop()
