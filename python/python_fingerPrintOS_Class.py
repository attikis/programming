#!/usr/bin/env python

# Script docstrings
'''
Usage:
./fileName.py

Permissions: 
chmod +x fileName.py

Description:
This is an example class that can be used to fingerprint the OS type used by the user. It supports detection of Mac OS X, Ubuntu, Red Hat/Cent OS, FreeBSD and SunOS.
'''
import platform

class OpSysType(object):
    '''
    This class determines OS type using the platform module.
    '''

    def __getatt__(self, attr): #this seems to do nothing. something is wrong here
        if attr == "osx":
            return "osx"
        elif attr == "rhel":
            return "redhat"
        elif attr == "fbsd":
            return "FreeBSD"
        elif attr == "sun":
            return "SunOS"
        elif attr == "unknown_linux":
            return "unknown_linux"
        elif attr == "unknown":
            return "unknown"
        else:
            raise AttributeError, attr


    def linuxType(self):
        '''
        Uses various methods to determine the Linux Type
        '''

        if platform.dist()[0] == "rhel": #self.rhel:
            return "rhel" #return self.rhel
        elif platform.uname()[1] == "ubu": #self.ubu:
            return "ubu" #return self.ubu
        else:
            return "unknown_linux" #return self.unknown_linux
        
    def queryOS(self):
        if platform.system() == "Darwin":
            return "osx" # return self.osx
        elif platform.system() == "Linux":
            return self.linuxType()
        elif platform.system() == self.sun:
            return "SunOS" # return self.sun
        elif platform.system == self.fbsb:
            return "FreeBSD" # return self.fbsd
        else:
            return "Unknown platform"
