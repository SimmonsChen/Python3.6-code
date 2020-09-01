from tkinter import *
# 创建主窗口
root = Tk()
# 绝对位置
Button(root, text="绝对位置").place(x=20, y=10)
# 相对位置
Button(root, text="相对位置").place(relx=0.8, rely=0.2, relwidth=0.5, width=10, anchor=NE)
# 消息循环
root.mainloop()
