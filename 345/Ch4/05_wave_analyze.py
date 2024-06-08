# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:09:38 2024

@author: MAJOR
"""

# 4-5  小波变换特征提取代码
# 利用小波分析进行特征分析
# 参数初始化
inputfile= '../data/chap4/leleccum.mat'  # 提取自Matlab的信号文件

from scipy.io import loadmat  # mat是Python专用格式，需要用loadmat读取它
mat = loadmat(inputfile)
signal = mat['leleccum'][0]

import pywt  # 导入PyWavelets
coeffs = pywt.wavedec(signal, 'bior3.7', level = 5)
# 返回结果为level+1个数字，第一个数组为逼近系数数组，后面的依次是细节系数数组
