import fileinput
for line in fileinput.input("测试.txt",openhook=fileinput.hook_encoded("utf-8")):
    lineno = fileinput.filelineno()
    print(lineno,line)
