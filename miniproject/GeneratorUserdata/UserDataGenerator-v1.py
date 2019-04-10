# !/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import textwrap
import os
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
from utils import lunar
from configparser import ConfigParser
#from pprint import ppringt

__description__ = textwrap.dedent('''\
			About the project you need to know
		 ---------------------------------------
			Designed for generate user data.
			Supplying which is absent from we need.
			Expansibility by configs.
			''')

__version__ = "GU.0.0.2"
parser = argparse.ArgumentParser(description=__description__, formatter_class=argparse.RawDescriptionHelpFormatter,
								 prog='UserDataGenerator', epilog="Nowhere to be seen.")
#argument:servnumber,region,cfgfile
parser.add_argument('servnumber', metavar='servnumber', type=str,
					help='The 11 integer for the servnumber.')

parser.add_argument('region', metavar='region', type=str,
					help='The region of servnumber.')

parser.add_argument('-c','--config', action='append',dest='cfg',nargs='+',
					help='Specific business config.')

#addtional info
parser.add_argument('-b','--brand', required=False, type=str,choices=['szx','SZX','gt','GT'],
					help='Brand like szx as BrandSzx or gt as BrandGotone.')
parser.add_argument('-a','--active', required=False, type=str,action="store_true",
					help='If this servnumber activated.')
parser.add_argument('-r','--route', required=False, type=str,action="store_true",
					help='If route info is exists.')
parser.add_argument('-e','--env', required=False, type=str,choices=['crm','CRM','test','TEST'],
					help='Environment like crm as or test.')

#add_help
parser.add_argument('-v','--version', help='version:%s' % (__version__))
parser.add_argument('-d','--debug',action='store_true',help='show about debug',default=False)


args = parser.parse_args()

#init
__brand__=["BrandSzx","BrandGotone"]
#root path for os.path.join
rootdir=os.getcwd()
busidir=os.path.join(rootdir,'business')
sqlfdir=os.path.join(rootdir,'sqlfiles')
predata=os.path.join(rootdir,'predata')


#global variable for append sql when cbrand,cactive,croute
datalist =[]
sql_list = []
dt = datetime.now()
def direxist(dir):
	if not os.path.exists(dir):
		os.makedirs(dir,mode=0o777)



def replace_dict(cfgfile=os.path.join(busidir,'GlobalSettings.ini')):
	"""
	Get the Variables configfiles for initial.
	:param cfgfile:
	:return:
	"""
	init_dict = {}
	list_key = []
	cfg = ConfigParser()
	cfg.read(cfgfile)
	seclist = [sec for sec in cfg.sections()]
	for sec in seclist:
		for col in cfg[sec]:
			list_key.append(col)
			init_dict[col] = cfg[sec][col]
			# pprint(init_dict)
	return init_dict

def mfdate(inidate,mode=1):
	# 读取ini中的datetime对象进行格式化
    if mode == 1:
        statement='(%s).' % (inidate)+'strftime("%Y-%m-%d %H:%M:%S")'
    elif mode ==2:
        statement='(%s).' % (inidate)+'strftime("%Y%m%d%H%M%S")'
    return eval(statement)


def init_dict():
	# 初始化替换变量,改为读取配置文件ini
	pass
	"""
	var_dict = {'servnumber':args.servnumber,
				'subsid':'100'+args.servnumber,
				'acctid':'100'+args.servnumber,
				'custid':'100'+args.servnumber,
				'subsprodid':args.servnumber+'01',
				'statusdate':dt.strftime("%Y%m%d"),
				'region':args.cfg,
				'lifestatedate':dt.strftime("%Y%m%d"),
				'prolongstartdate':dt.strftime("%Y%m%d"),
				'changedate':dt.strftime("%Y%m%d")
				}
	return var_dict
	"""
def selfclean(table,wh=None):
	#清理表，条件待定
	pass


def cbrand(brand=args.brand):
	if brand.upper()=='SZX':
		#加载预付费专属配置ABM_BILL_DAY等等
		szx_dict = {'billtime':dt.strftime("%Y%m%d"),
					'billday':dt.strftime("%Y%m%d"),
					'nextbillday':lunar.lunar(dt).nextbillday,
					'billcycle':dt.strftime("%Y%m00")}
		# sql数据列
		jdata = readcfg(cfg='base_BrandSzx_0001.json')
		u = cfgparser(jdata)
		for tbdsql,DbDriver in u:
			print(f"DbDriver={DbDriver},tbdsql={tbdsql}")
			sql = replacer(tbdsql,**szx_dict)
			sql_list.append((sql,DbDriver))
	elif brand.upper()=='GT':
		pass
	else:
		print("May be wrong with cfgfiles.")


def cactive(active=args.active):
	# 调用sqlplus查询，或者直接给定状态
	if active is True:
		#加载激活专属配置
		act_dict = {'active':1}
		# sql数据列
		jdata = readcfg(cfg='active_BrandSzx_0001.json')
		u = cfgparser(jdata)
		for tbdsql,DbDriver in u:
			print(f"DbDriver={DbDriver},tbdsql={tbdsql}")
			sql = replacer(tbdsql,**act_dict)
			sql_list.append((sql,DbDriver))
	elif active is False:
		pass
	else:
		print("May be wrong with cfgfiles.")


def croute(route=args.route):
	# 调用sqlplus查询，或者直接给定状态
	if route is True:
		#加载路由专属配置
		r_dict = {'nodeid':2522}
		# sql数据列
		jdata = readcfg(cfg='route_BrandSzx_0001.json')
		u = cfgparser(jdata)
		for tbdsql,DbDriver in u:
			print(f"DbDriver={DbDriver},tbdsql={tbdsql}")
			sql = replacer(tbdsql,**r_dict)
			sql_list.append((sql,DbDriver))
	elif route is False:
		pass
	else:
		print("May be wrong with cfgfiles.")

def readcfg(cfg=args.cfg):
	#判断是否列表
	
	#读取单个配置
	cfg = os.path.join(busidir,args.cfg)
	with open(cfg,'r',encoding='utf-8') as f:
		jdata=json.load(f)
	#删除注释
	del jdata['note']
	return jdata


def cfgparser(jdata):
	"""
	加载业务配置
	:param jdata:
	:return:
	"""
	for k in jdata.keys():
		DbDriver,Table,DML,BusiUniq = k.split(".")
		sql = replacer(jdata[k],**init_dict())
		# print(sql,DbDriver)
		yield sql,DbDriver


def replacer(tbdsql,**var_dict):
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

def generator(sql,DbDriver='oracle'):
	"""
	DbDriver,tbdsql in cfgparser(jdata
	:param sql:
	:param DbDriver:
	:return:
	"""
	with open(os.path.join(sqlfdir,'%s_%s.sql' % (DbDriver,args.servnumber)),'a',encoding='utf-8') as f:
		f.write(sql)
		f.write("\n")
	print(f"记录追加:{DbDriver}_{args.servnumber}.sql")

if __name__ == '__main__':
	pass