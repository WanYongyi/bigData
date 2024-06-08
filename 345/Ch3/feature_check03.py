# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:46:05 2024

@author: MAJOR

对比分析
"""

# 3-5 不同部门在各月份的销售对比情况
# 部门之间销售金额比较
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel("../data/chap3/dish_sale.xls")
plt.figure(figsize=(8, 4))
plt.plot(data['月份'], data['A部门'], color='green', label='A部门',marker='o')
plt.plot(data['月份'], data['B部门'], color='red', label='B部门',marker='s')
plt.plot(data['月份'], data['C部门'],  color='skyblue', label='C部门',marker='x')
plt.legend() # 显示图例
plt.ylabel('salse（Ten-thousand）')
plt.show()


#  B部门各年份之间销售金额的比较
data=pd.read_excel("../data/chap3/dish_sale_b.xls")
plt.figure(figsize=(8, 4))
plt.plot(data['月份'], data['2012年'], color='green', label='2012年',marker='o')
plt.plot(data['月份'], data['2013年'], color='red', label='2013年',marker='s')
plt.plot(data['月份'], data['2014年'],  color='skyblue', label='2014年',marker='x')
plt.legend() # 显示图例
plt.ylabel('salse（Ten-thousand）')
plt.show()
