# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:41:33 2024

@author: MAJOR
"""

import pandas as pd
import numpy as np


def loadDataSet():
    inputfile = './data/GoodsOrder.csv'
    data = pd.read_csv(inputfile, encoding='gbk')

    # 根据id对“Goods”列合并，并使用“，”将各商品隔开
    data['Goods'] = data['Goods'].apply(lambda x: ',' + x)
    data = data.groupby('id').sum().reset_index()

    # 对合并的商品列转换数据格式
    data['Goods'] = data['Goods'].apply(lambda x: [x[1:]])
    data_list = list(data['Goods'])

    # 分割商品名为每个元素
    data_translation = []
    for i in data_list:
        p = i[0].split(',')
        data_translation.append(p)

    return data_translation


def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return list(map(frozenset, C1))


def grey_relation_analysis(matrix, reference, rho=0.5):
    diff_matrix = np.abs(matrix - reference)
    min_diff = np.min(diff_matrix)
    max_diff = np.max(diff_matrix)
    grey_rel = (min_diff + rho * max_diff) / (diff_matrix + rho * max_diff)
    return grey_rel


def generate_association_rules(dataSet, minGreyRel=0.6):
    item_list = createC1(dataSet)
    data_matrix = np.array([[(1 if item.issubset(transaction) else 0) for transaction in dataSet] for item in item_list])

    association_rules = []
    for i, item1 in enumerate(item_list):
        for j, item2 in enumerate(item_list):
            if i != j:
                grey_rel = grey_relation_analysis(data_matrix[i], data_matrix[j])
                avg_grey_rel = np.mean(grey_rel)
                if avg_grey_rel >= minGreyRel:
                    association_rules.append((item1, item2, avg_grey_rel))
    return association_rules


if __name__ == '__main__':
    dataSet = loadDataSet()
    minGreyRel = 0.6
    rules = generate_association_rules(dataSet, minGreyRel)

    for rule in rules:
        item1, item2, grey_rel = rule
        print(f"{item1} --> {item2} 灰色关联度：{grey_rel:.6f}")

