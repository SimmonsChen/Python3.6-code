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
# 通过add_command()方法添加下拉菜单

file_menu.add_command(label="新建", compound='left', accelerator='Ctrl+N', underline=0)
file_menu.add_command(label="打开", compound='left', accelerator='Ctrl+O', underline=0)
file_menu.add_separator()
file_menu.add_command(label="保存", compound='left', accelerator='Ctrl+S', underline=0)
file_menu.add_command(label="另存为...", accelerator='Ctrl+Shift+S', underline=1)
file_menu.add_command(label="重命名", accelerator='Ctrl+Shift+R', underline=0)
file_menu.add_separator()
file_menu.add_command(label="关闭", accelerator='Alt+F4', underline=0)

# 编辑菜单项
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='编辑', menu=edit_menu)
edit_menu.add_command(label="返回")
edit_menu.add_command(label="重做")
edit_menu.add_command(label="剪切", accelerator="Ctrl+X")
edit_menu.add_command(label="复制", accelerator="Ctrl+C")
edit_menu.add_command(label="粘贴", accelerator="Ctrl+V")
edit_menu.add_command(label="删除", accelerator="del")
edit_menu.add_command(label="选定所有", accelerator="Ctrl+A")
edit_menu.add_command(label="查找", accelerator="Ctrl+F")

# 视图菜单项
view_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='视图', menu=view_menu)

# 关于菜单项
about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='关于', menu=about_menu)
about_menu.add_command(label="关于我")
# 帮助菜单项
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='帮助', menu=help_menu)
help_menu.add_command(label="帮助索引")
help_menu.add_command(label="许可")

root.config(menu=menu_bar)
# 消息循环
root.mainloop()