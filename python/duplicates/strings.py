#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Multiple ways of defining strings in python

def PrintStringTypes():
    string1 = 'This is a string'
    string2 = "This is another string"
    string3 = '''This is still another string'''
    string4 = """And one more string"""
    stringList = [string1,string2,string3,string4]
    print stringList

    quoteString1 = "This is a string with 'quotes' in it"
    quoteString2 = "This is another string with \'quotes\' in it"
    quoteString3 = 'This is still another string with "quotes" in it'
    quoteString4 = 'And one more string with \"quotes\" in it'
    quoteStringList = [quoteString1,quoteString2,quoteString3,quoteString4]
    print quoteStringList

# The triple-quotes are useful when you want to produce a multiline in the python shell or IPython. Using them you can start a string in one line, press enter and continue in the next line, and so on. For a script they offer nothing new than single quotes.
    mLineString1 = '''This is a multiline string\n'''
    lineSeparator = "*" * 40
    print mLineString1 + lineSeparator

if __name__ == '__main__':
    PrintStringTypes()

