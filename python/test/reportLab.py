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

from reportlab.pdfgen import canvas

def hello():
    # First create a canvas
    myCanvas = canvas.Canvas("helloworld.pdf")
    # Next write to the canvas in similar fashion to writing to a file with fileObject.write(string)
    myCanvas.drawString(100, 100, "Hello World!")
    # Stop the drawing with the showPage() function
    myCanvas.showPage()
    # Create the pdf document with the save() function
    myCanvas.save()

if __name__ == "__main__":
    hello()
