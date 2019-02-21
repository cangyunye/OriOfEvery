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
def method1(cols,vals):
	COLUMNS = ",".join(cols) #可取消字符串对应的单引号
	VALUES = tuple(vals) #自带括号
	sql=f"INSERT INTO TABLE1  ({COLUMNS})  VALUES {VALUES}"


#method2
def method2(cols,vals):
	from functools import reduce
	# 拼接列
	COLUMNS = reduce(lambda x,y:x + ',' + y,cols)
	# 拼接值
	VALUES = reduce(lambda x,y:x + ',' + y,vals)
	sql = "INSERT INTO TABLE1 ( {COLUMNS} ) VALUES ( {VALUES} )".format(COLUMNS=COLUMNS, VALUES=VALUES)


#method3
def method3(cols,vals):
	COLUMNS = ",".join(cols)
	VALUES = ",".join(vals)
	sql="INSERT INTO TABLE1 ( {COLUMNS} ) VALUES ( {VALUES} )"
	sql.format(COLUMNS=COLUMNS,VALUES=VALUES)