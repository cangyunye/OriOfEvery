"""
    文件操作
    open('filename','mode')
    mode:打开模式
    r 只读，文件不存在则报错
    w 只写，文件不存在则自动创建
    a 在文件末尾附加
    b 二进制模式
    t 文本模式(default)
    r+ 读写
    write():将文本数据写入文件中
    writelines():将字符串列表写入文件中
    f.tell()返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
    f.seek(offset, from_what)
    from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
    seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
    seek(x,1) ： 表示从当前位置往后移动x个字符
    seek(-x,2)：表示从文件的结尾往前移动x个字符
    next()：返回文件下一行
    close():终止与文件的关联
"""
#文件名
file_name = 'passnote.txt'
#设置循环开关
iscontinue = 1
#打开文件追加
f1 = open(file_name,'a')
# with open(file_name,'a') as f1:  使用with，在with的“:”内，用完自动关闭
print('type of open is [%s]' % type(f1))
while iscontinue == 1 :
    #待组合文本
    user = input('请输入用户名:')
    password = input('请输入密码:')
    #控制写入文本组合，利用\n切行
    text_format1 =user + '/' + password + '\n'
    print('密令写入成功')
    f1.write('$$密令>用户名：{},密码：{}\n'.format(user,password))
    # f1.write(text_format1)
    iscontinue = int(input('是否继续？(1/0)'))
f1.close
