"""
    requests模块
    方法
    requests.get('https://api.github.com/user', auth=('user', 'pass'))
    requests.post('http://httpbin.org/post', data = {'key':'value'})
    requests.put('http://httpbin.org/put', data = {'key':'value'})
    requests.delete('http://httpbin.org/delete')
    requests.head('http://httpbin.org/get')
    requests.options('http://httpbin.org/get')
    属性
    status_code:返回网页链接状态代码如404链接失效
    raise_for_status() :解释上面返回码
    encoding:返回编码
    text：根据encoding状态返回页面文本字符串形式
    content:Binary Response Content
    json():返回页面json形式
    headers:返回页面文件头as Python的dictionary
    url:返回网页地址
"""
import requests
def get_url():
    #获取网页
    r = requests.get('http://www.moe123.net/', params=None,timeout=0.001)
    #输出编码
    print('原始编码：',r.encoding)
    #改变编码，影响到text的获取
    r.encoding = 'utf-8'
    print('转换编码：',r.encoding)
    print('文件头headers组:\n',r.headers)
    return r
def url_text():
    r = get_url()
    confirm_value = input('---------------------------------------\nT打印网页文本，J输出Json格式，R输出socket socket,其他输出二进制内容，退出请按Q:\n')
    if confirm_value in ['q','Q']:
        exit
    elif confirm_value in ['T','t']:
        #text根据当前encoding状态输出
        utext=r.text
    elif confirm_value in ['J','j']:
        utext=r.json
    elif confirm_value in ['R','r']:
        r = requests.get('http://www.moe123.net', stream=True)
        utext=str(r.raw)+'\n'+str(r.raw.read(10))
    else:
        #输出了二进制内容
        utext=r.content
    print(utext)
def post_msg():
    payload = {'key1': 'exactly!', 'key2': 'sure'}#能使用dictionary
    payload2 = (('key1', 'value1'), ('key1', 'value2'))#能使用turples
    r = requests.post("http://httpbin.org/post", data=payload2)
    print(r.text)
def pass_param():
    #传递参数
    payload = {'key1': 'exactly!', 'key2': ['exactly', 'sure']}#能使用dictionary
    payload2 = (('key1', 'value1'), ('key1', 'value2'))#能使用turples
    payloadz = {'': ['exactly!', 'sure']}
    # list_key = ['exactly!','exactly'] #不能使用list
    r = requests.get('http://dict.cn/', params=payloadz)
    print(r.url)
def send_cookies():
    url = 'http://httpbin.org/cookies'
    cookies = dict(cookies_are='good_job')
    r = requests.get(url, cookies=cookies)
    print(r.text)

def main():
    # url_text()
    # pass_param()
    # post_msg()
    send_cookies()

if __name__ == '__main__':
    main()
