"""
    散点图
    pyplot.scatter(x,y)
"""
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
