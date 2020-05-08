from string import Template
t_varchar=Template(" '''||$COL||''' ")
t_date=Template(" 'to_date('''||$COL||''',''yyyy-mm-dd HH:MM:SS''') ")
t_timestamp=Template(" '''||$COL||''' ")
t_number=Template(" ||$COL|| ")

INS = Template(
    "SELECT 'INSERT INTO $TABLENAME ($COLUMNS) VALUES($VALUES);' FROM $TABLENAME $WHERE;")

def setvals(coltype,colvals):
    if coltype.upper().startswith('VARCHAR'):
        colvals.append(t_varchar.substitute(COL=col))
    elif coltype =='date':
        colvals.append(t_date.substitute(COL=col))
    elif coltype == 'timestamp':
        colvals.append(t_timestamp.substitute(COL=col))
    elif coltype == 'number':
        colvals.append(t_number.substitute(COL=col))
    else:
        colvals.append(t_varchar.substitute(COL=col))

zeta = {
    'table_list':['table_name'],
    'table_name': {'text': 'varchar',
                   'changedate': 'date',
                   'efftime': 'timestamp',
                   'num': 'number'},
    'table_name_wh':'num=5',

}
# 获取表ITERATOR
TABLELIST = zeta['table_list']

# 获取单表名称
for TABLE in TABLELIST:
    # TABLE=TABLELIST[0]
    colvals=[]
    # 获取字段ITERATOR
    columns=zeta[TABLE].keys()
    for col in columns:
        # 单字段
        # col=columns[0]
        coltype=zeta[TABLE][col]
        setvals(coltype,colvals)
    # 组装
    INS_TABLENAME=TABLE
    INS_COLUMNS=','.join(columns)
    INS_VALUES='||','||'.join(colvals)
    INS_CONDITIONS=zeta[f'{TABLE}_wh']
    s = INS.substitute(TABLENAME=INS_TABLENAME, COLUMNS=INS_COLUMNS, 
    VALUES=INS_VALUES,WHERE=INS_CONDITIONS)
    print(s)

