list1 = []
x = 2000
while x <= 3200:
    if x % 7 == 0 and x % 5 != 0:
        list1.append(x)
    x = x + 1

print(str(list1).strip("[]"))
