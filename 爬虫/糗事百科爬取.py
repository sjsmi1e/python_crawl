#! /usr/bin/env python
# !-*-coding:utf-8 -*-
# ! @Time     : 16:27
# ! @Author   :smile丶
# ! @File     :.py
import requests
import re
from fake_useragent import UserAgent
headers = {
    "user-agent" : UserAgent().chrome
}
url = "https://www.qiushibaike.com/hot/"
resp = requests.get(url,headers=headers)
resp.encoding="utf-8"
info = resp.text
infos=re.findall(r'<div class="content">\W+<span>\W+(.+)',info)
# 写入到文件
with open("段子.txt","a",encoding="utf-8") as f:
    index=1
    for i in infos:
        result=re.sub(r'<br/>',"\n",i)
        # print(result)
        f.write("第"+str(index)+"个段子：\n\n"+result+"\n\n\n")
        index+=1