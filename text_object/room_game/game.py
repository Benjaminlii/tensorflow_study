"""
尝试用python面向对象写一个之前Java写过的房间游戏
这是其中的Game类
author：Benjamin
"""
from text_object.room_game.room import Room


class Game:
    def __init__(self):
        kd = Room("空地")
        ty = Room("庭院")
        ld = Room("林地")
        cb = Room("城堡")
        jg = Room("酒馆")
        qjs = Room("起居室")
        lwt = Room("瞭望台")
        sf = Room("书房")
        dj = Room("地窖")

        kd.add_exit("north", ty)
        ty.add_exit("north", cb)
        ty.add_exit("east", ld)
        ld.add_exit("west", ty)
        cb.add_exit("north", lwt)
        cb.add_exit("south", ty)
        cb.add_exit("west", qjs)
        cb.add_exit("east", jg)
        cb.add_exit("up", sf)
        cb.add_exit("down", dj)
        dj.add_exit("up", cb)
        jg.add_exit("west", cb)
        qjs.add_exit("east", cb)
        sf.add_exit("down", cb)
        lwt.add_exit("south", cb)

        self.one = kd

    def print_welcome(self):
        print("特别无聊的游戏，要不是比较简单，我才不会去写这个")
        print("简单地说，就是有一个地图，键盘通过获取指令来进行人物的移动")
        print("然后，就没有然后了。。。。。。。。。")
        print("开始吧！")
        print("尝试输入‘help’来获取提示")
        print("你现在在{0}".format(self.one.get_name))
        print("你能去的方向：" + self.one.get_direction)

    def go_there(self, exit1):
        if self.one.get_direction.find(exit1) != -1:
            self.one = self.one.get_exit_room(exit1)
            print("\n我现在在{0}".format(self.one.get_name))
            print("我能去的方向：" + self.one.get_direction)
        else:
            print("what's the fuck you doing???")

    @staticmethod
    def print_help():
        print("\n你可以做的事情有：go bye help")
        print("例如：go north")


# 程序的开始
one = Game()
one.print_welcome()
while 1:
    words = input().split(" ")
    if words[0] == "help":
        one.print_help()
    elif words[0] == "bye":
        print("游戏结束")
        break
    elif words[0] == "go":
        one.go_there(words[1])
    else:
        print("what's the fuck you doing???")



