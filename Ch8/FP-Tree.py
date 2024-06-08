# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:05:39 2024

@author: MAJOR
"""

import pandas as pd
from collections import defaultdict, namedtuple


class TreeNode:
    def __init__(self, name_value, num_occurrences, parent_node):
        self.name = name_value
        self.count = num_occurrences
        self.node_link = None
        self.parent = parent_node
        self.children = {}

    def inc(self, num_occurrences):
        self.count += num_occurrences


def load_data():
    inputfile = './data/GoodsOrder.csv'
    data = pd.read_csv(inputfile, encoding='gbk')
    data['Goods'] = data['Goods'].apply(lambda x: ',' + x)
    data = data.groupby('id').sum().reset_index()
    data['Goods'] = data['Goods'].apply(lambda x: [x[1:]])
    data_list = list(data['Goods'])
    data_translation = []
    for i in data_list:
        p = i[0].split(',')
        data_translation.append(p)
    return data_translation


def create_initial_set(data_set):
    ret_dict = {}
    for trans in data_set:
        ret_dict[frozenset(trans)] = 1
    return ret_dict


def create_tree(data_set, min_support=1):
    header_table = {}
    for trans in data_set:
        for item in trans:
            header_table[item] = header_table.get(item, 0) + data_set[trans]

    for k in list(header_table.keys()):
        if header_table[k] < min_support:
            del(header_table[k])

    freq_item_set = set(header_table.keys())
    if len(freq_item_set) == 0:
        return None, None

    for k in header_table:
        header_table[k] = [header_table[k], None]

    ret_tree = TreeNode('Null Set', 1, None)
    for tran_set, count in data_set.items():
        local_d = {}
        for item in tran_set:
            if item in freq_item_set:
                local_d[item] = header_table[item][0]

        if len(local_d) > 0:
            ordered_items = [v[0] for v in sorted(
                local_d.items(), key=lambda p: p[1], reverse=True)]
            update_tree(ordered_items, ret_tree, header_table, count)
    return ret_tree, header_table


def update_tree(items, in_tree, header_table, count):
    if items[0] in in_tree.children:
        in_tree.children[items[0]].inc(count)
    else:
        in_tree.children[items[0]] = TreeNode(items[0], count, in_tree)
        if header_table[items[0]][1] is None:
            header_table[items[0]][1] = in_tree.children[items[0]]
        else:
            update_header(header_table[items[0]][1],
                          in_tree.children[items[0]])
    if len(items) > 1:
        update_tree(items[1:], in_tree.children[items[0]], header_table, count)


def update_header(node_to_test, target_node):
    while (node_to_test.node_link is not None):
        node_to_test = node_to_test.node_link
    node_to_test.node_link = target_node


def ascend_tree(leaf_node, prefix_path):
    if leaf_node.parent is not None:
        prefix_path.append(leaf_node.name)
        ascend_tree(leaf_node.parent, prefix_path)


def find_prefix_path(base_pat, tree_node):
    cond_pats = {}
    while tree_node is not None:
        prefix_path = []
        ascend_tree(tree_node, prefix_path)
        if len(prefix_path) > 1:
            cond_pats[frozenset(prefix_path[1:])] = tree_node.count
        tree_node = tree_node.node_link
    return cond_pats


def mine_tree(in_tree, header_table, min_support, pre_fix, freq_item_list):
    big_l = [v[0] for v in sorted(header_table.items(), key=lambda p: p[1][0])]
    for base_pat in big_l:
        new_freq_set = pre_fix.copy()
        new_freq_set.add(base_pat)
        freq_item_list.append(new_freq_set)
        cond_patt_bases = find_prefix_path(base_pat, header_table[base_pat][1])
        my_cond_tree, my_head = create_tree(cond_patt_bases, min_support)

        if my_head is not None:
            mine_tree(my_cond_tree, my_head, min_support,
                      new_freq_set, freq_item_list)


# 生成关联规则
def calcSupport(dataSet, itemSet):
    """计算支持度"""
    count = 0
    for trans in dataSet:
        if itemSet.issubset(trans):
            count += 1
    return count / float(len(dataSet))

def generateRules(freqItemList, dataSet, minConf=0.7):
    """生成关联规则"""
    rules = []
    for freqSet in freqItemList:
        if len(freqSet) > 1:
            H1 = [frozenset([item]) for item in freqSet]
            calcConf(freqSet, H1, dataSet, rules, minConf)
    return rules

def calcConf(freqSet, H, dataSet, ruleList, minConf=0.7):
    """置信度"""
    for conseq in H:
        conf = calcSupport(dataSet, freqSet) / calcSupport(dataSet, freqSet - conseq)
        lift = conf / calcSupport(dataSet, conseq)
        if conf >= minConf and lift > 1:
            ruleList.append((freqSet - conseq, conseq, calcSupport(dataSet, freqSet), conf, lift))
            print(freqSet - conseq, '-->', conseq, '支持度', round(calcSupport(dataSet, freqSet), 6),
                  '置信度', round(conf, 6), 'lift值', round(lift, 6))


if __name__ == '__main__':
    # 最小的情况概率为2%（即数据集中出现这种情况的数量为2%）
    min_support = 0.02
    dataSet = load_data()
    support_num = len(dataSet) * min_support
    init_set = create_initial_set(dataSet)
    my_fp_tree, my_header_tab = create_tree(init_set, support_num)

    freq_items = []
    mine_tree(my_fp_tree, my_header_tab, support_num, set([]), freq_items)
    # print(freq_items)
    
    rules = generateRules(freq_items, dataSet, minConf=0.35)
    
    
    
    
