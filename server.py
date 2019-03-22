#import socket module
from socket import *

#import thread module
from _thread import *
import threading

#Import time module for calculating RTT
import time

#Create a lock that will be used to manage the threads
data_lock = threading.Lock()

#Thread function
def threaded(connectionSocket):
    
    while True:
         
        try:
            #Request received from client
            message = connectionSocket.recv(1024)

            #Create received time stamp
            recv_time = time.time()

            #If the request is coming from the CLI, do this:
            filename = message

            #If the request is coming from a browser, do this:
            if len(message.decode('utf-8')) > 20:
                #Parse message from client
                filename = message.split()[1]
    
            filename = filename.decode('utf-8')
            f = open('.' + filename, 'rb')
            outputdata = f.read(1024)

            #Send HTTP 200 OK Response message
            connectionSocket.send(bytes("HTTP/1.0 200 OK\n", "utf-8"))

            #Send data to client
            connectionSocket.send(outputdata)

            #Display response to console
            print("HTTP Status: HTTP/1.0 200 OK")
            
            #Create sent time stamp
            sent_time = time.time()
            break
        
        except:

            #Send response message for file not found
            connectionSocket.send(bytes('HTTP/1.0 404 File Not Found \n', 'utf-8'))

            #Display to console
            print("HTTP Status: HTTP/1.0 404 File Not Found")

            #Create time stamp
            sent_time = time.time()
            break
            
    #Calculate RTT
    rtt = round((sent_time - recv_time), 3)

    #Display RTT
    print("RTT: " + str(rtt) + "ms")
    
    #Close connection and release lock
    connectionSocket.close()
    data_lock.release()
    print("Lock Released\n")

#This is the main logic of the server
def serve():

    #Create a server socket
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a server socket
    HOST = '127.0.0.1'
    PORT = 8080
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(5)

    while True:
        
        #Acquire lock
        data_lock.acquire()
        print("Lock Acquired")
        print('Ready to serve...')
        
        #Establish the connection
        connectionSocket, addr = serverSocket.accept()
        print("Host Name: " + gethostname())
        print('Peer Name:' + str(connectionSocket.getpeername()))
        print("Protocol: TCP")
        
        #Start new thread
        start_new_thread(threaded, (connectionSocket,))
        break
        
    #Close this socket
    serverSocket.close()
    

def Main():

    while True:
        serve()

if __name__ == '__main__':
    Main()
