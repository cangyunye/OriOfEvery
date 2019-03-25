#!/usr/bin/env python
# encoding: utf-8
'''
@author: cangyunye
@Email: cangyunye@gmail.com
@wechat:whyNless
@file: readmanual.py
@time: 2019/3/25/025 21:20
@desc: 从文件中读取BEGIN和END中间的部分
'''
import re
from pprint import pprint

"""
#示例文件
#DIR-Begin
1|hunan|orange
2|guangdong|apple
3|beijing|pear
#DIR-End

#SHELL-Begin
WY|loufangzhongjie
PC|aozhoudaigou
#SHELL-End
"""

def rdl(txt):
	with open(txt,'r') as f:
		while True:
			line = f.readline()
			print(line)
			if not line:
				break

def rdls(txt):
	# 设定状态，用于判断begin以后的添加
	status = 0
	DIR = {}
	p_begin = re.compile(r'Begin')
	p_end = re.compile(r'End')
	with open(txt,'r') as f:
		content = f.readlines()
		for line in content :
			print('checking % s' % line)
			if not re.search(p_begin,line) and status == 0:
				print('1')
				continue
			elif re.search(p_begin,line):
				print('2')
				status = 1
				name = line.split('-')[0][1:]
				DIR[name]=[]
			elif status == 1:
				print('3')
				DIR[name].append(line)
			elif re.search(p_end,line):
				print('4')
				status = 0
		pprint(DIR)





def main():
	txt = 'manual.txt'
	rdls(txt)


if __name__ == '__main__':
	main()