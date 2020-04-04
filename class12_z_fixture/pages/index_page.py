# -*- coding: utf-8 -*-
# @Time     : 2020/3/23 16:47
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : index_page.py
# @Software : 


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from class12_z_fixture.pages.base import BasePage


class IndexPage(BasePage):
    # 中间有空格的值，XPATH元素定位，python找不到
    # bid_ele_locator = (By.XPATH, "//a[@class='btn btn-special']")
    bid_ele_locator = (By.XPATH, "//a[contains(@class,'btn-special')]")

    def get_user(self):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(
            (By.XPATH, "//img[@class='mr-5']/..")))

    def bid(self):
        # 先元素定位
        return self.get_bid_button().click()

    def get_bid_button(self):
        return self.get_visible_element(self.bid_ele_locator)

