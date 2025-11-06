################################################
#   Name:           Webserver.py
#   Description:    A low-level web server that listens on a specified socket for incoming requests, and serves them from a specified directory
#   Author:         Xander Palermo <ajp2s@missouristate.edu>
#   Date:           7 November 2025
#
#   Class:          CSC 565 Computer NetworkingFALL 2025
#   Professor:      Dr. Hui Liu
#   Assignment:     Socket Programming Assignment II
################################################



# Import socket module
from socket import *
import sys

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port
#Fill in start

HOST = gethostbyname(gethostname())

serverSocket.bind((HOST, serverPort))

#Fill in end

# Listen to at most 1 connection at a time
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections

while True:
    print(f'The server is ready to receive at: {HOST}:{serverPort}')

    # Set up a new connection from the client
    #Fill in start

    connectionSocket, addr = serverSocket.accept()

    #Fill in end

    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        # Receives the request message from the client
        message = connectionSocket.recv(1024).decode()
        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        #Fill in start

        print("Received Request:")

        print(message)
        print()
        #Fill in end

        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character
        #Fill in start

        path = message[message.find('/')+1:message.find(' ',message.find('/'))]

        if path.count('/') > 0:
            #Handle malicious requests

            print("Bad Request...\nClosing Connection\n\n")
            connectionSocket.send("HTTP/1.1 400 BAD REQUEST\r\n\r\n".encode())

            connectionSocket.close()

            continue

        path = "static/" + path

        #Fill in end

        # Store the entire content of the requested file in a temporary buffer
        #Fill in start

        print(f"Encoding and sending {path}...")


        requested_document = open(path) # if not exist -> Throws IOError
        document = requested_document.read()

        #Fill in end

        # Send the HTTP response header line to the connection socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
 
        # Send the content of the requested file to the connection socket
        #Fill in start
        connectionSocket.send(document.encode())

        print("Closing Connection\n\n")
        #Fill in end

        # Close the client connection socket
        connectionSocket.close()

    except IOError: # File does not exist

            print("Not found...\nClosing Connection\n\n")

            # Send HTTP response message for file not found
            #Fill in start
            connectionSocket.send("HTTP/1.1 404 NOT FOUND\r\n\r\n".encode())
            #Fill in end

            # Close the client connection socket
            connectionSocket.close()

serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data
