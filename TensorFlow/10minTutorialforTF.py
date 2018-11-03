import tensorflow as tf
#h5py\__init__.py:36: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`
#解决方案：pip install --upgrade h5py

# graph（流图)是tensorflow的核心，每个计算，操作，变量都在流图中有定位。在代码中所有的事件都定位在TF给的默认graph中
graph = tf.get_default_graph()
#获取当前所有操作，返回为列表，由于现在尚无任何操作，所有返回为空[]
graph.get_operations()
#打印graph中的operations名称
for op in graph.get_operations():
    print(op.name)
#TensorFlow 会话
"""
Graph流图是用来定义操作的，操作只在session会话中运行，会话和流图是互相独立的，你可以想象为流图即蓝图，会话为工作站。
Graph仅定义计算方式或者构建蓝图，而不会有任何变量和值，除非是在会话里面运行。
"""
#创建会话
sess=tf.Session()
#Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
#出现以上问题是由于TF默认是给GPU用，且是在没有CPU的环境，这里对于一般设备可以直接用如下方法忽略
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#无论何时，都要记得关闭，可以使用with语句表示
sess.close()

with tf.Session() as sess:
    sess.run(f)

#TenSorFlow中的张量
#>TF中的张量数据和numPy的多维数组相似
#a)常量
a=tf.constant(1.0)
print(a)

