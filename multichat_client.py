import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Client configuration
server_host = 'localhost'
server_port = 12345

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_host, server_port))

# Function to send messages to the server
def send_message():
    message = entry.get()
    if message:
        client_socket.send(message.encode('utf-8'))
        entry.delete(0, tk.END)

# Function to receive messages and display them in the chat window
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            chat_text.config(state=tk.NORMAL)
            chat_text.insert(tk.END, message + '\n')
            chat_text.config(state=tk.DISABLED)
        except:
            break

# Create the GUI window
window = tk.Tk()
window.title("Multi-User Chat")

# Create a scrolled text widget for the chat
chat_text = scrolledtext.ScrolledText(window)
chat_text.config(state=tk.DISABLED)
chat_text.pack()

# Create an entry widget for typing messages
entry = tk.Entry(window)
entry.pack()

# Create a send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Run the GUI main loop
window.mainloop()

# Close the client socket when the window is closed
client_socket.close()
