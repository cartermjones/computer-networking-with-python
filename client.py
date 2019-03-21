#import socket module
from socket import *

#Import time module for calculating RTT
import time

#Import sys module to take arguments from command line
import sys

#create socket
HOST = '127.0.0.1'
PORT = 50007

clientSocket = socket(AF_INET, SOCK_STREAM)

#establish connection
clientSocket.connect((HOST, PORT))

#Display connection information
print("Host Name: " + gethostname())
print("Peer Name: " + str(clientSocket.getpeername()))
print("Protocol: TCP")

#Retrieve requested file name from CLI
requestname = sys.argv[1]

#Create sending time stamp
sent_time = time.time()

#Send request to server
clientSocket.send(bytes(requestname, 'utf-8'))

#Receive status message from server
status = clientSocket.recv(1024)

#Receive and decode data from server
data = clientSocket.recv(1024).decode('utf-8')

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
