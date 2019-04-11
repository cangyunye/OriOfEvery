#/usr/bin/python3
#-*- coding :utf-8 -*-
#@author :cangyunye
#@email :cangyunye@gmail.com
from subprocess import Popen,PIPE
import re
from time import sleep
"""
后续考虑，直接继承Popen，然后改写方法
"""
class DataBaseOperator():
	def __init__(self, user, passwd,host,db='oracle'):
		self.user = user
		self.passwd = passwd
		self.host = host
		self.db = db
	
	@property
	def sqlstr(self):
		return self._sqlstr
		
	@sqlstr.setter
	def sqlstr(self,value):
		self._sqlstr=value
	
	def __enter__(self):
		if self.db=='oracle':
			self.server=self.oracleserver()
		elif self.db =='timesten':
			self.server=self.timestenserver()
		elif self.db == 'mysql':
			self.server=self.mysqlserver()
		return self.server

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.close()

	def close(self):
		if self.db=='oracle':
			close=b'quit\n'
		elif self.db =='timesten':
			close=b'quit\n'
		elif self.db == 'mysql':
			close=b'quit\n'
		self.server.stdin.write(close)
	
	def oracleserver(self):
		try:
			server = Popen('sqlplus -s %s/%s@%s'%(self.user,self.passwd,self.host),shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
			initset = """set head off;
			set linesize 5000;
			set pagesize 0;
			set colsep '|';
			set numwidth 15"""
			server.stdin.write(initset.encode('ascii')+b'\n')
			return server
		except Exception as e:
			print(e)

	def timestenserver(self):
		try:
			conn = 'ttIsqlCS -connStr "dsn=%s;uid=%s;pwd=%s" -v 1'%(self.host,self.user,self.passwd)
			server = Popen(conn,shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
			return server
		except Exception as e:
			print(e)

	def mysqlserver(self):
		try:
			conn = 'mysql -u%s -p%s -h%s -B'%(self.user,self.passwd,self.host)
			# conn = 'mysql -u%s -p%s -h%s -s'%(self.user,self.passwd,self.host)
			server = Popen(conn,shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
			return server
		except Exception as e:
			print(e)

	def runscript(self,script):
		if self.db=='oracle':
			p=Popen('sqlplus -s %s/%s@%s @%s'%(self.user,self.passwd,self.host,script),shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
		elif self.db =='timesten':
			p=Popen('ttIsqlCS -connStr "dsn=%s;uid=%s;pwd=%s" -f %s'%(self.host,self.user,self.passwd,script),shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
		elif self.db == 'mysql':
			p=Popen('mysql -u%s -p%s -h%s < %s'%(self.user,self.passwd,self.host,script),shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE)
		else:
			raise NotImplementedError("%s not exist!"%(self.db))

	def run(self,sql=None,server=None):
		if self._sqlstr:
			sql=self._sqlstr
		if self.server:
			server=self.server
		while True:
			if sql:
				try:
					server.stdin.write(sql.encode('ascii')+b'\n')
					(stdout,stderr)=server.communicate()
					yield stdout
				except Exception as e:
					print(e)
			elif sql in ['exit','quit','bye']:
				self.close()
			else:
				sleep(1)

	def output(self,stdout,decode='utf-8'):
		text=stdout.decode(decode)
		if self.db=='oracle':
			pattern = re.compile(r'\s')
			output=re.sub(pattern,"",text,re.ASCII).split('|')
		elif self.db =='timesten':
			pattern = re.compile(r'\s|<|>')
			output=re.sub(pattern,"",text,re.ASCII).split(',')
		elif self.db == 'mysql':
			output=re.split("\t",text)
		else:
			raise NotImplementedError("%s not exist!"%(self.db))
		return output

if __name__ == "__main__":
	with DataBaseOperator('yunye','yunye','ora','oracle') as DB:
		text=DB.stdin.write('select 1+1 from dual;')
	print(text)