import multiprocessing
import random
import time


def prnum():
    for i in range(100):
        print(i**2,end="")
        time.sleep(0.02)



def prword():
    for i in range(100):
        print(random.choice("abcdefghijklmnopqrstuvwxyz"),end="")
        time.sleep(0.02)

def yuanshi():
    opentime = time.time()
    prnum()
    prword()
    endtime = time.time()
    print("\n,\n,\n")
    print(endtime-opentime)


process1 = multiprocessing.Process(target=prnum())
process2 = multiprocessing.Process(target=prword())

def processtext():
    opentime = time.time()
    process1.start()
    process2.start()
    endtime = time.time()
    print("\n,\n,\n")
    print(endtime - opentime)

processtext()
yuanshi()

