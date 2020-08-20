# tcp_socket

1. When creating a TCP socket, the three-way handshake takes place within the transport layer, invisible to developers.
2. Handshake is done with the _welcoming socket_, while segments are transmitted to _connection socket_.
2. Make sure the server port is enabled in `firewalld`.
