# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:13:19 2024

@author: MAJOR
"""

# 7-7 属性选择

# 属性选择、构造与数据标准化

from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

# 读取数据清洗后的数据
cleanedfile = './tmp/data_cleaned.csv'  # 数据清洗后保存的文件路径
airline = pd.read_csv(cleanedfile, encoding='utf-8')
# 选取需求属性
airline_selection = airline[['FFP_DATE', 'LOAD_TIME', 'LAST_TO_END',
                             'FLIGHT_COUNT', 'SEG_KM_SUM', 'avg_discount']]
print('筛选的属性前5行为：\n', airline_selection.head())


# 7-8 属性构造与数据标准化

# 构造属性L
L = pd.to_datetime(airline_selection['LOAD_TIME']) - \
    pd.to_datetime(airline_selection['FFP_DATE'])
L = L.astype('str').str.split().str[0]
# 计算月数
L = L.astype('int')/30

# 合并属性
# L表示客户关系长度，R表示消费时间间隔，F表示消费频率，M表示飞行里程，C表示折扣系数平均值
# 删去前两列再与L合并
airline_features = pd.concat([L, airline_selection.iloc[:, 2:]], axis=1)
airline_features.columns = ['L', 'R', 'F', 'M', 'C']
print('构建的LRFMC属性前5行为：\n', airline_features.head())

# 数据标准化
data = StandardScaler().fit_transform(airline_features)
np.savez('./tmp/airline_scale.npz', data)
print('标准化后LRFMC五个属性为：\n', data[:5, :])
