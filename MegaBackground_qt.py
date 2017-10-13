#!/bin/env python

import os
import sys
import time
import threading

from PyQt5 import QtWidgets, QtGui
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

        self.connectButton.clicked.connect(self.connect_vpn)
        self.incrementButton.clicked.connect(self.increment_vpn)
        self.disconnectButton.clicked.connect(self.disconnect_vpn)

        self.countryCode.addItems(Options.vpn_countries)
        self.countryCode.currentIndexChanged.connect(self.country_code)
        self.set_combobox_values()

    def set_combobox_values(self):
        # The server number needs to be set only once
        current_vpn = vpn_functions.get_current_connection()
        if current_vpn:
            self.countryCode.setCurrentIndex(self.countryCode.findText(current_vpn[0][:2]))
            self.serverNumber.setCurrentIndex(self.serverNumber.findText(current_vpn[0][2:]))
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


def updater():
    while True:
        form.all_update()
        time.sleep(2)


def main():
    global form
    app = QtWidgets.QApplication(sys.argv)
    form = MainUI()
    form.show()
    app.exec_()


if __name__ == '__main__':
    threading.Thread(target=main).start()
    time.sleep(1)
    # daemonizing the worker thread ensures it exits when the main (UI) thread does
    threading.Thread(target=updater, daemon=True).start()
