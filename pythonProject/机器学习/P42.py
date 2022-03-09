from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score,confusion_matrix

from prettytable import PrettyTable

import numpy as np

X=np.matrix('1 0.1;2 0.9;2 0.4;4 0.9;5 0.4;6 0.4;6 0.8;6 0.7;7 0.2;7 0.8;7 0.9;8 0.1;8 0.6;8 0.8;3 0.9;8 0.5;7 0.2;4 0.5;4 0.7;2 0.9')

y_true=np.matrix('0; 0; 0; 1; 0;0; 1; 1; 0; 1;1; 0; 1; 1; 0;1; 0; 0; 1; 1')

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
