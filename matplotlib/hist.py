"""
    直方图
    matplotlib.​pyplot.​hist(x, bins=int, range=None, normed=bool, weights=None, cumulative=bool, bottom=None, histtype=unicode, align=unicode, orientation=unicode, rwidth=None, log=bool, color=None, label=None, stacked=bool, hold=None, data=None, **kwargs)
"""
import matplotlib.pyplot as plt
import random as rdm
data = [] #数据列表
for i in range(100):
    data.append(rdm.randint(1,100))
print(data,"\n")

bins = [] #分组边界
for j in range(10):
    bins.append(j*10)
print(bins)
plt.hist(data,bins=bins)#data数据列表y，bins分组边界x
plt.show()
