# importing socket module 
import socket 
import time

UDP_IP = "192.169.2.1"
UDP_PORT = 10003

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT)) 
while(True):
        data, addr = sock.recvfrom(310)
        
        ints = list(data)
        print(ints[82]*(0.085))
        #print ("Received message:", data)