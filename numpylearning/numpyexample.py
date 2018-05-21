import matplotlib.pyplot as plt
import numpy as np


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
def main():
    first()
    second()
    third()
if __name__ == '__main__':
    main()
