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
    """Main entrance of the TCP server module."""

    server_address = ('', 12345)

    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server_socket:
        server_socket.bind(server_address)
        server_socket.settimeout(5*60) # Set before listen()
        server_socket.listen(1)

        print("The server is ready to receive segments.")
        while True:
            connection_socket, client_address = server_socket.accept()
            with connection_socket:
                print("Connected from:", client_address)

                client_message = connection_socket.recv(2048).decode()
                if not client_message:
                    print("Received nothing from the client. Continue ...")
                    continue
                print("Message received:", client_message)

                upper_message = client_message.upper()
                connection_socket.sendall(upper_message.encode())
                print("Message sent:", upper_message)
                
if __name__ == "__main__":
    sys.exit(main())
