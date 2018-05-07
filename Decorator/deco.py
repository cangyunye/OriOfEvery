"""
Python中的装饰器(decorator)
想理解Python的decorator首先要知道在Python中函数也是一个对象，所以你可以

将函数复制给变量
将函数当做参数
返回一个函数
"""
#初级装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper  #调用log，返回的wrapper，而非wrapper()

#给装饰器传文本
def logz(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
#装饰器内参数判断
def logl(level):
    def decorator(func):
        def wrapper(*args, **kw):
            if level == 0:
                print('[INFO]:%s():' % (func.__name__))
            elif level == 1:
                print('[WARN]:%s():' % (func.__name__))
            elif level == 2:
                print('[DEBUG]:%s():' % (func.__name__))
            elif level == 3:
                print('[ERROR]:%s():' % (func.__name__))
            else:
                print('[FATAL]:%s():' % (func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log
def now(para):
    print('test now() = log(now)(),para=%s' % (para))

@logz('execute')
def nowz():
    print('test nowz = logz(text)(nowz)()')

@logl(1)#入参为int
def nowl():
    print('test nowl = logz(level)(nowl)()')

now('Para in Func')
nowz()
nowl()
