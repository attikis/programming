#!/usr/bin/env python
#To launch: python fileName.py

class Server(object):
    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname
    def set_ip (self, hostname):
        self.ip = ip
    def set_hostname(self, hostname):
        self.hostname = hostname
    def ping (self, ip_address):
        print "+++ Pinging %s from %s (%s)" % (ip_address, self.ip, self.hostname)

if __name__ == '__main__':
    server = Server('10.0.1.2', 'alexandros')
    server.ping('10.0.1.2')
