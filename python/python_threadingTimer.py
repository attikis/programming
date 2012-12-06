#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is simple illustration of how to run a timed execution of a function insed of a thread, by using threading. It take a single argument when executing, which is the
time delay of the thread.

Usage:
python_threadingTimer.py delay_time_in_seconds

Example:
python_threadingTimer.py 5

[attikis:python]> python python_threadingTimer.py 3
Out[1] Waiting 3 seconds to run function
Out[2] Main program is still running for 3 more seconds.
Out[3] Main program is still running for 2 more seconds.
Out[4] Main program is still running for 1 more seconds.
Out[5] Hello, I just got called after a 3 second delay
Out[6] Done! Script Execution time:
	0 days, 0 hours, 0 minutes, 3.0 seconds.
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
from threading import Timer
import sys
import time
import copy

# Define a simple function to run
def hello():
    mf.Cout("Hello, I just got called after a %s second delay" % call_time)

if __name__ == "__main__":
    mf.StopWatchStart()
    
    if len(sys.argv) != 2:
        mf.Cout("ERROR! Must enter a time interval as script argument. Printing docstrings. Exiting python shell.")
        print __doc__
        sys.exit(1)
    else:
        # Get the user-defined delay time (in seconds)
        delay = sys.argv[1] #remember. sys.argv[0] is the script name
        # Copy the delay to use later on
        call_time = copy.copy(delay)
        # Define the thread you want
        t = Timer(int(delay), hello)
        # Start threading
        t.start()

        # Validate that we are not blocked, and that the main program continues.
        mf.Cout("Waiting %s seconds to run function" % (delay))
        for x in range(int(delay)):
            mf.Cout("Main program is still running for %s more seconds." % (delay))
            delay = int(delay)-1
            time.sleep(1)

            
        mf.StopWatchStop()
