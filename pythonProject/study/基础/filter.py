list1 = [1,2,3,4,5,6,7,8]
def A(x):
    return x%2==0

print(list(filter(A,list1)))