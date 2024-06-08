# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:00:54 2024

@author: MAJOR

相关性分析
"""

# 3-9 餐饮销量数据相关性分析

# 餐饮销量数据相关性分析
from __future__ import print_function
import pandas as pd

catering_sale = '../data/chap3/catering_sale_all.xls'  # 餐饮数据，含有其他属性
data = pd.read_excel(catering_sale, index_col = '日期')  # 读取数据，指定“日期”列为索引列

print(data.corr())  # 相关系数矩阵，即给出了任意两款菜式之间的相关系数
print(data.corr()['百合酱蒸凤爪'])  # 只显示“百合酱蒸凤爪”与其他菜式的相关系数
# 计算“百合酱蒸凤爪”与“翡翠蒸香茜饺”的相关系数
print(data['百合酱蒸凤爪'].corr(data['翡翠蒸香茜饺']))