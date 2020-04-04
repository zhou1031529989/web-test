# -*- coding: utf-8 -*-
# @Time     : 2020/3/23 21:34
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : login_locator.py
# @Software :
from selenium.webdriver.common.by import By


class LoginLocator:
    # toast提示定位器
    flash_msg_locator = (By.XPATH, "//div[@class='form-error-info']")
    # 描红提示定位器
    alert_locator = (By.XPATH, "//div[@class='layui-layer-content']")
    # 手机号码定位器
    phone_locator = (By.NAME, 'phone')
    # 密码定位器
    pwd_locator = (By.NAME, 'password')
