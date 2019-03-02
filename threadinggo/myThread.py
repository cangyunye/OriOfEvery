import threading
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
