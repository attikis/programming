#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : My very own example use of the regular expression (re) search() function

# Import regular expressions module
import re
# Import my general functions module
import python_myGeneralFunctions as myGFs

gf = myGFs.GeneralFunctions()

gf.Cout("Example 1: Phonebook")
myStringList = ["Alexandros Attikis 08/05/1982", "Charalambos Charalambous 21/05/1982", "Constantinos Attikis 21/01/1979"]
myPattern = r"(?P<FirstName>\w+) (?P<Surname>\w+) (?P<Bday>\S+)"
reObject = re.compile(myPattern)

# Loop over string list
for iString in myStringList:
    search = reObject.search(iString)
    gf.DisplayMatchObject(search)
    print
    import sys
    sys.exit()
    
# A nice poker-program example
gf.Cout("Example 2: Poker program")

# First define the allowed pattern
validCards = r"^[a2-9tjqk]{5}$" #represents valid pattern: a=ace, 2-9 = numbers 2-9, t=10, j=jack, q=queen, k=king

# Compile the pattern
rePoker = re.compile(validCards)

# Define some players' hands (string to search if valid)
PlayerHands = ["22tqa", "ttaqk", "563ta", "qqjt9", "eeeee"]

# Define allowed hands here
rePair = re.compile(r".*(.).*\1")

# Loop over all 4 hands to see if the cards are valid (not the hands)
for iPlayer in PlayerHands:

    print "Hand:"
    searchHands = rePoker.match(iPlayer)
    (gf.DisplayMatchObject(searchHands))

    print "Pair:"
    searchForPairs = rePair.match(iPlayer)
    if searchForPairs:
        print 'This dude has a pair of "%s"' % (searchForPairs.group(1))
    (gf.DisplayMatchObject(searchForPairs))
    print

