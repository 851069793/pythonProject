# 0.引入依赖
from sklearn.datasets import load_iris  # 导入数据集iris
import numpy as np
import pandas as pd  # 科学计算和数值分析​
from sklearn.datasets import load_iris  # 这里直接引入sklearn（机器学习库）里的示例数据集：iris鸢尾花
from sklearn.model_selection import train_test_split  # 切分数据集为训练集和测试集
from sklearn.metrics import accuracy_score  # 计算分类预测的准确率
import matplotlib.pyplot as plt

#可视化
def iris_vis():
    # 载入数据集
    iris = load_iris()
    # 获取花卉两列数据集
    DD = iris.data
    X = [x[0] for x in DD]
    print(X)
    Y = [x[1] for x in DD]
    print(Y)

    #plt.scatter(X, Y, c=iris.target, marker='x')
    plt.scatter(X[:50], Y[:50], color='red',
                marker='o', label='setosa')  # 前50个样本
    plt.scatter(X[50:100], Y[50:100], color='blue',
                marker='x', label='versicolor')  # 中间50个
    plt.scatter(X[100:], Y[100:], color='green',
                marker='+', label='Virginica')  # 后50个样本
    plt.legend(loc=2)  # loc=1，2，3，4分别表示label在右上角，左上角，左下角，右下角
    plt.show()

iris_vis()

# 1.数据加载和预处理
# 类似字典：键值对（map）。可以理解为一个对象，有各种属性(type为sklearn.utils.Bunch)
# data为核心数据样本点（二维数组），即x；target值为0，1,2，为每一个样本点对应的分类（一维数组），即y
iris = load_iris()
# print(iris.data)
# print(iris.target)

# DataFrame是Python中Pandas库中的一种数据结构，它类似excel，是一种二维表
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['class'] = iris.target  # 输出结果见图2
df['class'] = df['class'].map(
    {0: iris.target_names[0], 1: iris.target_names[1], 2: iris.target_names[2]})  # 用名字代替分类里的0,1,2
df.describe()
print(df)
#dataFrame.describe(percentiles=None,include=None,exclude=None)
# 用于生成描述性统计数据，统计数据集的集中趋势，分散和行列的分布情况


#数据预处理
x = iris.data  # 二维数组，可以认为是一个矩阵 (150,4)
y = iris.target.reshape(-1, 1)  # (150,1)reshape(-1,1)将一维数组转成一个矩阵（列向量）
print(x.shape, y.shape)  # x150行4列，y150行1列
# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=35, stratify=y)  # random_state随机种子，stratify=y按照y的分布等比例分割
#print(x_train.shape, y_train.shape)  # x 105行4列，y105行1列
#print(x_test.shape, y_test.shape)  # x 45行4列，y45行1列

#print(x_test[0].reshape(1, -1).shape)  # 1行4列
#print(np.abs(x_train-x_test[0].reshape(1, -1)))#
#np.sum(np.abs(x_train-x_test[0].reshape(1, -1)),axis=1)  # 当axis=1时，数组的变化是横向的，体现出列的增加或者减少


# 2.核心算法实现
# 距离函数定义
def l1_distance(a, b):  # l1距离为曼哈顿距离去掉根号。a可以是一个矩阵,b必须为行向量
    return np.sum(np.abs(a-b), axis=1)  # axis=1表示把每一行加起来，将结果保存成一列

def l2_distance(a, b):  # l2距离为欧式距离。a可以是一个矩阵,b必须为行向量
    return np.sqrt(np.sum((a-b)**2, axis=1))  # axis=1表示把每一行加起来，将结果保存成一列


# 分类器实现
class kNN(object):  
    # 定义一个初始化方法，__init__是类的构造方法
    # 类里的参数第一个都要传self。self是类的实例，self.class才是类本身
    def __init__(self, n_neighbors=1, dist_func=l1_distance):
        self.n_neighbors = n_neighbors
        self.dist_func = dist_func

    # 训练模型方法
    # 求得训练集X的均值啊，方差啊，最大值啊，最小值,这些训练集X固有的属性。
    # 可以理解为一个训练过程
    def fit(self, x, y):
        self.x_train = x
        self.y_train = y

    # 模型预测方法
    def predict(self, x):  # 预测不要传y
        #print(self.n_neighbors,self.dist_func)#3,l1
        # 初始化预测分类数组
        # np.zeros初始化一个零数组,x.shape[0]行1列 x.shape=[45,4]
        y_pred = np.zeros((x.shape[0], 1), dtype=self.y_train.dtype)

        # 遍历输入的x数据点，取出每一个数据点的序号i和数据x_test
        # i为测试点的序号，保存到对应的预测y值中。enumerate枚举，拿出来的是元组，前面是序号，后面是值
        for i, x_test in enumerate(x):
            # x_test跟所有训练数据计算距离
            distances = self.dist_func(self.x_train, x_test)
            # 得到的距离按照由近到远排序，取出索引值
            nn_index = np.argsort(distances)
            # 选取最近的k个点，保存它们对应的分类类别
            nn_y = self.y_train[nn_index[:self.n_neighbors]
                                ].ravel()  # n个近邻对应的y值（类别）
            # 统计类别出现频率最高的那个，赋给y_pred[i]
            # bincount统计nn_y中每个数出现的次数，也是输出一个数组
            y_pred[i] = np.argmax(np.bincount(nn_y))
        return y_pred

# 3.测试
# 定义一个knn实例（指定k=3，距离度量为l1距离）
knn = kNN(n_neighbors=3)
# 训练模型
knn.fit(x_train, y_train)
# 传入测试数据做预测
y_pred = knn.predict(x_test)
# 评估：二分类一般用精确率和召回率，多分类直接用准确率即可
# 求出预测准确率
accuracy = accuracy_score(y_test, y_pred)
print("预测准确率：", accuracy)

# 定义一个knn实例（k和距离做不同的选取）
knn = kNN()
# 训练模型
knn.fit(x_train, y_train)
# 保存结果list
result_list = []  # 定义一个空数组，方便最后显示
# 针对不同的参数选取，做预测（两层循环）
for p in [1, 2]:  # 距离函数是l1还是l2
    knn.dist_func = l1_distance if p == 1 else l2_distance  # 三元表达式
    for k in range(1, 10, 2):  # 考虑不同的k取值，步长为2(二分类里要避免k为偶数)
        knn.n_neighbors = k
        y_pred = knn.predict(x_test)  # 传入测试数据做预测
        accuracy = accuracy_score(y_test, y_pred)  # 求出预测准确率
        result_list.append(
            [k, 'l1_distance' if p == 1 else 'l2_distance', accuracy])
df = pd.DataFrame(result_list, columns=['k', '距离函数', '预测准确率'])
print(df)
