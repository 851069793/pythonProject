l=[('b',2),('a',1),('c',3),('d',4)]
print(sorted(l,key=lambda x:(x[1])))

m=(1,2,3,4,5,6,7,8,9,0)
print(sorted(m,key=lambda x:x%2==0))
