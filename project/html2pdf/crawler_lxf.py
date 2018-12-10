from __future__ import unicode_literals
import logging
import os
import re
import time
from urllib.parse import urlparse


import pdfkit
import requests
from bs4 import BeautifulSoup

import functools
import random
from time import sleep

def delay(func):
	"""
	random time for sleep as decorator
	"""
	@functools.wraps(func)
	def wrapper(*args,**kw):
		# sleep(random.sample([t for t in range(3)],1))
		delaytime = random.uniform(3,6)
		sleep(delaytime)
		print('delaytime:{}'.format(delaytime))
		return func(*args,**kw)
	return wrapper

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""


class Crawler(object):
	"""
	爬虫基类
	"""
	def __init__(self,name,start_url):
		"""
		:param name:将要被保存为PDF的文件名称
		:param start_url: 爬虫入口URL
		"""
		self.name = name
		self.start_url = start_url
		self.domain = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(self.start_url))



	@staticmethod
	@delay
	def request(url):
		"""
		网络请求，返回response对象
		:param url:
		:param kwargs:
		:return:
		"""
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

		#代理池https://www.kuaidaili.com/free/
		# proxyip = ['47.94.104.204:8118','124.206.133.227:80']
		# proxies = {'http':str(random.choice(proxyip))}

		response = requests.get(url,headers=headers)
		if response.status_code == 503:
			slt=random.uniform(3,6)
			print('遭遇反爬机制503，休息{}s'.format(slt))
			sleep(slt)
			response = Crawler.request(url)
		return response

	def parse_menu(self,response):
		"""
		从response中解析出所有目录的URL链接
		:param response:
		:return:
		"""
		raise NotImplementedError

	def parse_body(self,response):
		"""
		解析正文，由子类实现
		:param response:爬虫返回的response对象
		:return: 返回经过处理的html正文文本
		"""
		raise NotImplementedError

	def run(self):
		start = time.time()
		#pdfkit配置
		options = {
			'page-size':'Letter',
			'margin-top':'0.75in',
			'margin-right':'0.75in',
			'margin-bottom':'0.75in',
			'margin-left':'0.75in',
			'encoding':"UTF-8",
			'custom-header':[
				('Accept-Encoding','gzip')
			],
			'cookie':[
				('cookie-name1','cookie-value1'),
				('cookie-name2','cookie-value2'),
			],
			'outline-depth':10,
		}
		htmls = []

		urls = [url for url in self.parse_menu(self.request(self.start_url))]

		for index,url in enumerate(urls):
			f_name = ".".join([str(index),"html"])
			# 判断文件是否已存在，存在则continue跳过
			if os.path.exists(f_name):
				print("{}已经存在,处理下一页".format(f_name))
				continue
			html = self.parse_body(self.request(url))
			with open(f_name,'wb') as f:
				f.write(html)
			htmls.append(f_name)
			print("{}加载完成".format(f_name))
		pdfkit.from_file(htmls, self.name + ".pdf", options=options)
		for html in htmls:
			os.remove(html)
		total_time = time.time() - start
		print(u"总共耗时:%f 秒"%total_time)

class LiaoxuefengPythonCrawler(Crawler):
	"""
	廖雪峰Python3教程
	"""
	def parse_menu(self,response):
		"""
		解析目录结构，获取所有URL目录列表
		:param response: 爬虫返回的response对象
		:return: url生成器
		"""
		soup = BeautifulSoup(response.content,"html.parser")
		menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]#导航栏
		for li in menu_tag.find_all("div"):
			url = li.a.get("href")
			if not url.startswith("http"):
				url = "".join([self.domain,url])
			yield url


	def parse_body(self,response):
		"""
		解析正文
		:param response:爬虫返回的response对象
		:return: 返回处理后的html文本
		"""
		try:
			soup = BeautifulSoup(response.content,'html.parser')
			body = soup.find_all(class_="x-wiki-content x-main-content")[0]

			# 加入标题，居中显示
			# 获取原来的h4标题
			title = soup.find('h4').get_text()
			# 新建标签center
			center_tag = soup.new_tag("center")
			# 新建标签h1
			title_tag = soup.new_tag('h1')
			title_tag.string = title
			center_tag.insert(1,title_tag)
			body.insert(1,center_tag)

			html = str(body)
			# body中的img标签的src相对路径的改成绝对路径
			pattern = "(<img .*?src=\")(.*?)(\")"

			def func(m):
				if not m.group(2).startswith("http"):
					rtn = "".join([m.group(1),self.domain,m.group(2),m.group(3)])
					return rtn
				else:
					return "".join([m.group(1),m.group(2),m.group(3)])
			html = re.compile(pattern).sub(func,html)
			html = html_template.format(content=html)#重置初始化模板
			html = html.encode("utf-8")
			return html
		except Exception as e:
			logging.error("解析错误",exc_info=True)

if __name__ == '__main__':
	start_url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
	crawler = LiaoxuefengPythonCrawler("廖雪峰Python3",start_url)
	crawler.run()