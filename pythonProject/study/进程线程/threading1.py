import threading
def main():
    print(threading.active_count())
    print((threading.enumerate()))
    added_thread = threading.Thread(target=job1)
    added_thread.start()
    print(threading.active_count())
    print((threading.enumerate()))

def job1():
    print("新建了一个线程")

if __name__ == "__main__":
    main()
