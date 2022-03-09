# 用pytorch中的一些工具去实现线性回归
# 1\准备数据集 
# 2\设计模型,模型计算预测值
# 3\计算损失,进行优化
# 4\写训练周期,
#前馈算损失反馈算梯度,用梯度下降更新权重
# 在numpy计算的时候,会自动广播,扩充矩阵\

import torch
x_data = torch.Tensor([[1.0], [2.0], [3.0]])
y_data = torch.Tensor([[2.0], [4.0], [6.0]])
# 使用minibanch,小数据集,比如现在有三个数据样本

# 线性单元,根据x和y的维度大小确定w和b的大小,但最后得到的loss值需要去求和

class LinearModel(torch.nn.Module):
    def __init__(self):
        super(LinearModel,self).__init__()
        # 必须有的一步
        self.linear=torch.nn.Linear(1,1,bias=True)
        # nn代表神经网络,其中包含组件
    #   pytorch中的一个类,linear包含了权重w和偏置b,构造对象
    #   可以去查看linear的官方文档,包含三个参数,input,output,bias=True
    #   构造函数,构造的module可以自动构建反向运算

    def forward(self,x):
        y_pred=self.linear(x)
        return y_pred
    # class中的调用,*args表示随便传递参数值
    # 设计模型,实现了

model=LinearModel()
# 把模型实例化

criterion = torch.nn.MSELoss(size_average= False)
# 使用mseloss,直接调用,两个参数,是否求均值;确定是否降维
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
# 随后进行优化模块,参数:parameters权重,(对哪些tensor进行优化)学习率lr

for epoch in range(100):
    y_pred = model(x_data)
    loss = criterion(y_pred, y_data)
    print(epoch, loss)
    optimizer.zero_grad()
    # 注意梯度归零
    loss.backward()
    optimizer.step()

# Output weight and bias
print( 'w = ', model.linear.weight.item())
print( 'b = ', model.linear.bias.item())

# Test Model
x_test = torch.Tensor([[4.0]])
y_test = model(x_test)
print( 'y_pred = ', y_test.data)