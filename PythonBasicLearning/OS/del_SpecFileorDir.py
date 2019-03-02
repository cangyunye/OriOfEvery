
title = 'this is a test for del svn directorys'

import os
import sys
import stat
import time

DEL_DIR=['.svn', '.CVS']
DEL_FILE=['.bak', '.back','.o']
log='delsvn.log'

def creatlog(object):
    if os.path.isdir(object):
        name = object + "\\" + log
    else:
        return False
    f=open(name, "w+")

   return f


def writelog(object):
    t=time.strftime("%Y%m%d %H:%M:%S")

    if os.path.isdir(object):
        line=t+" delete dir:"+object+"\n"

    else:
        line=t+" delete file:"+object + "\n"
    loghandel.write(line)
    loghandel.flush()
    
def closelog():
        loghandel.close()

def isdeldir(object):
    if not os.path.isdir(object):
        return False
    path, curdir = os.path.split(object)

    if not curdir:
        return False

    for eachfile in DEL_DIR :
        if eachfile == curdir:
            return True 

    return False

def isdelfile(object):
    if os.path.isfile(object):
        path, suff = os.path.splitext(object)

    else:
        return False

    if suff:
        for each in DEL_FILE :
            if each == suff:
                return True

    return False
        
def deldir(object):
    for file in os.listdir(object):
        file = os.path.join(object, file)

        if os.path.isdir(file):
            print("remove dir", file)
            os.chmod(file, stat.S_IWRITE|stat.S_IWOTH)
            deldir(file)
            writelog(file)

        elif os.path.isfile(file) :
            print("remove file", file)
            os.chmod(file, stat.S_IWRITE|stat.S_IWOTH)
            os.remove(file)
            writelog(file)
    os.rmdir(object)


def delfile(object):
    if isdelfile(object):
        print("del file", object)
        try:
            os.remove(object)
        except IOError as e:
            print("error ,", e.message)
        writelog(object)


def deldirfile(object):
    if os.path.isdir(object):
        files=os.listdir(object)
        for file in files:
            file = os.path.join(object, file)
            if os.path.isdir(file):
                if isdeldir(file):
                    try:                   
                        deldir(file)
                    except IOError:
                        print ('error ', IOError.message)
                else:
                    deldirfile(file)       
            elif os.path.isfile(file):
                delfile(file)
    elif os.path.isfile(object) :       
        delfile(object)
    else:
        print ( "undefined " , object )

def main(object):
    curpath = os.curdir 
    if len(sys.argv) > 1:
        curpath = sys.argv[1]    
    try:
        print(curpath)
        global loghandel
        loghandel=creatlog(curpath)
        if not loghandel:
            print ("creat log error ", curpath)
        deldirfile(curpath)
        closelog()
    except IOError:
        print ("error is ", IOError.message)
    print ("end")


if __name__ == '__main__':
    main(sys.argv)
    if not loghandel.closed:
        loghandel.flush()
        closelog()
    
