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

'''

# All required modules here
import python_myFunctions as myFunctions
import paramiko
from optparse import OptionParser 
import getpass

# Object and variable declarations here
mf = myFunctions.CreateObject()
parser = OptionParser()

parser.add_option("-a", "--remote_host_address", default = "lxplus5.cern.ch", dest = "remote_host_address", help = "ADDRESS OF REMOTE HOST", metavar = "ADDRESS OF REMOTE HOST")
parser.add_option("-u", "--username", dest = "username", default = "attikis", help = "AUTHENTICATION USERNAME", metavar = "AUTHENTICATION USERNAME")
(options, args) = parser.parse_args()

hostName = options.remote_host_address
userName = options.username

if not (options.remote_host_address and options.username):
    print __doc__
    parser.error("REMOTE HOST and USERNAME are mandatory")

if __name__ == "__main__":
    mf.StopWatchStart()
    paramiko.util.log_to_file("ssh.log")
    ssh = paramiko.SSHClient()
    # Load the host keys (comes from the "know_hosts" file)
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Securely get password before connecting
    passWord = getpass.getpass("\tPassword = ")

    # Connect to the SSH server
    mf.Cout("Attempting to ssh:\n\t%s@%s" % (userName, hostName))    
    ssh.connect(hostName, username = userName, password = passWord) #ssh.connect("194.42.1.1", username = "php7aa2", password = "ez2?u2gf")

    # Execute a command remotely
    mf.Cout("Executing a command remotely and return three file handles associated with it.")
    stdin, stdout, stderr = ssh.exec_command("ls -lt")
    mf.Cout("stderr.read():\n\t%s" % (stderr.read()))
    mf.Cout("stdout.read():\n\t%s" % (stdout.read()))

    # Close connection
    mf.Cout("Closing connection.")
    ssh.close()

    # Investigate report log
    logFileName = "ssh.log"
    logFile = open(logFileName, "r")
    mf.Cout("Logfile %s:\n\t" % (logFileName) )
    print logFile.read()

    # Print elapsed time for script execution 
    mf.StopWatchStop()

