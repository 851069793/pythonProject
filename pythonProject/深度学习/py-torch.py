import numpy as np
import torch

from torch import nn
from torch.nn import functional as F
from torch import optim

import torchvision
from matplotlib import pyplot as plt


# select
# a = torch.rand(1, 3, 1)
# mask = a.ge(0.5)
# print(mask)
# print(torch.masked_select(a, mask))
# print(torch.take(a, torch.tensor(3)))

# switch dimension
# a = a.expand(3, -1, -1)  # just 1 to N
# print(a.shape)
# a.unsqueeze(1)  # insert a dimension  from index
# a = a.squeeze(2)  # delete a dimension size 1 from index
# print(a.shape)
# a = a.repeat(4, 1)  # copy the data
# print(a)
# a = a.t() # only 2d tensor , switch dimension
# print(a)
# a = a.transpose(0,1) # switch from n dimension to m dimension
# print(a)
# cond = torch.rand((2,2))
# print(cond)
# b = torch.tensor([[1,2],[3,4]])
# c = torch.tensor([[5,6],[7,8]])
# print(torch.where(cond>0.5,c,b))
def homework1():
    # 创建 5*5 数值为一的矩阵
    x = torch.ones(5, 5)
    print(x.size(), type(x))

    # 编码实现以下函数，并说明分别做了什么事情

    x = torch.zeros((2, 2), out=None)
    print(x, x.size())

    x = torch.zeros_like(input=x)
    print(x, x.size())

    x = torch.ones((2, 2), out=None)
    x = torch.ones_like(x)
    print(x, x.size())

    x = torch.full((3, 3), 10)
    print(x)
    x = torch.full_like(x, fill_value=5)
    print(x)

    x = torch.arange(start=0, end=10, step=1)
    print(x)

    # 在GPU上面完成
    DEVICE = torch.device("cuda:0")
    x = x.to(DEVICE)
    print(x)


def homework2():
    # 编码实现创建（0,100）之间均匀分布采样的随机整数，并生成(5,5)矩阵
    x = torch.randint(0, 100, (5, 5))
    print(x.size())
    print(x)

    # 编码实现返回0~1之间均匀分布采样的元素所组成的（5,5,5）的矩阵
    x = torch.rand(5, 5, 5)
    print(x.size())
    print(x)

    # 编码实现返回（5，5，5）的正态分布采样元素所组成的均值
    x = torch.randn(5, 5, 5)
    print(x.size())
    print(x)


def homework3():
    a = torch.from_numpy(np.array([[1, 2], [-3, 4]]))
    b = torch.from_numpy(np.array([[3, 4], [5, 6]]))
    x = torch.from_numpy(np.array([-1, 2, 3, -4]))
    c = torch.rand(2, 2)

    # 编码实现创建矩阵a,b，完成a，b乘法，观察结果并说明
    print(a * b)
    # 编码实现使用Torch.mm：观察结果并说
    print(torch.mm(a, b))
    # 编码实现使用torch.round将小数部分化整；
    print(torch.round(c))
    # 编码实现使用torch.clamp去掉矩阵中小于1的数；
    print(torch.clamp(x, min=1))


def homework4():
    a = torch.rand(4, 3, 28, 28)
    temp = torch.Tensor([[1, 2, 3], [5, 5, 5], [7, 8, 9], [5, 5, 5], [1, 2, 3, ], [1, 2, 4]])
    # 从最左边开始索引
    print(a[0].shape)
    print(a[0, 0].shape)
    print(a[0, 0, 2, 4])

    # 冒号索引，和python中的列表的用法差不多

    print(a.shape)
    print(a[:2].shape)
    print(a[:1, :1].shape)
    print(a[:1, 1:].shape)
    print(a[:1, -1:].shape)

    # 隔行采样，和python也一样  start:end:step

    print(a[:1, :1, 0:10:2].shape)
    print(a[:1, :1, ::2].shape)

    # 布尔索引
    print(temp[temp != 5])

    # where使用
    zeros = torch.zeros(temp.shape)
    x = torch.where(temp != 5, zeros, temp)
    print(x)


def homework5():
    # 创建一个轴的个数为4个任意维度的矩阵
    temp = torch.randint(0, 16, (5, 4))
    # 打印出元素的个数
    print(temp.shape)
    print(temp.size(1))

    # 使用view将矩阵变换为一维的
    print(temp.view(20).size())

    #  使用view将矩阵变换为一维的
    print(temp.reshape(2, 10).size())

    # 使用permute进行维度变换
    print(temp.permute(1, 0).size())


def homework6():
    temp = torch.FloatTensor(2, 3, 5, 5)
    temp2 = torch.FloatTensor(2, 3, 5, 5)
    print(temp.size())

    # 编码实现用stack进行连接，分析stack的结果以及维度并说明
    print(torch.stack((temp, temp2), dim=0))

    # 编码实现用cat进行连接，分析cat的结果以及维度，并说明
    print(torch.cat((temp, temp2), dim=0))


def homework7():
    #  编码实现创建一个维度为（20,3,32,32）的张量，类似为20张3通道的图片，执行以下操作
    img = torch.randn(20, 3, 32, 32)
    # . 编码实现获取第0张图片的数据和shape
    print(img[0].size())
    # . 编码实现获取第0张图片的数据和shape
    print(img[0, 0].size())
    # . 编码实现连续从选取两张图片
    print(img[:20:2].size())
    # 编码实现获取第3,4，15，张照片的数据，并说明shape是多少？
    index = np.array([3, 4, 15])
    print(img[index].size())
    # 使用chunk将20张图片分为5组
    a, b, c, d, e = torch.chunk(img, 5)
    print(a.size())


homework2()
