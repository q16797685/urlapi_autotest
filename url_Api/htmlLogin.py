#!/usr/bin/python
# coding:utf-8


"""
Created on 2017-07-20

@author: Wangchenyang

@userdict: 双击病人信息
"""


import re
import login_Workbench

# " + str(encounter_id) + "
# 变量
_url = 'http://172.17.200.94/login'
_data = {"username": "3958", "password": "3958"}
# 患者个人信息
_getPatientByEncounterId = "http://172.17.200.94/emr/reservation/getPatientByEncounterId?encounterId" \
                           "=223709"
# 患者病历信息
_getEncounter = "http://172.17.200.94/emr/reservation/getEncounter?enId" \
                "=213293&resId=229505"
# 页面红点和数字
_encounterSummary = "http://172.17.200.94/emr/encounter/encounterSummary?encounterId=223709"
# 患者诊断信息
_getDiagnosisRecord = "http://172.17.200.94/emr/diagnosis/getDiagnosisRecord?encounterId=223709"
# 患者上传的附件
_attach = "http://172.17.200.94/emr/reservation/encounters/223709/attachs"
_findByEncounterId = "http://172.17.200.94/emr/order/findByEncounterId?encounterId=76396"
# cookie持久化
cookies = login_Workbench._session_cookie


# 获取患者个人信息
def patient_info():
    # 调用getPatientByEncounterId接口
    patient_by_encounter_id = cookies.get(url = _getPatientByEncounterId)
    # 对http返回值进行判断，对于200做基本校验
    try:
        # 判断getPatientByEncounterId接口返回的接口200
        if patient_by_encounter_id.status_code == 200:
            # 获取返回的参数值
            patient_byencounter_id_dict = patient_by_encounter_id.json()
            code = patient_byencounter_id_dict['code']
            name = patient_byencounter_id_dict['data']['name']
            print "患者个人信息:%s" % code
            print name
        else:
            raise Exception("http error info:%s" % (patient_by_encounter_id.status_code))
    except ImportError:
        print 'ImportError'


# 获取患者病历信息
def patient_encounter_info():
    # 调用getEncounter接口
    patient_encounter_id = cookies.get(url = _getEncounter)
    # 对http返回值进行判断，对于200做基本校验
    try:
        # 判断getEncounter接口返回的接口200
        if patient_encounter_id.status_code == 200:
            # 获取返回的参数值
            # patient_encounter_id_dict = patient_encounter_id.json()
            # code = patient_encounter_id_dict['code']
            print "患者病历信息: %s" % patient_encounter_id.content
            # pattern = re.compile('"title":"(.*?)".*?,"value":"(.*?)"')
            pattern = re.compile('"value":"(.*?)"')
            match = re.findall(pattern, patient_encounter_id.content)
            print match[0]
        else:
            raise Exception("http error info:%s" % (patient_encounter_id.status_code))
    except ImportError:
        print 'ImportError'


# 获取患者量表数量
def patient_encounter_summary():
    # 调用encounterSummary接口
    patient_encounter_summary_info = cookies.get(url = _encounterSummary)
    # 对http返回值进行判断，对于200做基本校验
    try:
        # 判断encounterSummary接口返回的接口200
        if patient_encounter_summary_info.status_code == 200:
            # 获取返回的参数值
            print patient_encounter_summary_info.content
            patient_scale_summary_dict = patient_encounter_summary_info.json()
            code = patient_scale_summary_dict['code']
            # name = patient_scale_summary_dict['data']['name']
            print code
        else:
            raise Exception("http error info:%s" % (patient_encounter_summary_info.status_code))
    except  ImportError:
        print 'ImportError'


# 获取患者诊断信息
def patient_diagnosis_record():
    # 调用getDiagnosisRecord接口
    patient_diagnosis_info = cookies.get(url = _getDiagnosisRecord)
    # 对http返回值进行判断，对于200做基本校验
    try:
        # 判断getDiagnosisRecord接口返回的接口200
        if patient_diagnosis_info.status_code == 200:
            # 获取返回的参数值
            print "患者诊断信息: %s" % patient_diagnosis_info.content
            print type(patient_diagnosis_info.content)
            patient_diagnosis_info_dict = patient_diagnosis_info.json()
            print patient_diagnosis_info_dict
            code = patient_diagnosis_info_dict['code']
            print code
        else:
            raise Exception("http error info:%s" % (patient_diagnosis_info.status_code))
    except ImportError:
        print 'ImportError'


# 获得患者量表列表
def patient_scale_number():
    # 调用attach接口
    patient_scale_number_info = cookies.get(url = _attach)
    # 对http返回值进行判断，对于200做基本校验
    try:
        # 判断attach接口返回的接口200
        if patient_scale_number_info.status_code == 200:
            # 获取返回的参数值
            print "患者上传的附件信息:%s" % patient_scale_number_info.content
            patient_attach_info_dict = patient_scale_number_info.json()
            code = patient_attach_info_dict['code']
            # name = patient_scale_summary_dict['data']['name']
            print code
        else:
            raise Exception("http error info:%s" % (patient_scale_number_info.status_code))
    except ImportError:
        print 'ImportError'


# 获得患者上传的附件
def patient_attach_number():
    # 调用attach接口
    patient_attach_info = cookies.get(url = _attach)
    # 对http返回值进行判断，对于200做基本校验
    try:
        # 判断attach接口返回的接口200
        if patient_attach_info.status_code == 200:
            # 获取返回的参数值
            print "患者上传的附件信息:%s" % patient_attach_info.content
            patient_attach_info_dict = patient_attach_info.json()
            code = patient_attach_info_dict['code']
            # name = patient_scale_summary_dict['data']['name']
            print code
        else:
            raise Exception("http error info:%s" % (patient_attach_info.status_code))
    except ImportError:
        print 'ImportError'


# 获得患者当次就诊的医嘱信息
def patient_find_By_EncounterId():
    # 调用findByEncounterId接口
    patient_find_by_encounter_info = cookies.get(url = _findByEncounterId)
    # 对http返回值进行判断，对于200做基本校验
    try:
        # 判断attach接口返回的接口200
        if patient_find_by_encounter_info.status_code == 200:
            # 获取返回的参数值
            print "患者当次就诊的医嘱信息:%s" % patient_find_by_encounter_info.content
            patient_find_by_encounter_info_dict = patient_find_by_encounter_info.json()
            code = patient_find_by_encounter_info_dict['code']
            print code
        else:
            raise Exception("http error info:%s" % (patient_find_by_encounter_info.status_code))
    except ImportError:
        print 'ImportError'
