#!/usr/bin/python
# coding:utf-8


"""
Created on 2017-07-20

@author: Wangchenyang

@userdict: 测试Url接口
"""

import login_Workbench
import htmlLogin
import print_Encounter
import history_Diagnosis
import history_OrderMedicines
import orderApply


class urlApi(object):
    def testcase(self):
        login_Workbench.login_workbench()
        htmlLogin.patient_info()
        htmlLogin.patient_encounter_info()
        htmlLogin.patient_scale_number()
        htmlLogin.patient_diagnosis_record()
        htmlLogin.patient_attach_number()
        print_Encounter.patient_print_encounter()
        history_Diagnosis.patient_historyDiagnosis()
        history_OrderMedicines.patient_historyOrderMedicines()
        orderApply.order_apply()

if __name__ == '__main__':
    Test = urlApi()
    Test.testcase()