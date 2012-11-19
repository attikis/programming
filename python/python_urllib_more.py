#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Use urllib to read/retrieve files on the web

# docstrings
'''
Usage:
python python_urllib2.py 

Description:
This script retrieves a file from the internet, from a user defined URL, and saves it to the current directory with a specified file-name. It employs the "urllib" 
python module, which, among other things, can also identify and use FTP resources.

Help:
[attikis:python]> python python_urllib2.py -h
Usage: python_urllib2.py [options]

Options:
  -h, --help            show this help message and exit
  -a URL ADDRESS, --url_address=URL ADDRESS
                        URL ADDRESS
  -l NAME OF LOCAL FILE, --local_file_name=NAME OF LOCAL FILE
                        NAME OF LOCAL FILE
  -u USERNAME, --username=USERNAME
                        USERNAME for url
  -p PASSWORD, --password=PASSWORD
                        PASSWORD for url

Usage:
[attikis:python]> python python_urllib2.py -a http://cmsdoc.cern.ch/~attikis/attikis/docs/HPlusNote11_Poster.pdf -l poster.pdf
Out[1] Retrieving file in URL:
	http://cmsdoc.cern.ch/~attikis/attikis/docs/HPlusNote11_Poster.pdf
Out[2] Saved file in current directory:
	poster.pdf
Out[3] Script Execution time:
	0 days, 0 hours, 0 minutes, 1.0 seconds.
'''

import sys
import urllib
import python_myFunctions as myGFs
from optparse import OptionParser 

# Object declaration here
mf = myGFs.CreateObject()
mf.StopWatchStart()
parser = OptionParser() 

# Other declarations here
myURL = "http://cmsdoc.cern.ch/~attikis/attikis/docs/cv.pdf"

# Options: Mandatory
parser.add_option("-a", "--url_address", dest = "url_address", help = "URL ADDRESS", metavar = "URL ADDRESS")
parser.add_option("-l", "--local_file_name", dest = "local_file_name", help = "NAME OF LOCAL FILE", metavar = "NAME OF LOCAL FILE")
# Options: Optional
parser.add_option("-u", "--username", dest = "username", help = "USERNAME for url", metavar = "USERNAME") 
parser.add_option("-p", "--password", dest = "password", help = "PASSWORD for url", metavar = "PASSWORD")
(options, args) = parser.parse_args()

# Check that all mandatory arguments have been passed before proceeding
if not (options.url_address and options.local_file_name):
    print __doc__
    parser.error("The following arguments are mandatory for script execution:\n\tURL ADDRESS, LOCAL FILE NAME")
    
# Pull down the specified URL and save it to a specified local file name
mf.Cout("Retrieving file in URL:\n\t%s" % (options.url_address))
urllib.urlretrieve(options.url_address, options.local_file_name)
mf.Cout("Saved file in current directory:\n\t%s" % (options.local_file_name))
mf.StopWatchStop()
