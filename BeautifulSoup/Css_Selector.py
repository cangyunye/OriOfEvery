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
#关于CSS选择器，参考http://www.w3school.com.cn/cssref/css_selectors.asp
#我们仅调用select()方法，传入为CSS选择器
#selector=".class"，选择class="panel"的类，再选择其下class="panel-heading"
print(Soup.select('.panel .panel-heading'))
#选择标签ul之下li标签
print(Soup.select('ul li'))
#选择id="list-2",class="element"
print(Soup.select('#list-2 .element'))
print(type(Soup.select('ul')[0]))

#选择所有ul节点后选择之下li节点
for ul in Soup.select('ul'):
    print(ul.select('li'))


#对Tag元素获取属性
for attr in (map(lambda x:x['id'],Soup.select('ul'))):
    print(attr)

#get_text()或者string获取文本
for li in Soup.select('li'):
    print('Get Text:',li.get_text())
    print('String:',li.string)