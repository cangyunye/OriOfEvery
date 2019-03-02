from bs4 import BeautifulSoup
html="""<body>
<p class="story">Once upon a time there were three little sisters; and their names were
<a class="sister" href="http://example.com/elsie" id="link1"><span>Elsie</span></a><a class="sister" href="http://example.com/lacie" id="link2"><span>Lacie</span></a> and
<a class="sister" href="http://example.com/tillie" id="link3"><span>Tillie</span></a>
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
"""
Soup=BeautifulSoup(html,'lxml')

print("基点\n",Soup.p)
#直接输入p下节点b
print(Soup.p.b)
#输入contents，返回直接子节点列表形式，不对子孙节点再划分
print("contents直接子节点:\n",Soup.p.contents)
#输入children，返回直接子节点生成器
print("children直接子节点生成器:\n",Soup.p.children)
print("children:\n",list(Soup.p.children))
#输入descendants，返回向下级递归生成器,包含每个下级直到最终的值，含所有子孙节点
print("descendants下级递归生成器:\n",Soup.p.descendants)
print("descendants:\n",list(Soup.p.descendants))


print("基点\n",Soup.a)
#输入parent，a的父节点升级到其p节点
print("父节点\n",Soup.a.parent)
print("父之父节点\n",Soup.a.parent.parent)
#输入parents，返回a的所有祖先节点
print("parents上级递归生成器点\n",Soup.a.parents)


print("基点\n",Soup.a)
#输入next_sibling，a的后向兄弟节点
print("后向兄弟节点\n",Soup.a.next_sibling)
#输入next_siblings，a的后向兄弟节点生成器
print("后向兄弟节点生成器\n",list(enumerate(Soup.a.next_siblings)))
#输入previous_sibling，a的前向兄弟节点
print("前向兄弟节点\n",Soup.a.previous_sibling)
#输入previous_siblings，a的前向兄弟节点生成器
print("前向兄弟节点\n",list(enumerate(Soup.a.previous_siblings)))