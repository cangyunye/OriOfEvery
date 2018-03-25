"""
•ord是unicode ordinal的缩写,即编号
•chr是character的缩写,即字符
•ord和chr是互相对应转换的.
•但是由于chr局限于ascii,长度只有256,于是又多了个unichr.
"""
import random as rdm
def random_verification():
    #4位的验证码
    v = []
    i = 1
    for i in range(4) :
        #必须转化为4位
        v.append(str(rdm.randint(0,9)))
    print('验证码：',v)
    return v
def verification(z,chs):
    #验证输入
    if len(chs) != 4 :
        print('Wrong of the verification!')
        verification()
    elif chs[0] == z[0] and chs[1] == z[1] and chs[2] == z[2] and chs[3] == z[3] :
        print('execellent!')
    else :
        print('There must be somewhere wrong!')

def main():
    z=random_verification()
    chs = input('Please input 4 character:\n')
    verification(z,chs)
if __name__ == '__main__':
    main()
