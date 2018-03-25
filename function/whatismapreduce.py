"""
    map(func, *iterables) 映射
    reduce(func, [x1, x2, x3, x4]) = func(func(func(x1, x2), x3), x4) 归约

"""
from functools import reduce
def add(x, y):
    return x + y
def f(x):
    return x*x

def str2int(s):
    # def fn(x, y):
    #     return x * 10 + y
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]
    # return reduce(fn, map(char2num, s))
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
def main():
    r = reduce(add, [1, 3, 5, 7, 9])
    print(r)
    m = map(f,list(range(1,10)))
    #map属性的值，通过list打印出来
    print(list(m))
    #将map用在reduce内
    print(str2int('13579'))
if __name__ == '__main__':
    main()
