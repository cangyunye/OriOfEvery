#/usr/bin/python3
#-*- coding :utf-8 -*-
#@author :cangyunye
#@email :cangyunye@gmail.com
import os
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
from utils import lunar,DataBaseOperator
from configparser import ConfigParser
from collections import namedtuple,defaultdict

#init
__brand__=["BrandSzx","BrandGotone"]

#root path for os.path.join
rootdir=os.getcwd()
busidir=os.path.join(rootdir,'business')
sqlfdir=os.path.join(rootdir,'sqlfiles')
predata=os.path.join(rootdir,'predata')
dt = datetime.now()

class UserDataGenerator():
	def __init__(self, servnumber):
		self.servnumber = str(servnumber)
		# global store
		self.init_dict = defaultdict(lambda:None)
		self.sql_list = []

	def direxist(self,dir):
		# 目录创建
		if not os.path.exists(dir):
			os.makedirs(dir,mode=0o777)

	def getinfo(self,servnumber):
		"""获取用户基本信息
		:param servnumber:
		:return:()
		"""
		DBO = DataBaseOperator('root', 'passwd', '127.0.0.1', 'oracle')
		DBT = DataBaseOperator('root', 'passwd', '127.0.0.1', 'timesten')
		retf = []
		subs_info = namedtuple('subs',['servnumber','subsid','acctid','custid','region','brand','active','route','nodeid'])
		subs_sql = "select servnumber,subsid,acctid,custid,region,brand from hsc_subs_subscriber where servnumber=%s;" % (servnumber)
		# 返回二进制结果
		ret = DBT.run(subs_sql)
		if ret :
			# 二进制解码与格式调整
			retf +=DBT.output(ret)
		else:
			retf +=['None']*6

		active_sql = "select active from hsc_subs_active where subsid=%s;"% (retf[1])
		ret = DBT.run(active_sql)
		if ret :
			retf +=DBT.output(ret)
		else:
			retf +=['None']

		route_sql = "select nodeid from hsc_route_nbr where servnumber=%s;"% (servnumber)
		ret = DBO.run(route_sql)

		if ret :
			retf +=DBO.output(ret)
		else:
			retf +=['None']

		# sql4 = "select decode(count(1),0,'False','True') from hsc_route_node where beginno>=%s and endnno <=%s;"% (servnumber,servnumber)
	
		"""查询结果桩模拟
		subsid  = '100'+servnumber
		acctid  =  '101'+servnumber
		custid  =  '102'+servnumber
		region  = 200 if True else 759
		brand  = 'BrandSzx'
		active  = True
		route  = True
		nodeid  = 2522"""
		# map(info._make, cursor.fetchall())
		# subs = info(servnumber,subsid,acctid,custid,region,brand,active,route,nodeid)
		# subs = subs_info._make(retf)
		subs = subs_info(retf)
		# 加载到全局变量
		self.init_dict['servnumber']=subs.servnumber
		self.init_dict['subsid']=subs.subsid
		self.init_dict['acctid']=subs.acctid
		self.init_dict['custid']=subs.custid
		self.init_dict['region']=subs.region
		self.init_dict['brand']=subs.brand
		self.init_dict['active']=subs.active
		self.init_dict['route']=subs.route
		self.init_dict['nodeid']=subs.nodeid
		
		return subs
		

	def replace_dict(self,cfgfile='GlobalSettings.ini'):
		"""
		从ini文件获取所有变量保存到全局字典
		:param cfgfile:
		:return:
		"""
		cfg = ConfigParser()
		cfg.read(cfgfile,encoding='utf-8')
		seclist = [sec for sec in cfg.sections()]
		for sec in seclist:
			for col in cfg[sec]:
				if self.init_dict[col]:
					# 已加载变量不重复加载
					continue
				self.init_dict[col] = cfg[sec][col]
				# pprint(self.init_dict)
		return self.init_dict

	def mfdate(self,inidate,mode=1):
		# 读取ini中的datetime对象进行格式化
		if mode == 1:
			statement='(%s).' % (inidate)+'strftime("%Y-%m-%d %H:%M:%S")'
		elif mode ==2:
			statement='(%s).' % (inidate)+'strftime("%Y%m%d%H%M%S")'
		elif mode ==3:
			statement='(%s).' % (inidate)+'strftime("%Y-%m-%d")'
		elif mode ==4:
			statement='(%s).' % (inidate)+'strftime("%Y%m00")'
		return eval(statement)

	def selfclean(self):
		#清理表，通用清理方案
		jdata = self.readcfg(cfg='clean_Common_0001.json')
		u = self.cfgparser(jdata)
		for tbdsql,DbDriver in u:
			print(f"DbDriver={DbDriver},tbdsql={tbdsql}")
			sql = self.replacer(tbdsql,**self.init_dict)
			self.sql_list.append((sql,DbDriver))

	def cbrand(self,brand):
		if brand.upper()=='SZX':
			#加载预付费专属配置ABM_BILL_DAY等等
			szx_dict = {'billtime':dt.strftime("%Y%m%d"),
						'billday':dt.strftime("%Y%m%d"),
						'nextbillday':lunar(dt).nextbillday,
						'billcycle':dt.strftime("%Y%m00")}
			# sql数据列
			jdata = self.readcfg(cfg='base_BrandSzx_0001.json')
			u = self.cfgparser(jdata)
			for tbdsql,DbDriver in u:
				print(f"DbDriver={DbDriver},tbdsql={tbdsql}")
				sql = self.replacer(tbdsql,**szx_dict)
				self.sql_list.append((sql,DbDriver))
		elif brand.upper()=='GT':
			pass
		else:
			print("May be wrong with cfgfiles.")


	def cactive(self,active):
		# 调用sqlplus查询，或者直接给定状态
		if active is True:
			#加载激活专属配置
			act_dict = {'active':1}
			# sql数据列
			jdata = self.readcfg(cfg='active_BrandSzx_0001.json')
			u = self.cfgparser(jdata)
			for tbdsql,DbDriver in u:
				print(f"DbDriver={DbDriver},tbdsql={tbdsql}")
				sql = self.replacer(tbdsql,**act_dict)
				self.sql_list.append((sql,DbDriver))
		elif active is False:
			pass
		else:
			print("May be wrong with cfgfiles.")


	def croute(self,route):
		# 调用sqlplus查询，或者直接给定状态
		if route is True:
			#加载路由专属配置
			r_dict = {'nodeid':2522}
			# sql数据列
			jdata = self.readcfg(cfg='route_BrandSzx_0001.json')
			u = self.cfgparser(jdata)
			for tbdsql,DbDriver in u:
				print(f"DbDriver={DbDriver},tbdsql={tbdsql}")
				sql = self.replacer(tbdsql,**r_dict)
				self.sql_list.append((sql,DbDriver))
		elif route is False:
			pass
		else:
			print("May be wrong with cfgfiles.")

	def busidata(self,cfg='base_prod206_0001'):
		# 选择业务数据生成
		jdata = self.readcfg(cfg)
		u = self.cfgparser(jdata)
		for tbdsql,DbDriver in u:
			print(f"DbDriver={DbDriver},tbdsql={tbdsql}")
			sql = self.replacer(tbdsql,**self.init_dict)
			self.sql_list.append((sql,DbDriver))
	def readcfg(self,cfg):
		#读取单个配置
		cfg = os.path.join(busidir,cfg)
		with open(cfg,'r',encoding='utf-8') as f:
			jdata=json.load(f)
		#删除注释
		del jdata['note']
		return jdata


	def cfgparser(self,jdata):
		"""
		加载业务配置
		:param jdata:
		:return:
		"""
		for k in jdata.keys():
			# DbDriver,Table,DML,BusiUniq = k.split(".")
			DbDriver = k.split(".")[0]
			sql = self.replacer(jdata[k],**{})
			# print(sql,DbDriver)
			yield sql,DbDriver


	def replacer(self,tbdsql,**var_dict):
		"""
		:param tbd:sql model to be replace.
		:param var_dict:matched variables for sql model.
		:return:
		"""
		try:
			sql = tbdsql.format(**var_dict)
			return sql
		except ValueError as e:
			print(e)
			print("通常来说，你可能输错值了。")

	def generator(self,sql,DbDriver='oracle'):
		"""
		DbDriver,tbdsql in cfgparser(jdata)
		:param sql:
		:param DbDriver:
		:return:
		"""
		os.makedirs(self.servnumber)
		with open(os.path.join(sqlfdir,self.servnumber,'%s_%s.sql' % (DbDriver,self.servnumber)),'a',encoding='utf-8') as f:
			f.write(sql)
			f.write("\n")
		print("记录追加:%s_%s.sql" % (DbDriver,self.servnumber))

	def sqlexecutor(self):
		#执行对应号码下的所有脚本
		pass

	def process(self):
		# 目录结构完整
		self.direxist(busidir)
		self.direxist(sqlfdir)
		self.direxist(predata)
		# 获取用户现存资料
		subs=self.getinfo(self.servnumber)
		# 品牌判断
		self.cbrand(subs.brand)
		# 是否激活
		self.cactive(subs.active)
		# 是否有路由信息
		self.croute(subs.route)
		# 加载全局变量
		self.replace_dict()
		# 数据清理
		self.selfclean()
		# 业务数据
		self.busidata()
		# 生成sql文件
		self.generator(self.sql_list)
		# sql执行器
		self.sqlexecutor()

def main():
	# test
	servnumber=13502400909
	tester=UserDataGenerator(servnumber)
	tester.process()

if __name__ == '__main__':
	main()