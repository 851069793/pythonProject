import threading1
from time import sleep


def func1(x,y):
    for i in range(x,y):
        print(i)
        sleep(1)

t1 = threading1.Thread(target = func1, args = (0, 10))
t2 = threading1.Thread(target = func1, args = (10, 20))
t1.start()
t1.join()
t2.start()
print("t1:",t1.is_alive())
print("t2:",t2.is_alive())
