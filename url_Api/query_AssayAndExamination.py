#!/usr/bin/python
# coding:utf-8


"""
Created on 2017-07-20

@author: Wangchenyang

@userdict: 查询患者的检查检验列表
"""

import login_Workbench as htmlLogin


# 患者的检查检验列表
_queryAssayAndExamination = "http://172.17.200.94/emr/encounter/queryAssayAndExamination" \
                            "?patientId=2c928088-5ce3ef0a-015c-e71ea1ec-018a"
# 引用htmlLoign的cookie
cookies = htmlLogin._session_cookie


# 获得患者的检查检验列表
def patient_AssayAndExamination():
    # 调用queryAssayAndExamination接口
    patient_assay_examination_info = cookies.get(url = _queryAssayAndExamination)
    # 对http返回值进行判断，对于200做基本校验
    try:
        # 判断queryAssayAndExamination接口返回的接口200
        if patient_assay_examination_info.status_code == 200:
            # 获取返回的参数值
            print "患者检查检验列表信息:%s" % patient_assay_examination_info.content
            patient_assay_examination_info_dict = patient_assay_examination_info.json()
            code = patient_assay_examination_info_dict['code']
            print code
        else:
            raise Exception("http error info:%s" % (patient_assay_examination_info.status_code))
    except ImportError:
        print 'ImportError'
