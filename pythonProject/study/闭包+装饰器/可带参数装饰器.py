def 装饰器(func):
    def 新函数(*args,**kwargs):
        func(*args,**kwargs)
        print("这是装饰器内容")
    return 新函数



@装饰器
def 原函数():
    print("不带参原函数")


@装饰器
def 原函数2(a,b,c):
    print("带参原函数2"+str(a)+str(b)+str(c))


原函数()
原函数2(1,2,3)