#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is an example which introduces the processing module. It basically involves creating 10 processes, adding them to a Queue and starting them. Each process is forced to 
sleep for a number of seconds corresponding to its assigned label. Once the waiting is over the process ends. In summary, all this program does is tell each process to sleep 
as long as the number of the process.


Help:
If this module is not available, install it by typing:
|\> sudo easy_install processing
'''

# Import my own modules here
import python_myFunctions as myFunctions
mf = myFunctions.CreateObject()

# All other required modules here
from processing import Process, Queue
import time

def f(queue):
    x = queue.get()
    mf.Cout("Process number %s, sleeps for %s seconds" % (x,x))
    time.sleep(x)
    mf.Cout("Process number %s finished" % (x))
    
if __name__ == "__main__":
    mf.StopWatchStart()
    # Create a queue object 
    queue = Queue()
    # Create 10 processes
    for i in range(10):
        # Put an item into the queue. 10 queues in total
        queue.put(i)
        # Declare the process
        mf.Cout("Creating process #%s" % (i))
        i = Process(target = f, args=[queue]) #for a Thread: threading.Thread(target = f, args=(queue)) => Similar structure
        # Start the process
        i.start()

    mf.Cout("Main process joins on queue")
    # Block process until all items in the Queue have been gotten and processed
    i.join()
    mf.Cout("Main program finished")

    mf.StopWatchStop()
