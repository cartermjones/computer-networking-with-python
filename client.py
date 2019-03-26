'''
Author: Carter Jones

Code adapted from Kurose/Ross textbook and supplement,
geeksforgeeks.com, realpython.com, and Python documentation.
'''

#import socket module
from socket import *

#Import time module for calculating RTT
import time

#Import sys module to take arguments from command line
import sys

#create socket, taking HOST and PORT names from CLI
HOST = sys.argv[1]
PORT = int(sys.argv[2])

clientSocket = socket(AF_INET, SOCK_STREAM)

#establish connection
clientSocket.connect((HOST, PORT))

#Display connection information
print("Host Name: " + gethostname())
print("Peer Name: " + str(clientSocket.getpeername()))
print('Socket Family: INET')
print('Socket Type: STREAM')
print("Protocol: TCP")

#Retrieve requested file name from CLI
requestname = sys.argv[3]

#Create sending time stamp
sent_time = time.time()

#Send request to server
clientSocket.send(bytes(requestname, 'utf-8'))

#Receive status message from server
status = clientSocket.recv(5120r)

#Receive and decode data from server
data = clientSocket.recv(5120).decode('utf-8')

#Create received time stamp
recv_time = time.time()

#Calculate Round-Trip Time (RTT)
rtt = round((recv_time - sent_time), 3)

#Display received status message
print('HTTP Status: ' + str(status.decode('utf-8')))

#Display received data
print(data)

#Display calculated RTT
print("RTT: " + str(rtt) +"ms")
