import scrapy
class xuweiweiSpider(scrapy.Spider):
	name = "xuweiwei"
	def start_requests(self):
		urls = ["https://www.meituri.com/a/25811/",
 				"https://www.meituri.com/a/25786/",
 				"https://www.meituri.com/a/25387/",
 				"https://www.meituri.com/a/25382/",
 				"https://www.meituri.com/a/25368/",
 				"https://www.meituri.com/a/25226/",
 				"https://www.meituri.com/a/25218/",
 				"https://www.meituri.com/a/25018/",
 				"https://www.meituri.com/a/25006/",
 				"https://www.meituri.com/a/24816/",
 				"https://www.meituri.com/a/24813/",
 				"https://www.meituri.com/a/24804/",
 				"https://www.meituri.com/a/24605/",
 				"https://www.meituri.com/a/24602/",
 				"https://www.meituri.com/a/24294/",
 				"https://www.meituri.com/a/24292/",
 				"https://www.meituri.com/a/24082/",
 				"https://www.meituri.com/a/24077/",]
		for url in urls:
			yield scrapy.Request(url=url,callback=self.parse)

	def parse(self,response):
		page = response.url.split("/")[-2]
		filename = 'xuweiwei-%s.html' % page
		with open(filename,'wb') as f:
			f.write(response.body)
		self.log('Saved file %s',filename)
