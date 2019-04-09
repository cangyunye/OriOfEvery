#!/usr/bin/python3
#-*- coding:utf-8 -*-
from datetime import datetime,timedelta
import calendar
"""
billday caculator
"""

class lunar():
	def __init__(self,now:datetime):
		self.dt = now

	def calcdeltadays(self,dt,deltamon=0):
		# How many days till next bill days showld we plus.
		lunaryear = lambda year:year % 4==0 and not year % 400 ==0
		bmon = lambda month : month in [1,3,5,7,8,10,12]
		mon=dt.month+deltamon
		# print(mon)
		if bmon(mon):
			deltadays = 31
		elif mon == 2 and lunaryear(dt.year):
			deltadays = 29
		elif mon == 2:
			deltadays = 28
		else:
			deltadays = 30
		if deltadays > calendar.mdays[mon + 1]:
			deltadays = calendar.mdays[mon + 1]
		# print(deltadays)
		if mon < dt.month:
			return -deltadays
		return deltadays

	@property
	def nextbillday(self):
		deltadays=self.calcdeltadays(self.dt,0)
		sBillNextDay = (self.dt + timedelta(days=deltadays)).strftime("%Y%m%d")
		return sBillNextDay

	@property
	def lastbillday(self):
		deltadays =self.calcdeltadays(self.dt,-2)
		sBilllastday = (self.dt + timedelta(days=deltadays)).strftime("%Y%m%d")
		return sBilllastday

def main():
	t=lunar(datetime.now())
	print(t.nextbillday,t.lastbillday)

if __name__ == '__main__':
	main()

