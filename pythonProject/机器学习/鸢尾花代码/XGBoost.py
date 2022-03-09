#算法详细简介请参考《鸢尾花数据集实现人工智能经典算法》-科技创新与应用2021年 第18期。
import xgboost as xgb
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
data = load_iris()
# x_train, x_test, y_train, y_test = train_test_split(data['data'],data['target'],random_state=random.randint())
x_train, x_test, y_train, y_test = train_test_split(data['data'],data['target'],random_state=0)
data_train = xgb.DMatrix(x_train, label=y_train,missing = 0)
data_test = xgb.DMatrix(x_test, label=y_test, missing = 0)

params = {
    'booster': 'gbtree',
    'objective': 'multi:softmax',  # 多分类的问题
    'num_class': 3,               # 类别数，与 multisoftmax 并用
    'gamma': 0.1,                  # 用于控制是否后剪枝的参数,越大越保守，一般0.1、0.2这样子。
    'max_depth': 12,               # 构建树的深度，越大越容易过拟合
    'lambda': 2,                   # 控制模型复杂度的权重值的L2正则化项参数，参数越大，模型越不容易过拟合。
    'subsample': 0.7,              # 随机采样训练样本
    'colsample_bytree': 0.7,       # 生成树时进行的列采样
    'min_child_weight': 3,
    'silent': 1,                   # 设置成1则没有运行信息输出，最好是设置为0.
    'eta': 0.007,                  # 如同学习率
    'seed': 1000,
    'nthread': 4,                  # cpu 线程数
}
num_round = 100
bst = xgb.train(params, data_train, num_round)

# 对测试集进行预测
dtest = xgb.DMatrix(x_test)
ans = bst.predict(dtest)

# 计算准确率
cnt1 = 0
cnt2 = 0
for i in range(len(y_test)):
    if ans[i] == y_test[i]:
        cnt1 += 1
    else:
        cnt2 += 1
print("acc:",cnt1 / (cnt1 + cnt2))
# acc: 0.9736842105263158