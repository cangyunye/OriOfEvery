# urlencode将字典将其序列化为GET请求参数
from urllib.parse import urlencode
params = {
    'name' : 'germey',
    'age' : 22
}

base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)

# parse_qs反序列化，将query部分，转换为字典类型
from urllib.parse import parse_qs
query = 'name=germey&age=22'
print(parse_qs(query))

# parse_qsl反序列化，将query部分，转换为列表类型
from urllib.parse import parse_qsl
query = 'name=germey&age=22'
print(parse_qsl(query))