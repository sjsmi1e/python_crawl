#! /usr/bin/env python
# !-*-coding:utf-8 -*-
# !@Time     : 17:18
# !@Author   :smile丶
# !@File     :.py
import os
import uuid
from time import sleep
import requests
from selenium import webdriver
from lxml import etree
from fake_useragent import UserAgent
from queue import Queue
from threading import Thread
#无头打开
options = webdriver.ChromeOptions()
options.add_argument("--headless")
chrome = webdriver.Chrome(chrome_options=options)
#
headers = {
    "user-agent" : UserAgent().chrome
}

#请求
def get_html(url):
    chrome.get(url)
    js = 'document.documentElement.scrollTop=100000'
    chrome.execute_script(js)
    sleep(10)
    html = chrome.page_source
    # 解析
    e = etree.HTML(html)
    info = etree.tostring(e)
    info.decode("utf-8")
    return e


def get_url(keyword,pages):
    urls=Queue()
    for i in range(0,pages):
        res = "https://search.jd.com/Search?keyword="+keyword+"&enc=utf-8&page="+str(2*(i+1)-1)+"&wq="+keyword
        i += 1
        urls.put(res)
    return urls

# 保存
def save_imgs(imgs,keyword):
    for i in imgs:
        if i != "done":
            url="http:"+i
            resp = requests.get(url, headers=headers)
            result = resp.content
            with open("./imgs/"+keyword+"/"+str(uuid.uuid1())+".jpg","wb") as f:
                f.write(result)
                f.close()
# 多线程
class  begin_go( Thread ):
    def __init__(self,urls,keyword):
        Thread.__init__(self)
        self.urls=urls
        self.keyword=keyword
    def run(self):
        while self.urls.empty() == False:
            e = get_html(urls.get())
            imgs1 = e.xpath('//li[@class="gl-item"]/div/div[@class="p-img"]/a/img/@src')
            imgs2 = e.xpath('//li[@class="gl-item"]/div/div[@class="p-img"]/a/img/@data-lazy-img')
            imgs = imgs1 + imgs2
            save_imgs(imgs,keyword)
            print("爬取完成")



if __name__ == '__main__':
    keyword = input("请输入搜索的商品名：")
    if os.path.exists("./imgs/"+keyword):
        pass
    else:
        os.mkdir("./imgs/"+keyword)
    urls = get_url(keyword, 10)
    crawl_list = []
    for i in range(0, 10):
        crawl1 = begin_go(urls,keyword)
        crawl_list.append(crawl1)
        crawl1.start()

    for crawl in crawl_list:
        crawl.join()

    print("按爬取完成，进入imgs查看结果，按CTRL+C退出吧。。。")


