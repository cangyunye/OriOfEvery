import numpy as np
#导入多项式生成包
from sklearn.preprocessing import PolynomialFeatures
#创造3X2的矩阵
X = np.arange(6).reshape(3,2)
#多项式生成器特征，阶数为2，允许特征不仅互乘，可自乘，允许偏差常数
pl = PolynomialFeatures(degree=2,interaction_only=False,include_bias=True)
#根据矩阵生成多项式
pl.fit_transform(X)