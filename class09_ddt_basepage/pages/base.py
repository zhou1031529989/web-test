# -*- coding: utf-8 -*-
# @Time     : 2020/3/23 17:44
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : base.py
# @Software :

from appium.webdriver import WebElement
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import logging

logging.basicConfig(filename='test.log',level='DEBUG')
logger = logging.getLogger()

class BasePage:

    def __init__(self, driver:Chrome):
        self.driver = driver

    # 接受定义的复杂
    def get_visible_element(self, locator, time=20) -> WebElement:
        try:
            return WebDriverWait(self.driver, time).until(
                ec.visibility_of_element_located(locator))
        except Exception as e:
            # log保存截图
            self.driver.save_screenshot('test.jpg')
            # 控制台打印错误
            logger.error("no this element:{}",e)
