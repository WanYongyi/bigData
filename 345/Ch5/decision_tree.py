# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:53:05 2024

@author: MAJOR
"""

# 5-2 使用ID3决策树算法预测销量高低

from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier as DTC
import pandas as pd

# 参数初始化
filename = './data/sales_data.xls'
data = pd.read_excel(filename, index_col='序号')  # 导入数据

# 数据是类别标签，要将它转换为数据
# 用1来表示“好”“是”“高”这三个属性，用-1来表示“坏”“否”“低”
data[data == '好'] = 1
data[data == '是'] = 1
data[data == '高'] = 1
data[data != 1] = -1
x = data.iloc[:, :3].astype(int)
y = data.iloc[:, 3].astype(int)


dtc = DTC(criterion='entropy')  # 建立决策树模型，基于信息熵
dtc.fit(x, y)  # 训练模型

# 导入相关函数，可视化决策树。
# 导出的结果是一个dot文件，需要安装Graphviz才能将它转换为pdf或png等格式。
x = pd.DataFrame(x)

with open("./tmp/tree.dot", 'w') as f:
    export_graphviz(dtc, feature_names = x.columns, out_file = f)
    f.close()
