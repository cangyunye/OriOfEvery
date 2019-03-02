
'''
Created on 2011-3-23
www.iplaypy.com

'''
from time import time

def logged (when):
    def log(f,*args,**kargs):
        print('''called: 
        function: %s 
        args :%r 
        kargs:%r''' %(f,args,kargs))
        
    def pre_logged(f):
        def wrapper(*args,**kargs):
            log(f,*args,**kargs)
            print('in pre_logged')
            return f(*args,**kargs)
        return wrapper
    
    def post_logged(f):
        def wrapper(*args,**kargs):
            print('in post_logged *')
            now =time()
            try:
                return f(*args,**kargs)
            finally:
                log(f,*args,**kargs)
                print('time delta: %s' % (time()-now))
                print('in post_logged')
        return wrapper
    
    try:
        return {"pre":pre_logged,"post":post_logged}[when]
    except KeyError as e:
        raise ValueError(e)('must be "pre" or "post" ')
    
@logged('pre')    
@logged('post')
def hello(name):
    print('hello, ',name)


hello('world!')
