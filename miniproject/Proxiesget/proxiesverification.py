#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import requests
from pyquery import PyQuery as pq

# config-start
testUrl = "https://www.ipip.net/ip.html/"
timeout = 10  # 设置超时
threadNumber = 50  # 设置线程数
proxiesFileName = "proxies.csv"
successFileName = "success.txt"
# config-end
headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1'
}
def ipok(content):
	#返回本机上网ip
	doc = pq(content)
	ip = doc('table tr a').eq(0).text()
	return ip

def verificate(ip,port,protocol):
	'''
	测试HTTP代理是否可用
		在响应的页面中寻找本机IP , 如果找到 , 则说明代理可以成功连接
	'''
	global successFileName
	global testUrl
	global timeout

	if protocol == "HTTPS":
		proxies = {"http":"http://"+ip+":"+port,"https":"http://"+ip+":"+port}
	elif protocol == "SOCKS5":
		proxies = {"http":"socks5://"+ip+":"+port,"https":"socks5://"+ip+":"+port}
	else: # 不指定协议时使用HTTP协议
		proxies = {"http":"http://"+ip+":"+port,"https":"http://"+ip+":"+port}

	try:
		content=requests.get(testUrl,headers=headers,proxies=proxies,timeout=timeout)
		if ipok(content.text) == ip:
			print(ip+":"+port+"@"+protocol)
			with open(successFileName,"a+") as file:
				file.write(ip+":"+port+"@"+protocol+"\n")
		else:
			print("Proxy{}:{},{} Error...".format(ip,port,protocol))
	except Exception as e:
		# print() e
		print("NetWork{}:{},{} Error...".format(ip,port,protocol))

class myThread (threading.Thread):
	def __init__(self, ip, port, protocol):
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.protocol = protocol
	def run(self):
		verificate(self.ip,self.port,self.protocol)


threads = [] # 线程池
f_p = open(proxiesFileName,'r')
f_proxies=f_p.readlines()
for line in f_proxies:
	ip,port,protocol=line.split(',')
	if len(port)> 5:
		continue
	threads.append(myThread(ip, port, protocol))
f_p.close()

for t in threads:
	t.start()
	while True:
		if(len(threading.enumerate())<threadNumber):
			break
