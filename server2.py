import socket

# Define the server host and port
server_host = 'localhost'
server_port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address
server_socket.bind((server_host, server_port))

print(f"Server is listening on {server_host}:{server_port}")

while True:
    # Receive data from the client
    data, client_address = server_socket.recvfrom(1024)
    
    # Decode the received data
    data = data.decode('utf-8')
    
    if not data:
        break  # If no data received, exit the loop

    print(f"Received data from {client_address}: {data}")

    # Send the received data back to the client
    server_socket.sendto(data.encode('utf-8'), client_address)

# Close the server socket
server_socket.close()
