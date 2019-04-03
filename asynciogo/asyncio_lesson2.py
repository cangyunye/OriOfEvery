"""
在调用协程之后，如requests请求网页之后，打印请求状态。
首先，封装callback() 方法实现获取请求状态
再调用 task对象add_done_callback() 方法传入callback
这样当 task 执行完毕之后就可以调用 callback() 方法了，
同时 task 对象还会作为参数传递给 callback() 方法，
调用 task 对象的 result() 方法就可以获取返回结果了。
"""
import asyncio
import requests


async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status


def callback(task):
    print('Status:', task.result())

coroutine = request()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)
