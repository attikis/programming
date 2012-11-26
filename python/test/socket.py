#!/usr/bin/env python
# Permissions : chmod +x fileName.py

'''
Usage:
./python_socket.py

Description:
This is a simple test for creating/using socket objects in python.
'''

# All required modules here
import python_myFunctions as myFunctions
import socket 

# Object and variable declarations here
mf = myFunctions.CreateObject()

# Get my ip and hostname using the socket module
myHostName = socket.gethostname()
myIpAddress = socket.gethostbyname(myHostName)
mf.Cout("host-name: %s" % (myHostName) )
mf.Cout("IP-address: %s" % (myIpAddress) )

# Create a default socket object (no arguments passed): a TCP/IP socket
# The Transmission Control Protocol (TCP) is one of the core protocols of the Internet Protocol Suite. TCP is one of the two original components of the suite,
# complementing the Internet Protocol (IP), and therefore the entire suite is commonly referred to as TCP/IP. TCP provides reliable, ordered delivery of a stream
# of octets from a program on one computer to another program on another computer. TCP is the protocol used by major Internet applications such as the World Wide Web (WWW),
# email, remote administration and file transfer. 
mySocket = socket.socket()

# Connect to my ip-address using a given port
connectionPort = 80
ipToConnectTo = "smtp.cern.ch"
#ipToConnectTo = "smtp.gmail.com"
try:
    mf.Cout("Connecting to IP-address =  %s, through port = %s" % (ipToConnectTo, connectionPort) )
    # Establish a communication channel between mySocket object and the remote socket.
    mySocket.connect( (ipToConnectTo, connectionPort) ) # will not work! canno think of a valid IP address to test this
    # Transmit data from mySocket object to the remote socket: Send the server the string "GET / HTTP/1.0\n\n", which is simply an HTTP request.
    mf.Cout("Transmitting data to remote socket.")
    mySocket.send("GET / HTTP/1.0\n\n")
    mf.Cout("Receiving data from remote socket.")
    nFirstBytesToReceive = 200
    mySocket.recv(nFirstBytesToReceive)
finally:
    # Terminate the communication channel (close connection) between the two sockets.
    mySocket.close() 

    
