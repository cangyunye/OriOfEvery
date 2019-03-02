
#导入方法模块
import os
import tarfile
import gzip
import string 
import shutil

def zipDir(src,dst):
    
    initPath = os.getcwd()
    #tempDST =  os.path.join(os.getcwd(),dst)
    #tempSRC =  os.path.join(os.getcwd(),src)
    os.chdir( src )

    files = os.listdir(src)

    if dst.find("\\") != -1:
        temp = dst.rsplit("\\",1)
        dstname = temp[1]
        dstpath = temp[0]
    #print files


    tar = tarfile.open(dstname,"gz")

    for file in files:
        tar.add(file)
    tar.close()
    os.chdir( initPath )

    if os.path.isfile(dst) == True:
        os.remove(dst)

    shutil.copy(os.path.join(src,dstname), dst)
    os.remove(os.path.join(src,dstname))

    print os.getcwd()


if __name__ == '__main__':
    
    zipDir("D:\\AutoUpdate\\DataDist\\viruswall\\Data\\KSVW-VirusDB\\",
           "d:\\AutoUpdate\\DataDist\\viruswall\\Data\\update\\KSVW-VirusDB.tgz")

