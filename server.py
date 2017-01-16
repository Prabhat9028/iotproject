#!/usr/bin/env python
# IMPORTS 
import socket

## SAMPLE SERVER PROGRAM
#s = socket.socket()
#host = '127.0.0.1'
#print(host)
#port = 12345
#s.bind((host,port))
#
#s.listen(5)
#while True:
#    c, addr = s.accept()
#    print "Got Connection from  ", addr
#    c.send("Thank You For Connecting")
#    c.close()

## -------------------------------------------------------------
## -> THEORY
#We need to create a thread that keeps listening to 
#new connections and stores it to array allConnections.
#
#Also provide with different methods to do various server
#related tasks such as sending messages, closing connections,
#mapping devices.
#
#Create manager to manage all the above task that works on
#seperate thread
## -------------------------------------------------------------

## CREATE CLASS OF SERVER 

class Serv:
    s = socket.socket()
    allConnections = [] # stores all connections in list of dict's
        
    def __init__(self,host = "127.0.0.1",port = 8787):
        self.host = host
        self.port = port 
        self.s.bind((host,port))
        
    
        
    ## Temporary function
    def printBind(self):
        print "SERVER Binded with host address of ",self.host," and on port no ",self.port
        
