def 装饰器1(func):
    def 新功能函数():
        print("这是装饰器中新加的函数功能")
        func()
    return 新功能函数

def 装饰器2(func):
    def 新功能函数():
        func()
        print("这是装饰器2")
    return 新功能函数

@装饰器1
@装饰器2
def 原函数():
    print("这是原函数")


原函数()