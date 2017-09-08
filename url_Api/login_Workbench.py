#!/usr/bin/python
# coding:utf-8


"""
Created on 2017-07-20

@author: Wangchenyang

@userdict: 登录医生工作站
"""

import requests


_url = 'http://172.17.200.94/login'
_data = {"username": "3958", "password": "3958"}
# cookie持久化
_session_cookie = requests.Session()

# 调用登录接口
def login_workbench():
    try:
        # 对http返回值进行判断，对于200做基本校验
        # 调用登录接口
        login_success = _session_cookie.post(url=_url, data=_data)
        if login_success.status_code == 200:
            print '接口登录成功'
        else:
            # 对于http返回非200的code，输出相应的code
            raise Exception("http error info:%s" % login_success.status_code)
    except ImportError:
        print 'ImportError!'

login_workbench()