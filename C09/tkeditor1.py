from tkinter import *
# 创建主窗口
root = Tk()
#设置窗口标题
root.title('tkeditor')
# 设置窗口大小可调性，分别表示x,y方向的可变性, 0,0表示窗口不可变
#root.resizable(0, 0)
# 设定初始窗口大小
root.geometry('450x300')
# 这里用于添加我们的代码# 这里用于添加我们的代码
menu_bar = Menu(root)
# 文件菜单项
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='文件', menu=file_menu)
# 编辑菜单项
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='编辑', menu=edit_menu)
# 视图菜单项
view_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='视图', menu=view_menu)
# 关于菜单项
about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='关于', menu=about_menu)
# 帮助菜单项
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='帮助', menu=help_menu)

root.config(menu=menu_bar)
# 消息循环
root.mainloop()
