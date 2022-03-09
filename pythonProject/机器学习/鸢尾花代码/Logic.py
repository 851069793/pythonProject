#机器学习算法 ，逻辑回归代码描述By Jack1101 20200130 
#算法详细简介请参考《鸢尾花数据集实现人工智能经典算法》-科技创新与应用2021年 第18期
# Sigmoid曲线:
import matplotlib.pyplot as plt
import numpy as np
def Sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

x = np.arange(-10, 10, 0.1)
h = Sigmoid(x)  # Sigmoid函数
plt.plot(x, h)
plt.axvline(0.0, color='k')
plt.axhline(y=0.5, ls='dotted', color='k')
plt.yticks([0.0,  0.5, 1.0])  # y axis label
plt.title(r'Sigmoid curve ', fontsize = 15)
plt.text(5,0.8,r'$y = \frac{1}{1+e^{-z}}$', fontsize = 18)
plt.show()


#数据分析开始：
# 导入必要的几个包
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris   
from sklearn.linear_model import LogisticRegression 
# 载入数据集,Y的值有0,1,2三种情况，每种特征50个样本
iris = load_iris()         
X = iris.data[:, [0,2]]   #获取花卉两列数据集
#X = iris.data[:, :2]   #获取花卉两列数据集
Y = iris.target
#逻辑回归模型，C=1e5表示目标函数。
lr = LogisticRegression(C=1e5)  
lr = lr.fit(X,Y)
# 将样本集花在坐标上
plt.scatter(X[:50, 0], X[:50, 1],color='red', marker='o', label='setosa') # 前50个样本的散点图
plt.scatter(X[50:100, 0], X[50:100, 1],color='blue', marker='x', label='versicolor') # 中间50个样本的散点图
plt.scatter(X[100:, 0], X[100:, 1],color='green', marker='+', label='Virginica') # 后50个样本的散点图
plt.legend(loc=2) #左上角
plt.title('Original Data')
plt.show()
# meshgrid函数生成两个网格矩阵，h表示步进长度
h = .01
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
#调用predict()函数进行预测，预测结果赋值给Z
Z = lr.predict(np.c_[xx.ravel(), yy.ravel()])
# 对预测的结果进行可视化
Z = Z.reshape(xx.shape)
plt.figure(1, figsize=(8,6))
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)
#plt.show()
# 导入样本集，绘制分类后的散点图
plt.scatter(X[:50, 0], X[:50, 1],color='red', marker='o', label='setosa') # 前50个样本的散点图
plt.scatter(X[50:100, 0], X[50:100, 1],color='blue', marker='x', label='versicolor') # 中间50个样本的散点图
plt.scatter(X[100:, 0], X[100:, 1],color='green', marker='+', label='Virginica') # 后50个样本的散点图
#输出如上图所示，经过逻辑回归后划分为三个区域，左上角部分为红色的圆点，对应setosa鸢尾花；
#右上角部分为绿色方块，对应virginica鸢尾花；中间下部分为蓝色星形，对应versicolor鸢尾花。散点图为各数据点真实的花类型，
#划分的三个区域为数据点预测的花类型，预测的分类结果与训练数据的真实结果结果基本一致，部分鸢尾花出现交叉。
#plt.xlabel('Sepal length')
plt.xlabel('Sepal length')
#plt.ylabel('Sepal width')
plt.ylabel('Petal length')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks(())
plt.yticks(())
plt.legend(loc=2) 
plt.title('Final Data')
plt.show()