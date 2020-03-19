"""
0. 无需继承类
1. 创建socket(address family ,type)，选择传输方式
2. 传输bytes二进制数据
"""
from socket import socket,AF_INET,SOCK_STREAM 
import sys

HOST,PORT ="localhost",9999
data = " ".join(sys.argv[1:])
with socket(AF_INET,SOCK_STREAM) as sock:
    sock.connect((HOST,PORT))
    sock.sendall(bytes(data+"\n","utf-8"))

    received = str(sock.recv(1024),"utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))