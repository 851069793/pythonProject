# 用pytorch中的一些工具去实现线性回归
# 1\准备数据集
# 2\设计模型,模型计算预测值
# 3\计算损失,进行优化
# 4\写训练周期,
# 前馈算损失反馈算梯度,用梯度下降更新权重
# 在numpy计算的时候,会自动广播,扩充矩阵\

import torch

'''x_data = torch.Tensor([[1.0], [2.0], [3.0]])  # 张量 3*1
y_data = torch.Tensor([[2.0], [4.0], [6.0]])'''

x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

w = torch.Tensor([1.0])
w.requires_grad = True

def forward(x):
    y_pred = x*w
    return y_pred

def loss(y_pred, y_true):
    return (y_pred-y_true)**2 

print("predict(before)", 4, forward(4).item())

for epoch in range(100):
    for x, y in zip(x_data, y_data):
        y_pred = forward(x)
        l = loss(y_pred, y)
        l.backward()
        print('\tgrad:', x, y, y_pred,l, w.data, w.grad.item())
        w.data = w.data-0.01*w.grad.item()

        w.grad.data.zero_()#梯度清零
    print("progress:", epoch, l.item())

print("predit(after)", 4, forward(4).item())
