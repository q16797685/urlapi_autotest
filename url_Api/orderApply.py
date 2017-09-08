#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-07-20

@author: Wangchenyang

@userdict:申请医嘱接口
"""

import json
import login_Workbench as htmlLogin

# 变量
_order_data = \
    {"encounterId": "218211",
     "id": "",
     "itemList":
    [{"dermaticFlag": 0,
      "dosage": 150,
      "dosageUnit": "mg",
      "durationId": 1,
      "eqQty": 50,
      "eqUnit": "mg",
      "frequenceId": 1,
      "instructionId": 49,
      "medicineId": 1878,
      "orderMasterId": 25405,
      "orderMasterType": "medicine",
      "outputFactor": 14,
      "outputPrice": 82,
      "riorityType": "NORM",
      "quantity": 1,
      "specs": "50mg*14",
      "targetHisLocCode": "2340208",
      "treatmentDays": 1}
     ]}
_headers = {"Content-Type": "application/json"}
_submit = 'http://172.17.200.94/emr/order/submit'

# 引用htmlLoign的cookie
cookies = htmlLogin._session_cookie


# 医嘱申请
def order_apply():
    # 调用submit接口
    order_apply_info = cookies.post(url= _submit, data= json.dumps(_order_data), headers= _headers)
    # 对http返回值进行判断，对于200做基本校验
    try:
        # 判断submit接口返回的接口200
        if order_apply_info.status_code == 200:
            # 获取返回的参数值
            print "医嘱申请信息:%s" % order_apply_info.content
            order_apply_info_dict = order_apply_info.json()
            print order_apply_info_dict
        else:
            raise Exception("http error info:%s" % (order_apply_info.status_code))
    except ImportError:
        print 'ImportError'