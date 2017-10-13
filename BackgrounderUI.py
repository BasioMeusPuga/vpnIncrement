# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Background.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(758, 123)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.countryCode = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.countryCode.sizePolicy().hasHeightForWidth())
        self.countryCode.setSizePolicy(sizePolicy)
        self.countryCode.setObjectName("countryCode")
        self.horizontalLayout.addWidget(self.countryCode)
        self.serverNumber = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serverNumber.sizePolicy().hasHeightForWidth())
        self.serverNumber.setSizePolicy(sizePolicy)
        self.serverNumber.setObjectName("serverNumber")
        self.horizontalLayout.addWidget(self.serverNumber)
        self.dataLimit = QtWidgets.QLineEdit(self.centralwidget)
        self.dataLimit.setToolTipDuration(1500)
        self.dataLimit.setAlignment(QtCore.Qt.AlignCenter)
        self.dataLimit.setPlaceholderText("")
        self.dataLimit.setObjectName("dataLimit")
        self.horizontalLayout.addWidget(self.dataLimit)
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy)
        self.connectButton.setToolTip("")
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout.addWidget(self.connectButton)
        self.disconnectButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disconnectButton.sizePolicy().hasHeightForWidth())
        self.disconnectButton.setSizePolicy(sizePolicy)
        self.disconnectButton.setObjectName("disconnectButton")
        self.horizontalLayout.addWidget(self.disconnectButton)
        self.incrementButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.incrementButton.sizePolicy().hasHeightForWidth())
        self.incrementButton.setSizePolicy(sizePolicy)
        self.incrementButton.setObjectName("incrementButton")
        self.horizontalLayout.addWidget(self.incrementButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mega VPN Incrementer - NordVPN"))
        self.dataLimit.setToolTip(_translate("MainWindow", "Data Limit (GB)"))
        self.dataLimit.setText(_translate("MainWindow", "4.7"))
        self.connectButton.setText(_translate("MainWindow", "(re)Connect"))
        self.disconnectButton.setText(_translate("MainWindow", "Disconnect"))
        self.incrementButton.setToolTip(_translate("MainWindow", "Increment VPN"))
        self.incrementButton.setText(_translate("MainWindow", "Increment"))

