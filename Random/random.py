"""
    相关：random
    random()：生成一个[0，1.0)之间的随机浮点数
    uniform(a,b)：生成一个a到b之间的随机浮点数
    randint(a,b)：生成一个a到b之间的随机整数
    choice(<list>)：从列表中随机返回一个元素
    shuffle(<list>)：从列表中元素随机打乱
    sample(<list>,k)：从制定列表中随机获取k个元素
    enumerate()：函数用于将可遍历的组合转换为一个索引序列和元素值
    zip()：将两个列表打包成一个元组zip(key_list,value_list)
"""
import random as rdm
list1=[1,3,5,7,9,11,13]
list2=[1,2,3,4,5,6]
for i,x in enumerate(list1):
    print("index={},value={}".format(i,x))
turple_list=zip(list1,list2) #超量的部分或少量的部分不会被zip匹配
print ("when dict(zip(list1,list2))\n",dict(turple_list)) #将zip类型转换为dict
rdm.shuffle(list1)
print("What's randint(10,100):",rdm.randint(10,100))
print("After shuffle:",list1)
print("After choice:",rdm.choice(list2))
print("After sample3:",rdm.sample(list2,3))
