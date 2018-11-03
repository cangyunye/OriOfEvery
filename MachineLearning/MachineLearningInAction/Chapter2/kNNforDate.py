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
    

def file2matrix(filename):
    fr = open(filename)
    love_dictionary = {'largeDoses':3, 'smallDoses':2, 'didntLike':1}
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip() #清除行前后的空格以及换行符
        listFromLine = line.split('\t') #根据\t分组
        returnMat[index,:] = listFromLine[0:3]# 将前三行赋值
        if listFromLine[-1].isdigit():#矩阵最后一列是否数字
            classLabelVector.append((int(listFromLine[-1])))
        else:
            classLabelVector.append(love_dictionary.get(listFromLine[-1]))
        index += 1
    fr.close()
    return returnMat,classLabelVector


def plot_sca():
    import matplotlib
    import matplotlib.pyplot as plt
    fig = plt.figure() #指定画布
    ax = fig.add_subplot(111) #在指定画布中分割为1行1列，选择第1块
    ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
    plt.show()  

def autoNorm(dataSet):
  minVals = dataSet.min(0) #axis=0;求每列的最小值
  maxVals = dataSet.max(0) #axis=0,求每列的最大值
  ranges = maxVals - minVals 
  normDataSet = zeros(shape(dataSet)) #以dataSet行列设置0值矩阵
  m = dataSet.shape[0] #axis=0，每列的长度
  normDataSet = dataSet - tile(minVals,(m,1)) #矩阵相减在同一size
  normDataSet = normDataSet/tile(ranges,(m,1)) #矩阵相除在同一size
  return normDataSet,ranges,minVals

def datingClassTest():
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix('datingTestSet.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]  #总样本量
    numTestVecs = int(m*hoRatio) #测试数据集抽取hoRatio的量
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],4) #m-numTestVecs个样本
        print("the classifier came back with:%d, the real answer is: %d" % (classifierResult ,datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
            print("the total error rate is:%f" % (errorCount/float(numTestVecs)))

def classifyPerson():
    resultList = ['not at all','in small doses', 'in large doses']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat,ranges,minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,iceCream])
    classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print("You will probably like this person:",resultList[classifierResult-1])

    