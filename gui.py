# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed Apr 10 16:15:24 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1027, 543)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 191, 501))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.listPorts = QtGui.QListWidget(self.groupBox)
        self.listPorts.setGeometry(QtCore.QRect(10, 20, 171, 471))
        self.listPorts.setObjectName(_fromUtf8("listPorts"))
        item = QtGui.QListWidgetItem()
        self.listPorts.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listPorts.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listPorts.addItem(item)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(210, 10, 131, 501))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 20, 111, 131))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.radioEven = QtGui.QRadioButton(self.groupBox_3)
        self.radioEven.setGeometry(QtCore.QRect(10, 20, 116, 22))
        self.radioEven.setObjectName(_fromUtf8("radioEven"))
        self.radioOdd = QtGui.QRadioButton(self.groupBox_3)
        self.radioOdd.setGeometry(QtCore.QRect(10, 40, 116, 22))
        self.radioOdd.setObjectName(_fromUtf8("radioOdd"))
        self.radioMark = QtGui.QRadioButton(self.groupBox_3)
        self.radioMark.setGeometry(QtCore.QRect(10, 60, 116, 22))
        self.radioMark.setObjectName(_fromUtf8("radioMark"))
        self.radioNone = QtGui.QRadioButton(self.groupBox_3)
        self.radioNone.setGeometry(QtCore.QRect(10, 100, 116, 22))
        self.radioNone.setObjectName(_fromUtf8("radioNone"))
        self.radioSpace = QtGui.QRadioButton(self.groupBox_3)
        self.radioSpace.setGeometry(QtCore.QRect(10, 80, 116, 22))
        self.radioSpace.setObjectName(_fromUtf8("radioSpace"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 160, 111, 91))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.radio1 = QtGui.QRadioButton(self.groupBox_4)
        self.radio1.setGeometry(QtCore.QRect(10, 20, 116, 22))
        self.radio1.setObjectName(_fromUtf8("radio1"))
        self.radio15 = QtGui.QRadioButton(self.groupBox_4)
        self.radio15.setGeometry(QtCore.QRect(10, 40, 116, 22))
        self.radio15.setObjectName(_fromUtf8("radio15"))
        self.radio2 = QtGui.QRadioButton(self.groupBox_4)
        self.radio2.setGeometry(QtCore.QRect(10, 60, 116, 22))
        self.radio2.setObjectName(_fromUtf8("radio2"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 260, 111, 111))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.radio5 = QtGui.QRadioButton(self.groupBox_5)
        self.radio5.setGeometry(QtCore.QRect(10, 20, 116, 22))
        self.radio5.setObjectName(_fromUtf8("radio5"))
        self.radio6 = QtGui.QRadioButton(self.groupBox_5)
        self.radio6.setGeometry(QtCore.QRect(10, 40, 116, 22))
        self.radio6.setObjectName(_fromUtf8("radio6"))
        self.radio7 = QtGui.QRadioButton(self.groupBox_5)
        self.radio7.setGeometry(QtCore.QRect(10, 60, 116, 22))
        self.radio7.setObjectName(_fromUtf8("radio7"))
        self.radio8 = QtGui.QRadioButton(self.groupBox_5)
        self.radio8.setGeometry(QtCore.QRect(10, 80, 116, 22))
        self.radio8.setObjectName(_fromUtf8("radio8"))
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 380, 111, 51))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.comboBaudRate = QtGui.QComboBox(self.groupBox_8)
        self.comboBaudRate.setGeometry(QtCore.QRect(10, 19, 91, 22))
        self.comboBaudRate.setObjectName(_fromUtf8("comboBaudRate"))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.comboBaudRate.addItem(_fromUtf8(""))
        self.groupBox_10 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 440, 111, 51))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.textName = QtGui.QLineEdit(self.groupBox_10)
        self.textName.setGeometry(QtCore.QRect(10, 20, 91, 20))
        self.textName.setObjectName(_fromUtf8("textName"))
        self.groupBox_6 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(350, 10, 661, 501))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 20, 161, 471))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.listNodes = QtGui.QListWidget(self.groupBox_7)
        self.listNodes.setGeometry(QtCore.QRect(10, 20, 141, 291))
        self.listNodes.setObjectName(_fromUtf8("listNodes"))
        item = QtGui.QListWidgetItem()
        self.listNodes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listNodes.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listNodes.addItem(item)
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 320, 141, 81))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.textSend = QtGui.QLineEdit(self.groupBox_9)
        self.textSend.setGeometry(QtCore.QRect(10, 20, 121, 20))
        self.textSend.setObjectName(_fromUtf8("textSend"))
        self.btnSend = QtGui.QPushButton(self.groupBox_9)
        self.btnSend.setGeometry(QtCore.QRect(10, 50, 121, 23))
        self.btnSend.setObjectName(_fromUtf8("btnSend"))
        self.groupBox_14 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_14.setGeometry(QtCore.QRect(10, 410, 141, 51))
        self.groupBox_14.setObjectName(_fromUtf8("groupBox_14"))
        self.btnSendImage = QtGui.QPushButton(self.groupBox_14)
        self.btnSendImage.setGeometry(QtCore.QRect(10, 20, 121, 23))
        self.btnSendImage.setObjectName(_fromUtf8("btnSendImage"))
        self.groupBox_11 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_11.setGeometry(QtCore.QRect(180, 20, 471, 151))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.listSentData = QtGui.QListWidget(self.groupBox_11)
        self.listSentData.setGeometry(QtCore.QRect(10, 20, 451, 121))
        self.listSentData.setWordWrap(True)
        self.listSentData.setObjectName(_fromUtf8("listSentData"))
        item = QtGui.QListWidgetItem()
        self.listSentData.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listSentData.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listSentData.addItem(item)
        self.groupBox_12 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_12.setGeometry(QtCore.QRect(180, 180, 471, 151))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.listReceivedData = QtGui.QListWidget(self.groupBox_12)
        self.listReceivedData.setGeometry(QtCore.QRect(10, 20, 451, 121))
        self.listReceivedData.setObjectName(_fromUtf8("listReceivedData"))
        item = QtGui.QListWidgetItem()
        self.listReceivedData.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listReceivedData.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listReceivedData.addItem(item)
        self.groupBox_13 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_13.setGeometry(QtCore.QRect(180, 340, 471, 151))
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.listRelayedData = QtGui.QListWidget(self.groupBox_13)
        self.listRelayedData.setGeometry(QtCore.QRect(10, 20, 451, 121))
        self.listRelayedData.setObjectName(_fromUtf8("listRelayedData"))
        item = QtGui.QListWidgetItem()
        self.listRelayedData.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listRelayedData.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listRelayedData.addItem(item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBaudRate.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Network Testing Application", None))
        self.groupBox.setTitle(_translate("MainWindow", "Port Selection", None))
        __sortingEnabled = self.listPorts.isSortingEnabled()
        self.listPorts.setSortingEnabled(False)
        item = self.listPorts.item(0)
        item.setText(_translate("MainWindow", "USB01", None))
        item = self.listPorts.item(1)
        item.setText(_translate("MainWindow", "USB02", None))
        item = self.listPorts.item(2)
        item.setText(_translate("MainWindow", "USB03", None))
        self.listPorts.setSortingEnabled(__sortingEnabled)
        self.groupBox_2.setTitle(_translate("MainWindow", "Network Settings", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Parity", None))
        self.radioEven.setText(_translate("MainWindow", "Even", None))
        self.radioOdd.setText(_translate("MainWindow", "Odd", None))
        self.radioMark.setText(_translate("MainWindow", "Mark", None))
        self.radioNone.setText(_translate("MainWindow", "None", None))
        self.radioSpace.setText(_translate("MainWindow", "Space", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Stop Bits", None))
        self.radio1.setText(_translate("MainWindow", "1", None))
        self.radio15.setText(_translate("MainWindow", "1.5", None))
        self.radio2.setText(_translate("MainWindow", "2", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Byte Size", None))
        self.radio5.setText(_translate("MainWindow", "5", None))
        self.radio6.setText(_translate("MainWindow", "6", None))
        self.radio7.setText(_translate("MainWindow", "7", None))
        self.radio8.setText(_translate("MainWindow", "8", None))
        self.groupBox_8.setTitle(_translate("MainWindow", "Baud Rate", None))
        self.comboBaudRate.setItemText(0, _translate("MainWindow", "50", None))
        self.comboBaudRate.setItemText(1, _translate("MainWindow", "75", None))
        self.comboBaudRate.setItemText(2, _translate("MainWindow", "110", None))
        self.comboBaudRate.setItemText(3, _translate("MainWindow", "134", None))
        self.comboBaudRate.setItemText(4, _translate("MainWindow", "150", None))
        self.comboBaudRate.setItemText(5, _translate("MainWindow", "200", None))
        self.comboBaudRate.setItemText(6, _translate("MainWindow", "300", None))
        self.comboBaudRate.setItemText(7, _translate("MainWindow", "600", None))
        self.comboBaudRate.setItemText(8, _translate("MainWindow", "1200", None))
        self.comboBaudRate.setItemText(9, _translate("MainWindow", "1800", None))
        self.comboBaudRate.setItemText(10, _translate("MainWindow", "2400", None))
        self.comboBaudRate.setItemText(11, _translate("MainWindow", "4800", None))
        self.comboBaudRate.setItemText(12, _translate("MainWindow", "9600", None))
        self.comboBaudRate.setItemText(13, _translate("MainWindow", "19200", None))
        self.comboBaudRate.setItemText(14, _translate("MainWindow", "38400", None))
        self.comboBaudRate.setItemText(15, _translate("MainWindow", "57600", None))
        self.comboBaudRate.setItemText(16, _translate("MainWindow", "115200", None))
        self.groupBox_10.setTitle(_translate("MainWindow", "Node Name", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Network", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Nodes in Range", None))
        __sortingEnabled = self.listNodes.isSortingEnabled()
        self.listNodes.setSortingEnabled(False)
        item = self.listNodes.item(0)
        item.setText(_translate("MainWindow", "A", None))
        item = self.listNodes.item(1)
        item.setText(_translate("MainWindow", "C", None))
        item = self.listNodes.item(2)
        item.setText(_translate("MainWindow", "D", None))
        self.listNodes.setSortingEnabled(__sortingEnabled)
        self.groupBox_9.setTitle(_translate("MainWindow", "Send Text", None))
        self.btnSend.setText(_translate("MainWindow", "Send to Node", None))
        self.groupBox_14.setTitle(_translate("MainWindow", "Send Image", None))
        self.btnSendImage.setText(_translate("MainWindow", "Select Image", None))
        self.groupBox_11.setTitle(_translate("MainWindow", "Sent Data", None))
        __sortingEnabled = self.listSentData.isSortingEnabled()
        self.listSentData.setSortingEnabled(False)
        item = self.listSentData.item(0)
        item.setText(_translate("MainWindow", "A", None))
        item = self.listSentData.item(1)
        item.setText(_translate("MainWindow", "C", None))
        item = self.listSentData.item(2)
        item.setText(_translate("MainWindow", "D", None))
        self.listSentData.setSortingEnabled(__sortingEnabled)
        self.groupBox_12.setTitle(_translate("MainWindow", "Received Data", None))
        __sortingEnabled = self.listReceivedData.isSortingEnabled()
        self.listReceivedData.setSortingEnabled(False)
        item = self.listReceivedData.item(0)
        item.setText(_translate("MainWindow", "A", None))
        item = self.listReceivedData.item(1)
        item.setText(_translate("MainWindow", "C", None))
        item = self.listReceivedData.item(2)
        item.setText(_translate("MainWindow", "D", None))
        self.listReceivedData.setSortingEnabled(__sortingEnabled)
        self.groupBox_13.setTitle(_translate("MainWindow", "Relayed Data", None))
        __sortingEnabled = self.listRelayedData.isSortingEnabled()
        self.listRelayedData.setSortingEnabled(False)
        item = self.listRelayedData.item(0)
        item.setText(_translate("MainWindow", "A", None))
        item = self.listRelayedData.item(1)
        item.setText(_translate("MainWindow", "C", None))
        item = self.listRelayedData.item(2)
        item.setText(_translate("MainWindow", "D", None))
        self.listRelayedData.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

