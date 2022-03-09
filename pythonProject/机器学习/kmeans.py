import numpy as np
import random
from sklearn.datasets import load_iris
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.cluster import KMeans

#数据导入
def load_data():
    data = load_iris()
    x, y = data.data, data.target
    return x, y

# 随机初始化K个簇中心，X,K分别表示聚类数据集和簇中心的个数
def InitCentroids(X, K):
    n = np.size(X, 0)#样本的个数
    rands_index = np.array(random.sample(range(1, n), K))#sample()方法返回一个列表，其中从序列中随机选择指定数量的项目
    centriod = X[rands_index, :]
    print(np.size(centriod,0))
    return centriod

# 计算样本到簇的距离，对于簇分配矩阵的实现，只需要遍历每个样本点，然后计算其到簇中心的聚类，选择较近的即可：
def findClostestCentroids(X, centroid):
    idx = np.zeros((np.size(X, 0)), dtype=int)#idx先清空[样本数量]
    print(idx.shape)
    n = X.shape[0]  # n 表示样本个数
    for i in range(n):#每个样本循环计算到簇中心的距离
        subs = centroid - X[i, :]
        dimension2 = np.power(subs, 2)
        dimension_s = np.sum(dimension2, axis=1)  # 得到每个点到k个簇的距离sum of each row
        dimension_s = np.nan_to_num(dimension_s)
        idx[i] = np.where(dimension_s == dimension_s.min())[0][0]  # 选择最小距离所对应的簇编号
    return idx


'''
需要注意的是，我们在实际的编码过程中其实并不需要返回这么一个形状为n*k的分配矩阵u。
只需要将每个簇进行一个类别编号，然后对每个样本点赋予一个对应的编号即可。
因此，上述代码中返回的idx就是每个样本点距离其最近簇的簇编号。
例如idx=[0,1,2]就表示这四个样本点分别属于第0个簇、第1个簇和第2个簇。
'''

#对于簇中心矩阵的计算
# 只需要遍历K个簇，然后分别计算每个簇中所有样本点的平均中心即可：
def computeCentroids(X, idx, K):
    n, m = X.shape
    centriod = np.zeros((K, m), dtype=float)
    for k in range(K):
        index = np.where(idx == k)[0]  # 一个簇一个簇的分开来计算
        temp = X[index, :]  # ? by m # 每次先取出一个簇中的所有样本
        s = np.sum(temp, axis=0)
        centriod[k, :] = s / np.size(index)
    return centriod

#三个步骤的过程，整合
def kmeans(X, K, max_iter=200):
    centroids = InitCentroids(X, K)#随机选择
    idx = None
    for i in range(max_iter):#开始迭代
        idx = findClostestCentroids(X, centroids)#找到最近的簇
        centroids = computeCentroids(X, idx, K)##重新计算簇中心
    return idx


if __name__ == '__main__':
    x, y = load_data()#加载数据
    K = len(np.unique(y))
    y_pred = kmeans(x, K)#
    nmi = normalized_mutual_info_score(y, y_pred)#其中nmi为一种聚类评价指标，越大越好
    print("NMI by ours: ", nmi)

    model = KMeans(n_clusters=K)
    model.fit(x)
    y_pred = model.predict(x)
    nmi = normalized_mutual_info_score(y, y_pred)
    print("NMI by sklearn: ", nmi)
    