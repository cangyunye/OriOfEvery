from sklearn import preprocessing
import numpy as numpy
from sklearn.model_selection import train_test_split
#生成分类数据
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# a = np.array([[10,2.7,3.6],
# [-100,5,-2],
# [120,20,40]],dtype=np.float64)
# print(a)
# print(preprocessing.scale(a))
#构造分类数据，300个样本，2个特征，2个相关属性(informative)，随机产生22个状态（random_state)，
X,y = make_classification(n_samples=300,n_features=2,n_redundant=0,n_informative=2,random_state=22,n_clusters_per_class=1,scale=100 )
#绘制散点图
plt.scatter(X[:,0],X[:,1],c=y)
plt.show()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
#采用C-Support Vector Classification模型
clf = SVC()
#拟合训练
clf.fit(X_train,y_train)
#用test数据预估
clf.predict(X_test)
print(y_test)
print(clf.score(X_test,y_test))

#区间缩放，比例尺缩小
X = preprocessing.scale(X)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
#采用C-Support Vector Classification模型
clf = SVC()
#拟合训练
clf.fit(X_train,y_train)
#用test数据预估
clf.predict(X_test)
print(y_test)
print(clf.score(X_test,y_test))
