import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2  = x**2
plt.figure(num=1)

#设置取值范围
plt.xlim((-1,2))
plt.ylim((-2,3))
#轴标签名
plt.xlabel('Label X')
plt.ylabel('Label Y')

#设置图例标签
plt.plot(x,y2,label='up')
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')
#绘制图例
plt.legend()

plt.show()

