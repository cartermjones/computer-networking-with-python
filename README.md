The server code in this repository is (supposed to be) a multi-threaded server. It is written in Python 3.5.1
and is adapted from code on Geeksforgeeks.com, RealPython.com, and from the Kurose/Ross Computer Networking textbook and its companion material, as well as Python documentation.

Specific links for adapted material (besides the Kurose/Ross material): 

https://www.geeksforgeeks.org/socket-programming-multi-threading-python/

https://realpython.com/python-sockets/#socket-api-overview

https://docs.python.org/3/howto/sockets.html

The code was written using the IDLE IDE, and primarily tested running in IDLE. I have also run the scripts in a CLI (Windows 10) with mixed success.

Currently the server.py script seems to successfully send files via HTTP to the client, but the files' contents do not appear on
the screen. This is the current problem that I'm working on. 

The client.py script is a simple web client written with code gleaned or adapted from the same above resources, for the most part, with some adaptations to meet requirements specified in the project outline. 

It can be run in a Windows CLI as follows:

C:/somedirectory/> py client.py </filename_to_be_requested>

This will yield a result like the following: 

Host Name: DESKTOP-5DDS25T
Peer Name: ('127.0.0.1', 50007)
Protocol: TCP
HTTP Status: HTTP/1.0 200 OK

Some Data
RTT: 0.015ms

It is important to note that the '/' character must be included in the file name, or else the server.py script will return a 404 File Not Found message. (While it can infer the '.' in the relative path, it doesn't infer the '/'.)

For the client.py and server.py scripts to work, they must be in the same folder as the documents being requested. There is currently no way for them to deal with absolute paths. 

