import threading
import time

lock = threading.Lock()

class myThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global x
        lock.acquire()
        # lock.acquire()
        for i in range(3):
            x= x+i
        time.sleep(2)
        print(x)
        lock.release()

tlist = []
for i in range(10):
    t = myThread()
    tlist.append(t)

x=0
for t in tlist:
    t.start()


