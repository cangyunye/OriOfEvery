"""
    用dict定义菜单
    请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
    和list比较，dict有以下几个特点：
    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。
    而list相反：
    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。
    所以，dict是用空间来换取时间的一种方法。
    
"""
# dict_menu = dict()
#初始化dict_menu
dict_menu = {'eggs':1.00,'milk':3.50,'baozi':2.00,'dumpling':15.00}
dict_menu['gongbaojiding'] = 23.00
dict_menu['qingjiaochaojirou'] = 15.00
dict_menu_new = {'juanxincai':1.5,'dabaicai':2.00,'shengcai':3.15}
dict_menu.update(dict_menu_new)
print(type(dict_menu))
print('eggs=',dict_menu['eggs'],'\npotato=',dict_menu.get('potato', 3.2))#不存在的则给默认值
print('------------------dict_menu---------------------\n',dict_menu)
day_in_month = {1:30,
                2:28,
                3:31,
                4:30,
                5:31,
                6:30,
                7:31,
                8:31,
                9:30,
                10:31,
                11:30,
                12:31}
print('------------------day_in_month---------------------\n',day_in_month)
day_in_month_setdict = {30:{4,6,9,11},31:{1,3,5,7,8,10,12}}
print('------------------day_in_month_setdict[30]---------------------')
print(day_in_month_setdict[30])
print('------------------After Print---------------------')
for i2 in day_in_month_setdict[30]:
    print (i2)
print('-------------------day_in_month_setdict--------------------')
for i4 in day_in_month_setdict:#输出字典的所有键
    print (i4)
print('------------------day_in_month_setdict.keys()---------------------')
for i1 in day_in_month_setdict.keys():#打印字典的键day_in_month_setdict
    print (i1)
print('-------------------day_in_month_setdict.values()--------------------')
for i3 in day_in_month_setdict.values():#分行输出字典的所有值
    print (i3)
print('-------------------day_in_month_setdict.items()--------------------')
for i5,i6 in day_in_month_setdict.items():#遍历字典所有数据项
    print (i5,i6)
print('-------------------day_in_month_setdict.items()--------------------')
for i5 in day_in_month_setdict.items():#遍历字典所有数据项
    print (i5)
dict_menu.update()
print(dict_menu.get('eggs'))#取得字典值
dict_menu.pop('eggs')#删除字典值
dict_menu.setdefault('eggs',9.99)#如果eggs不存在，则返回9.99,类似于get()
print(dict_menu.get('eggs'))  # 取得字典值
