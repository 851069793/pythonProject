a=[1,2,3,4,5,6,7,5,4,3,2,8,2]
a.append(999)
a.insert(0,998)
a.remove(2)
print(a.pop(2))
a.reverse()
print(a)
del a[0]
print(sorted(a))
print(sorted(a,reverse=True))
import random
import copy

b=[1,2,3,4,5,6,7]
c=copy.deepcopy(b)
del b[::2]
print(b,c)
random.shuffle(c)
print(c)


e=[1,2,3]
f=[9,8,7,6,5,4]
g=zip(e,f)  #g是一个迭代对象
# print(g)
# for i in g:
#     print(i)
print(g)

print(list(g))


