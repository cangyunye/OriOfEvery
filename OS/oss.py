# -*- coding:utf-8 -*-
__author__ = 'cangyunye@gmail.com'
import os

def main():
    print(f'Current work path is {os.getcwd()}')
    filepathA='amadefolder\\arent\\nothing'
    filepathB='bmadefolder'
    filepathC='cmadefolder'
    if os.path.isdir(filepathA) is True: #判断filepathA是否目录
        print(f'当前目录:{os.getcwd()}')
        z = os.listdir(filepathA)
        if len(z) != 0 :
            for sth in z:
                print(f'文件:{sth}')
                stho = os.path.join(filepathA,sth) #拼接文件目录与文件名
                print(f'文件地址:{stho}')
                if os.path.isfile(stho):
                    print(stho)
                    os.remove(stho)
        os.removedirs(filepathA)#递归删除目录
    os.makedirs(filepathA, mode=0o777, exist_ok=True)#递归创建目录
    if os.path.exists(filepathB) is True: #判断filepathB是否存在
        os.rmdir(filepathB)#单个目录删除
    os.mkdir('bmadefolder')#单个目录创建
    print(f'There are {os.listdir(os.getcwd())} in this path.')
    os.chdir(filepathA)
    print(f'当前目录:{os.getcwd()}')
    fd = open("wrt.txt",'w+')#读写模式
    context = "Write sth for u.\nWhen you need me,I am near by."
    fd.write(context)
    fd.close()
    with open('wrt.txt','r') as frd: #with无需再close()
        print(frd.readlines())#按行读取转换为列表
        print(frd.readline())#逐行读取
    with open('wrt.txt','r') as frz: #with无需再close()
        print(frz.read())#全部读取或按字节读取

if __name__ == '__main__':
    main()
