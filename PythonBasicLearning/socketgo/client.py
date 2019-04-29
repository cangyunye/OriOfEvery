#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@author: cangyunye
@Email: cangyunye@gmail.com
@wechat:whyNless
@file: client.py
@time: 2019/4/28/028 23:48
@desc:
'''

from socket import AF_INET, SOCK_STREAM, socket

HOST = '127.0.0.1'
PORT = 9999
BUFSIZE = 1024

with socket(AF_INET,SOCK_STREAM) as stcp:
	try:
		stcp.connect((HOST,PORT))
		# 由于服务器有初始发送信息，这里通过接收服务器头信息防止阻塞。
		stcp.recv(BUFSIZE)
		while True:
			msg = input(">")
			if not msg:
				break
			stcp.send(bytes(msg,'utf-8'))
			data = stcp.recv(BUFSIZE)
			if not data:
				continue
			print(f'Received :{data.decode("utf-8")} ')
	except ConnectionAbortedError:
		stcp.close()
