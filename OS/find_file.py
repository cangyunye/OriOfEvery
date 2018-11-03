
#coding:cp936

import os
#保存当前有的磁盘
def existdisk():
	curdisks = []
	allDisks = ['C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', \
			    'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', \
                'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:', 'A:', 'B:']
	for disk in allDisks:
		if os.path.exists(disk):
			curdisks.append(disk)
			
	return curdisks

#目录中含有查找的字符
def SearchDirFile(path, src):
	if not os.path.exists(path):
		print "%s 路径不存在" % path
	for root , dirs, files in os.walk(path, True):
		if - 1 != root.find(src):   #路径名中是否存在要查找的字符
			print root  
		for item in files:
			 path = os.path.join(root, item)
			 if - 1 != path.find(src):         #文件列表中是否有要查找的字符
			 	print path

			 	
			 	
#查找文件内容中有要查找的字符
def SearchFile(path, src):	
	if not os.path.exists(path):
		print "%s 路径不存在" % path
	for root, dirs, files in os.walk(path, True):
		for item in files:
			path = os.path.join(root, item)
			
			try:
				f = open(path, 'r')
				for eachline in f.readlines():
					if - 1 != eachline.find(src):    #文本内容中是否有要查找的字符
						print path
						f.close()
						break
			except:
				pass
	
#www.iplaypy.com	
#查找当前所有磁盘目录下是否有要找的字符
def   SearchAllDirFile(src):	
	curdisks = existdisk()
	for disk in curdisks:
		disk = disk + '\\'
		SearchDirFile(disk, src)
	print "完成搜索"
	
#查找当前所有磁盘目录文件内容下是否有要找的字符
def   SearchALLFile(src):			
	curdisks = existdisk()
	for disk in curdisks:
		disk = disk + "\\"
		SearchFile(disk, src)
	print "完成搜索"
	
	
SearchALLFile('XXX')
