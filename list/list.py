"""
    list.append(x) 将x添加到列表末尾
    list.sort()对列表元素排序
    list.reverse()将列表元素逆序
    list.index(x)返回第一次出现元素x的索引值
    list.insert(i,x)在位置i处插入新元素x
    list.count(x)返回元素x在列表中的数量
    list.remove(x)删除列表中第一次出现的元素x
    list.pop(i)取出列表中i位置上的元素，并将其删除
"""
l1=[1,3,5,7,9]
l2=[2,4,6,8,0]
l3=list ( range (1,31) )
print('l1={}\nl2={}\n'.format(l1,l2))
print("1 in l1=",1 in l1)
print("3 in l2=",3 in l2)
print("l1+l2=",l1+l2)
print("l1*3",l1*3)
l1.append(11)
print("After l1.append(11)\n",l1)
print("list ( range (1,31) )\n",l3)
print('2 in l2=','2' in l2)
