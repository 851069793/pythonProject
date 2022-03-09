#算法详细简介请参考《鸢尾花数据集实现人工智能经典算法》-科技创新与应用2021年 第18期。

#机器学习算法 ，K-Means算法， 鸢尾花代码描述By Jack1101 20200130 
#为了做效果对比，另引入层次聚类（Agnes）和密度聚类（DBSCAN）的图

import matplotlib.pyplot as plt  
import numpy as np  
from sklearn.cluster import KMeans
from sklearn import datasets 
 
iris = datasets.load_iris() 
X = iris.data[:, :4]  # #表示我们取特征空间中的4个维度
print(X.shape)
 
# 绘制数据分布图
plt.scatter(X[:, 0], X[:, 1], c="red", marker='o', label='see')  
plt.xlabel('sepal length')  
plt.ylabel('sepal width')  
plt.legend(loc=2)  
plt.title("Original Data Figure")
plt.show()  
 
estimator = KMeans(n_clusters=3)  # 构造聚类器
estimator.fit(X)  # 聚类
label_pred = estimator.labels_  # 获取聚类标签
# 绘制k-means结果
x0 = X[label_pred == 0]
x1 = X[label_pred == 1]
x2 = X[label_pred == 2]
plt.scatter(x0[:, 0], x0[:, 1], c="red", marker='o', label='label0')  
plt.scatter(x1[:, 0], x1[:, 1], c="green", marker='*', label='label1')  
plt.scatter(x2[:, 0], x2[:, 1], c="blue", marker='+', label='label2')  
plt.xlabel('sepal length')  
plt.ylabel('sepal width')  
plt.legend(loc=2)  
plt.title("KMeans Clustering")
plt.show()

#以上为K-Means聚类，是一种分散聚类。以下代码演示层次聚类(Agnes)：
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
irisdata = iris.data
from sklearn.metrics import confusion_matrix
clustering = AgglomerativeClustering(linkage='ward', n_clusters=3)
res = clustering.fit(irisdata)
print ("各个簇的样本数目：")
print (pd.Series(clustering.labels_).value_counts())
print ("聚类结果：")
print (confusion_matrix(iris.target, clustering.labels_))
 
plt.figure()
d0 = irisdata[clustering.labels_ == 0]
plt.plot(d0[:, 0], d0[:, 1], 'r.')
d1 = irisdata[clustering.labels_ == 1]
plt.plot(d1[:, 0], d1[:, 1], 'go')
d2 = irisdata[clustering.labels_ == 2]
plt.plot(d2[:, 0], d2[:, 1], 'b*')
plt.xlabel("Sepal.Length")
plt.ylabel("Sepal.Width")
plt.title("AGNES Clustering")
plt.show()

#以下展示密度聚类DBScan代码：
from  sklearn.cluster import DBSCAN
 
iris = datasets.load_iris() 
X = iris.data[:, :4]  # #表示我们只取特征空间中的4个维度
print(X.shape)
 
dbscan = DBSCAN(eps=0.4, min_samples=9)
dbscan.fit(X) 
label_pred = dbscan.labels_
 
# 绘制DBScan结果，与前两图区别很大
x0 = X[label_pred == 0]
x1 = X[label_pred == 1]
x2 = X[label_pred == 2]
plt.scatter(x0[:, 0], x0[:, 1], c="red", marker='o', label='label0')  
plt.scatter(x1[:, 0], x1[:, 1], c="green", marker='*', label='label1')  
plt.scatter(x2[:, 0], x2[:, 1], c="blue", marker='+', label='label2')  
plt.xlabel('sepal length')  
plt.ylabel('sepal width')  
plt.legend(loc=2)  
plt.title("DBSCAN Clustering")
plt.show()