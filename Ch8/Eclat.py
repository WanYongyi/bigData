# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:32:57 2024

@author: MAJOR
"""

import pandas as pd
from collections import defaultdict
from itertools import combinations

def load_data():
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

def eclat(prefix, items, min_support, freq_itemsets):
    while items:
        i, itids = items.pop()
        support = len(itids)
        if support >= min_support:
            freq_itemsets[frozenset(prefix + [i])] = support
            suffix = []
            for j, ojtids in items:
                new_tids = itids & ojtids
                if len(new_tids) >= min_support:
                    suffix.append((j, new_tids))
            eclat(prefix + [i], suffix, min_support, freq_itemsets)

def get_frequent_itemsets(transactions, min_support):
    min_support_count = min_support * len(transactions)
    item_tidsets = defaultdict(set)
    for tid, transaction in enumerate(transactions):
        for item in transaction:
            item_tidsets[item].add(tid)
    items = [(item, tidset) for item, tidset in item_tidsets.items()]
    freq_itemsets = {}
    eclat([], sorted(items, key=lambda x: len(x[1]), reverse=True), min_support_count, freq_itemsets)
    return freq_itemsets

def generate_association_rules(freq_itemsets, transactions, min_confidence):
    rules = []
    for itemset, support in freq_itemsets.items():
        if len(itemset) > 1:
            subsets = [frozenset(x) for i in range(1, len(itemset)) for x in combinations(itemset, i)]
            itemset_support = support / len(transactions)
            for antecedent in subsets:
                consequent = itemset - antecedent
                antecedent_support = freq_itemsets.get(antecedent, 0) / len(transactions)
                consequent_support = freq_itemsets.get(consequent, 0) / len(transactions)
                confidence = itemset_support / antecedent_support
                lift = confidence / consequent_support
                if confidence >= min_confidence and lift > 1:
                    rules.append((antecedent, consequent, itemset_support, confidence, lift))
    return rules

if __name__ == '__main__':
    dataSet = load_data()
    min_support = 0.02
    min_confidence = 0.35

    transactions = [set(transaction) for transaction in dataSet]
    freq_itemsets = get_frequent_itemsets(transactions, min_support)
    rules = generate_association_rules(freq_itemsets, transactions, min_confidence)

    for antecedent, consequent, support, confidence, lift in rules:
        print(f"{antecedent} --> {consequent} 支持度 {round(support, 6)} 置信度： {round(confidence, 6)} lift值为： {round(lift, 6)}")



