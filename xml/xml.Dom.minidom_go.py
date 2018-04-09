# import os
import xml.dom.minidom
import os
xmlpath = 'F:\\DreamToDream\\OnMyWay\\Programming\\Python\\xml'
os.chdir(xmlpath)
filename = 'WorkforDom.xml'
# os.path.abspath()
#读取dom对象
# print(os.getcwd())
# print(filename)
print(f'调试:{os.path.join(os.getcwd(),filename)}')
dom = xml.dom.minidom.parse(filename)
#获取文档元素对象
# print(dom)
root = dom.documentElement
print('调试root:',root)


table = root.getElementsByTagName('Ticket Number')
print('调试table:', table)
# name = table.getElementsByTagName("Name")[0]
for node in dom.childNodes:
    print(node.nodeName)
    for model in node.childNodes:
        print(model.nodeName)
        #得到子节点，保证节点的类型
        if model.nodeType in (node.ELEMENT_NODE, node.CDATA_SECTION_NODE, node.TEXT_NODE):
            #获取属性
            sCat = model.getAttribute('Ticket Number')
