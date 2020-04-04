# -*- coding: utf-8 -*-
# @Time     : 2020/3/23 16:24
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : login_data.py
# @Software :

# login_data.user_correct 模块也是对象

# 正确的用户信息
user_correct = {"phone": "18684720553", "password": "python"}

# 错误的用户信息
user_incorrect = [
    {"phone": "", "password": "", "expected": "请输入手机号"},
    {"phone": "12", "password": "", "expected": "请输入正确的手机号"},
    {"phone": "13443256789", "password": "", "expected": "请输入密码"}
]

# 未授权的用户信息  未授权
# 调试器 暂停 js不继续执行 ，此时可定位到toast弹窗（Chrome）
user_unauthorized = [
    {"phone": "13443256789", "password": "12", "expected": "此账号没有经过授权，请联系管理员!"}
]


