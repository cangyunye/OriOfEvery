"""
功能：汇率换算
版本：函数定义与调用
日期：2017年12月9日
"""
def convert_currency(money=100,rate=6.77):#带默认值的情况下，不要求输入参数
    turnvalue = money * rate
    return turnvalue
def main():
    invalue = input('输入带单位金额(100USD):')
    unit = invalue[-3:]
    inmon = eval(invalue[:-3])
    print(inmon,':',unit)
    if unit == 'CNY':
        exchange_rate = 1/6.77
    elif unit == 'USD':
        exchange_rate = 6.77
    else:
        exchange_rate = -1
    pt=convert_currency(inmon,exchange_rate)
    print(unit,'>>',pt)
if __name__ == '__main__':
    main()
print(__name__,'is the name')
"""
一个python的文件有两种使用的方法，
第一是直接作为脚本执行，
第二是import到其他的python脚本中被调用（模块重用）执行。
因此if __name__ == 'main': 的作用就是控制这两种情况执行代码的过程，
在if __name__ == 'main': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，
而import到其他脚本中是不会被执行的。
调用其他脚本中if __name__ == '__main__':的时候，name为对应脚本名
"""
