# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 13:19:40 2024

@author: MAJOR
"""

# 7-9 K-means聚类标准化后的数据

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans  # 导入kmeans算法

# 读取标准化后的数据
airline_scale = np.load('./tmp/airline_scale.npz')['arr_0']
# 结合业务分析需要聚类的数量（书上是5类）
k = 5  # 确定聚类中心数

# 构建模型，随机种子设为123
kmeans_model = KMeans(n_clusters=k, n_init=4, random_state=123)
fit_kmeans = kmeans_model.fit(airline_scale)  # 模型训练

# 查看聚类结果
kmeans_cc = kmeans_model.cluster_centers_  # 聚类中心
print('各类聚类中心为：\n', kmeans_cc)
kmeans_labels = kmeans_model.labels_  # 样本的类别标签
print('各样本的类别标签为：\n', kmeans_labels)
r1 = pd.Series(kmeans_model.labels_).value_counts()  # 统计不同类别样本的数目
print('最终每个类别的数目为：\n', r1)
# 输出聚类分群的结果
cluster_center = pd.DataFrame(kmeans_model.cluster_centers_,
                              columns=['ZL', 'ZR', 'ZF', 'ZM', 'ZC'])   # 将聚类中心放在数据框中
cluster_center.index = pd.DataFrame(kmeans_model.labels_).\
    drop_duplicates().iloc[:, 0]  # 将样本类别作为数据框索引
print(cluster_center)


# 7-10 绘制客户分群雷达图
# %matplotlib inline

# 客户分群雷达图
labels = ['ZL', 'ZR', 'ZF', 'ZM', 'ZC']
legen = ['客户群' + str(i + 1) for i in cluster_center.index]  # 客户群命名，作为雷达图的图例
lstype = ['-', '--', (0, (3, 5, 1, 5, 1, 5)), ':', '-.']
kinds = list(cluster_center.index)

centers = np.array(cluster_center)  # 将 DataFrame 转换为 numpy 数组

# 分割圆周长，并让其闭合
n = len(labels)
angle = np.linspace(0, 2 * np.pi, n, endpoint=False)
angle = np.concatenate((angle, [angle[0]]))
labels = np.concatenate((labels, [labels[0]]))  # 重复第一个标签以确保标签数目与角度数目一致

# 绘图
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, polar=True)  # 以极坐标的形式绘制图形
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 画线
for i in range(len(kinds)):
    ax.plot(angle, np.concatenate((centers[i], [centers[i][0]])), linestyle=lstype[i],
            linewidth=2, label=legen[i])
# 添加属性标签
ax.set_thetagrids(angle * 180 / np.pi, labels)
plt.title('客户特征分析雷达图')
plt.legend(legen)
plt.show()
plt.close()

'''
雷达图分析
1. 客户群3，特征C处的值最大，说明该客户群体消费越高
2. 客户群4，特征F和特征M处的值最大，R上的值最小，说明该客户群体最频繁乘机且近期有登机记录
3. 客户群1，特征R处的值最大，说明该客户群体价值低
4. 客户群2，在各各值都较小，说明是新客户群体
5. 客户群5，特征L处的值最大，说明入会时间较长，频率高，高价值用户群体
'''