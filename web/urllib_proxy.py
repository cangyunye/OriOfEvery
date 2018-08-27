#本地搭建代理访问网页
from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener
proxy_handler = ProxyHandler({
    'http':'http://127.0.0.9743',
    'https':'http://127.0.0.9743'
})
opener = build_opener(proxy_handler)
try :
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)