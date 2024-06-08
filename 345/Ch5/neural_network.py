# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:57:31 2024

@author: MAJOR
"""

from cm_plot import *  # 导入自行编写的混淆矩阵可视化函数
from keras.layers import Dense, Activation
from keras.models import Sequential
import pandas as pd
import numpy as np

# 参数初始化
inputfile = './data/sales_data.xls'
data = pd.read_excel(inputfile, index_col='序号')  # 导入数据

# 数据是类别标签，要将它转换为数据
# 用1来表示“好”“是”“高”这三个属性，用0来表示“坏”“否”“低”
data[data == '好'] = 1
data[data == '是'] = 1
data[data == '高'] = 1
data[data != 1] = 0
x = data.iloc[:, :3].astype(int)
y = data.iloc[:, 3].astype(int)


model = Sequential()  # 建立模型
model.add(Dense(input_dim=3, units=10))
model.add(Activation('relu'))  # 用relu函数作为激活函数，能够大幅提供准确度
model.add(Dense(input_dim=10, units=1))
model.add(Activation('sigmoid'))  # 由于是0-1输出，用sigmoid函数作为激活函数

model.compile(loss='binary_crossentropy', optimizer='adam')
# 编译模型。由于我们做的是二元分类，所以我们指定损失函数为binary_crossentropy，以及模式为binary
# 另外常见的损失函数还有mean_squared_error、categorical_crossentropy等，请阅读帮助文件。
# 求解方法我们指定用adam，还有sgd、rmsprop等可选

model.fit(x, y, epochs=1000, batch_size=10)  # 训练模型，学习一千次
pred = model.predict(x)  # 分类预测
yp = np.where(pred > 0.5, 1,0)
cm_plot(y, yp).show()  # 显示混淆矩阵可视化结果
