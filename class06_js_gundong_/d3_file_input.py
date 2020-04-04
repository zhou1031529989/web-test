# -*- coding: utf-8 -*-
# @Time     : 2020/3/22 15:13
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : d3_file_input.py
# @Software : 
import time
# 上传文件
# chrome

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('file:///C:/Users/zhouchao/PycharmProjects/python13-web/class1_html/doc/ningmeng.html')
# 找到上传文件的元素
driver.find_element_by_name('file').send_keys(r"d:\test.txt")
time.sleep(3)

driver.quit()

