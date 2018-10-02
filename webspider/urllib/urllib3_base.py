from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import urllib3
http = urllib3.PoolManager()
website='https://www.python.org/'

r = http.request('GET',website)
print(r.data)