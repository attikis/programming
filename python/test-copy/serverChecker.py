#!/usr/bin/env python
# Permissions : chmod +x fileName.py

'''
Usage:
/python_serverChecker.py
or
python python_serverChecker.py -

Description:
This is a socket-based web server checker. It allows one to determine what the status of a web server is, whether the web server generates HTTP headers 
with expected status code for some specific URL.

Example:
Could not find a server/port combination that would work. So all my tests failed. The code itself should be ok since I followed word by word from the book.
'''

# All required modules here
import python_myFunctions as myFunctions
import socket
import re
import sys

# Object and variable declarations here
mf = myFunctions.CreateObject()

def checkWebServer(address, port, resource):
    # Construct HTTP request string
    if not resource.startswith("/"):
        resource = "/" + resource
    request_string = "GET %s HTTP/1.1\r\nHost: %s\r\n\r\n" % (resource, address)
    mf.Cout("HTTP request:")
    mf.Cout("||| %s |||" % (request_string))
    
    # Create a TCP socket
    s = socket.socket()
    mf.Cout("Attempting to connect to %s, on port %s" % (address, port))
    try:
        # Connect with socket object to the defined server
        s.connect( (address, port) )
        mf.Cout("Connected to %s, on port %s" % (address, port))
        # Send the HTTP request to the server
        s.send(request_string)
        # Read back 100 bytes of the server response
        nBytes = 100
        serverRespond = s.recv(nBytes)
        mf.Cout("Received %s bytes of HTTP response" % (nBytes) )
        mf.Cout("||| %s |||" % (serverRespond))
        # Handle respond exceptions
    except socket.error, e:
        mf.Cout("Connection to %s, on port %s failed:\n\t%s" % (address, port, e))
        return False
    finally: 
        # Close connection to server
        s.close()
        
    # Extract the status code from the server respond
    lines = serverRespond.splitlines()
    for i in lines:
        mf.Cout("Line#%i of HTTP response: %s" % (i, lines[0]))

    try:
        version, status, message = re.split(r"\s+", lines[0], 2)
        mf.Cout("Versions: %s, Status: %s, Message: %s" % (version, status, message))
    except ValueError:
        mf.Cout("Failed to split status line.")
        return False
    if status in ["200", "301"]: # 200 = "OK", 301= "Moved Permanently". See http://www.searchenginepromotionhelp.com/m/http-server-response/http-response-codes.php
        mf.Cout("Success! Status was %s." % (status))
        return True
    else:
        mf.Cout("Status was %s." % (status))
        return False
    
# Main now business here
if __name__ == "__main__":
    from optparse import OptionParser
    # Define a parser object and add script options
    parser = OptionParser()
    parser.add_option("-a", "--address", dest = "address", default = "localhost", help = "ADDRESS of web-server", metavar = "ADDRESS")
    parser.add_option("-p", "--port"   , dest = "port"   , type = int, default = 80, help = "PORT of web-server", metavar = "PORT")
    parser.add_option("-r", "--resource",dest = "resource", default = "index.html", help = "RESOURCE to check", metavar = "RESOURCE")

(options, args) = parser.parse_args()

mf.Cout("Options:\n\t%s" % (options))
mf.Cout("Arguments:\n\t%s" % (args))
check = checkWebServer(options.address, options.port, options.resource)
mf.Cout("checkWebServer(%s, %s, %s) returned %s." % (options.address, options.port, options.resource, check))
sys.exit(not check)
