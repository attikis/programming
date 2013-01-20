#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is a 
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
import subprocess
import os
import time
import sys

if __name__ == "__main__":
    mf.StopWatchStart()
    
    # Get cwd so that you can go pack once screen is launched
    cwd = os.getcwd()

    # Choose a command that takes some time to execute. Use random ip address
    cmd1 = "screen"
    #p1 = subprocess.call(cmd1, shell = True)
    
    # Go back to the previous working directory (screen launches at home)
    os.chdir(cwd)

    ### GNU Screen: -d option. "screen -d CommandToLaunch" does not start screen, but detaches the elsewhere running screen session. It has the same effect as typing 
    # "C-a d" from screen's controlling  terminal.

    ### GNU Screen: -m option. "screen -d CommandToLaunch" causes  screen  to ignore the $STY environment variable. With "screen -m" creation of a new session is 
    # enforced, regardless whether screen is called from within another screen session or not. This flag has a special meaning in connection with the `-d' option 
    # (i.e. screen -d -m)  which starts screen in "detached" mode. This creates a new session but doesn't attach to it. This is useful for system startup scripts.

    ### GNU Screen: -S option. "screen -S CommandName CommandToLaunch" means the CommandName (-S) can be used  for creating  a  new  session. This option can be used to
    # specify a meaningful name for the session. This name identifies the session for "screen -list" and "screen -r" actions. It substitutes the default [tty.host] suffix.
    cmd1 = "screen -dmS p1 ping -c 6 10.00.0.1"
    cmd2 = "screen -r p1"
    
    mf.CmdPipe(cmd1)
    reAttach = mf.Cin('To re-attach session press "y"')
    if reAttach == "y":
        mf.Cout('Re-attaching session:\n\t"%s"' % (cmd2))
        mf.Cout('Press "Ctr-A" "Ctrl-D" at any point to detach session')
        overwrite = 0
        for sec in range(3,0,-1):
            sys.stdout.write("%s seconds%s\r" % (sec, " "*overwrite ))
            sys.stdout.flush()
            time.sleep(1)
            overwrite = len("seconds")
        
        mf.CmdPipe(cmd2)
    else:
        mf.Cout('To re-attach at any time type:\n\t"screen -r session_name"')
    

    mf.StopWatchStop()