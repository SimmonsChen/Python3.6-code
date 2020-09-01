import os
from tkinter import *
from tkinter import filedialog as ft
from tkinter import messagebox as tmb
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

# 添加文本控件及滚动条控件
content_text = Text(root, wrap='word')
content_text.pack(expand='yes', fill='both')
content_text.tag_configure('active_line', background='#f1f1f1')


scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')


# 创建文件
def new_text(event=None):
    root.title("Untitled")
    global file_name
    file_name = None


# 另存为
def save_as(event=None):
    t = content_text.get("1.0", "end-1c")
    save_location = ft.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("所有文件", "*.*"), ("文本文件", "*.txt")])
    file1 = open(save_location, "w+")
    file1.write(t)
    global file_name
    file_name = save_location
    root.title('{} - {}'.format(os.path.basename(save_location), "tkeditor"))
    file1.close()

# 保存
def save(event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        t = content_text.get("1.0", "end-1c")
        file1 = open(file_name, "w+")
        file1.write(t)
    return "break"


# 打开
def open(event=None):
    input_file_name = ft.askopenfilename(defaultextension=".txt",
                                         filetypes=[("所有文件", "*.*"), ("文本文件", "*.txt")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        root.title('{} - {}'.format(os.path.basename(file_name), "tkditor"))
        content_text.delete(1.0, END)
        file = open(input_file_name, 'r')
        if file != '':
            try:
                txt = file.read()
            except:
                tmb.showwarning("Invalid", "Please select a valid file to open")
            content_text.insert(INSERT, txt)
        else:
            pass


# 剪切
def cut():
    content_text.event_generate("<<Cut>>")


# 复制
def copy():
    content_text.event_generate("<<Copy>>")


# 粘贴
def paste():
    content_text.event_generate("<<Paste>>")


# 删除
def delete():
    content_text.event_generate("<<Delete>>")


# 选择所有
def selectAll():
    content_text.event_generate("<<SelectAll>>")


#返回
def undo():
    content_text.event_generate("<<Undo>>")


#重做
def redo():
    content_text.event_generate("<<Redo>>")


# 关闭
def close():
    content_text.event_generate("<<Close>>")

# 退出
def exit():
    if tmb.askokcancel("退出?", "真的退出?"):
        root.destroy()


def highlight(interval=100):
    content_text.tag_remove("active_line", 1.0, "end")
    content_text.tag_add("active_line", "insert linestart", "insert lineend+1c")
    content_text.after(interval, toggle_highlight)


def remove_highlight():
    content_text.tag_remove("active_line", 1.0, "end")


def toggle_highlight(event=None):
    if show_highlight.get():
        highlight()
    else:
        remove_highlight()

def display_about_messagebox(event=None):
    tmb.showinfo(title="关于", message="这是一个简单的记事本，纯做演示讲解用。")


def display_help_messagebox(event=None):
    tmb.showinfo("帮助", "就这东西你还需要帮助。", icon='question')

def display_lience_messagebox(event=None):
    tmb.showinfo(title="许可", message="你想拿它干啥就干啥。")


def display_common_messagebox():
    tmb.showinfo(title='信息', message="不提供信息。")

# 文件菜单项
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='文件', menu=file_menu)
# 通过add_command()方法添加下拉菜单
file_menu.add_command(label="新建", compound='left', command=new_text,  accelerator='Ctrl+N', underline=0)
file_menu.add_command(label="打开", compound='left', command=open, accelerator='Ctrl+O', underline=0)
file_menu.add_separator()
file_menu.add_command(label="保存", compound='left', command=save, accelerator='Ctrl+S', underline=0)
file_menu.add_command(label="另存为...", command=save_as, accelerator='Ctrl+Shift+S', underline=1)
file_menu.add_separator()
file_menu.add_command(label="关闭", accelerator='Alt+F4',command=close, underline=0)
file_menu.add_command(label="退出", command=exit)

# 编辑菜单项
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='编辑', menu=edit_menu)
edit_menu.add_command(label="返回",command=undo)
edit_menu.add_command(label="重做", command=redo)
edit_menu.add_command(label="剪切", accelerator="Ctrl+X", command=cut)
edit_menu.add_command(label="复制", accelerator="Ctrl+C",command=copy)
edit_menu.add_command(label="粘贴", accelerator="Ctrl+V", command=paste)
edit_menu.add_command(label="删除", accelerator="del",command=delete)
edit_menu.add_command(label="选定所有", accelerator="Ctrl+A", command=selectAll)
edit_menu.add_command(label="查找", accelerator="Ctrl+F",command=display_common_messagebox)

# 视图菜单项
view_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='视图', menu=view_menu)
show_highlight = BooleanVar()
view_menu.add_checkbutton(label="高亮当前行", onvalue=1, offvalue=0, variable=show_highlight, command=toggle_highlight)

# 关于菜单项
about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='关于', menu=about_menu)
about_menu.add_command(label="关于我", command=display_about_messagebox)

# 帮助菜单项
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='帮助', menu=help_menu)
help_menu.add_command(label="帮助索引", command=display_help_messagebox)
help_menu.add_command(label="许可", command=display_lience_messagebox)

root.config(menu=menu_bar)
# 消息循环
root.mainloop()
