"""
Description:
	return a merged string by inputing a number and a string.
eg. merge(3,'%s'),return '%s,%s,%s'

Where could be used for?
	When you designed a sql script like below.
	sql='INSERT INTO TABLE1 ( COLUMNS ) \
	VALUES ( VALS )'
	COLUMNS = '%s,%s,%s'
	VALS = '%s,%s,%s'
	sql % (a,b,c,d,e,f)

"""
#datapreset
cols = ['version','begindate','enddate','executor']
vals = ['IT100','20190219','20190319','hy']


#method1
def fmt(num,s):
	it = ',%s' % (s)
	return  '%s' % (s) + (num - 1) * it
COLUMNS = fmt(len(cols),'%s')
VALUES = fmt(len(vals),'%s')

def fmv(cols,s=''):
	while len(cols)>1:
		s = s + cols.pop() + ','
	return s + cols.pop()

sql=f"INSERT INTO TABLE1 ( {COLUMNS} ) VALUES ( {VALUES} )" % (fmv(cols+vals))


#method2
from functools import reduce

def merge(iterstr):
	return reduce(lambda x,y:x + ',' + y,iterstr)
# 拼接列
COLUMNS = merge(cols)
# 拼接值
VALUES = merge(vals)
sql="INSERT INTO TABLE1 ( {COLUMNS} ) VALUES ( {VALUES} )"
sql.format(COLUMNS=COLUMNS,VALUES=VALUES)

#method3

COLUMNS = ",".join(cols)
VALUES = ",".join(vals)
sql="INSERT INTO TABLE1 ( {COLUMNS} ) VALUES ( {VALUES} )"
sql.format(COLUMNS=COLUMNS,VALUES=VALUES)