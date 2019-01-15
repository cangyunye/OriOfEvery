import numpy as np
from operator import itemgetter

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
	#角色,CPP,JAVA,SHELL,PYTHON,SQL,可分配量。
	role_info=[['hwx',30,60,70,80,50,50],['cwx',0,0,40,50,40,100],['dwx',50,30,80,70,60,30],['nwx',0,100,80,0,30,70]]
	#任务,CPP,JAVA,SHELL,PYTHON,SQL,预分配量,执行人数
	task_info=[['testframe',0,10,20,70,30,100,5],['database',30,30,20,20,80,20,2],['excel',0,0,0,60,60,20,2],['scriptcomp',0,0,50,60,10,10,1]]
	return role_info,task_info

def skillBasedRecommend(roles,task):
	"""根据任务需求技能比重系数C与人物能力比重系数S的矢量相乘,即得内积，任务适应值D。
	:param roles:所有角色
   	eg [['hwx',30,60,70,80,50,50],['cwx',0,0,40,50,40,100],['dwx',50,30,80,70,60,30],['nwx',0,100,80,0,30,70]]
	:param task:一个任务，并含有所有技能需求系数和执行人数
	eg ['testframe',30,60,70,80,50,50,5]
	:return:对每个任务按技能最适应排序
	"""
	#初始化技能推荐字典
	skillRecommend={}
	#任务能力需求系数 
	C=np.array(task[1:-3]) #[0,10,20,70,30]
	#任务能力涉及度
	N=len(C)
	for role in roles:
		#个人能力系数
		S=np.array(role[1:-2]) #[30,60,70,80,50]
		#任务适应度
		D=S*C
		#求方差
		sq=np.sqrt((D-C)**2/N*np.tile(1,(C.shape[0],C.shape[1])))
		s_sum=np.sum(sq,axis=0)
		#添加角色对应适应匹配值到字典
		skillRecommend[role[0]]=s_sum
	#对每个任务按技能最适应排序,sorted返回为list
	return sorted(skillRecommend.items(),key=lambda item:item[1],reverse=True)

def allTaskFit(tasks):
	pass
def allotTasks():
	for task in tasksort:
		Executor=''
		task[]

if __name__ == "__main__":
	roles,tasks=datas_test()
	skillBasedRecommend(roles,task)
