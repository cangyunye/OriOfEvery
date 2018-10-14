import numpy as np
from keras.models import Sequential
from keras.layers import Dense #Layer属性
import matplotlib.pyplot as plt

#生成200个线性数据，在-1,1之间
X=np.linspace(-1,1,200)
#对X进行打乱
np.random.shuffle(X)
#设计训练用数据 normal使数据保持正态分布，换种说法是，标准差稳定，数据间不会相差太大
Y=0.5*X+2+np.random.normal(0,0.05,(200,))
#描点
plt.scatter(X,Y)
plt.show()

X_train,Y_train = X[:160],Y[:160]#前160个数据
X_test,Y_test = X[160:],Y[160:]#后40个数据
#构建序列化模型
model=Sequential()
#第一层神经网络，输入1维数据X，input_dim=1，输出到1维数据Y，output_dim=1
model.add(Dense(output_dim=1,input_dim=1))
#第二层input_dim即为第一层的output_dim,由于上一层output_dim已经是1了，所以不需要加第2层了
#model.add(Dense(output_dim=1))
#选择代价函数和优化方法，https://keras.io/
model.compile(loss='mse',optimizer='sgd')
print('Training-------------')
for step in range(301):
    #指定数据的批次训练
    cost = model.train_on_batch(X_train,Y_train)
    if step % 100 ==0:
        print('train cost:',cost)
print('Testing--------------')
#将测试数据的所有40个数据进行评估
cost = model.evaluate(X_test,Y_test,batch_size=40)
print('test cost:',cost)
#选择第一层数据，获取权重
W,b=model.layers[0].get_weights()
print('Weights=',W,'\nbiases=',b)
#开始预测
Y_pred = model.predict(X_test)
plt.scatter(X_test,Y_test)
plt.plot(X_test,Y_pred)
plt.show()
