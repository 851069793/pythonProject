def test(list,num):     #给定的list集合  num数值
    no = 0    #数组标
    result = []
    for x in list:
        no_2 = 0
        if no+1<len(list):
            for a in list[no+1:]:
                if a+x == num:

                    tuple1 = (no,no+1+no_2)
                    result.append(tuple1)
                no_2=no_2+1
        no=no+1
    return result


list= [2,7,11,6,3]
num= 13
print(test(list,num))