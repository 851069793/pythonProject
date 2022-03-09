# -*- coding: utf-8 -*-
import torch
from torch.nn.modules.activation import Softmax
import torchvision
import numpy as np
import matplotlib.pyplot as plt
from torchvision import datasets, transforms

# 1. 加载MNIST手写数字数据集数据和标签
transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, ), (0.5, ))])
trainset = datasets.MNIST(root='./data', train=True,
                          download=True, transform=transform)
trainsetloader = torch.utils.data.DataLoader(
    trainset, batch_size=64, shuffle=True)

testset = datasets.MNIST(root='./data', train=True,
                         download=True, transform=transform)
testsetloader = torch.utils.data.DataLoader(
    testset, batch_size=64, shuffle=True)


# 2. 设计网络结构
first_in, first_out, second_out, out = 28*28,  128, 32, 10
model = torch.nn.Sequential(
    torch.nn.Linear(first_in, first_out),
    torch.nn.ReLU(),
    torch.nn.Linear(first_out, second_out),
    torch.nn.ReLU(),
    torch.nn.Linear(second_out, out),
    torch.nn.Softmax()
)

# 3. 设计损失函数
loss_fn = torch.nn.CrossEntropyLoss()

# 4. 设置用于自动调节神经网络参数的优化器
learning_rate = 1e-4
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# 5. 训练神经网络（重复训练10次）
for t in range(10):
    for i, one_batch in enumerate(trainsetloader, 0):
        data, label = one_batch
        # print(data.shape,label.shape)#[64,1,28,28],[64]
        data[0].view(1, 784)  # 将28x28的图片变成784的向量
        data = data.view(data.shape[0], -1)
        # print(data.shape)  # [64,784]

        # 让神经网络根据现有的参数，根据当前的输入计算一个输出
        model_output = model(data)
        # 5.1 用所设计算损失(误差)函数计算误差
        loss = loss_fn(model_output, label)
        if i % 50 == 0:
            print(t, loss)
        # 5.2 每次训练前清零之前计算的梯度(导数)
        optimizer.zero_grad()
        # 5.3 根据误差反向传播计算误差对各个权重的导数
        loss.backward()
        # 5.4 根据优化器里面的算法自动调整神经网络权重
        optimizer.step()

# 保存下训练好的模型,省得下次再重新训练
torch.save(model, './my_handwrite_recognize_model.pt')


##########现在你已经训练好了#################
# 6. 用这个神经网络解决你的问题，比如手写数字识别，输入一个图片矩阵，然后模型返回一个数字
testdataiter = iter(testsetloader)
testimages, testlabels = testdataiter.next()

plt.imshow(testimages[0].numpy().squeeze())
plt.show()
print(testimages.shape)
print(testlabels.shape)

img_vector = testimages[0].squeeze().view(1, -1)
# 模型返回的是一个1x10的矩阵，第几个元素值最大那就是表示模型认为当前图片是数字几
result_digit = model(img_vector)
print("该手写数字图片识别结果为：", result_digit,
      result_digit.max(1)[1], "标签为：", testlabels[0])

'''
布置一个小作业：请帮忙测试该网络的准确率!整个测试集有10000张照片
'''

#######显示图片代码#######
'''dataiter = iter(trainsetloader)
images, labels = dataiter.next()
import numpy as np
import matplotlib.pyplot as plt
plt.imshow(images[0].numpy().squeeze())
plt.show()
print(images.shape)
print(labels.shape)'''
