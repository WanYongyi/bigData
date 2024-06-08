# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:33:43 2024

@author: MAJOR
"""
# 6-5 灰色预测模型预测
import sys
sys.path.append('../Ch6')  # 设置路径
import numpy as np
import pandas as pd
from GM11 import GM11  # 引入自编的灰色预测函数
import xlwt

inputfile1 = 'new_reg_data.csv'  # 输入的数据文件
inputfile2 = 'data.csv'  # 输入的数据文件
new_reg_data = pd.read_csv(inputfile1)  # 读取经过特征选择后的数据
data = pd.read_csv(inputfile2)  # 读取总的数据
new_reg_data.index = range(1994, 2014)
new_reg_data.loc[2014] = None
new_reg_data.loc[2015] = None
features = ['x1', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x13']
# 检查列名是否正确
print("DataFrame columns:", new_reg_data.columns)


for feature in features:
    f = GM11(new_reg_data.loc[range(1994, 2014),feature].to_numpy())[0]
    new_reg_data.loc[2014,feature] = f(len(new_reg_data)-1)  # 2014年预测结果
    new_reg_data.loc[2015,feature] = f(len(new_reg_data))  # 2015年预测结果
    new_reg_data[feature] = new_reg_data[feature].round(2)  # 保留两位小数


# outputfile = '../tmp/new_reg_data_GM11.xls'  # 灰色预测后保存的路径

y = list(data['y'].values)  # 提取财政收入列，合并至新数据框中
y.extend([np.nan,np.nan])
new_reg_data['y'] = y
# new_reg_data.to_excel(outputfile)  # 结果输出
print('预测结果为：\n',new_reg_data.loc[2014:2015,:])  # 预测结果展示

