#!/usr/bin/python
# coding:utf-8


"""
Created on 2017-07-20

@author: Wangchenyang

@userdict: 数据库操作
"""

from mysql import connector
import random


# 获取数据库DB连接
conn = connector.connect(host='172.17.200.94', user='root', passwd='123456', db='FEMR', port=3306)
cur = conn.cursor()
# 数据库语句
cur.execute("select id,reservation_id from EMR_ENCOUNTER where patient_id = '2c928085-5bdd5680-015b-dd580eb1-0001'")
# 获取查询的所有信息
patient_log = cur.fetchall()
# 随机获取1-166数据
choice_num = random.randint(1, 166)
# 获取encounter_id
encounter_id = patient_log[choice_num][0]
# 获取reservation_id
reservation_id = patient_log[choice_num][1]
