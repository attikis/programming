#!/usr/bin/env python
# Permissions : chmod +x fileName.py

'''
Usage:
./python_scriptOptions.py
or
python python_scriptOptions.py -a smtp.gmail.com -p 587

Description:
This is a simple script that provides an example of how to create a script that takes arguments from the shell, upon execution of the script.

Example:
attikis:python]> python python_scriptOptions.py -f writelines.txt -l 4
Out[1] Options: {'nLines': 4, 'fileName': 'writelines.txt'}, args: []
Out[2] Attempting to open file:
	writelines.txt
Out[3] File openened succesfully. Printing lines.
Line 0: *** This is line number 0.

Line 1: *** This is line number 1.

Line 2: *** This is line number 2.

Line 3: *** This is line number 3.

Out[4] readFile(writelines.txt, 4) returned True

Help:
[attikis:python]> python python_scriptOptions.py -h
Usage: python_scriptOptions.py [options]

Options:
  -h, --help            show this help message and exit
  -f FILENAME, --fileName=FILENAME
                        FILENAME for read
  -l NLINES, --nLines=NLINES
                        NLINES to read
'''

# All required modules here
import python_myFunctions as myFunctions
from optparse import OptionParser
import sys

# Object and variable declarations here
mf = myFunctions.CreateObject()

def readFile(fileName, nLines):
    mf.Cout( "Attempting to open file:\n\t%s" % (fileName) )
    try:
        myFile = open(fileName, "r")
        mf.Cout( "File openened succesfully. Printing lines.")
        for i in range (0, nLines):
            lineRead = myFile.readline()
            print "Line %s: %s" % (i, lineRead)
        returnValue = True
    except IOError as e:
        mf.Cout("I/O error({0}): {1}".format(e.errno, e.strerror))
        returnValue = False
    except:
        mf.Cout("Unexpected error:", sys.exc_info()[0])
        returnValue = False

    return returnValue

if __name__ == "__main__":
    # Define script options here. First define a parser object
    parser = OptionParser()
    # Parse the user-defined arguments, and put them into an appropriate format to pass to the readFile(fileName, nLines) function
    parser.add_option("-f", "--fileName", dest = "fileName", default = "writelines.txt", help = "FILENAME for read", metavar = "FILENAME")
    parser.add_option("-l", "--nLines"  , dest = "nLines"  , default = 5, type = "int" , help = "NLINES to read "  , metavar = "NLINES")
    (options, args) = parser.parse_args()
    mf.Cout( "Options: %s, args: %s" % (options, args) )

    # Now call our main function, giving as input either the user-defined shell arguments or the default ones (if the user fails to provide his own)
    readFile = readFile(options.fileName, options.nLines)
    # Print the exit status of the function
    mf.Cout( "readFile(%s, %s) returned %s" % (options.fileName, options.nLines, readFile) )
    if readFile == False:
        mf.Cout( "Please read the module docstrings:")
        print __doc__
    
    sys.exit(not readFile) #failure == 1, success == 0
    #sys.exit(__doc__) # will print the function's docstrings upon exiting
