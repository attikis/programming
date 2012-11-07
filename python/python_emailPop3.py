#!/usr/bin/env python
# Permissions : chmod +x fileName.py
# To launch   : python fileName.py    OR    ./fileName.py 
# Definition  : Example script of how to retrieve email from a server

# Import modules here
import python_myGeneralFunctions as myGFs
import poplib

gf = myGFs.GeneralFunctions()
mail_server = "pop3.live.com"
port = 995

hotmail = poplib.POP3(mail_server, port)
try:
#Get the username and password from the standard input
    gf.Cout("Please provide your login credentials:\n\t")
    hotmail.user(raw_input("username: ")) 
    hotmail.pass_(raw_input("password: "))

for msg_id in hotmail.list()[1]:
    print msg_id
    #outf = open('%s.eml' % msg_id, 'w')
    #outf.write('\n'.join(p.retr(msg_id)[1]))
    #outf.close()
hotmail.quit()
