"""
Network Testing Application

This application allows for the sending and retrieval of data across a network
which uses serial ports on multiple machines. It adopts its own protocol and 
allows for text to be sent from one machine to another.

Author: Nick Klose (nick.klose@ualberta.ca)
http://ualberta.ca/~klose
"""
import serial
import threading
import os, sys
import time

class SerialListen(threading.Thread):
    def __init__(self, parent):
        super(SerialListen, self).__init__()
        self._stop = threading.Event()
        
        self.serial = parent.serial # take control of parent's serial connection
        self.ui = parent.ui # enable parent UI updating
        self.input = "" # the string being read from the serial
        self.name = parent.name # save parent name to check if messages are for us
        self.sender = "" # save sender name from serial
        self.recipient = "" # save recipient name from serial
        self.pinger = "" # name of node having sent most recent ping
        self.text = "" # save text message from sender
        self.parent = parent
        self.queue = parent.queue
        self.nodes = parent.nodes
        self.pastNodes = [] # nodes which were detected during the last ping
        
    def run(self):
        while self.serial != None:
            c = self.serial.read()
            self.input += c
            
            # reset buffer if a new command is sent
            if self.input[-1:] == "{":
                self.input = "{"
                
            # end buffer if command close character is sent
            if self.input[-1:] == "}":
                if self.input[:6] == "{NAME=":
                    pinger = self.input[6:-1]
                    self.pinger = pinger
                    if pinger not in self.nodes:
                        self.nodes.append(pinger)
                    self.update_nodes_in_range()
                elif self.input[:6] == "{FROM=":
                    self.sender = self.input[6:-1]
                elif self.input[:4] == "{TO=":
                    self.recipient = self.input[4:-1]
                elif self.input[:6] == "{TEXT=":
                    self.text = self.input[6:-1]
                    
                    # the recipient is this node
                    if self.recipient == self.name:
                        message = "<From: " + self.sender + "> " + self.text
                        self.ui.listReceivedData.addItem(message)
                    # the recipient is another node, so relay the message
                    else:
                        #self.parent.send(self.sender, self.recipient, self.text)
                        message = "<From: " + self.sender + "> <To: "
                        message += self.recipient + "> " + self.text
                        self.ui.listRelayedData.addItem(message)
                    
            # send any queued messages
            for message in self.queue:
                self.serial.write(message)
                del message
        
    def update_nodes_in_range(self):
        self.ui.listNodes.clear()
        for node in self.pastNodes:
            self.ui.listNodes.addItem(node)
        self.pastNodes = self.nodes
        self.nodes = []
    
    def stop(self):
        self._stop.set()