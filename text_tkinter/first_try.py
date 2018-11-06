"""
    初次尝试使用tkinter进行GUI的设计
    author:Benjamin
"""
import tkinter as tk


class App:
    # Window类定义窗口组件
    def __init__(self, root):
        #
        frame = tk.Frame(root)
        frame.pack()

        self.hi = tk.Button(frame, text="say hi!", command=App.say_hi)
        self.hi.pack()

    @staticmethod
    def say_hi():
        win = tk.Tk()
        win.geometry("256x100")
        win.title("say hi")
        lable_hi = tk.Label(win, text="hi")
        lable_hi.pack()


root = tk.Tk()
root.geometry("256x100")
root.title("a choice")
window = App(root)

root.mainloop()


