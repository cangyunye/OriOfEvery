"""
    **kw参数为关键字参数，可任意决定是否输入，即代表0个或0+个参数。
    在调用函数，输入参数的时候，需要注意，调用方式为写入dict类型值进行调用。
    和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
    *args参数为可变参数，可传入0及0+参数
    调用时，类似指针
    不是必须写成kw

"""
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print('calc->',sum)
def calcu(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print('calc->',sum)
def person(name,age,**kw):
    print('name:{}\nage:{}\nother:{}'.format(name,age,kw))
def personz(name, age, *, city, job):
    print(name, age, city, job)
def main():
    name='Scarlet'
    age=15
    #限制关键字参数名字
    personz(name, age,city='xiangtan',job='Tester')
    #关键字参数
    person(name, age,attr='Nothing Special!',Dream='xu')
    #或者如下方式
    extrakw={'attr':'Nothing Special!','Dream':'yu','date':'Every Day!'}
    person(name, age,**extrakw)
    #可变参数
    li=[1,2,3]
    #调用calc时，我们可以输入list作为参数
    calc(li)
    #调用calcu时，我们可以输入*list作为参数
    calcu(*li)
if __name__ == '__main__':
    main()
