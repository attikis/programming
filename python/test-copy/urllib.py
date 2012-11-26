#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Use urllib to read files on the web

import urllib
import python_myGeneralFunctions as myGFs

gf = myGFs.GeneralFunctions()
#myURL = "http://cmsdoc.cern.ch/~attikis/attikis/docs/cv.pdf"
myURL = "http://cmsdoc.cern.ch/~attikis/attikis/docs/cv.tex"

try:
    myFile = urllib.urlopen(myURL)
    myOpenFile = myFile.read()
    # Read only the first 100 characters
    gf.Cout(myOpenFile[:100])
    # Read only the last 100 characters
    gf.Cout(myOpenFile[-100:])
    gf.Cout(len(myOpenFile))
    
finally:
    myFile.close()
    gf.Cout("Done")
