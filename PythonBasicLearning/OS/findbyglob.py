
#encoding=utf-8

import os
import glob

def findfiles(dirname,pattern):
    cwd = os.getcwd() #保存当前工作目录
    if dirname:
        os.chdir(dirname)

    result = []
    for filename in glob.iglob(pattern): #此处可以用glob.glob(pattern) 返回所有结果
        result.append(filename)
    #恢复工作目录
    os.chdir(cwd)
    return result

if __name__ == '__main__': print(findfiles(r'D:\python\windows-service','*.py'))
