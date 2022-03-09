# -*- coding: utf-8 -*-
"""
算法详细简介请参考《鸢尾花数据集实现人工智能经典算法》-科技创新与应用2021年 第18期

@author: jacky 20200130
"""

from sklearn import datasets 
from sklearn import model_selection
from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib import colors
# step1.加载数据
iris = datasets.load_iris()
X = iris.data   #取出前四个特征值
x=X[:,[0,2]] #在 X中取前两列作为特征（为了后期的可视化画图更加直观，故只取前两列特征值向量进行训练，指萼片长度、萼片宽度）
y = iris.target #取出标签，标签即具体是哪一种鸢尾花
# 2.将原始数据集划分成训练集和测试集
#数据集分割，30%的测试数据；random_state随机数种子，为整数使每次生成的测试数据相同，若为 None 时，每次生成的测试数据都是随机，
#       可能不一样；默认为None
x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y,random_state=1,test_size=0.3)
# 3.搭建模型，训练SVM分类器
#参数解释：
#C: float 参数 默认值为 1.0，错误项的惩罚系数。C 越大，即对分错样本的惩罚程度越大，因此在训练样本中准确率越高，但是泛化能力降低，
#   也就是对测试数据的分类准确率降低。相反，减小 C 的话，容许训练样本中有一些误分类错误样本，泛化能力强。对于训练样本带有噪声的情况，
#    一般采用后者，把训练样本集中错误分类的样本作为噪声。
# kernel: str 参数 ，算法中采用的核函数类型，默认为‘rbf’
#           linear’: 线性核函数
#           ‘poly’：多项式核函数
#           ‘rbf’：径像核函数 / 高斯核
#           ‘sigmod’:sigmod 核函数
#           ‘precomputed’: 核矩阵
#gamma: float 参数 ，核函数系数，默认为 auto，代表其值为样本特征数的倒数，即 1/n_features
#     只对‘rbf’,‘poly’,‘sigmod’有效
#decision_function_shape: 分类决策 ovo或vor或None
#       ovo 每次在所有的 T 类样本里面选择两类样本出来，不妨记为 T1 类和 T2 类，
#           把所有的输出为 T1 和 T2 的样本放在一起，把 T1 作为正例，T2 作为负例，
#           进行二元分类，得到模型参数。我们一共需要 T(T-1)/2 次分类。
#       ovr 对于第 K 类的分类决策，我们把所有第 K 类的样本作为正例，除了第 K 类
#           样本以外的所有样本都作为负例，然后在上面做二元分类，
classifier=svm.SVC(kernel='rbf',gamma=0.1,decision_function_shape='ovo',C=0.8)
#开始训练
#ravel()函数将矩阵转变成一维数组，因为y_train最开始是行数据，是竖着的
classifier.fit(x_train,y_train.ravel())
# 4.计算svm分类器的准确率
print('SVM-输出训练集的准确率为： %.2f' % classifier.score(x_train, y_train))
print('SVM-输出测试集的准确率为 %.2f' % classifier.score(x_test, y_test))

#y_hat=classifier.predict(x_train)

x1_min, x1_max = x[:, 0].min(), x[:, 0].max() # 第0列的范围
x2_min, x2_max = x[:, 1].min(), x[:, 1].max() # 第1列的范围
x1, x2 = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j] # 生成网格采样点
#grid_test = np.stack((x1.flat, x2.flat), axis=1) # 测试点
grid_test = np.dstack((x1.flat, x2.flat))[0] # 测试点
 
# 预测分类值
grid_hat = classifier.predict(grid_test) 
grid_hat = grid_hat.reshape(x1.shape) # 使之与输入的形状相同

 # 3.绘制
cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])
 
alpha=0.5

plt.pcolormesh(x1, x2, grid_hat, cmap=cm_light) # 预测值的显示
plt.plot(x[:, 0], x[:, 1], 'o', alpha=alpha, color='blue', markeredgecolor='k')
plt.scatter(x_test[:, 0], x_test[:, 1], s=120, facecolors='none', zorder=10)  # 圈中测试集样本
plt.xlabel('petal length', fontsize=13)
plt.ylabel('sepal length', fontsize=13)
plt.xlim(x1_min, x1_max)
plt.ylim(x2_min, x2_max)
plt.title('SVM', fontsize=15)
 #plt.grid()
plt.show()
