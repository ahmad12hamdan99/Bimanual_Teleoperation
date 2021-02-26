# importing socket module 
import socket 
import time

def pack():
    print('M')

bufTX = bytearray([b'bb'] * 241)

for i in range(8):
    idx = bytes(i+1)
    bufTX[16*i] = idx
    bufTX[16*i + 128] = idx

UDP_IP = "192.169.2.1"
UDP_PORT = 10003

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))

Encoders= {'L.ShoulderF':{'Index':2, 'Scale':-0.085}, 
           'L.ShoulderS':{'Index':270, 'Scale':0.08789063}, 
           'L.ElbowR':{'Index':268, 'Scale':0.08789063}, 
           'L.Elbow':{'Index':34, 'Scale':-0.02}, 
           'L.WristR':{'Index':18, 'Scale':0.085}, 
           'L.WristS':{'Index':264, 'Scale':0.08789063}, 
           'L.WristF':{'Index':266, 'Scale':-0.08789063},
           'L.Finger.IndexF':{'Index':66, 'Scale':-0.085},
           'L.Finger.LittleF':{'Index':114, 'Scale':0.085},
           'L.Finger.MiddleF':{'Index':82, 'Scale':0.085},
           'L.Finger.RingF':{'Index':98, 'Scale':-0.085},
           'L.Finger.ThumbF':{'Index':50, 'Scale':-0.085},
           }

sock.send(bufTX) 
# while(True):
#         data, addr = sock.recvfrom(310)
#         print(data[Encoders['L.Finger.MiddleF']['Index']] * Encoders['L.Finger.MiddleF']['Scale'])
        