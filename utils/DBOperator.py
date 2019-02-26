import subprocess

class oracleop():

	def __init__(self,user,passwd,dsn):
		self.user=user
		self.passwd=passwd
		self.dsn=dsn

	def run(self,sql):
		"""
		:param sql:bytes of sqlstring
		:return:bytes to be decode('utf-8')
		"""

		try:
			conn = "sqlplus -S " + self.user + "/" + self.passwd + "@" + self.dsn
			p = subprocess.Popen(conn,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			p.stdin.write(sql)
			return p.communicate()
		except Exception as e:
			print(e)

