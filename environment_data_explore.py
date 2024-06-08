# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:33:11 2024

@author: MAJOR
"""

import pandas as pd
import matplotlib.pyplot as plt

datafile= './data/environment_data.xls'  # 航空原始数据,第一行为属性标签

# 读取原始数据
data = pd.read_excel(datafile).iloc[:,range(0,6)]
labels = pd.read_excel(datafile).iloc[:,-1].replace(['I','II','III','IV','V','VI','VII'],[1,2,3,4,5,6,7])

lv_1 = pd.value_counts(labels)[1]
lv_2 = pd.value_counts(labels)[2]
lv_3 = pd.value_counts(labels)[3]
lv_4 = pd.value_counts(labels)[4]
lv_5 = pd.value_counts(labels)[5]
lv_6 = pd.value_counts(labels)[6]
lv_7 = pd.value_counts(labels)[7]

fig = plt.figure(figsize = (8 ,5))  # 设置画布大小
plt.bar(x=range(7), height=[lv_1,lv_2,lv_3,lv_4,lv_5,lv_6,lv_7], width=0.4, alpha=0.8, color='skyblue')
plt.xticks([index for index in range(7)], ['I','II','III','IV','V','VI','VII'])
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.xlabel('空气等级')
plt.ylabel('数量')
plt.title('各空气等级数量')
plt.show()
plt.close()