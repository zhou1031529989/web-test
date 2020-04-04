# -*- coding: utf-8 -*-
# @Time     : 2020/3/21 11:27
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : d2.py
# @Software : 

from selenium import webdriver
from selenium import common

# class MyException(common.WebDriverException):
#     def __

# 如果Chromewebdriver没有放在python跟目录下，改webdriver路径即可
# driver = webdriver.Chrome(executable_path=r"D:\chromedriver.exe")

driver = webdriver.Chrome()  # 初始化一个对象
driver.get("http://www.baidu.com")
print(driver)  # 获取一个对象

# 元素定位
element = driver.find_element_by_id("kw")
print(element)  # 获取一个webelement对象
print(element.get_attribute("class"))  # 获取对象的某个属性


# 不具备唯一性都有element和elements两个方法
# 找到WebElement对象，找到第一个就返回
driver.find_element_by_name("wd")
# 如果不具备唯一性，则可以找到多个
# driver.find_elements_by_tag_name() # 返回一个列表[]，可通过列表取要找的元素
# 找超链接里面的文本，如新闻
driver.find_element_by_partial_link_text("新闻")
# 找超链接里面的文本，包含法，如闻
driver.find_element_by_partial_link_text("闻")
# 全文本
driver.find_element_by_link_text("新闻")
# class
driver.find_element_by_class_name('kk')

# css 综合，如元素tagname是input且id是kw且class是s_ipt
driver.find_element_by_css_selector("input#kw.s_ipt")
driver.find_element_by_css_selector("input[name='kw']")
