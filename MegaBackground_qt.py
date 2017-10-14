#!/bin/env python

""" TODO
    Get rid of the dependency on the helper script
    A counter of how much data has been downloaded
"""

import os
import sys
import time

from PyQt5 import QtWidgets, QtGui, QtCore
import BackgrounderUI
import vpn_functions

if os.geteuid() != 0:
    print('I need root.')
    exit(1)


class Options:
    all_vpns = vpn_functions.all_vpns()
    vpn_countries = [i for i in all_vpns]
    vpn_countries.sort()
    update_needed = True


class MainUI(QtWidgets.QMainWindow, BackgrounderUI.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.setFixedSize(758, 123)
        window_icon = QtGui.QIcon(os.path.dirname(__file__) + '/mega.png')
        self.setWindowIcon(window_icon)

        # Associate all push buttons with their actions
        self.connectButton.clicked.connect(self.connect_vpn)
        self.incrementButton.clicked.connect(self.increment_vpn)
        self.disconnectButton.clicked.connect(self.disconnect_vpn)

        # Set a check timer to go off every 2000 ms
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.all_update)
        self.timer.start(2000)

        # Populate the combo boxes with the names of the vpns
        self.countryCode.addItems(Options.vpn_countries)
        self.countryCode.currentIndexChanged.connect(self.country_code)
        self.set_combobox_values()

    def set_combobox_values(self):
        current_vpn = vpn_functions.get_current_connection()
        if current_vpn:
            self.countryCode.setCurrentIndex(
                self.countryCode.findText(current_vpn[0][:2]))
            self.serverNumber.setCurrentIndex(
                self.serverNumber.findText(current_vpn[0][2:]))
        else:
            self.countryCode.setCurrentIndex(self.countryCode.findText('de'))
        self.all_update()

    def all_update(self):
        if not Options.update_needed:
            return

        current_vpn = vpn_functions.get_current_connection()
        try:
            data_limit = float(self.dataLimit.text())
        except ValueError:
            data_limit = 4.7
            self.statusbar.showMessage('Datalimit error. Setting to default.')
            self.dataLimit.setText('4.7')

        if current_vpn:
            Options.connected = True
            country = current_vpn[0][:2]
            server_code = current_vpn[0][2:]
            incoming_gbytes = current_vpn[1] * 1e-9

            if incoming_gbytes > data_limit:
                self.progressBar.setValue(100)
                self.increment_vpn()
                return

            percentage = incoming_gbytes * 100 / data_limit

            # Check to see which widget is highlighted
            self.statusbar.showMessage('Connected to: ' + country + server_code)
            self.progressBar.setValue(percentage)
            self.disconnectButton.setEnabled(True)
            self.incrementButton.setEnabled(True)
        else:
            # Do all of this when the vpn is disconnected
            self.progressBar.setValue(0)
            self.statusbar.showMessage('Not connected to a VPN')
            self.incrementButton.setEnabled(False)
            self.disconnectButton.setEnabled(False)
            return

    def connect_vpn(self):
        Options.update_needed = False
        desired_server = self.countryCode.currentText() + self.serverNumber.currentText()
        self.statusbar.showMessage(f'Connecting to {desired_server}')
        vpn_functions.helper_script_shenanigans(desired_server)
        Options.update_needed = True

    def disconnect_vpn(self):
        vpn_functions.helper_script_shenanigans(None)

    def increment_vpn(self):
        Options.update_needed = False
        self.incrementButton.setEnabled(False)
        self.statusbar.showMessage('Incrementing vpn...')
        vpn_functions.increment_connection()
        self.set_combobox_values()
        Options.update_needed = True

    def country_code(self):
        selected_country = self.countryCode.currentText()
        self.serverNumber.clear()
        self.serverNumber.addItems(Options.all_vpns[selected_country])

    def closeEvent(self, event):
        event.ignore()
        self.setHidden(True)


class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)

        self.menu = QtWidgets.QMenu(parent)
        exitAction = self.menu.addAction("Exit")
        exitAction.triggered.connect(QtWidgets.qApp.exit)
        self.setContextMenu(self.menu)
        self.activated.connect(self.clickety)

    def clickety(self, reason):
        if reason == 3:  # Single click
            if form.isHidden():
                form.setHidden(False)
            else:
                form.setHidden(True)


def main():
    global form, systray
    app = QtWidgets.QApplication(sys.argv)
    form = MainUI()
    window_icon = QtGui.QIcon(os.path.dirname(__file__) + '/mega.png')
    systray = SystemTrayIcon(window_icon)
    form.show()
    systray.show()
    app.exec_()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
