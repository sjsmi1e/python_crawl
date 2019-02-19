#! /usr/bin/env python
# !-*-coding:utf-8 -*-
# !@Time     : 12:03
# !@Author   :smile丶
# !@File     :.py

from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
result = result.decode("utf-8")
# print(result)
info = html.xpath('//li//text()')
print(info)

