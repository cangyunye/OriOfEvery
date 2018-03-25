"""
    功能：掷骰子
    设计方案：
    1：模拟骰子的6个面
    2：模拟1个骰子所有结果
    3：模拟2个骰子所有结果
    4：模拟1个骰子的结果成像直方图
    5：模拟2个骰子的结果成像直方图
    6: 模拟n个骰子，每个面不同值，投掷模拟直方图
"""
import random as rdm
import matplotlib.pyplot as plt
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
class Dice:
    """掷骰子"""
    def __init__(self, rolltimes,dice_num):
        self.rolltimes = rolltimes #投掷次数
        self.dice_num = dice_num #骰子数目
    def dice_urself(self):
        #定义多面体
        self.dice_face = input('输入多面体>：')
        #数组化，split分出的为字符串数组
        self.dice_face = self.dice_face.split(' ')
        #设定面数
        self.face_num = len(self.dice_face)
        #字符串转数字
        for i in range(self.face_num):
            self.dice_face[i] = eval(self.dice_face[i])
    def dice_value(self):
        #输出面值
        print("输入为{}面体,投掷{}次".format(self.face_num,self.rolltimes))
        print("面值为：\n",self.dice_face)
        # print("输出对应关系：")
        # for i in range(self.face_num):
        #     print("第{}面，面值{}".format(i+1,self.dice_face[i]))
    def hexahedron(self):
        """定义六面体-骰子"""
        self.dice_face = [1,2,3,4,5,6]
        self.face_num = len(self.dice_face)
    def diceplus(self):
        """随机投掷结果"""
        self.dice_result = 0 #重置投掷点数
        #计算投掷点数之和
        for j in range(self.dice_num):
            # print(self.dice_face[rdm.randint(0,self.face_num-1)])
            self.dice_result += self.dice_face[rdm.randint(0,self.face_num-1)]
        return self.dice_result
    def result_list(self):
        """结果记录"""
        self.dice_result_list = []
        #累计投掷点数
        for k in range(self.rolltimes):
            self.dice_result_list.append(self.diceplus())#此处已做调用diceplus
        print ("投掷结果：\n",self.dice_result_list)
    def hist_make(self):
        #绘制直方图
        plt.hist(self.dice_result_list, bins=range(min(self.dice_result_list), max(self.dice_result_list)), normed=1, edgecolor='black', linewidth=1)
        plt.title('骰子点数统计')
        plt.xlabel('点数')
        plt.ylabel('频率')
        plt.show()
    def process(self):
        # print("内建函数dir:\n",dir(self))
        # print("内建函数__dict__\n",self.__dict__)
        confirm=eval(input("使用默认六边形输入1，定制多面体输入2？"))
        if confirm == 1:
            self.hexahedron()
        elif confirm == 2:
            self.dice_urself()#自定义多面体及面值
        else:
            print("输出错误，请重新输入。")
            self.process()
        self.dice_value()
        self.result_list()
        print("MAX={},min={}".format(max(self.dice_result_list),min(self.dice_result_list)))
        self.hist_make()
        print("test4end!")
def main():
    dc = Dice(100,2)
    # dc.dice_urself()
    # dc.dice_value()
    dc.process()

if __name__ == '__main__':
    main()
