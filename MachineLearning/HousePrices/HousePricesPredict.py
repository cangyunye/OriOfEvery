#-*- coding:utf-8 -*-
# from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from scipy.stats import skew
# import matplotlib.pyplot as plt
import pandas as pd


#导入数据
def get_csv(file_name):
    data=pd.read_csv(file_name)
    #查看文件顶部数据
    print(data.head())
    #查看1到3行，'MSSubClass'列到'SaleCondition'
    print(data.loc[1:3,'MSSubClass':'SaleCondition'])
    return data

#数据
# def TwoDimension_figure(axis_lists):
#     plt.figure()
#     #读取数据中的每列，然后循环每段，输出段与prices的图
#     for index in axis_lists:
#         plt.plot(axis_lists[0])

# def main():
file_train='train.csv'
file_test='test.csv'

#读取训练数据和测试数据
train = get_csv(file_train)
test = get_csv(file_test)
#配置训练值
X_train = train.loc[:,'MSSubClass':'SaleCondition']
y_train = train.loc[:,'SalePrice']
#将所有非典型数据变量(字符串型)转换为虚拟数值型枚举值
X_train = pd.get_dummies(X_train)
#用列均值填充空值(NaN)
X_train = X_train.fillna(X_train.mean())
# X_train = X_train[X_train.shape[0]]
#配置测试值
X_test = test.loc[:,'MSSubClass':'SaleCondition']
# y_test = test.loc[:,'SalePrice']
#将所有非典型数据变量(字符串型)转换为虚拟数值型枚举值
X_test = pd.get_dummies(X_test)
#用列均值填充空值(NaN)
X_test = X_test.fillna(X_test.mean())
# X_test = X_test[X_test.shape[0]]
# y_test = pd.get_dummies(y_test)
#构建线性回归模型
LR = LinearRegression()

#查询在X_train中不在X_test中字段
from collections import Iterable
isinstance(X_train.columns,Iterable)
set_Xtrain=set(X_train.columns)
set_Xtest=set(X_test.columns)
#差集
retD = list(set_Xtrain.difference(set_Xtest))
#并集
retU = list(set_Xtrain.union(set_Xtest))
#排除X_train中差集部分
for delcol in retD:
    X_train.pop(delcol)
#构建拟合函数
LR.fit(X_train,y_train)
#测试数据预期
LR.predict(X_test)

"""
all_data = pd.concat((train.loc[:,'MSSubClass':'SaleCondition'],
                      test.loc[:,'MSSubClass':'SaleCondition']))
#取得所有非float，int，datetime，string等pandas数据类型的index
numeric_feats = all_data.dtypes[all_data.dtypes != "object"].index
#利用skew根据离散程度重新分布非pandas数据类型特征字段值，并删除缺失值（NaN)
skewed_feats = train[numeric_feats].apply(lambda x: skew(x.dropna())) #compute skewness
#将离散程度大于0.75的保留
skewed_feats = skewed_feats[skewed_feats > 0.75]
#重新获取离散程度大于0.75的字段
skewed_feats = skewed_feats.index
#取合并数据中
all_data[skewed_feats] = np.log1p(all_data[skewed_feats])
all_data = pd.get_dummies(all_data)
all_data = all_data.fillna(all_data.mean())
X_train = all_data[:train.shape[0]]
X_test = all_data[train.shape[0]:]
y = train.SalePrice
# if __name__ == '__main__':
#     main()"""