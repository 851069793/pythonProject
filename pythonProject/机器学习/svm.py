#!/usr/bin/env python
# coding: utf-8
# python svm.py --c 0.01 --batchsize 1
# Created:  2021-10-16

import argparse

import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_blobs


def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('testSet.txt')#x1,x2,y
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([float(lineArr[0]), float(lineArr[1])])#设置x0 为1
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat


def train(X, Y, model, args):
    X = torch.FloatTensor(X)
    Y = torch.FloatTensor(Y)
    N = len(Y)  # 

    optimizer = optim.SGD(model.parameters(), lr=args.lr)

    model.train()
    for epoch in range(args.epoch):
        perm = torch.randperm(N)
        sum_loss = 0

        for i in range(0, N, args.batchsize):
            x = X[perm[i: i + args.batchsize]].to(args.device)
            y = Y[perm[i: i + args.batchsize]].to(args.device)

            optimizer.zero_grad()#
            output = model(x).squeeze()
            weight = model.weight.squeeze()

            loss = torch.mean(torch.clamp(1 - y * output, min=0))
            loss += args.c * (weight.t() @ weight) / 2.0
            # t() 转置   @是用来对tensor进行矩阵相乘的：

            loss.backward()
            optimizer.step()

            sum_loss += float(loss)

        print("Epoch: {:4d}\tloss: {}".format(epoch, sum_loss / N))
    return weight


def visualize(X, Y, model):
    W = model.weight.squeeze().detach().cpu().numpy()
    b = model.bias.squeeze().detach().cpu().numpy()

    delta = 0.001
    x = np.arange(X[:, 0].min(), X[:, 0].max(), delta)
    y = np.arange(X[:, 1].min(), X[:, 1].max(), delta)
    x, y = np.meshgrid(x, y)
    xy = list(map(np.ravel, [x, y]))

    z = (W.dot(xy) + b).reshape(x.shape)
    z[np.where(z > 1.0)] = 4
    z[np.where((z > 0.0) & (z <= 1.0))] = 3
    z[np.where((z > -1.0) & (z <= 0.0))] = 2
    z[np.where(z <= -1.0)] = 1

    plt.figure(figsize=(10, 10))
    plt.xlim([X[:, 0].min() + delta, X[:, 0].max() - delta])
    plt.ylim([X[:, 1].min() + delta, X[:, 1].max() - delta])
    plt.contourf(x, y, z, alpha=0.8, cmap="rainbow")
    plt.scatter(x=X[:, 0], y=X[:, 1], c="black", s=10)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--c", type=float, default=0.01)
    parser.add_argument("--lr", type=float, default=0.01)
    parser.add_argument("--batchsize", type=int, default=5)
    parser.add_argument("--epoch", type=int, default=100)
    parser.add_argument("--device", default="cuda", choices=["cpu", "cuda"])
    args = parser.parse_args()
    args.device = torch.device(
        args.device if torch.cuda.is_available() else "cpu")

    print(args)

    '''
    make_blobs 生成数据，返回值：
    形状为[n_samples，n_features]的X数组
    形状为[n_samples]的y数组
    
    X, Y = make_blobs(n_samples=500, centers=3, n_features=2,
                      random_state=0, cluster_std=0.4)
    print(X, Y,type(X))
    '''

    Xdata,Ydata = loadDataSet()#list
    X = np.array(Xdata)
    Y = np.array(Ydata)

    plt.scatter(X[:, 0], X[:, 1], c=Y, cmap="rainbow")
    plt.show()

    # normalization标准化数据
    X = (X - X.mean()) / X.std()  # 平均，std标准差
    Y[np.where(Y == 0)] = -1
    print(X, Y)

    model = nn.Linear(2, 1)
    model.to(args.device)

    weight = train(X, Y, model, args)

    
    visualize(X, Y, model)
