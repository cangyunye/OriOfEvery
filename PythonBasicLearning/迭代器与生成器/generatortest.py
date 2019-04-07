"""
    创建生成器
    第一种方法：把一个列表生成式的[]改成()，就创建了一个generator
    第二种方法：在一个普通函数中使用yield，类似断点，效果，每次next(函数)时，依次到yield进行返回
    第三种方法：iter()，直接将其他迭代对象Iterable转换为Iterator迭代器
    Iterator可以被next()调用
    凡是可作用于for循环的对象都是Iterable类型；
    凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
    集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
    Python的for循环本质上就是通过不断调用next()函数实现的
"""
#列表生成器
L = [x * x for x in range(10)]
#创建生成器
g = (x * x for x in range(10))
#获得生成器的返回值
next(g)
#generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

#常规调用方法，即直接循环调用
[x for x in g ]
#如第2次再调用，则结果为[]
[x for x in g]
#重置g生成器
g = (x * x for x in range(10))
#只打印部分
[x  for x in g if x < 50 ]
#处理尽头之后无法再调用的异常
"""
>>> while True:
...     try:
...         x = next(g)
...         print('g:', x)
...     except StopIteration as e:
...         print('Generator return value:', e.value)
...         break
"""
