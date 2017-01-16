#!/usr/bin/env python
# IMPORTS 
import socket
import threading
import time

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
    listen = False
        
    ## CONSTRUCTOR
    def __init__(self,host = "127.0.0.1",port = 8787):
        print "Initializing Server"
        self.host = host
        self.port = port 
        self.s.bind((host,port))
        self.t = threading.Thread(target=self.listenForConnection)

    def listenForConnection(self):
        print "Listening on port ", self.port
        self.s.listen(5)
        while self.listen:
            c, addr = self.s.accept()
            name = c.recv(1024)
            self.allConnections.append({'conn':c, 'addr': addr, 'name': name})
            print "Got Connection from ",addr

    def beginListening(self):
        self.listen = True
        self.t.start()

    ## DESTRUCTOR
    def destroy(self):
        self.listen = False
        ## create a dummy connection
        ## and connect to server
        self.term = socket.socket()
        self.term.connect((self.host,self.port))
        self.term.close()
        self.s.close()

        
    ## Temporary function
    def displayConn(self):
        print self.allConnections

        
if __name__ == "__main__":
    serv = Serv()
    # the following code gets stuck into listen method
    # while i want to keep listening and return ctrl to main
    serv.beginListening()
    time.sleep(30)
    serv.displayConn()
    serv.destroy()
    exit()
