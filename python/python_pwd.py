#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a script that explains how to use pwd, the password database module (instead of subprocess). 
The pwd module provides access to the Unix user account and password database. It is available on all Unix versions.
Password database entries are reported as a tuple-like object, whose attributes correspond to the members of the passwd structure (Attribute field below, see <pwd.h>):
Index	Attribute            Meaning
0	pw_name	             Login name
1	pw_passwd	     Optional encrypted password
2	pw_uid	Numerical    user ID
3	pw_gid	Numerical    group ID
4	pw_gecos	     User name or comment field
5	pw_dir	             User home directory
6	pw_shell	     User command interpreter
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import pwd

if __name__ == "__main__":
    mf.StopWatchStart()

    # Get the password database entry for the given user name.
    loginList = ["attikis", 'root', 'administrator']
    
    for loginName in loginList:
        pwdDB = pwd.getpwnam(loginName)
        mf.Cout( 'Password DataBase for user "%s":\n\t%s' % (loginName, pwdDB) )
        
        # Get the last entry (tuple[6] or tuple[-1]) or of the tuple (shell). 
        shell = pwd.getpwnam('root')[-1] # same as: [6]
        mf.Cout( 'The %s command interpreter is:\n\t"%s"' % (loginName, shell) )
        print

    mf.StopWatchStop()

