import socket

size = 241
bufTX = bytearray(b'\x9C' * 241)
print(type(bufTX[0]))

for i in range(8):
    idx = bytes(i+1)
    bufTX[16 * i] = idx
    bufTX[16*i + 128] = idx

HOST = '192.169.2.1'  # Standard loopback interface address (localhost)
PORT = 10003        # Port to listen on (non-privileged ports are > 1023)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))

sock.send(bytes(6))
