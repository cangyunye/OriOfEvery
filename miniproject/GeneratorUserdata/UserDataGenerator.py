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
from shutil import rmtree
import logging
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
		# 目录结构完整
		self.direxist(busidir)
		self.direxist(sqlfdir)
		self.direxist(predata)

	def direxist(self,dir):
		# 目录创建
		if not os.path.exists(dir):
			os.makedirs(dir,mode=0o777)

	def getinfo(self,servnumber):
		"""获取用户基本信息
		:param servnumber:
		:return:()
		"""
		oracleconn = eval(self.init_dict['oracleconn'])
		timestenconn = eval(self.init_dict['timestenconn'])
		DBO = DataBaseOperator(*oracleconn)
		DBT = DataBaseOperator(*timestenconn)
		def ret(DB,sql):
			dout = DB.output(DB.run(sql),decode='utf-8')
			if dout[0]:
				return dout
			else:
				return ['None']
		# ret = lambda DB,sql:DB.output(DB.run(sql),decode='utf-8') if :DB.output(DB.run(sql),decode='utf-8')[0] else ['None']
		subsl = []
		subs_info = namedtuple('subs',['servnumber','subsid','acctid','custid','region','brand','active','nodeid'])
		
		# 用户基本信息
		subs_sql = f"select servnumber,subsid,acctid,custid,region,brand from hsc_subs_subscriber where servnumber='{servnumber}';"
		tmp00 = ret(DBT,subs_sql)
		if  'None'  not in tmp00:
			subsl += ret(DBT,subs_sql) + [self.init_dict['active'],self.init_dict['nodeid']]
		else:
			os._exit(0)
		# 元组组装
		subs = subs_info._make(subsl)
		# map(subs_info._make, subsl)

		# 用户激活信息
		active_sql = f"select active from hsc_subs_additional where subsid=f{subs.subsid};"
		tmp0 = ret(DBT,active_sql)[0]
		if tmp0 != 'None':
			subs = subs._replace(active=tmp0)
		else:
			print("There isn't active data.")
		route1_sql = f"select data_nodeid from hsc_route_nbr where servnumber='{servnumber}';"
		route2_sql = f"select nodeid from hsc_nosect_abmnode where beginno>={servnumber} and endno<={servnumber};"
		tmp1 = ret(DBO,route1_sql)[0]
		tmp2 = ret(DBO,route2_sql)[0]

		if tmp2 != 'None':
			subs = subs._replace(nodeid=tmp2)
		elif tmp1 != 'None':
			subs = subs._replace(nodeid=tmp1)
		else:
			print("There isn't route data.")
		# 加载到全局变量
		self.init_dict['servnumber']=subs.servnumber
		self.init_dict['subsid']=subs.subsid
		self.init_dict['acctid']=subs.acctid
		self.init_dict['custid']=subs.custid
		self.init_dict['region']=subs.region
		self.init_dict['brand']=subs.brand
		self.init_dict['active']=subs.active
		self.init_dict['nodeid']=subs.nodeid
		print(subs)
		return subs
		

	def replace_dict(self,cfgfile='GlobalSettings.ini'):
		"""
		从ini文件获取所有变量保存到全局字典
		:param cfgfile:
		:return:
		"""
		cfg = ConfigParser()
		cfg.read(cfgfile,encoding='utf-8')

		# 用户数据段
		for col in cfg['sqlvar']:
			if self.init_dict[col]:
				continue
			self.init_dict[col] = cfg['userdata'][col]
		# eval解析段
		for col in cfg['pyeval']:
			if self.init_dict[col]:
				continue
			self.init_dict[col] = eval(cfg['pyeval'][col])
		# 数据库连接信息段
		for col in cfg['dbconstr']:
			if self.init_dict[col]:
				continue
			self.init_dict[col] = cfg['dbconstr'][col]
		# 配置文件自定义段
		for sec in cfg['configfile']:
			if self.init_dict[sec]:
				continue
				self.init_dict[sec] = cfg['configfile'][sec]
		# 从sectiondef段读取其他需要读取的配置段
		for spe in cfg['secdef']:
			for col in cfg[spe]:
				if self.init_dict[col]:
					# 优先级最低，不覆盖
					continue
				self.init_dict[col] = cfg[spe][col]
		return self.init_dict

	def mfdate(self,inidate,mode=1):
		# 读取ini中的datetime对象进行格式化,废弃，改为配置文件中指定section进行读取
		if mode == 1:
			statement='(%s).' % (inidate)+'strftime("%Y-%m-%d %H:%M:%S")'
		elif mode ==2:
			statement='(%s).' % (inidate)+'strftime("%Y%m%d%H%M%S")'
		elif mode ==3:
			statement='(%s).' % (inidate)+'strftime("%Y-%m-%d")'
		elif mode ==4:
			statement='(%s).' % (inidate)+'strftime("%Y%m00")'
		return eval(statement)

	def selfclean(self,cfg='clean_Common_0001.json'):
		#清理表，通用清理方案
		jdata = self.readcfg(cfg=cfg)
		u = self.cfgparser(jdata)
		for tbdsql,DbDriver in u:
			print(f"DbDriver={DbDriver},tbdsql={tbdsql}")
			# sql = self.replacer(tbdsql,**self.init_dict)
			self.sql_list.append((tbdsql,DbDriver))

	def cbrand(self,cfg='base_BrandSzx_0001.json'):
		if self.init_dict['brand'].upper()=='SZX':
			#加载预付费专属配置ABM_BILL_DAY等等
			# sql数据列
			jdata = self.readcfg(cfg=cfg)
			u = self.cfgparser(jdata)
			for tbdsql,DbDriver in u:
				print(f"DbDriver={DbDriver},tbdsql={tbdsql}")
				# sql = self.replacer(tbdsql,**szx_dict)
				self.sql_list.append((tbdsql,DbDriver))
		elif self.init_dict['brand'].upper()=='GT':
			pass
		else:
			print("May be wrong with cfgfiles.")


	def cactive(self,cfg):
		# 调用sqlplus查询，或者直接给定状态
		if self.init_dict['active'] is True:
			#加载激活专属配置
			# act_dict = {'active':1} 废弃，改为使用全局配置
			# sql数据列
			jdata = self.readcfg(cfg=cfg)
			u = self.cfgparser(jdata)
			for tbdsql,DbDriver in u:
				print(f"DbDriver={DbDriver},tbdsql={tbdsql}")
				# sql = self.replacer(tbdsql,**act_dict)
				self.sql_list.append((tbdsql,DbDriver))
		elif self.init_dict['active'] is False:
			pass
		else:
			print("May be wrong with cfgfiles.")

	def croute(self,cfg='route_BrandSzx_0001.json'):
		# 调用sqlplus查询，或者直接给定状态
		if self.init_dict['nodeid'] is True:
			# sql数据列
			jdata = self.readcfg(cfg=cfg)
			u = self.cfgparser(jdata)
			for tbdsql,DbDriver in u:
				print(f"DbDriver={DbDriver},tbdsql={tbdsql}")
				# sql = self.replacer(tbdsql,**r_dict)
				self.sql_list.append((tbdsql,DbDriver))
		elif self.init_dict['nodeid'] is False:
			pass
		else:
			print("May be wrong with cfgfiles.")

	def busidata(self,cfg='base_prod206_0001.json'):
		# 选择业务数据生成
		jdata = self.readcfg(cfg=self.init_dict['bcfg'])
		u = self.cfgparser(jdata)
		for tbdsql,DbDriver in u:
			print(f"DbDriver={DbDriver},tbdsql={tbdsql}")
			# sql = self.replacer(tbdsql,**self.init_dict)
			self.sql_list.append((tbdsql,DbDriver))

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
			sql = self.replacer(jdata[k],**self.init_dict)
			# sql = jdata[k]
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
		except KeyError as e:
			print(e)
			print("配置字典缺少对应值。")

	def ltuple2dict(self,ltuple):
		"""
		sqllist trans to sqldict
		:param ltuple:
		:return:
		"""
		dtuple = {}
		# 统计key值
		allkey = set([x[1] for x in ltuple])
		for db in allkey:
			# 根据每个key构造对应的[]
			dtuple[db] = []
		for tup in ltuple:
			dtuple[tup[1]].append(tup[0])
		return dtuple

	def generator(self,sqllist):
		"""
		DbDriver,tbdsql in cfgparser(jdata)
		:param sql:
		:param DbDriver:
		:return:
		"""
		sqld = os.path.join(sqlfdir,self.init_dict['servnumber'])
		if not os.path.exists(sqld):
			os.makedirs(sqld)
		else:
			rmtree(sqld)
			os.makedirs(sqld)
		# 根据DbDriver归类
		sqldict = self.ltuple2dict(sqllist)
		for DbDriver in sqldict.keys():
			filename = f"{DbDriver}_{self.init_dict['servnumber']}.sql"
			with open(os.path.join(sqld,filename),'a',encoding='utf-8') as f:
				sqllist = sqldict[DbDriver]
				for sql in sqllist:
					f.write(sql)
					f.write("\n")
					
	def sqlexecutor(self):
		#执行对应号码下的所有脚本
		pass

	def process(self,**kwargs):
		"""
		Do not disturb the order
		Especially Function replace_dict
		"""
		# 加载全局变量
		if kwargs.get('cfgfile',None):
			self.replace_dict(kwargs['cfgfile'])
		else:
			self.replace_dict('GlobalSettings.ini')
		
		# 获取用户现存资料
		if kwargs.get('servnumber',None):
			self.getinfo(kwargs['servnumber'])
		else:
			self.getinfo(self.init_dict['servnumber'])

		# 品牌判断
		if kwargs.get('brand',None):
			self.cbrand(kwargs['brand'])
		else:
			self.cbrand(self.init_dict['servnumber'])
		# 是否激活
		if kwargs.get('brand',None):
			self.cbrand(kwargs['brand'])
		else:
			self.cbrand(self.init_dict['servnumber'])
		self.cactive(self.init_dict['active'])
		# 是否有路由信息
		if kwargs.get('brand',None):
			self.cbrand(kwargs['brand'])
		else:
			self.cbrand(self.init_dict['servnumber'])
		self.croute(self.init_dict['nodeid'])
		# 数据清理
		if kwargs.get('brand',None):
			self.selfclean()
		else:
			self.selfclean(self.init_dict['scfg'])
		# 业务数据
		if kwargs.get('brand',None):
			self.busidata()
		else:
			self.busidata(self.init_dict['bcfg'])
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