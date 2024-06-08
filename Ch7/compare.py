# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

# 生成示例数据
np.random.seed(42)
X = np.random.rand(100, 5) * 100  # 生成一个 100 x 5 的随机矩阵，模拟原始数据

# 原始数据
kmeans_original = KMeans(n_clusters=3, random_state=42)
labels_original = kmeans_original.fit_predict(X)
score_original = silhouette_score(X, labels_original)

# 标准化数据
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)
kmeans_standardized = KMeans(n_clusters=3, random_state=42)
labels_standardized = kmeans_standardized.fit_predict(X_standardized)
score_standardized = silhouette_score(X_standardized, labels_standardized)

# 归一化数据
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)
kmeans_normalized = KMeans(n_clusters=3, random_state=42)
labels_normalized = kmeans_normalized.fit_predict(X_normalized)
score_normalized = silhouette_score(X_normalized, labels_normalized)

# 主成分分析（PCA）数据
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
kmeans_pca = KMeans(n_clusters=3, random_state=42)
labels_pca = kmeans_pca.fit_predict(X_pca)
score_pca = silhouette_score(X_pca, labels_pca)

# 绘制聚类结果
def plot_clusters(X, labels, title):
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    plt.title(title)
    plt.show()

plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
plot_clusters(X_pca, labels_original, f'Original Data\nSilhouette Score: {score_original:.2f}')

plt.subplot(2, 2, 2)
plot_clusters(X_pca, labels_standardized, f'Standardized Data\nSilhouette Score: {score_standardized:.2f}')

plt.subplot(2, 2, 3)
plot_clusters(X_pca, labels_normalized, f'Normalized Data\nSilhouette Score: {score_normalized:.2f}')

plt.subplot(2, 2, 4)
plot_clusters(X_pca, labels_pca, f'PCA Data\nSilhouette Score: {score_pca:.2f}')

plt.tight_layout()
plt.show()

# 打印轮廓系数
print(f'Silhouette Scores:')
print(f'Original Data: {score_original:.2f}')
print(f'Standardized Data: {score_standardized:.2f}')
print(f'Normalized Data: {score_normalized:.2f}')
print(f'PCA Data: {score_pca:.2f}')
