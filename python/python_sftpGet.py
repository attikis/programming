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
In this example we present how to retrieve files from an SSH server.

Help:
Usage: python_sftGet.py [options]

Options:
  -h, --help            show this help message and exit
  -a ADDRESS OF REMOTE HOST, --remote_host_address=ADDRESS OF REMOTE HOST
                        ADDRESS OF REMOTE HOST
  -u AUTHENTICATION USERNAME, --username=AUTHENTICATION USERNAME
                        AUTHENTICATION USERNAME

Example:
[attikis:python]> python python_sftGet.py -a lxplus5.cern.ch -u attikis
attikis@lxplus5.cern.ch's password: 
Out[1] Connecting to:
	attikis@lxplus5.cern.ch
Out[2] Checking if lxplus5.cern.ch is active:
	True
Out[3] Listing all files in remote directory:
	/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/
Out[4] Remote directory file-list:
	['.git', '.gitignore', 'README', 'data', 'koe.txt', 'src', 'workspace', 'root', 'programs', 'bin', 'refs', 'info', 'branches', 'hooks', 'description', 'objects', 'HEAD', 'config']
Out[5] Looping over all files/dirs in remote directory:
	/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/
Out[6] Skipping directory: /afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/.git
Out[7] Retrieving file:
	/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/.gitignore
to:
	/Users/administrator/my_work/programming/python/ssh_more/.gitignore
Out[8] Retrieving file:
	/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/README
to:
	/Users/administrator/my_work/programming/python/ssh_more/README
Out[9] Skipping directory: /afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/data
Out[10] Retrieving file:
	/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/koe.txt
to:
	/Users/administrator/my_work/programming/python/ssh_more/koe.txt
Out[11] Skipping directory: /afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/src
Out[12] Skipping directory: /afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/workspace
Out[13] Skipping directory: /afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/root
Out[14] Skipping directory: /afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/programs
Out[15] Skipping directory: /afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/bin
Out[16] Skipping directory: /afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/refs
Out[17] Skipping directory: /afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/info
Out[18] Skipping directory: /afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/branches
Out[19] Skipping directory: /afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/hooks
Out[20] Retrieving file:
	/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/description
to:
	/Users/administrator/my_work/programming/python/ssh_more/description
Out[21] Skipping directory: /afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/objects
Out[22] Retrieving file:
	/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/HEAD
to:
	/Users/administrator/my_work/programming/python/ssh_more/HEAD
Out[23] Retrieving file:
	/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/config
to:
	/Users/administrator/my_work/programming/python/ssh_more/config
Out[24] Closing connection.
Out[25] Logfile ssh_more.log:
	
DEB [20121120-15:23:00.335] thr=1   paramiko.transport: starting thread (client mode): 0x6843d50L
INF [20121120-15:23:00.438] thr=1   paramiko.transport: Connected (version 2.0, client OpenSSH_4.3)
DEB [20121120-15:23:00.520] thr=1   paramiko.transport: kex algos:['diffie-hellman-group-exchange-sha1', 'diffie-hellman-group14-sha1', 'diffie-hellman-group1-sha1'] server key:['ssh-rsa', 'ssh-dss'] client encrypt:['aes128-ctr', 'aes192-ctr', 'aes256-ctr', 'arcfour256', 'arcfour128', 'aes128-cbc', '3des-cbc', 'blowfish-cbc', 'cast128-cbc', 'aes192-cbc', 'aes256-cbc', 'arcfour', 'rijndael-cbc@lysator.liu.se'] server encrypt:['aes128-ctr', 'aes192-ctr', 'aes256-ctr', 'arcfour256', 'arcfour128', 'aes128-cbc', '3des-cbc', 'blowfish-cbc', 'cast128-cbc', 'aes192-cbc', 'aes256-cbc', 'arcfour', 'rijndael-cbc@lysator.liu.se'] client mac:['hmac-md5', 'hmac-sha1', 'hmac-ripemd160', 'hmac-ripemd160@openssh.com', 'hmac-sha1-96', 'hmac-md5-96'] server mac:['hmac-md5', 'hmac-sha1', 'hmac-ripemd160', 'hmac-ripemd160@openssh.com', 'hmac-sha1-96', 'hmac-md5-96'] client compress:['none', 'zlib@openssh.com'] server compress:['none', 'zlib@openssh.com'] client lang:[''] server lang:[''] kex follows?False
DEB [20121120-15:23:00.521] thr=1   paramiko.transport: Ciphers agreed: local=aes128-ctr, remote=aes128-ctr
DEB [20121120-15:23:00.521] thr=1   paramiko.transport: using kex diffie-hellman-group1-sha1; server key type ssh-rsa; cipher: local aes128-ctr, remote aes128-ctr; mac: local hmac-sha1, remote hmac-sha1; compression: local none, remote none
DEB [20121120-15:23:00.660] thr=1   paramiko.transport: Switch to new keys ...
DEB [20121120-15:23:00.676] thr=2   paramiko.transport: Attempting password auth...
DEB [20121120-15:23:00.868] thr=1   paramiko.transport: userauth is OK
INF [20121120-15:23:01.362] thr=1   paramiko.transport: Authentication (password) successful!
DEB [20121120-15:23:01.385] thr=2   paramiko.transport: [chan 1] Max packet in: 34816 bytes
DEB [20121120-15:23:01.771] thr=1   paramiko.transport: [chan 1] Max packet out: 32768 bytes
INF [20121120-15:23:01.771] thr=1   paramiko.transport: Secsh channel 1 opened.
DEB [20121120-15:23:01.902] thr=1   paramiko.transport: [chan 1] Sesch channel 1 request ok
INF [20121120-15:23:03.616] thr=2   paramiko.transport.sftp: [chan 1] Opened sftp connection (server version 3)
DEB [20121120-15:23:03.618] thr=2   paramiko.transport.sftp: [chan 1] listdir('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/')
DEB [20121120-15:23:03.964] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/.git')
DEB [20121120-15:23:04.049] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/.gitignore')
DEB [20121120-15:23:04.132] thr=2   paramiko.transport.sftp: [chan 1] open('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/.gitignore', 'rb')
DEB [20121120-15:23:04.216] thr=2   paramiko.transport.sftp: [chan 1] open('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/.gitignore', 'rb') -> 00000000
DEB [20121120-15:23:04.217] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/.gitignore')
DEB [20121120-15:23:04.638] thr=2   paramiko.transport.sftp: [chan 1] close(00000000)
DEB [20121120-15:23:04.728] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/README')
DEB [20121120-15:23:04.814] thr=2   paramiko.transport.sftp: [chan 1] open('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/README', 'rb')
DEB [20121120-15:23:04.903] thr=2   paramiko.transport.sftp: [chan 1] open('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/README', 'rb') -> 00000000
DEB [20121120-15:23:04.903] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/README')
DEB [20121120-15:23:05.544] thr=2   paramiko.transport.sftp: [chan 1] close(00000000)
DEB [20121120-15:23:05.628] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/data')
DEB [20121120-15:23:05.712] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/koe.txt')
DEB [20121120-15:23:05.797] thr=2   paramiko.transport.sftp: [chan 1] open('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/koe.txt', 'rb')
DEB [20121120-15:23:05.880] thr=2   paramiko.transport.sftp: [chan 1] open('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/koe.txt', 'rb') -> 00000000
DEB [20121120-15:23:05.880] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/koe.txt')
DEB [20121120-15:23:06.306] thr=2   paramiko.transport.sftp: [chan 1] close(00000000)
DEB [20121120-15:23:06.391] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/src')
DEB [20121120-15:23:06.475] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/workspace')
DEB [20121120-15:23:06.562] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/root')
DEB [20121120-15:23:06.648] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/programs')
DEB [20121120-15:23:06.733] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/bin')
DEB [20121120-15:23:06.822] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/refs')
DEB [20121120-15:23:06.907] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/info')
DEB [20121120-15:23:06.994] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/branches')
DEB [20121120-15:23:07.079] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/hooks')
DEB [20121120-15:23:07.164] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/description')
DEB [20121120-15:23:07.264] thr=2   paramiko.transport.sftp: [chan 1] open('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/description', 'rb')
DEB [20121120-15:23:07.348] thr=2   paramiko.transport.sftp: [chan 1] open('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/description', 'rb') -> 00000000
DEB [20121120-15:23:07.348] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/description')
DEB [20121120-15:23:07.775] thr=2   paramiko.transport.sftp: [chan 1] close(00000000)
DEB [20121120-15:23:07.861] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/objects')
DEB [20121120-15:23:07.947] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/HEAD')
DEB [20121120-15:23:08.031] thr=2   paramiko.transport.sftp: [chan 1] open('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/HEAD', 'rb')
DEB [20121120-15:23:08.115] thr=2   paramiko.transport.sftp: [chan 1] open('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/HEAD', 'rb') -> 00000000
DEB [20121120-15:23:08.116] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/HEAD')
DEB [20121120-15:23:08.536] thr=2   paramiko.transport.sftp: [chan 1] close(00000000)
DEB [20121120-15:23:08.622] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/config')
DEB [20121120-15:23:08.718] thr=2   paramiko.transport.sftp: [chan 1] open('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/config', 'rb')
DEB [20121120-15:23:08.803] thr=2   paramiko.transport.sftp: [chan 1] open('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/config', 'rb') -> 00000000
DEB [20121120-15:23:08.803] thr=2   paramiko.transport.sftp: [chan 1] stat('/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/config')
DEB [20121120-15:23:09.350] thr=2   paramiko.transport.sftp: [chan 1] close(00000000)
DEB [20121120-15:23:09.536] thr=1   paramiko.transport: EOF in transport thread

Out[26] Script Execution time:
	0 days, 0 hours, 0 minutes, 14.0 seconds.
'''

# All required modules here
import python_myFunctions as myFunctions
import paramiko
from optparse import OptionParser 
import getpass
import os

# Object and variable declarations here
mf = myFunctions.CreateObject()
parser = OptionParser()

parser.add_option("-a", "--remote_host_address", default = "lxplus5.cern.ch", dest = "remote_host_address", help = "ADDRESS OF REMOTE HOST", metavar = "ADDRESS OF REMOTE HOST")
parser.add_option("-u", "--username", dest = "username", default = "attikis", help = "AUTHENTICATION USERNAME", metavar = "AUTHENTICATION USERNAME")
(options, args) = parser.parse_args()

hostName = options.remote_host_address
userName = options.username
myPort = 22
remoteDir = "/afs/cern.ch/user/a/attikis/scratch0/Top2HPlus/"
logFileName = "ssh_more.log"
localDir = "/Users/administrator/my_work/programming/python/ssh_more/"

if not (options.remote_host_address and options.username):
    print __doc__
    parser.error("REMOTE HOST and USERNAME are mandatory")

if __name__ == "__main__":
    mf.StopWatchStart()
    
    # Track what we do in a log-file
    paramiko.util.log_to_file(logFileName)

    # Create a transport object and connect to SSH server
    passWord = getpass.getpass("%s@%s's password: " % (userName, hostName))
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

    # Loop over all files in remote path
    mf.Cout("Looping over all files/dirs in remote directory:\n\t%s" % (remoteDir) )
    # Create directory to save files locally
    mf.EnsureIsDir(localDir)
    for file in files:
        fileName = os.path.join(remoteDir, file)
        if mf.IsRemoteDir(sftp, fileName):
            mf.Cout("Skipping directory: %s" % (fileName))
            continue
        else:
            savePath = localDir+file
            fileToGet = os.path.join(remoteDir, file)
            mf.Cout("Retrieving file:\n\t%s\nto:\n\t%s" % (fileName, savePath))
            sftp.get(fileToGet, savePath)
            
    # Close connection
    mf.Cout("Closing connection.")
    myTransport.close()

    # Investigate report log
    logFile = open(logFileName, "r")
    mf.Cout("Logfile %s:\n\t" % (logFileName) )
    print logFile.read()

    # Print elapsed time for script execution 
    mf.StopWatchStop()
