# 导入tkinter模块，并付给tk
import tkinter as tk


#定义一个Application,该类继承tk.Frame
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
    # 创建控件函数
    # 如下代码其实类似于：
    # hi_button=tk.Button(text="Hello World! （点击）", command=say_hi)
    # button.pack(side="botton")
    # quit_button = tk.Button(text="退出", fg="#ff0000", command=root.destory)
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = u"Hello World! （点击）"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text=u"退出", fg="#ff0000",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print(u"点击Hello World命令行输出该语句！")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
