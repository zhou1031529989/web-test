# -*- coding: utf-8 -*-
# @Time     : 2020/3/22 14:34
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : d2_file_not_input.py
# @Software :上传文件


import time
# 上传文件
# chrome
import win32gui
import win32con


from selenium import webdriver

# 安装 解决方法：https://stackoverflow.com/questions/3956178/cant-load-pywin32-library-win32gui
# First check that "pywin32" module is installed in your system or not. If not installed then install it first.
# /Lib/site-packages/pywin32_system32

driver = webdriver.Chrome()

driver.get('file:///C:/Users/zhouchao/PycharmProjects/python13-web/class1_html/doc/ningmeng.html')

e = driver.find_element_by_name('file').click()

# 一定要等待，WebDriverWait不能操作系统控件，所以用sleep,sleep长一点，不然文件传不进去
time.sleep(5)

# win32gui
dialog = win32gui.FindWindow("#32770","打开")                        # 一级窗口
print(dialog)
# 找到窗口
ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)  # 二级
print(ComboBoxEx32)
comboBox = win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None)    # 三级
print(comboBox)
edit = win32gui.FindWindowEx(comboBox,0,'Edit',None)                # 四级
print(edit)
button = win32gui.FindWindowEx(dialog,0,'Button','打开(&O)')         # 四级
print(button)
print('ok')
time.sleep(5)
# 操作
win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,r'd:\test.txt')   # 输入绝对地址，可封装成函数，只需要将文件路径作为参数传入

time.sleep(3)
# 发送文件路径
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)    # 点击打开按钮

time.sleep(4)
driver.quit()

