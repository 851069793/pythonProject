def relist(nums):   #nums参数是一个集合
    list = []
    list2 = []
    n = len(nums)
    for a in range(1, n + 1):
        list2.append(a)
    for x in list2:
        if x not in nums:
            list.append(x)



    print(list)


relist([4, 3, 2, 7, 8, 2, 3, 1])

