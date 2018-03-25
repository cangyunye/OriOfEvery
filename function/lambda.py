"""
lambda简单应用
函数名 = lambda 参数 : 表达式
直接返回表达式
"""
inp = input('输入数值:')
inp = eval(inp)
pts = lambda x,y: x * 30-y
print('数值扩大30倍-y：',pts(inp,inp))

"""
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
"""
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
