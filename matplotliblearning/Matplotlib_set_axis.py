import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2  = x**2
plt.figure(num=1)
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
#设置取值范围
plt.xlim((-1,2))
plt.ylim((-2,3))
#轴标签名
plt.xlabel('Label X')
plt.ylabel('Label Y')
#轴坐标名
new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3,],['really bad','bad','normal','good','really good'])
#改变字体
# plt.yticks([-2,-1.8,-1,1.22,3,],[r'$really\ bad$','$bad$','$normal$','$good$','$really\ good$'])

#gca = 'get current axis'获取当前轴
ax = plt.gca()
#轴的脊梁，相对初始状态的4个边，以下将右边和上边置空
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#将底边作为X轴,左边作为Y轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#将底边的(-1,1)作为坐标原点，即底边从(-1[normal])穿过，左边从1穿过，定位方式data，即按值定位
ax.spines['bottom'].set_position(('data',-1))
ax.spines['left'].set_position(('data',1))
plt.show()

