#/usr/bin/python3
#-*- coding :utf-8 -*-
import re
import csv
from collections import namedtuple
class filechecker():
	def __init__(self,tbd):
		self.file,self.developer = tbd

	def checkerule(self,file=self.file):
		err = []
		if file.find(' '):
			err.append((file,'文件名含有空格。'))
		if len(file) > 30:
			err.append((file,'文件名超长。'))
		if dosorunix(file):
			err.append((file, '文件为dos格式。'))
		if file.endswith(".sql"):
			pass
		elif file.endswith(".sh"):
			pass
		elif file.endswith(".cfg"):
			pass

	def content(self,file):
		with open(file,'rb') as f:
			content = f.read()
		return content

	def dosorunix(self,content):
		if re.findall(r'\r\n',content):
			return True
		else:
			return False

	def authorin(self,content):
		if re.findall(self.developer):
			return True
		else:
			return False

	def jobnum2mail(self,jobnum:str):
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
		with open(cfg,'r',encoding='utf-8')  as f:
			csvfile = csv.DictReader(f)
			j2m_dict = {d['JobNumber']:d['Email'] for d in csvfile}
			return j2m_dict
			# 	print(row['JobNumber'],row['Name'],row['Email'])

if __name__ == '__main__':
	pass




