"""
    读取操作
    read():返回值包含整个文件内容的一个字符串
    readline():返回值为文件下一行内容的字符串
    readlines():返回值为整个文件内容的列表，每项是以换行符为结尾的一行字符串
"""
#先用同目录下open.py写文件
#文件名
file_name = 'passnote.txt'

f1 = open(file_name,'r')
#通过变量存储读取内容
#对于任意情况使用了read方法后，都会影响后续读取
text1 = f1.read()
print('read()\n',text1)
f1.close

f1 = open(file_name,'r')
text2 = f1.readline()
print('readline()\n',text2)
print('After read()\n',f1.read())
f1.close

f1 = open(file_name,'r')
for line in f1:#可以直接用open后的内容做范围判断，无需read()
    print ('$$>\t',line)
f1.close

f1 = open(file_name,'r')
text3 = f1.readlines()
print('readlines()\n',text3 )
print('readlines()[2]=',text3[2])
f1.close
