# -*- coding: utf-8 -*-
# @Time     : 2020/3/23 16:47
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : index_page.py
# @Software : 

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from class9_ddt_basepage.pages.base import BasePage

class IndexPage(BasePage):

    bid_ele_locator = (By.XPATH, "//a[@class='btn btn-special']")

    def get_user(self):
        return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(
            (By.XPATH, "//img[@class='mr-5']/..")))

