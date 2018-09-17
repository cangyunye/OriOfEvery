[TOC]
### 通过GET方式获取网页
```python
import urllib.request
#urlopen仅传递网页参数时为GET方法
response = urllib.request.urlopen('https://www.python.org')
#打印网页源码
print(response.read().decode('utf-8'))
#查看类型
print(type(response))
#查看urlopen类的使用方法
help(type(response))
#返回码
print(response.status)
#响应头head信息
print(response.getheaders())
print(dict(response.getheaders())['Server'])
```
> 那么这里print出来的结果就是HTML网页源码了，截取部分
```HTML
<!doctype html>
<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
<!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]-->

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">

    <meta name="application-name" content="Python.org">
    <meta name="msapplication-tooltip" content="The official home of the Python Programming Language">
    <meta name="apple-mobile-web-app-title" content="Python.org">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
```

### 通过POST形式发送数据到指定地址
```python
import urllib.request
import urllib.parse
#data为二进制字节流数据
data = bytes(urllib.parse.urlencode({'word':'help'}),encoding='utf-8')
print(data)
#urlopen指定data参数时，使用POST方法
response=urllib.request.urlopen('http://httpbin.org/post',data=data)
rd=response.read()
#打印返回信息
print(rd.decode('utf-8'))
```
### 指定浏览器User-Agent和URL地址
>Request必须使用bytes类型，因此使用parse的urlencode编码

```python
from urllib import request,parse
url = 'http://httpbin.org/post'
headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Host':'httpbin.org'
    }
    dict1 = {
        'name' : 'Germey'
    }
data = bytes(parse.urlencode(dict1),encoding='UTF-8')
req = request.Request(url=url,data=data,headers=headers,method='POST')
#如果没定义headers可以使用
#req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
```

