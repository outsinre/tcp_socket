# tcp_socket

1. The client sends a lower-case sentence and the server replies the upper-case variant.
2. When creating a TCP socket, the three-way handshake takes place within the transport layer, invisible to developers.
3. Handshake is done with the _welcoming_ socket by `listen()`, while segments are transmitted to and received from _connection_ socket by `accept()`.
4. Use `with` instead of `try` so that exceptions are not handled and terminate the program immediately.
5. Make sure the server port is enabled in `firewalld`.
