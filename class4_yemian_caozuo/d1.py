# -*- coding: utf-8 -*-
# @Time     : 2020/3/21 17:45
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : d1.py
# @Software : 常用页面操作

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

# 刷新
driver.refresh()
# 全屏
driver.maximize_window()
# 调整大小,宽度，高度
# driver.set_window_size()

# 再打开一个网页
driver.get("http://douban.com")

# 后退到百度
driver.back()

# 前进到豆瓣
driver.forward()

# url
print(driver.current_url)

# 获取标题
print(driver.title)
# 关闭标签
driver.close()
# 截屏保存
# driver.save_screenshot()
# 关闭浏览器
driver.quit()




