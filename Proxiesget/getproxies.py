import requests
import random
from pyquery import PyQuery as pq
from urllib.parse import urljoin



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




def get_proxies(html):
	#写入mysql的结构体
	struct2mysql = []
	# 组合成代理
	doc = pq(html)
	# print(doc('table'))
	ip = doc('tbody .tbl-proxy-ip').items()
	port = doc('tbody .tbl-proxy-port img').items()
	type = doc('tbody .tbl-proxy-type').items()
	mipu_base = 'https://proxy.mimvp.com/'
	for i in range(10):
		# print("{}:{}|{}".format(ip.__next__().text(),urljoin(mipu_base,port.__next__().attr('src')),type.__next__().text()))
		struct2mysql.append([ip.__next__().text(),urljoin(mipu_base,port.__next__().attr('src')),type.__next__().text()])
	return struct2mysql

def write_file(content):
	# 写入保存
	with open('proxies.csv','w+') as pr:
		for line in content:
			print(line)
			pr.writelines(line[0]+","+line[1]+","+line[2]+"\n")


if __name__ == '__main__':
	# 代理网址
	mipukaifangdaili = 'https://proxy.mimvp.com/free.php'
	mipu_base='https://proxy.mimvp.com/'
	mipusmhttp = 'https://proxy.mimvp.com/freesecret.php?proxy=in_hp'
	mipusmsocks = 'https://proxy.mimvp.com/freesecret.php?proxy=in_socks'
	mipus=[mipusmhttp,mipusmsocks]
	# 提取代理html
	for url in mipus:
		testhtml=get_html(url)
		struct=get_proxies(testhtml)
		write_file(struct)