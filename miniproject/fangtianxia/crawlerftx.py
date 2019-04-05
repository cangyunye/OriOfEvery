import requests
import re
from pyquery import PyQuery as pq
import random
from collections import namedtuple
from pprint import pprint


class crawlerftx():
	def __init__(self):
		# 房天下广州楼盘
		self.baseurl = 'https://gz.newhouse.fang.com/house/s/'
		self.user_agent_list = [
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
		self.headers = {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Host': 'xiangjiangtianfu.fang.com',
			'Referer': 'http://gz.newhouse.fang.com/house/s/',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': random.choice(self.user_agent_list)
		}

	def ftxparser(self, url):
		# 房天下页面解码
		rq = requests.get(url, headers=self.headers)
		doc = pq(rq.content.decode('gb18030'))
		return doc

	def navparser(self, doc):
		# 导航栏链接（楼盘详情页，楼盘户型页）
		nav = doc('#orginalNaviBox a')
		url_detail = 'https:'+nav.eq(1).attr('href')
		url_huxing = 'https:'+nav.eq(2).attr('href')
		navigator = namedtuple("navigator", ['detail', 'type'])
		return navigator(url_detail, url_huxing)

	def lphomepage(self, doc):
		# 楼盘首页
		info = doc('body > div.main_1200.tf > div.firstbox > div.firstright.fr > div.information')
		hsname = info('.inf_left1 .tit strong').text()
		alias = info('.inf_left1 .tit span').eq(0).text()
		rank = info('.inf_left1 .tit a').text()
		price = doc('.information_li.mb5 .prib.cn_ff').text()
		price_detail = doc('.fnzoushi01').text()
		hp = namedtuple(
			'homepage', ['hsname', 'alias','rank', 'price', 'pricedetail'])
		return hp(hsname, alias, rank,price, price_detail)

	def lpdetailpage(self, doc):
		information = {}
		# 楼盘详情页
		# 基本信息
		basic_info = doc(".main-item").eq(0)
		price = basic_info(".main-info-price")('em').text()
		comment_href = basic_info(".main-info-comment")('a').attr('href')
		comment = basic_info(".main-info-comment")('span').eq(2).text()
		list_clearfixb = basic_info("ul li")  # basic_info(".list.clearfix")
		wuyetype = list_clearfixb.eq(0)(".list-right").text()
		projectfeature = list_clearfixb.eq(1)(".list-right")(".tag").text()
		archtype = list_clearfixb.eq(2)(".list-right").text()
		fitment = list_clearfixb.eq(3)(".list-right").text()
		chanquan = list_clearfixb.eq(4)(".list-right").text()
		developer = list_clearfixb.eq(6)(".list-right-text").text()
		address = list_clearfixb.eq(7)(".list-right-text").text()
		bdtp = namedtuple('basic', ['price', 'comment_href', 'comment',
									'wuyetype', 'projectfeature', 'archtype', 'fitment', 'chanquan', 'developer', 'address'])
		information['basic'] = bdtp(price, comment_href, comment,
									wuyetype, projectfeature, archtype, fitment, chanquan, developer, address)

		# 销售信息
		sale_info = doc(".main-item").eq(1)
		list_clearfixs = sale_info(".list.clearfix")('li')
		sale_status = list_clearfixs.eq(0)(".list-right").text()
		discounts = list_clearfixs.eq(1)(".list-right").text()
		opdate = list_clearfixs.eq(2)(".list-right").text()
		completiondate = list_clearfixs.eq(3)(".list-right").text()
		salesaddr = list_clearfixs.eq(4)(".list-right").text()
		advisory = list_clearfixs.eq(5)(".list-right").text()
		mainhousetype = list_clearfixs.eq(6)(".list-right-text").text()
		sdtp = namedtuple('sale', ['sale_status', 'discounts', 'opdate',
								   'completiondate', 'salesaddr', 'advisory', 'mainhousetype'])
		information['sale'] = sdtp(
			sale_status, discounts, opdate, completiondate, salesaddr, advisory, mainhousetype)

		# 周边设施
		surroundingfacility = doc(".main-item").eq(2)
		list_clearfixf = surroundingfacility(".sheshi_zb")('li')
		traffic = list_clearfixf.eq(0).text()
		kindergarten = list_clearfixf.eq(1).text()
		education = list_clearfixf.eq(2).text()
		univercity = list_clearfixf.eq(3).text()
		coodepartment = list_clearfixf.eq(4).text()
		hospital = list_clearfixf.eq(5).text()
		bank = list_clearfixf.eq(6).text()
		rest = list_clearfixf.eq(7).text()
		facilities = list_clearfixf.eq(8).text()
		fdtp = namedtuple('facility', ['traffic', 'kindergarten', 'education',
									   'univercity', 'coodepartment', 'hospital', 'bank', 'rest', 'facilities'])
		information['facility'] = fdtp(
			traffic, kindergarten, education, univercity, coodepartment, hospital, bank, rest, facilities)
		return information

	def housetype(self, url):
		# 户型页，但是以下参数需要进行人工拼接
		query_string = {
			'newcode': 2812199376,
			'count': 'false',
			'start': 12,
			'limit': 12,
			'room': 'all',
			'city': '%E5%B9%BF%E5%B7%9E'
		}
		url_house = url+"house/ajaxrequest/householdlist_get.php?"
		headers = {
			'Referer': 'https://xiangjiangtianfu.fang.com/photo/list_900_2811174364.htm',
			'User-Agent': random.choice(self.user_agent_list),
			'x-requested-with': 'XMLHttpRequest'
		}
		houses_ajax = requests.get(
			url_house, params=query_string, headers=headers)
		return houses_ajax


def main():
	# 定位楼盘首页
	url = 'http://xiangjiangtianfu.fang.com/'
	ftx = crawlerftx()
	doc = ftx.ftxparser(url)
	hp = ftx.lphomepage(doc)
	pprint(hp)
	nav = ftx.navparser(doc)
	url_detail, url_huxing = nav.detail, nav.type
	print(url_detail, '\n', url_huxing)
	doc_d = ftx.ftxparser(url_detail)
	doc_h = ftx.ftxparser(url_huxing)
	lp = ftx.lpdetailpage(doc_d)
	pprint(lp)

if __name__ == "__main__":
	main()
