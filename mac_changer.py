#!/usr/bin/env python3

# Herramienta para Cambiar la Dirección MAC
# Este script cambia automáticamente la dirección MAC.


import subprocess
import sys
import re
import random
from colorama import Fore, init

# Inicializar colorama
init(autoreset=True)


def obtener_mac_actual(iface):
    # Obtiene la dirección MAC actual de la interfaz especificada.
    try:
        resultado = subprocess.run(
            ["ifconfig", iface], capture_output=True, text=True, check=True
        )
        mac_regex = r"([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}"
        mac_encontrada = re.search(mac_regex, resultado.stdout)
        if mac_encontrada:
            return mac_encontrada.group(0)
        else:
            print(
                Fore.RED + "\n[!] No se pudo obtener la dirección MAC actual\n"
            )
        sys.exit(1)
    except subprocess.CalledProcessError as error:
        print(Fore.RED + f"\n[!] Falló el comando: {error}\n")
        sys.exit(1)


def generar_mac_aleatoria():
    # Genera una dirección MAC aleatoria.
    return "02:00:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )


def ejecutar_comando(comando):
    # Ejecuta un comando en la terminal y maneja errores.
    try:
        subprocess.run(comando, check=True, text=True)
    except subprocess.CalledProcessError as error:
        print(Fore.RED + f"\n[!] Falló el comando: {error}\n")
        sys.exit(1)


def actualizar_mac(iface):
    # Cambia la dirección MAC de la interfaz de red especificada.
    mac_actual = obtener_mac_actual(iface)
    print(Fore.GREEN + f"\n[+] Tu dirección MAC actual es: {mac_actual}")
    nueva_mac = generar_mac_aleatoria()
    ejecutar_comando(["ifconfig", iface, "down"])
    ejecutar_comando(["ifconfig", iface, "hw", "ether", nueva_mac])
    ejecutar_comando(["ifconfig", iface, "up"])
    print(Fore.GREEN + f"[+] Tu nueva dirección MAC es: {nueva_mac}\n")


def main():
    # Función principal para cambiar la dirección MAC automáticamente.
    interfaz = "eth0"  # Define tu interfaz de red predeterminada aquí.
    actualizar_mac(interfaz)


if __name__ == "__main__":
    main()
