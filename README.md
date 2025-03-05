# MAC Address Changer v1.0

Python-based tool to change the MAC address of a network interface quickly and efficiently.

## Features

- **Command Line Interface**: Easily specify the network interface and the new MAC address using command-line arguments.
- **Input Validation**: Ensures the provided network interface and MAC address are in the correct format.
- **Error Handling**: Manages potential errors gracefully to ensure a smooth user experience.

## Requirements

- Python 3.x
- `termcolor` (install via pip)
- `argparse` (built-in)
- `subprocess` (built-in)
- `re` (built-in)
- `signal` (built-in)
- `sys` (built-in)

## Installation & Use

1. **Clone the repository**:

    ```bash
    git clone https://github.com/YourUsername/mac-address-changer
    cd mac-address-changer
    ```

2. **Install the required packages**:

    ### Debian-based distributions (e.g., Kali)

    ```bash
    sudo apt-get update
    sudo apt-get install python3 python3-pip
    pip3 install termcolor
    ```

    ### Arch-based distributions (e.g., BlackArch)

    ```bash
    sudo pacman -Syu
    sudo pacman -S python python-pip
    pip install termcolor
    ```

3. **Run the script and specify the network interface and the new MAC address**:

    ```bash
    python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
    ```

## How It Works

1. **Input**: The script accepts command-line arguments for the network interface and the new MAC address.
2. **Validation**: The input is validated to ensure the network interface and MAC address are in the correct format.
3. **MAC Address Change**: The script brings down the network interface, changes the MAC address, and brings the interface back up.
4. **Output**: The script prints the status of the operation, including success or failure messages.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This project was inspired by the need to have a simple and efficient tool to change MAC addresses using Python.

Special thanks to the developers of the `termcolor` library for providing colorful terminal output.





