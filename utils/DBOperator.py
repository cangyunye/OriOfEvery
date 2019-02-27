import subprocess

"""
后续需要设计为支持上下文管理器with形式
"""
class oracleop():

	def __init__(self,user,passwd,dsn=None):
		"""
		:param user:
		:param passwd:
		:param dsn: for oracle is dsn,for mysql is host
		"""
		self.user=user
		self.passwd=passwd
		self.dsn=dsn

	def __enter__(self):
		return self

	def __exit__(self, *args):
		self.close()

	def connection(self,database='oracle',mode='s'):
		"""
		:param database:
		:param mode:
		:return:
		"""
		if database.upper() == 'ORACLE':
			conn = "sqlplus -S " + self.user + "/" + self.passwd + "@" + self.dsn
		elif database.upper() == 'MYSQL' :
			conn = "mysql -u" + self.user + " -p" + self.passwd
			if self.dsn:
				conn = conn + " -h" + self.dsn
		else :
			conn = input("ConnectSting:")
		try:
			p = subprocess.Popen(conn, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			if mode.upper() == 'S':
				setinit = """set colsep' ';　　　　 //-域输出分隔符
				set echo off;　　　　 //显示start启动的脚本中的每个sql命令，缺省为on
				set feedback off;　    //回显本次sql命令处理的记录条数，缺省为on
				set heading off;　　 //输出域标题，缺省为on
				set pagesize 9999;　　    //输出每页行数，缺省为24,为了避免分页，可设定为0。
				set linesize 32767;　　   //输出一行字符个数，缺省为80
				set numwidth 40;　    //输出number类型域长度，缺省为10
				set termout off;　　   //显示脚本中的命令的执行结果，缺省为on
				set trimout on;　　　//去除标准输出每行的拖尾空格，缺省为off
				set trimspool on;　　//去除重定向（spool）输出每行的拖尾空格，缺省为off
				set serveroutput off; //设置允许显示输出类似dbms_output
				set timing off;          //设置显示“已用时间：XXXX”
				set autotrace off;    //设置允许对执行的sql进行分析
				set term off verify off feedback off tab off;"""
				p.stdin.write(setinit)
			return p
		except Exception as e:
			print(e)

	def close(self,p):
		p.stdin.write("exit")
		return p.communicate()

	def run(self,sql):
		"""
		:param sql:bytes of sqlstring
		:return:bytes to be decode('utf-8')
		"""
		try:
			conn = "sqlplus -S " + self.user + "/" + self.passwd + "@" + self.dsn
			p = subprocess.Popen(conn,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			p.stdin.write(setinit)
			p.stdin.write(sql)
			return p.communicate()
		except Exception as e:
			print(e)

