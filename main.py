import socket
import sys
import serial #to open tty/USB0
#ser=serial.Serial('/dev/ttyUSB0')
#data_to_send=b'Hello world'
#ser.write(data_to_send)
#ser.close()
from utils import crc_sum,port_check

while True: 
    
    if port_check()==True:
        print('port connected')
        break
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address=('192.168.1.158',5000)
print(socket.gethostbyname_ex(socket.gethostname()))
server.bind(server_address)
server.listen()
user,adres=server.accept()
print('connected')

while True:
    msg=user.recv(1024)
    print(msg,type(msg),len(msg))
    tmp=[]
    for i in range(2,10):
        print(msg[i])
        tmp.append(msg[i])
    crc=msg[10]
    print(crc_sum(tmp,crc))
    

