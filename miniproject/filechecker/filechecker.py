#/usr/bin/python3
#-*- coding :utf-8 -*-
import re
import csv
from collections import namedtuple
class filechecker():
	def __init__(self,tbd):
		"""
		:param tbd:(filepath,developer)
		"""
		self.file,self.developer = tbd

	def checkerule(self,file=self.file):
		"""
		检查种类设置
		:param file:
		:return:
		"""
		err = []
		#文件名检查
		if file.find(' '):
			err.append((file,'文件名含有空格。'))
		if len(file) > 30:
			err.append((file,'文件名超长。'))
		if dosorunix(file):
			err.append((file, '文件为dos格式。'))
		#内容检查
		content=self.content(file)
		if file.endswith(".sql"):
			self.sqlcheck(content)
		elif file.endswith(".sh"):
			self.shcheck()
		elif file.endswith(".cfg"):
			pass

	def content(self,file):
		#读取文件
		with open(file,'rb') as f:
			content = f.read()
		return content

	def dosorunix(self,content):
		#判断是否为dos格式
		if re.findall(r'\r\n',content):
			return True
		else:
			return False

	def authorin(self,content):
		#内容中是否带作者名
		if re.findall(self.developer):
			return True
		else:
			return False

	def shcheck(self,content):
		#检查shell
		pass

	def sqlcheck(self,content):
		#检查sql
		self.authorin(content)
		pass

	def cfgcheck(self,content):
		#检查cfg
		pass
	def manualcheck(self,content):
		#检查manual
		pass

	def jobnum2mail(self,jobnum:str):
		#根据工号定位邮箱
		j2m_dict = self.j2mcfg2()
		mail = j2m_dict[str(jobnum)]
		return mail

	def j2mcfg(self,cfg='job2mail.csv'):
		with open(cfg,'r',encoding='utf-8') as f:
			csvfile = csv.reader(f)
			headings = next(csvfile)
			Row = namedtuple('j2m',headings)
			for r in csvfile:
				row = Row(*r)
				print(row.JobNumber,row.Name,row.Email)

	def j2mcfg2(self,cfg='job2mail.csv'):
		"""
		读取配置加载到字典
		:param cfg:
		:return:
		"""
		with open(cfg,'r',encoding='utf-8')  as f:
			csvfile = csv.DictReader(f)
			j2m_dict = {d['JobNumber']:d['Email'] for d in csvfile}
			return j2m_dict
			# 	print(row['JobNumber'],row['Name'],row['Email'])

if __name__ == '__main__':
	pass




