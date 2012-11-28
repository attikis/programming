#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Above line enables utf-8 encoding characters to be recognised by python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : A demonstration of the replace command, which takes two arguments. The string to replace and the string to replace it with. 

# import modules here
from string import ascii_lowercase
from string import ascii_uppercase

# class definition here
class myEnigma(object):
    def __init__(self, input):
        # Definitions here
        self.input = input
        print "+++ Input sequence:\n%s\n" % (self.input)
        self.encryption = ""
        self.decryption = ""
        self.lowerUnencryptedList = []
        self.upperUnencryptedList = []
        self.alphabetEncryptedList = []
        self.specialCharUnencryptedList = []
        self.specialCharEncryptedList = []
        self.numEncryptedList = []
        self.numUnencryptedList = []

        # store lower-case alphabet in list
        for i in ascii_lowercase:
            self.lowerUnencryptedList.append(i)
        #print self.lowerUnencryptedList
        #print

       # store upper-case alphabet in list
        for i in ascii_uppercase:
            self.upperUnencryptedList.append(i)
        #print self.upperUnencryptedList
        #print
    
        # create lists with substitution characters for alphabet (lower- and upper- case)
        self.alphabetEncryptedList = ["œ", "∑", "®", "†", "¥", "ø", "π", "“", "‘", "å", "ß", "∂", "ƒ", "©", "˙", "∆", "˚", "…", "æ", "«", "Ω", "≈", "ç", "√", "∫", "~"]
        #print self.alphabetEncryptedList
        #print
        
        # special characters    
        self.specialCharUnencryptedList = ["+", "-", "*", "!", ",", ":", ";", "[", "]", ".", '"', "?", " "]
        self.specialCharEncryptedList = ["v", "w", "x", "y", "z", "0", "1", "2", "3", "4", '5', "6", "7"]
        #print self.specialCharUnencryptedList
        #print self.specialCharEncryptedList
        #print

        # now for the numbers in range 0-9
        for i in range(0,10):
            self.numUnencryptedList.append(str(i))
        #print self.numUnencryptedList
        #print

        # replace numbers in range 0-9 with specific characters
        self.numEncryptedList = ["≤", "≥", "÷", "¡", "€", "#", "¢", "∞", "§", "¶"]
        #print self.numEncryptedList
        #print
        
    # encryption function
    def encrypt(self):
        output = self.input.lower()
        
        # First remove all whitespace to make it difficult to recognise blocks of words
        #print "+++ Replacing %s with %s" % (" ", "æ")
        #output = self.input.replace(" ", "æ")

        #1) For numbers in range 0-9
        for i, j in map(None, self.numUnencryptedList, self.numEncryptedList):
            #print "+++ Replacing %s with %s" % (i,j)
            output = output.replace(i,j)
        #print
            
        #2) lower-case letters: Loop over character substitution map
        for i, j in map(None, self.lowerUnencryptedList, self.alphabetEncryptedList):
            #print "+++ Replacing %s with %s" % (i,j)
            output = output.replace(i,j)
        #print

        #3) special characters
        for i, j in map(None, self.specialCharUnencryptedList, self.specialCharEncryptedList):            
            #print "+++ Replacing %s with %s" % (i,j)
            output = output.replace(i,j)
        #print

        self.encryption = output
        print "+++ Encrypted sequence:\n%s\n " % (self.encryption)
        return output

    # decryption function
    def decrypt(self):
        output = self.encryption

        # First remove all whitespace to make it difficult to recognise blocks of words
        #print "+++ Replacing %s with %s" % ("æ"," ")
        #output = self.encryption.replace("æ", " ")

        #3) special characters
        for i, j in map(None, self.specialCharUnencryptedList, self.specialCharEncryptedList):            
            #print "+++ Replacing %s with %s" % (j,i)
            output = output.replace(j,i)
        #print
            
        #2) lower-case letters: Loop over character substitution map
        for i, j in map(None, self.lowerUnencryptedList, self.alphabetEncryptedList):
            #print "+++ Replacing %s with %s" % (j,i)
            output = output.replace(j,i)
        #print

        #1) For numbers in range 0-9
        for i, j in map(None, self.numUnencryptedList, self.numEncryptedList):
            #print "+++ Replacing %s with %s" % (j,i)
            output = output.replace(j,i)
        #print

        self.decryption = output
        print "+++ Decrypted sequence:\n%s\n" % (self.decryption)
        return output
    
# main function here
if __name__ == '__main__':
    message = 'CLASSIFIED! Operation Overlord is the code name for the Battle of Normandy, the operation that will launch the invasion of German-occupied western Europe by Allied forces. The operation will commence on the 6th of June 1944 with the Normandy landings, aka "Operation Neptune" or "D-Day".'
    code = myEnigma(message)
    encryption = code.encrypt()
    decryption = code.decrypt()