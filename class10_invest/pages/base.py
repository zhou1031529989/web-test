# -*- coding: utf-8 -*-
# @Time     : 2020/3/23 17:44
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : base.py
# @Software :

# from appium.webdriver import WebElement
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import logging

logging.basicConfig(filename='logs/test.log',level='DEBUG')
logger = logging.getLogger()


class BasePage:

    def __init__(self, driver:Chrome):
        self.driver = driver

    # 获取时间戳
    def getTime(self):
        tamp = int(time.time())
        return tamp

    # 接受定义的复杂
    # def get_visible_element(self, locator, time = 20) -> WebElement:
    def get_visible_element(self, locator, time = 20):
        times = self.getTime()
        filename = 'logs/ %s.png' % times
        try:
            return WebDriverWait(self.driver, time).until(
                ec.visibility_of_element_located(locator))
        except Exception as e:
            # log保存截图
            self.driver.get_screenshot_as_file(filename)
            # 控制台打印错误
            logger.error("no this element:{}",e)

    def get_clickable_element(self, locator, time=20):
        try:
            return WebDriverWait(self.driver, time).until(
                ec.element_to_be_clickable(locator))
        except Exception as e:
            self.driver.save_screenshot('logs/test.png')
            logger.error(e)

    def switch_window(self, time=30, name=None):
        if not name:
            current_handle = self.driver.current_window_handle
            WebDriverWait(self.driver,time).until(ec.new_window_is_opened(current_handle))
            handles = self.driver.window_handles
            return self.driver.switch_to.window(handles[-1])
        return self.driver.switch_to.window(name)















