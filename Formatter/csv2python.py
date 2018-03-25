"""
    python2csv
"""
# import os
import csv
filepath='python2csv.csv'
with open(filepath,mode='r',encoding='utf-8', newline='') as csvf:
    #读取csv文件转换为list
    csvr= csv.reader(csvf)
    print('-----------',type(csvr))
    #读取I/O数据，必须在with之内
    python_list = []
    for line in csvr:
        python_list.append(line)
#分行展示
# for i in python_list:
#     print(i)
#数据保存结果展示
print(python_list)
