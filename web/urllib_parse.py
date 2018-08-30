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