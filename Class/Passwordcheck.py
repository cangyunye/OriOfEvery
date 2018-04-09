"""
    功能：密码强度检测
    Python中就规定好了，类中函数的第一个参数，就必须是实例对象本身，并且建议，约定俗成，把其名字写为self
    所以class中的self在类中所有函数中出现在第一个参数
    self即实例，在class中用于贯通的实例
    当以class PasswordTool定义到实例pwdt中时，pwdt即代替了所有self
    类中方法即函数,没有对应实例，方法是无法被调用的
    类中内建函数
    dir():返回对象属性的名字列表
    __dict__：返回字典(属性名+键值)
    __name__:类的名字（字符串）
    __bases__：类的所有父类构成元组
    __module__:类定义所在的模块
    __class__：实例所对应的类
"""
class PasswordTool:#类名首字母大写
    """
        密码工具类
    """
    def __init__(self,password):
        #类的属性初始化，调用类时，自动调用，且定义类的传入参数
        self.password = password
        self.pwdlevel = 0
        self.try_times = 1
            #类的方法
    def check_len(self):
        #定义密码长度大于8
        if len(self.password) > 8 :
            return True
        print('密码要求长度大于8位！')
        return False
    def check_num_exist(self):
        #判断密码是否含数字
        for i in self.password:
            if i.isnumeric() :
                return True
        print('密码要求包含数字！')
        return False
    def check_alp_exist(self):
        #判断字母是否含数字
        for i in self.password:
            if i.isalpha() :
                return True
        print('密码要求包含字母！')
        return False
    def pwd_confirm(self):
        while self.try_times <= 5:
            pass_word_confirm = input('请确认密码：')
            if self.password == pass_word_confirm:
                print('密码确认通过。')
                #不知道什么情况，return无法退出函数
                self.try_times = 6
                #通过标记
                return 'pass'
            print('密码输入错误已达{}次，密码确认失败'.format(self.try_times))
            self.try_times += 1
        #失败标记
        return 'fail'
    #密码级别升位
    def pwd_level(self,boolvalue):
        if boolvalue :
            return 1
        return 0
    def pwdlevelup(self):#连续调用3种强度检测
        self.pwdlevel += self.pwd_level(self.check_len())+self.pwd_level(self.check_alp_exist())+self.pwd_level(self.check_num_exist())
    def process(self):
        # self.check_len()
        # self.check_alp_exist()
        # self.check_num_exist()
        self.pwdlevelup()
        print('密码级别为：',self.pwdlevel)
        if self.pwdlevel >= 3 :
            print('恭喜，密码强度合格！')
        else:
            self.pwdlevel = 0 #重置密码强度以免累加
            self.password = input('请重新输入密码：')
            self.process()
        self.pwd_confirm()

class FileTool:
    """
    文件工具类
    """
    def __init__(self,filepath):
        self.filepath = filepath
    def write_to_file(self,line):
        ff = open(self.filepath,'a')
        lines = ff.write(line)
        ff.close
    def read_from_file(self):
        ff = open(self.filepath,'r')
        lines = ff.read()
        ff.close
        return lines

def main():
    password = input('请输入密码：')
    #密码实例化工具对象
    pwdt = PasswordTool(password)
    pwdt.process()
    text1 ='user' + pwdt.password + str(pwdt.pwdlevel) + '\n'
    #文件操作实例化工具对象
    ft = FileTool('file_tmp.txt')
    # ft.write_to_file(text1)
    ft.write_to_file('yaaaa\n')
    lines = ft.read_from_file()
    print(lines)
    print(dir(PasswordTool))#通过类中内建函数查看类中属性
    print(PasswordTool.__dict__)#通过类中内建函数查看类中属性
if __name__ == '__main__':
    main()
