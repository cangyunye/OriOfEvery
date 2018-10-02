from urllib import request,error
try:
    #打开不存在页面
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
    #返回错误原因
    print(e.reason)
    #返回错误码
    print(e.code)
    #返回请求头
    print(e.headers)

from urllib import request,error
try:
    #打开不存在页面
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    #返回错误原因
    print(e.reason)
    #返回错误码
    print(e.code)
    #返回请求头
    print(e.headers)

import socket
import urllib.request
import urllib.error
try:
    response = urllib.request.urlopen('https://www.baidu.com',timeout=0.01)
except urllib.error.URLError as e:
    print(e.reason)
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')