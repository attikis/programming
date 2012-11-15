#!/usr/bin/env python
# Permissions : chmod +x fileName.py

'''
Usage:
./python_portChecker.

Description:
This is a simple script that makes a socket connection to a web server, to chech that the server is still up and it is still listening on some port.
'''

# All required modules here
import python_myFunctions as myFunctions
import socket
import re
import sys

# Object and variable declarations here
mf = myFunctions.CreateObject()

def checkServer(address, port):
    # Create a default TCP socket object
    s = socket.socket()
    mf.Cout( "Attempting to connect to %s, on port %s" % (address, port) )
    try:
        # Try to connect to the specified address and port number
        s.connect( (address, port) ) 
        mf.Cout( "Succesfully connected to %s, on port %s" % (address, port) )
        # If connection succeeds return true
        return True
    # If connection fails, the socket.connect() call will throw and exception (which is handled) and the function returns false
    except socket.error, e:
        mf.Cout( "Connection to %s, on port %s failed: %s " % (address, port, e) )
        return False
        
if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    # Parse the checkServer(address, port) arguments from the user and put them into an appropriate format to pass to the checkServer() function
    parser.add_option("-a", "--address", dest = "address", default = "pop3.live.com", help = "ADDRESS for server", metavar = "ADDRESS")
    parser.add_option("-p", "--port", dest = "port", type = "int", default = 995, help="PORT for server", metavar = "PORT")
    
    (options, args) = parser.parse_args()
    mf.Cout( "Options: %s, args: %s" % (options, args) )
    check = checkServer(options.address, options.port)
    mf.Cout( "checkServer(%s, %s) returned %s" % (options.address, options.port, check) )
    # Return the opposite of the checkServer() return code to the shell. Typically, utilities like this return 0 to the shell on success
    # and something else than 0 on failure (typically a positive integer, like 1)
    sys.exit(not check) #failure == 1, success == 0
    #sys.exit(__doc__) # will print the function's docstrings upon exiting

#In [8]: sys.exit??
#Type:       builtin_function_or_method
#String Form:<built-in function exit>
#Docstring:
#exit([status])

#Exit the interpreter by raising SystemExit(status).
#If the status is omitted or None, it defaults to zero (i.e., success).
#If the status is numeric, it will be used as the system exit status.
#If it is another kind of object, it will be printed and the system
#exit status will be one (i.e., failure).
