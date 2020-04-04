# -*- coding: utf-8 -*-
# @Time     : 2020/3/21 18:31
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : d3.py
# @Software : 等待

# 隐式等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# 摄像头
driver.implicitly_wait(30)

driver.get("http://baidu.com")

# driver.find_element_by_xpath("//input[@id='kw']")
# driver.find_element_by_id("su")

# 显式等待
wait = WebDriverWait(driver,30)  # 初始化WebDriverWait对象
e = wait.until(EC.element_to_be_clickable((By.ID,"kw")))  # 调用until方法，使用条件element_to_be_clickable
print(e)  # 找到了，返回WebElement对象

