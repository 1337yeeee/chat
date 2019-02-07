import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
B_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print("Connection address: {}".format('Big_Mack'))
while 1:
    data, sended_adr = s.recv(B_SIZE)
    if not data:
        break
    if data == b'STOP':
        s.close()
    print("received data: {}".format(data), " from: {}".format(sended_adr))
    s.send(data)

s.close()
