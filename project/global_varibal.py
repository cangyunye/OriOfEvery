glo1 = 1 #全局变量，未在函数中使用global声明，仅可输出，不可改变
glo2 = 2  #全局变量，在函数中使用global声明后，可进行同步关联
def g1():
    print(glo1)
    glo1 += 1  #如果不加入则报错
    print(glo1)

def g2():
    global glo2
    print(glo2)
    glo2 += 2
    print(glo2)
g1()
print('--------------')
g2()
