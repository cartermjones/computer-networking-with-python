#import socket module
from socket import *

#import thread module
from _thread import *
import threading

print_lock = threading.Lock()

#Thread function
def threaded(connectionSocket):
    while True:
        
        try:
            #data received from client
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            filename = filename.decode('utf-8')
            f = open('.' + filename, 'rb')
            outputdata = f.read(1024)
        
            #Send HTTP 200 OK Response message
            connectionSocket.send(bytes("HTTP/1.0 200 OK\n", "utf-8"))

            #Send data to client
            connectionSocket.send(outputdata)
            print("File sent")
            print_lock.release()
            break
        
        except:

            #Send response message for file not found
            connectionSocket.send(bytes('HTTP/1.0 404 File Not Found \n', 'utf-8'))

            #Close client socket
            print_lock.release()
            connectionSocket.close()
            break
            
        #Close connection
        
        connectionSocket.close()

def Main():
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a server socket
    HOST = gethostname()
    PORT = 50007

    serverSocket.bind((HOST, PORT))
    serverSocket.listen(5)
    
    while True:
        print_lock.acquire()
        #Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
       
        print('Connected by ' + str(addr)) 
        start_new_thread(threaded, (connectionSocket,))
    
    #Close this socket
    serverSocket.close()

if __name__ == '__main__':
    Main()

    
        
