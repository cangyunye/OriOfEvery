import matplotlib.pyplot as plt
import numpy as np
"""axis说明：axis=None 表示对所有元素求和。
axis=0 表示在第1个维度上求和。
axis=1 表示在第2个维度上求和。
以此类推…"""

def first():
    total_times = 10000
    # 记录骰子的结果
    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_arr + roll2_arr
    print("Rdom1:{}\nRdom2:{}\nrandom plus:{}".format(roll1_arr,roll2_arr,result_arr))

def second():
    #设置数组
    array = np.array([[1,2,3],[2,3,4]])
    print(array)
    print('number of dim:',len(array))  #维度
    print('shape:',array.shape) #行列数
    print('size:',array.size)  #元素个数

def third():
    a = np.array([2,23,4],dtype=np.int)
    print("dtype:",a.dtype)
    b = np.array([2,23,4],dtype=np.float) #float默认64位，可以调整位float16/32
    print("dtype:",b.dtype)
    c = np.zeros((3,4))#定义3行4列位0矩阵
    print("Zeros:",c)
    d = np.arange(10,20,2) #(起始10，终止20，步长2)
    print("arange:",d)
    f = np.arange(12).reshape((3,4))#重新定义3行4列从0到11的数列
    print("arange.reshape:\n",f)
    e = np.linspace(1,39,20).reshape(4,5)#将1到39中间38等分（去掉20-首尾2段），重定义到4行5列20个元素
    print("linspace.reshape:\n",e)

def forth():
    a = np.array([10,20,30,40])
    b = np.arange(4)
    print(a,b)
    c1=a+b
    c2=a-b
    c3=b**2
    print("c1:{}\nc2:{}\nc3:{}".format(c1,c2,c3))
    print(b==3) #逐个比较，判断等于3的位真
def fifth():
    a = np.array([[1,1],[0,1]])
    b = np.arange(4).reshape((2,2))
    c = a*b
    c_dot = np.dot(a,b) #矩阵运算
    c_dot_2 = a.dot(b) #矩阵运算
    print("a\n{}\nb\n{}".format(a,b))
    print("C\n",c)
    print("C_dot\n",c_dot)
    print("C_dot_2\n",c_dot_2)
def sixth():
    a = np.random.random((2,4))
    print(a)
    print("np.sum(a,axis=1)",np.sum(a,axis=1)) #按行求和
    print("np.min(a,axis=0)",np.min(a,axis=0)) #按列取最小值
    print("np.max(a)",np.max(a)) #求矩阵最大值

def seventh():
    A = np.arange(2,14).reshape((3,4))
    print(A)
    print(np.argmin(A))#最小索引
    print(np.argmax(A))#最大索引
    print(np.mean(A))#平均值
    print(A.mean())#平均值
    print(np.mean(A,axis=1))#对行进行求平均
    print(np.mean(A,axis=0))#对列进行求平均
    print(np.average(A))#平均值
    print(np.median(A))#中位数
    print(np.cumsum(A))#累加，每两个数相加，类似Fibonacci
    print(np.diff(A))#累差，两数相减
    print(np.nonzero(A))#列出非零行的第几行第几列

def eighth():
    A = np.arange(14,2,-1).reshape((3,4))
    print(np.sort(A))#逐行进行排序
    print(np.transpose(A))#矩阵转置，行变列
    print(A.T)#矩阵的转置，行变列
    print((A.T).dot(A))
    print(np.clip(A,5,9))#将所有小与5的转为5，大于9的转为9，类似滤波器


def main():
    # first()
    # second()
    # third()
    # forth()
    # fifth()
    # sixth()
    # seventh()
    eighth()
if __name__ == '__main__':
    main()
