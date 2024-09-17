#!/usr/bin/env python3

import socket as soc
import threading

# Code to create a server socket
def run_server():
    # Create socket object
    server = soc.socket(soc.AF_INET, soc.SOCK_STREAM)

    # Bind the server socket to an IP address & port
    ip = "localhost"  # Could use "192.168.0.2" for a specific IP
    port = 8080
    server.bind((ip, port))

    # After binding, listen for incoming connections
    server.listen(5)  # Allow 5 connection in the queue
    print(f"Listening on {ip}:{port}")

    # Accept connections
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    
    #To block some modafucker
    if client_address[0] in blocked_ips:
            print(f"Blocked connection attempt from {client_address[0]}")
            client_socket.close()

    # Communication loop for sending and receiving messages
    while True:
        # Receive messages from the client
        request = client_socket.recv(1024).decode("utf-8")  # Receive up to 1024 bytes and decode to string
        print(f"Received: {request}")

        # If the client sends "close", break out of the loop and close the connection
        if request.lower() == "close":
            client_socket.send("Connection closing...".encode("utf-8"))
            break

        # Server sends a response back to the client
        response = input("Enter your response: ")
        client_socket.send(response.encode("utf-8"))

    # Close the connection with the client
    client_socket.close()
    print("Connection with client closed")


    # Close the server socket
    server.close()
    
    try:
        while True:
            # Simulating a long-running process
            print("Running...")
    except KeyboardInterrupt:
        pass  # Silently handle the KeyboardInterrupt and exit


# Call the server function
run_server()

