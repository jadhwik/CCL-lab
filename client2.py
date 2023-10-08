import socket

# Define the server host and port
server_host = 'localhost'
server_port = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Get user input
    message = input("Enter a message to send to the server (or 'exit' to quit): ")

    if message == 'exit':
        break

    # Send the message to the server
    client_socket.sendto(message.encode('utf-8'), (server_host, server_port))

    # Receive the response from the server
    response, server_address = client_socket.recvfrom(1024)
    
    # Decode and print the response
    response = response.decode('utf-8')
    print(f"Server response: {response}")

# Close the client socket
client_socket.close()
