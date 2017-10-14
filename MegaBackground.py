#!/usr/bin/env python

import os
import time
import progressbar

import vpn_functions

if os.geteuid() != 0:
    print('I need root.')
    exit(1)

# Options
vpn_interface = 'tun0'
data_limit = 4.7  # GB


class Colors:
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    ENDC = '\033[0m'


def check_proc():
    with open('/proc/net/dev', 'r') as datafile:
        for i in datafile:
            if i.strip().startswith(vpn_interface):
                incoming_bytes = int(i.split()[1])
                return incoming_bytes


current_connection = vpn_functions.get_current_connection()
if current_connection:
    print(' ' + Colors.CYAN + current_connection[0] + Colors.ENDC)

pbar = progressbar.ProgressBar(
    maxval=data_limit,
    widgets=[
        progressbar.Bar('=', '[', ']'),
        ' ', progressbar.Percentage(),
        ' ', progressbar.AdaptiveETA()])

while True:
    try:
        total_incoming = check_proc() * 1e-9
        pbar.update(total_incoming)
        time.sleep(1)

    except ValueError:
        # Triggered on total_incoming exceeding data_limit
        pbar.update(data_limit)
        vpn_functions.increment_connection()

    except TypeError:
        # Triggered on the vpn being inactive
        try:
            pbar.update(0)
            time.sleep(5)
        except KeyboardInterrupt:
            exit()

    except KeyboardInterrupt:
        exit()
