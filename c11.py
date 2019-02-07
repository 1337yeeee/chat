import socket
# import time

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
B_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
    print('*-'*10)
    message = input('Write something here:\n')
    if message == 'STOP':
        print('Closing connection...')
        s.send(b'STOP')
        time.sleep(2.0)
        s.close()
        break
    s.send(bytes(message, encoding='utf-8'))
    print('_-'*10)
    sended = s.recv(1024)
    print('You send:\n'+sended)

s.close()
