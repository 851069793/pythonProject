#机器学习算法 ，KNN算法， 鸢尾花代码描述By Jack1101 20200130 
#算法详细简介请参考《鸢尾花数据集实现人工智能经典算法》-科技创新与应用2021年 第18期。
from sklearn.datasets import load_iris
#%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
#加载鸢尾花数据集，在Python中，该数据集自带于sklearn默认数据集中，无需单独下载。
iris_dataset = load_iris()
#打印鸢尾花的数据列格式
print("key of iris_dataset:\n{}".format(iris_dataset.keys()))


#X_train,X_test,y_train,y_test = train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=0)
X_train,X_test,y_train,y_test = train_test_split(iris.data, iris.target, test_size=0.25, random_state=33)    
# 使用train_test_split，利用随机种子random_state采样25%的数据作为测试集。
iris_dataframe = pd.DataFrame(X_train,columns=iris_dataset.feature_names)
#绘制散点图，查看鸢尾花数据集
grr = pd.plotting.scatter_matrix(iris_dataframe,c=y_train,marker='o',figsize=(10,10),hist_kwds={'bins':20},s=60,alpha=0.8,cmap='viridis')


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1) #KNN训练数据集
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
print('Test set score:\n{}'.format(np.mean(y_pred == y_test)))

#  模型预测
knn_y_predict = knn.predict(X_test)

# 预测结果画图
x_test_len = range(len(X_test))
plt.figure(figsize=(12, 9), facecolor='w')
plt.ylim(0.5,3.5)
plt.plot(x_test_len, y_test, 'ro',markersize = 6, zorder=3, label=u'real value')
plt.plot(x_test_len, knn_y_predict, 'yo', markersize = 16, zorder=1, label=u'KNNpredict value,$R^2$=%.3f' % knn.score(X_test, y_test))
plt.legend(loc = 'lower right')
plt.xlabel(u'data serial number', fontsize=18)
plt.ylabel(u'Kinds', fontsize=18)
plt.title(u'Data Classify', fontsize=20)
plt.show()