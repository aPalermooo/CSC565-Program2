# Socket Programming Assignment II 

Xander Palermo <ajp2s@missouristate.edu>

CSC565 Computer Networking Fall 2025

Dr. Hiu Liu

7 November 2025

<hr/>

# Files Included

## Webserver.py

This file contains a python script to open the computer running to begin accepting HTTP requests on port 6789.
This script is meant to emulate how a real Web Server would receive, and process HTTP requests on a low level.
By default, any device connected to the same LAN as the HTTP server is able to connect and send requests to the Server.


The way that this script processes requests is locating the file name requested in the HTTP GET header, and searching for a matching file contained in the `static` folder (in the same directory as the script).
- If a document is found in the `static` folder that meets this condition, the server will return a __200 OK__ status and the contents of the document to the client.
- If a document is not found in the `static` folder, an error is thrown and caught by the server, and the server sends a __404 NOT FOUND__ to the client
- If a client requests a file path that tries to escape the `static` folder (such as "`/../../sensitive-info.text`"). The server will return a __400 BAD REQUEST__ code to the client.

This script will also log the following to standard output:
- When the server is available to receive requests from a client
- The header of requests received
- The path of the document requested
- Outgoing traffic back to the client

## static/HelloWorld.html

This is a sample file of what types of documents the HTTP server can serve to clients. Being a very low-level web server. the script is unable to handle requests for index.html and handle back-end computations like a typical web server. However, client-side applications can still are available through a plain HTML+CSS+JS framework.

<hr/>

# Usage 

## Required Files

All required files are contained within the submitted .zip file. The program can also be installed by the command:

> git clone https://github.com/aPalermooo/CSC565-Program2

Servers can be initiated by calling their file name using the python3 interpreter

Document files can be added and removed from the static folder, depending on what files you want to make accessible for clients to request

## Initialization 

Open a terminal on the computer to run the server, navigate to the directory containing Webserver.py, and run it using a python3 interpreter

> python3 Webserver.py

## Usage 

Upon initializing, the script will print the IP and port number that the script is listening to. This is the endpoint that all requests will be made to.

### Browser

To make requests, open your preferred browser and enter

> http://X.X.X.X:6789/Document

Where X.X.X.X is the IP address that the server printed to console, and Document being the file you are requesting from the server (ex "HelloWorld.html")

### Terminal

Requests can also be created through a terminal window through the curl command

> curl -v http://X.X.X.X:6789/Document

Where X.X.X.X is the IP address that the server printed to console, and Document being the file you are requesting from the server (ex "HelloWorld.html")

## Terminating

Send an interupt key input (typically cmd/ctrl + c to the terminal that is running the script)