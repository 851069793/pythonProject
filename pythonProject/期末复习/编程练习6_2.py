def A(list):
    sylist = []
    no=0
    lenlist = len(list)
    for x in list:
        if no == 0 or no ==lenlist-1:
            no = no+1
            continue
        if x >= max(list[0:no]) and x<=(min(list[no:lenlist-1:1])):
            sylist.append(no)
        no = no+1


    if lenlist <=2 or len(sylist)==0:
        print(-1)
    else:
        print(sylist)


list =[21, 11, 45, 56, 9, 66, 77, 89, 78, 68, 100, 120, 111]
A(list)