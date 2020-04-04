# -*- coding: utf-8 -*-
# @Time     : 2020/3/21 20:39
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : d1.py
# @Software : 
# 隐式等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# 摄像头
driver.implicitly_wait(30)

driver.get("http://baidu.com")

# 找到输入框
input_ele = driver.find_element_by_id("kw")
# 输入内容
input_ele.send_keys("柠檬班")
# 提交 找到提交按钮，点击
# input_ele.click()
driver.find_element_by_id("su").click()

# 解决访问Https时不受信任SSL证书问题
# options = webdriver.ChromeOptions()
# options.add_argument("service_args=[’–ignore-ssl-errors=true’, ‘–ssl-protocol=TLSv1’]") # Python2/3
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
# driver.maximize_window()


# 柠檬班定位 加等待
nm = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'lemon.ke.qq.com')]")))
# nm = driver.find_element_by_xpath('//a[contains(text(),"lemon.ke.qq.com")]')
nm.click()

# 查询 有几个Windows页面
print(driver.window_handles)
# 打印当前页面
print(driver.current_window_handle)

# 切换到第二个页面,打印所有的窗口，要切换的就是最后的那一个
driver.switch_to.window(driver.window_handles[-1])
# 等待
# EC.new_window_is_opened()

# 华华 等待
huahua = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//h4[text()='华华老师']")))
# huahua = driver.find_element_by_xpath("//h4[text()='华华老师']")
print(huahua.tag_name)
print(huahua.text)



# alert 和 iframe











