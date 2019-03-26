#!/usr/bin/env python
# encoding: utf-8
'''
@author: cangyunye
@Email: cangyunye@gmail.com
@wechat:whyNless
@file: readmanual.py
@time: 2019/3/25/025 21:20
@desc: 从文件中读取BEGIN和END中间的部分并分组
'''
import re
from pprint import pprint
from collections import defaultdict
"""
#示例文件
#CMD_REGION_BEGIN
1|hunan|orange
2|guangdong|apple
3|beijing|pear
#CMD_REGION_END

#CMD_SHELL_BEGIN
WY|loufangzhongjie
PC|aozhoudaigou
#CMD_SHELL_END
"""

def rdls(txt):
	# 设定状态，用于判断begin以后的添加	，只能判断一组BEGIN-END
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
			elif status == 1 and not re.search(p_end,line)::
				print('3')
				DIR[name].append(line)
				print(re.split(r'\|',line))
			elif re.search(p_end,line):
				print('4')
				status = 0
		pprint(DIR)


def spat(txt):
	# 可以判断多组BEGIN-END
	dic = defaultdict(list)
	p_b = re.compile(r'#CMD_(\w+)_BEGIN')
	p_e = re.compile(r'#CMD_(\w+)_END')
	# 0表示追踪BEGIN，1表示追踪到BEGIN之后的已定位状态
	status = 0 
	with open(txt,'r',coding='utf-8') as f:
		line = True
		while line:
			line = f.readline()
			search_b = re.search(p_b,line)
			if status ==0 and not search_b:
				# 如果是追踪状态，且本行不是BEGIN
				continue
			elif search_b:
				# 找到BEGIN
				# 分组名称
				name = line.split('_')[1]
				# name = search_b.group(1)
				dic[name] = []
				# 进入已定位状态
				status = 1
			elif status == 1 and not re.search(p_e,line):
				# 如果是已定位状态，且非END行
			elif re.search(p_e,line):
				# 如果是END行，重置状态为追踪
				status = 0
			else:
				print("Exception:",line)
	pprint(dic)






def main():
	txt = 'manual.txt'
	rdls(txt)


if __name__ == '__main__':
	main()