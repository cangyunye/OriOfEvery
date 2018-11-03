
# coding=gbk
  
import os,ConfigParser

'''
递归列出某目录下的文件，放入List中
'''
def listDir (fileList,path):
    files=os.listdir(path)

    for i in  files:
        file_path=path+"\\"+i
        if os.path.isfile(file_path):
            fileList.append(file_path)

    for i in files:
        file_path=path+"\\"+i
        if os.path.isdir(file_path):
            #fileList.append(file_path)
            listDir(fileList,file_path)

    return fileList

'''
将List中内容写入文件
www.iplaypy.com
'''
def writeListToFile(list,path):
    strs="\n".join(list)
    f=open(path,'wb')
    f.write(strs)
    f.close()


'''
读入文件内容并放入List中
'''
def readFileToList(path):
    lists=[]
    f=open(path,'rb')
    lines=f.readlines()
    for line in lines:
        lists.append(line.strip())
    f.close()
    return lists


'''
比较文件--以Set方式
'''
def compList(list1,list2):
    return list(set(list1)-set(list2))

'''
复制List中文件到指定位置
'''
def copyFiles(fileList,targetDir):

    for file in fileList:
        targetPath=os.path.join(targetDir,os.path.dirname(file))
        targetFile=os.path.join(targetDir,file)

        if not os.path.exists(targetPath):
            os.makedirs(targetPath)

        if not os.path.exists(targetFile) or (os.path.exists(targetFile) and os.path.getsize(targetFile)!=os.path.getsize(file)):
            print "正在复制文件："+file
            open(targetFile,'wb').write(open(file,'rb').read())

        else:
            print "文件已存在，不复制！"


if __name__ == '__main__':
    path=".svn"
    #获取源目录
    
    txtFile="1.txt"
    #目录结构输出的目的文件
    
    tdir="cpfile"
    #复制到的目标目录
    
    cfFile="config.ini";
    #配置文件文件名
    fileList=[]
    
    #读取配置文件
    if(os.path.exists(cfFile)):
        cf=ConfigParser.ConfigParser()
        cf.read(cfFile)
        
        path=cf.get("main", "sourceDir")
        txtFile=cf.get("main","txtFile")
        tdir=cf.get("main","targetDir")
    else:
        print "配置文件不存在！"
        raw_input("\n按 回车键 退出\n")

        exit()
    
    if(os.path.exists(txtFile)):
        #如果导出的文件存在，就读取后比较
        list1=readFileToList(txtFile)

        print "正在读取文件列表……"

        fileList=listDir (fileList,path)

        print "正在比较文件……"

        list_res=compList(fileList,list1)
        
        if len(list_res)>0:
            print "以下是原目录中不存在的文件：\n"
            print "\n".join(list_res)
            print "\n共计文件数："+str(len(list_res))+"\n"
            if raw_input("\n是否复制文件？（y/n）")!='n':
                copyFiles(list_res,tdir)
        else:
            print "没有不相同的文件！"
    else:
        #如果导出的文件不存在，则导出文件
        print "正在读取文件列表……"
        fileList=listDir (fileList,path)
        writeListToFile(fi
2000
leList,txtFile)
        print "已保存到文件："+txtFile
        
    raw_input("\n按 回车键 退出\n")
