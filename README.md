# tcp_socket

1. When creating a TCP socket, the three-way handshake takes place within the transport layer, invisible to developers.
2. Handshake is done with the _welcoming_ socket by `listen()`, while segments are transmitted to and received from _connection_ socket by `accept()`.
3. Use `with` instead of `try` to catch exceptions automatically.
4. Make sure the server port is enabled in `firewalld`.
