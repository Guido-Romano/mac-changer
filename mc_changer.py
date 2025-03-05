#!/usr/bin/env python3
"""
MAC Address Changer Tool

This script allows changing the MAC address of a specified network interface.
"""

import argparse
import subprocess
import signal
import sys
import re
from termcolor import colored


def signal_handler(sig, frame):
    """Handles Ctrl+C (SIGINT) to exit gracefully."""
    print(colored("\n[!] Exiting the program...\n", 'red'))
    sys.exit(1)


signal.signal(signal.SIGINT, signal_handler)


def get_args():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Tool to change the MAC address of a network interface"
    )
    parser.add_argument(
        "-i", "--interface", required=True, dest="iface",
        help="Name of the network interface"
    )
    parser.add_argument(
        "-m", "--mac", required=True, dest="new_mac",
        help="New MAC address for the network interface"
    )
    return parser.parse_args()


def validate_input(iface, new_mac):
    """Validates the interface name and MAC address format."""
    valid_iface = re.match(r'^[a-zA-Z0-9-]+$', iface)
    valid_mac = re.match(r'^([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$', new_mac)
    return valid_iface and valid_mac


def execute_command(command):
    """Executes a shell command and handles errors."""
    try:
        subprocess.run(command, check=True, text=True)
    except subprocess.CalledProcessError as error:
        print(colored(f"\n[!] Command failed: {error}\n", 'red'))
        sys.exit(1)


def update_mac(iface, new_mac):
    """Updates the MAC address of the specified network interface."""
    if validate_input(iface, new_mac):
        execute_command(["ifconfig", iface, "down"])
        execute_command(["ifconfig", iface, "hw", "ether", new_mac])
        execute_command(["ifconfig", iface, "up"])
        print(colored(
            "\n[+] MAC address has been successfully changed\n", 'green'))
    else:
        print(colored("\n[!] Invalid input data\n", 'red'))


def main():
    """Main function to parse arguments and change MAC address."""
    args = get_args()
    update_mac(args.iface, args.new_mac)


if __name__ == "__main__":
    main()
