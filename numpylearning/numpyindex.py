import numpy as np

def first():
    A = np.arange(3,15)
    print(A)
    print(A[3]) #索引第3个值

def second():
    A = np.arange(3,15).reshape(3,4)
    print(A)
    print(A[2]) #第3行所有数
    print(A[2,:])#第3行所有数
    print(A[2][1])#第3行，第2列
    print(A[2,1])#第3行，第2列
    print(A[:,1])#第2列所有数
    print(A[1,1:4])#第2行，第2列到第4列之列的数，右边为开区间
    print(A.flat) #返回所有A里的元素，作为迭代器
    for item in A.flat:
        print(item)
    print(A.flatten()) #返回所有A里的元素



def main():
    # first()
    second()
    # third()
    # forth()
    # fifth()
    # sixth()
    # seventh()
    # eighth()
if __name__ == '__main__':
    main()
