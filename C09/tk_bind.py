from tkinter import *
from tkinter import messagebox as tmb
# 创建主窗口
root = Tk()
# 标签包管理器
Label(root, text='点击如下框架，你能获取到你点击的x轴和y轴的位置').pack()
# 定义回调函数


def callback(event):
  # 用户弹窗显示信息
  tmb.showinfo(title='信息', message="你点击的x轴和y轴的位置："+ str(event.x)+", " + str(event.y)+"")


# 创建框架
frame = Frame(root, bg='#ff9900', width=250, height=150)
# 绑定事件，调取回调函数
frame.bind("<Button-1>", callback)
frame.pack()
# 消息循环
root.mainloop()
