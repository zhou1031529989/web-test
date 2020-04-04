# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 17:18
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : conftest.py
# @Software : 


# 管理测试用例执行环境,不可继承unittest,fixture与ddt相冲突
# allure安装包https://github.com/allure-framework/allure2/releases
# 将目录F:\allure\allure-commandline-2.13.2\allure-2.13.2\bin放到环境变量里

import pytest
from selenium import webdriver
from class12_z_fixture.pages.login_page import LoginPage
from class12_z_fixture.pages.bid_page import BidPage

from class12_z_fixture.datas import login_data


@pytest.fixture(scope='class')
def my_set_class():
    print("begin my class")
    driver = webdriver.Chrome()
    # 不用unittest的setUpClass函数后，打开浏览器的操作要放到这里来
    driver.get('http://120.78.128.25:8765/Index/login.html')
    login_page = LoginPage(driver)

    yield (driver,login_page)

    print("finish my class")
    driver.quit()

@pytest.fixture(scope='class')
def my_set2_class():
    print("begin my class2")
    driver = webdriver.Chrome()
    driver.get('http://120.78.128.25:8765/Index/login.html')
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.submit_userinfo(
        login_data.user_correct['phone'], login_data.user_correct['password'])
    bid_page = BidPage(driver)

    yield (driver,bid_page)

    print("finish my class2")
    driver.quit()

# True 定义后自动执行，无需加装饰
@pytest.fixture('session',autouse=True)
def my_session():
    print("begin my session")

    yield

    print("finish my session")




