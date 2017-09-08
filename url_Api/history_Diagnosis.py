#!/usr/bin/python
# coding:utf-8


"""
Created on 2017-07-20

@author: Wangchenyang

@userdict: 查询
"""

import requests
import login_Workbench as htmlLogin


# 患者历史诊断信息
_historyDiagnosis = "http://172.17.200.94/emr/encounter/historyDiagnosis?patientId=40289081-5bdc9c22-015b-dcaa74ea-00b0"
# 引用htmlLoign的cookie
cookies = htmlLogin._session_cookie


# 获得患者的历史病历
def patient_historyDiagnosis():
    # 调用historyDiagnosis接口
    patient_history_diagnosis_info = cookies.get(url = _historyDiagnosis)
    # 对http返回值进行判断，对于200做基本校验
    try:
        # 判断historyDiagnosis接口返回的接口200
        if patient_history_diagnosis_info.status_code == 200:
            # 获取返回的参数值
            print "患者的历史病历信息:%s" % patient_history_diagnosis_info.content
            patient_history_diagnosis_info_dict = patient_history_diagnosis_info.json()
            print patient_history_diagnosis_info_dict
        else:
            raise Exception("http error info:%s" % (patient_history_diagnosis_info.status_code))
    except ImportError:
        print 'ImportError'
