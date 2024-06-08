# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:43:49 2024

@author: MAJOR
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import seaborn as sn

datafile= './data/environment_data.xls'  # 航空原始数据,第一行为属性标签

# 读取原始数据
data = pd.read_excel(datafile).iloc[:,range(0,6)]
labels = pd.read_excel(datafile).iloc[:,-1].replace(['I','II','III','IV','V','VI','VII'],[1,2,3,4,5,6,7])


# 拆分数据
data_tr,data_te,label_tr,label_te = train_test_split(data,labels,test_size=0.2,random_state=10)
# 支持向量机训练
clf = svm.SVC()  # class
# 训练
clf.fit(data_tr, label_tr.astype('int'))
# 预测
label_pr = clf.predict(data_te)


df_cm = pd.DataFrame(confusion_matrix(label_te, label_pr))
print(accuracy_score(label_te,label_pr))


# sn.heatmap(df_cm, annot=True, cmap='Blues', xticklabels =['1','2','3','4','5','6'], yticklabels =['1','2','3','4','5','6'])
# 绘制混淆矩阵热图
plt.figure(figsize=(10, 7))
sn.heatmap(df_cm, annot=True, cmap='Blues', fmt='g')
plt.xlabel('predict')
plt.ylabel('real')
plt.title('confusion matrix')
plt.show()