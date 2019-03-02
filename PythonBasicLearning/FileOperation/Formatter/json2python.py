"""
    Json2python字典格式转换工具
    json文件中字段为双引号
    dumps(内容，文件)：将Python数据类型转换为JSON格式字符串，实际限制为只能使用字符串
    loads()：将JSON格式字符串转换为Python数据类型字符串
    dump()：与dumps()功能一致，输出到文件
    load()：与loads()功能一致，从文件读入
"""
import json

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
    #读取AQI前5
    city_list.sort(key=lambda city:city['aqi'])
    top5_list = city_list[:5]
    print(top5_list)
    #写文件
    filetop5 = open('top5_aqi.json', mode='w',encoding='utf-8')
    #不使用二进制，区别是，生成文件内容
    json.dump(top5_list,filetop5,ensure_ascii=False)
    filetop5.close()



if __name__ == '__main__':
    main()
