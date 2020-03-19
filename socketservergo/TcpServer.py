#!/bin/python3
"""
socketserver:
四种简单协议服务
socketserver.TCPServer->socketserver.UnixStreamServer 
socketserver.UDPServer->socketserver.UnixDatagramServer
后者继承前者，但是IP address family不同

serve_forever(poll_interval=0.5) 开启间隔循环扫描信息
shutdown 关闭serve_forever 循环
server_close() 关闭server

BaseRequestHandler  消息的接口类
StreamRequestHandler
DatagramRequestHandler

以上handler中
self.request 收到的请求
self.rfile   读取request数据，self.rfile.readline()相当于多次self.request.recv()操作直到遇见新行
self.wfile  写数据并返回client，self.wfile.write()可代替self.request.sendall()操作
self.client_address 客户端地址
self.server 服务器本身


通常操作
1、 继承BaseRequestHandler类（消息接口类）
2、 重新定义handle方法
3
"""
from socketserver import TCPServer,BaseRequestHandler

class MyTCPHandler(BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        # self.data = self.rfile.readline().strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # send back the data
        self.request.sendall(self.data.upper())
        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        # self.wfile.write(self.data.upper())

if __name__ == "__main__":
    HOST,PORT = "localhost",9999
    with TCPServer((HOST,PORT),MyTCPHandler) as server:
        # Activate the server
        server.serve_forever()


