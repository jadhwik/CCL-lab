import socket
import threading

# Server configuration
server_host = 'localhost'
server_port = 12345

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket
server_socket.bind((server_host, server_port))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server is listening on {server_host}:{server_port}")

# Dictionary to store client sockets and their usernames
clients = {}

# Function to broadcast messages to all clients with sender's username
def broadcast(message, sender_socket):
    sender_username = clients[sender_socket]
    message_with_username = f"{sender_username}: {message}"
    for client_socket in clients.keys():
        if client_socket != sender_socket:
            try:
                client_socket.send(message_with_username.encode('utf-8'))
            except:
                remove(client_socket)

# Function to remove a client from the dictionary
def remove(client_socket):
    if client_socket in clients:
        username = clients[client_socket]
        del clients[client_socket]
        broadcast(f"{username} has left the chat.\n", client_socket)

# Function to handle a client connection
def handle_client(client_socket):
    try:
        # Receive and broadcast messages
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            message=message[::-1]
            if not message:
                break
            broadcast(message, client_socket)
    except:
        # Handle disconnection or errors
        remove(client_socket)
    finally:
        # Close the client socket
        client_socket.close()

# Accept client connections and start handling them
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Prompt the client for a username
    client_socket.send(b"Enter your username: ")
    username = client_socket.recv(1024).decode('utf-8')

    # Add the client and username to the dictionary
    clients[client_socket] = username

    # Notify all clients about the new user
    notification_message = f"{username} has joined the chat!\n"
    broadcast(notification_message, client_socket)

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
