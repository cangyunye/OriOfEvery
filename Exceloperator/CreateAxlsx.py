# _*_ coding:utf-8 _*_
#用xlrd读取，用openpyxl写入。xlwt耗时大概为openpyxl的42.3%，效率明显较高。
#----------------------------------------------------------------------------
import xlrd
import openpyxl
#import matplotlib
#----------------------------------------------------------------------------



def log():
    #写日志
    pass

def createxlsx(wbname):
    #创建表文件
    wb = openpyxl.Workbook()
    wb.save(filename=wbname)

def savetoexcel(data,fields,sheetname,wbname):
    # 写入excel文件中 data 数据，date是list数据类型， fields 表头
    #读取表文件，并保存
    wb = openpyxl.load_workbook(filename=wbname)

    sheet = wb.active #获取当前active的Worksheet
    sheet.title = sheetname #定义active的标签名

    field = 1 #定义输入坐标
    for field in range(1,len(fields)+1): #写入表头
        to_insert=sheet.cell(row=1,column=field,value=str(fields[field-1]))
    row1 = 1
    col1 = 0
    div = divmod(len(data),len(fields))
    print('div:',div)
    if div[1] != 0:
        print('数据输入错误，含不完整{}列数据，要求每组含{}列数据'.format(div[1],div[0]))
        # exit 0
    for row1 in range(2,div[0]+1):#从表头下写入数据
        print(range(2,div[0]+1))
        print('row1',row1)
        for col1 in range(1,len(fields)*(row1-1)+1):
            to_insert=sheet.cell(row=row1,column=col1,value=str(data[col1-1]))
            print('col1',col1)
    wb.save(filename=wbname)

def readexcel(wbname,sheetname):
    #打开表
    wb = xlrd.open_workbook(filename=wbname)
    print ("表单数量:", wb.nsheets)
    print ("表单名称:", wb.sheet_names())
    # 获取第1个表单
    #sh = wb.sheet_by_index(0)
    sh = wb.sheet_by_name(sheet_name=sheetname)
    print (u"表单 %s 共 %d 行 %d 列" % (sh.name, sh.nrows, sh.ncols))
    print ("第二行第三列:", sh.cell_value(1, 2))
    # 遍历所有表单
    for s in wb.sheets():
        for r in range(s.nrows):
            # 输出指定行
            print (s.row(r))


def main():
    data_file = './Hideyourheart.xlsx' #当前目录下表文件
    sheetname = 'Snow' #标签
    fields = ['Version','Task','Executor','ExpFinTime','State']
    data =  ['LG6022','DtsCountData','Hei','20180504','Processing',
    'LG6122','PythonTeaching','Ei','20180509','Design']
    stored_file = data_file #处理后保存文件
    createxlsx(data_file)
    savetoexcel(data,fields,sheetname,data_file)
if __name__ == '__main__':
    main()
