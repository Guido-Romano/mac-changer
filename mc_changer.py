#!/usr/bin/env python3
"""
MAC Address Changer Tool

This script automatically changes the MAC address.
"""

import subprocess
import sys
import re
import random


def get_current_mac(iface):
    # Retrieves the current MAC address of the specified interface.
    try:
        result = subprocess.run(
            ["ifconfig", iface], capture_output=True, text=True, check=True
        )
        mac_regex = r"([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}"
        mac_address_match = re.search(mac_regex, result.stdout)
        if mac_address_match:
            return mac_address_match.group(0)
        else:
            print("\n[!] Could not retrieve the current MAC address\n")
            sys.exit(1)
    except subprocess.CalledProcessError as error:
        print(f"\n[!] Command failed: {error}\n")
        sys.exit(1)


def generate_random_mac():
    # Generates a random MAC address.
    return "02:00:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


def execute_command(command):
    # Executes a shell command and handles errors.
    try:
        subprocess.run(command, check=True, text=True)
    except subprocess.CalledProcessError as error:
        print(f"\n[!] Command failed: {error}\n")
        sys.exit(1)


def update_mac(iface):
    # Updates the MAC address of the specified network interface.
    current_mac = get_current_mac(iface)
    print(f"\n[+] Your current MAC address is: {current_mac}")
    new_mac = generate_random_mac()
    execute_command(["ifconfig", iface, "down"])
    execute_command(["ifconfig", iface, "hw", "ether", new_mac])
    execute_command(["ifconfig", iface, "up"])
    print(f"[+] Your new MAC address is: {new_mac}\n")


def main():
    # Main function to change the MAC address automatically.
    interface = "eth0"  # Define your default network interface here.
    update_mac(interface)


if __name__ == "__main__":
    main()
