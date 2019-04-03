import asyncio
import aiohttp
import time
"""
直接通过requests的get方法是不能通过await挂起异步处理的，这里需要借助aiohttp库进行异步操作。
开始运行时，时间循环会运行第一个 task，针对第一个 task 来说，
当执行到第一个 await 跟着的 get() 方法时，它被挂起，但这个 get() 方法第一步的执行是非阻塞的，
挂起之后立马被唤醒，所以立即又进入执行，创建了 ClientSession 对象，接着遇到了第二个 await，
调用了 session.get() 请求方法，然后就被挂起了，由于请求需要耗时很久，所以一直没有被唤醒，好第一个 task 被挂起了，
那接下来该怎么办呢？事件循环会寻找当前未被挂起的协程继续执行，于是就转而执行第二个 task 了，
也是一样的流程操作，直到执行了第五个 task 的 session.get() 方法之后，全部的 task 都被挂起了。
所有 task 都已经处于挂起状态，那咋办？只好等待了。3 秒之后，几个请求几乎同时都有了响应，
然后几个 task 也被唤醒接着执行，输出请求结果，最后耗时，3 秒！
"""
start = time.time()

async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    result = await response.text()
    session.close()
    return result

async def request():
    url = 'http://127.0.0.1:5000'
    print('Waiting for', url)
    result = await get(url)
    print('Get response from', url, 'Result:', result)

tasks = [asyncio.ensure_future(request()) for _ in range(5)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)