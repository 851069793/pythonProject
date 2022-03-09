s = input("请输入测试字符串：")

# 创建一个特殊列表
stack = []
   
for c in s:
    # 如果是左括号，那么添加到特殊列表中
    if c == '(' or c == '[' or c == '{':
        stack.append(c)
    # 如果是右括号的情况
    else:
        # 如果碰到右括号，但特殊列表中没有左括号，那么肯定是非法的
        if len(stack) == 0:
            print("非法")
            break
   
        # 逐个给出 c 对应的右括号 d
        if c == ')':
            d = '('
        elif c == ']':
            d = '['
        elif c == '}':
            d = '{'
   
        # 对比 d 和从特殊列表尾部弹出的元素
        if d != stack.pop():
            print("非法")
            break
else:
    if len(stack) == 0:
        print("合法")
    else:
        print("非法")
