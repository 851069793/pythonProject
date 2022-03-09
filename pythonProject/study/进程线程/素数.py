import threading
from time import sleep

p = input("请输入最大值")
num = iter(range(int(p)+1))
list1 =[]
lock = threading.Lock()

def 判断(x):
    if x<2:
        return False
    if x in (2,3):
        return True
    if x%2 == 0:
        return False
    for i in range(3,int(x**0.5)+1,2):
        if x%i ==0:
            return False
    return True

def worker(num,i):
    while 1:
        try:
            p=next(num)
        except:
            break
        if 判断(p):
            print("线程{0}输出:{1}".format(i,p))
            sleep(0.05)



for i in range(10):
    t = threading.Thread(target=worker,args=(num,i))
    t.start()

