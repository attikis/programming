#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Create a txt file file carrying a custom string for a specified number of lines

def CreateFile(file_name):

	"""
		CreateFile(file_name): makes a text file.
	"""

	path = '/Users/administrator/my_work/programming/python/' + file_name
	file = open(path, "w")
        # For loop here (number of lines)
        for i in range(1, 100000):
            string = "*** My pDq name is Alexandros Attikis pDq. ***\n"
            file.write(string)
	file.close()
	print '+++ Execution completed.'

if __name__ == "__main__":
    CreateFile('test.txt')
    print
