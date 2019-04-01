import asyncio
from collections.abc import Generator,Coroutine
import time
"""
常规协程
学习资料
https://cuiqingcai.com/6160.html
http://python.jobbole.com/88291/
http://aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html
http://python.jobbole.com/89290/

"""


async def wy(t):
    print("wy:Begin from {} sleep {}s.".format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()),t))
    await asyncio.sleep(t)
    print("wy:End sleep at {}.".format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))

# 协程顺序运行
async def main():
    print("Main Control start from {}.".format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))
    await wy(3)
    await wy(4)
    print("Main Control end at {}.".format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))


# asyncio.run(main())

# 创建task对象，让协程并发运行
async def main2():
    task = asyncio.create_task(wy(3))
    task2 = asyncio.create_task(wy(4))
    print("Main Control start from {}.".format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))
    await task
    await task2
    print("Main Control end at {}.".format(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())))

# asyncio.run(main2())


# 声明协程方法
async def lovewy():
    print("WY，加油！")

# 实例化协程方法，但并未执行
print("实例化协程方法")
lw = lovewy()
print("返回协程对象{}，但无法直接执行".format(lw))
# 注册事件循环
print("注册事件循环")
loop = asyncio.get_event_loop()

# 将协程方法加入事件循环
print("协程对象加入循环")
loop.run_until_complete(lw)
print("done")


# 通过创建Task对象，可以查看协程的状态
async def execute(x):
    print('Number:', x)
    return x
 
coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')
 
loop2 = asyncio.get_event_loop()
task2 = loop2.create_task(coroutine)
print('Task:', task2)
loop2.run_until_complete(task2)
print('Task:', task2)
print('After calling loop')

