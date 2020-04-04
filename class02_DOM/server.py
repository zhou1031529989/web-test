# -*- coding: utf-8 -*-
# @Time     : 2020/3/20 15:48
# @Author   : Zhou_Chao
# @Email    : 1031529989@qq.com
# @File     : server.py
# @Software :

from flask import Flask,request,jsonify

app = Flask(__name__)
@app.route("/")
def index():
    method = request.method
    print(method)
    res = {}
    if method == 'GET':
        print(request.args)
        res = dict(request.args)
    elif method == 'POST':
        res = dict(request.form)

    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True,port=4556)

# 访问服务,并输入参数  localhost:4556?yuze=45