import numpy as np
from operator import itemgetter
#from collections import Counter

# import matplotlib


def datafromDB():
    pass


def datafromExcel():
    pass


def datafromtxt():
    pass


def datas_test():
    """
    设置数据
    第一列为名称，最后一列为时间，中间为技能
    人物技能：
    任务属性：
    """
    # 角色,CPP,JAVA,SHELL,PYTHON,SQL,可分配量。
    role_info = [['hwx', 30, 60, 70, 80, 50, 50], ['cwx', 0, 0, 40, 50, 40, 100], [
        'dwx', 50, 30, 80, 70, 60, 30], ['nwx', 0, 100, 80, 0, 30, 70]]
    # 任务,CPP,JAVA,SHELL,PYTHON,SQL,预分配量,执行人数
    task_info = [['testframe', 0, 10, 20, 70, 30, 100, 5], ['database', 30, 30, 20, 20, 80, 20, 2], [
        'excel', 0, 0, 0, 60, 60, 20, 2], ['scriptcomp', 0, 0, 50, 60, 10, 10, 1]]
    return role_info, task_info


def skillBasedRecommend(roles, task):
    """根据任务需求技能比重系数C与人物能力比重系数S的矢量相乘,即得内积，任务适应值D。
    :param roles:所有角色
    eg [['hwx',30,60,70,80,50,50],['cwx',0,0,40,50,40,100],['dwx',50,30,80,70,60,30],['nwx',0,100,80,0,30,70]]
    :param task:一个任务，并含有所有技能需求系数和执行人数
    eg ['testframe', 0, 10, 20, 70, 30, 100, 5]
    :return :对每个任务按技能最适应排序
    """
    # 初始化技能推荐字典
    skillRecommend = {}
    # 任务能力需求系数
    C = np.array(task[1:-2])  # [0,10,20,70,30]
    # 任务能力涉及度
    N = len(C)
    for role in roles:
        # 个人能力系数
        S = np.array(role[1:-1])  # [30,60,70,80,50]
        # 任务适应度
        D = S*C
        # 求方差
        delta = (D - C) ** 2
        distance = np.max(delta) - np.min(delta)
        divide = N * np.tile(1 * distance, C.shape)
        sq = np.sqrt((D - C) ** 2 / divide)
        s_sum = np.sum(sq, axis=0)
        # 添加角色对应适应匹配值到字典
        skillRecommend[role[0]] = s_sum
    # 对每个任务按技能最适应排序,sorted返回为list
    return sorted(skillRecommend.items(), key=lambda item: item[1], reverse=True)


def allTaskFit(roles, tasks):
    """遍历所有任务获取角色能力推荐
    :param roles:
    :param tasks:
    :return :返回为字典，key为任务,value为list型角色适应度排序
    """
    allTask = {}
    for task in tasks:
        allTask[task[0]] = skillBasedRecommend(roles, task)
    return allTask


def allotTasks(roles, tasks):
    """
    :param Tasks:所有任务及对应任务适应角色匹配度排序
    """
    # 获取所有任务角色能力分配(字典)
    # {'testframe':[['hwx',200],['cwx',100]]}
    allFit = allTaskFit(roles, tasks)
    # 所有人员
    workers = set(r[0] for r in roles)  # {'cwx', 'dwx', 'hwx', 'nwx'}
    # 人员工量
    assignment = {k[0]: k[-1] for k in roles} # {'hwx': 70.0, 'cwx': 130.0, 'dwx': 46.0, 'nwx': 94.0}
    # 任务分配结果
    allot = []
    # 任务已分配人员
    Executors = []
    for task in tasks:
        # 任务执行者数量
        ExecutorNum = task[-1]
        # 当前人选
        fit = 0
        # 已分配人数
        i = 1
        # 任务均分量
        taskavg = task[-2]/ExecutorNum
        while i <= ExecutorNum:
            # 任务匹配人选
            BestFit = allFit[task[0]][fit]  # ('hwx',200)
            print(f"{BestFit[0]}已分配{Executors.count(BestFit[0])}剩余分配量{assignment[BestFit[0]]}任务要求均值{task[-2]}")
            if Executors.count(BestFit[0]) == 0 and assignment[BestFit[0]] >= taskavg:
                # 人物可分配量重新赋值
                assignment[BestFit[0]] -= taskavg
                # 添加(任务，人选)
                allot.append([task[0], list(BestFit)]) # ['testframe',['hwx',200]]
                Executors.append(BestFit[0])
                print(f"{task[0]}分配{BestFit},已分配第{i}个")
                i += 1
            elif workers.difference(Executors):
                # 如果有剩余待命人，选择下个人员
                fit += 1
                # 保留一个bug，fit > ExecutorNum
                continue
            else:
                # 每次轮回，先分配有余闲的待命人员
                # 如果没有余闲的人，则重置待命人员列表
                Executors = []
                # 所有人员可分配量按定义配量补充
                assignment = {k[0]: k[-1] * 0.2 + 10 + v for k, v in zip(roles, assignment.values())}
                continue


    print(allot) #[['testframe', ('hwx', 22183627.91253946)]]
    return allot

def allotRoles():
    """按角色优先分配
    """
    pass

def writeToCsv(content):
    from datetime import datetime
    title = 'task,role,adaption'
    with open('Assiginment_{}.csv'.format(datetime.now().day)) as f:
        f.write(title)
        f.writeliness(content)



def plot():
    pass


if __name__ == "__main__":
    # 获取数据
    roles, tasks = datas_test()
    # 任务适应分析
    #allTask = allTaskFit(roles, tasks)
    # 任务分配
    allotTasks(roles, tasks)
