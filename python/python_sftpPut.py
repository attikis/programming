#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
The Secure SHell (SSH) protocol allows one to securely connect to a remote server, execute shell commands, transfer files and forward ports in both directions (local<->remote).
It is incredibly powerful and widely used. Using the ssh command in parallel with the full power of python can be extremely useful. The dedicated library is called "paramkio". 
In this example we present how to put (copy) local files to an SSH server.

Help:
Usage: python_sftpPut.py [options]

Options:
  -h, --help            show this help message and exit
  -a ADDRESS OF REMOTE HOST, --remote_host_address=ADDRESS OF REMOTE HOST
                        ADDRESS OF REMOTE HOST
  -u AUTHENTICATION USERNAME, --username=AUTHENTICATION USERNAME
                        AUTHENTICATION USERNAME

Example:
[attikis:python]> python python_sftpPut.py -a lxplus5.cern.ch -u attikis
Out[1] Connecting to:
	attikis@lxplus5.cern.ch
Out[2] Checking if lxplus5.cern.ch is active:
	True
Out[3] Listing all files in remote directory:
	/afs/cern.ch/user/a/attikis/scratch0/
Out[4] Remote directory file-list:
	['CMSSW_4_2_8_patch2', 'Top2HPlus', 'Top2HPlus.old', 'Python_Unix_and_Linux_admin.pdf', 'tmp.txt', 'CMSSW_4_4_4']
Out[5] Copying file:
	/Users/administrator/my_work/programming/python/doc/Python_Unix_and_Linux_admin.pdf
to:
	/afs/cern.ch/user/a/attikis/scratch0/Python_Unix_and_Linux_admin.pdf
Out[6] Found file Python_Unix_and_Linux_admin.pdf on remote host.
Out[7] File /Users/administrator/my_work/programming/python/doc/Python_Unix_and_Linux_admin.pdf succescully copied to /afs/cern.ch/user/a/attikis/scratch0/Python_Unix_and_Linux_admin.pdf on attikis@lxplus5.cern.ch
Out[8] Closing connection.
Out[9] Logfile sftpPut.log:
	
DEB [20121120-18:17:40.939] thr=1   paramiko.transport: starting thread (client mode): 0x74f2d50L
INF [20121120-18:17:41.064] thr=1   paramiko.transport: Connected (version 2.0, client OpenSSH_4.3)
DEB [20121120-18:17:41.188] thr=1   paramiko.transport: kex algos:['diffie-hellman-group-exchange-sha1', 'diffie-hellman-group14-sha1', 'diffie-hellman-group1-sha1'] server key:['ssh-rsa', 'ssh-dss'] client encrypt:['aes128-ctr', 'aes192-ctr', 'aes256-ctr', 'arcfour256', 'arcfour128', 'aes128-cbc', '3des-cbc', 'blowfish-cbc', 'cast128-cbc', 'aes192-cbc', 'aes256-cbc', 'arcfour', 'rijndael-cbc@lysator.liu.se'] server encrypt:['aes128-ctr', 'aes192-ctr', 'aes256-ctr', 'arcfour256', 'arcfour128', 'aes128-cbc', '3des-cbc', 'blowfish-cbc', 'cast128-cbc', 'aes192-cbc', 'aes256-cbc', 'arcfour', 'rijndael-cbc@lysator.liu.se'] client mac:['hmac-md5', 'hmac-sha1', 'hmac-ripemd160', 'hmac-ripemd160@openssh.com', 'hmac-sha1-96', 'hmac-md5-96'] server mac:['hmac-md5', 'hmac-sha1', 'hmac-ripemd160', 'hmac-ripemd160@openssh.com', 'hmac-sha1-96', 'hmac-md5-96'] client compress:['none', 'zlib@openssh.com'] server compress:['none', 'zlib@openssh.com'] client lang:[''] server lang:[''] kex follows?False
DEB [20121120-18:17:41.188] thr=1   paramiko.transport: Ciphers agreed: local=aes128-ctr, remote=aes128-ctr
DEB [20121120-18:17:41.188] thr=1   paramiko.transport: using kex diffie-hellman-group1-sha1; server key type ssh-rsa; cipher: local aes128-ctr, remote aes128-ctr; mac: local hmac-sha1, remote hmac-sha1; compression: local none, remote none
DEB [20121120-18:17:41.393] thr=1   paramiko.transport: Switch to new keys ...
DEB [20121120-18:17:41.412] thr=2   paramiko.transport: Attempting password auth...
DEB [20121120-18:17:41.723] thr=1   paramiko.transport: userauth is OK
INF [20121120-18:17:42.677] thr=1   paramiko.transport: Authentication (password) successful!
DEB [20121120-18:17:42.693] thr=2   paramiko.transport: [chan 1] Max packet in: 34816 bytes
DEB [20121120-18:17:43.804] thr=1   paramiko.transport: [chan 1] Max packet out: 32768 bytes
INF [20121120-18:17:43.805] thr=1   paramiko.transport: Secsh channel 1 opened.
DEB [20121120-18:17:43.955] thr=1   paramiko.transport: [chan 1] Sesch channel 1 request ok
INF [20121120-18:17:46.262] thr=2   paramiko.transport.sftp: [chan 1] Opened sftp connection (server version 3)
DEB [20121120-18:17:46.262] thr=2   paramiko.transport.sftp: [chan 1] listdir('/afs/cern.ch/user/a/attikis/scratch0/')
DEB [20121120-18:17:47.186] thr=2   paramiko.transport.sftp: [chan 1] open('/afs/cern.ch/user/a/attikis/scratch0/Python_Unix_and_Linux_admin.pdf', 'wb')
DEB [20121120-18:17:47.357] thr=2   paramiko.transport.sftp: [chan 1] open('/afs/cern.ch/user/a/attikis/scratch0/Python_Unix_and_Linux_admin.pdf', 'wb') -> 00000000
DEB [20121120-18:18:37.678] thr=2   paramiko.transport.sftp: [chan 1] close(00000000)
DEB [20121120-18:18:39.217] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Python_Unix_and_Linux_admin.pdf')
DEB [20121120-18:18:39.367] thr=2   paramiko.transport.sftp: [chan 1] listdir('/afs/cern.ch/user/a/attikis/scratch0/')
DEB [20121120-18:18:40.074] thr=1   paramiko.transport: EOF in transport thread

Out[10] Script Execution time:
	0 days, 0 hours, 0 minutes, 59.0 seconds.
'''

# All required modules here
import python_myFunctions as myFunctions
import paramiko
from optparse import OptionParser 
import getpass
import os
import time
import sys

# Object and variable declarations here
mf = myFunctions.CreateObject()
parser = OptionParser()

parser.add_option("-a", "--remote_host_address", default = "lxplus5.cern.ch", dest = "remote_host_address", help = "ADDRESS OF REMOTE HOST", metavar = "ADDRESS OF REMOTE HOST")
parser.add_option("-u", "--username", dest = "username", default = "attikis", help = "AUTHENTICATION USERNAME", metavar = "AUTHENTICATION USERNAME")
(options, args) = parser.parse_args()

hostName = options.remote_host_address
userName = options.username
myPort = 22
remoteDir = "/afs/cern.ch/user/a/attikis/scratch0/"
logFileName = "sftpPut.log"
localDir = "/Users/administrator/my_work/programming/python/doc/"
localFile = "Python_Unix_and_Linux_admin.pdf"

if not (options.remote_host_address and options.username):
    print __doc__
    parser.error("REMOTE HOST and USERNAME are mandatory")

if __name__ == "__main__":
    mf.StopWatchStart()
    
    # Track what we do in a log-file
    paramiko.util.log_to_file(logFileName)

    # Create a transport object and connect to SSH server
    #passWord = getpass.getpass("%s@%s's password: " % (userName, hostName))
    passWord = "xKa[99448024]aa569282piasme"
    myTransport = paramiko.Transport( (hostName, myPort) )

    mf.Cout("Connecting to:\n\t%s@%s" % (userName, hostName) )
    myTransport.connect( username=userName, password=passWord )
    
    # Check if host is active before continuing
    bActive = myTransport.is_active()
    mf.Cout("Checking if %s is active:\n\t%s" % (hostName, bActive) )

    # Create a Secure File Transfer Protocol (SFTP) object
    sftp = paramiko.SFTPClient.from_transport(myTransport)

    # List file in remote path
    mf.Cout("Listing all files in remote directory:\n\t%s" % (remoteDir) )
    files = sftp.listdir(remoteDir)
    mf.Cout("Remote directory file-list:\n\t%s" % (files) )

    localFileName = os.path.join(localDir, localFile)
    remoteFileName = os.path.join(remoteDir, localFile)
    if not mf.IsFile(localFileName):
        sys.exit(1)
    mf.Cout("Copying file:\n\t%s\nto:\n\t%s" % (localFileName, remoteFileName))
    sftp.put(localFileName, remoteFileName)
            
    # List file in remote path again to see if file was indeed copied
    newFiles = sftp.listdir(remoteDir)
    bFileFound = False
    for file in newFiles:
        if file == localFile:
            bFileFound = True
            mf.Cout("Found file %s on remote host." % (file) )
            break
        else:
            bFileFound = False
            
    if bFileFound == True:
        mf.Cout("File %s succescully copied to %s on %s@%s" % (localFileName, remoteFileName, userName, hostName) )
    
    # Close connection
    mf.Cout("Closing connection.")
    myTransport.close()

    # Investigate report log
    logFile = open(logFileName, "r")
    mf.Cout("Logfile %s:\n\t" % (logFileName) )
    print logFile.read()

    # Print elapsed time for script execution 
    mf.StopWatchStop()
