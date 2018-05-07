"""位置参数 ,对于power(x)函数，参数x就是一个位置参数。"""
def power(x):
    return x * x
"""修改后的power(x, n)函数有两个参数：x和n，这两个参数都是位置参数"""
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
"""
>>> power(5)
25
>>> power(5, 2)
25
"""
"""默认参数,必选参数在前，默认参数在后
多个默认参数时，调用的时候，既可以按顺序提供默认参数
当不按顺序提供部分默认参数时，需要把参数名写上
默认参数实际是变量，必须指向不变对象！否则因内部变化会导致默认参数变化"""
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
"""
>>> enroll('Sarah', 'F')
name: Sarah
gender: F
age: 6
city: Beijing
"""
"""可变参数，可变参数就是传入的参数个数是可变的
可以是1个、2个到任意个，还可以是0个。
在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple
把list或tuple的元素变成可变参数传进去"""
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
"""
>>> nums = [1, 2, 3]
>>> calc(*nums)
"""
"""关键字参数,关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict"""
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
"""
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
"""
"""
**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
"""
"""命名关键字参数,对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
至于到底传入了哪些，就需要在函数内部通过kw检查。"""
def person(name, age, **kw):
    #检查是否有city和job参数：
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

def person(name, age, *, city, job):
    #限制关键字参数的名字，“*”后面的参数被视为命名关键字参数
    print(name, age, city, job)
"""
>>> person('Jack', 24, city='Beijing', job='Engineer')
Jack 24 Beijing Engineer
"""
"""
如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
"""
def person(name, age, *args, city='Beijing', job):
    print(name, age, args, city, job)
"""
参数组合
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
"""
