"""
    Python内建的filter()函数用于过滤序列。
    和map()类似，filter()也接收一个函数和一个序列。
    和map()不同的是，filter()把传入的函数依次作用于每个元素，
    筛选法，则根据序列返回值是True还是False决定保留还是丢弃该元素。
"""
def is_odd(n):
    #求素数，return返回True或False
    return n % 2 == 1
"""
    用filter求素数
    计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
    首先，列出从2开始的所有自然数，构造一个序列：
    2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
    取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
    下一次算法同理。
"""
def _odd_iter():
    #先生成序列
    n = 1
    while True:
        n = n + 2
        #yield代替return返回的n，即，在每次调用函数，会生成下一次n
        yield n
def _not_divisible(n):
    #定义筛选函数，筛选不能被整除的，然后返回True或False
    return lambda x : x % n > 0 #为什么这里能直接用lambda而且不用参数呢，解释在filter调用

def primes():
    yield 2#先将2作为第一个数返回
    it = _odd_iter() # 从2以后逐步初始序列
    while True:
        n = next(it) # 返回序列的第一个数,即素数
        yield n
        #每次返回第一个数后，下一次调用
        it = filter(_not_divisible(n), it) # it的值作为lambda的x的参数
def primes_print():
    # 打印1000以内的素数:
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

def main():
    l=[1,2,3,4]
    # print(list(map(is_odd,l)))
    # print(list(filter(is_odd, l)))
    # primes_print()
    it = _odd_iter() # 初始序列
    n=1
    while n<100:
        n = next(it)
        print(n)
    # print(_not_divisible(3))
if __name__ == '__main__':
    main()
