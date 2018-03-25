from functools import reduce
def is_odd(n):
    yield n
    i = 3
    print (i)
def main():
    l=[1,2,3,4]
    # print(list(map(is_odd,l)))
    # #filter根据list的真假，返回原有list值
    # print(list(filter(is_odd, l)))
    for x in l:
        print(next(is_odd(x)))
if __name__ == '__main__':
    main()
