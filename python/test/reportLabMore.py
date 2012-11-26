#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : 

'''
Usage:
./python_reportLabMore.py

Description:
This is an example of how to create a disk usage report and save it in PDF format.
'''

# All required modules here
import subprocess
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import python_myFunctions as myFunctions

# Object and variable declarations here
mf = myFunctions.CreateObject()

# Define function that calls the "df -h" command and returns it as a list
def diskReport(myShellCommand):
    mf.Cout("Calling subprocess:\n\t%s" % (myShellCommand) )
    myProcess = subprocess.Popen(myShellCommand, shell = True, stdout=subprocess.PIPE)
    return myProcess.stdout.readlines()

# Define function that creates a PDF report using the report as an input 
def createPDF(input, output = "disk_report.pdf"):
    mf.Cout("Creating PDF file:\n\t%s" % (output) )
    # Create datetime object from "now"
    now = datetime.datetime.now()
    date = now.strftime("%h %d %Y %H:%M:%S") #change to user-friendly date format
    # Create a canvas object
    myCanvas = canvas.Canvas(output)
    # Create a text object that will be placed in the PDF document
    textObject = myCanvas.beginText()
    # Define the way you want the data to pack into the page: Set the text origin at 28 cm
    textObject.setTextOrigin(cm, 28*cm)
    # Define the Title of the document
    textObject.textLines('''
Disk Capacity Report: %s
''' % (date) )

    # Iterate over our list of lines from the "df" command
    for line in input:
        textObject.textLine( line.strip() ) # need strip to remove newline characters \n (shown as black squares instead)

    # Draw the text object on the canvas
    myCanvas.drawText(textObject)
    # Stop the canvas drawing with the showPage() function
    myCanvas.showPage()
    # Save the canvas with the already defined name "disk_report.pdf"
    myCanvas.save()
    
# Run main function here
if __name__ == "__main__":
    report = diskReport("df -h")
    fileName = "my_disk_report.pdf"
    createPDF(report, fileName)
    mf.Cout("Opening file:\n\t%s" % (fileName) )
    subprocess.Popen("open " + fileName, shell = True)
    
