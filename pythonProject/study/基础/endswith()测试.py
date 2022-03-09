import os

var = [filename for filename in os.listdir(r"E:\Documents\Pictures\桌面背景") if filename.endswith(("jpg", "txt", "png"))]
print(var)