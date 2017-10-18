#!/usr/bin/env python3

import os
import time
import subprocess

def all_vpns():
    vpn_dict = {}
    conf_dir = '/etc/openvpn/client'
    conf_files = os.listdir(conf_dir)

    for i in conf_files:
        try:
            middle_field = i.split('_')[1]
            country_code = middle_field[:2]
            server_number = int(middle_field[2:])
        except (ValueError, IndexError):
            pass

        try:
            vpn_dict[country_code].append(server_number)
        except KeyError:
            vpn_dict[country_code] = [server_number]


    for i in vpn_dict:
        vpn_dict[i] = list(set(vpn_dict[i]))
        vpn_dict[i].sort()
        vpn_dict[i] = [str(i) for i in vpn_dict[i]]

    return vpn_dict


def get_vpn_list(country_code):
    vpn_list = []

    conf_dir = '/etc/openvpn/client'
    conf_files = os.listdir(conf_dir)

    for i in conf_files:
        try:
            middle_field = i.split('_')[1]
            if country_code:
                if middle_field.startswith(country_code):
                    vpn_list.append(middle_field)
        except IndexError:
            pass

    vpn_list = list(set(vpn_list))
    vpn_list.sort()

    return vpn_list


def get_current_connection(vpn_interface='tun0'):
    incoming_bytes = None

    with open('/proc/net/dev', 'r') as datafile:
        for i in datafile:
            if i.strip().startswith(vpn_interface):
                incoming_bytes = int(i.split()[1])

    if incoming_bytes:
        systemctl_process = subprocess.run(
            'systemctl --type=service | grep openvpn-client',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL)
        vpn_name = systemctl_process.stdout.decode(
            'utf-8').split('@')[1].split('_')[1]
        return vpn_name, incoming_bytes
    else:
        return None


def helper_script_shenanigans(start_vpn):
    stop_command = 'sudo nordvpn stop'
    if not start_vpn:
        subprocess.run(
            stop_command,
            shell=True)
        return

    time.sleep(1.5)

    start_command = f'sudo nordvpn start {start_vpn}'
    subprocess.run(
        start_command,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL)


def increment_connection():
    try:
        current_connection = get_current_connection()
        current_vpn_name = current_connection[0]
        country_code = current_vpn_name[:2]
    except TypeError:
        # Account for the possibility of being able to establish a new VPN connection here
        return

    vpn_list = get_vpn_list(country_code)
    current_vpn_index = vpn_list.index(current_vpn_name)
    incremented_vpn_index = current_vpn_index + 1

    try:
        next_vpn_name = vpn_list[incremented_vpn_index]
    except IndexError:
        next_vpn_name = vpn_list[0]

    helper_script_shenanigans(next_vpn_name)
