#!/usr/bin/python
#coding:utf-8

'''
Created on 2017-07-20

@author: Wangchenyang

@userdict:调用登录接口
'''

import urllib2
import urllib

moblies = {}
moblies['mobile'] = "13787044789"
moblies['password'] = "123456"
moblies['devicetype'] = "android"
moblies['devicesystem'] = "Nexus 6P"
moblies['deviceid'] = "1d1904010431c695"
send_headers = {
 'Content-Type':'application/json'}


data = urllib.urlencode(moblies)
url = "https://api.emr.fulcruminfo.cn/v1/users/login"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()