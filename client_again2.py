#!/usr/bin/env python3

import socket as soc
import threading

# Code to create a client socket
def run_client():
    # Create a socket object
    client = soc.socket(soc.AF_INET, soc.SOCK_STREAM)

    # Connect to the server (localhost and port 8080)
    client.connect(("localhost", 8080))

    # Communication loop
    while True:
        # Send a message to the server
        message = input("Enter message: ")
        client.send(message.encode("utf-8"))

        # If the client sends "close", break out of the loop and close the connection
        if message.lower() == "close":
            print(client.recv(1024).decode("utf-8"))  # Receive the closing message from the server
            break

        # Receive a response from the server
        response = client.recv(1024).decode("utf-8")
        print(f"Server: {response}")

    # Close the client socket
    client.close()

    try:
        while True:
            # Simulating a long-running process
            print("Running...")
    except KeyboardInterrupt:
        pass  # Silently handle the KeyboardInterrupt and exit

# Call the client function
run_client()

