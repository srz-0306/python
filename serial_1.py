# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serial_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1390, 671)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 80, 101, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 80, 51, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 71, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(104, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(104, 240, 101, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(104, 300, 101, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(104, 360, 101, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(360, 60, 331, 371))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 440, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(220, 240, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(220, 360, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(220, 300, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 430, 101, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(220, 430, 111, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(730, 60, 111, 371))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(750, 440, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(900, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(900, 180, 111, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(930, 90, 51, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(930, 220, 71, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(900, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(1050, 50, 256, 371))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1150, 430, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(910, 480, 101, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(1050, 480, 261, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_5.sizePolicy().hasHeightForWidth())
        self.textEdit_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setObjectName("textEdit_5")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(910, 550, 101, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1390, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.activated['QString'].connect(MainWindow.port_change1) # type: ignore
        self.comboBox_2.activated['QString'].connect(MainWindow.baud_change1) # type: ignore
        self.pushButton.clicked.connect(MainWindow.connect_btu1) # type: ignore
        self.pushButton_2.clicked.connect(MainWindow.set_dir) # type: ignore
        self.pushButton_3.clicked.connect(MainWindow.set_speed) # type: ignore
        self.pushButton_4.clicked.connect(MainWindow.set_step) # type: ignore
        self.pushButton_5.clicked.connect(MainWindow.set_air) # type: ignore
        self.comboBox_3.activated['QString'].connect(MainWindow.port_change2) # type: ignore
        self.comboBox_4.activated['QString'].connect(MainWindow.baud_change2) # type: ignore
        self.pushButton_6.clicked.connect(MainWindow.connect_btu2) # type: ignore
        self.pushButton_7.clicked.connect(MainWindow.set_sensor) # type: ignore
        self.pushButton_8.clicked.connect(MainWindow.set_auto) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "9600"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "19200"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "38400"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "115200"))
        self.label.setText(_translate("MainWindow", "串口1"))
        self.label_2.setText(_translate("MainWindow", "波特率1"))
        self.pushButton.setText(_translate("MainWindow", "连接1"))
        self.pushButton_2.setText(_translate("MainWindow", "设置方向"))
        self.pushButton_3.setText(_translate("MainWindow", "设置速度"))
        self.pushButton_4.setText(_translate("MainWindow", "设置距离"))
        self.label_3.setText(_translate("MainWindow", "接收显示"))
        self.pushButton_5.setText(_translate("MainWindow", "设置气压"))
        self.label_4.setText(_translate("MainWindow", "气压显示"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "9600"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "19200"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "38400"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "115200"))
        self.label_5.setText(_translate("MainWindow", "串口2"))
        self.label_6.setText(_translate("MainWindow", "波特率2"))
        self.pushButton_6.setText(_translate("MainWindow", "连接2"))
        self.label_7.setText(_translate("MainWindow", "力传感器"))
        self.pushButton_7.setText(_translate("MainWindow", "设置传感器"))
        self.pushButton_8.setText(_translate("MainWindow", "自动"))
