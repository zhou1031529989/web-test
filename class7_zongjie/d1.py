# -*- coding: utf-8 -*-
# @Time     : 2020/3/22 21:15
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : d1.py
# @Software : 


# 项目经验，职责描述
# 1. 分析产品化测试；
# 10 天 ==》 10 分钟需求，设计测试用例；
# 简历反面教材：
# # 2. 执行测试用例，跟踪 bug;
# # 3. 利用禅道等工具管理；
# # 4. 使用 python + requests 去实现接口自动

# cpu ==> 人工   cpu 一秒，人间一年。
# 学会了怎么使用自动化，你就会很好的表达出来。


# 简历原则：
# star 1 目标，2. 途径，方法，3 效果。

# 企业对于测试人员的要求。
#

# 比较系统的总结。


# 比较表层的是知识 == 》 思维过程

# 1. UI 自动化？？ ==》 面试题： UI自动化测试比手工测试好吗？你对web自动化测试的理解？
# 简历里面？？ 我使用 selenium 做了。。。实现了web自动化测试 ==》
# 2. HTML ==》 标签，属性，text,下属标签 (css_selector, xpath)
# 3. Form --> 后台接口，name , value
# 4. JS,DOM.  1. 获取元素，元素定位；2.改变元素的属性，内容 3. 事件
# alert ==> onload 父级对象，子级对象。同胞。。
# 5. !!!Selenium 原理 ==》 1. service , subprocess ==> webdriver.exe
# 2. client ==> urlib3 访问服务，类似于 requests 作用
# 6. 8 大元素定位。 1. id, name, tagname, link_text, partial_link_text,
# class_name, css_selector, xpath
# 7. 都是调用 find_element() # 变量名，函数名，类名 ，有意义。
# 8. 很少的注释，但是你可以看懂，命名编码规范。XPATH
# 9. 列表，复数。 XPATH ,大写，不到万不得已不要给我重新赋值。
# global
# 10.！！！等待。必不可少。有可能你的页面发生变化的时候，一定要等待。
# 如果出现该有的元素没有定位到，很有可能就是没有等待。
# 交互操作。select ==> 1.通过点击option 。2. Select
# 鼠标操作。ActionChains
# 设计。链式调用 ==> 数据库  查询Query name= age=  ... order_by.. limit(2).first()
# 键盘。 send_keys()
# 窗口滚动。。。 ==》 动态加载，懒加载， JS脚本
# JS 脚本怎么操作。 arguments[0].value = 'new'  arguments[1].value = 'new'
# driver.execute_script(js_code, js_param0, js_param1)
# element.set_attribute() 更新数据 ==> 发送 js 脚本
# 文件上传。pypiwin32。 你在web自动化测试遇到需要用操作系统原生控件的时候怎么办？
# excel => openpyxl xls xlrd ==>，  数据库 ==> pymysql cymysql,
# 窗口切换 ==》 切换 窗口，frame, alert. accept,dismiss

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import sqlite3

ac = ActionChains()
ac.click().move_to_element()




# webdriver 是个什么类型，类？函数？模块？包？
from selenium import webdriver
#
driver = webdriver.Chrome()

driver.switch_to.alert()

# 动态属性, 分数，Student

class Student:
    def __init__(self):
        self.grade = 0
        self.age = 23

a = Student() # 0- 100
a.grade = 10000
# 动态属性 python 面试题！！！

# xianshi 等待的 __init__.py 文件有什么作用？可以用来简化包内部的调用过程。
# 模块来调用，单例模式。python 去设计一个单例模式。 模块导入

# 单例

# class A:
#     def __init__(self):
#         pass
#
# a = A()
# print(id(a))
#
# b = A()
# print(id(b))

# 不些注释
driver.find_element()






