#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Regular expressions in python
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is an example of performing reObject.findall(string) on given a sentence or string. In particular, raw string patterns are used to search for words beginning with the letter "t" (\bt) and end with the letter "e" (e\b), with anything in-between (.*?)
'''

# First import the regular expressions module
import re

# Create a string representing a pattern to look for. The .*? command matches anything, including whitespace.
# Remember, raw strings (r"Some string here") ignore escape sequences (\n, \t, \b, \w) and interpret them as normal characters.
rawStringPattern1 = r"\bt.*?e\b"
reObject1 = re.compile(rawStringPattern1)
# The above raw string pattern indicates to search for words beginning with the letter "t" (\bt) and end with the letter "e" (e\b), with anything in-between (.*?)

myString = "The beat poet, Alexandros Attikis, spent some tenacious and precious time in times square, near the Hilton hotel."
result1 = reObject1.findall(myString)
print result1

# The findall(myString) command returns:
# ['tenacious and precious time', 'times square', 'the']
# ignoring the word "The" due to the capital "T". It returns the words 'tenacious and precious time' since it found a word starting with the letter "t" (tenacious) and it 
# continued to look through the string until it found a word that ended with the letter "e" (time). It also successfully found the word "the" as is starts and ends with the 
# two specified letters. 

# To exclude the whitespace we must use the raw string r"\bt\w*e\b" (\w*)
rawStringPattern2 = r"\bt\w*e\b"
reObject2 = re.compile(rawStringPattern2)
result2 = reObject2.findall(myString)
print result2
# The second attempt returns:
# ['time', 'the']
