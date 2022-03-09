from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score,confusion_matrix

from prettytable import PrettyTable

import numpy as np

def colicTest():
    #打开训练集和测试集
    frTrain = open('./horseColicTraining.txt'); frTest = open('./horseColicTest.txt')
    trainingSet = []; trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    return trainingSet,trainingLabels

X, y_true=colicTest()

#导入数据，并设置训练和测试数据比例为8:2

X_train, X_test, y_train, y_test = train_test_split(X, np.ravel(y_true),test_size=0.2)

reg = LogisticRegression(C=1e5, solver='lbfgs')

#训练

reg.fit(X_train,y_train)

#测试

y_pred=reg.predict(X_test)

print('test accuracy:\n',accuracy_score(y_test,y_pred))#打印模型精度

print('weights:\n', reg.coef_, '＼nbias:\n', reg.intercept_)#打印模型参数

pre=reg.predict(X)

cm = confusion_matrix(y_true, pre)

print("confusion_matrix:")#打印混淆矩阵

cm_table = PrettyTable(["","predict: 0 class", "predict: 1 class"])

cm_table.add_row(["true: 0 class",cm[0,0], cm[0,1]])

cm_table.add_row(["true: 1 class",cm[1,0], cm[1,1]])

print(cm_table)
