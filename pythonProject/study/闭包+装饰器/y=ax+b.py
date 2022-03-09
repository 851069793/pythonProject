def func1(a,b):
    def func2(x):
        print(a*x+b)
    return func2



a=func1(2,10)   #y=2x+10

a(5)     #  x=5