"""
    json2csv
    csv.writer(csvfile, dialect='excel', **fmtparams)
    --If csvfile is a file object, it should be opened with newline=''
    csv.riter.writerow(row/list)
    Write the row/list parameter to the writer’s file object, formatted according to the current dialect.
    csv.writer.writerows(rows)
    Write all the rows parameters (a list of row objects as described above) to the writer’s file object, formatted according to the current dialect.
    csv.DictWriter.writeheader()
    Write a row with the field names (as specified in the constructor).
    csv.reader()
"""
import json
import csv

def process_json_file(filepath):
    """
        解析JSON文件
    """
    jsonf = open(filepath, mode='r',encoding='utf-8')
    #读取JSON文件，赋值给city_list为列表形式
    city_list = json.load(jsonf)
    #原始读取操作,但是如果需要同时显示结果，则不能使用同一个实例
    f0 = open(filepath, mode='r',encoding='utf-8')
    city_test = f0.read()
    # print('------------------->',type(jsonf))
    # print('------------------->',type(city_list))
    print('------------------->',city_test)
    jsonf.close()
    return city_list
def main():
    # filepath = input('请输入JSON文件：\n')
    filepath = 'beijing_aqi.json'
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city:city['aqi'])
    #设定需转换为csv的读取列表
    csv_line = []
    #先加入字段头,即索引keys字段
    csv_line.append(city_list[0].keys())
    for city in city_list:
        csv_line.append(city.values())
    print('------------csv_line-----------\n',csv_line)
    print('------------type(csv_line)-----------\n',type(csv_line))
    csvf = open('python2csv.csv',mode='w',encoding='utf-8',newline='')
    #调用writer，并控制分隔符为“|”,默认为“,”
    csv_list = csv.writer(csvf,delimiter=',')
    print('------------type(csv_list)-----------\n',type(csv_list))
    print('------------csv_list-----------\n',csv_list)
    #将列表全部写入
    csv_list.writerows(csv_line)
    #单行写入
    # for line in csv_line:
    #     csv_list.writerow(line)
    csvf.close()
    with open('python2csv.csv',mode='r',encoding='utf-8',newline='') as fcsv:
        print(fcsv.read())




if __name__ == '__main__':
    main()
