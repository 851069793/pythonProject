def demo(s):
    new_str = ""
    for i in range(len(s)):
        if (i + 1) % 3 == 0:
            new_str += s[i-2:i+1][::-1]
    if len(s) != len(new_str):
        new_str += s[len(new_str):][::-1]
    return new_str

old_str = "12345678"
print(demo(old_str))
