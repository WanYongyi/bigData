# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:04:38 2024

@author: MAJOR
"""

# 4-4 线损率属性构造
import pandas as pd

# 参数初始化
inputfile= '../data/chap4/electricity_data.xls'  # 供入供出电量数据
outputfile = '../tmp/electricity_data.xlsx'  # 属性构造后数据文件

data = pd.read_excel(inputfile)  # 读入数据
data['线损率'] = (data['供入电量'] - data['供出电量']) / data['供入电量']

data.to_excel(outputfile, index = False)  # 保存结果