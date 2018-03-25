"""
    AQI网页爬取
"""
import requests

def get_html_text(url):
    """
        获取url文本
    """
    r = requests.get(url, timeout=30)
    print('访问状态：',r.status_code)
    return r.text

def main():
    city_pinyin = input('请输入查询城市(如shanghai):')
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_text(url)
    print(url_text)
    #定位AQI_VALUE在网页中的位置，在浏览器中，通过Ctrl+U访问源码
    aqi_div = """    <div class="span12 data">
        <div class="span1">
          <div class="value">
            """
    #利用find返回aqi_div所查询字符串的索引号
    begin_index = url_text.find(aqi_div) + len(aqi_div)
    end_index = begin_index + 2
    print('begin_index=%d,end_index=%d' % (begin_index,end_index))
    print('{}的AQI值为{}'.format(city_pinyin,url_text[begin_index:end_index]))

    print (url_text.index)
if __name__ == '__main__':
    main()
