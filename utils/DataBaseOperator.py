# /usr/bin/python3
# -*- coding :utf-8 -*-
# @author :cangyunye
# @email :cangyunye@gmail.com
# version:1.0
from subprocess import Popen, PIPE
import re
"""
小结：
1.使用communicate会直接关闭stdin，管道无法设计连续的sql语句在dbdriver中输入
2.如果要将Pin作为with语句输入，实现with内作为一次session模拟连续性输入
参考1不可行，但可采取特别方案，将communicate作为结尾，只调用一次，中间循环接受stdin.write
每次stdin.write必须存在一个用于区分每次
"""
class DataBaseOperator():
	def __init__(self, user, passwd, host, db='oracle'):
		self.user = user
		self.passwd = passwd
		self.host = host
		self.db = db
		self.Pin = None

	def _oraclePin(self):
		try:
			initset = """set head off;
			set linesize 5000;
			set pagesize 0;
			set colsep '|';
			set numwidth 15"""
			conn = 'sqlplus -s %s/%s@%s' % (self.user, self.passwd, self.host)
			Pin = Popen(conn, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
			Pin.stdin.write(initset.encode('ascii')+b'\n')
			return Pin
		except Exception as e:
			print(e)

	def _timestenPin(self):
		try:
			conn = 'ttIsqlCS -v 1 -connStr "dsn=%s;uid=%s;pwd=%s" ' % (
				self.host, self.user, self.passwd)
			Pin = Popen(conn, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
			return Pin
		except Exception as e:
			print(e)

	def _mysqlPin(self):
		try:
			conn = 'mysql -u%s -p%s -h%s -B' % (self.user,
												self.passwd, self.host)
			# conn = 'mysql -u%s -p%s -h%s -s'%(self.user,self.passwd,self.host)
			print(conn)
			Pin = Popen(conn, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
			return Pin
		except Exception as e:
			print(e)

	def runscript(self, script):
		if self.db == 'oracle':
			p = Popen('sqlplus -s %s/%s@%s @%s' % (self.user, self.passwd,
												   self.host, script), shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
		elif self.db == 'timesten':
			p = Popen('ttIsqlCS -connStr "dsn=%s;uid=%s;pwd=%s" -f %s' % (self.host, self.user,
																		  self.passwd, script), shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
		elif self.db == 'mysql':
			p = Popen('mysql -u%s -p%s -h%s < %s' % (self.user, self.passwd,
													 self.host, script), shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
		else:
			raise NotImplementedError("%s not exist!" % (self.db))

	def run(self, sql):
		if self.db == 'oracle':
			self.Pin = self._oraclePin()
		elif self.db == 'timesten':
			self.Pin = self._timestenPin()
		elif self.db == 'mysql':
			self.Pin = self._mysqlPin()
		else:
			raise NameError("DB not exist!")
		self.Pin.stdin.write(sql.encode('ascii')+b'\n')
		(stdout, stderr) = self.Pin.communicate()
		assert self.Pin.returncode == 0, 'Popen cmd failed.'
		return stdout

	def output(self, stdout, decode='utf-8'):
		text = stdout.decode(decode)
		if self.db == 'oracle':
			pattern = re.compile(r'\s')
			output = re.sub(pattern, "", text, re.ASCII).split('|')
		elif self.db == 'timesten':
			pattern = re.compile(r'\s|<|>')
			output = re.sub(pattern, "", text, re.ASCII).split(',')
		elif self.db == 'mysql':
			pattern = re.compile(r'\r|\n')
			output = re.sub(pattern, "", text, re.ASCII).split('\t')
		else:
			raise NotImplementedError("%s not exist!" % (self.db))
		return output


def main():
	DB = DataBaseOperator('root', 'ppppp', '127.0.0.1', 'mysql')
	sql = 'select * from sakila.film  limit 0,5;'
	r = DB.run(sql)
	print(r.decode('utf-8'))
	o = DB.output(r)
	print(o)
if __name__ == "__main__":
	main()

