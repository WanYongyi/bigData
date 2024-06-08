# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:44:07 2024

@author: MAJOR
"""

# MLP

import sys
sys.path.append('../Ch6')  # 设置路径
import numpy as np
import pandas as pd
from GM11 import GM11  # 引入自编的灰色预测函数
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

# 引入使用灰色预测模型预测的：各个影响财政收入的关键因素在2014和2015年的值
inputfile = ('E:\pycode\\6789\Ch6\\new_reg_dat'
             'a_GM11.xls')  # 灰色预测后保存的路径
data = pd.read_excel(inputfile, index_col=0)  # 读取数据
features = ['x1', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x13']  # 属性所在列
data_train = data.loc[range(1994, 2014)].copy()  # 取2014年前的数据建模
# 归一化
data_mean = data_train.mean()
data_std = data_train.std()



data_train = (data_train - data_mean) / data_std  # 数据标准化
x_train = data_train[features].to_numpy()  # 属性数据
y_train = data_train['y'].to_numpy()  # 标签数据

# 训练，MLP
mlp = MLPRegressor(hidden_layer_sizes=(150,), max_iter=1000, random_state=42)  # 调用MLPRegressor()函数
mlp.fit(x_train, y_train)
x = ((data[features] - data_mean[features]) / data_std[features]).to_numpy()  # 预测，并还原结果
data['y_pred'] = mlp.predict(x) * data_std['y'] + data_mean['y']

print('真实值与预测值分别为：\n', data[['y', 'y_pred']])

fig = data[['y', 'y_pred']].plot(subplots=True, style=['b-o', 'r-*'])  # 画出预测结果图
plt.show()


# outputfile_mlp = '../tmp/new_reg_data_GM11_revenue_MLP.xls'  # MLP预测后保存的结果
# data.to_excel(outputfile_mlp, index=True)  # 保留索引列

