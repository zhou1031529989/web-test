# -*- coding: utf-8 -*-
# @Time     : 2020/3/22 11:35
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : d5.py
# @Software : 操作键盘

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(30)
# 访问
driver.get("http://baidu.com")
driver.maximize_window()

# e = driver.find_element_by_id('kw')
# 向下
# e.send_keys('柠檬班',Keys.DOWN)

# 鼠标操作，先初始化一个对象
ac = ActionChains(driver)
# 先找到要悬浮的对象，如设置，再传进
e = WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//a[@name = 'tj_settingicon' and contains(@href,'baidu')]")))
# 悬浮到设置上,要释放perform才能执行，不然就只是将动作存在一个列表里
ac.move_to_element(e).perform()
# 点击高级搜索
driver.find_element_by_xpath("//a[text()='高级搜索']").click()




















