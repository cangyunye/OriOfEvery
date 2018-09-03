from urllib.robotparser import RobotFileParser
#声明类
rp = RobotFileParser()
#设置robots.txt文件链接
rp.set_url('https://www.jianshu.com/robots.txt')
#读取并分析（其他操作之前必须执行）
rp.read()
#can_fetch()，传入User-agent和URL
print(rp.can_fetch('*','https://www.jianshu.com/p/ce636d6e9923'))
print(rp.can_fetch('*',"https://www.jianshu.com/search?=q=python&page=1&type=collections"))


from urllib.robotparser import RobotFileParser
from urllib.request import urlopen
#声明类
rp = RobotFileParser()
#解析robots.txt文件
rp.parse(urlopen('https://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('*','https://www.jianshu.com/p/ce636d6e9923'))
print(rp.can_fetch('*',"https://www.jianshu.com/search?=q=python&page=1&type=collections"))