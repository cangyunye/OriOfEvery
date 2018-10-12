from bs4 import BeautifulSoup
#从HTML文件读取内容
# Soup = BeautifulSoup(open("index.html"))
#读取HTML格式的内容
# Soup = BeautifulSoup("<html>data</html>")
#BeautifulSoup将HTML文档转换成Unicode格式,由于未指定解析器，会选择对应markup内容（即HTML代码部分）的最佳解析器
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span>Elsie</span></a>
<a href="http://example.com/lacie" class="sister" id="link2"><span>Lacie</span></a> and
<a href="http://example.com/tillie" class="sister" id="link3"><span>Tillie</span></a>
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
Soup = BeautifulSoup(html_doc,'lxml')
#打印title节点
print("节点所有元素:",Soup.title)
#打印title属性的类型为Tag
print(type(Soup.title))
print("title节点的值:",Soup.title.string)
print("head节点:",Soup.head)
print("p节点:",Soup.p)
print("节点名称:",Soup.title.name)
print("p节点属性:",Soup.p.attrs)
print("p节点class属性:",Soup.p.attrs["class"])
print("p节点class属性:",Soup.p["class"])