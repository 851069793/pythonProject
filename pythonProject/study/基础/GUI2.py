import tkinter
from datetime import time
from tkinter import *

root = Tk()
def nowtime():
    # time1= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    tkinter.tkMessagebox.showinfo(message="time1")
    tkMessageBox.showinfo("Say Hello", "Hello World")

buttorn1 = tkinter.Button(root,text="显示当前时间",command=nowtime)
buttorn1.pack()
text1 = Text(root)
text1.pack()
root.mainloop()