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
"""
列表推导式（list comprehensions）
列表推导式（又称列表解析式）提供了一种简明扼要的方法来创建列表。
它的结构是在一个中括号里包含一个表达式，然后是一个for语句，然后是0个或多个for或者if语句。那个表达式可以是任意的，意思是你可以在列表中放入任意类型的对象。返回结果将是一个新的列表，在这个以if和for语句为上下文的表达式运行完成之后产生。
规范
"""
#variable = [out_exp for out_exp in input_list if out_exp == True]

# 这里是另外一个简明例子:
multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)
# Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

# 双层或多层循环
mulcircle = [m + n for m in 'ABC' for n in 'EFG']
print(mulcircle)
# 输出了所有可能的组合