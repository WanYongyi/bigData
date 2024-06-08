# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:53:48 2024

@author: MAJOR
"""

# 4-2  数据规范化
import pandas as pd
import numpy as np
datafile = '../data/chap4/normalization_data.xls'  # 参数初始化
data = pd.read_excel(datafile, header = None)  # 读取数据
print(data)

(data - data.min()) / (data.max() - data.min())  # 最小-最大规范化
(data - data.mean()) / data.std()  # 零-均值规范化
data / 10 ** np.ceil(np.log10(data.abs().max()))  # 小数定标规范化

