# -*- coding: utf-8 -*-
# @Time     : 2020/3/21 23:16
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : d4.py
# @Software : Select类
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(30)
# 访问
driver.get("http://baidu.com")
# 找百度页面的设置
driver.find_element_by_xpath("//a[@name = 'tj_settingicon' and contains(@href,'baidu')]").click()
# 找到设置下拉里面的高级搜索,ctrl+shift+c
driver.find_element_by_xpath("//a[text()='高级搜索']").click()
# 找到全部时间
e = driver.find_element_by_xpath('//*[@id="adv-setting-4"]/select')
print(e)
# 通过Select类里面的方法，选择文档格式
sele = Select(e)
# 找到他所有的下拉选择点击事件（全部时间，最近一天，最近一周，最近一月，最近一年）
print(sele.options)
# 找到稳当格式option为“微软Word(.doc)”点击一下
w = driver.find_element_by_xpath('//*[@id="adv-setting-5"]/select')
Select(w).select_by_value('doc')


