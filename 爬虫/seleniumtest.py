#! /usr/bin/env python
# !-*-coding:utf-8 -*-
# !@Time     : 12:27
# !@Author   :smile丶
# !@File     :.py

# 导入 webdriver
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--headless')
# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.Chrome(chrome_options=options)

# 如果没有在环境变量指定PhantomJS位置
# driver = webdriver.PhantomJS(executable_path="./phantomjs"))

# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
data=driver.get("http://www.baidu.com/")
# # 打印数据内容
# print(data)
# 打印网页渲染后的源代码
print(driver.page_source)
# 关闭浏览器
driver.quit()