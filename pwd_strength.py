"""
    功能：密码强度检测
    长度判断：len() 返回字符串长度
    包含数字判断：isnumeric() 返回True
    包含字母判断：isalpha() 返回True
"""
def check_len(password):
    #定义密码长度大于8
    if len(password) > 8 :
        return True
    print('密码要求长度大于8位！')
    return False
def check_num_exist(password):
    #判断密码是否含数字
    for i in password:
        if i.isnumeric() :
            return True
    print('密码要求包含数字！')
    return False
def check_alp_exist(password):
    #判断字母是否含数字
    for i in password:
        if i.isalpha() :
            return True
    print('密码要求包含字母！')
    return False
def pwd_level(boolvalue):
    if boolvalue :
        return 1
    return 0
def pwd_confirm(password):
    #密码可尝试输入次数
    try_times = 1
    while try_times <= 5:
        pass_word_confirm = input('请确认密码：')
        if password == pass_word_confirm:
            print('密码确认通过。')
            #通过标记
            return 'pass'
        print('密码输入错误已达{}次，密码确认失败'.format(try_times))
        try_times += 1
    #失败标记
    return 'fail'

def main():
    #密码强度变量
    pwdlevel = 0
    #符合规则，密码强度增加
    password = input('请输入密码：')
    pwdlevel += pwd_level(check_len(password))+pwd_level(check_alp_exist(password))+pwd_level(check_num_exist(password))
    print('密码级别为：',pwdlevel)
    if pwdlevel >= 3 :
        print('恭喜，密码强度合格！')
    #将密码写入文件
    f1 = open('password_tmp.txt','a')
    #控制写入文本组合
    print(text1,'密码已写入文件')
    text1 ='user' + password + pwdlevel + '\n'
    f1.write(text1)
    f1.close
    pwd_confirm(password)

if __name__ == '__main__':
    main()
