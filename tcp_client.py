#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""TCP Client

1. Capture user's lower-case string and send to the server.
2. Receive upper-case string from the server and print on screen.

"""

__author__ = "Jim Gray"
__email__ = "jimgray@outlook.com"
__credits__ = ["Google","Python3.8 Manual"]
__copyright__ = "Copyright 2020, China"
__license__ = "GPL"
__version__ = "0.1"
__status__ = "Development"

import sys
import socket

def main():
    """Main entrance of the TCP client module."""

    server_address = ("192.168.56.105", 12345)

    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as client_socket:
        user_input = input('Input lower-case sentence: ')

        client_socket.settimeout(5) # Set before connect()
        client_socket.connect(server_address)
        print("Connected to: ", server_address)

        client_socket.sendall(user_input.encode())
        print("Message sent:", user_input)

        server_data = client_socket.recv(2048)
        if not server_data:
            raise socket.error("Receive nothing from the server.")
        print("Message received:", server_data.decode())

if __name__ == "__main__":
    sys.exit(main())
