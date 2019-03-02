import requests
import random
from pyquery import PyQuery as pq
from urllib.parse import urljoin
from time import sleep


def get_html(url):
	#
	try:
		user_agent_list = [
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
			"Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
			"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
			"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
			"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
			"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
			"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
			"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
		]

		headers = {
			'user-agent': random.choice(user_agent_list)
		}

		rg = requests.get(url,headers=headers)
		if rg.status_code == 200:
			return rg.text
	except Exception as e:
		print(e)
		return None



def getmipu_proxies(html):
	iphosttpye = []
	doc = pq(html)
	# print(doc('table'))
	ip = doc('tbody .tbl-proxy-ip').items()
	port = doc('tbody .tbl-proxy-port img').items()
	protocol = doc('tbody .tbl-proxy-type').items()
	mipu_base = 'https://proxy.mimvp.com/'
	for i in range(10):
		# print("{}:{}|{}".format(ip.__next__().text(),urljoin(mipu_base,port.__next__().attr('src')),protocol.__next__().text()))
		iphosttpye.append([ip.__next__().text(),urljoin(mipu_base,port.__next__().attr('src')),protocol.__next__().text()])
	return iphosttpye

def getkdl_proxies(html):
	iphosttpye = []
	doc = pq(html)
	for i in doc('tbody tr').items():
		# print("{}:{}|{}".format(i('td').eq(0).text(),i('td').eq(1).text(),i('td').eq(3).text()))
		iphosttpye.append([i('td').eq(0).text(),i('td').eq(1).text(),i('td').eq(3).text()])
	return iphosttpye




def write_file(content):
	# 写入保存
	with open('proxies.csv','a') as pr:
		for line in content:
			# print(line)
			pr.writelines(line[0]+","+line[1]+","+line[2]+"\n")


if __name__ == '__main__':
	"""
	mipukaifangdaili = 'https://proxy.mimvp.com/free.php'
	mipu_base='https://proxy.mimvp.com/'
	# mipusmhttp = 'https://proxy.mimvp.com/freesecret.php?proxy=in_hp'
	# mipusmsocks = 'https://proxy.mimvp.com/freesecret.php?proxy=in_socks'
	mipusmfreeputong = 'https://proxy.mimvp.com/freeopen.php?proxy=in_tp'
	mipusmfreenimin = 'https://proxy.mimvp.com/freeopen.php?proxy=in_hp'
	mipusmfreesocks = 'https://proxy.mimvp.com/freeopen.php?proxy=in_socks'
	mipus=[mipusmfreeputong,mipusmfreenimin,mipusmfreesocks]
	# 提取代理html
	for url in mipus:
		testhtml=get_html(url)
		struct=getmipu_proxies(testhtml)
		write_file(struct)
	"""
	kdlnimin='https://www.kuaidaili.com/free/inha/1/'
	kdlpt='https://www.kuaidaili.com/free/intr/1/'
	kdl=[kdlnimin,kdlpt]
	# 提取代理html
	for url in kdl:
		testhtml=get_html(url)
		struct=getkdl_proxies(testhtml)
		write_file(struct)
		sleep(2)#必须加，网站有请求间隔限制，不然无法返回正确值
	print("代理刷新完成")