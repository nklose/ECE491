"""
Network Testing Application

This application allows for the sending and retrieval of data across a network
which uses serial ports on multiple machines. It adopts its own protocol and 
allows for text to be sent from one machine to another.

Author: Nick Klose (nick.klose@ualberta.ca)
http://ualberta.ca/~klose
"""
import time
import serial
import platform
import glob
import random
import threading
import os, sys
from PyQt4 import QtCore, QtGui
from serial_listen import SerialListen
from gui import Ui_MainWindow
from PIL import Image

# Default connection parameters
PORT = None
BAUD_RATE = 9600
PARITY = serial.PARITY_EVEN
STOP_BITS = serial.STOPBITS_TWO
BYTE_SIZE = serial.EIGHTBITS
NODE_NAME = None

class NetworkTest(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setFixedSize(self.size()) # disable resizing
        
        self.serial = None # serial object with configs
        self.ports = [] # list of open ports
        self.name = NODE_NAME # name of this node
        self.node = None # name of node to send to
        self.input = "" # text input from another device
        self.nodes = [] # nodes in range of this one
        self.oldNodes = []
        self.thread = None # thread for listening to the network
        self.queue = [] # queue of messages to send when possible
        
        self.port = PORT
        self.baud = BAUD_RATE
        self.parity = PARITY
        self.stopBits = STOP_BITS
        self.byteSize = BYTE_SIZE
        
        self.initialize() # initialize the interface
        
        # QT signals used
        clicked = QtCore.SIGNAL("clicked()")
        toggled = QtCore.SIGNAL("toggled(bool)")
        itemClicked = QtCore.SIGNAL("itemClicked(QListWidgetItem *)")
        indexChanged = QtCore.SIGNAL("currentIndexChanged(const QString&)")
        textChanged = QtCore.SIGNAL("textChanged(const QString&)")
        returnPressed = QtCore.SIGNAL("returnPressed()")
        
        # list widget connections
        QtCore.QObject.connect(self.ui.listPorts, itemClicked, self.select_port)
        QtCore.QObject.connect(self.ui.listNodes, itemClicked, self.select_node)
        
        # radio button connections
        QtCore.QObject.connect(self.ui.radioEven, toggled, self.select_parity)
        QtCore.QObject.connect(self.ui.radioOdd, toggled, self.select_parity)
        QtCore.QObject.connect(self.ui.radioMark, toggled, self.select_parity)
        QtCore.QObject.connect(self.ui.radioSpace, toggled, self.select_parity)
        QtCore.QObject.connect(self.ui.radioNone, toggled, self.select_parity)
        
        QtCore.QObject.connect(self.ui.radio1, toggled, self.select_stop_bits)
        QtCore.QObject.connect(self.ui.radio15, toggled, self.select_stop_bits)
        QtCore.QObject.connect(self.ui.radio2, toggled, self.select_stop_bits)
        
        QtCore.QObject.connect(self.ui.radio5, toggled, self.select_byte_size)
        QtCore.QObject.connect(self.ui.radio6, toggled, self.select_byte_size)
        QtCore.QObject.connect(self.ui.radio7, toggled, self.select_byte_size)
        QtCore.QObject.connect(self.ui.radio8, toggled, self.select_byte_size)
        
        # combo box connections
        QtCore.QObject.connect(self.ui.comboBaudRate, indexChanged, self.select_baud)
       
        # line edit connections
        QtCore.QObject.connect(self.ui.textName, textChanged, self.change_name)
        QtCore.QObject.connect(self.ui.textSend, returnPressed, self.send_text)
        
        # button connections
        QtCore.QObject.connect(self.ui.btnSend, clicked, self.send_text)
        QtCore.QObject.connect(self.ui.btnSendImage, clicked, self.send_image)
    
    def refresh(self):
        if self.thread != None:
            self.thread.stop()
        if self.serial != None:
            if self.serial.isOpen():
                self.serial.close()
                self.update_serial()
        self.thread = SerialListen(self)
        self.thread.start()
                
    def initialize(self):
        self.msg("Initializing...")
        
        self.ui.listPorts.clear()
        self.ports = self.list_ports()
        for port in self.ports:
            self.ui.listPorts.addItem(str(port))
        
        # Set default baud rate
        self.select_baud(BAUD_RATE)
        
        # Set default parity
        if PARITY == serial.PARITY_NONE:
            self.ui.radioNone.setChecked(True)
        elif PARITY == serial.PARITY_ODD:
            self.ui.radioOdd.setChecked(True)
        elif PARITY == serial.PARITY_MARK:
            self.ui.radioMark.setChecked(True)
        elif PARITY == serial.PARITY_SPACE:
            self.ui.radioSpace.setChecked(True)
        else:
            self.ui.radioEven.setChecked(True)
            self.parity = serial.PARITY_EVEN
        
        # Set default stop bits
        if float(STOP_BITS) == 1.0:
            self.ui.radio1.setChecked(True)
        elif float(STOP_BITS) == 1.5:
            self.ui.radio15.setChecked(True)
        else:
            self.stopBits = 2
            self.ui.radio2.setChecked(True)
        
        # Set default byte size
        if BYTE_SIZE == 5:
            self.ui.radio5.setChecked(True)
        elif BYTE_SIZE == 6:
            self.ui.radio6.setChecked(True)
        elif BYTE_SIZE == 7:
            self.ui.radio7.setChecked(True)
        else:
            self.ui.radio8.setChecked(True)
            self.byteSize = 8
        
        # Set default name
        self.change_name(self.random_name())
        
        # Clear list widgets
        self.ui.listNodes.clear()
        self.ui.listSentData.clear()
        self.ui.listReceivedData.clear()
        self.ui.listRelayedData.clear()
        
        
        self.msg("Initialized.")
    
    def send_ping(self):
        threading.Timer(5.0, self.send_ping).start()
        self.serial.write("{NAME=" + self.name + "}")
        self.oldNodes = self.nodes
        self.nodes = []
        
    def select_port(self, item):
        self.msg("Selecting new port: " + str(item.text()))
        self.port = int(item.text()[3:])
        self.update_serial()
        self.refresh()
        
    def select_node(self, item):
        self.msg("Selecting new node: " + str(item.text()))
        self.node = str(item.text())
        
    def select_parity(self, button):
        self.msg("Selecting new parity.")
        if self.ui.radioEven.isChecked():
            self.parity = serial.PARITY_EVEN
        elif self.ui.radioOdd.isChecked():
            self.parity = serial.PARITY_ODD
        elif self.ui.radioMark.isChecked():
            self.parity = serial.PARITY_MARK
        elif self.ui.radioSpace.isChecked():
            self.parity = serial.PARITY_SPACE
        else:
            selfparity = serial.PARITY_NONE
        
        
    def select_stop_bits(self, button):
        self.msg("Selecting new stop bits.")
        if self.ui.radio1.isChecked():
            self.stopBits = serial.STOPBITS_ONE
        elif self.ui.radio15.isChecked():
            self.stopBits = serial.STOPBITS_ONE_POINT_FIVE
        else:
            self.stopBits = serial.STOPBITS_TWO
            
        
    def select_byte_size(self, button):
        self.msg("Selecting new byte size.")
        if self.ui.radio5.isChecked():
            self.byteSize = serial.FIVEBITS
        elif self.ui.radio6.isChecked():
            self.byteSize = serial.SIXBITS
        elif self.ui.radio7.isChecked():
            self.byteSize = serial.SEVENBITS
        else:
            self.byteSize = serial.EIGHTBITS
            
        self.refresh()
    
    def select_baud(self, baud):
        self.msg("Selecting new baud rate: " + str(baud))
        index = self.ui.comboBaudRate.findText(str(baud))
        self.baud = self.ui.comboBaudRate.itemText(index)
        self.ui.comboBaudRate.setCurrentIndex(index)
        
        self.refresh()
        
    def change_name(self, name):
        self.msg("Changing this node's name to " + str(name))
        self.ui.textName.setText(name)
        self.name = name
        
    def send_text(self):
        if str(self.ui.textSend.text()) != "" and self.node != None:
            self.msg("Sending text: " + str(self.ui.textSend.text()))
            self.send(self.name, self.node, self.ui.textSend.text())
            self.ui.textSend.clear()
        elif self.node == None:
            self.msg("You must select a node to send this message.")
        else:
            self.msg("No text entered.")
     
    def send_image(self):
        image = str(QtGui.QFileDialog.getOpenFileName())
        imageStr = Image.open(image).tostring()
        self.serial.write(imageStr)
     
    # Sends a message with a specified sender and recipient
    def send(self, sender, recipient, text):
        message = "{FROM=" + sender + "}{TO=" + recipient + "}{TEXT=" + text + "}"
        #self.queue.append(message)
        self.serial.write(message)
        if sender == self.name:
            self.ui.listSentData.addItem("<To: " + recipient + "> " + text)
        
    # Prints a message to the user via the status bar.
    def msg(self, text):
        self.ui.statusbar.showMessage(str(text))

    def list_ports(self):
        ports = None
        if platform.system() == "Windows":
            ports = []
            for i in range(256):
                try:
                    s = serial.Serial(i)
                    ports.append("USB" + str("%03d" % (i,)))
                    s.close()
                except serial.SerialException:
                    pass
        else:
            ports = glob.glob("/dev/ttyS*") + glob.glob("/dev/ttyUSB*")
        return ports
        
    # Generates a random name for this node.
    def random_name(self):
        names = ["Donut", "Penguin", "Stumpy", "Whicker", "Howard",
                 "Wilshire", "Disco", "Jack", "Bear", "Sneak", "Wisp",
                 "Crazy", "Goat", "Pirate", "Hambone", "Walla", "Snake",
                 "Caboose", "Sleepy", "Stompy", "Mopey", "Dopey", "Weasel",
                 "Ghost", "Dasher", "Grumpy", "Hollywood", "Noodle", "Cupid",
                 "Abraham", "Prancer", "Blinky", "Bonobo", "Banana", "Cinnabon"]
                 
        rand = random.randint(0, len(names) - 1)
        return names[rand]
    
    def update_serial(self):
        try:
            #self.serial = serial.Serial(self.port, self.baud, self.byteSize, 
            #                            self.parity, self.stopBits)
            if self.thread != None:
                self.thread.stop()
                self.thread = None
            if self.serial != None:
                if self.serial.isOpen():
                    self.serial.close()
                    self.serial = None
                    
            self.serial = serial.Serial(self.port)
            self.send_ping()
        except Exception as e:
            self.msg("Serial already initialized, " + str(e))
           
# call main function
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    nt = NetworkTest()
    nt.show()
    sys.exit(app.exec_())
