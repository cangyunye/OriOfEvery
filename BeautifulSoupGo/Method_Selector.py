from bs4 import BeautifulSoup
html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
    <ul class="list" id="list-1">
        <li class="element">Foo</li>
        <li class="element">Bar</li>
        <li class="element">Jay</li>
    </ul>
    <ul class="list list-small" id="list-2">
        <li class="element">Foo</li>
        <li class="element">Bar</li>
    </ul>
    </div>
</div>
'''
Soup = BeautifulSoup(html,'lxml')
#name参数可以输入Tag,返回为列表元素为bs4.element.Tag，故继承Tag搜索方法
print(Soup.find_all(name='ul'))

for ul in Soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)
#attrs参数输入是字典类型，{属性:值}，返回列表元素为bs4.element.Tag
print(Soup.find_all(attrs={'id':'list-1'}))
#text传入匹配节点的文本，可以是正则表达式
htmlZ='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <a>hello,I'm study Machine Learning!</a>
        <a>hello,I'm study Deep Learning!</a>
    </div>
 </div>
'''
import re
SoupZ=BeautifulSoup(htmlZ,'lxml')
SoupZ.find_all(text=re.compile('Learning'))