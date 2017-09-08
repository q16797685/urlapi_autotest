#!/usr/bin/python
# coding:utf-8


"""
Created on 2017-07-20

@author: Wangchenyang

@userdict: 打印病历
"""

import login_Workbench as htmlLogin


# 打印患者门诊病历
_getHistoryEncounterById = "http://172.17.200.94/emr/reservation/getHistoryEncounterById?encounterId=76422"
# 引用htmlLoign的cookie
cookies = htmlLogin._session_cookie


# 打印患者门诊病历
def patient_print_encounter():
    # 调用getHistoryEncounterById接口
    patient_print_encounter_info = cookies.get(url = _getHistoryEncounterById)
    # 对http返回值进行判断，对于200做基本校验
    try:
        # 判断getHistoryEncounterById接口返回的接口200
        if patient_print_encounter_info.status_code == 200:
            # 获取返回的参数值
            print "打印患者门诊病历:%s" % patient_print_encounter_info.content
            patient_print_encounter_info_dict = patient_print_encounter_info.json()
            code = patient_print_encounter_info_dict['code']
            print code
        else:
            raise Exception("http error info:%s" % (patient_print_encounter_info.status_code))
    except ImportError:
        print 'ImportError'
