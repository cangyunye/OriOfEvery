import os
os.environ['KERAS_BACKEND'] = 'tensorflow'
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
import numpy as np
"""
2 tuples:
x_train, x_test: uint8 array of grayscale image data with shape (num_samples, 28, 28).
y_train, y_test: uint8 array of digit labels (integers in range 0-9) with shape (num_samples,).
"""
# X构成(60000个采样数据，28*28的灰度图像),y构成(10个类)，数据集取自mnist的handwritten手写0-9
(X_train, y_train), (X_test, y_test) = mnist.load_data()
#将60000*28*28个元素，分成60000行，每行自动填充，即为28*28=784，由于色彩RGB分布为256色，最大为255，最小0，故除255
X_train = X_train.reshape(X_train.shape[0], -1)/255  # 正则化
X_test = X_test.reshape(X_test.shape[0], -1)/255  # 正则化
#将y的值，变成one-hot-data，即分类为10类，每类仅1个点位1，比如y有6w条数据，共10类，然后对每条数据分成10份，对于2来说，第2份为1，其他9份为0，用这个10份的真值表代表2
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)
# 构建神经网络
model = Sequential()
model.add(Dense(output_dim=32, input_dim=784, activation='relu'))
model.add(Dense(output_dim=10, activation='softmax'))
# lr为learning rate
rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
model.compile(optimizer=rmsprop, loss='categorical_crossentropy',
              metrics=['accuracy'])

print('Training----------------')
# 训练2次，每批32个数据
model.fit(X_train, y_train, nb_epoch=2, batch_size=32)
print('Testing-----------------')
loss, accuracy = model.evaluate(X_test, y_test)
print('test loss: ', loss)
print('test accuracy: ', accuracy)
