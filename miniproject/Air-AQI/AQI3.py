"""
    AQI网页爬取
    BeautifulSoup
    [parser]
    BeautifulSoup(markup, "html.parser")
    BeautifulSoup(markup, "lxml")
    BeautifulSoup(markup, "lxml-xml")only supported XML parser
    BeautifulSoup(markup, "xml")only  supported XML parser
    BeautifulSoup(markup, "html5lib")  HTML5 Very slow
    use lxml for speed
    [function]
    soup.find_all('title', limit=1)查询所有tag为title的记录不超过1条
    soup.find_all("a", string="Elsie")查询TAG为a的，值为Elsie的记录
    soup.find_all(string="Elsie")仅查询值为Elsie的记录
    soup.find_all("a", class_="sister")class由于是关键词，所以带下划线
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
    soup.find_all(attrs={"data-foo": "value"})
    # [<div data-foo="value">foo!</div>]
    soup.find_all(href=re.compile("elsie"))
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
    soup.find_all(id='link2')
    # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
    soup.find('title')查询一条tag为title的记录
    soup.select("p.strikeout.body")
    # [<p class="body strikeout"></p>]
    soup.get_text(strip=True)提取标签中的值,并去除空格
    soup.text()提取标签中的值
"""
import requests
from bs4 import BeautifulSoup
import csv
def get_all_cities():
    """
        获取所有城市列表
    """
    city_name = []
    url = 'http://pm25.in/'
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text,'lxml')
    #由于网页中查询的bottom能查到2组结果，选择第2组
    city_div_list = soup.find_all('div',{'class':'bottom'})[1]
    #寻找a节点
    city_link_list = city_div_list.find_all('a')
    for city in city_link_list:
        city_cn = city.get_text(strip=True)
        #从soup型列表中，提取href字段的值，并去掉"/"
        city_py = city['href'][1:]
        city_name.append((city_cn,city_py))
    # print(city_name)
    return city_name
def get_city_aqi(city_pinyin):
    """
        获取城市的AQI
    """
    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url, timeout=30)
    #通过BeautifulSoup调用lxml解析器解析网页
    soup = BeautifulSoup(r.text,'lxml')
    # print('{}\n----------------\n{}\n--------------------'.format(soup.title,soup.head))
    #查找div结点下，class为span1的所有结果，组合成“列表”
    div_list = soup.find_all('div',{'class':'span1'})
    # div_list = soup.find_all('div',class_="span1")
    # print('div_list:\n',div_list)
    city_aqi = []
    for i in range(8):
        #此处不能用find_all,find_all查出来的是列表，不能使用后续text指令
        caption = div_list[i].find('div',{"class": "caption"}).get_text(strip=True)
        value = div_list[i].find('div',{'class': 'value'}).get_text(strip=True)
        # print('{},{}'.format(caption,value))
        #append只适合添加1个值，故需要将caption和value合并为一个值追加
        # city_aqi.append((caption,value))
        city_aqi.append(value)
    return city_aqi
def to_csv():
    with open('AQI_v3.csv', mode='w',encoding='utf-8',newline='') as csvf:
        city_name = get_all_cities()
        header = ['City', 'AQI', 'PM2.5/1h', 'PM10/h', 'CO/1h', 'NO2/1h', 'O3/1h', 'O3/8h', 'SO2/1h']
        csvv = csv.writer(csvf)
        csvv.writerow(header)
        for i, city in enumerate(city_name):
            if (i + 1) % 10 == 0:
                print('已处理{}条记录。(共{}条记录)'.format(i + 1, len(city_name)))
            row =[city[0]] + get_city_aqi(city[1])
            csvv.writerow(row)


def out_print():
    # city_pinyin = input('请输入查询城市(如shanghai):')
    city = get_all_cities()
    for city_zz in city:
        city_aqi = get_city_aqi(city_zz[1])
        print('{}的AQI为\n'.format(city_zz[0]))
        for line in city_aqi:
            print (line)
def main():
    # out_print()
    to_csv()


if __name__ == '__main__':
    main()
