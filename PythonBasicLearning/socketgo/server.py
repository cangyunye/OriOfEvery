#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@author: cangyunye
@Email: cangyunye@gmail.com
@wechat:whyNless
@file: server.py
@time: 2019/4/28/028 23:18
@desc: 客户端服务器端socket持续通讯工具
'''

"""
问题记录
1. 如果想进行循环连接，必须考虑到服务器端与客户端都要有对于阻塞步骤的处理，否则会一方无法循环
2. 由于接收和发送数据是二进制，进行判断的时候，需要以二进制数据判断或者转换为统一编码
"""
from socket import socket,AF_INET,SOCK_STREAM
from time import ctime,sleep

# 0.将服务端打造为机器人回复模式，判断输入数据，然后进行智能返回
# 1.第一阶段使用字典方式进行答复
# 2.字典保存在其他文件对象中读取
# 实例化socket对象

# UDP连接方式
#sudp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 定义socket绑定地址和端口
ADDR = '127.0.0.1'
PORT = 9999

# 定义BUFSIZE表示每次接收信息大小
BUFSIZE = 1024



# TCP连接方式
with socket(AF_INET,SOCK_STREAM) as stcp:
	stcp.bind((ADDR, PORT))
	# TCP端口监听,指定允许5个连接
	stcp.listen(5)
	# accept以阻塞的方式，传递远端请求连接信息
	# 返回连接的sock对象和地址addr
	while True:
		conn_sock,addr=stcp.accept()
		# 打开连接对象
		with conn_sock:
			print(f"connected to {addr}.")
			conn_sock.send(bytes("Welcome to the test-server.",'utf-8'))
			# 不断监听信号
			while True:
				print("On Reciving.")
				data = conn_sock.recv(BUFSIZE)
				if not data:
					break
				# 转换为utf-8再判断
				elif data.decode('utf-8') == 'Hello':
					print('1')
					conn_sock.send(bytes('Join the party,and learning together.','utf-8'))
					# 跳出本次循环，继续轮询客户端输入
					continue
				elif data.decode('utf-8') == 'quit':
					print('2')
					conn_sock.send(bytes(f'Disconnect at {ctime}','utf-8'))
					conn_sock.close()
					break
				else:
					print(f"Recieved:{data}.")
					conn_sock.send(bytes(f'Unknow message', 'utf-8'))
					continue
			# 关闭连接对象


