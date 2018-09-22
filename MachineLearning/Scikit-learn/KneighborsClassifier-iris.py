#Iris鸢尾花数据
import numpy as np
#datasets集合是官方预设用于练习的数据包
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
iris = datasets.load_iris()
#iris属性
iris_X = iris.data
print(iris_X[:2,:])
#iris分类
iris_y = iris.target
print(iris_y)
#测试比例占用0.3，即x_test和y_test为30%的总数据,x_train,y_train占70%数据
#那这是为什么要分开嘞，因为这个分开就是就是拿一组数据集合里分给你什么是测试的部分什么是当做（训练）实际的部分
#然后用实际的部分训练完成后的预期函数再读取测试部分，预估要一致
X_train,X_test,y_train,y_test = train_test_split(iris_X,iris_y,test_size=0.3)
print(y_train)
#定义选择的模块为最近邻http://sklearn.apachecn.org/cn/0.19.0/modules/neighbors.html
knn = KNeighborsClassifier()
#放入拟合用训练数据
knn.fit(X_train,y_train)
#用测试数据去预测
print(knn.predict(X_test))
print(y_test)
#对预测准确度打分
print(knn.score(X_test,y_test))