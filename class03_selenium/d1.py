# -*- coding: utf-8 -*-
# @Time     : 2020/3/20 22:27
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : d1.py
# @Software : 

# python ->  webdriver(接口)   -> （js 浏览器）

# 测试内容：1.数据正确 2.交互效果 3.兼容性...
# 1.数据正常 1.>定位元素 dict['key']   /  2.>DOM_OBJ.attr
#
# document.getElementBy...

# python 去命令 js 执行
import requests
url = ""
params = {
    "command":"getElementById",
    "id":"title"
}
# res = requests.get(url,params=params)  # ojb.text   obj.id

# webdriver ==>  js执行 ==> document.getElementById("title")  ==> DOM obj
# webdriver 进行拼接 document + command + () 【selenium原理】


def get_element_by_id(title):
        params = {
        "command":"getElementById",
        "id":"title"
    }
        requests.get(url,params)

def get_element_by_name():
    pass

url = "http://www.baidu.com"
res = requests.get(url)
print(res.text)

# -->转成对象 --> 需要网页解析工具 BeautifulSoup lxml pyquery  把HTML映射成对象，再通过对象里面的方法查找

# selenium 解析 刷新 后退













