# -*- coding: utf-8 -*-
# @Time     : 2020/3/21 22:56
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : d3.py
# @Software : alert

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(30)
#访问
driver.get("file:///C:/Users/zhouchao/PycharmProjects/python13-web/class1_html/hello.html")

# 切换到alert
alert = driver.switch_to.alert
print(alert.text)
# 如果要使用原来的页面
alert.dismiss()
# 等待
# EC.alert_is_present

print('ok')
