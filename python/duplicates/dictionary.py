#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example of creating and using a dictionary

import python_myGeneralFunctions as myGFs
gf = myGFs.GeneralFunctions()

gf.Cout("A simple example")
addressbook = {'name': "Alexandros", 'surname': "Attikis"} 
print addressbook['name']
print

gf.Cout("A more complex example")

# Delcarations here
nameList = ["Alexandros", "Xenios", "Ino", "Constantinos", "Stelios", "Leonidas"] #key
surnameList = ["Attikis", "Attikis", "Attiki", "Attikis", "Charalambous", "Michaelides"] #value
myDictionary = {} #empty dictionary

# Loop over item in lists
for name, surName in map(None, nameList, surnameList):
    # Fill in Dictionary{'key': value} with Dictionary['key'] = value
    myDictionary[name] = surName 
#print type(myDictionary)
    
# Function to sort keys
def sortedDictKeys(dict):
    ''' sortedDictKeys(dict):
    A mapping (such as a "dictionary) has NO order, thus it cannot be sorted. Still, its keys can be extracted as a list, which can then be sorted.
    '''
    keys = dict.keys()
    keys.sort()
    return [key for key in keys]

# Function to sort keys
def sortedDictValues(dict):
    ''' sortedDictValues(dict):
    A mapping (such as a "dictionary) has NO order, thus it cannot be sorted. Still, its keys can be extracted as a list, which can then be sorted.
    '''
    keys = dict.keys()
    keys.sort()
    return [dict[key] for key in keys]

gf.Cout("Printing dictionary")
print myDictionary

gf.Cout("Printing dictionary.keys()")
print myDictionary.keys()

gf.Cout("Printing sorted keys of dictionary")
print sortedDictKeys(myDictionary)

gf.Cout("Printing dictionary of sorted keys")
print sortedDictValues(myDictionary)

gf.Cout("Printing values of specific keys")
key = "Constantinos"
print "myDictionary[%s] = %s" % (key, myDictionary[key])
key = "Ino"
print "myDictionary[%s] = %s" % (key, myDictionary[key])


gf.Cout("Check if a key exists")
key = "Alexandros" 
print '%s in myDictionary = %s' % (key, key in myDictionary)

gf.Cout("This is an example of setdefault(key, value) method of a dictionary.")
print myDictionary
print myDictionary.setdefault("Alexandros", "Blah") #this key exists so it will return the already assigned value ("Attikis")
print myDictionary.setdefault("test", "Blah_Test")  #this key does not exist sto it will add it to the dictionary
print myDictionary
