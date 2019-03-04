#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import textwrap
import os
import json


__description__ = textwrap.dedent('''\
			About the project you need to know
		 ---------------------------------------
			Designed for generate user data.
			Supplying which is absent from we need.
			Expansibility by configs.
			''')

__version__ = "GU.0.0.1"
parser = argparse.ArgumentParser(description=__description__, formatter_class=argparse.RawDescriptionHelpFormatter,
								 prog='UserDataGenerator', epilog="Nowhere to be seen.")
#argument:servnumber,region,cfgfile
parser.add_argument('servnumber', metavar='serv', type=int,
					help='The 11 integer for the servnumber.')

parser.add_argument('region', metavar='rg', type=str,
					help='The region of servnumber.')

parser.add_argument('-c','--config', action='append',dest='cfg',nargs='+',
					help='The region of servnumber.')

#addtional info
parser.add_argument('-b','--brand', required=False, type=str,choices=['szx','SZX','gt','GT'],
					help='Brand like szx as BrandSzx or gt as BrandGotone.')
parser.add_argument('-e','--env', required=False, type=str,choices=['crm','CRM','test','TEST'],
					help='Environment like crm as or test.')

#add_help
parser.add_argument('-v','--version', help='version:%s' % (__version__))


args = parser.parse_args()

#init
__brand__=["BrandSzx","BrandGotone"]
#root path for os.path.join
rootdir=os.getcwd()
busidir=os.path.join(rootdir,'business')

#global variable for append sql when cbrand,cactive,croute
global datalist = []

def cbrand(brand=args.brand):
	if brand.upper()=='SZX':
		#加载预付费专属配置ABM_BILL_DAY等等
		pass
	elif brand.upper()=='GT':
		pass
	pass

def selfclean(table,wh=None):
	#清理表，条件待定
	pass

def cactive():
	# 调用sqlplus查询，或者直接给定状态
	pass

def croute():
	# 调用sqlplus查询，或者直接给定状态
	pass


def readcfg(cfg=args.cfg):
	#判断是否列表

	#读取单个配置
	with open(cfg,'r',encoding='utf-8') as f:
		jdata=json.load(f)
	#删除注释
	del jdata['note']
	return jdata




def cfgparser(jdata):
	#解析key
	for k in jdata.keys() :
		DbDriver,Table,DML,BusiUniq=k.split(".")
		data=replacer(jdata[k])
		generator(data)#生成sql文件
		#loadtobase(DbDriver,data)#加载到数据库
	pass

def replacer(tbd):
	#sql模板语句处理器,用于替换sql中的变量
	pass

def generator(data):
	with open(os.path.join(busidir,'%i_%s.sql' % (args.serv,args.cfg)),'a',encoding='utf-8') as f:
		f.write(data)

if __name__ == '__main__':
	pass