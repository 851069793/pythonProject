def demo(newitem,old_list=[]):
    old_list.append(newitem)
    return old_list


print(demo("123",[1,2,34]))
print(demo("aad",["bb",'33']))
print(demo("a"))
print(demo("999"))   #本来应该输出['999']
print(demo("新的",["新的登记反馈的减肥"]))