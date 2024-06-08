# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:55:11 2024

@author: MAJOR

周期性分析
"""

# 3-7 某单位日用电量预测分析

import pandas as pd
import matplotlib.pyplot as plt

df_normal = pd.read_csv("../data/chap3/user.csv")
plt.figure(figsize=(8,4))
plt.plot(df_normal["Date"],df_normal["Eletricity"])
plt.xlabel("日期")
plt.ylabel("每日电量")
# 设置x轴刻度间隔
x_major_locator = plt.MultipleLocator(7)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.title("正常用户电量趋势")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.show()  # 展示图片

# 窃电用户用电趋势分析
df_steal = pd.read_csv("../data/chap3/Steal user.csv")
plt.figure(figsize=(10, 9))
plt.plot(df_steal["Date"],df_steal["Eletricity"])
plt.xlabel("日期")
plt.ylabel("日期")
# 设置x轴刻度间隔
x_major_locator = plt.MultipleLocator(7)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.title("窃电用户电量趋势")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.show()  # 展示图片