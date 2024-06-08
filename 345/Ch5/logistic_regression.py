# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:49:12 2024

@author: MAJOR
"""

# 5-1 逻辑回归

import pandas as pd
from sklearn.linear_model import LogisticRegression as LR
import numpy as np

# 参数初始化
filename = './data/bankloan.xls'
data = pd.read_excel(filename)
x = data.iloc[:,:8].to_numpy()
y = data.iloc[:,8].to_numpy()

lr = LR()  # 建立逻辑回归模型
lr.fit(x, y)  # 用筛选后的特征数据来训练模型
print('模型的平均准确度为：%s' % lr.score(x, y))