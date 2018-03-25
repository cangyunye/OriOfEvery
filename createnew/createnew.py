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
def get_xinwen():
    """
        新闻信息
    """
    url = 'http://www.3dmgame.com/news/'
def get_zatan():
    """
        杂谈信息
    """

    zatan_info = []
    url = 'http://www.3dmgame.com/zt/'
    r = requests.get(url, timeout=30)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text,'lxml')
    #由于网页中查询的bottom能查到2组结果，选择第2组
    zatan_div_list = soup.find_all('div',{'class':'QZlisttxt'})[0]
    zatan_info_list = zatan_div_list.find_all('a')
    zatan_link_list = []
    for list_index,link_value in enumerate(zatan_info_list):
        if list_index % 2 == 1 :
            zatan_link_list.append((list_index,link_value))
        else :
            continue
    # # zatan_link_list = zatan_div_list.find_all('a')
    print('-----------------\n',zatan_link_list[3])
    # for zatan in zatan_link_list:
    #     zatan_title = zatan.get_text(strip=True)
    #     #从soup型列表中，提取href字段的值，并去掉"/"
    #     zatan_link = zatan['href'][1:]
    #     zatan_info.append((zatan_title,zatan_link))
    # print(zatan_info)
    # return city_name

def to_csv():
    pass


def out_print():
    pass
def main():
    # out_print()
    # to_csv()
    # print(get_city_aqi('guangzhou'))
    get_zatan()

if __name__ == '__main__':
    main()
