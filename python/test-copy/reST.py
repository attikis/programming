#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : 

'''
Usage:
./python_.

Description:
This is a ...

Example:
[attikis:python]> ./python_
Out[1] 
...
'''

# Import required modules here
import docutils.core

# Define the re-Structured Text here
reStructuredText = '''
=======
Heading
=======
SubHeading
----------
This is a simple subsections of a reStructuredText (reST). 
This is how a bulleted list is represented:

- item one
- item two
- item three
'''

# Format the reST text as HTML. By default the docutils library puts an embedded stylesheet in the generated HTML page so that it doesn't look too plain.
html = docutils.core.publish_string(source = reStructuredText, writer_name = "html")
html_slice = html[html.find("<body>") + 6:html.find("</body>")]
print html
print "*********************************************************************"
print html_slice

# Now save html format of reST text to a file and close it
try:
    saveFile = open("reST.html", "w")
    saveFile.write(html)
    saveFile_slice = open("reST_slice.html", "w")
    saveFile_slice.write(html_slice)
finally:
    saveFile.close()
    saveFile_slice.close()

# To see how this file is interpreted in html visit: 
# http://cmsdoc.cern.ch/~attikis/attikis/docs/reST.html
# and
# http://cmsdoc.cern.ch/~attikis/attikis/docs/reST_slice.html
# For details on reST syntax visit: http://docutils.sourceforge.net/docs/user/rst/quickref.html
