from tkinter import *
# 创建主窗口
root = Tk()
#标签及其几何位置
Label(root, text="用户名").grid(row=0, sticky=W)
Label(root, text="密码").grid(row=1, sticky=W)
Label(root, text="邮箱").grid(row=2, sticky=W)
# 文本及其几何位置
Entry(root).grid(row=0, column=1, sticky=E)
Entry(root).grid(row=1, column=1, sticky=E)
Entry(root).grid(row=2, column=1, sticky=E)
Checkbutton(root, text='记录输入值').grid(row=3, column=1, columnspan=4, sticky='w')
Button(root, text="注册").grid(row=4, column=1, sticky=W)
# 消息循环
root.mainloop()