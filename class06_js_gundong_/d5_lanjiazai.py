# -*- coding: utf-8 -*-
# @Time     : 2020/3/22 17:17
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : d5_lanjiazai.py
# @Software : 拖动到可见才加载

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://douban.com')
# 找到元素
# e = driver.find_element_by_xpath("//span[@id='icp']")
# # 然后将元素放入可见的区域里
# e.location_once_scrolled_into_view

# 通过js来直接将元素放入可见区域
# 找到元素的坐标然后拖动window.scrollTo(100,1000)
# js拖动到最底部的操作window.scrollTo(0,document.body.scrollHeight)
js_code = "window.scrollTo(0,document.body.scrollHeight)"
# 执行JavaScript
driver.execute_script(js_code)
time.sleep(5)

driver.quit()


