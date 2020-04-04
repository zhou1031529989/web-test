# -*- coding: utf-8 -*-
# @Time     : 2020/3/24 17:18
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : conftest.py
# @Software : 


# 管理测试用例执行环境,可不继承unittest,fixture与ddt相冲突
import pytest
from selenium import webdriver
from class11_pytest_fixture.pages.login_page import LoginPage



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

# True 定义后自动执行，无需加装饰
@pytest.fixture('session',autouse=True)
def my_session():
    print("begin my session")

    yield

    print("finish my session")




