# -*- coding: utf-8 -*-
"""
算法详细简介请参考《鸢尾花数据集实现人工智能经典算法》-科技创新与应用2021年 第18期。

@author: ji 决策树DecisionTree
"""

from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
# 加载数据集
iris = load_iris()
# 引入决策树训练模型
clf = tree.DecisionTreeClassifier()
X = iris.data
y = iris.target
# 分割数据集
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=33)
# 开始训练
clf.fit(X_train,y_train)
# 预测
y_predict=clf.predict(X_test)
from sklearn.metrics import classification_report
#显示预测的准确性
# X : array-like, shape = (n_samples, n_features)
#        Test samples.
#    y : array-like, shape = (n_samples) or (n_samples, n_outputs)
#        True labels for X.

print(clf.score(X_test,y_test))# 输出结果为0.9111111111111111
print(classification_report(y_predict,y_test))
# 输出结果为
'''
  precision    recall  f1-score   support

          0       1.00      1.00      1.00        11
          1       1.00      0.79      0.88        19
          2       0.79      1.00      0.88        15

avg / total       0.93      0.91      0.91        45
'''
#导出为图片
from IPython.display import Image 
dot_data = tree.export_graphviz(clf, out_file=None,
feature_names=iris.feature_names, class_names=iris.target_names,filled=True, rounded=True,special_characters=True)