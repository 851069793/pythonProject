import torch
x = torch.ones(5,5)
print(x.dtype,x.device)

a = torch.zeros((3,4), out=None)# 返回大小为3*4的零矩阵
torch.zeros_like(a) # 返回与input相同size的零矩阵
b = torch.ones((5,5)) #返回大小为5*5的全为1的矩阵
torch.ones_like(b) #返回与b相同size的单位矩阵
c = torch.full((5,6), 99) #返回大小为5*6,单位值为99的矩阵
d = torch.full_like(c,98) #返回与input相同size，单位值为fill_value的矩阵
e = torch.arange(0,10,2) #返回从0到10, 单位步长为step的2的 tensor.
print(c)
print(d)
print(e)