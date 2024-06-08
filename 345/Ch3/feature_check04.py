# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:53:34 2024

@author: MAJOR

统计量分析
"""

# 3-6 餐饮销量数据统计量分析
import pandas as pd

catering_sale = '../data/chap3/catering_sale.xls'  # 餐饮数据
data = pd.read_excel(catering_sale, index_col = '日期')  # 读取数据，指定“日期”列为索引列
data = data[(data['销量'] > 400)&(data['销量'] < 5000)]  # 过滤异常数据
statistics = data.describe()  # 保存基本统计量

statistics.loc['range'] = statistics.loc['max']-statistics.loc['min']  # 极差
statistics.loc['var'] = statistics.loc['std']/statistics.loc['mean']  # 变异系数
statistics.loc['dis'] = statistics.loc['75%']-statistics.loc['25%']  # 四分位数间距

print(statistics)