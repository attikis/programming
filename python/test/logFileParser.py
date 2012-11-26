#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example of how to parse a logfile

''' 
Usage:
python_logFileParser.py someLogFile

Description:
This script takes one command line argument (name of log-file to parse) and it parses it
 to generate a report which associates remote hosts with number of bytes transferred to them.
''' 

# Import all modules here
import sys
import python_myGeneralFunctions as myGFs
import socket #to get hostname and ip

# Declarations here
gf = myGFs.GeneralFunctions()

hostName = socket.gethostname()
ipAddress = socket.gethostbyname(hostName)
myString =  "%s %s" % (hostName, ipAddress)

gf.Cout("Obtaining ip address and my host-name using the socket module.")
try:
    ipFileName = "/Users/administrator/my_work/programming/python/myIP.txt"
    inFile = open(ipFileName, "w") #"a" for append mode
    inFile.write(myString)
    inFile.write("\n")
    gf.Cout('Wrote information to file "%s."' % (ipFileName))
finally:
    gf.Cout('Reading information written in file "%s".' % (ipFileName))
    inFile.close()

try:
    inFile = open("myIP.txt", "r")
    print inFile.readlines()
finally:
    inFile.close()
    
# Function-definition here
def DictifyLine(line):
    ''' def DictifyLine(line):
    Return a dictionary of the relevant pieces of a log-file
    '''
    # Use line split to generate a dictionary
    splitLine = line.split()
    output = {'host-name': splitLine[0],
              'ip-address': splitLine[1],
              }
    return output

def GenerateLogReport(inputFile):
    ''' def GenerateLogReport(inputFile):
    Return a dictionary of format host_name=>[ip_address]
    
    This function takes a file object, iterates through all the lines in the file, and generates 
    a report of the host-name and ip-address.
    '''
    # Create empty dictionary
    reportDict = {}
    # Loop over all lines ins input file, split lines to strings and assign first item in list as host-name, second as ip-address
    for line in inputFile:
        lineDict = DictifyLine(line)
        ip_address = lineDict['ip-address']
        reportDict.setdefault(lineDict['host-name'], []).append(ip_address)
    return reportDict


if __name__ == "__main__":
    # If no argument is passed when running this script, print the script's documentation and exit
    if not len(sys.argv) > 1:
        gf.Cout("ERROR! No input file specified. Please specify a valid file to parse. Exiting python shell.")
        print __doc__
        sys.exit(1)
    # Define the script input as the first argument passed when running the script: |\> python python_logFileParser.py argument
    inFileName = sys.argv[1]
    try:
        inFile = open(inFileName, "r")
    except IOError:
        gf.Cout("ERROR! Input file with name %s in invalid. Please specify a valid file to parse. Exiting python shell." % (inFileName))
        print __doc__
        sys.exit(1)
    # If everythin is ok execute the main program and print the log-report. Then close the input file
    finally:
        gf.Cout('Generating log report using file "%s" as input.' % (ipFileName))
        logReport = GenerateLogReport(inFile)
        gf.Cout("Log report output:")
        gf.Cout(logReport)
        #inFile.close() #no need since we use "try" and "finally"
