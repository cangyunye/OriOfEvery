import matplotlib.pyplot as plt
print(range(1,10))
print(type(range(1,10)))
for i in list(range(1,10)):
    print(i)
l1 = list(range(1,10))
l2 = list(range(1,10))
l3 = dict(zip(l1,l2))
print(l3)
for x,y in l3.items():
    plt.scatter(x,y)
plt.show()
for char in 'liangdianshui' :
    print ( char , end = ' ' )
print('\n')
#列表生成式，从右往左读取
[x * x for x in range(1, 11) if x is not None]
[m + n for m in 'ABC' for n in 'XYZ']
#生成器g
g = (x * x for x in range(10))
[x  for x in g if x < 50 ]
