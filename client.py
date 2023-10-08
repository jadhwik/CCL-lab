import socket

# Define the server host and port
server_host = 'localhost'
server_port = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))
client_socket.settimeout(10.0)

while True:
    # Get user input
    message = input("Enter a message to send to the server (or 'exit' to quit): ")

    if message == 'exit':
        break

    # Send the message to the server
    client_socket.send(message.encode('utf-8'))

    # Receive the response from the server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {response}")

# Close the client socket
client_socket.close()
