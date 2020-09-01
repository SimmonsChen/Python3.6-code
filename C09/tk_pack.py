from tkinter import *
# 创建主窗口
root = Tk()
# 创建框架
frame = Frame(root)

# 包管理器中的标签文本
Label(frame, text="包侧面和填充的演示").pack()
#　左边，Y填充
Button(frame, text="左边，Y填充").pack(side=LEFT, fill=Y)
# 顶部，X填充
Button(frame, text="顶部，X填充").pack(side=TOP, fill=X)
# 右边，不填充
Button(frame, text="右边，不填充").pack(side=RIGHT, fill=NONE)
# 顶部，底部填充
Button(frame, text="顶部，底部填充").pack(side=TOP, fill=BOTH)

frame.pack()

# 包管理器的标签文本
Label(root, text="包扩展演示").pack()
# 不扩展
Button(root, text="不扩展").pack()
# 扩展不填充
Button(root, text="扩展不填充").pack(expand = 1)
# 填充X且扩展
Button(root, text="填充扩展").pack(fill=X, expand=1)
# 消息循环
root.mainloop()