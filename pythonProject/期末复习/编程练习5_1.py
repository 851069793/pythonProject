from functools import reduce
a=b=1
x=3
while x<=11:
    g=b
    b=reduce(lambda x,y:x+y,[a,b])
    a=g
    x=x+1
print(b)