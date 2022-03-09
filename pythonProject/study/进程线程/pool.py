from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import Pool
from statistics import mean

list1 = [list(range(10)),list(range(10,20)),list(range(20,30)),list(range(30,40))]
if __name__ == '__main__':
    with Pool(5) as p:    #创建了5个进程
        print(p.map(mean,list1))



# with ThreadPoolExecutor() as pool:
#     futures = [pool.submit(mean,list1) for i in list1]
#     for future in as_completed(futures):
#         print(future.result())