# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:21:27 2024

@author: MAJOR

定量数据的分布分析
"""
# 3-3 捞起生鱼片的季度销售情况
import pandas as pd
import numpy as np

catering_sale = '../data/chap3/catering_fish_congee.xls'  # 餐饮数据
data = pd.read_excel(catering_sale,names=['date','sale'])  # 读取数据，指定“日期”列为索引

import matplotlib.pyplot as plt
d = 500  # 设置组距
num_bins = round((max(data['sale']) - min(data['sale'])) / d)  # 计算组数（极差/组距）
plt.figure(figsize=(10,6))  # 设置图框大小尺寸
plt.hist(data['sale'], num_bins)
plt.xticks(range(0, 4000, d))
plt.xlabel('sale分层')
plt.grid()
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.title('季度销售额频率分布直方图',fontsize=20)
plt.show()