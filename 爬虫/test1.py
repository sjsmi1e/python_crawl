import requests
import re
from fake_useragent import UserAgent

#请求头
headers = {
    "User-Agent": UserAgent().chrome
}

url="https://www.baidu.com/"
resp = requests.get(url,headers=headers)
resp.encoding="utf-8"
print(resp.text)

