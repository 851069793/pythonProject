import torch as t
x = t.ones(2, 1, requires_grad=True)
y = x + 2
z = t.mean(t.pow(y, 2))
z.backward()
x.gard   #这是求z对x的导数，求得tensor([3.])
