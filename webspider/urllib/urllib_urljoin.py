from urllib.parse import urljoin
print(urljoin('http://www.baidu.com','FAQ.html'))
print(urljoin('http://www.baidu.com','https://www.python.org/downloads/release/python-370/'))
print(urljoin('https://docs.python.org/','3.8/whatsnew/3.8.html#new-features'))
print(urljoin('https://docs.python.org/???','3.8/whatsnew/3.8.html#new-features'))