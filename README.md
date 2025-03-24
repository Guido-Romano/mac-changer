# MAC Address Changer Tool v1.0

A Python-based tool designed to automatically change the MAC address of a network interface.

## Features

- **Random MAC Generation**: Generates new, random MAC addresses automatically.
- **Command Execution**: Executes the necessary shell commands to update the MAC address.
- **MAC Address Validation**: Retrieves and validates the current MAC address using regular expressions.

## Requirements

- Python 3.x
- `subprocess` (built-in)
- `sys` (built-in)
- `re` (built-in)
- `random` (built-in)

## Installation & Usage

### Debian-based Distributions (e.g., Ubuntu, Kali)

1. **Update package lists**:

    ```bash
    sudo apt-get update
    ```

2. **Install Python**:

    ```bash
    sudo apt-get install python3
    ```

3. **Run the script**:

    ```bash
    python3 mac_address_changer.py
    ```

### Arch-based Distributions (e.g., Arch Linux, BlackArch)

1. **Update package lists**:

    ```bash
    sudo pacman -Syu
    ```

2. **Install Python**:

    ```bash
    sudo pacman -S python
    ```

3. **Run the script**:

    ```bash
    python3 mac_address_changer.py
    ```

### Red Hat-based Distributions (e.g., CentOS, Fedora)

1. **Update package lists**:

    ```bash
    sudo dnf update
    ```

2. **Install Python**:

    ```bash
    sudo dnf install python3
    ```

3. **Run the script**:

    ```bash
    python3 mac_address_changer.py
    ```

### How It Works

1. **Input**: The user specifies the network interface they want to modify (default is `eth0`).
2. **MAC Address Change**: The script generates a new random MAC address and assigns it to the specified network interface.
3. **Output**: Displays the current MAC address and the newly generated one, while handling errors effectively.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Special thanks to Python's `subprocess`, `re`, and `random` libraries for enabling efficient and reliable MAC address changes.
