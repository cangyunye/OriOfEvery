#!/usr/bin/env python
# -*-coding:utf-8-*-'

import sys, os
from urllib.request import urlretrieve


def urlcallback(a, b, c):
	"""
		call back function
		a,已下载的数据块
		b,数据块的大小
		c,远程文件的大小
	"""
	print("callback")
	prec = 100.0 * a * b / c
	if 100 < prec:
		prec = 100
	print("%.2f%%" % (prec,))


def main(file):
	"""
		main
	"""
	print("start...")
	urlretrieve(file , urlcallback)
	print("end...")



if __name__ == "__main__":
	main(file="https://media.readthedocs.org/htmlzip/python3-cookbook/latest/python3-cookbook.zip")