from string import Template

# 视图模板
view = Template("CREATE OR REPLACE  VIEW $viewname  AS $query;")

# 表数据
# {owner.tablename:[columns]}
#
data = [('gzib','ib_rentfee_log','oid'),
('gzib','ib_rentfee_log','fee'),
('gzib','ib_rentfee_log','cycle'),]

# for owner,tablename,column in data:
#     print(f'{owner}.{tablename}:{column}')
d = {}
columns  = [i[2].upper() for i in data]
owner=data[0][0].upper()
tablename=data[0][1].upper()
viewname=f'{owner}.{tablename}'
d.update({viewname:columns})
print(d)
ind = columns.index('OID')
columns[ind]='BSID'
colpart = ','.join(columns)
query=f'select {colpart} from {viewname}'
print(view.substitute(viewname=viewname,query=query))

