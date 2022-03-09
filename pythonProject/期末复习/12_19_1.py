# 编写程序，实现输入一个整数计算给定数的阶乘的程序。
#
# 例如输入:8
#
# 则输出为:40320
from functools import reduce
8
x=int(input("请输入一个非负整数:"))
if x==0:
    print(0)
else:
    print(reduce(lambda x,y:x*y,range(1,x+1)))