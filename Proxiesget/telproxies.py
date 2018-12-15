import telnetlib
#快代理https://www.kuaidaili.com/free/
def demo_test():
	proxyipinfo = """111.160.236.84	40610	高匿名	HTTP	天津市天津市 联通	2秒	2018-12-15 21:30:57
	47.96.148.248	8118	高匿名	HTTP	中国 浙江 杭州 阿里云	1秒	2018-12-15 20:30:55
	47.95.9.128	8118	高匿名	HTTP	中国 北京 北京 阿里云	2秒	2018-12-15 19:30:58
	183.230.145.112	8888	高匿名	HTTP	重庆市重庆市 移动	1秒	2018-12-15 18:30:59
	106.2.1.5	3128	高匿名	HTTP	北京市朝阳区 迅达云 BGP多线	0.3秒	2018-12-15 17:31:00
	115.223.246.239	9000	高匿名	HTTP	浙江省温州市 电信	3秒	2018-12-15 16:30:59
	115.210.31.75	9000	高匿名	HTTP	浙江省金华市 电信	2秒	2018-12-15 15:30:59
	180.118.134.73	9000	高匿名	HTTP	中国 江苏省 镇江市 电信	3秒	2018-12-15 14:31:00
	115.218.216.23	9000	高匿名	HTTP	浙江省温州市 电信	1秒	2018-12-15 13:31:00
	124.235.135.87	80	高匿名	HTTP	吉林省长春市 电信	3秒	2018-12-15 12:31:00
	59.37.33.62	50686	高匿名	HTTP	广东省惠州市 电信	3秒	2018-12-15 11:30:59
	118.24.61.165	8118	高匿名	HTTP	中国 四川 成都 电信	0.4秒	2018-12-15 10:30:58
	119.51.89.18	1080	高匿名	HTTP	吉林省长春市 联通	2秒	2018-12-15 09:30:59
	115.223.207.144	9000	高匿名	HTTP	浙江省温州市 电信	0.9秒	2018-12-15 08:30:56
	117.87.177.179	9000	高匿名	HTTP	江苏省徐州市 电信	3秒	2018-12-15 07:31:00"""
	proxyipinfo=[x.strip().split() for x in proxyipinfo.split('\n') if len(x)>0]

	for line in proxyipinfo:
		print(line)
	proxyusable=[]

	for i in range(len(proxyipinfo)):
		ip=proxyipinfo[i][0]
		port=proxyipinfo[i][1]
		types=proxyipinfo[i][3]
		try:
			print(f"{ip}:{port}".format(ip, port))
			telnetlib.Telnet(ip, port=port, timeout=20)
		except:
			print('connect failed')
		else:
			print('success')
			proxyusable.append([ip,port])
	print(proxyusable)


def test_proxies(ip, port):
	proxyusable = []
	try:
		print(f"{ip}:{port}".format(ip, port))
		telnetlib.Telnet(ip, port=port, timeout=20)
	except:
		print('connect failed')
	else:
		print('success')
		proxyusable.append([ip, port])
	return proxyusable


if __name__ == '__main__':
	demo_test()
	# test_proxies(ip, port)