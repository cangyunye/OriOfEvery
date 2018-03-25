import datetime
print('输出当前时间now():\n',datetime.datetime.now())#输出当前时间
print('输出世界统一时间时间utnow():\n',datetime.datetime.utcnow())#输出世界统一时间时间
print('输出当前日期now().date():\n',datetime.datetime.now().date())#输出当前日期
print('解析时间字符串到时间格式strptime():\n',datetime.datetime.strptime('2017/12/16 13:00:00','%Y/%m/%d %H:%M:%S'))#解析时间字符串
reprtime=repr(datetime.datetime.now())#时间格式转换为字符串型表达式
print('时间格式转换为字符串型表达式repr(now()):\n',type(reprtime))#无法直接代替变量
daynow = str(datetime.datetime.now().date())#时间格式转换为字符串
print('str转换+isocalendar():\n',datetime.datetime.strptime(daynow,'%Y-%m-%d').isocalendar())#获取年、周、日
daynow2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #datetime时间格式转换为字符串
print('strftime():\n',daynow2)
print('strftime转换+isocalendar():\n',datetime.datetime.strptime(daynow2,'%Y-%m-%d %H:%M:%S').isocalendar())#获取年、周、日
print('timetuple():\n',datetime.datetime.now().timetuple())#返回当前时间标签组
print('timetuple().tm_year:\n',datetime.datetime.now().timetuple().tm_year)#返回当前时间标签组
print('timedelta(days=1):\n',datetime.datetime.now() + datetime.timedelta(days=1))
print('timedelta(hours=1):\n',datetime.datetime.now() + datetime.timedelta(hours=1))
print('timedelta(minutes=155):\n',datetime.datetime.now() + datetime.timedelta(minutes=15))
print('timedelta(seconds=60):\n',datetime.datetime.now() + datetime.timedelta(seconds=60))
print('timedelta(weeks=1):\n',datetime.datetime.now() + datetime.timedelta(weeks=1))
#class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

"""
%d	Day of the month as a zero-padded decimal number.	01, 02, …, 31
%m	Month as a zero-padded decimal number.	01, 02, …, 12
%y	Year without century as a zero-padded decimal number.	00, 01, …, 99
%Y	Year with century as a decimal number.	0001, 0002, …, 2013, 2014, …, 9998, 9999
%H	Hour (24-hour clock) as a zero-padded decimal number.	00, 01, …, 23
%I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, …, 12
%p	Locale’s equivalent of either AM or PM.
AM, PM (en_US);
am, pm (de_DE)
%M	Minute as a zero-padded decimal number.	00, 01, …, 59
%S	Second as a zero-padded decimal number.	00, 01, …, 59
%z	UTC offset in the form ±HHMM[SS] (empty string if the object is naive).	(empty), +0000, -0400, +1030
%Z	Time zone name (empty string if the object is naive).	(empty), UTC, EST, CST
%j	Day of the year as a zero-padded decimal number.	001, 002, …, 366
%U	Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.	00, 01, …, 53
%W	Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.	00, 01, …, 53
"""
