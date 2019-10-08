#!/usr/bin/python3

import argparse
import argparse
from gpiozero import Button

from time import sleep

def wait_button(reboot_id=19, poweroff_id=26, wait_time=0.5):
    reboot_bt = Button(reboot_id)
    poweroff_bt = Button(poweroff_id)

    while True:
        if reboot_bt.is_pressed:
            reboot()
        elif poweroff_bt.is_pressed:
            poweroff()
        sleep(wait_time)

def load_nodes():
    nodes = []
    with open('./nodes.txt') as f:
        lines = f.readlines()
        for line in lines:
            nodes.append(line)
    return nodes

def reboot():
    nodes = load_nodes()
    for node in nodes:
        print('reboot ' + node)

def poweroff():
    nodes = load_nodes()
    for node in nodes:
        print('poweroff ' + node)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Service to monitor the power button')
    parser.add_argument('-r', '--reboot', metavar='reboot', default='19', nargs='?',
                        help='The GPIO number used for the reboot')
    parser.add_argument('-p', '--poweroff', metavar='poweroff', default='26', nargs='?',
                        help='The GPIO number used for the poweroff')
    parser.add_argument('-w', '--wait', metavar='wait', default='0.5', nargs='?',
                        help='The time to wait for polling the button')

    args = parser.parse_args()
    wait_button(int(args.reboot), int(args.poweroff), float(args.wait))
    