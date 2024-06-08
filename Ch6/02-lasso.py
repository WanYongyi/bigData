# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:30:26 2024

@author: MAJOR
"""

# 6-4 Lasso回归选取关键属性

import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso

inputfile = 'data.csv'  # 输入的数据文件
outputfile = 'new_reg_data.csv'  # 输出的数据文件
data = pd.read_csv(inputfile)  # 读取数据
data.columns = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6',
                'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'y']
lasso = Lasso(1000)  # 调用Lasso()函数，设置λ的值为1000
lasso.fit(data.iloc[:, 0:13], data['y'])
print('相关系数为：', np.round(lasso.coef_, 5))  # 输出结果，保留五位小数

print('相关系数非零个数为：', np.sum(lasso.coef_ != 0))  # 计算相关系数非零的个数

mask = lasso.coef_ != 0  # 返回一个相关系数是否为零的布尔数组
print('相关系数是否为零：', mask)
# 使用布尔掩码选择特征列
selected_features = data.columns[:13][mask].tolist()  # 只选择前13列特征的列名
print("选择的特征列：", selected_features)
# 创建新的数据框，仅包含选择的特征和目标变量
new_reg_data = data[selected_features + ['y']]
new_reg_data.to_csv(outputfile, index=False)  # 存储数据
print('输出数据的维度为：', new_reg_data.shape)  # 查看输出数据的维度

