# # -*- coding: utf-8 -*-
# """
# Created on Tue Jun  4 15:21:12 2024
#
# @author: MAJOR
# """
#
# from __future__ import print_function
# import pandas as pd
# from apriori import *  # 导入自行编写的apriori函数
#
# inputfile = './data/menu_orders.xls'
# outputfile = './tmp/apriori_rules.xls'  # 结果文件
# data = pd.read_excel(inputfile, header=None)
#
# print('\n转换原始数据至0-1矩阵...')
#
#
# def ct(x): return pd.Series(1, index=x[pd.notnull(x)])  # 转换0-1矩阵的过渡函数
#
#
# b = map(ct, data.to_numpy())  # 用map方式执行
# data = pd.DataFrame(list(b)).fillna(0)  # 实现矩阵转换，空值用0填充
# print('\n转换完毕。')
# del b  # 删除中间变量b，节省内存
#
# support = 0.2  # 最小支持度
# confidence = 0.5  # 最小置信度
# ms = '---'  # 连接符，默认'---'，用来区分不同元素，如A---B。需要保证原始表格中不含有该字符
#
#
# # 修改 find_rule 函数中的代码以使用 pandas.concat
# def find_rule(data, support, confidence, ms):
#     import pandas as pd
#     # 定义连接符
#     ms = '---'
#     results = []
#
#     # 支持度计算
#     support_series = 1.0 * data.sum() / len(data)
#     column = list(support_series[support_series > support].index)
#     k = 0
#
#     while len(column) > 1:
#         k = k + 1
#         print(f'\n正在进行第{k}次搜索...')
#         column = pd.DataFrame(column)
#         column_len = len(column)
#         index_list = []
#
#         for i in range(column_len):
#             for j in range(i + 1, column_len):
#                 index_list.append(pd.concat([column.iloc[i, :], column.iloc[j, :]]).reset_index(drop=True))
#
#         index_list = pd.DataFrame(index_list)
#         index_list = index_list.drop_duplicates()
#
#         # 用pandas.concat替换append
#         column = index_list.apply(lambda x: ','.join(sorted(set(x.dropna()))), axis=1).drop_duplicates().reset_index(
#             drop=True)
#
#         df_list = []
#         for i in range(len(data)):
#             row_sum = []
#             for item in column:
#                 item_list = list(item.split(','))
#                 row_sum.append(data.loc[i, item_list].sum())
#             df_list.append(row_sum)
#
#         df = pd.DataFrame(df_list, columns=column)
#
#         support_series_2 = 1.0 * df.sum() / len(data)
#         column = list(support_series_2[support_series_2 > support].index)
#         support_series = pd.concat([support_series, support_series_2])
#         support_series = support_series.groupby(support_series.index).sum()  # 去重
#
#         # 置信度计算
#         column2 = pd.Series(column).apply(lambda x: x.split(','))
#         d = list(column2.apply(lambda x: (x, support_series[','.join(x)])))
#
#         for i in range(len(d)):
#             for j in range(i + 1, len(d)):
#                 key = ','.join(sorted(set(d[i][0]).union(d[j][0])))
#                 if key in support_series:
#                     confidence_value = support_series[key] / support_series[','.join(d[i][0])]
#                     if confidence_value > confidence:
#                         results.append(
#                             [','.join(d[i][0]), ','.join(d[j][0]), support_series[','.join(d[i][0])], confidence_value])
#
#     result = pd.DataFrame(results, columns=['前项', '后项', '支持度', '置信度'])
#     return result
#
#
# find_rule(data, support, confidence, ms).to_excel(outputfile)  # 保存结果

from __future__ import print_function
import pandas as pd
from apriori import *  # 导入自行编写的apriori函数

inputfile = './data/menu_orders.xls'
outputfile = './tmp/apriori_rules.xls'  # 结果文件
data = pd.read_excel(inputfile, header=None)

print('\n转换原始数据至0-1矩阵...')
def ct(x): return pd.Series(1, index=x[pd.notnull(x)])  # 转换0-1矩阵的过渡函数


b = map(ct, data.to_numpy())  # 用map方式执行
data = pd.DataFrame(list(b)).fillna(0)  # 实现矩阵转换，空值用0填充
print('\n转换完毕。')
del b  # 删除中间变量b，节省内存

support = 0.2  # 最小支持度
confidence = 0.5  # 最小置信度
ms = '---'  # 连接符，默认'--'，用来区分不同元素，如A--B。需要保证原始表格中不含有该字符

find_rule(data, support, confidence, ms).to_excel(outputfile)  # 保存结果
