#科学计算工具包
from numpy import *
#运算符模块
import operator 

def createDataSet():
    #用于创建数据集合标签
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inX,dataSet,labels,k):
    #第n维，即表示列表符号"[]"第几层，从1层开始，第1维表示[a,b,c]的a,b,c等3个项
    #统计第1维项数量，即数据的行数
    dataSetSize = dataSet.shape[0]
    #将输入坐标通过tile，扩大为样本数据的行数，然后每行减去对应行的样本
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    #求矩阵各项平方
    sqDiffMat = diffMat**2
    #对第2维项求和,即对所有列求和
    sqDistances = sqDiffMat.sum(axis=1)
    #取根号
    distances = sqDistances**0.5
    #按照距离递增排序,返回索引号
    sortedDistIndicies = distances.argsort()
    classCount = {}
    #选择距离最小的k个点
    for i in range(k):
        #排序的前k个点对应的类
        voteIlabel = labels[sortedDistIndicies[i]]
        #字典对每个类的统计
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
    