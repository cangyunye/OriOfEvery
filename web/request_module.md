
# requests多种常用方法


```python
import requests
r = requests.post('http://httpbin.org/post')
print(r.text)
r = requests.put('https://httpbin.org/put')
print(r.text)
r = requests.delete('https://httpbin.org/delete')
print(r.text)
r = requests.head('https://httpbin.org/get')
print(r.text)
r = requests.options('https://httpbin.org/get')
print(r.text)
```

# GET请求


```python
# -*- coding:utf-8 -*-
import requests
r = requests.get('https://www.baidu.com')
# 查看requests.get返回类型
print(type(r))
# 查看状态码
print(r.status_code)
# 查看请求的网页
print(r.text)
# 打印cookies
print(tuple(r.cookies))
```

> 通过get()方法实现请求，查询name=myu,age=21，可以直接输入
> r = requests.get('https://httpbin.org/get?name=myu&age=21')
> 由于get后返回为str类型的JSON格式
> 使用json()方法，可以转换为字典格式
> 如果返回的结果不是JSON格式，则会出现解析错误。


```python
import requests
data = {
    'name':'myu',
    'age':21
}
r = requests.get('https://httpbin.org/get',params=data)
#查看请求的网页
print(r.url)
print(r.text)
print(r.json())
```

```json
https://httpbin.org/get?name=myu&age=21
{
  "args": {
    "age": "21", 
    "name": "myu"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.4"
  }, 
  "origin": "211.97.11.16", 
  "url": "https://httpbin.org/get?name=myu&age=21"
}

{'args': {'age': '21', 'name': 'myu'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.18.4'}, 'origin': '211.97.11.16', 'url': 'https://httpbin.org/get?name=myu&age=21'}
```


# 从知乎的发现页找寻内容


```python
import requests
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML,like Gecko) chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore',headers=headers)
#re.S表示匹配除\n换行符外的任何字符，即不是每行单独匹配，而是整体匹配
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
print(r.text)
titles = re.findall(pattern,r.text)
print(titles)

```

根据一下内容涉及寻找特征pattern
```html
<div class="explore-feed feed-item" data-offset="1">
<h2><a class="question_link" href="/question/33313490/answer/487565704" target="_blank" data-id="5532014" data-za-element-name="Title">
有哪些吃西餐时非常 low 的行为？
</a></h2>
```

# 抓取二进制数据
图片、音频、视频这些文件本质上是二进制码，根据特定的解析方式才形成我们看到的多媒体。


```python
# 以bilibili站点图标为例
import requests
r = requests.get("https://www.bilibili.com/favicon.ico")
print(r.text)
print(r.content)
# 保存图标,wb为写入二进制格式
with open('favicon.ico','wb') as f:
    f.write(r.content)
```

```python
>>> print(r.text)
  ╔ ╔     ╔   จ     (       @   ╔

                                                       ��� ��� ��� ��� ��� ��� �
�� ��� ��� ��� ��� ��� ��� ��� ��� ��� ��� ��� ��� ��� ��� ��

>>> print(r.content)
b'\x00\x00\x01\x00\x01\x00  \x00\x00\x01\x00 \x00\xa8\x10\x00\x00\x16\x00\x00\x00(\x00\x00\x00 \x00\x00\x00@\x00\x00\x00\x01\x00 \x00\x00\x00\x00\x00\x00\x10\x00\x00\x13\x0b\x00\x00\x13\x0b\x00\x00\x00\x00\x00\x0
```
如上即为图标的二进制格式

# POST请求


```python
import requests
data = {
    'name':'myu',
    'age':21
}
r = requests.post('http://httpbin.org/post',params=data)
print(r.text)
print(r.url)
print(r.history)
```

    {
      "args": {
        "age": "21", 
        "name": "myu"
      }, 
      "data": "", 
      "files": {}, 
      "form": {}, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Connection": "close", 
        "Content-Length": "0", 
        "Host": "httpbin.org", 
        "User-Agent": "python-requests/2.18.4"
      }, 
      "json": null, 
      "origin": "211.97.11.16", 
      "url": "http://httpbin.org/post?name=myu&age=21"
    }
    
    http://httpbin.org/post?name=myu&age=21
    []


# requests.codes 查询

查找requests\status_codes.py 
```python

    # Informational.
    100: ('continue',),
    101: ('switching_protocols',),
    102: ('processing',),
    103: ('checkpoint',),
    122: ('uri_too_long', 'request_uri_too_long'),
    200: ('ok', 'okay', 'all_ok', 'all_okay', 'all_good', '\\o/', '✓'),
    201: ('created',),
    202: ('accepted',),
    203: ('non_authoritative_info', 'non_authoritative_information'),
    204: ('no_content',),
    205: ('reset_content', 'reset'),
    206: ('partial_content', 'partial'),
    207: ('multi_status', 'multiple_status', 'multi_stati', 'multiple_stati'),
    208: ('already_reported',),
    226: ('im_used',),
        ******
```


```python
requests.codes.ok
```




    200




```python
requests.codes.not_found
```




    404




```python
requests.codes.switching_protocols
```




    101



# 文件上传


```python
import requests
files = {'file':open('favicon.ico','rb')}
r = requests.post("http://httpbin.org/post",files=files)
print(r.text)
```

以前文下载的favicon.ico为例，继续上传favicon.ico，返回response的Files部分即上传文件
```json
{
  "args": {},
  "data": "",
  "files": {
    "file": "data:application/octet-stream;base64,AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAABMLAAATCwAAAAAAAAAAAAD///8A////..."
  },
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Content-Length": "4433",
    "Content-Type": "multipart/form-data; boundary=f6e8e725c80b445da8ed3f83e023418f",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.18.4"
  },
  "json": null,
  "origin": "211.97.11.16",
  "url": "http://httpbin.org/post"
}
```

# Cookies 


```python
import requests
r = requests.get('https://www.baidu.com/')
print(r.cookies)
print(tuple(r.cookies))
for key,value in r.cookies.items():
    print(key + '=' + value)

```

```python
<RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
(Cookie(version=0, name='BDORZ', value='27315', port=None, port_specified=False, domain='.baidu.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1536711758, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False),)
BDORZ=27315
```


# 使用自己的cookies登录baidu
按之前提到的方法，使用Chrome 浏览器F12，找到Network中的Headers->Request Headers->Cookie.
对于返回的结果，可以查询自己的登录信息进行验证


```python
import requests
headers = {
'Cookie': 'BAIDUID=...',
'Host': 'www.baidu.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
r = requests.get('https://www.baidu.com/',headers=headers)
print(r.text)
```




# 会话维持
为什么需要维持会话，因为，我们每次通过post和get方法模拟网页请求，实际上相当于打开了不同的会话，我们可以用cookies来保持登录到同一个会话，同样也有其他方法。 利用Session，模拟同一个会话打开同一站点的不同页面。


```python
import requests
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
```

```json
{
  "cookies": {
    "number": "123456789"
  }
}
```


    

# SSL证书验证
访问12306页面时，我们有必要忽略这个验证错误。


```python
import requests
response = requests.get('https://www.12306.cn')
print(response.status_code)
```

直接打开，会保SSLError错误，故我们需要加入verify=False来忽略验证


```python
import requests
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)
```

    200


    f:\ProgramData\Anaconda3\lib\site-packages\urllib3\connectionpool.py:858: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
      InsecureRequestWarning)


尽管忽略了验证，但同时会收到建议使用指定证书。所以我们可以设置忽略警告进行屏蔽


```python
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)
```

    200


或者通过捕获警告日志的方式忽略警告


```python
import requests
import logging
logging.captureWarnings(True)
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)
```

    200


同样也支持指定证书


```python
import requests
response = requests.get('https://www.12306.cn',cert=('/path/server.crt','/path/key'))
print(response.status_code)
```

# 使用代理
对于大规模爬取内容时，请求过多，容易导致网站弹出验证码，或者跳转到登录认证界面甚至是查封IP。因此，一定程度上需要使用代理解决本问题


```python
import requests
proxies = {
    "http":"http://user:password@10.75.171.10:8688",
}
requests.get("https://www.google.com",proxies=proxies)
```

# 超时设置
对于某些网站的爬取，如果出现服务器响应慢，为了针对报错，可以设置一个超时时间
不加参数，或者设置timeout=None则表示永远等待,timeout=(5,11)表示连接时间和读取时间


```python
import requests
response = requests.get('https://www.taobao.com/',timeout=(5,11))
print(response.status_code)
```

    200


# 身份认证
对于身份验证框的信息，可以采用如下方式直接认证


```python
import requests
from requests.auth import HTTPBasicAuth
response = requests.get('https://mail.qq.com/cgi-bin/loginpage',auth=HTTPBasicAuth('username','password'))
print(response.status_code)
#验证正确返回200，错误返回401
```

    200


# 完整数据结构的请求
利用url,data,headers构造Request对象，通过SEssion的prepare_request方法转换为Prepared Request对象，然后通过send发送


```python
from requests import Request,Session
url = 'http://httpbin.org/post'
data = {
    'name':'myu'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
s = Session()
req = Request('POST',url,data=data,headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
```

```json
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "name": "myu"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "8", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
  }, 
  "json": null, 
  "origin": "211.97.11.16", 
  "url": "http://httpbin.org/post"
}
```


    
