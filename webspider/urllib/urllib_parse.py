#解析为元组
from urllib.parse import urlparse
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)
print(type(result),result[0],result.scheme)
#反解析
from urllib.parse import urlparse,urlunparse
result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)
res = urlunparse(result)
res2 = urlunparse(['https','www.baidu.com','index.html','user','a=6','comment'])
res3 = urlunparse(('https','www.baidu.com','index.html','user','a=7','comment'))
print(type(res),res)
print(type(res2),res2)
print(type(res3),res3)
#将中文编码转化为URL编码
from urllib.parse import quote
keyword = '壁纸'
url= 'https://www.baidu.com/s?wd='+quote(keyword)
print(url)
#对URL进行解码
from urllib.parse import unquote
url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))