"""
    集合set类型，是无序，没有索引的，不可重复的
"""
set1 = {1,2,3,4,5}
set2 = {1,3,5,7,9}
print(type(set1))
print('set1={}\nsest2={}\n'.format(set1,set2))
print('"-"set1-set2补集',set1-set2)#同set1.difference(set2)，返回在set1中，不在set2中元素
print('"&"set1&set2交集',set1&set2)#同set1.intersectiono(set2),返回在set1和set2中的元素
print('"|"set1|set2并集',set1|set2)#同set1.union(set2)，返回所有set1与set2的元素
print('"^"set1^set2交集对并集的补集',set1^set2)#同set1.symmetric_difference(set2),返回不同时在set1和set2中的元素

def is_leap_year(year):
    #判断闰年
    if ((year % 400 ==0) or ((year % 4 == 0) and (year % 100 !=0) ) and month > 2):
        return True
    else:
        return False
#30天月份集合
_30_days_month_set = {4,6,9,11}
#31天月份集合
_31_days_month_set = {1,3,5,7,8,10,12}
#初始天数，当前日期天数
days = 31
#判断到12月31日为止，今年有多少天
for month in range(1,12):
    if month in _30_days_month_set:
        days += 30
    elif month in _31_days_month_set:
        days += 31
    elif is_leap_year(2017) and month >= 2 :
        days += 29
    else:
        days += 28
print("days=",days)
