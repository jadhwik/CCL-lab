import socket

# Define the server host and port
server_host = 'localhost'  # Use '0.0.0.0' to listen on all available network interfaces
server_port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address
server_socket.bind((server_host, server_port))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server is listening on {server_host}:{server_port}")

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break  # If no data received, exit the loop

    print(f"Received data from client: {data}")

    # Send the received data back to the client
    client_socket.send(data.encode('utf-8'))

    # Close the client socket
    client_socket.close()

# Close the server socket
server_socket.close()
